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
    if pg.get("card_theses"):  # W1: 카드는 5개 상한 — 테제가 6개 이상이면 card_theses 로 고른다
        th = [t for t in th if t.get("id") in pg["card_theses"]]
    cnt = {}
    for t in th:
        cnt[t.get("status", "유지")] = cnt.get(t.get("status", "유지"), 0) + 1
    cnt_s = " · ".join(f"{k} {v}" for k, v in cnt.items())
    # 쉬운 판(2026-09-26) — card_style:"easy" 페이지는 해요체 문장(claim_easy·one_easy)을 쓴다. 어미를 기계로 바꾸면 불규칙
    # 활용(지운다→지워요 · 안다→알아요)에서 틀리므로 문장을 브레인에 저장해 두고, 원문이 바뀌어 *_src 와 어긋나면 원문으로 돌아간다.
    easy = pg.get("card_style") == "easy"
    stale = []
    def txt(o, k):
        if easy and o.get(k + "_easy") and o.get(k + "_easy_src") == o.get(k):
            return o[k + "_easy"]
        if easy and o.get(k + "_easy"):
            stale.append(o.get("id", "한 문장"))
        return o.get(k)
    rows = []
    for t in th:
        st = t.get("status", "유지")
        rows.append(
            f'<tr style="border-top:1px solid var(--line)">'
            f'<td style="padding:10px 8px 10px 0;vertical-align:top;white-space:nowrap"><b>{e(t["id"])}</b><br>'
            f'<span style="font-family:var(--mono);font-size:.68rem;color:{COLOR.get(st, "var(--ink-2)")}">{e(st)}</span></td>'
            f'<td style="padding:10px 0;vertical-align:top"><b>{e(txt(t, "claim"))}</b>'
            + (f'<br><span style="color:var(--ink-2)">근거 — {e(t["basis"])}</span>' if t.get("basis") else "")
            + (f'<br><span style="color:var(--ink-2)">반증 — {e(t["falsifier"])}</span>' if t.get("falsifier") else "")
            + ((lambda lg: f'<br><span style="font-family:var(--mono);font-size:.68rem;color:var(--ink-3)">근거 log {len(lg)}건 · 최근 {lg[-1].get("date","")} {e(lg[-1].get("mark",""))} {e(lg[-1].get("text",""))[:90]}</span>' if lg else "")(t.get("log") or []))
            + (f'<br><span style="color:var(--ink-2)">판정 — {e(t["event"])}'
               + (f' · 마지막 검증 {e(t["last_tested"])}' if t.get("last_tested") else "") + "</span>" if t.get("event") else "")
            + "</td></tr>")
    one = txt(pg, "one")
    nxt = "".join(f"<br>· {e(x)}" for x in pg.get("next", []))
    label = (f'쉬운 판 · <code>brain/theses.json</code>에서 생성 {date.today().isoformat()} · 테제 {len(th)} ({cnt_s})'
             + (f' · ⚠ 원문이 바뀌어 쉬운 문장 대신 원문: {e(", ".join(stale))}' if stale else "")) if easy else \
            f'브레인 카드 · <code>brain/theses.json</code>에서 생성 {date.today().isoformat()} · 테제 {len(th)} ({cnt_s})'

    pos = e(pg.get("position") or "—")
    return (
        f"{START}\n"
        f'<section id="now" class="blk"><div class="wrap">\n'
        f'<div data-brain-card="{e(path)}" style="padding:18px 20px;border-left:4px solid var(--accent);background:rgba(249,115,22,.06);line-height:1.75">\n'
        f'<div style="font-weight:900;font-size:1.15em;color:var(--accent);margin-bottom:6px">▎현재 판단 · {d} '
        f'<span style="font-size:.7em;font-weight:600;color:var(--ink-3)">— {label}</span></div>\n'
        f'<b style="font-size:1.05em">{"한 문장으로 말하면" if easy else "한 문장"} — {e(one)}</b>\n'
        f'<table style="width:100%;border-collapse:collapse;font-size:.95rem;margin-top:12px">{"".join(rows)}</table>\n'
        f'<div id="falsify" style="margin-top:14px;padding-top:10px;border-top:1px solid var(--line)"><b style="color:#60a5fa">▎다음 검증 — 날짜가 아니라 이벤트</b>{nxt}</div>\n'
        f'<div style="margin-top:10px;color:var(--ink-2)"><b>포지션</b> — {pos}</div>\n'
        f'<div style="margin-top:8px;font-size:.78rem;color:var(--ink-3)">이 카드는 손으로 고치지 않는다 — 정본은 <code>brain/theses.json</code>이고, 경위는 <code>brain/routing.jsonl</code>과 아래 타임라인에 있다. 값의 분자·분모·기준일은 <code>brain/facts.json</code>.</div>\n'
        f"</div>\n</div></section>\n{END}")


# ═══ v3 (2026-09-15) — 시장 카드(brain/regime.json → index.html) · 포트 카드(brain/portfolio.json → tracker)
REGIME, PORTFOLIO = "brain/regime.json", "brain/portfolio.json"
MSTART, MEND = "<!-- brain:market:start -->", "<!-- brain:market:end -->"
PSTART, PEND = "<!-- brain:portfolio:start -->", "<!-- brain:portfolio:end -->"
HSTART, HEND = "  /* brain:holdings:start */", "  /* brain:holdings:end */"
PRICES = os.path.join(ROOT, "portfolio", "data", "prices.json") if "ROOT" in globals() else "portfolio/data/prices.json"
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
    # 2026-09-23 구조 변경 — 실보유 holdings_table 이 사이징 정본, 구 US 후보 표(table_1pct)는 sizing.candidates 로 보존.
    # 낙폭이 null 인 칸은 사용자 기입 대기라 0% 로 찍지 않고 「미기입」으로 둔다(값이 없는 것과 0 은 다르다).
    dd = lambda v: "미기입" if v is None else f"{(v * 100 if abs(v) <= 1 else v):+.0f}%"  # 필드명은 _pct 지만 값은 후보 표와 같은 비율(−0.2 = −20%)로 들어온다
    tb = "".join(f'<tr><td>{e(r.get("name"))}</td><td style="text-align:right">{dd(r.get("drawdown_at_falsifier_pct"))}</td><td style="{SUB}">{e(r.get("time_window_event"))}</td></tr>' for r in sz.get("holdings_table", []))
    cand = sz.get("candidates") or {}
    tc = "".join(f'<tr><td>{e(r["sym"])}</td><td style="text-align:right">{r["price"]:,}</td><td style="text-align:right">{cand.get("drawdown_at_falsifier", {}).get(r["sym"], 0)*100:+.0f}%</td><td style="text-align:right">{r["position_krw"]/1e8:.2f}억</td><td style="text-align:right">{r["qty"]:,}주</td></tr>' for r in cand.get("table_1pct", []))
    tr = "".join(f'<li><b>{t["n"]}회차 · {e(t["window"])}</b> — {e(", ".join(t["names"]))} <span style="{SUB}">({e(t["why"])})</span></li>' for t in pf["tranches"])
    pc = "".join(f'<li><b>{e(x.get("if") or x.get("trigger",""))}</b> → {e(x.get("then") or x.get("result",""))}</li>' for x in pf["precommits"])
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
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎사이징 산술</b> — {e(sz["formula"])} · 변수 {e(sz["variable"])}' + (f' · 낙폭 {e(sz["grade"])}' if sz.get("grade") else "") +
        f'<table style="border-collapse:collapse;font-size:.92em;margin-top:6px"><tr style="{SUB}"><th style="text-align:left">보유</th><th>반증 시 낙폭</th><th style="text-align:left">판정 창</th></tr>{tb}</table>'
        + (f'<table style="border-collapse:collapse;font-size:.92em;margin-top:6px"><tr style="{SUB}"><th style="text-align:left">후보</th><th>현가</th><th>반증 시 낙폭</th><th>허용 1%</th><th>수량</th></tr>{tc}</table>' if tc else "")
        + f'<span style="{SUB}">{e(sz.get("note"))}</span></div>\n'
        f'<div style="margin-top:12px"><b style="color:#60a5fa">▎회차 — 판정 이벤트 경계</b><ul style="margin:6px 0 0 18px;padding:0">{tr}</ul></div>\n'
        f'<div style="margin-top:12px"><b style="color:#f87171">▎미리 적어 둔 뒤집기</b><ul style="margin:6px 0 0 18px;padding:0">{pc}</ul></div>\n'
        f'<div style="margin-top:12px"><b>투자자 결정</b><ul style="margin:6px 0 0 18px;padding:0">{dc}</ul></div>\n'
        f'<div style="margin-top:8px;font-size:.78rem;{SUB}">수량·비중·집행은 투자자가 정한다(§J3). 이 카드는 산술과 구조이며 정본은 <code>brain/portfolio.json</code>이다.</div>\n'
        f"</div></section>\n{PEND}")


def render_holdings(pf):
    """트래커 <script> 안의 HOLDINGS·CASH_REMAINING 을 brain/portfolio.json 에서 찍는다(2026-09-17 C). JSON 객체는 그대로 JS 리터럴이다."""
    rows = ",\n    ".join(json.dumps(h, ensure_ascii=False) for h in pf.get("holdings", []))
    cash = pf.get("cash", {})
    if cash.get("value") is None:  # 현금은 사용자 값 — 비어 있으면 트래커 산술(NaN)을 깨지 않게 블록을 건드리지 않는다(2026-09-26)
        print(f"[cards] ⚠ portfolio.cash.value 없음({cash.get('grade', '')}) — 트래커 HOLDINGS·CASH 블록 렌더 건너뜀")
        return None
    return (f"{HSTART}\n  /* 정본 brain/portfolio.json → 훅 렌더. 매매는 portfolio.json 의 holdings·cash 에만 반영한다. */\n"
            f"  var HOLDINGS = [\n    {rows}\n  ];\n"
            f"  var CASH_REMAINING = {int(cash.get('value', 0))};  /* {cash.get('asof', '')} · {str(cash.get('note', ''))[:120]} */\n"
            f"{HEND}")


def check_positions(pf):
    """§J4 — 스톱·반증선 도달을 훅이 센다. prices.json 의 정규 종가로 보유 종목 손익과 스톱 거리를 찍는다."""
    try:
        px = json.load(io.open(PRICES, encoding="utf-8"))
    except OSError:
        return
    prices = px.get("prices", {})
    tot_cost = tot_val = 0
    for h in pf.get("holdings", []):
        key = h.get("priceKey") or h["name"]
        p = prices.get(key)
        if not p:
            continue
        tot_cost += h["totalCost"]; tot_val += p * h["qty"]
    if tot_cost:
        print(f"[positions] {px.get('updated', '')} 주식 {tot_val/1e8:.3f}억 (원가 대비 {(tot_val/tot_cost-1)*100:+.2f}%) · 현금 {(lambda c: '미기입' if c is None else f'{c/1e8:.2f}억')(pf.get('cash', {}).get('value'))}")
    for st in pf.get("stops", []):
        p = prices.get(st.get("priceKey") or st["name"])
        if not p or st.get("level") is None:  # 스톱 값은 사용자 몫 — 비어 있으면 거리를 못 잰다(watch.py 가 「값 없음」으로 알린다)
            continue
        d = (p / st["level"] - 1) * 100
        flag = "🔴 도달" if p <= st["level"] else ("🟠 10% 이내" if d < 10 else "✓")
        print(f"[positions] {st['name']} {st['kind']} {st['level']:,} vs {p:,.0f} → {d:+.1f}% {flag}")


def render_v3(check=False):
    out = []
    for src, page, fn, st, en in ((REGIME, "index.html", render_market, MSTART, MEND),
                                  (PORTFOLIO, "portfolio/portfolio_tracker.html", render_portfolio, PSTART, PEND),
                                  (PORTFOLIO, "portfolio/portfolio_tracker.html", render_holdings, HSTART, HEND)):
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
        if new is None:
            continue
        norm = lambda x: re.sub(r"생성 \d{4}-\d{2}-\d{2}", "생성", x)
        if norm(s[i:j + len(en)]) == norm(new):
            continue
        if check:
            print(f"[cards] ⚠ 카드가 브레인과 다르다 — {page}"); out.append(page); continue
        io.open(page, "w", encoding="utf-8").write(s[:i] + new + s[j + len(en):])
        print(f"[cards] 카드 렌더 — {page}")
        out.append(page)
    try:
        check_positions(json.load(io.open(PORTFOLIO, encoding="utf-8")))
    except (OSError, ValueError, KeyError) as e:
        print(f"[positions] ⚠ 검사 실패: {e}")
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
        # 카드 게이트(2026-09-17) — 근거·반증·판정 이벤트가 빈 테제가 있으면 카드를 찍지 않는다(빈 카드가 「현재 판단」으로 보이는 것을 막는다)
        gate = [(t.get("id"), k) for t in (pg.get("theses") or []) if (not pg.get("card_theses") or t.get("id") in pg["card_theses"]) for k in ("basis", "falsifier", "event") if not t.get(k)]
        if gate or not pg.get("one"):
            print(f"[cards] ⚠ 카드 게이트 — {path}: 빈 칸 {gate[:4]}{' · one 없음' if not pg.get('one') else ''} → 렌더 건너뜀")
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
