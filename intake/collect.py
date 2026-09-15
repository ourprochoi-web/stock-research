#!/usr/bin/env python3
"""자동 수집 — 판단 없이 받아서 intake/collected.jsonl 에 한 줄, intake/files/ 에 스냅샷.

매일 워크플로(update-prices.yml)가 부른다. 사람이 안 붙여 넣어도 정보가 들어오게 하는 것이
목적이며, 라우팅(등급·테제 착지)은 하지 않는다 — 그것은 brain/routing.jsonl 의 일이다.

수집원 (2026-09-13 시범 → 2026-09-15 v2: 매크로·수급·breadth 추가):
  macro    FRED(10Y·2Y·30Y·BEI·WTI·브렌트·Henry Hub·VIX) + 네이버(KOSPI·KOSDAQ 종가·투자자별·VIX·S&P·NASDAQ)
           + prices.json 로 추적 종목 breadth(상승/하락 수·중앙값) → intake/files/macro/{date}.json · 한 줄
           ⚠ 네이버 국내 closePrice 는 2026-09-14부터 20:00 애프터마켓가다(session 필드에 기록)
  soonsal  일일 브리핑 soonsal.com/newsletters/{YYYY}/{MMDD}.html — 매일 11~12시 KST 발행 · 2차 요약(②~③)
  tsmc     월별 매출 investor.tsmc.com/english/monthly-revenue/{YYYY} — 월 10일경 갱신 · ① 등급
실패(차단·404)도 status 와 host 를 남긴다 — 「못 한다」에는 시도 기록이 붙어야 한다(§W5).
용법: collect.py [--dry-run] [--date YYYY-MM-DD]
"""
import hashlib
import io
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
FILES = os.path.join(ROOT, "intake", "files")
UA = "ourprochoi Research (kenchoi@keywestaim.com)"


def kst_today():
    return datetime.now(timezone(timedelta(hours=9))).date()


def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001 — 실패 사유를 기록하는 것이 목적
        return 0, str(e).encode()


def existing_ids_and_hashes():
    ids, hashes = set(), set()
    if os.path.exists(LOG):
        for ln in io.open(LOG, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                ids.add(d["id"])
                if d.get("sha256"):
                    hashes.add(d["sha256"])
    return ids, hashes


def next_id(ids, day):
    n = 1
    while f"c-{day:%Y%m%d}-{n:02d}" in ids:
        n += 1
    return f"c-{day:%Y%m%d}-{n:02d}"


# ═══ v2 (2026-09-15) — 매크로·수급·breadth 스냅샷. 판단 없음. 값의 정본은 이 스냅샷이고 brain/facts.json#macro 가 인용한다.
FRED = {"DGS10": "us10y", "DGS2": "us2y", "DGS30": "us30y", "T10YIE": "bei10", "DCOILWTICO": "wti",
        "DCOILBRENTEU": "brent", "DHHNGSP": "henry_hub", "VIXCLS": "vix_close", "DTWEXBGS": "dxy_broad"}
NAVER_IDX = {"KOSPI": "https://m.stock.naver.com/api/index/KOSPI/basic", "KOSDAQ": "https://m.stock.naver.com/api/index/KOSDAQ/basic"}
NAVER_WORLD = {"sp500": ".INX", "nasdaq": ".IXIC", "vix": ".VIX", "sox": ".SOX"}


def fetch_json(url, ua="Mozilla/5.0", timeout=15):
    st, body = fetch_ua(url, ua, timeout)
    if st != 200 or not body:
        return None, st
    try:
        return json.loads(body.decode("utf-8", "ignore")), st
    except ValueError:
        return None, st


def fetch_ua(url, ua, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:  # noqa: BLE001
        return 0, str(e).encode()


def collect_macro(day):
    """FRED + 네이버 지수·투자자 + breadth. 실패는 errors 에 host/path/status 로 남긴다(§W5)."""
    out = {"asof_run": datetime.now(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST"), "fred": {}, "naver": {}, "breadth": {}, "errors": []}
    for sid, key in FRED.items():
        st, body = fetch_ua(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", UA, 20)
        if st != 200 or not body:
            out["errors"].append({"host": "fred.stlouisfed.org", "path": f"fredgraph.csv?id={sid}", "status": st}); continue
        # 2026-09-15: 빈 값('' 또는 '.')이 섞인 계열(RRPONTSYD 등)에서 float('') 로 죽었다 → 값 있는 행만
        rows = []
        for ln in body.decode("utf-8", "ignore").strip().split("\n")[1:]:
            parts = ln.split(",")
            if len(parts) >= 2 and parts[1] not in ("", "."):
                try:
                    rows.append((parts[0], float(parts[1])))
                except ValueError:
                    continue
        if rows:
            last = rows[-1]
            out["fred"][key] = {"date": last[0], "value": last[1], "series": sid,
                                "w1": rows[-6][1] if len(rows) > 6 else None, "m1": rows[-22][1] if len(rows) > 22 else None}
    for name, url in NAVER_IDX.items():
        d, st = fetch_json(url)
        if not d:
            out["errors"].append({"host": "m.stock.naver.com", "path": url.split("naver.com", 1)[1], "status": st}); continue
        out["naver"][name] = {"close": d.get("closePrice"), "chg_pct": d.get("fluctuationsRatio"), "traded_at": d.get("localTradedAt"),
                              "session": (d.get("overMarketPriceInfo") or {}).get("tradingSessionType") or d.get("tradingSessionType") or "REGULAR?"}
    d, st = fetch_json("https://m.stock.naver.com/api/index/KOSPI/trend?pageSize=5")
    if d:
        out["naver"]["kospi_investors_억"] = {k: d.get(k) for k in ("bizdate", "personalValue", "foreignValue", "institutionalValue")}
    else:
        out["errors"].append({"host": "m.stock.naver.com", "path": "/api/index/KOSPI/trend", "status": st})
    for name, sym in NAVER_WORLD.items():
        d, st = fetch_json(f"https://api.stock.naver.com/index/{sym}/basic")
        if d:
            out["naver"][name] = {"close": d.get("closePrice"), "chg_pct": d.get("fluctuationsRatio"), "traded_at": d.get("localTradedAt"), "status": d.get("marketStatus")}
        else:
            out["errors"].append({"host": "api.stock.naver.com", "path": f"/index/{sym}/basic", "status": st})
    d, st = fetch_json("https://m.stock.naver.com/api/stock/000660/basic")
    if d:
        o = d.get("overMarketPriceInfo") or {}
        out["naver"]["price_definition_probe"] = {"code": "000660", "closePrice": d.get("closePrice"), "traded_at": d.get("localTradedAt"),
                                                   "session": o.get("tradingSessionType"), "over_status": o.get("overMarketStatus")}
    # breadth — 오늘 prices.json(봇이 직전에 갱신) vs 직전 커밋의 prices.json
    try:
        import subprocess
        cur = json.load(io.open(os.path.join(ROOT, "portfolio", "data", "prices.json"), encoding="utf-8"))
        prev = json.loads(subprocess.run(["git", "show", "HEAD:portfolio/data/prices.json"], capture_output=True, text=True, cwd=ROOT).stdout)
        mv = []
        for n, p in cur["prices"].items():
            q = prev["prices"].get(n)
            if p and q and cur.get("updated") != prev.get("updated"):
                mv.append((n, (p / q - 1) * 100))
        if mv:
            mv.sort(key=lambda x: x[1])
            vals = [c for _, c in mv]
            out["breadth"] = {"asof": cur.get("updated"), "prev": prev.get("updated"), "n": len(mv), "up": sum(1 for c in vals if c > 0),
                              "down": sum(1 for c in vals if c < 0), "median_pct": round(sorted(vals)[len(vals) // 2], 2),
                              "leaders": [f"{n} {c:+.1f}" for n, c in mv[-6:][::-1]], "laggards": [f"{n} {c:+.1f}" for n, c in mv[:6]],
                              "price_definition": cur.get("updatedTime")}
        else:
            out["breadth"] = {"note": "prices.json 미갱신(같은 updated) — breadth 계산 안 함"}
    except Exception as e:  # noqa: BLE001
        out["errors"].append({"host": "local", "path": "prices.json breadth", "status": str(e)[:80]})
    return out


def collect_macro_v3(day, out):
    """스카우트(2026-09-15)로 확보한 소스 — collect_sources.py 를 쓴다. 실패는 errors 에."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("cs", os.path.join(ROOT, "intake", "collect_sources.py"))
    cs = importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)
    ymd = f"{day:%Y%m%d}"
    def tryit(key, fn, *a, **k):
        try:
            out.setdefault("v3", {})[key] = fn(*a, **k)
        except Exception as e:  # noqa: BLE001
            out["errors"].append({"host": key, "path": str(getattr(e, "url", ""))[:80], "status": str(getattr(e, "status", e))[:80]})
    tryit("kospi_flows_daum", cs.daum_index_investor_days, "KOSPI", 1, 5)
    tryit("kosdaq_flows_daum", cs.daum_index_investor_days, "KOSDAQ", 1, 5)
    tryit("kospi_investor_detail", cs.naver_investor_deal_trend_day, "01", ymd, 1)
    tryit("breadth_kospi", cs.naver_breadth, "KOSPI")
    tryit("breadth_kosdaq", cs.naver_breadth, "KOSDAQ")
    tryit("energy_settle", lambda: {c: cs.naver_marketindex_prices("energy", c, 3) for c in ("CLcv1", "LCOcv1", "DCBc1", "NGcv1")})
    tryit("dxy", cs.naver_marketindex_prices, "exchange", ".DXY", 3)
    tryit("yields", lambda: {c: cs.naver_marketindex_prices("bond", c, 3) for c in ("US2YT=RR", "US10YT=RR", "US30YT=RR", "KR10YT=RR")})
    tryit("ttf_yahoo", cs.yahoo_chart, "TTF=F", "5d", "1d")
    tryit("cnn_fear_greed", cs.cnn_fear_greed)
    tryit("cboe_put_call", cs.cboe_put_call, (day - timedelta(days=1)).isoformat())
    tryit("leverage_etf_aum", lambda: {c: cs.naver_etf_basic(c) for c in ("0193T0", "0195S0", "0193W0", "0195R0")})
    tryit("csop_7709", cs.naver_world_stock_basic, "7709.HK")
    tryit("cftc_ng", cs.cftc_cot_managed_money, "023651", 2)
    tryit("cftc_wti", cs.cftc_cot_managed_money, "067651", 2)
    tryit("skh_regular_close", cs.krx_regular_close, "000660", ymd)
    return out


def macro_record(day, ids, dry):
    if os.path.exists(LOG):
        lines = [ln for ln in io.open(LOG, encoding="utf-8") if ln.strip()]
        ok = [ln for ln in lines if json.loads(ln).get("kind") == "매크로" and json.loads(ln).get("date") == f"{day:%Y-%m-%d}" and json.loads(ln).get("status") == "ok"]
        if ok:
            return 0
        # 같은 날 실패 기록은 성공 시 교체한다
        kept = [ln for ln in lines if not (json.loads(ln).get("kind") == "매크로" and json.loads(ln).get("date") == f"{day:%Y-%m-%d}" and json.loads(ln).get("status") == "error")]
        if len(kept) != len(lines) and not dry:
            io.open(LOG, "w", encoding="utf-8").write("".join(kept))
            for ln in lines:
                if ln not in kept:
                    ids.discard(json.loads(ln)["id"])
    snap = collect_macro(day)
    try:
        collect_macro_v3(day, snap)
    except Exception as e:  # noqa: BLE001
        snap["errors"].append({"host": "collect_macro_v3", "path": "", "status": str(e)[:80]})
    rel = f"macro/{day:%Y-%m-%d}.json"
    fr = snap["fred"]; nv = snap["naver"]; br = snap.get("breadth", {})
    def v(k, src=fr):
        x = src.get(k) or {}
        return x.get("value") if src is fr else x.get("close")
    subject = (f"매크로 스냅샷 {day:%Y-%m-%d} — 10Y {v('us10y')} · 30Y {v('us30y')} · 브렌트 {v('brent')} · HH {v('henry_hub')} · VIX {v('vix', nv)} · "
               f"코스피 {v('KOSPI', nv)}({(nv.get('KOSPI') or {}).get('chg_pct')}% · {(nv.get('KOSPI') or {}).get('session')}) · "
               f"외국인 {(nv.get('kospi_investors_억') or {}).get('foreignValue')}억 · breadth {br.get('up')}/{br.get('n')} 상승")
    rec = {"id": next_id(ids, day), "date": f"{day:%Y-%m-%d}", "kind": "매크로", "host": "fred.stlouisfed.org · m.stock.naver.com · api.stock.naver.com",
           "path": "collect.py macro", "subject": subject, "grade_hint": "①(FRED·거래소) · breadth 는 prices.json 파생",
           "status": "ok" if (fr or nv) else "blocked", "file": "intake/files/" + rel, "routed": False, "auto": True,
           "note": (f"실패 {len(snap['errors'])}건: " + "; ".join(f"{e['host']}{e['path']} {e['status']}" for e in snap["errors"][:4])) if snap["errors"] else ""}
    if dry:
        print("[dry]", json.dumps(rec, ensure_ascii=False)[:600])
    else:
        path = os.path.join(FILES, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        io.open(path, "w", encoding="utf-8").write(json.dumps(snap, ensure_ascii=False, indent=1))
        io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
    ids.add(rec["id"])
    return 1


def main(argv):
    dry = "--dry-run" in argv
    day = kst_today()
    if "--date" in argv:
        day = datetime.strptime(argv[argv.index("--date") + 1], "%Y-%m-%d").date()
    ids, hashes = existing_ids_and_hashes()
    targets = [
        dict(kind="뉴스레터", key="soonsal", host="soonsal.com",
             url=f"https://soonsal.com/newsletters/{day:%Y}/{day:%m%d}.html",
             subject=f"일일 브리핑 {day:%Y-%m-%d}", grade_hint="②~③(2차 요약 — 항목마다 등급을 따로 매긴다)",
             file=f"soonsal/{day:%Y}/{day:%m%d}.html", monthly=False),
        dict(kind="월지표", key="tsmc", host="investor.tsmc.com",
             url=f"https://investor.tsmc.com/english/monthly-revenue/{day:%Y}",
             subject=f"TSMC 월별 매출 페이지 {day:%Y}", grade_hint="①(회사 공시 · NT$ · 가이던스는 US$라 환율 가정 대조 필요)",
             file=f"tsmc/monthly-revenue-{day:%Y}.html", monthly=True),
    ]
    written = 0
    # 같은 날 같은 host 의 실패 기록이 이미 있으면 다시 적지 않는다(2026-09-15 — 수동 재실행 시 중복 방지)
    seen_today = set()
    if os.path.exists(LOG):
        for ln in io.open(LOG, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                if d.get("date") == f"{day:%Y-%m-%d}":
                    seen_today.add((d.get("host"), d.get("kind")))
    for t in targets:
        if (t["host"], t["kind"]) in seen_today:
            continue
        status, body = fetch(t["url"])
        rec = {"id": next_id(ids, day), "date": f"{day:%Y-%m-%d}", "kind": t["kind"], "host": t["host"],
               "path": t["url"].split(t["host"], 1)[1], "subject": t["subject"], "grade_hint": t["grade_hint"],
               "status": "ok" if status == 200 and body else ("blocked" if status in (0, 403, 407) else str(status)),
               "file": None, "routed": False, "auto": True}
        if rec["status"] == "ok":
            h = hashlib.sha256(body).hexdigest()
            if h in hashes:  # 같은 내용(월지표가 안 바뀐 날) — 줄을 늘리지 않는다
                continue
            rec["sha256"] = h
            rec["bytes"] = len(body)
            rec["file"] = "intake/files/" + t["file"]
            if not dry:
                path = os.path.join(FILES, t["file"])
                os.makedirs(os.path.dirname(path), exist_ok=True)
                io.open(path, "wb").write(body)
        else:
            rec["note"] = f"HTTP {status}" if status else body.decode(errors="ignore")[:160]
            if t["monthly"] and status == 404:
                continue  # 연도 페이지가 아직 없을 때만 조용히 넘어간다
        ids.add(rec["id"])
        if dry:
            print("[dry]", json.dumps(rec, ensure_ascii=False))
        else:
            io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        written += 1
    if "--no-macro" not in argv:
        try:
            written += macro_record(day, ids, dry)
        except Exception as e:  # noqa: BLE001
            # 2026-09-15: 봇에서 실패하면 Actions 로그를 못 보므로 트레이스백을 collected.jsonl 에 남긴다(§W5)
            import traceback
            tb = traceback.format_exc()[-600:]
            print(f"[collect] ⚠ macro 실패 — {e}")
            rec = {"id": next_id(ids, day), "date": f"{day:%Y-%m-%d}", "kind": "매크로", "host": "collect.py", "path": "macro_record",
                   "subject": f"매크로 스냅샷 {day:%Y-%m-%d} 실패", "status": "error", "file": None, "routed": False, "auto": True, "note": tb}
            if not dry:
                io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"[collect] {day} · {written}건 기록" + (" (dry-run)" if dry else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
