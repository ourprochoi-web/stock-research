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
        f'<div style="margin-top:8px;font-size:.78rem;color:var(--ink-3)">이 카드는 손으로 고치지 않는다 — 정본은 <code>brain/theses.json</code>이고, 경위는 <code>brain/inbox.jsonl</code>과 아래 타임라인에 있다. 값의 분자·분모·기준일은 <code>brain/facts.json</code>.</div>\n'
        f"</div>\n</div></section>\n{END}")


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
    if check:
        for p in drift:
            print(f"[cards] ⚠ 카드가 브레인과 다르다 — {p}")
        return 1 if drift else 0
    for p in changed:
        print(f"[cards] 카드 렌더 — {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
