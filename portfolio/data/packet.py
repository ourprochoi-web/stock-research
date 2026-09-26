#!/usr/bin/env python3
"""종목 패킷 — §J2 답의 입력을 브레인·intake·시세에서 <읽기 전용>으로 조립한다. 판단은 하지 않는다.

왜(2026-09-25): theses.json 1MB · routing.jsonl 490KB 를 세션(또는 Lead 봇)이 직접 뒤지면 J2 의 품질이
  「그날 얼마나 잘 뒤졌나」에 달린다. 층 사이를 읽는 스크립트 하나로 고정한다 — 새 저장소가 아니다(§H1).
  AGENTS.md §7: 종목·포지션 질문에는 이 패킷 <위에서만> 답한다.

출력(마크다운): ⓪ 레짐 · ① 기준일 · 엔티티(+watch) · 보유·스톱·노출 · <지난 번 이후>(델타) · 테제(claim/status/저울/basis/falsifier/event)
  · <반대편>(ⓑ 모음) · facts(값·분자·분모·기준일·등급) · 시세·배수·수익률·수급(창 명시) · 판정 이벤트 · 열린 질문 · 최근 routing · 미채점 예측 · <비어 있는 칸>
2026-09-26 v2 — 판정(status)만 보여주던 것에 <종합>을 붙였다: 테제별 증거 저울(ⓐ/ⓑ 수 · 등급 분포 · 마지막 ⓑ),
  「지난 번 이후」(기본 = 이 이름의 마지막 kind:judgment 이후 · 없으면 30일), 반대편, 엔티티 watch[], 비어 있는 칸(= 딥리서치 티켓).
용법: packet.py <이름|티커|별칭> [--json] [--routing N] [--full] [--since YYYY-MM-DD]
  기본은 주 페이지(보유·엔티티·card:true)만 전문, 나머지 언급 페이지는 한 줄. --full 이면 전부 전문.
"""
import io
import json
import re
import sys
from datetime import date, timedelta

B = "brain/"


def J(p):
    try:
        return json.load(io.open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def JL(p):
    try:
        return [json.loads(l) for l in io.open(p, encoding="utf-8") if l.strip()]
    except (OSError, ValueError):
        return []


def resolve(q, names, holdings, facts_c, entities_c):
    """이름·티커·별칭 → (표준 이름, 코드, name_index 항목). 못 찾으면 (q, None, None)."""
    ql = q.lower()
    for nm, v in names.items():
        keys = [nm, v.get("code", ""), v.get("entity", "")] + list(v.get("aliases") or [])
        if any(k and str(k).lower() == ql for k in keys):
            return nm, v.get("entity") or v.get("code"), v
    for h in holdings:
        if q in (h.get("name"), h.get("ticker"), h.get("priceKey")):
            nm = h.get("priceKey") or h["name"]
            return nm, h.get("ticker"), names.get(nm)
    for tk, c in {**facts_c, **entities_c}.items():
        if ql in (tk.lower(), str(c.get("name", "")).lower()):
            return c.get("name", tk), tk, names.get(c.get("name", tk))
    # 부분 일치(마지막 수단 · 후보 나열)
    part = [nm for nm in names if ql in nm.lower()]
    if len(part) == 1:
        v = names[part[0]]
        return part[0], v.get("entity") or v.get("code"), v
    if part:
        print(f"[packet] 후보가 여럿이다: {part[:10]}", file=sys.stderr)
    return q, None, None


MARK_RE = re.compile(r"[ⓐⓑⓒ]")
GRADE_RE = re.compile(r"[①②③④]")


def balance(logs, since=None):
    """테제 log[] → 증거 저울. 판정(status)이 아니라 <무엇이 얼마나 쌓였나>를 보여준다."""
    marks = {"ⓐ": 0, "ⓑ": 0, "ⓒ": 0, "기타": 0}
    grades = {"①": 0, "②": 0, "③": 0, "④": 0}
    recent = {"ⓐ": 0, "ⓑ": 0}
    last_b = None
    for e in logs:
        m = MARK_RE.search(str(e.get("mark", "")))
        k = m.group(0) if m else "기타"
        marks[k] += 1
        for g in GRADE_RE.findall(str(e.get("text", ""))):
            grades[g] += 1
        if k == "ⓑ":
            last_b = e
        if since and str(e.get("date", "")) >= since and k in recent:
            recent[k] += 1
    return {"marks": marks, "grades": grades, "since": recent,
            "last_b": {"date": last_b.get("date"), "rid": last_b.get("rid"), "text": str(last_b.get("text", ""))[:200]} if last_b else None}


def main(argv):
    if not argv or argv[0].startswith("-"):
        print(__doc__)
        return 2
    q = argv[0]
    as_json = "--json" in argv
    nrt = int(argv[argv.index("--routing") + 1]) if "--routing" in argv else 5
    full = "--full" in argv
    since_arg = argv[argv.index("--since") + 1] if "--since" in argv else None
    clip = 100000 if full else 320
    today = date.today()

    names = J("docs/name_index.json").get("names", {})
    T = J(B + "theses.json").get("pages", {})
    F = J(B + "facts.json")
    E = J(B + "entities.json")
    EV = J(B + "events.json").get("events", [])
    O = J(B + "open.json").get("open", [])
    R = J(B + "regime.json")
    P = J(B + "portfolio.json")
    PR = J("portfolio/data/prices.json")
    RT = JL(B + "routing.jsonl")

    facts_c = F.get("companies", {})
    ent_c = E.get("companies", {})
    holdings = P.get("holdings", [])
    name, code, nidx = resolve(q, names, holdings, facts_c, ent_c)
    keys = {k for k in [name, code, q] if k}
    if nidx:
        keys |= set(nidx.get("aliases") or [])
    primary = []
    for h in holdings:
        if h.get("name") == name or h.get("priceKey") == name or h.get("ticker") == code:
            pg = (h.get("page") or "").lstrip("./")
            if pg and pg not in primary:
                primary.append(pg)
    ent = ent_c.get(code) or next((c for c in ent_c.values() if c.get("name") == name), None)
    fc = facts_c.get(code) or next((c for c in facts_c.values() if c.get("name") == name), None)
    if ent:
        for pg in ent.get("pages", []):
            if pg not in primary:
                primary.append(pg)
    if fc and fc.get("canonical_page") and fc["canonical_page"] not in primary:
        primary.append(fc["canonical_page"])
    pages = list(primary)
    for pg in (nidx or {}).get("theses", {}).keys():
        if pg not in pages:
            pages.append(pg)
    if not primary:  # 보유·엔티티 페이지가 없으면 card:true 페이지를 주 페이지로
        primary = [pg for pg in pages if T.get(pg, {}).get("card")] or pages[:1]
    def mentions(s):
        s = str(s or "")
        return any(k in s for k in keys) or any(pg.split("/")[-1].replace(".html", "") in s for pg in pages)

    out = {"query": q, "name": name, "code": code, "asof": today.isoformat(),
           "regime": {"asof": R.get("asof"), "one": R.get("one"), "changes_if": R.get("changes_if")},
           "prices_asof": PR.get("updated"), "price_definition": PR.get("priceDefinition")}

    # 이 이름에 걸린 routing — 델타의 기준점(마지막 J2 judgment)도 여기서
    ent_key = f"entity:{code}" if code else None
    rel = [r for r in RT if mentions(r.get("claim")) or any(mentions(x) for x in (r.get("routed") or []))
           or (ent_key and ent_key in str(r.get("parked", "")))]
    last_j = max((str(r.get("date", "")) for r in rel if r.get("kind") == "judgment"), default=None)
    since = since_arg or last_j or (today - timedelta(days=30)).isoformat()
    out["since"] = {"date": since, "basis": "--since" if since_arg else ("마지막 J2 judgment" if last_j else "기본 30일")}

    # 엔티티 (+ watch — 테제에 안 걸린 관측의 종합 · AGENTS.md §4 관측 축적)
    if ent:
        out["entity"] = {k: ent.get(k) for k in ("name", "market", "layer", "business", "business_grade", "theses", "status") if k in ent}
        watch = ent.get("watch") or []
        out["watch"] = {"total": len(watch), "since": sum(1 for w in watch if str(w.get("date", "")) >= since),
                        "recent": [{k: w.get(k) for k in ("date", "grade", "rid", "one")} for w in watch[-8:]]}

    # 보유 · 스톱 · 사이징 · 노출
    hs = [h for h in holdings if h.get("name") == name or h.get("priceKey") == name or h.get("ticker") == code]
    px = PR.get("prices", {}).get(name)
    if px is None and name in PR.get("us", {}):
        px = PR["us"][name].get("price")
    pos = []
    for h in hs:
        row = {k: h.get(k) for k in ("name", "qty", "avgPrice", "totalCost", "thesis", "legacy", "note")}
        if px and h.get("qty") and h.get("avgPrice"):
            row["price"] = px
            row["value"] = px * h["qty"]
            row["pnl_pct"] = round((px / h["avgPrice"] - 1) * 100, 1)
        pos.append(row)
    out["position"] = pos or "보유 없음"
    out["stops"] = [s for s in P.get("stops", []) if s.get("name") in {h.get("name") for h in hs} or s.get("priceKey") == name]
    for s in out["stops"]:
        if s.get("level") and px:
            s["distance_pct_now"] = round((px / s["level"] - 1) * 100, 1)
    out["sizing_row"] = next((r for r in P.get("sizing", {}).get("holdings_table", []) if r.get("name") in {h.get("name") for h in hs} or r.get("ticker") == code), None)
    out["exposures"] = {k: {kk: v.get(kk) for kk in ("share_of_equity", "direction", "mechanisms")}
                        for k, v in P.get("exposures", {}).items() if name in (v.get("names") or [])}
    out["precommits"] = [p for p in P.get("precommits", []) if mentions(p.get("if")) or mentions(p.get("then"))]

    # 테제
    th_out = []
    for pg in pages:
        page = T.get(pg)
        if not page:
            th_out.append({"page": pg, "note": "brain/theses.json 에 없음 — 페이지만 있다(카드 미전환)"})
            continue
        want = set((nidx or {}).get("theses", {}).get(pg, []))
        rows = []
        if pg not in primary and not full:
            th_out.append({"page": pg, "judged": page.get("judged"), "secondary": True,
                           "theses": [{"id": t["id"], "status": t.get("status"), "claim": str(t.get("claim"))[:90]}
                                      for t in page.get("theses", []) if (not want or t["id"] in want or mentions(t.get("claim")))]})
            continue
        for t in page.get("theses", []):
            if want and t["id"] not in want and not mentions(t.get("claim")):
                continue
            lg = t.get("log") or []
            rows.append({"id": t["id"], "status": t.get("status"), "claim": t.get("claim"), "basis": str(t.get("basis") or "")[:clip],
                         "auto_basis": bool(t.get("auto_basis")), "falsifier": t.get("falsifier"), "event": t.get("event"),
                         "last_tested": t.get("last_tested"), "facts": t.get("facts"),
                         "log_n": len(lg), "log_last": lg[-1] if lg else None,
                         "balance": balance(lg, since),
                         "log_since": [{"date": e.get("date"), "mark": e.get("mark"), "rid": e.get("rid"), "text": str(e.get("text", ""))[:160]}
                                       for e in lg if str(e.get("date", "")) >= since]})
        th_out.append({"page": pg, "judged": page.get("judged"), "one": page.get("one"), "card": bool(page.get("card")),
                       "position": page.get("position"), "next": page.get("next"), "theses": rows})
    out["theses"] = th_out

    # facts — 값 + 분자·분모 + 기준일 + 등급
    if fc:
        out["facts"] = {k: {kk: m.get(kk) for kk in ("value", "unit", "basis", "asof", "num", "den", "grade", "source")}
                        for k, m in fc.get("metrics", {}).items()}
        out["facts_intake"] = fc.get("intake")

    # 시세 · 배수 · 수익률 · 수급 — 창을 밝힌 관측(§J4)
    mk = {}
    if name in PR.get("prices", {}):
        mk["price_regular"] = PR["prices"][name]
        mk["after"] = PR.get("after", {}).get(name)
    if name in PR.get("us", {}):
        mk["us"] = {k: PR["us"][name].get(k) for k in ("price", "mcapB", "EBIT", "매출액", "OPM", "EBIT_YoY", "목표주가", "quarters")}
    if name in PR.get("fundamentals", {}):
        mk["fundamentals(naver 라벨 · 분자분모 미확인)"] = PR["fundamentals"][name]
    if name in PR.get("returns", {}):
        mk["returns"] = PR["returns"][name]
    if name in PR.get("flows", {}):
        mk["flows(창 명시 · 테제 아님)"] = PR["flows"][name]
    out["market"] = mk or None

    # 판정 이벤트 — 이 종목·페이지에 걸린 것 · due 순
    evs = [e for e in EV if mentions(e.get("judges")) or mentions(e.get("what"))]
    evs.sort(key=lambda e: e.get("due") or "9999")
    out["events"] = [{"due": e.get("due"), "when": e.get("when"), "what": e.get("what"), "judges": e.get("judges"),
                      "grade": e.get("grade"), "precommit": e.get("precommit"),
                      "overdue": bool(e.get("due") and e["due"] < today.isoformat())} for e in evs]

    # 열린 질문
    out["open"] = [{"id": o.get("id"), "since": o.get("since"), "what": o.get("what")[:300]} for o in O if mentions(o.get("what"))]

    # 최근 routing · 미채점 예측
    out["routing_recent"] = [{k: r.get(k) for k in ("id", "date", "kind", "grade", "claim", "routed", "verdict", "action",
                                                     "priced_in", "variant", "breaks_if", "resolve_by")} for r in rel[-nrt:]]
    out["predictions_open"] = [{k: r.get(k) for k in ("id", "date", "claim", "resolve_by", "confidence")}
                               for r in rel if r.get("kind") == "prediction" and not (r.get("outcome") or r.get("judged_by"))]
    out["routing_total"] = len(rel)

    # 지난 번 이후 — 결정 시점의 종합은 「전체」가 아니라 델타다
    prim_rows = [t for pg in th_out if not pg.get("secondary") for t in pg.get("theses", [])]
    facts_since = [k for k, m in (out.get("facts") or {}).items() if str(m.get("asof", "")) >= since]
    out["delta"] = {
        "routing": [{k: r.get(k) for k in ("id", "date", "kind", "grade", "claim", "verdict", "parked")} for r in rel if str(r.get("date", "")) >= since],
        "log": [{"thesis": t["id"], **e} for t in prim_rows for e in t["log_since"]],
        "watch": [w for w in (out.get("watch") or {}).get("recent", []) if str(w.get("date", "")) >= since],
        "facts": facts_since,
        "status_changed": [{"thesis": t["id"], "status": t["status"], "last_tested": t["last_tested"]}
                           for t in prim_rows if str(t.get("last_tested", "")) >= since and str(t.get("status")) not in ("유지",)],
    }

    # 반대편 — 저울의 다른 쪽을 한 곳에 모은다(ⓑ 로그 · 도전 routing)
    contra = []
    for pg in th_out:
        if pg.get("secondary") or pg.get("note"):
            continue
        src = {x["id"]: x for x in T.get(pg["page"], {}).get("theses", [])}
        for t in pg.get("theses", []):
            for e in src.get(t["id"], {}).get("log") or []:
                if "ⓑ" in str(e.get("mark", "")):
                    contra.append({"date": e.get("date"), "thesis": f"{pg['page'].split('/')[-1]}#{t['id']}", "rid": e.get("rid"),
                                   "text": str(e.get("text", ""))[:200]})
    for r in rel:
        if "ⓑ" in str(r.get("verdict", "")) or "도전" in str(r.get("verdict", "")):
            tgt = ",".join(x.split("/")[-1] for x in (r.get("routed") or [])) or str(r.get("parked"))
            contra.append({"date": r.get("date"), "thesis": tgt[:70], "rid": r.get("id"),
                           "text": str(r.get("claim", ""))[:200]})
    contra.sort(key=lambda x: str(x.get("date", "")), reverse=True)
    out["contra"] = contra[:8]
    out["contra_total"] = len(contra)

    # 비어 있는 칸 — 채워야 근거 등급이 오르는 자리 = 딥리서치 티켓
    gaps = []
    for k, m in (out.get("facts") or {}).items():
        if m.get("value") is not None and (m.get("num") in (None, "") or m.get("den") in (None, "")):
            gaps.append(f"facts.{k}: 값 {m.get('value')} 은 있는데 분자·분모가 없다(§W2 — 아직 값이 아니다)")
    for t in prim_rows:
        if not str(t.get("falsifier") or "").strip():
            gaps.append(f"{t['id']}: 반증 조건 없음 — 틀렸음을 알 방법이 없다")
        ev_s = str(t.get("event") or "").strip()
        if not ev_s or ev_s.startswith("미정"):
            gaps.append(f"{t['id']}: 판정 창 없음/미정 — 언제 틀렸는지 모른다")
        if t.get("auto_basis"):
            gaps.append(f"{t['id']}: basis 가 파서 추출(auto_basis) — 재검증 전")
        b = t["balance"]
        if b["marks"]["ⓐ"] >= 3 and b["marks"]["ⓑ"] == 0:
            gaps.append(f"{t['id']}: ⓐ {b['marks']['ⓐ']}건 · ⓑ 0건 — 반대편을 찾지 않았다(저울이 한쪽)")
        if b["grades"]["①"] == 0 and (b["grades"]["③"] + b["grades"]["②"]) >= 3:
            gaps.append(f"{t['id']}: 로그에 ① 0건 · ②③ {b['grades']['②'] + b['grades']['③']}건 — 하우스 의견만 쌓였다")
    if ent and ent.get("status") == "후보":
        n = (out.get("watch") or {}).get("total", 0)
        gaps.append(f"후보 카드 · watch {n}줄 · 테제 0 — {'승격 판단 시점' if n >= 5 else '아직 쌓는 중'}")
    for s in out["stops"]:
        if s.get("level") is None:
            gaps.append(f"스톱 {s.get('name')}: level 없음(사용자 몫) — 잃는 크기를 못 센다")
    out["gaps"] = gaps

    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return 0
    print(render(out, today))
    return 0


def render(o, today):
    L = []
    a = L.append
    a(f"# 패킷 · {o['name']}" + (f" ({o['code']})" if o.get("code") else "") + f" · 기준일 {o['asof']}")
    rg = o["regime"]
    age = (today - date.fromisoformat(rg["asof"])).days if rg.get("asof") else None
    a(f"\n## ⓪ 레짐 ({rg.get('asof')} · {age}일{' 🟠' if age and age > 7 else ''})\n{rg.get('one')}")
    if rg.get("changes_if"):
        a("바뀌면 — " + " · ".join(str(x)[:80] for x in rg["changes_if"][:4]))
    a(f"\n## ① 기준일 — 시세 {o.get('prices_asof')} · {o.get('price_definition')}")
    if o.get("entity"):
        e = o["entity"]
        a(f"\n## 엔티티 — {e.get('layer')} · {e.get('business')} ({e.get('business_grade')})" + (f" · **{e['status']}**" if e.get("status") else ""))
        w = o.get("watch") or {}
        if w.get("total"):
            a(f"watch {w['total']}줄 (지난 번 이후 {w['since']}) — 테제에 안 걸린 관측의 종합")
            for x in w["recent"]:
                a(f"- {x.get('date')} {x.get('grade')} {x.get('one')} ({x.get('rid')})")
    a("\n## 보유 · 스톱 · 노출")
    if isinstance(o["position"], str):
        a(o["position"])
    else:
        for p in o["position"]:
            a(f"- {p['name']}: {p.get('qty')}주 @ {p.get('avgPrice'):,} · 현재 {p.get('price') and format(p['price'], ',')} · "
              f"손익 {p.get('pnl_pct')}% · 테제 {p.get('thesis')}" + (" · ⚠ legacy" if p.get("legacy") else ""))
    for s in o["stops"]:
        a(f"- 스톱 {s.get('name')}: level {s.get('level')} · 거리 {s.get('distance_pct_now')}%" + (f" · {s.get('note')}" if s.get("note") else "")
          + ("  ← 🔴 값 없음(사용자 몫)" if s.get("level") is None else ""))
    sr = o.get("sizing_row")
    if sr:
        a(f"- 사이징: 반증 낙폭 {sr.get('drawdown_at_falsifier_pct')}%{' ← 🔴 미측정' if sr.get('drawdown_at_falsifier_pct') is None else ''} · 창 {sr.get('time_window_event')}")
    for k, v in o["exposures"].items():
        a(f"- 노출 {k}: share {v.get('share_of_equity')} · {v.get('direction')} · mech {v.get('mechanisms')}")
    for p in o["precommits"]:
        a(f"- 사전약속: if {p.get('if')} → {p.get('then')}")
    d = o.get("delta") or {}
    s = o.get("since") or {}
    a(f"\n## 지난 번 이후 — {s.get('date')} ({s.get('basis')}) · routing {len(d.get('routing', []))} · 테제 log {len(d.get('log', []))} · watch {len(d.get('watch', []))} · facts 갱신 {len(d.get('facts', []))}")
    if not any(d.get(k) for k in ("routing", "log", "watch", "facts", "status_changed")):
        a("들어온 것 없음 — 판단을 바꿀 새 정보가 없다는 것도 정식 결과다")
    for x in d.get("status_changed", []):
        a(f"- 🔶 {x['thesis']} status {x['status']} (검증 {x['last_tested']})")
    for x in d.get("log", []):
        a(f"- {x.get('date')} {x.get('mark')} {x['thesis']} — {x.get('text')}")
    for x in d.get("watch", []):
        a(f"- {x.get('date')} watch {x.get('grade')} — {x.get('one')}")
    for x in d.get("routing", []):
        if x.get("kind") in ("judgment", "prediction", "verdict", "correction", "decision"):
            a(f"- {x.get('date')} {x.get('kind')} {x['id']} — {str(x.get('claim'))[:140]}")
    if d.get("facts"):
        a(f"- facts 갱신: {', '.join(d['facts'])}")
    a("\n## 테제 (저울 = ⓐ/ⓑ 수 · 로그의 등급 분포 · 마지막 ⓑ — status 보다 먼저 읽는다)")
    for pg in o["theses"]:
        if pg.get("secondary"):
            a(f"- (언급 페이지) {pg['page']} · 판단 {pg.get('judged')} — " + " / ".join(f"{t['id']}[{t['status']}] {t['claim']}" for t in pg["theses"][:4]) + "  (--full 로 전문)")
            continue
        a(f"### {pg['page']}" + (f" · 판단 {pg.get('judged')} · card {pg.get('card')}" if "judged" in pg else ""))
        if pg.get("note"):
            a(pg["note"])
            continue
        if pg.get("one"):
            a(f"한 문장 — {pg['one']}")
        for t in pg["theses"]:
            a(f"- **{t['id']} [{t['status']}]** {t['claim']}")
            b = t.get("balance") or {}
            if b:
                m, g, r = b["marks"], b["grades"], b["since"]
                lean = "한쪽" if (m["ⓐ"] >= 3 and m["ⓑ"] == 0) else ("반반" if m["ⓑ"] and m["ⓑ"] >= m["ⓐ"] * 0.5 else "")
                a(f"  - 저울: ⓐ {m['ⓐ']} · ⓑ {m['ⓑ']}" + (f" · ⓒ {m['ⓒ']}" if m["ⓒ"] else "") +
                  f" · 등급 ①{g['①']} ②{g['②']} ③{g['③']} ④{g['④']}" + (f" · 지난 번 이후 ⓐ{r['ⓐ']}/ⓑ{r['ⓑ']}" if (r["ⓐ"] or r["ⓑ"]) else "") +
                  (f" · **{lean}**" if lean else "") + (" · ①0 — 하우스 의견만" if g["①"] == 0 and (g["②"] + g["③"]) >= 3 else ""))
                if b.get("last_b"):
                    a(f"  - 마지막 ⓑ {b['last_b']['date']}: {b['last_b']['text'][:160]}")
            a(f"  - 근거{' (auto_basis · 파서 추출 · 재검증 전)' if t['auto_basis'] else ''}: {t.get('basis')}")
            a(f"  - 반증: {t.get('falsifier')}")
            a(f"  - 판정: {t.get('event')} · 마지막 검증 {t.get('last_tested')} · log {t['log_n']}건"
              + (f" · 최근 {t['log_last'].get('date')} {t['log_last'].get('mark')} {str(t['log_last'].get('text'))[:100]}" if t.get("log_last") else ""))
    a(f"\n## 반대편 {min(len(o.get('contra', [])), 8)}/{o.get('contra_total', 0)} — 테제에 맞서는 기록(ⓑ 로그 · 도전 routing)")
    for c in o.get("contra") or ["없음 — 반대편을 아직 찾지 않았다는 뜻일 수도 있다"]:
        if isinstance(c, str):
            a(c); continue
        a(f"- {c.get('date')} {c.get('thesis')} — {c.get('text')}" + (f" ({c.get('rid')})" if c.get("rid") else ""))
    if o.get("facts"):
        a("\n## facts (값 · 분자/분모 · 기준일 · 등급)")
        for k, m in o["facts"].items():
            a(f"- {k} = {m.get('value')} {m.get('unit') or ''} · {m.get('num')} / {m.get('den')} · {m.get('asof')} · {m.get('grade')} · {m.get('basis')}")
    if o.get("market"):
        a("\n## 시세 · 관측 (테제 아님 · 창 명시)")
        for k, v in o["market"].items():
            a(f"- {k}: {json.dumps(v, ensure_ascii=False)}")
    a("\n## 판정 이벤트")
    for e in o["events"][:12] or ["없음"]:
        if isinstance(e, str):
            a(e); continue
        a(f"- {'🔴 지남 ' if e['overdue'] else ''}{e.get('due') or '조건'} · {e['what'][:140]} · {e.get('grade')}"
          + (f" · 사전약속 {json.dumps(e['precommit'], ensure_ascii=False)[:120]}" if e.get("precommit") else ""))
    if o["open"]:
        a("\n## 열린 질문")
        for x in o["open"]:
            a(f"- ({x.get('since')}) {x['what'][:200]}")
    a(f"\n## 최근 routing {len(o['routing_recent'])}/{o['routing_total']}")
    for r in o["routing_recent"]:
        a(f"- {r['id']} {r.get('kind') or 'route'} {r.get('grade')} — {str(r.get('claim'))[:120]} → {r.get('routed')} · {r.get('verdict')}"
          + (f"\n  - priced_in: {str(r.get('priced_in'))[:120]} / variant: {str(r.get('variant'))[:120]} / breaks_if: {str(r.get('breaks_if'))[:120]}" if r.get("priced_in") else ""))
    if o["predictions_open"]:
        a("\n## 미채점 예측")
        for p in o["predictions_open"]:
            a(f"- {p['id']} ({p.get('resolve_by')} · {p.get('confidence')}) {str(p.get('claim'))[:120]}")
    a(f"\n## 비어 있는 칸 {len(o.get('gaps', []))} — 채워야 근거 등급이 오르는 자리(= 딥리서치 티켓)")
    for g in o.get("gaps") or ["없음"]:
        a(f"- {g}")
    a("\n---\nJ2 답은 이 패킷 위에서만 — 저울과 「지난 번 이후」를 먼저, status 는 뒤에. ② 배수는 facts 의 분자·분모로, ④ 잃는 크기는 stops·sizing 이 null 이면 「미측정」으로, ⑥ 은 exposures 로. 답을 냈으면 routing kind:judgment 한 줄(다음 델타의 기준점).")
    return "\n".join(L)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
