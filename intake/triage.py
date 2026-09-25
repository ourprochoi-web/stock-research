#!/usr/bin/env python3
"""수집 직후 트리아지 — 판단이 아니라 <분류>다. 라우팅 큐에 넣을 것과 넣지 않을 것을 가른다.

왜(2026-09-25 실측): 텔레그램 수집기가 붙은 09-23부터 사흘간 501건이 전부 routed:false 로 들어와
  미라우팅 큐가 456건(52%)이 됐다. 라우팅 처리량은 하루 중앙값 ~15건. 큐에 들어온 것의 상당수는
  링크만(46건) · 이름도 수치도 없는 잡담이라 「라우팅할 주장」이 없다. 이것을 사람이 골라내는 것이
  세션 시간을 다 먹었다(§R3 「routed:false 를 읽는다」가 실행 불가능해진 이유).

세 갈래(intake/README 「routed 값」):
  routed:false            주장이 있다 — 라우팅 대기. candidates[] 에 걸리는 테제 후보를 붙인다(라우팅은 사람·Lead가 한다)
  routed:"skip:<이유>"    라우팅 대상이 아니다 — link(링크만) · short(본문 없음) · media(미디어만) · no-claim(이름도 주장 신호도 없음)
  routed:"data"           수치 원료(기존 · collect.py)

버리지 않는다 — 줄과 files/ 조각은 그대로 남는다(intake 규칙 4). skip 은 「지금 큐에 없다」일 뿐이고 grep 으로 언제든 찾는다.
이름 매치는 docs/name_index.json(훅이 생성 · 318명). 이름이 없어도 주장 신호(수치·목표가·가이던스·수주·정책)가 있으면 큐에 남긴다 —
이름 색인은 <이미 아는 회사>만 잡으므로 ⓒ 신규가 영원히 안 보이게 되는 것을 막는다.

용법:
  from triage import triage; kind, cands = triage(text)
  python3 intake/triage.py --retriage            # 기존 routed:false 텔레그램 줄에 소급 적용(routed 값·candidates 만 바꾼다)
  python3 intake/triage.py --retriage --dry-run
"""
from __future__ import annotations

import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
NAME_INDEX = os.path.join(ROOT, "docs", "name_index.json")

URL_RE = re.compile(r"https?://\S+")
# 주장 신호 — 숫자가 단위와 붙었거나, 애널·공시·정책 어휘가 있다. 넓게 잡는다(후보를 좁힐 뿐 판정하지 않는다 · §C1).
CLAIM_RE = re.compile(
    r"(\d[\d,.]*\s*(%|％|억|조|만\s*원|원|bn|B\b|M\b|mn|k\b|GW|MW|TWh|kW|mb/d|bp|배|주|톤|t\b|\$|USD|€|¥|위안|달러)"
    r"|\$\s?\d"
    r"|목표주가|목표가|TP\b|PT\b|가이던스|guidance|컨센서스|consensus|상향|하향|upgrade|downgrade"
    r"|Overweight|Underweight|Outperform|Neutral\b|\bBuy\b|\bSell\b|\bHold\b|매수|매도|비중\s*(확대|축소)"
    r"|수주|계약|공시|실적|영업이익|매출|OP\b|EPS|ASP|CapEx|캐펙스|투자\s*발표|증설|감산|가격\s*인상|인하"
    r"|FOMC|금리|관세|제재|행정명령|법안|규제|허가|승인|출시|양산|퀄|인증"
    r"|YoY|QoQ|MoM|전년|전분기|분기|1Q|2Q|3Q|4Q|FY\d"
    # 매크로·레짐 내러티브 어휘(regime.json narratives · mechanisms nodes) — 회사 이름이 없어도 레짐에 걸린다
    r"|호르무즈|Hormuz|이란|Iran|사우디|OPEC|유가|브렌트|Brent|WTI|천연가스|TTF|JKM|Henry\s*Hub"
    r"|연준|Fed\b|파월|국채|10년물|장기물|일드|수익률\s*곡선|환율|원화|달러\s*인덱스|DXY|CPI|PCE|고용|실업"
    r"|중간선거|midterm|CXMT|YMTC|화웨이|Huawei|엔비디아|NVIDIA|하이퍼스케일러|hyperscaler)",
    re.I,
)
_NIDX = None


def _names():
    global _NIDX
    if _NIDX is None:
        try:
            raw = json.load(io.open(NAME_INDEX, encoding="utf-8"))["names"]
        except (OSError, ValueError, KeyError):
            raw = {}
        keys = []
        for nm, v in raw.items():
            if not v.get("theses"):
                continue
            for k in [nm] + list(v.get("aliases") or []):
                k = str(k).strip()
                if len(k) >= 2:
                    keys.append((k, nm, v))
        # 긴 이름 먼저(「SK」보다 「SK하이닉스」) · 대소문자는 영문만 무시
        keys.sort(key=lambda x: -len(x[0]))
        _NIDX = keys
    return _NIDX


def _contains(text, key):
    if re.search(r"[가-힣]", key):
        return key in text
    # 영문 키는 단어 경계 + 대소문자 무시 (「Arm」이 「farm」에 걸리지 않게)
    return re.search(r"(?<![A-Za-z])" + re.escape(key) + r"(?![A-Za-z])", text, re.I) is not None


def candidates(text, limit=12):
    """이름 색인 매치 → [{name, theses:[page#T,…]}]. 라우팅 후보일 뿐 판정이 아니다."""
    out, seen = [], set()
    for key, nm, v in _names():
        if nm in seen or not _contains(text, key):
            continue
        seen.add(nm)
        th = []
        for pg, ids in list(v["theses"].items())[:3]:
            th += [f"{pg}#{i}" for i in ids[:3]]
        out.append({"name": nm, "theses": th})
        if len(out) >= limit:
            break
    return out


def triage(text):
    """→ (routed 값, candidates). routed 값은 False(큐) 또는 'skip:<이유>'."""
    t = (text or "").strip()
    if not t or t.startswith("[no text"):
        return "skip:media", []
    body = URL_RE.sub("", t).strip()
    if len(body) < 20 and URL_RE.search(t):
        return "skip:link", []
    if len(body) < 40:
        return "skip:short", []
    cands = candidates(t)
    if cands:
        return False, cands
    if CLAIM_RE.search(body):
        return False, []
    return "skip:no-claim", []


def apply(rec):
    """수집 레코드에 트리아지 결과를 써 넣는다(status ok 인 것만)."""
    if rec.get("status", "ok") != "ok":
        return rec
    routed, cands = triage(rec.get("text") or "")
    rec["routed"] = routed
    if cands:
        rec["candidates"] = cands
    elif "candidates" in rec:
        del rec["candidates"]
    rec["triage"] = "v1"
    return rec


def retriage(dry=False, kinds=("telegram",)):
    """기존 줄 중 routed:false · status ok · kind in kinds 에 소급 적용. text·subject·id 는 건드리지 않는다."""
    lines = io.open(LOG, encoding="utf-8").read().splitlines()
    out, stats = [], {"seen": 0, "queue": 0, "with_candidates": 0, "skip": {}}
    for ln in lines:
        if not ln.strip():
            out.append(ln)
            continue
        try:
            rec = json.loads(ln)
        except ValueError:
            out.append(ln)
            continue
        if rec.get("kind") in kinds and rec.get("routed") is False and rec.get("status", "ok") == "ok" and not rec.get("triage"):
            stats["seen"] += 1
            apply(rec)
            r = rec["routed"]
            if r is False:
                stats["queue"] += 1
                if rec.get("candidates"):
                    stats["with_candidates"] += 1
            else:
                stats["skip"][r] = stats["skip"].get(r, 0) + 1
            out.append(json.dumps(rec, ensure_ascii=False))
        else:
            out.append(ln)
    if not dry:
        io.open(LOG, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return stats


if __name__ == "__main__":
    if "--retriage" in sys.argv:
        st = retriage(dry="--dry-run" in sys.argv)
        print(f"[triage] 대상 {st['seen']} → 큐 잔류 {st['queue']} (후보 부착 {st['with_candidates']}) · skip {st['skip']}"
              + (" · dry-run" if "--dry-run" in sys.argv else ""))
    else:
        txt = sys.stdin.read()
        print(json.dumps({"routed": triage(txt)[0], "candidates": triage(txt)[1]}, ensure_ascii=False, indent=1))
