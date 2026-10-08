#!/usr/bin/env python3
"""Fill outcome fields on matured judgment-ledger rows and write the scorecard.

Does not edit routing.jsonl, theses.json, portfolio holdings, or regime.one.
Unmatured horizons stay pending. Missing prices stay null.

  python3 scripts/score_ledger.py
  python3 scripts/score_ledger.py --asof 2026-11-15
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

from ledger_common import (
    HORIZONS,
    LEDGER_PATH,
    SCORECARD_PATH,
    SUMMARY_PATH,
    build_scorecard,
    endpoint_for,
    eval_price_break,
    fred_series,
    load_thesis_index,
    naver_daily,
    read_jsonl,
    score_horizon,
    summarize,
    write_jsonl,
    yyyymmdd,
)


def series_for(row, start, end):
    ref = row.get("ref") or {}
    kind = None
    code = ref.get("naver_code")
    market = row.get("market")
    # Kind is not stored on older rows; infer from market + code shape.
    if row.get("market") == "KR" and code and code.isdigit():
        kind = "domestic/item"
    elif row.get("market") == "JP" or (code and "." in code and code.endswith(".T")):
        kind = "foreign/item"
    elif code:
        kind = "foreign/item"
    if not kind or not code:
        return []
    try:
        return naver_daily(kind, code, start, end)
    except Exception:
        return []


def bench_series(row, start, end):
    bench = row.get("benchmark") or {}
    kind = bench.get("kind")
    code = bench.get("naver_code")
    if not kind or not code:
        return []
    try:
        return naver_daily(kind, code, start, end)
    except Exception:
        return []


def macro_series(metric, start_iso, end_iso):
    series_id = metric.split(":", 1)[1]
    try:
        points = fred_series(series_id)
    except Exception:
        return []
    start, end = start_iso, end_iso
    out = []
    for date, value in points:
        if value is None or date < start or date > end:
            continue
        out.append((date.replace("-", ""), value))
    return out


def score_rows(rows, today, fetch=True):
    start = "20260901"
    end = yyyymmdd(today)
    for row in rows:
        ref = row.get("ref") or {}
        ref_asof = ref.get("asof")
        horizons = {}
        need_fetch = fetch and ref_asof and any(today >= _due(ref_asof, days) for _, days in HORIZONS)
        stock = bench = []
        if need_fetch and row.get("score_mode") == "excess":
            stock = series_for(row, start, end)
            bench = bench_series(row, start, end)
        for label, days in HORIZONS:
            if not ref_asof:
                horizons[label] = {
                    "due": None, "status": "unverified", "ret": None, "bench_ret": None,
                    "excess": None, "px_asof": None, "bench_asof": None, "verdict": "unverified",
                }
                continue
            horizons[label] = score_horizon(
                row.get("stance"), row.get("score_mode"), ref.get("price"),
                stock, bench, ref_asof, days, today,
            )
        break_results = []
        for cond in row.get("breaks_if") or []:
            series = []
            if fetch and cond.get("check") == "price":
                series = series_for(row, start, end)
                # close_on_or_before expects YYYYMMDD dates; series_for already does.
            elif fetch and cond.get("check") == "macro":
                series = macro_series(cond.get("metric") or "", ref_asof or "1900-01-01", today)
            item = eval_price_break(cond, series, today)
            item["text"] = cond.get("text")
            item["check"] = cond.get("check")
            break_results.append(item)
            if item["status"] == "fired":
                for horizon in horizons.values():
                    if horizon["status"] == "scored":
                        horizon["verdict"] = "invalidated"
                        horizon["invalidated_by"] = cond.get("text")
        row["scores"] = {
            "scored_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "asof": today,
            "price_endpoint": endpoint_for(
                "foreign/item" if row.get("market") != "KR" else "domestic/item",
                (row.get("ref") or {}).get("naver_code") or "",
            ),
            "horizons": horizons,
            "breaks_if": break_results,
        }
    return rows


def _due(ref_asof, days):
    from ledger_common import add_days
    return add_days(ref_asof, days)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Score matured judgment-ledger rows")
    ap.add_argument("--ledger", default=LEDGER_PATH)
    ap.add_argument("--asof", default=datetime.now(timezone.utc).date().isoformat())
    ap.add_argument("--no-fetch", action="store_true", help="do not call Naver or FRED")
    args = ap.parse_args(argv)
    rows = read_jsonl(args.ledger)
    rows = score_rows(rows, args.asof, fetch=not args.no_fetch)
    write_jsonl(args.ledger, rows)
    card = build_scorecard(rows, load_thesis_index())
    summary = summarize(rows, card)
    summary["asof"] = args.asof
    summary["note"] = (
        "적중률 분모는 hit+miss 만이다. 중립은 no-call, 헤지와 CDS 는 manual, "
        "호라이즌 전은 pending. 가격을 만들지 않는다."
    )
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=1)
        f.write("\n")
    with open(SCORECARD_PATH, "w", encoding="utf-8") as f:
        json.dump({"asof": args.asof, "warn_at_confirm_streak": 5, "theses": card}, f, ensure_ascii=False, indent=1)
        f.write("\n")
    pending = sum(1 for r in rows if (r["scores"]["horizons"]["30d"]["status"] == "pending"))
    print(f"scored {len(rows)} rows · 30d pending {pending} · warnings {summary['priced_in_warning_n']}")
    print(f"wrote {args.ledger} {SUMMARY_PATH} {SCORECARD_PATH}")


if __name__ == "__main__":
    main()
