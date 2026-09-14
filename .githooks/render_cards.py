#!/usr/bin/env python3
"""brain/theses.json 의 card:true 페이지에 「현재 판단 카드」를 렌더해 끼워 넣는다.

페이지 안의 <!-- brain:card:start --> … <!-- brain:card:end --> 사이를 통째로 교체한다.
마커가 없는 페이지는 건드리지 않는다(첫 전환은 사람이 마커를 넣는다 — 옛 판단 블록을
어디로 옮길지는 판단이 필요하다).
용법: render_cards.py [--check] [페이지 ...]   (--check: 바꾸지 않고 어긋난 페이지만 출력)
"""
import html as H
import io
import json
import re
import sys
from datetime import date

THESES = "brain/theses.json"
START, END = "<!-- brain:card:start -->", "<!-- brain:card:end -->"
COLOR = {"유지": "var(--bull)", "도전": "#f87171", "정정": "#f87171", "철회": "var(--ink-3)",
         "관측": "#60a5fa", "방법": "var(--ink-3)"}


def e(s):
    return H.escape(str(s or ""), quote=False)


def render(path, pg):
    d = pg["judged"].replace("-", ".")
    th = pg.get("theses", [])
    cnt = {}
    for t in th:
        cnt[t.get("status", "유지")] = cnt.get(t.get("status", "유지"), 0) + 1
    cnt_s = " · ".join(f"{k} {v}" for k, v in cnt.items())
    rows = []
    for t in th:
        st = t.get("status", "유지")
        rows.append(
            f'<tr style="border-top:1px solid var(--line)">'
            f'<td style="padding:10px 8px 10px 0;vertical-align:top;white-space:nowrap"><b>{e(t["id"])}</b><br>'
            f'<span style="font-family:var(--mono);font-size:.68rem;color:{COLOR.get(st, "var(--ink-2)")}">{e(st)}</span></td>'
            f'<td style="padding:10px 0;vertical-align:top"><b>{e(t["claim"])}</b>'
            + (f'<br><span style="color:var(--ink-2)">근거 — {e(t["basis"])}</span>' if t.get("basis") else "")
            + (f'<br><span style="color:var(--ink-2)">반증 — {e(t["falsifier"])}</span>' if t.get("falsifier") else "")
            + (f'<br><span style="color:var(--ink-2)">판정 — {e(t["event"])}'
               + (f' · 마지막 검증 {e(t["last_tested"])}' if t.get("last_tested") else "") + "</span>" if t.get("event") else "")
            + "</td></tr>")
    nxt = "".join(f"<br>· {e(x)}" for x in pg.get("next", []))
    pos = e(pg.get("position") or "—")
    return (
        f"{START}\n"
        f'<section id="now" class="blk"><div class="wrap">\n'
        f'<div data-brain-card="{e(path)}" style="padding:18px 20px;border-left:4px solid var(--accent);background:rgba(249,115,22,.06);line-height:1.75">\n'
        f'<div style="font-weight:900;font-size:1.15em;color:var(--accent);margin-bottom:6px">▎현재 판단 · {d} '
        f'<span style="font-size:.7em;font-weight:600;color:var(--ink-3)">— 브레인 카드 · <code>brain/theses.json</code>에서 생성 {date.today().isoformat()} · 테제 {len(th)} ({cnt_s})</span></div>\n'
        f'<b style="font-size:1.05em">한 문장 — {e(pg.get("one"))}</b>\n'
        f'<table style="width:100%;border-collapse:collapse;font-size:.95rem;margin-top:12px">{"".join(rows)}</table>\n'
        f'<div id="falsify" style="margin-top:14px;padding-top:10px;border-top:1px solid var(--line)"><b style="color:#60a5fa">▎다음 검증 — 날짜가 아니라 이벤트</b>{nxt}</div>\n'
        f'<div style="margin-top:10px;color:var(--ink-2)"><b>포지션</b> — {pos}</div>\n'
        f'<div style="margin-top:8px;font-size:.78rem;color:var(--ink-3)">이 카드는 손으로 고치지 않는다 — 정본은 <code>brain/theses.json</code>이고, 경위는 <code>brain/routing.jsonl</code>과 아래 타임라인에 있다. 값의 분자·분모·기준일은 <code>brain/facts.json</code>.</div>\n'
        f"</div>\n</div></section>\n{END}")


# ═══ v3 (2026-09-15) — 시장 카드(brain/regime.json → index.html) · 포트 카드(brain/portfolio.json → tracker)
REGIME, PORTFOLIO = "brain/regime.json", "brain/portfolio.json"
MSTART, MEND = "<!-- brain:market:start -->", "<!-- brain:market:end -->"
PSTART, PEND = "<!-- brain:portfolio:start -->", "<!-- brain:portfolio:end -->"
BOX = "padding:18px 20px;border-left:4px solid #f97316;background:rgba(249,115,22,.06);line-height:1.75;font-size:.95rem;color:inherit"
SUB = "color:#8a94a6"


def render_market(rg):
    m, k, fl = rg["macro"], rg["market"], rg["flows"]
    nar = "".join(f'<li><b>{e(n["text"])}</b> <span style="{SUB}">— {e(n["since"])}부터 · 깨지면: {e(n["breaks_if"])} · {e(n.get("status",""))}</span></li>' for n in rg.get("narratives", []))
    chg = "".join(f"<li>{e(x)}</li>" for x in rg.get("changes_if", []))
    rot = rg.get("rotation", {})
    return (f"{MSTART}\n"
        f'<section id="market-now" style="max-width:1100px;margin:28px auto 0;padding:0 20px"><div data-brain-market style="{BOX}">\n'
        f'<div style="font-weight:900;font-size:1.15em;color:#f97316;margin-bottom:6px">▎지금 시장 · {e(rg["asof"]).replace("-", ".")} '
        f'<span style="font-size:.7em;font-weight:600;{SUB}">— 레짐 카드 · <code>brain/regime.json</code>에서 생성 {date.today().isoformat()}</span></div>\n'
        f'<b style="font-size:1.05em">{e(rg["one"])}</b>\n'
        f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px 18px;margin-top:12px">'
        f'<div><b>금리</b> — {e(m["rates"].get("state"))}<br><span style="{SUB}">10Y {m["rates"].get("us10y")}% · 2Y {m["rates"].get("us2y")}% · 30Y {m["rates"].get("us30y")}% · 다음 {e(m["rates"].get("next"))}</span></div>'
        f'<div><b>유가</b> — {e(m["oil"].get("state"))}<br><span style="{SUB}">브렌트 {m["oil"].get("brent")} ({e(m["oil"].get("asof"))}) · {e(m["oil"].get("physical") or m["oil"].get("premium_est") or "")}<br>종료 시: {e(m["oil"].get("baseline_if_ends") or "—")}<br>깨지면: {e(m["oil"].get("breaks_if"))}</span></div>'
        f'<div><b>가스</b> — {e(m["gas"].get("state"))}<br><span style="{SUB}">HH {m["gas"].get("hh")} · TTF {e(m["gas"].get("ttf"))} · JKM {e(m["gas"].get("jkm"))} · 전환 신호 {e(m["gas"].get("transition_signal"))}</span></div>'
        f'<div><b>한국</b> — {e(k["kr"].get("phase"))}<br><span style="{SUB}">코스피 {k["kr"].get("kospi")} · 고점({e((k["kr"].get("peak") or {}).get("date"))}) 대비 {k["kr"].get("drawdown_pct")}% · {e(k["kr"].get("breadth"))} · {e(k["kr"].get("valuation_proxy"))}</span></div>'
        f'<div><b>미국</b> — {e(k["us"].get("phase"))}<br><span style="{SUB}">S&P {k["us"].get("sp500")} · VIX {k["us"].get("vix")} · {e(k["us"].get("read"))}</span></div>'
        f'<div><b>수급</b> — 외국인 {e((fl.get("kr_foreign") or {}).get("net"))}<br><span style="{SUB}">{e((fl.get("kr_foreign") or {}).get("read"))} · 개인 {e((fl.get("kr_individual") or {}).get("net"))} · 환율 {(m.get("fx") or {}).get("usdkrw")}</span></div>'
        f'</div>\n'
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎시장이 지금 말하는 것</b><ul style="margin:6px 0 0 18px;padding:0">{nar}</ul></div>\n'
        f'<div style="margin-top:10px"><b>회전({e(rot.get("asof",""))})</b> — 오른 쪽 {e(" · ".join(rot.get("leaders_1d",[])[:4]))} / 내린 쪽 {e(" · ".join(rot.get("laggards_1d",[])[:4]))}<br><span style="{SUB}">{e(rot.get("read",""))}</span></div>\n'
        f'<div style="margin-top:12px;padding-top:10px;border-top:1px solid rgba(138,148,166,.35)"><b style="color:#f87171">▎이 레짐 판단이 틀렸음을 보여줄 것</b><ul style="margin:6px 0 0 18px;padding:0">{chg}</ul></div>\n'
        f'<div style="margin-top:8px;font-size:.78rem;{SUB}">이 카드는 손으로 고치지 않는다 — 정본 <code>brain/regime.json</code> · 값 <code>brain/facts.json#macro</code> · 인과 <code>brain/mechanisms.json</code>.</div>\n'
        f"</div></section>\n{MEND}")


def render_portfolio(pf):
    ex = pf["exposures"]; sc = pf["scenarios"]; sz = pf["sizing"]
    exr = "".join(f'<li><b>{e(kk)}</b> — {e(v.get("direction",""))}' + (f' <span style="{SUB}">({e(", ".join(v.get("names",[])[:5]))}{" · 주식의 %.0f%%" % (v["share_of_equity"]*100) if v.get("share_of_equity") else ""})</span>' if v.get("names") or v.get("share_of_equity") else "") + "</li>" for kk, v in ex.items())
    scr = "".join(f'<tr style="border-top:1px solid rgba(138,148,166,.35)"><td style="padding:6px 8px 6px 0;vertical-align:top"><b>{e(kk)}</b><br><span style="{SUB}">{e(v["trigger"])}</span></td><td style="padding:6px 8px;vertical-align:top">{e(v["book"])}</td><td style="padding:6px 8px;vertical-align:top">{e(v["hedge"])}</td><td style="padding:6px 0;vertical-align:top;{SUB}">{e(v["action"])}</td></tr>' for kk, v in sc.items())
    tb = "".join(f'<tr><td>{e(r["sym"])}</td><td style="text-align:right">{r["price"]:,}</td><td style="text-align:right">{sz["drawdown_at_falsifier"].get(r["sym"],0)*100:+.0f}%</td><td style="text-align:right">{r["position_krw"]/1e8:.2f}억</td><td style="text-align:right">{r["qty"]:,}주</td></tr>' for r in sz["table_1pct"])
    tr = "".join(f'<li><b>{t["n"]}회차 · {e(t["window"])}</b> — {e(", ".join(t["names"]))} <span style="{SUB}">({e(t["why"])})</span></li>' for t in pf["tranches"])
    pc = "".join(f'<li><b>{e(x["if"])}</b> → {e(x["then"])}</li>' for x in pf["precommits"])
    dc = "".join(f'<li>{e(d["date"])} — {e(d["what"])}</li>' for d in pf["decisions"])
    b = pf["base"]
    return (f"{PSTART}\n"
        f'<section id="portfolio-now"><div data-brain-portfolio style="{BOX};margin-bottom:18px">\n'
        f'<div style="font-weight:900;font-size:1.15em;color:#f97316;margin-bottom:6px">▎포트폴리오 테제 · {e(pf["asof"]).replace("-", ".")} '
        f'<span style="font-size:.7em;font-weight:600;{SUB}">— 포트 카드 · <code>brain/portfolio.json</code>에서 생성 {date.today().isoformat()} · 총자산 {b["total_assets"]/1e8:.2f}억 · 현금 {b["cash"]/1e8:.2f}억 · 시세 정의: {e(b["price_definition"])}</span></div>\n'
        f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px 24px">'
        f'<div><b style="color:#60a5fa">▎노출 — 무엇에 걸려 있나</b><ul style="margin:6px 0 0 18px;padding:0">{exr}</ul></div>'
        f'<div><b style="color:#60a5fa">▎헤지 지도</b><br>헤지가 되는 것: {e(", ".join(pf["hedge_map"]["hedges"]))}<br>헤지가 아닌 것: {e(", ".join(pf["hedge_map"]["not_hedges"]))}<br><span style="{SUB}">{e(pf["hedge_map"]["why"])}</span></div>'
        f'</div>\n'
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎시나리오 — 어느 쪽이 와도</b><table style="width:100%;border-collapse:collapse;font-size:.92em;margin-top:6px"><tr style="{SUB}"><th style="text-align:left">시나리오</th><th style="text-align:left">본진</th><th style="text-align:left">헤지</th><th style="text-align:left">행동</th></tr>{scr}</table></div>\n'
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎사이징 산술</b> — {e(sz["formula"])} · 변수 {e(sz["variable"])} · 낙폭 {e(sz["grade"])}'
        f'<table style="border-collapse:collapse;font-size:.92em;margin-top:6px"><tr style="{SUB}"><th style="text-align:left">종목</th><th>현가</th><th>반증 시 낙폭</th><th>허용 1%</th><th>수량</th></tr>{tb}</table><span style="{SUB}">{e(sz["note"])}</span></div>\n'
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎회차 — 판정 이벤트 경계</b><ul style="margin:6px 0 0 18px;padding:0">{tr}</ul></div>\n'
        f'<div style="margin-top:12px"><b style="color:#f87171">▎미리 적어 둔 뒤집기</b><ul style="margin:6px 0 0 18px;padding:0">{pc}</ul></div>\n'
        f'<div style="margin-top:12px"><b>투자자 결정</b><ul style="margin:6px 0 0 18px;padding:0">{dc}</ul></div>\n'
        f'<div style="margin-top:8px;font-size:.78rem;{SUB}">수량·비중·집행은 투자자가 정한다(§J3). 이 카드는 산술과 구조이며 정본은 <code>brain/portfolio.json</code>이다.</div>\n'
        f"</div></section>\n{PEND}")


def render_v3(check=False):
    out = []
    for src, page, fn, st, en in ((REGIME, "index.html", render_market, MSTART, MEND),
                                  (PORTFOLIO, "portfolio/portfolio_tracker.html", render_portfolio, PSTART, PEND)):
        try:
            doc = json.load(io.open(src, encoding="utf-8"))
            s = io.open(page, encoding="utf-8").read()
        except OSError:
            continue
        i, j = s.find(st), s.find(en)
        if i < 0 or j < 0:
            print(f"[cards] ⚠ 마커 없음 — {page} ({src})")
            continue
        new = fn(doc)
        norm = lambda x: re.sub(r"생성 \d{4}-\d{2}-\d{2}", "생성", x)
        if norm(s[i:j + len(en)]) == norm(new):
            continue
        if check:
            print(f"[cards] ⚠ 카드가 브레인과 다르다 — {page}"); out.append(page); continue
        io.open(page, "w", encoding="utf-8").write(s[:i] + new + s[j + len(en):])
        print(f"[cards] 카드 렌더 — {page}")
        out.append(page)
    return out


def main(argv):
    check = "--check" in argv
    only = set(a for a in argv[1:] if not a.startswith("--"))
    doc = json.load(io.open(THESES, encoding="utf-8"))
    changed, drift = [], []
    for path, pg in doc["pages"].items():
        if not pg.get("card") or (only and path not in only):
            continue
        try:
            s = io.open(path, encoding="utf-8").read()
        except OSError:
            continue
        i, j = s.find(START), s.find(END)
        if i < 0 or j < 0:
            print(f"[cards] ⚠ 마커 없음 — {path} (첫 전환은 마커를 넣어야 한다)")
            continue
        new = render(path, pg)
        cur = s[i:j + len(END)]
        # 생성일만 다른 경우는 드리프트로 보지 않는다
        norm = lambda x: re.sub(r"생성 \d{4}-\d{2}-\d{2}", "생성", x)
        if norm(cur) == norm(new):
            continue
        if check:
            drift.append(path)
            continue
        io.open(path, "w", encoding="utf-8").write(s[:i] + new + s[j + len(END):])
        changed.append(path)
    v3 = render_v3(check=check)
    if check:
        for p in drift:
            print(f"[cards] ⚠ 카드가 브레인과 다르다 — {p}")
        return 1 if (drift or v3) else 0
    for p in changed:
        print(f"[cards] 카드 렌더 — {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
