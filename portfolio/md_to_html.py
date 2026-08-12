#!/usr/bin/env python3
"""Markdown → 사이트 디자인 HTML 변환 (Pretendard, card layout, hero, nav, print-ready)"""

import markdown
import re
import os
import sys

# ─── 문서별 메타데이터 ───
META = {
    "portfolio_recommendation_202607": {
        "eyebrow": "PORTFOLIO STRATEGY",
        "title": "금융기관용 주식 포트폴리오 추천안",
        "version": "v3",
        "lede": "밸류에이션 4차원 분석 · 4인 에이전트 토론 · 3건 딥다이브 · 6개 클러스터 포트폴리오",
        "stats": [
            ("10~20억", "투자 규모"),
            ("코어 40%", "위성 20% · 현금 40%"),
            ("12종목", "6개 클러스터"),
        ],
        "color": "#1b4965",
        "accent": "#2e8b57",
    },
    "etf_study_hybrid_portfolio_202607": {
        "eyebrow": "ETF STUDY & HYBRID PORTFOLIO",
        "title": "ETF 스터디 & 하이브리드 포트폴리오",
        "version": "v4",
        "lede": "테마별 ETF 심층 비교 · TIMEFOLIO 액티브 분석 · AGIX 심층 분석 · 개별 4종목 + ETF 7종 하이브리드",
        "stats": [
            ("10~20억", "투자 규모"),
            ("개별 20%", "ETF 40% · 현금 40%"),
            ("130+종목", "실질 분산 노출"),
        ],
        "color": "#2e6b8a",
        "accent": "#c79a2f",
    },
}

CSS = r"""
:root{
  --ink:#19212b; --sub:#566270; --faint:#909aa6;
  --bg:#f0ede7; --card:#ffffff; --line:#d8dbd1; --note:#ebe8e0; --chip-bg:#e4e6dc;
  --gold:#c79a2f; --golds:#f7f0db; --gold-line:#e8d5a0;
  --navy:#1c2a3e;
  --up:#1d7a59; --ups:#e3f2ec;
  --down:#bd442d; --downs:#f8e9e5;
  --caution:#b3801f; --cautions:#f5edd5;
  --blue:#37588a; --blues:#e7eef7;
  --steel:#3c5167; --steels:#e8edf2;
  --accent:ACCENT_PLACEHOLDER;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Pretendard',-apple-system,'Apple SD Gothic Neo',sans-serif;background:var(--bg);color:var(--ink);font-size:16.5px;line-height:1.78;-webkit-font-smoothing:antialiased;overflow-x:hidden}

/* ═══ PROGRESS BAR ═══ */
#prog{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--gold),var(--up),var(--blue),var(--gold));width:0%;z-index:99;transition:width .15s}

/* ═══ NAV ═══ */
nav{position:sticky;top:0;background:rgba(240,237,231,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);z-index:90;padding:10px 16px;display:flex;gap:8px;overflow-x:auto;-webkit-overflow-scrolling:touch}
nav a{flex:none;font-size:12.5px;font-weight:700;color:var(--sub);text-decoration:none;padding:6px 13px;border:1px solid var(--line);border-radius:999px;background:var(--card);white-space:nowrap;transition:all .2s}
nav a:hover{background:var(--chip-bg);color:var(--ink)}

/* ═══ WRAP ═══ */
.wrap{max-width:820px;margin:0 auto;padding:0 20px 100px}

/* ═══ HERO ═══ */
.hero-shell{background:linear-gradient(170deg,#1a1f2e 0%,COLOR_PLACEHOLDER 40%,#162232 100%);color:#eef2f6;position:relative;overflow:hidden}
.hero-shell::before{content:'';position:absolute;inset:0;opacity:.35;background-image:
  repeating-linear-gradient(0deg, transparent 0 48px, rgba(199,154,47,.07) 48px 49px),
  repeating-linear-gradient(90deg, transparent 0 48px, rgba(199,154,47,.07) 48px 49px);pointer-events:none}
.hero-shell::after{content:'';position:absolute;bottom:0;left:0;right:0;height:200px;background:linear-gradient(to top,rgba(22,34,50,.9),transparent);pointer-events:none}
.hero{position:relative;max-width:820px;margin:0 auto;padding:74px 20px 36px;text-align:center;z-index:1}
.hero .eyebrow{font-size:12px;letter-spacing:.28em;color:var(--gold);font-weight:800}
.hero .version{display:inline-block;background:var(--gold);color:#1a1f2e;font-size:11px;font-weight:900;padding:3px 10px;border-radius:999px;margin-left:8px;letter-spacing:.05em}
.hero h1{font-size:clamp(28px,6.8vw,46px);font-weight:900;letter-spacing:-.03em;line-height:1.16;margin:16px 0 14px;
  background:linear-gradient(110deg,#fff 20%,#e7c77e 50%,#fff 80%);-webkit-background-clip:text;background-clip:text;color:transparent;background-size:200% 100%;animation:shine 6s linear infinite}
@keyframes shine{to{background-position:-200% 0}}
.hero p.lede{color:#9aa8b8;max-width:660px;margin:0 auto;font-size:15.5px}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:660px;margin:34px auto 0}
.stat{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.10);border-radius:16px;padding:16px 8px;backdrop-filter:blur(4px)}
.stat .n{font-size:clamp(18px,4.6vw,28px);font-weight:900;color:#e7c77e;letter-spacing:-.02em}
.stat .l{font-size:11.5px;color:#8a96a6;margin-top:5px;line-height:1.45}

/* ═══ CONTENT SECTIONS ═══ */
section{padding-top:10px}
.zone-head{margin:58px 0 6px;position:relative}
.zone-head h2{font-size:clamp(22px,5vw,30px);font-weight:900;letter-spacing:-.02em;margin-top:6px;color:var(--ink);border-bottom:2px solid var(--accent);padding-bottom:8px}

.floor{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:28px 26px;margin:22px 0;opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s ease,box-shadow .3s ease}
.floor.visible{opacity:1;transform:none}
@media(hover:hover){.floor:hover{box-shadow:0 14px 38px -20px rgba(25,33,43,.25)}}

/* ═══ HEADINGS inside cards ═══ */
.content-body h2{font-size:clamp(22px,5vw,30px);font-weight:900;letter-spacing:-.02em;color:var(--ink);border-bottom:2px solid var(--accent);padding-bottom:8px;margin:58px 0 14px}
.content-body h3{font-size:18.5px;font-weight:800;color:var(--navy);margin:32px 0 10px;padding-left:14px;border-left:4px solid var(--accent)}
.content-body h4{font-size:16px;font-weight:700;color:var(--steel);margin:22px 0 8px}

/* ═══ TABLES ═══ */
.table-wrap{overflow-x:auto;margin:14px 0;border-radius:14px;border:1px solid var(--line);background:var(--card)}
table{width:100%;border-collapse:collapse;font-size:13.3px}
th{background:var(--ink);color:#fff;font-size:11.5px;letter-spacing:.06em;padding:10px 12px;text-align:left;font-weight:700;white-space:nowrap}
td{padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top;font-size:13px}
tr:last-child td{border-bottom:none}
tr:nth-child(even) td{background:#f8f8f5}
td:first-child{font-weight:700;white-space:nowrap}
td strong{color:var(--up)}

/* ═══ BLOCKQUOTE ═══ */
blockquote{border-left:4px solid var(--accent);margin:16px 0;padding:12px 18px;background:var(--note);border-radius:0 12px 12px 0;font-size:15px;color:var(--sub)}
blockquote strong{color:var(--ink)}

/* ═══ LISTS ═══ */
ul,ol{margin:8px 0;padding-left:24px}
li{margin:4px 0;font-size:15.5px;line-height:1.7}
li strong{color:var(--ink)}

/* ═══ CODE ═══ */
code{font-family:'SF Mono',Menlo,monospace;font-size:13px;background:var(--chip-bg);padding:2px 6px;border-radius:5px}
pre{background:#f6f8fa;border:1px solid var(--line);border-radius:12px;padding:14px;font-size:12px;overflow-x:auto;margin:12px 0}

/* ═══ HR ═══ */
hr{border:none;border-top:1px solid var(--line);margin:36px 0}

/* ═══ LINKS ═══ */
a{color:var(--blue);text-decoration:none;font-weight:600}
a:hover{text-decoration:underline}

/* ═══ BADGES ═══ */
.tag-up{display:inline-block;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:6px;background:var(--ups);color:var(--up)}
.tag-dn{display:inline-block;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:6px;background:var(--downs);color:var(--down)}
.tag-ca{display:inline-block;font-size:10.5px;font-weight:800;padding:2px 8px;border-radius:6px;background:var(--cautions);color:var(--caution)}

/* ═══ BACK TO TOP ═══ */
.btt{position:fixed;bottom:28px;right:28px;width:46px;height:46px;border-radius:50%;background:var(--ink);color:#fff;border:none;cursor:pointer;font-size:20px;box-shadow:0 4px 16px rgba(0,0,0,.2);opacity:0;transition:opacity .3s;z-index:80;display:flex;align-items:center;justify-content:center}
.btt.show{opacity:1}

/* ═══ FOOTER ═══ */
.site-footer{text-align:center;padding:40px 20px;font-size:13px;color:var(--faint);border-top:1px solid var(--line);margin-top:60px}

/* ═══ PRINT ═══ */
@media print{
  body{background:#fff;font-size:10pt}
  .hero-shell{background:#1c2a3e!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  nav,#prog,.btt{display:none!important}
  .floor{opacity:1!important;transform:none!important;box-shadow:none!important;break-inside:avoid;border:1px solid #ddd}
  .wrap{max-width:100%;padding:0 10px}
  .table-wrap{overflow:visible}
  table{font-size:9pt}
  th{background:#333!important;color:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
  a{color:#333}
  a::after{content:" (" attr(href) ")";font-size:8pt;color:#888}
}

/* ═══ RESPONSIVE — TABLET ═══ */
@media(max-width:768px){
  body{font-size:15px;line-height:1.7}
  .wrap{max-width:100%;padding:0 16px 80px}
  .hero{padding:56px 16px 28px}
  .hero h1{font-size:clamp(24px,6vw,36px)}
  .hero p.lede{font-size:14px}
  .stats{gap:8px}
  .stat{padding:12px 6px}
  .stat .n{font-size:20px}
  .stat .l{font-size:10.5px}
  .content-body h2{font-size:22px;margin:40px 0 12px}
  .content-body h3{font-size:16.5px;margin:24px 0 8px}
  .content-body h4{font-size:14.5px}
  .floor{padding:22px 18px;border-radius:14px;margin:16px 0}
  li{font-size:14.5px}
  blockquote{padding:10px 14px;font-size:14px}
  nav{padding:8px 12px;gap:6px}
  nav a{font-size:11.5px;padding:5px 10px}
}

/* ═══ RESPONSIVE — MOBILE ═══ */
@media(max-width:480px){
  body{font-size:14.5px;line-height:1.65}
  .wrap{padding:0 10px 60px}
  .hero{padding:44px 14px 22px}
  .hero .eyebrow{font-size:10px;letter-spacing:.18em}
  .hero h1{font-size:clamp(20px,5.5vw,28px);margin:10px 0 10px}
  .hero p.lede{font-size:13px}
  .stats{grid-template-columns:1fr;gap:6px;margin-top:20px}
  .stat{padding:10px 8px;border-radius:12px;display:flex;align-items:center;gap:10px;text-align:left}
  .stat .n{font-size:18px;min-width:80px}
  .stat .l{font-size:10px;margin-top:0}
  .content-body h2{font-size:19px;margin:32px 0 10px}
  .content-body h3{font-size:15.5px;margin:20px 0 6px;padding-left:10px;border-left-width:3px}
  .content-body h4{font-size:13.5px;margin:16px 0 6px}
  .floor{padding:16px 12px;border-radius:12px;margin:12px 0}
  li{font-size:13.5px}
  p{font-size:13.5px}
  blockquote{padding:8px 10px;font-size:13px;margin:10px 0}
  nav{padding:6px 8px;gap:4px}
  nav a{font-size:10.5px;padding:4px 8px}
  .btt{width:38px;height:38px;font-size:16px;bottom:16px;right:16px}
  .site-footer{font-size:11px;padding:24px 12px}
}

/* ═══ RESPONSIVE — TABLE MOBILE ═══ */
@media(max-width:768px){
  .table-wrap{margin:10px -10px;border-radius:10px;border-left:none;border-right:none}
  table{font-size:11.5px;min-width:500px}
  th{font-size:10px;padding:8px 6px;letter-spacing:.03em}
  td{padding:7px 6px;font-size:11px}
  td:first-child{white-space:normal;min-width:70px}
}

/* ═══ RESPONSIVE — TABLE CARD MODE (very small) ═══ */
@media(max-width:400px){
  table{min-width:420px}
  th{font-size:9px;padding:6px 4px}
  td{padding:5px 4px;font-size:10px}
  .table-wrap{margin:8px -6px;border-radius:8px}
  /* Scroll hint shadow */
  .table-wrap{
    background:
      linear-gradient(to right, var(--card) 30%, transparent),
      linear-gradient(to left, var(--card) 30%, transparent),
      linear-gradient(to right, rgba(0,0,0,.12), transparent 40px),
      linear-gradient(to left, rgba(0,0,0,.12), transparent 40px);
    background-position: left center, right center, left center, right center;
    background-repeat: no-repeat;
    background-size: 20px 100%, 20px 100%, 20px 100%, 20px 100%;
    background-attachment: local, local, scroll, scroll;
  }
}
"""


JS = r"""
// Progress bar
window.addEventListener('scroll',()=>{
  const h=document.documentElement;
  const pct=h.scrollTop/(h.scrollHeight-h.clientHeight)*100;
  document.getElementById('prog').style.width=pct+'%';
});

// Scroll reveal
const obs=new IntersectionObserver(es=>{
  es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')})
},{threshold:.08});
document.querySelectorAll('.floor').forEach(el=>obs.observe(el));

// Back to top
const btt=document.querySelector('.btt');
window.addEventListener('scroll',()=>{
  btt.classList.toggle('show',window.scrollY>600);
});
btt.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));

// Active nav highlight
const sections=document.querySelectorAll('section[id]');
const navLinks=document.querySelectorAll('nav a');
window.addEventListener('scroll',()=>{
  let current='';
  sections.forEach(s=>{
    if(window.scrollY>=s.offsetTop-120) current=s.id;
  });
  navLinks.forEach(a=>{
    a.style.background=a.getAttribute('href')==='#'+current?'var(--chip-bg)':'var(--card)';
    a.style.color=a.getAttribute('href')==='#'+current?'var(--ink)':'var(--sub)';
  });
});
"""


def process_valuation_tags(html):
    """Convert valuation keywords to colored badges."""
    replacements = [
        (r'\*\*저평가\*\*', '<span class="tag-up">저평가</span>'),
        (r'\*\*매우 저평가\*\*', '<span class="tag-up">매우 저평가</span>'),
        (r'적정~저평가', '<span class="tag-up">적정~저평가</span>'),
        (r'\*\*적정\*\*', '<span class="tag-ca">적정</span>'),
        (r'적정', '<span class="tag-ca">적정</span>'),
        (r'고평가 \(제외\)', '<span class="tag-dn">고평가 (제외)</span>'),
        (r'고평가', '<span class="tag-dn">고평가</span>'),
        (r'중립 \(제외\)', '<span class="tag-ca">중립 (제외)</span>'),
        (r'매력적이나 사이클 주의', '<span class="tag-ca">사이클 주의</span>'),
    ]
    for pattern, replacement in replacements:
        html = re.sub(pattern, replacement, html)
    return html


def wrap_tables(html):
    """Wrap tables in scrollable container."""
    return re.sub(r'(<table>)', r'<div class="table-wrap">\1', html)


def close_table_wraps(html):
    return re.sub(r'(</table>)', r'\1</div>', html)


def extract_nav_sections(html):
    """Extract h2 headings for nav generation."""
    sections = []
    pattern = re.compile(r'<h2[^>]*id="([^"]*)"[^>]*>(.*?)</h2>', re.DOTALL)
    for m in pattern.finditer(html):
        sid = m.group(1)
        text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        # Shorten for nav
        short = text.split('—')[0].split(' — ')[0].strip()
        if len(short) > 20:
            short = short[:18] + '…'
        sections.append((sid, short))
    return sections


def add_section_ids(html):
    """Wrap each h2 in a <section> with an id for nav anchoring."""
    parts = re.split(r'(<h2[^>]*>)', html)
    result = []
    section_open = False
    sec_idx = 0
    for i, part in enumerate(parts):
        if part.startswith('<h2'):
            if section_open:
                result.append('</section>')
            sec_idx += 1
            result.append(f'<section id="sec-{sec_idx}">')
            # Add id to h2 if not present
            if 'id="' not in part:
                part = part.replace('<h2', f'<h2 id="sec-{sec_idx}"', 1)
            else:
                # Replace existing id
                part = re.sub(r'id="[^"]*"', f'id="sec-{sec_idx}"', part, 1)
            section_open = True
        result.append(part)
    if section_open:
        result.append('</section>')
    return ''.join(result)


def convert_md_to_html(md_path, html_path, meta):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Remove the first h1 line (we use hero instead)
    md_text = re.sub(r'^#\s+.*\n', '', md_text, count=1)
    # Remove the meta line right after
    md_text = re.sub(r'^\*\*작성일:?\*\*.*\n', '', md_text, count=1)
    md_text = re.sub(r'^\*\*분석 프레임워크:?\*\*.*\n', '', md_text, count=1)
    md_text = re.sub(r'^\*\*기반:?\*\*.*\n', '', md_text, count=1)

    extensions = ['tables', 'fenced_code', 'toc', 'sane_lists']
    extension_configs = {
        'toc': {'toc_depth': '2-3', 'title': '', 'permalink': False},
    }

    md = markdown.Markdown(extensions=extensions, extension_configs=extension_configs)
    html_body = md.convert(md_text)

    # Post-processing
    html_body = process_valuation_tags(html_body)
    html_body = wrap_tables(html_body)
    html_body = close_table_wraps(html_body)
    html_body = add_section_ids(html_body)

    # Extract nav items
    nav_items = extract_nav_sections(html_body)

    # Build nav HTML
    nav_html = '\n'.join(
        f'  <a href="#{sid}">{label}</a>' for sid, label in nav_items
    )

    # Build stats HTML
    stats_html = '\n'.join(
        f'<div class="stat"><div class="n">{n}</div><div class="l">{l}</div></div>'
        for n, l in meta['stats']
    )

    # Apply color to CSS
    css = CSS.replace('COLOR_PLACEHOLDER', meta['color']).replace('ACCENT_PLACEHOLDER', meta['accent'])

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta['title']} ({meta['version']}) — ourprochoi Research</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>{css}</style>
</head>
<body>

<div id="prog"></div>

<div class="hero-shell">
<div class="hero">
  <div class="eyebrow">{meta['eyebrow']} <span class="version">{meta['version']}</span></div>
  <h1>{meta['title']}</h1>
  <p class="lede">{meta['lede']}</p>
  <div class="stats">{stats_html}</div>
</div>
</div>

<nav>
  <a href="#sec-1">Overview</a>
{nav_html}
</nav>

<div class="wrap">
<div class="content-body">
{html_body}
</div>
</div>

<footer class="site-footer">
  ourprochoi Research Archive &middot; 2026-07-02 &middot; 본 자료는 투자 참고용이며, 투자 판단의 최종 책임은 투자자 본인에게 있습니다.
</footer>

<button class="btt" aria-label="Back to top">&uarr;</button>

<script>{JS}</script>
</body>
</html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    size_kb = os.path.getsize(html_path) / 1024
    print(f"  >> {os.path.basename(html_path)} ({size_kb:.0f} KB)")


if __name__ == '__main__':
    portfolio_dir = os.path.dirname(os.path.abspath(__file__))

    md_files = sorted([f for f in os.listdir(portfolio_dir) if f.endswith('.md')])

    if not md_files:
        print('No .md files found')
        sys.exit(1)

    print(f'변환 대상: {len(md_files)}개 파일\n')

    for md_file in md_files:
        stem = md_file.replace('.md', '')
        meta = META.get(stem)
        if not meta:
            print(f'  !! {md_file} — 메타데이터 없음, 스킵')
            continue

        md_path = os.path.join(portfolio_dir, md_file)
        html_path = os.path.join(portfolio_dir, stem + '.html')
        print(f'변환 중: {md_file} ...')
        try:
            convert_md_to_html(md_path, html_path, meta)
        except Exception as e:
            print(f'  !! {md_file} 실패: {e}')
            import traceback
            traceback.print_exc()

    print('\n완료!')
