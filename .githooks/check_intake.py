#!/usr/bin/env python3
"""세 층의 포인터가 실재하는지 검사한다(경고만).

  brain/routing.jsonl 의 intake[]  →  intake/user.jsonl · collected.jsonl 의 id
  brain/facts.json 의 companies.*.intake[]  →  같은 곳
  brain/theses.json 의 theses[].facts[]  →  brain/facts.json 의 companies.<tk>.metrics.<key>
포인터가 끊기면 「무엇이 왔나」와 「그래서 어떻게 봤나」가 다시 분리되므로 여기서 잡는다.
"""
import io
import json
import re
import sys


def jsonl(path):
    try:
        return [json.loads(l) for l in io.open(path, encoding="utf-8") if l.strip()]
    except OSError:
        return []


def main():
    ids = {r["id"] for r in jsonl("intake/user.jsonl") + jsonl("intake/collected.jsonl")}
    bad = []
    for r in jsonl("brain/routing.jsonl"):
        for i in r.get("intake", []):
            if i not in ids:
                bad.append(f"routing {r.get('date')} «{r.get('claim', '')[:30]}» → intake {i} 없음")
    try:
        F = json.load(io.open("brain/facts.json", encoding="utf-8"))["companies"]
    except (OSError, ValueError, KeyError):
        F = {}
    for tk, c in F.items():
        for i in c.get("intake", []):
            if i not in ids:
                bad.append(f"facts {tk} → intake {i} 없음")
    try:
        T = json.load(io.open("brain/theses.json", encoding="utf-8"))["pages"]
    except (OSError, ValueError, KeyError):
        T = {}
    for path, pg in T.items():
        for t in pg.get("theses", []):
            for fk in t.get("facts", []):
                tk, _, key = fk.rpartition(".")
                if tk not in F or key not in F[tk].get("metrics", {}):
                    bad.append(f"theses {path}#{t['id']} → facts {fk} 없음")
    # 지난 날짜 판정 이벤트(§H1: 도래하면 판정하고 지운다) — 2026-09-17
    try:
        from datetime import date as _d
        ev = json.load(io.open("brain/events.json", encoding="utf-8")).get("events", [])
        today = _d.today().isoformat()
        past = [e for e in ev if re.match(r"^\d{4}-\d{2}-\d{2}$", str(e.get("when", "")).strip()) and e["when"] < today]
        if past:
            print(f"[events] ⚠ 지난 판정 이벤트 {len(past)}건 — 판정하고 지운다(§H1)")
            for e in past[:5]:
                print(f"    · {e['when']} {str(e.get('what',''))[:70]}")
    except (OSError, ValueError):
        pass
    # id 중복 검사(2026-09-20 실측으로 추가) — 층 전체가 id 로 서로를 가리키는데
    #   append-only JSONL 에 <여러 주체>가 쓴다(세션 여럿 · 수집기 셋 · 시세 봇).
    #   각자 「자기가 본 파일」로 다음 번호를 세면 같은 id 가 두 번 나고, 그러면
    #   라우팅 포인터가 <어느 줄을 가리키는지 알 수 없게> 된다 — 조용히 틀리는 종류다.
    #   09-20 에 실제로 13건 났다: routing 6(내가 손으로 번호를 적으며 파일을 안 봤다) ·
    #   user 6(같은 사유 + 앞선 배치) · collected 1(collect-fetch ↔ collect-sec 동시 실행).
    import collections
    for f in ("intake/collected.jsonl", "intake/user.jsonl", "brain/routing.jsonl"):
        try:
            cnt = collections.Counter(
                json.loads(ln)["id"] for ln in io.open(f, encoding="utf-8") if ln.strip())
        except (OSError, ValueError, KeyError):
            continue
        dup = {k: v for k, v in cnt.items() if v > 1}
        if dup:
            print(f"[intake] 🔴 {f} id 중복 {len(dup)}건 — 라우팅이 어느 줄을 가리키는지 알 수 없다")
            for k, v in list(dup.items())[:8]:
                print(f"    · {k} ×{v}")

    # WATCH 중복 키 검사(2026-09-20 추가) — 파이썬 dict 는 <같은 키를 조용히 덮는다>.
    #   뒤에 쓴 값이 이기고 앞의 것은 사라지는데 문법 오류도 경고도 없다.
    #   오늘 두 번 났다: "Cerebras" 를 CBRS 로 넣었는데 아래에 CBRS.O 가 이미 있었고,
    #   "S-Oil" 을 LNG 층에 넣었는데 이미 등록돼 있었다. 코드가 다르면 조용히 <다른 회사>를 받는다.
    try:
        import collections as _c
        src = io.open("portfolio/data/update_prices.py", encoding="utf-8").read()
        pairs = re.findall(r'"([^"]+)":\s*"([0-9A-Za-z.]{4,12})"', src)
        names = _c.Counter(k for k, _ in pairs)
        dup = {k: v for k, v in names.items() if v > 1}
        if dup:
            bycode = _c.defaultdict(set)
            for k, v in pairs:
                bycode[k].add(v)
            print(f"[watch] 🔴 update_prices WATCH 중복 키 {len(dup)}건 — dict 는 뒤엣것으로 조용히 덮는다")
            for k in list(dup)[:8]:
                codes = "/".join(sorted(bycode[k]))
                mark = " ⚠ 코드까지 다르다(다른 회사를 받는다)" if len(bycode[k]) > 1 else ""
                print(f"    · {k} ×{dup[k]} → {codes}{mark}")
    except (OSError, ValueError):
        pass

    if bad:
        print(f"[intake] ⚠ 끊긴 포인터 {len(bad)}건")
        for b in bad[:20]:
            print("    · " + b)
    else:
        print("[intake] ✓ 포인터 전부 실재")
    return 0


if __name__ == "__main__":
    sys.exit(main())
