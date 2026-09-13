#!/usr/bin/env python3
"""페이지의 「현재 판단」 블록에서 테제·반증 조건·다음 검증을 뽑아 docs/thesis_index.md 를 만든다.

CLAUDE.md §H 의 기준을 통과하는 이유 — 새 데이터를 만들지 않는다. 87편 HTML 에
이미 있는 판단을 한 파일로 <파생>할 뿐이고, pre-commit 이 페이지가 바뀔 때마다
다시 만들므로 사람이 유지하지 않는다(sitemap lastmod 동기화와 같은 종류).
정본은 언제나 페이지다. 이 파일은 「어느 페이지를 열 것인가」를 정하는 색인이다.
"""
import glob
import html as htmlmod
import io
import re
import sys
from datetime import date

OUT = "docs/thesis_index.md"
DATE = re.compile(r"현재 판단 · (\d{4}\.\d{2}\.\d{2})")
DM = re.compile(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})"')
TITLE = re.compile(r"<title>([^<]*)</title>")


def to_text(s):
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", s)
    s = re.sub(r"<br\s*/?>|</p>|</div>|</tr>|</li>|</h\d>|</table>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s).replace("\xa0", " ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s


def clip(s, n):
    s = re.sub(r"\s+", " ", s).strip(" —-·:")
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def parse(path):
    raw = io.open(path, encoding="utf-8", errors="ignore").read()
    m = DATE.search(raw)
    if not m:
        return None
    t = to_text(raw)
    i = t.find("현재 판단 ·")
    seg = t[i:]
    # 블록의 끝 — 「01 」로 시작하는 본문 절 또는 다음 큰 제목. 넉넉히 12K자.
    stop = re.search(r"\n\s*0[1-9]\s*\n", seg)
    seg = seg[: stop.start()] if stop and stop.start() > 300 else seg[:12000]

    j = seg.find("반증 조건")
    core = seg[:j] if j > 0 else seg
    tail = seg[j:] if j > 0 else ""

    one = ""
    m1 = re.search(r"한 문장[^\n]*?[—\-:]\s*(.+)", core)
    if m1:
        one = clip(m1.group(1), 220)

    theses = []
    for tm in re.finditer(r"(?:^|\n|\s)(T\d+)[.．]\s*(.+)", core):
        line = tm.group(2).strip()
        if len(line) < 8 or line.startswith("→"):
            continue
        theses.append((tm.group(1), clip(line, 170)))
    seen = set()
    theses = [x for x in theses if not (x[0] in seen or seen.add(x[0]))]

    fals = []
    # 제목 줄 「반증 조건 · 다음 검증」 자체를 건너뛰고, 줄머리의 「다음 검증」을 찾는다
    km = re.search(r"\n\s*다음 검증", tail)
    k = km.start() if km else -1
    fpart, npart = (tail[:k], tail[k:]) if k > 0 else (tail, "")
    for fm in re.finditer(r"(T\d+(?:[·,/]\s*T\d+)*)[^\n→]{0,14}→\s*(.+)", fpart):
        fals.append((fm.group(1), clip(fm.group(2), 170)))
    nexts = []
    for ln in npart.split("\n")[1:]:
        ln = ln.strip(" ·•-")
        if len(ln) < 6:
            continue
        if re.match(r"^(0\d|▎|최근 변경)", ln):
            break
        if ln.startswith("다음 검증") or ln.startswith("이 판단이 틀렸음"):
            continue
        nexts.append(clip(ln, 150))
        if len(nexts) >= 4:
            break

    tt = TITLE.search(raw)
    dm = DM.search(raw)
    return dict(
        path=path,
        title=htmlmod.unescape(tt.group(1)).strip() if tt else path,
        judged=m.group(1),
        modified=dm.group(1) if dm else "",
        one=one,
        theses=theses,
        fals=fals,
        nexts=nexts,
    )


def main():
    pages = []
    for f in sorted(glob.glob("*/*.html")):
        if "update_log" in f:
            continue
        p = parse(f)
        if p:
            pages.append(p)
    pages.sort(key=lambda p: p["judged"], reverse=True)

    out = []
    out.append("# 테제 색인 — 정본은 페이지다\n")
    out.append(f"자동 생성 · {date.today().isoformat()} · 판단 보유 {len(pages)}편 · "
               "생성기 `.githooks/build_thesis_index.py` (pre-commit 이 페이지가 바뀔 때 다시 만든다)\n")
    out.append("**용도** — 종목·테마 질문을 받으면 이 파일에서 해당 테제를 찾고, "
               "**그 페이지의 「현재 판단」만** 연다. 여기 적힌 문장은 페이지에서 잘라 온 첫 줄이며 "
               "**값·기준일·등급은 페이지가 정본**이다.\n")
    out.append("**⚠ 판단 날짜 < 갱신일**인 편은 §0 규칙5 결함 후보다(아래 표에 `⚠` 표시).\n")

    out.append("\n## 목차 (판단 날짜순)\n")
    out.append("| 판단 | 갱신 | 페이지 | 테제 |")
    out.append("|---|---|---|---|")
    for p in pages:
        flag = " ⚠" if p["modified"] and p["judged"].replace(".", "-") < p["modified"] else ""
        out.append(f"| {p['judged']}{flag} | {p['modified']} | [{clip(p['title'], 60)}]({p['path']}) | {len(p['theses'])} |")

    for p in pages:
        out.append(f"\n## {p['title']}\n")
        out.append(f"`{p['path']}` · 판단 {p['judged']} · 갱신 {p['modified']}\n")
        if p["one"]:
            out.append(f"**한 문장** — {p['one']}\n")
        if p["theses"]:
            for tid, s in p["theses"]:
                out.append(f"- **{tid}.** {s}")
        else:
            out.append("- (테제 헤드라인을 기계적으로 못 잘랐다 — 페이지를 연다)")
        if p["fals"]:
            out.append("\n**반증 조건**")
            for tid, s in p["fals"]:
                out.append(f"- {tid} → {s}")
        if p["nexts"]:
            out.append("\n**다음 검증**")
            for s in p["nexts"]:
                out.append(f"- {s}")

    io.open(OUT, "w", encoding="utf-8").write("\n".join(out) + "\n")
    ok = sum(1 for p in pages if p["theses"])
    print(f"[thesis-index] {len(pages)}편 → {OUT} (테제 추출 {ok}편)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
