#!/usr/bin/env python3
"""자동 수집 — 판단 없이 받아서 intake/collected.jsonl 에 한 줄, intake/files/ 에 스냅샷.

매일 워크플로(update-prices.yml)가 부른다. 사람이 안 붙여 넣어도 정보가 들어오게 하는 것이
목적이며, 라우팅(등급·테제 착지)은 하지 않는다 — 그것은 brain/routing.jsonl 의 일이다.

수집원 두 개(시범 · 2026-09-13):
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
    for t in targets:
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
    print(f"[collect] {day} · {written}건 기록" + (" (dry-run)" if dry else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
