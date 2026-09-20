#!/usr/bin/env python3
"""턴 스크린 — 「이익이 온 자리에는 값이 안 붙어 있고, 값이 붙은 자리에는 이익이 안 왔다」를 센다.

왜 있나(2026-09-20): 그날 한양디지텍(078350)을 찾아낸 것이 운이 아니라 조건 셋이었다 —
  ① 이익이 왔다(1H26 OP ≥ FY25 의 70%) ② 가속(2Q>1Q) ③ 값이 안 붙었다(PER 낮음)
  + ④ 아카이브 판단 0편. 그걸 유니버스 전체에 거는 것이 이 파일이다.
  leader_screen.py 와 다르다 — 저쪽은 주도·선행(가격 모멘텀 격자), 이쪽은 <이익 도착 시점 대비 가격>이다.

정본은 intake/files/financials/{날짜}/ 스냅샷(네이버 재무 원장 · ①).
  ⚠ 스키마가 둘이다 — 국내는 「영업이익」, 해외는 「EBIT」. 하나로 고정하면 해외 89종목이 통째로 빠진다
    (2026-09-20 실측: 고정 시 129/225 만 분석됐다 → 양쪽을 먹게 고쳐 218/225).
  ⚠ 커버리지 판정은 <이름과 티커를 둘 다> 본다. 이름만 보면 미국 종목이 전부 「판단 0편」으로 나온다
    (아카이브는 Diamondback 을 FANG 으로 부른다 — 2026-09-20 에 실제로 오판했다).
  ⚠ 짧은 티커(BE 등)는 부분일치로 과대 계상된다. 0 인지 아닌지만 믿고 숫자는 믿지 마라.

용법: python3 portfolio/data/turn_screen.py [스냅샷일자] [--all]
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def universe(day):
    d = os.path.join(ROOT, "intake", "files", "financials", day)
    names = {}
    src = open(os.path.join(ROOT, "portfolio/data/update_prices.py"), encoding="utf8").read()
    for m in re.finditer(r'"([^"]+)":\s*"([0-9A-Za-z.]{4,12})"', src):
        names.setdefault(m.group(2), m.group(1))
    th = open(os.path.join(ROOT, "brain/theses.json"), encoding="utf8").read()
    rows = []
    for p in sorted(glob.glob(d + "/*.json")):
        code = os.path.basename(p)[:-5]
        try:
            f = json.load(open(p))
        except Exception:  # noqa: BLE001 — 깨진 스냅샷은 건너뛰되 개수로 드러난다
            continue
        q, a = f.get("quarter") or {}, f.get("annual") or {}
        aq = [k for k in sorted(q) if not q[k].get("cx")]
        af = [k for k in sorted(a) if not a[k].get("cx")]
        if len(aq) < 5 or not af:
            continue
        op = lambda r: r.get("영업이익") if r.get("영업이익") is not None else r.get("EBIT")  # noqa: E731
        q2, q1, qy, fy = aq[-1], aq[-2], aq[-5], af[-1]
        o2, o1, oy, ofy = op(q[q2]), op(q[q1]), op(q[qy]), op(a[fy])
        r2, ry = q[q2].get("매출액"), q[qy].get("매출액")
        if o2 is None or o1 is None or ofy is None:
            continue
        nm = names.get(code, code)
        keys = {nm}
        t = re.sub(r"\.[A-Z]$", "", code)
        if re.fullmatch(r"[A-Z]{1,5}", t):
            keys.add(t)
        rows.append(dict(
            code=code, name=nm, us=q[q2].get("영업이익") is None,
            op2=o2, op1=o1, opy=oy, opfy=ofy,
            per=q[q2].get("PER") or a[fy].get("PER"), pbr=q[q2].get("PBR") or a[fy].get("PBR"),
            opm=q[q2].get("영업이익률") or ((o2 / r2 * 100) if r2 else None),
            ratio=(o1 + o2) / ofy if ofy > 0 else None,
            accel=o2 > o1, turn=(oy is not None and oy <= 0 < o2),
            fade=(oy is not None and oy > 0 and o2 < oy * 0.8),
            yoy=((o2 / oy - 1) if (oy and oy > 0) else None),
            rev_yoy=((r2 / ry - 1) if (r2 and ry and ry > 0) else None),
            th=max(th.count(k) for k in keys)))
    return rows


def show(title, rows):
    print(f"\n{'═' * 92}\n{title}  [{len(rows)}]\n{'═' * 92}")
    print(f"    {'종목':<17}{'1H÷FY':>7}{'2Q OP':>11}{'OPM':>8}{'매출YoY':>8}{'OP YoY':>8}{'PER':>8}{'PBR':>7}")
    for r in rows:
        ra = f"{r['ratio']*100:.0f}%" if r["ratio"] else ("흑전" if r["turn"] else "—")
        pe = f"{r['per']:.1f}" if r["per"] and 0 < r["per"] < 400 else ("적자" if (r["per"] or 0) <= 0 else "—")
        yy = f"{r['yoy']*100:+.0f}%" if r["yoy"] is not None else "—"
        rv = f"{r['rev_yoy']*100:+.0f}%" if r["rev_yoy"] is not None else "—"
        mk = "🔴" if r["th"] == 0 else ("🟡" if r["th"] < 5 else "  ")
        print(f"{mk}{'🇺🇸' if r['us'] else '  '}{r['name'][:16]:<17}{ra:>7}{r['op2']:>11,.0f}"
              f"{(r['opm'] or 0):>7.1f}%{rv:>8}{yy:>8}{pe:>8}{(r['pbr'] or 0):>7.2f}")


def main(argv):
    days = sorted(os.path.basename(x) for x in glob.glob(os.path.join(ROOT, "intake/files/financials/*")))
    day = next((a for a in argv[1:] if not a.startswith("--")), days[-1] if days else None)
    if not day:
        print("스냅샷이 없다 — leader_screen.py 를 먼저 돌려라")
        return 1
    rows = universe(day)
    print(f"스냅샷 {day} · 분석 {len(rows)}종목 (국내 {sum(1 for r in rows if not r['us'])} · 해외 {sum(1 for r in rows if r['us'])})")
    A = sorted((r for r in rows if r["ratio"] and r["ratio"] >= .70 and r["accel"] and r["per"] and 0 < r["per"] <= 15),
               key=lambda r: (r["th"], -r["ratio"]))
    B = sorted((r for r in rows if r["turn"] and r["accel"] and r["op2"] > 0), key=lambda r: (r["th"], -r["op2"]))
    C = sorted((r for r in rows if r["fade"] and (not r["per"] or r["per"] <= 0 or r["per"] >= 20)),
               key=lambda r: (r["yoy"] if r["yoy"] is not None else 0))
    show("Ⓐ 정방향 — 이익이 왔는데 값이 안 붙었다 (1H≥FY70% · 2Q>1Q · PER≤15)", A)
    show("Ⓑ 적자→흑자 + 가속", B)
    show("Ⓒ 역방향 — 이익이 빠지는데 값은 붙어 있다 (2Q OP < 작년동기 80% · PER≥20 또는 적자)",
         C if "--all" in argv else C[:18])
    print("\n🔴 = 아카이브 테제 0편(발굴 후보) · 🟡 = 5편 미만 · ⚠ 스크린은 후보를 좁힐 뿐 판단하지 않는다(§J1)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
