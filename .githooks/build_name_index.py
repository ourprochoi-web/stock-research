#!/usr/bin/env python3
"""종목명·키워드 → 테제/엔티티/facts 색인 (docs/name_index.md · docs/name_index.json).

CLAUDE.md §H 의 기준을 통과하는 이유 — 새 데이터를 만들지 않는다. brain 세 파일과
추적 목록(update_prices.py)에 이미 있는 것을 <파생>할 뿐이고, pre-commit 이 brain 이
바뀔 때마다 다시 만든다. 용도는 둘이다.
  ① 라우팅할 때 「이 이름이 어느 테제에 걸리나」를 grep 대신 표로 본다(2026-09-17 구조 개선 B).
  ② 봇이 뉴스레터를 수집할 때 본문에서 이름을 찾아 후보 테제 id 를 intake 에 붙인다(candidates).
정본은 언제나 brain/*.json 이다.
"""
import io
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "portfolio", "data"))
OUT_MD = os.path.join(ROOT, "docs", "name_index.md")
OUT_JS = os.path.join(ROOT, "docs", "name_index.json")

# 짧거나 흔한 이름은 본문 매칭에서 오탐이 많다 — 색인에는 두되 자동 후보(candidates)에서는 뺀다
AMBIGUOUS = {"두산", "LS", "풍산", "에스피지", "DI", "YC", "S", "NET", "ON", "FN"}
ALIAS = {  # 본문에 다르게 적히는 이름 → 추적 이름
    "블룸에너지": "Bloom Energy", "엔비디아": "NVIDIA", "브로드컴": "Broadcom",
    "마이크론": "Micron", "하이닉스": "SK하이닉스", "삼전": "삼성전자", "로빈후드": "Robinhood",
    "코인베이스": "Coinbase", "팔란티어": "Palantir", "테슬라": "Tesla", "알파벳": "Alphabet", 
    "아마존": "Amazon", "마이크로소프트": "Microsoft", "인텔": "Intel", "TSMC": "TSMC ADR",
    "셈텍": "Semtech", "크레도": "Credo", "마벨": "Marvell", "루멘텀": "Lumentum", "코히런트": "Coherent",
    "플루언스": "Fluence Energy", "제너락": "Generac", "GE버노바": "GE Vernova", "GE 버노바": "GE Vernova",
    "현중": "HD현대중공업", "효중": "효성중공업", "넥스원": "LIG디펜스앤에어로스페이스", "LIG넥스원": "LIG디펜스앤에어로스페이스",
    "에어로": "한화에어로스페이스", "삼바": "삼성바이오로직스", "SDI": "삼성SDI",
}


def tracked_names():
    try:
        import update_prices as up  # noqa: WPS433
    except Exception as e:  # noqa: BLE001
        print(f"[name_index] update_prices import 실패: {e}")
        return {}
    names = {}
    for dct, mk in ((getattr(up, "TICKERS", {}), "KR"), (getattr(up, "WATCH", {}), "KR"), (getattr(up, "WATCH_KR_ETF", {}), "KR-ETF"),
                    (getattr(up, "WATCH_US", {}), "US"), (getattr(up, "WATCH_US_ETF", {}), "US-ETF")):
        for n, c in dct.items():
            names[n] = {"code": c, "market": mk}
    return names


def main():
    names = tracked_names()
    T = json.load(io.open(os.path.join(ROOT, "brain", "theses.json"), encoding="utf-8"))["pages"]
    E = json.load(io.open(os.path.join(ROOT, "brain", "entities.json"), encoding="utf-8")).get("companies", {})
    F = json.load(io.open(os.path.join(ROOT, "brain", "facts.json"), encoding="utf-8")).get("companies", {})
    idx = {}
    for n, v in names.items():
        idx[n] = {"code": v["code"], "market": v["market"], "entity": None, "falsifier": None, "facts": 0, "theses": {}, "aliases": []}
    # 엔티티(이름 또는 코드/티커로 연결)
    code2name = {v["code"].split(".")[0]: n for n, v in names.items()}
    for key, ent in E.items():
        nm = ent.get("name", "")
        target = None
        if nm in idx:
            target = nm
        elif key.split(".")[0] in code2name:
            target = code2name[key.split(".")[0]]
        else:
            for n in idx:
                if nm and (nm in n or n in nm):
                    target = n
                    break
        if target is None:
            idx[nm or key] = {"code": key, "market": ent.get("market", "?"), "entity": key, "falsifier": ent.get("falsifier"), "facts": 0, "theses": {}, "aliases": []}
            target = nm or key
        idx[target]["entity"] = key
        idx[target]["falsifier"] = ent.get("falsifier") or ent.get("note")
        for th in ent.get("theses", []):
            if "#" in th:
                pg, tid = th.split("#", 1)
                idx[target]["theses"].setdefault(pg, set()).update(tid.split(","))
    # facts
    for key, c in F.items():
        nm = c.get("name", "")
        target = next((n for n in idx if n == nm or key.split(".")[0] == idx[n]["code"].split(".")[0] or (nm and (nm in n or n in nm))), None)
        if target:
            idx[target]["facts"] = len(c.get("metrics", {}))
    # 테제 본문 스캔 — 이름·별칭이 claim/basis/log 에 나오면 연결
    alias_rev = {}
    for a, n in ALIAS.items():
        if n in idx:
            alias_rev.setdefault(n, []).append(a)
            idx[n]["aliases"].append(a)
    for pg, v in T.items():
        head = str(v.get("title", "")) + " " + str(v.get("one", ""))
        for n in idx:
            keys = [n] + alias_rev.get(n, [])
            if any(k and k in head for k in keys):  # 페이지 제목·한 문장에 이름이 있으면 그 페이지 테제 전부
                idx[n]["theses"].setdefault(pg, set()).update(t.get("id") for t in v.get("theses", []))
        for t in v.get("theses", []):
            blob = " ".join([str(t.get("claim", "")), str(t.get("basis", "")), " ".join(x.get("text", "") for x in t.get("log", []) if isinstance(x, dict))])
            for n in idx:
                keys = [n] + alias_rev.get(n, [])
                if any(k and k in blob for k in keys):
                    idx[n]["theses"].setdefault(pg, set()).add(t.get("id"))
    # 출력
    rows = []
    for n, v in sorted(idx.items(), key=lambda kv: (kv[1]["market"], kv[0])):
        th = {pg: sorted(x for x in ids if x) for pg, ids in v["theses"].items()}
        v["theses"] = th
        v["auto_candidate"] = n not in AMBIGUOUS and len(n) >= 3
        rows.append((n, v))
    js = {"generated": date.today().isoformat(), "names": {n: v for n, v in rows}}
    io.open(OUT_JS, "w", encoding="utf-8").write(json.dumps(js, ensure_ascii=False, indent=1))
    with_th = sum(1 for _, v in rows if v["theses"])
    md = [f"# 이름 색인 — 종목·키워드 → 테제 · 엔티티 · facts (훅 생성 · {js['generated']})", "",
          f"추적 {len(rows)}개 · 테제가 걸린 이름 {with_th} · 엔티티 있음 {sum(1 for _, v in rows if v['entity'])} · facts 있음 {sum(1 for _, v in rows if v['facts'])}.",
          "라우팅할 때 이름으로 여기를 먼저 본다(§R2 ①). 테제 0인 이름에 정보가 오면 ⓒ 신규 — 배치처가 없다는 뜻이므로 판단을 세울지 버릴지 그 자리에서 정한다.", "",
          "| 시장 | 이름 | 코드 | 엔티티(반증) | 테제 | facts |", "|---|---|---|---|---|---|"]
    for n, v in rows:
        th = " · ".join(f"{pg.split('/')[-1].replace('.html','')}#{','.join(ids)}" for pg, ids in v["theses"].items()) or "—"
        fz = (v["falsifier"] or "")[:60]
        md.append(f"| {v['market']} | {n} | {v['code']} | {'✓ ' + fz if v['entity'] else '—'} | {th} | {v['facts'] or '—'} |")
    io.open(OUT_MD, "w", encoding="utf-8").write("\n".join(md) + "\n")
    print(f"[name_index] {len(rows)}개 이름 · 테제 연결 {with_th} · 엔티티 {sum(1 for _, v in rows if v['entity'])} → docs/name_index.md · .json")


if __name__ == "__main__":
    main()
