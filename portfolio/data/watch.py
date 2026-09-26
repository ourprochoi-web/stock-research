#!/usr/bin/env python3
"""§J4 감시 — 「묻지 않아도 즉시 말하는 것 넷」을 세션 없이 매일 계산한다. 판단은 하지 않는다.

왜(2026-09-25): 반증 충족·스톱 도달·이벤트 도래·보유 테제 상태 변경은 §J4 가 「먼저 말하라」고 정한 것인데,
  말하는 주체가 세션뿐이라 세션이 열리지 않으면 전부 git 안에 잠겨 있었다(지난 이벤트 9건이 그 증거).
  이 스크립트는 브레인·시세만 읽어 목록을 만든다 — 새 데이터를 만들지 않고(§H1) 렌더만 한다.

항목: ① 지난 판정 이벤트(due<오늘) · 7일 내 이벤트(+사전약속 유무)
      ② 스톱·매도선 거리(portfolio.stops × prices) · 값 없는 스톱
      ③ 보유 종목 테제 — status≠유지 · last_tested 오래됨 · auto_basis 잔존
      ④ breaks_if 관측 후보 — regime.narratives / precommits 의 조건에 걸린 매크로 값(facts.macro · prices.fx/rates)
      ⑤ 레짐 신선도 · 미라우팅 큐(false · candidates 유무) · 기한 도래 미채점 예측 · 계약 검사 결과
용법: watch.py [--json] [--telegram]   (--telegram: TELEGRAM_BOT_TOKEN · TELEGRAM_CHAT_ID 환경변수가 있으면 전송)
"""
import io
import json
import os
import re
import subprocess
import sys
import urllib.parse
import urllib.request
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


def main(argv):
    today = date.today()
    ts = today.isoformat()
    T = J(B + "theses.json").get("pages", {})
    EV = J(B + "events.json").get("events", [])
    R = J(B + "regime.json")
    P = J(B + "portfolio.json")
    PR = J("portfolio/data/prices.json")
    RT = JL(B + "routing.jsonl")
    IN = JL("intake/user.jsonl") + JL("intake/collected.jsonl")
    out = {"asof": ts, "prices_asof": PR.get("updated")}

    # ① 이벤트
    past = sorted([e for e in EV if e.get("due") and e["due"] < ts], key=lambda e: e["due"])
    soon = sorted([e for e in EV if e.get("due") and ts <= e["due"] <= (today + timedelta(days=7)).isoformat()], key=lambda e: e["due"])
    out["events_overdue"] = [{"due": e["due"], "what": e["what"][:120], "judges": e.get("judges"), "precommit": bool(e.get("precommit"))} for e in past]
    out["events_7d"] = [{"due": e["due"], "what": e["what"][:120], "judges": e.get("judges"), "precommit": bool(e.get("precommit"))} for e in soon]
    out["events_total"] = len(EV)
    out["events_nodue"] = sum(1 for e in EV if "due" not in e)

    # ② 스톱
    def price_of(key):
        if key in PR.get("prices", {}):
            return PR["prices"][key]
        if key in PR.get("us", {}):
            return PR["us"][key].get("price")
        return None
    stops = []
    for s in P.get("stops", []):
        key = s.get("priceKey") or s.get("name")
        px = price_of(key)
        row = {"name": s.get("name"), "level": s.get("level"), "price": px}
        if s.get("level") and px:
            row["distance_pct"] = round((px / s["level"] - 1) * 100, 1)
            row["hit"] = px <= s["level"]
        else:
            row["missing"] = True
        stops.append(row)
    out["stops"] = stops
    out["stops_hit"] = [s for s in stops if s.get("hit")]
    out["stops_missing"] = [s["name"] for s in stops if s.get("missing")]

    # ③ 보유 테제
    held = []
    for h in P.get("holdings", []):
        pg = (h.get("page") or "").lstrip("./")
        page = T.get(pg)
        if not page:
            held.append({"name": h.get("name"), "page": pg, "note": "brain 에 없음"})
            continue
        ids = set(re.findall(r"T\d+", str(h.get("thesis", ""))))
        for t in page.get("theses", []):
            if ids and t["id"] not in ids:
                continue
            lt = t.get("last_tested") or "0000-00-00"
            age = (today - date.fromisoformat(lt)).days if re.match(r"\d{4}-\d{2}-\d{2}", lt) else None
            flag = []
            if t.get("status") not in (None, "유지"):
                flag.append(f"status {t['status']}")
            if age is not None and age > 14:
                flag.append(f"미검증 {age}일")
            held.append({"name": h.get("name"), "page": pg, "id": t["id"], "status": t.get("status"),
                         "last_tested": t.get("last_tested"), "flags": flag, "claim": str(t.get("claim"))[:80]})
    out["held_theses"] = held
    out["held_flagged"] = [x for x in held if x.get("flags") or x.get("note")]
    out["held_auto_basis"] = sum(1 for h in P.get("holdings", []) for t in T.get((h.get("page") or "").lstrip("./"), {}).get("theses", [])
                                 if t.get("auto_basis") and (not re.findall(r"T\d+", str(h.get("thesis", ""))) or t["id"] in re.findall(r"T\d+", str(h.get("thesis", "")))))

    # ④ breaks_if 관측 후보 — 숫자 문턱을 가진 조건만 기계가 본다(후보 · 판정은 사람)
    macro = J(B + "facts.json").get("macro", {})
    # 시세 봇 계열(2026-09-26) — facts.macro 는 손으로 갱신하는 정본이라 늦는다. 봇 값이 더 새로우면 그쪽을 읽는다.
    bot = dict(PR.get("macro") or {})
    rt = PR.get("rates") or {}
    for key, sid in (("us10y", "DGS10"), ("us2y", "DGS2"), ("us30y", "DGS30")):
        if sid in (rt.get("levels") or {}):
            bot[key] = {"value": rt["levels"][sid], "asof": (rt.get("asofs") or {}).get(sid, rt.get("asof")),
                        "tail": (rt.get("tail") or {}).get(sid, [])}
    def mval(k):
        m, b2 = macro.get(k), bot.get(k)
        cands = [x for x in (m, b2) if isinstance(x, dict) and x.get("value") is not None]
        if not cands:
            return None, None
        x = max(cands, key=lambda c: str(c.get("asof") or ""))
        return x.get("value"), x.get("asof")
    checks = []
    conds = []
    for n in R.get("narratives", []):
        if n.get("breaks_if"):
            conds.append(("narrative " + n.get("id", "?"), n["breaks_if"]))
    for p in P.get("precommits", []):
        conds.append(("precommit", p.get("if", "")))
    for c in R.get("changes_if", []) or []:
        conds.append(("regime.changes_if", str(c)))
    keymap = {"브렌트": "brent", "Brent": "brent", "TTF": "ttf", "HH": "henry_hub", "10Y": "us10y", "10년": "us10y", "VIX": "vix", "WTI": "wti", "JKM": "jkm"}
    for src, txt in conds:
        for word, key in keymap.items():
            m = re.search(re.escape(word) + r"[^<>≤≥\d]{0,12}([<>≤≥])\s*\$?\s*([\d.]+)", txt)
            if not m:
                continue
            v, asof = mval(key)
            if v is None:
                continue
            op, thr = m.group(1), float(m.group(2))
            hit = (v < thr) if op in "<≤" else (v > thr)
            checks.append({"source": src, "cond": txt[:110], "key": key, "value": v, "asof": asof, "threshold": f"{op}{thr}", "hit": hit})
    out["breaks_if_checks"] = checks
    out["breaks_if_hit"] = [c for c in checks if c["hit"]]

    # ④-b 판정 재료 스냅샷(2026-09-26) — 이벤트가 묻는 모양 그대로: 10Y 5일 평균 vs 5.00 · 브렌트 현물−선물 · 탱커 vs 브렌트 5일
    def tail(k):
        return [v for _, v in (bot.get(k) or {}).get("tail") or []]
    snap = {}
    t10 = tail("us10y")
    if t10:
        snap["us10y"] = {"last": t10[-1], "avg5": round(sum(t10[-5:]) / len(t10[-5:]), 3), "asof": bot["us10y"].get("asof"), "line": 5.00}
    bs, bf = bot.get("brent"), bot.get("brent_front_ice")
    if bs and bf:
        # 같은 날짜끼리 뺀다 — FRED 현물은 2~3일 늦게 올라와서 최신값끼리 빼면 격차가 날짜 차이를 먹는다(09-26 실측 +10.57 vs 같은 날 +15.64)
        fm = dict((d, v) for d, v in bf.get("tail") or [])
        common = [(d, v) for d, v in bs.get("tail") or [] if d in fm]
        if common:
            d, v = common[-1]
            snap["brent_gap"] = {"date": d, "spot": v, "front": fm[d], "gap": round(v - fm[d], 2),
                                 "front_latest": bf["value"], "front_asof": bf["asof"]}
    def chg5(k):
        t = tail(k)
        return round((t[-1] / t[-6] - 1) * 100, 1) if len(t) >= 6 else None
    tk = {k.split("_", 1)[1]: chg5(k) for k in bot if k.startswith("tanker_") and chg5(k) is not None}
    if tk and chg5("brent_front_ice") is not None:
        snap["tanker_vs_brent_5d"] = {"brent_front": chg5("brent_front_ice"), "tankers": tk}
    out["macro_snap"] = snap

    # ⑤ 레짐 · 큐 · 예측 · 계약
    rage = (today - date.fromisoformat(R["asof"])).days if R.get("asof") else None
    out["regime"] = {"asof": R.get("asof"), "age_days": rage, "stale": bool(rage and rage > 7), "one": R.get("one")}
    q = [r for r in IN if r.get("routed") is False and r.get("status", "ok") == "ok"]
    out["queue"] = {"total": len(q), "with_candidates": sum(1 for r in q if r.get("candidates")),
                    "skipped": sum(1 for r in IN if str(r.get("routed", "")).startswith("skip:")),
                    "by_kind": {}}
    for r in q:
        k = r.get("kind") or r.get("channel") or "?"
        out["queue"]["by_kind"][k] = out["queue"]["by_kind"].get(k, 0) + 1
    preds = [r for r in RT if r.get("kind") == "prediction"]
    out["predictions_due_unscored"] = [{"id": r["id"], "resolve_by": r.get("resolve_by"), "claim": str(r.get("claim"))[:90]}
                                       for r in preds if r.get("resolve_by") and r["resolve_by"] <= ts and not (r.get("outcome") or r.get("judged_by"))]
    # 종합층(2026-09-26) — 테제에 안 걸린 관측이 회사 카드 watch[] 에 쌓인다. 쌓임 자체가 「승격 후보」 신호다
    ENT = J(B + "entities.json").get("companies", {})
    week = (today - timedelta(days=7)).isoformat()
    cands = [(k, c) for k, c in ENT.items() if c.get("status") == "후보"]
    out["watch"] = {
        "cards_with_watch": sum(1 for c in ENT.values() if c.get("watch")),
        "lines_7d": sum(1 for c in ENT.values() for w in c.get("watch") or [] if str(w.get("date", "")) >= week),
        "candidates": len(cands),
        "promote": [{"key": k, "name": c.get("name"), "watch": len(c.get("watch") or [])}
                    for k, c in cands if len(c.get("watch") or []) >= 5 and not c.get("theses")],
        "over_cap": [{"key": k, "name": c.get("name"), "watch": len(c.get("watch") or [])}
                     for k, c in ENT.items() if len(c.get("watch") or []) > 12],
    }
    out["routing_last_date"] = max((r.get("date", "") for r in RT), default=None)
    out["theses_last_touch"] = max((t.get("last_tested", "") for pg in T.values() for t in pg.get("theses", [])), default=None)
    try:
        r = subprocess.run([sys.executable, ".githooks/check_routing.py"], capture_output=True, text=True)
        out["contract"] = {"ok": r.returncode == 0, "tail": r.stdout.strip().splitlines()[-1] if r.stdout.strip() else ""}
    except OSError:
        out["contract"] = None

    if "--json" in argv:
        print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        text = render(out)
        print(text)
        if "--telegram" in argv:
            send_telegram(text)
    return 0


def render(o):
    L = [f"▎§J4 감시 · {o['asof']} · 시세 {o.get('prices_asof')}"]
    a = L.append
    if o["stops_hit"]:
        a("🔴 스톱 도달: " + " · ".join(f"{s['name']} {s['price']:,} ≤ {s['level']:,}" for s in o["stops_hit"]))
    if o["breaks_if_hit"]:
        a("🔴 반증 조건 관측치 충족(후보 · 판정은 사람):")
        for c in o["breaks_if_hit"]:
            a(f"   · {c['source']}: {c['key']}={c['value']} ({c['asof']}) {c['threshold']} — {c['cond']}")
    if o["events_overdue"]:
        a(f"🔴 지난 판정 이벤트 {len(o['events_overdue'])}건 — 판정하고 지운다:")
        for e in o["events_overdue"]:
            a(f"   · {e['due']} {e['what']}" + (" [사전약속]" if e["precommit"] else ""))
    a(f"▎7일 내 판정 이벤트 {len(o['events_7d'])}건" + (f" (전체 {o['events_total']} · due 없음 {o['events_nodue']})"))
    for e in o["events_7d"]:
        a(f"   · {e['due']} {e['what']}" + (" [사전약속]" if e["precommit"] else " [사전약속 없음]"))
    a("▎스톱 거리")
    for s in o["stops"]:
        a(f"   · {s['name']}: " + (f"{s.get('distance_pct')}% (현재 {s['price']:,} / 스톱 {s['level']:,})" if not s.get("missing") else "🔴 값 없음(사용자 몫)"))
    ms = o.get("macro_snap") or {}
    if ms:
        parts = []
        if ms.get("us10y"):
            u = ms["us10y"]
            parts.append(f"10Y {u['last']}({u['asof']}) · 5일 평균 {u['avg5']} {'< ' if u['avg5'] < u['line'] else '≥ '}{u['line']:.2f}")
        if ms.get("brent_gap"):
            g = ms["brent_gap"]
            parts.append(f"브렌트 현물−선물 {g['gap']:+}({g['date']} · {g['spot']}−{g['front']}) · 선물 최신 {g['front_latest']}({g['front_asof']})")
        if ms.get("tanker_vs_brent_5d"):
            t = ms["tanker_vs_brent_5d"]
            parts.append(f"5일: 브렌트 선물 {t['brent_front']:+}% vs 탱커 " + " ".join(f"{k} {v:+}%" for k, v in t["tankers"].items()))
        a("▎판정 재료 — " + " · ".join(parts))
    a(f"▎반증 문턱 검사 {len(o['breaks_if_checks'])}건 · 충족 {len(o['breaks_if_hit'])} · 보유 테제 중 auto_basis(파서 근거 · 재검증 전) {o.get('held_auto_basis')}건")
    if o["held_flagged"]:
        a(f"▎보유 테제 점검 {len(o['held_flagged'])}건 (status≠유지 · 14일 미검증)")
        for x in o["held_flagged"]:
            a(f"   · {x['name']} {x.get('id','')} [{x.get('status','')}] {', '.join(x.get('flags', [])) or x.get('note','')} — {x.get('claim','')}")
    rg = o["regime"]
    a(f"▎레짐 {rg['asof']} ({rg['age_days']}일{' 🟠 주 1회 리뷰 지남' if rg['stale'] else ''}) — {str(rg['one'])[:140]}")
    qn = o["queue"]
    a(f"▎라우팅 큐 {qn['total']}건 (후보 부착 {qn['with_candidates']} · skip 누적 {qn['skipped']}) · kind {qn['by_kind']}")
    w = o.get("watch") or {}
    a(f"▎종합(watch) 7일 {w.get('lines_7d', 0)}줄 · 카드 {w.get('cards_with_watch', 0)} · 후보 카드 {w.get('candidates', 0)}"
      + (" · 승격 판단: " + " · ".join(f"{x['name']}({x['watch']}줄)" for x in w["promote"]) if w.get("promote") else "")
      + (" · 🟠 12줄 초과: " + " · ".join(f"{x['name']}({x['watch']})" for x in w["over_cap"]) if w.get("over_cap") else ""))
    a(f"▎마지막 routing {o['routing_last_date']} · 마지막 테제 접촉 {o['theses_last_touch']}"
      + (" 🔴 routing 이 테제를 안 건드리고 있다" if o['routing_last_date'] and o['theses_last_touch'] and o['routing_last_date'] > o['theses_last_touch'] else ""))
    if o["predictions_due_unscored"]:
        a(f"▎기한 도래 미채점 예측 {len(o['predictions_due_unscored'])}건: " + " · ".join(f"{p['id']}({p['resolve_by']})" for p in o["predictions_due_unscored"]))
    if o.get("contract"):
        a(f"▎계약 검사 {'✓' if o['contract']['ok'] else '🔴 위반'} — {o['contract']['tail']}")
    return "\n".join(L)


def send_telegram(text):
    tok, chat = os.environ.get("TELEGRAM_BOT_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not tok or not chat:
        print("[watch] telegram 미전송 — TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID 없음", file=sys.stderr)
        return
    for chunk in [text[i:i + 3800] for i in range(0, len(text), 3800)]:
        data = urllib.parse.urlencode({"chat_id": chat, "text": chunk, "disable_web_page_preview": "true"}).encode()
        try:
            urllib.request.urlopen(f"https://api.telegram.org/bot{tok}/sendMessage", data=data, timeout=30).read()
        except Exception as e:  # noqa: BLE001
            print(f"[watch] telegram 전송 실패 — {e}", file=sys.stderr)
            return


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
