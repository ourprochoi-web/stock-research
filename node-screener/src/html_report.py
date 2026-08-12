"""Phase 3 — HTML 스코어보드 리포트 생성.

python3 cli.py report hbm 2026-07
python3 cli.py report ai_power 2026-07 --output-dir /path
"""

from __future__ import annotations

import json
from datetime import datetime
from html import escape as _e
from pathlib import Path

from .calibrate import leave_one_out, load_ground_truth, recall_at_k, resolve_gt_id
from .models import Graph
from .scoring import load_weights, score_companies, score_functions

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://ourprochoi-web.github.io/stock-research"

CHAIN_META = {
    "hbm": dict(
        display="HBM",
        title="HBM 밸류체인 병목 스코어보드",
        filename="node_screener_hbm_scoreboard.html",
        keywords="HBM,패키징,스코어보드,병목,밸류체인,SK하이닉스,TSMC,CoWoS,TC본딩,한미반도체",
    ),
    "ai_power": dict(
        display="AI 전력",
        title="AI 전력 밸류체인 병목 스코어보드",
        filename="node_screener_ai_power_scoreboard.html",
        keywords="AI전력,스코어보드,병목,밸류체인,변압기,가스터빈,송배전,데이터센터,SMR",
    ),
}


# ── 메인 ─────────────────────────────────────────────────────

def generate_scoreboard(
    graph: Graph, chain: str, year_month: str, output_dir: str | None = None,
) -> Path:
    """체인별 HTML 스코어보드 리포트 생성. 반환: 생성된 파일 경로."""
    if chain not in CHAIN_META:
        raise ValueError(f"미지원 체인: {chain}. 가능: {', '.join(CHAIN_META)}")

    meta = CHAIN_META[chain]
    weights = load_weights()
    fn_scores = score_functions(graph, weights)
    co_scores = score_companies(graph, fn_scores)
    gt = load_ground_truth(chain)

    fn_id_set = {r["fn_id"] for r in fn_scores}
    gt_fn_ids: set[str] = set()
    for g in gt:
        resolved = resolve_gt_id(g["id"], fn_id_set)
        if resolved:
            gt_fn_ids.add(resolved)

    recall = recall_at_k(fn_scores, gt) if gt else 0.0
    loo = leave_one_out(graph, gt, weights) if gt else []
    best_rarr = max(
        (r["rarr"]["rarr_ratio"] for r in fn_scores
         if r["rarr"].get("total_downstream", 0) > 0),
        default=0.0,
    )

    n_fn, n_co = len(fn_scores), len(co_scores)
    desc = (f"{meta['display']} 밸류체인 {n_fn}개 기능·{n_co}개 기업 "
            "5축 스코어링 병목 분석")
    url = f"{BASE_URL}/node-screener/{meta['filename']}"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    html = _assemble(
        meta=meta, desc=desc, url=url, year_month=year_month,
        fn_scores=fn_scores, co_scores=co_scores,
        gt_fn_ids=gt_fn_ids, gt=gt, loo=loo, recall=recall,
        best_rarr=best_rarr, n_fn=n_fn, n_co=n_co,
        n_edge=len(graph.edges), timestamp=now,
    )

    out = Path(output_dir) if output_dir else PROJECT_ROOT
    dest = out / meta["filename"]
    dest.write_text(html, encoding="utf-8")
    return dest


# ── 행 빌더 ──────────────────────────────────────────────────

def _fn_rows(fn_scores: list[dict], gt_fn_ids: set[str]) -> str:
    rows = []
    for r in fn_scores:
        gt = ' <span class="gt-badge">GT</span>' if r["fn_id"] in gt_fn_ids else ""
        rt = r["_ratios"]
        # RaRR 셀
        rarr = r.get("rarr", {})
        if rarr.get("total_downstream", 0) > 0:
            rv = rarr["rarr_ratio"]
            rc = "rarr-hi" if rv >= 0.5 else ("rarr-md" if rv >= 0.2 else "rarr-lo")
            rarr_td = f'<span class="{rc}">{rv:.0%}</span>'
        else:
            rarr_td = '<span class="rarr-lo">\u2014</span>'

        rows.append(
            f'<tr>'
            f'<td class="rk">{r["rank"]}</td>'
            f'<td><div class="fn-name">{_e(r["name"])}{gt}</div></td>'
            f'<td class="stage-tag">{_e(r["stage"])}</td>'
            f'<td class="axis-td"><div class="axis-bar" data-w="{rt["r1"]*100:.0f}"></div>'
            f'<span class="axis-val">{r["s1"]:.1f}</span></td>'
            f'<td class="axis-td"><div class="axis-bar" data-w="{rt["r2"]*100:.0f}"></div>'
            f'<span class="axis-val">{r["s2"]:.1f}</span></td>'
            f'<td class="axis-td"><div class="axis-bar" data-w="{rt["r3"]*100:.0f}"></div>'
            f'<span class="axis-val">{r["s3"]:.1f}</span></td>'
            f'<td class="axis-td"><div class="axis-bar" data-w="{rt["r4"]*100:.0f}"></div>'
            f'<span class="axis-val">{r["s4"]:.1f}</span></td>'
            f'<td class="axis-td"><div class="axis-bar penalty" data-w="{rt["r5"]*100:.0f}">'
            f'</div><span class="axis-val">{r["s5"]:.1f}</span></td>'
            f'<td class="total-val">{r["total"]:.1f}</td>'
            f'<td>{rarr_td}</td></tr>'
        )
    return "\n".join(rows)


def _co_rows(co_scores: list[dict], fn_scores: list[dict]) -> str:
    fn_map = {r["fn_id"]: r["name"] for r in fn_scores}
    rows = []
    for co in co_scores:
        tk = _e(co["ticker"]) if co.get("ticker") else "\u2014"
        top3 = co["contributing_fns"][:3]
        fns = (", ".join(_e(fn_map.get(f["fn"], f["fn"])) for f in top3)
               if top3 else "\u2014")
        rows.append(
            f'<tr><td class="rk">{co["rank"]}</td>'
            f'<td style="font-weight:750">{_e(co["name"])}</td>'
            f'<td class="tk">{tk}</td>'
            f'<td class="total-val">{co["score"]:.1f}</td>'
            f'<td class="contrib">{fns}</td></tr>'
        )
    return "\n".join(rows)


def _cal_html(gt: list, loo: list, recall: float) -> str:
    if not gt:
        return '<p style="color:var(--ink-2)">Ground truth 데이터 없음</p>'

    loo_p = sum(1 for lo in loo if lo["pass"])
    loo_t = len(loo)
    gate = recall >= 0.8 and loo_p == loo_t

    r_cls = "pass" if recall >= 0.8 else "fail"
    l_cls = "pass" if loo_p == loo_t else "fail"
    g_cls = "pass" if gate else "fail"
    g_txt = "PASS" if gate else "FAIL"

    cards = (
        '<div class="cal-grid">'
        f'<div class="cal-card"><div class="ck">Recall@20%</div>'
        f'<div class="cv {r_cls}">{recall:.0%}</div></div>'
        f'<div class="cal-card"><div class="ck">LOO 통과</div>'
        f'<div class="cv {l_cls}">{loo_p}/{loo_t}</div></div>'
        f'<div class="cal-card"><div class="ck">Gate 판정</div>'
        f'<div class="cv {g_cls}">{g_txt}</div></div></div>'
    )

    gt_rows = []
    for lo in loo:
        res = lo.get("resolved") or "\u2014"
        rk = str(lo["rank"]) if lo["rank"] is not None else "\u2014"
        rp = f'{lo["rank_pct"]:.0%}'
        pc = "ok" if lo["pass"] else "fail"
        pt = "PASS" if lo["pass"] else "FAIL"
        gt_rows.append(
            f'<tr><td style="font-weight:700">{_e(lo["left_out"])}</td>'
            f'<td class="tk">{_e(res)}</td>'
            f'<td style="text-align:center" class="mono">{rk}</td>'
            f'<td style="text-align:center" class="mono">{rp}</td>'
            f'<td style="text-align:center">'
            f'<span class="pass-tag {pc}">{pt}</span></td></tr>'
        )

    table = (
        '<div class="panel" style="margin-top:24px;overflow-x:auto">'
        '<h3 style="font-size:.92rem;font-weight:750;margin-bottom:16px">'
        'LOO 교차 검증 상세</h3>'
        '<table class="val-table"><thead><tr>'
        '<th>GT Node</th><th>Resolved</th><th>Rank</th><th>Rank%</th><th>Pass</th>'
        '</tr></thead><tbody>\n'
        + "\n".join(gt_rows)
        + '\n</tbody></table></div>'
    )

    return cards + "\n" + table


def _stage_cards(fn_scores: list[dict]) -> str:
    groups: dict[str, list] = {}
    for r in fn_scores:
        groups.setdefault(r["stage"], []).append(r)

    sorted_groups = sorted(
        groups.items(),
        key=lambda x: -sum(r["total"] for r in x[1]) / len(x[1]),
    )
    top_k = max(1, int(len(fn_scores) * 0.2))

    cards = []
    for i, (stage, fns) in enumerate(sorted_groups, 1):
        avg = sum(r["total"] for r in fns) / len(fns)
        fns_sorted = sorted(fns, key=lambda x: -x["total"])
        tags = []
        for fn in fns_sorted:
            hi = " hi" if fn["rank"] <= top_k else ""
            tags.append(
                f'<span class="stage-fn{hi}">'
                f'{_e(fn["name"])} ({fn["total"]:.0f})</span>'
            )
        dl = min(i, 3)
        cards.append(
            f'<div class="stage-card reveal d{dl}">'
            f'<div class="stage-num">Stage {i:02d} \u00b7 {len(fns)}개 기능</div>'
            f'<div class="stage-title">{_e(stage)}</div>'
            f'<div class="stage-avg">평균 점수 {avg:.1f}</div>'
            f'<div class="stage-fns">{"".join(tags)}</div></div>'
        )

    return '<div class="stage-grid">\n' + "\n".join(cards) + "\n</div>"


# ── 정적 자산 ────────────────────────────────────────────────

_CSS = """\
:root{
  --bg:#080B14;--bg-2:#0C1120;--surface:#121A2E;--surface-2:#16203A;
  --line:#23304D;--ink:#EAEFFA;--ink-2:#9DA9C2;--ink-3:#5E6B86;
  --accent:#D4A843;--accent-2:#FFB13E;--glow:#38E6D4;
  --bull:#48D597;--bear:#FF6B6B;
  --mono:'JetBrains Mono',ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  --sans:'Pretendard','Pretendard Variable',-apple-system,BlinkMacSystemFont,system-ui,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px}
.mono{font-family:var(--mono)}

/* NAV */
nav{position:sticky;top:0;z-index:50;background:rgba(8,11,20,.72);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;height:60px}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:-.02em;font-size:.95rem}
.brand .dot{width:9px;height:9px;border-radius:50%;background:var(--accent);box-shadow:0 0 12px var(--accent)}
.nav-links{display:flex;gap:4px}
.nav-links a{font-family:var(--mono);font-size:.74rem;letter-spacing:.04em;color:var(--ink-2);padding:8px 12px;border-radius:7px;transition:.2s}
.nav-links a:hover,.nav-links a.active{color:var(--ink);background:var(--surface)}
.nav-toggle{display:none;flex-direction:column;gap:5px;background:none;border:1px solid var(--line);border-radius:8px;padding:8px 10px;cursor:pointer}
.nav-toggle span{display:block;width:20px;height:2px;background:var(--ink-2);border-radius:2px}

/* HERO */
.hero{position:relative;min-height:80vh;display:flex;align-items:center;overflow:hidden}
.hero-bg{position:absolute;inset:0;z-index:0}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:64px 64px;-webkit-mask-image:radial-gradient(120% 90% at 70% 30%,#000 0%,transparent 72%);mask-image:radial-gradient(120% 90% at 70% 30%,#000 0%,transparent 72%);opacity:.45}
.glow-a{position:absolute;width:760px;height:760px;border-radius:50%;filter:blur(120px);opacity:.45;background:radial-gradient(circle,var(--accent),transparent 62%);top:-200px;right:-160px;animation:float 14s ease-in-out infinite}
.glow-b{position:absolute;width:560px;height:560px;border-radius:50%;filter:blur(120px);opacity:.28;background:radial-gradient(circle,var(--accent-2),transparent 62%);bottom:-180px;left:-120px;animation:float 18s ease-in-out infinite reverse}
@keyframes float{0%,100%{transform:translate(0,0)}50%{transform:translate(-30px,40px)}}
.spark{position:absolute;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--glow),transparent);opacity:0;animation:sweep 5.5s linear infinite}
.spark:nth-child(4){top:30%;animation-delay:0s}.spark:nth-child(5){top:58%;animation-delay:1.8s}.spark:nth-child(6){top:74%;animation-delay:3.4s}
@keyframes sweep{0%{transform:translateX(-100%);opacity:0}8%{opacity:.7}50%{opacity:.7}100%{transform:translateX(100%);opacity:0}}
.hero-in{position:relative;z-index:2;padding:120px 0 80px}
.eyebrow{display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--accent);border:1px solid var(--line);padding:7px 14px;border-radius:100px;background:rgba(212,168,67,.06);margin-bottom:28px}
.eyebrow::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--accent);box-shadow:0 0 8px var(--accent)}
h1.hero-title{font-size:clamp(2.5rem,6.4vw,4.9rem);font-weight:900;line-height:1.04;letter-spacing:-.035em;max-width:16ch}
h1.hero-title .hl{background:linear-gradient(105deg,var(--accent),var(--glow) 55%,var(--accent-2));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.hero-sub{margin-top:26px;font-size:clamp(1rem,1.6vw,1.22rem);color:var(--ink-2);max-width:56ch;font-weight:400}
.hero-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;margin-top:56px;background:var(--line);border:1px solid var(--line);border-radius:16px;overflow:hidden}
.hstat{background:var(--bg-2);padding:26px 22px}
.hstat .num{font-family:var(--mono);font-weight:800;font-size:clamp(1.5rem,3vw,2.15rem);letter-spacing:-.02em}
.hstat .num .u{color:var(--accent);font-size:.62em}
.hstat .lab{margin-top:8px;font-size:.82rem;color:var(--ink-2)}
.scroll-cue{margin-top:54px;display:flex;align-items:center;gap:10px;font-family:var(--mono);font-size:.72rem;color:var(--ink-3);letter-spacing:.1em}
.scroll-cue .bar{width:30px;height:1px;background:var(--ink-3);position:relative;overflow:hidden}
.scroll-cue .bar::after{content:"";position:absolute;inset:0;background:var(--accent);animation:loadbar 2.4s ease-in-out infinite}
@keyframes loadbar{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}

/* SECTIONS */
section.blk{padding:108px 0;scroll-margin-top:60px}
.sec-head{margin-bottom:52px;max-width:60ch}
.sec-eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);display:flex;align-items:center;gap:12px}
.sec-eyebrow .idx{color:var(--ink-3)}.sec-eyebrow .ln{flex:0 0 40px;height:1px;background:var(--line)}
h2.sec-title{font-size:clamp(1.8rem,3.6vw,2.7rem);font-weight:850;letter-spacing:-.03em;margin-top:18px;line-height:1.12}
.sec-lead{margin-top:18px;color:var(--ink-2);font-size:1.04rem;max-width:62ch}
.divider{height:1px;background:linear-gradient(90deg,var(--line),transparent)}

/* PANEL / TABLE */
.panel{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:30px}
.val-table{width:100%;border-collapse:collapse}
.val-table th{font-family:var(--mono);font-size:.68rem;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);padding:10px 14px;text-align:left;border-bottom:1px solid var(--line);background:var(--bg-2);white-space:nowrap}
.val-table td{padding:11px 14px;font-size:.84rem;border-bottom:1px solid rgba(35,48,77,.6);vertical-align:middle}
.val-table tr:last-child td{border-bottom:none}
.val-table tr:hover td{background:rgba(212,168,67,.04)}
.val-table .fn-name{font-weight:750;color:var(--ink);display:flex;align-items:center;gap:8px;white-space:nowrap}
.val-table .stage-tag{font-family:var(--mono);font-size:.66rem;color:var(--ink-3);max-width:160px}
.val-table .rk{text-align:center;font-family:var(--mono);font-weight:700;color:var(--ink-3)}
.val-table .tk{font-family:var(--mono);font-size:.74rem;color:var(--ink-3)}
.val-table .contrib{font-size:.78rem;color:var(--ink-2);max-width:260px}
.total-val{font-family:var(--mono);font-weight:800;font-size:.92rem;color:var(--ink)}

/* AXIS MINI-BAR */
.axis-td{min-width:68px}
.axis-bar{height:4px;border-radius:2px;background:linear-gradient(90deg,var(--accent),var(--accent-2));width:0;transition:width .8s cubic-bezier(.2,.8,.2,1);margin-bottom:3px}
.axis-bar.penalty{background:var(--bear)}
.axis-val{font-family:var(--mono);font-size:.74rem;font-weight:600}

/* GT BADGE */
.gt-badge{display:inline-flex;align-items:center;font-family:var(--mono);font-size:.58rem;font-weight:700;letter-spacing:.06em;color:var(--accent);background:rgba(212,168,67,.12);border:1px solid rgba(212,168,67,.35);border-radius:4px;padding:2px 5px;text-transform:uppercase}

/* RARR */
.rarr-hi{color:var(--bear);font-weight:700}
.rarr-md{color:var(--accent);font-weight:700}
.rarr-lo{color:var(--ink-3)}

/* STAGE CARDS */
.stage-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px;margin-top:8px}
.stage-card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:24px;position:relative;overflow:hidden}
.stage-card::before{content:"";position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,var(--accent),transparent)}
.stage-num{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin-bottom:10px}
.stage-title{font-size:1.05rem;font-weight:800;letter-spacing:-.02em;margin-bottom:14px}
.stage-avg{font-family:var(--mono);font-size:.82rem;color:var(--ink-2);margin-bottom:14px}
.stage-fns{display:flex;flex-wrap:wrap;gap:6px}
.stage-fn{font-family:var(--mono);font-size:.68rem;padding:4px 9px;border-radius:6px;border:1px solid var(--line);color:var(--ink-2);background:var(--bg-2)}
.stage-fn.hi{color:var(--accent);border-color:rgba(212,168,67,.3);background:rgba(212,168,67,.06)}

/* CALIBRATION */
.cal-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.cal-card{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:24px}
.cal-card .ck{font-family:var(--mono);font-size:.72rem;color:var(--ink-3);letter-spacing:.04em;text-transform:uppercase}
.cal-card .cv{font-family:var(--mono);font-weight:800;font-size:1.8rem;margin-top:8px;letter-spacing:-.02em}
.cal-card .cv.pass{color:var(--bull)}
.cal-card .cv.fail{color:var(--bear)}
.pass-tag{display:inline-block;font-family:var(--mono);font-size:.68rem;font-weight:700;padding:3px 8px;border-radius:5px}
.pass-tag.ok{color:var(--bull);background:rgba(72,213,151,.12);border:1px solid rgba(72,213,151,.3)}
.pass-tag.fail{color:var(--bear);background:rgba(255,107,107,.12);border:1px solid rgba(255,107,107,.3)}

/* REVEAL */
.reveal{opacity:0;transform:translateY(26px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.reveal.in{opacity:1;transform:none}
.reveal.d1{transition-delay:.08s}.reveal.d2{transition-delay:.16s}.reveal.d3{transition-delay:.24s}

/* FOOTER */
footer{border-top:1px solid var(--line);padding:48px 0 64px;margin-top:40px}
.disc-foot{font-size:.78rem;color:var(--ink-3);max-width:62ch;line-height:1.65}
.foot-brand{font-weight:800;letter-spacing:-.02em;font-size:1rem;margin-bottom:12px}
.foot-ts{margin-top:16px;font-family:var(--mono);font-size:.68rem;color:var(--ink-3)}

/* RESPONSIVE */
@media(max-width:860px){
  .nav-toggle{display:flex}
  .nav-links{display:none;position:absolute;top:60px;left:0;right:0;background:rgba(8,11,20,.96);backdrop-filter:blur(14px);border-bottom:1px solid var(--line);flex-direction:column;padding:12px 24px 20px;gap:0}
  .nav-links.open{display:flex}
  .nav-links a{padding:12px 0;border-radius:0;border-bottom:1px solid var(--line);font-size:.82rem}
  .hero-stats,.cal-grid{grid-template-columns:1fr}
  .stage-grid{grid-template-columns:1fr}
  .val-table th,.val-table td{padding:8px 8px;font-size:.76rem}
  .axis-td{min-width:55px}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}}"""

_JS = """\
(function(){
  var obs=new IntersectionObserver(function(ee){
    ee.forEach(function(e){
      if(e.isIntersecting){e.target.classList.add('in');obs.unobserve(e.target)}
    });
  },{threshold:.12});
  document.querySelectorAll('.reveal').forEach(function(el){obs.observe(el)});

  var barObs=new IntersectionObserver(function(ee){
    ee.forEach(function(e){
      if(e.isIntersecting){
        e.target.querySelectorAll('.axis-bar').forEach(function(b){
          b.style.width=b.getAttribute('data-w')+'%';
        });
        barObs.unobserve(e.target);
      }
    });
  },{threshold:.05});
  document.querySelectorAll('.score-table').forEach(function(el){barObs.observe(el)});

  var secs=document.querySelectorAll('section.blk');
  var navAs=document.querySelectorAll('.nav-links a');
  window.addEventListener('scroll',function(){
    var y=window.scrollY+120;
    secs.forEach(function(s,i){
      if(s.offsetTop<=y&&s.offsetTop+s.offsetHeight>y){
        navAs.forEach(function(a){a.classList.remove('active')});
        if(navAs[i])navAs[i].classList.add('active');
      }
    });
  });

  var btn=document.getElementById('navToggle');
  var lnk=document.querySelector('.nav-links');
  if(btn&&lnk){
    btn.addEventListener('click',function(){lnk.classList.toggle('open')});
    lnk.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click',function(){lnk.classList.remove('open')});
    });
  }
})();"""


# ── 조립 ─────────────────────────────────────────────────────

def _assemble(*, meta, desc, url, year_month,
              fn_scores, co_scores, gt_fn_ids, gt, loo, recall,
              best_rarr, n_fn, n_co, n_edge, timestamp):
    ym = year_month.replace("-", ".")
    recall_i = int(recall * 100)
    rarr_i = int(best_rarr * 100)

    json_ld = json.dumps({
        "@context": "https://schema.org", "@type": "Article",
        "headline": meta["title"], "description": desc,
        "datePublished": f"{year_month}-27",
        "dateModified": f"{year_month}-27",
        "author": {"@type": "Person", "name": "ourprochoi"},
        "publisher": {"@type": "Organization",
                      "name": "ourprochoi Research Archive"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
    }, ensure_ascii=False, indent=2)

    fn_rows_html = _fn_rows(fn_scores, gt_fn_ids)
    co_rows_html = _co_rows(co_scores, fn_scores)
    cal_section = _cal_html(gt, loo, recall)
    stage_section = _stage_cards(fn_scores)

    disp = _e(meta["display"])
    title_e = _e(meta["title"])
    desc_e = _e(desc)
    kw_e = _e(meta["keywords"])

    head = "\n".join([
        "<!DOCTYPE html>",
        '<html lang="ko">',
        "<head>",
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">',
        '<meta name="robots" content="index,follow">',
        f'<meta name="description" content="{desc_e}">',
        f'<meta name="keywords" content="{kw_e}">',
        f'<meta property="og:title" content="{title_e}">',
        f'<meta property="og:description" content="{desc_e}">',
        '<meta property="og:type" content="article">',
        f'<meta property="og:url" content="{url}">',
        '<meta property="og:locale" content="ko_KR">',
        '<meta property="og:site_name" content="ourprochoi Research Archive">',
        '<meta name="twitter:card" content="summary">',
        f'<meta name="twitter:title" content="{title_e}">',
        f'<meta name="twitter:description" content="{desc_e}">',
        f'<link rel="canonical" href="{url}">',
        f'<title>{title_e} — ourprochoi Research</title>',
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/'
        'pretendard@v1.3.9/dist/web/static/pretendard.min.css">',
        "<style>", _CSS, "</style>",
        '<script type="application/ld+json">', json_ld, "</script>",
        "</head>",
    ])

    body = _body(
        disp=meta["display"], ym=ym,
        n_fn=n_fn, n_co=n_co, n_edge=n_edge,
        recall_i=recall_i, rarr_i=rarr_i,
        fn_rows_html=fn_rows_html, co_rows_html=co_rows_html,
        cal_section=cal_section, stage_section=stage_section,
        timestamp=timestamp,
    )

    return (head + "\n<body>\n" + body
            + "\n<script>\n" + _JS + "\n</script>\n</body>\n</html>")


def _body(*, disp, ym, n_fn, n_co, n_edge,
          recall_i, rarr_i, fn_rows_html, co_rows_html,
          cal_section, stage_section, timestamp):
    return f"""\
<a href="../" style="position:fixed;top:20px;left:20px;z-index:9999;display:flex;align-items:center;gap:6px;padding:8px 16px 8px 12px;background:rgba(15,19,34,.85);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.12);border-radius:999px;color:#a5b4fc;text-decoration:none;font-family:Pretendard,sans-serif;font-size:13px;font-weight:600;transition:all .2s"><svg width="14" height="14" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Home</a>

<nav><div class="wrap nav-in">
<div class="brand"><span class="dot"></span>노드 스크리너 &middot; {_e(disp)}</div>
<button class="nav-toggle" id="navToggle" aria-label="메뉴"><span></span><span></span><span></span></button>
<div class="nav-links">
<a href="#fn-rank">01 / 기능</a>
<a href="#co-rank">02 / 기업</a>
<a href="#cal">03 / 검증</a>
<a href="#stages">04 / 단계</a>
</div></div></nav>

<header class="hero"><div class="hero-bg">
<div class="hero-grid"></div><div class="glow-a"></div><div class="glow-b"></div>
<div class="spark"></div><div class="spark"></div><div class="spark"></div>
</div><div class="wrap hero-in">
<span class="eyebrow">노드 스크리너 &middot; {_e(disp)} &middot; {ym}</span>
<h1 class="hero-title">병목<br><span class="hl">스코어보드</span></h1>
<p class="hero-sub">{_e(disp)} 밸류체인 {n_fn}개 기능 노드를 5축 스코어링으로 분석한 불가결 병목 랭킹</p>
<div class="hero-stats">
<div class="hstat"><div class="num">{n_fn}<span class="u">개</span></div><div class="lab">Function 노드</div></div>
<div class="hstat"><div class="num">{recall_i}<span class="u">%</span></div><div class="lab">Recall@20%</div></div>
<div class="hstat"><div class="num">{rarr_i}<span class="u">%</span></div><div class="lab">최고 RaRR</div></div>
</div>
<div class="scroll-cue"><div class="bar"></div>SCROLL</div>
</div></header>

<section id="fn-rank" class="blk"><div class="wrap">
<div class="sec-head reveal">
<div class="sec-eyebrow"><span class="idx">01</span><span class="ln"></span>FUNCTION RANKING</div>
<h2 class="sec-title">기능별 병목 점수</h2>
<p class="sec-lead">S1 구조 &middot; S2 대체 장벽 &middot; S3 경제성 &middot; S4 수요 내구성 &middot; S5 감점을 합산한 종합 스코어. GT 노드는 <span class="gt-badge">GT</span> 배지 표시.</p>
</div>
<div class="panel reveal d1" style="overflow-x:auto">
<table class="val-table score-table"><thead><tr>
<th style="text-align:center">#</th><th>Function</th><th>Stage</th>
<th>S1 구조</th><th>S2 장벽</th><th>S3 경제</th><th>S4 수요</th>
<th>S5 감점</th><th>Total</th><th>RaRR</th>
</tr></thead><tbody>
{fn_rows_html}
</tbody></table></div>
<p style="margin-top:16px;font-size:.82rem;color:var(--ink-3)">총 {n_fn}개 function &middot; {n_co}개 company &middot; {n_edge}개 edge</p>
</div></section>

<div class="wrap"><div class="divider"></div></div>

<section id="co-rank" class="blk"><div class="wrap">
<div class="sec-head reveal">
<div class="sec-eyebrow"><span class="idx">02</span><span class="ln"></span>COMPANY RANKING</div>
<h2 class="sec-title">기업별 스코어</h2>
<p class="sec-lead">기업이 수행하는 기능(function)의 점수를 점유율(share) 가중 평균하여 배분.</p>
</div>
<div class="panel reveal d1" style="overflow-x:auto">
<table class="val-table"><thead><tr>
<th style="text-align:center">#</th><th>Company</th><th>Ticker</th>
<th>Score</th><th>기여 Functions (Top 3)</th>
</tr></thead><tbody>
{co_rows_html}
</tbody></table></div>
</div></section>

<div class="wrap"><div class="divider"></div></div>

<section id="cal" class="blk"><div class="wrap">
<div class="sec-head reveal">
<div class="sec-eyebrow"><span class="idx">03</span><span class="ln"></span>CALIBRATION</div>
<h2 class="sec-title">캘리브레이션 검증</h2>
<p class="sec-lead">Ground Truth 정답 노드의 랭크 위치와 Leave-One-Out 교차 검증 결과.</p>
</div>
<div class="reveal d1">
{cal_section}
</div>
</div></section>

<div class="wrap"><div class="divider"></div></div>

<section id="stages" class="blk"><div class="wrap">
<div class="sec-head reveal">
<div class="sec-eyebrow"><span class="idx">04</span><span class="ln"></span>STAGE DISTRIBUTION</div>
<h2 class="sec-title">단계별 병목 분포</h2>
<p class="sec-lead">밸류체인 공정 단계별 기능 그룹핑. 상위 20% 기능은 골드 태그.</p>
</div>
<div class="reveal d1">
{stage_section}
</div>
</div></section>

<footer><div class="wrap">
<div class="foot-brand">ourprochoi Research</div>
<p class="disc-foot">본 보고서는 투자 권유가 아닌 연구 목적의 자료입니다. 포함된 정보의 정확성이나 완전성을 보장하지 않으며, 투자 의사결정의 책임은 투자자 본인에게 있습니다.</p>
<p class="foot-ts">데이터: 밸류체인 그래프 + ground_truth.yaml &middot; 생성: {timestamp} &middot; 노드 스크리너 v1.0</p>
</div></footer>"""
