#!/usr/bin/env python3
"""data/facts.json 의 각 값이 그 값을 산출한 정본 페이지에 실제로 있는지 검사한다.

경고만 한다 — 판정은 사람이 한다(§H). 두 방향의 드리프트를 잡는다:
  · 페이지를 고쳤는데 facts 를 안 고침 → 페이지에서 옛 값이 사라져 검출
  · facts 를 고쳤는데 페이지를 안 고침 → 새 값이 페이지에 없어 검출
용법: check_facts.py [페이지 경로 ...]  (인자 없으면 전부)
"""
import html as htmlmod
import io
import json
import re
import sys

FACTS = "data/facts.json"


def page_text(path):
    try:
        s = io.open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        return None
    s = re.sub(r"<script[\s\S]*?</script>|<style[\s\S]*?</style>", "", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = htmlmod.unescape(s).replace("\xa0", " ")
    return s.replace("−", "-").replace("–", "-")


def candidates(v):
    """값이 페이지에 적힐 수 있는 표기들."""
    out = set()
    if isinstance(v, bool) or v is None:
        return out
    if isinstance(v, (int, float)):
        a = abs(v)
        forms = {f"{a}", f"{a:,}", f"{a:.1f}", f"{a:,.1f}", f"{a:.2f}", f"{a:,.2f}", f"{a:.0f}", f"{a:,.0f}"}
        for f in forms:
            out.add(f)
            if f.endswith(".0"):
                out.add(f[:-2])
    else:
        out.add(str(v))
    return out


def main(argv):
    only = set(argv[1:])
    try:
        doc = json.load(io.open(FACTS, encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"[facts] {FACTS} 를 못 읽음: {e}")
        return 0
    cache, missing, checked = {}, [], 0
    for tk, c in doc.get("companies", {}).items():
        for key, mtr in c.get("metrics", {}).items():
            page = mtr.get("page")
            if not page or (only and page not in only):
                continue
            if page not in cache:
                cache[page] = page_text(page)
            text = cache[page]
            if text is None:
                missing.append((tk, key, page, "페이지 없음"))
                continue
            checked += 1
            cands = candidates(mtr.get("value"))
            if cands and not any(cd in text for cd in cands):
                missing.append((tk, key, page, mtr.get("value")))
    if missing:
        print(f"[facts] ⚠ 페이지에 없는 값 {len(missing)}건 / 검사 {checked}건 — facts 와 페이지 중 하나가 낡았다(§W4)")
        for tk, key, page, v in missing[:20]:
            print(f"    · {tk}.{key} = {v}  ↛  {page}")
    else:
        print(f"[facts] ✓ {checked}건 전부 정본 페이지에 있음")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
