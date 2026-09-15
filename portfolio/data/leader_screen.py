#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""주도주 스크린 v2 (2026-09-15 밤) — 추적 유니버스(KR 102 · US 90)에 우리 스코어링을 돌린다.

성상현(ABP) 격자의 <게이트>를 빌리고 팩터는 우리 데이터로 다시 짰다. v2 고도화(v1 대비):
  · 섹터 태그(naver industryCode / industryGroupKor) → 섹터 내 상대강도 · 섹터 캡 3/10 자동
  · 추정치 <변화>(1M): KR 추정EPS · US 목표주가 — git 의 prices.json 30일 전 스냅샷과 대조(「성장 기대 상향」의 실측)
  · SBC 페널티(facts.json sbc_to_rev_q > 15% → −5) · OCF/EBIT 경고(<0.7)
  · 판단 보유 여부(judged) · 추적에만 있고 시세 없는 US 종목은 그 자리에서 받는다(Semtech 등)
  G 성장 30  = 3년 매출 CAGR(12) + 최근 분기 매출 YoY(12) + 선행 성장(6 · KR 컨센 매출 / US EBIT YoY)
  P 가격 30  = 3M 상대강도 vs 지수(10) + 3M 상대강도 vs 섹터(6) + 6M vs 지수(8) + 1M 낙폭 가드(6)
  Q 질   20  = 분기 OPM 수준(7) + ΔOPM YoY(7) + ROE(6 · US는 ROA)   [− SBC 페널티 5]
  E 기대 20  = KR: 컨센 EPS 성장(6) + Δ추정EPS 1M(8) + 10일 외인+기관/시총(6) · US: TP 괴리(6) + ΔTP 1M(8) + 투자의견(6)
격자: G≥50 & P≥50 = A(보유) · G≥50 & P<50 = B(눌림목 vs 탈락 — ΔOPM·매출 YoY로 게이트) · G<50 & P≥50 = C(사이클·테마 점검) · 나머지 D.
점수는 시장별 백분위(0~100). 값의 정본은 intake/files/financials/{date}/ 스냅샷(naver finance annual·quarter).
용법: leader_screen.py [--date YYYY-MM-DD] [--no-fetch] [--top N]
출력: intake/files/leader_screen_{date}.json + 표. 판단은 하지 않는다 — 후보를 좁힌다(§C1).
"""
import io
import json
import os
import re
import sys
import time
import urllib.request
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PRICES = os.path.join(ROOT, "portfolio", "data", "prices.json")
FIN_DIR = os.path.join(ROOT, "intake", "files", "financials")
SECTORS = os.path.join(ROOT, "intake", "files", "sectors.json")
FACTS = os.path.join(ROOT, "brain", "facts.json")
THESES = os.path.join(ROOT, "brain", "theses.json")
ENTITIES = os.path.join(ROOT, "brain", "entities.json")
import subprocess
UA = {"User-Agent": "Mozilla/5.0"}
sys.path.insert(0, os.path.join(ROOT, "portfolio", "data"))
sys.path.insert(0, os.path.join(ROOT, "intake"))


def get(url, timeout=10):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return json.loads(r.read())
    except Exception:  # noqa: BLE001
        return None


def num(s):
    if s is None:
        return None
    m = re.search(r"-?[\d,]*\.?\d+", str(s))
    if not m:
        return None
    try:
        return float(m.group(0).replace(",", ""))
    except ValueError:
        return None


def parse_fin(d, us=False):
    """naver finance annual/quarter → {period: {매출액, 영업이익, ROE?}} (컨센서스 열은 cx 표시)"""
    fi = d.get("financeInfo", d) if d else None
    if not fi or not fi.get("trTitleList"):
        return None
    cols = {t["key"]: (t.get("isConsensus") == "Y") for t in fi["trTitleList"]}
    out = {}
    for row in fi.get("rowList", []):
        title = row.get("title")
        for k, c in (row.get("columns") or {}).items():
            out.setdefault(k, {"cx": cols.get(k, False)})[title] = num((c or {}).get("value"))
    return out


def fetch_financials(code, us):
    base = f"https://api.stock.naver.com/stock/{code}/finance/" if us else f"https://m.stock.naver.com/api/stock/{code}/finance/"
    a = parse_fin(get(base + "annual"), us)
    q = parse_fin(get(base + "quarter"), us)
    return {"annual": a, "quarter": q}


def cagr(vals):
    vals = [v for v in vals if v is not None and v > 0]
    if len(vals) < 2:
        return None
    n = len(vals) - 1
    return ((vals[-1] / vals[0]) ** (1 / n) - 1) * 100


def pct_rank(xs, x):
    v = [y for y in xs if y is not None]
    if x is None or not v:
        return None
    return 100.0 * sum(1 for y in v if y <= x) / len(v)


def load_universe():
    P = json.load(io.open(PRICES, encoding="utf-8"))
    import update_prices as up  # 코드 매핑
    kr = {}
    for name, code in {**up.TICKERS, **up.WATCH}.items():
        if name in P["prices"]:
            kr[name] = {"code": code, "us": False, "price": P["prices"][name], "ret": P["returns"].get(name, {}),
                        "fund": P["fundamentals"].get(name, {}), "flow": P["flows"].get(name, {})}
    usd = {}
    for name, rec in P["us"].items():
        usd[name] = {"code": rec["symbol"], "us": True, "price": rec.get("price"), "ret": P["returns"].get(name, {}),
                     "mcapB": rec.get("mcapB"), "tp": num(rec.get("목표주가")), "rating": num(rec.get("투자의견")),
                     "ebit_yoy": rec.get("EBIT_YoY"), "opm_now": rec.get("OPM")}
    # v2: 추적(WATCH_US)에는 있는데 prices.json 에 아직 없는 종목 — 봇을 기다리지 않고 받는다
    for name, sym in up.WATCH_US.items():
        if name in usd:
            continue
        d = up.fetch_us(sym)
        if not d:
            continue
        try:
            px = float(str(d["closePrice"]).replace(",", ""))
        except (KeyError, ValueError):
            continue
        fd = up.fetch_us_fundamentals(sym) or {}
        usd[name] = {"code": sym, "us": True, "price": px, "ret": up.fetch_returns(sym, foreign=True) or {},
                     "tp": num(fd.get("목표주가")), "rating": num(fd.get("투자의견")), "ebit_yoy": fd.get("EBIT_YoY"), "opm_now": fd.get("OPM"), "fresh": True}
        print(f"  + {name} ({sym}) 즉석 수집")
    return P, kr, usd


def load_sectors(allrec):
    """섹터 태그 — KR: integration.industryCode(숫자) · US: basic.industryCodeType.industryGroupKor. 캐시 intake/files/sectors.json"""
    sec = json.load(io.open(SECTORS, encoding="utf-8")) if os.path.exists(SECTORS) else {}
    changed = False
    for name, rec in allrec.items():
        if name in sec:
            continue
        if rec["us"]:
            d = get(f"https://api.stock.naver.com/stock/{rec['code']}/basic")
            tag = ((d or {}).get("industryCodeType") or {}).get("industryGroupKor")
        else:
            d = get(f"https://m.stock.naver.com/api/stock/{rec['code']}/integration")
            code = (d or {}).get("industryCode")
            peers = [x.get("stockName") for x in ((d or {}).get("industryCompareInfo") or [])][:3]
            tag = f"KR{code}" + (f"({'·'.join(p for p in peers if p)})" if peers else "") if code else None
            if (d or {}).get("stockEndType") == "etf":
                tag = "ETF"
        sec[name] = tag
        changed = True
        time.sleep(0.1)
    if changed:
        io.open(SECTORS, "w", encoding="utf-8").write(json.dumps(sec, ensure_ascii=False, indent=1))
    return sec


def load_prev_prices(days=30):
    """git 에서 days 일 전 prices.json — 추정치 변화(Δ추정EPS · ΔTP)의 분모"""
    try:
        log = subprocess.run(["git", "log", "--format=%h %ad", "--date=short", "--", "portfolio/data/prices.json"],
                             capture_output=True, text=True, cwd=ROOT).stdout.strip().split("\n")
        from datetime import timedelta
        cutoff = (date.today() - timedelta(days=days)).isoformat()
        rev = next((l.split()[0] for l in log if l.split()[1] <= cutoff), None)
        if not rev:
            return None, None
        txt = subprocess.run(["git", "show", f"{rev}:portfolio/data/prices.json"], capture_output=True, text=True, cwd=ROOT).stdout
        return json.loads(txt), rev
    except Exception:  # noqa: BLE001
        return None, None


def load_flags():
    """facts(SBC·OCF/EBIT) · 판단 보유 여부"""
    sbc, ocf = {}, {}
    try:
        F = json.load(io.open(FACTS, encoding="utf-8"))["companies"]
        for k, v in F.items():
            m = v.get("metrics", {})
            if "sbc_to_rev_q" in m:
                sbc[k] = m["sbc_to_rev_q"]["value"] if isinstance(m["sbc_to_rev_q"], dict) else m["sbc_to_rev_q"]
            if "ocf_to_ebit_q" in m:
                ocf[k] = m["ocf_to_ebit_q"]["value"] if isinstance(m["ocf_to_ebit_q"], dict) else m["ocf_to_ebit_q"]
    except Exception:  # noqa: BLE001
        pass
    judged = set()
    try:
        T = json.load(io.open(THESES, encoding="utf-8"))["pages"]
        blob = " ".join(p.get("title", "") + " " + " ".join(t["claim"] for t in p["theses"]) for p in T.values())
        E = json.load(io.open(ENTITIES, encoding="utf-8"))["companies"]
        judged = {v.get("name", "") for v in E.values()} | {k for k in E}
        judged_blob = blob
    except Exception:  # noqa: BLE001
        judged_blob = ""
    return sbc, ocf, judged, judged_blob


def bench_returns():
    import collect_sources as cs
    out = {}
    today = date.today().strftime("%Y%m%d")
    for key, fn in (("KR", lambda: cs.naver_index_daily("KOSPI", "20250601", today)),
                    ("US", lambda: cs.naver_foreign_index_daily(".INX", "20250601", today))):
        try:
            rows = fn()
            closes = [(r.get("localDate") or r.get("date"), float(r["closePrice"])) for r in rows]
            last = closes[-1][1]
            def back(n):
                return closes[-1 - n][1] if len(closes) > n else None
            out[key] = {"1M": (last / back(21) - 1) * 100 if back(21) else 0, "3M": (last / back(63) - 1) * 100 if back(63) else 0,
                        "6M": (last / back(126) - 1) * 100 if back(126) else 0, "asof": closes[-1][0]}
        except Exception as e:  # noqa: BLE001
            out[key] = {"1M": 0, "3M": 0, "6M": 0, "asof": None, "error": str(e)[:80]}
    return out


def mcap_krw(s):
    """'1,323조 6,522억' → 원"""
    if not s:
        return None
    t = 0
    m = re.search(r"([\d,]+)조", s)
    if m:
        t += float(m.group(1).replace(",", "")) * 1e12
    m = re.search(r"([\d,]+)억", s)
    if m:
        t += float(m.group(1).replace(",", "")) * 1e8
    return t or None


def compute(name, rec, fin, bench, sector=None, prev=None, flags=None):
    r = rec["ret"] or {}
    a = (fin or {}).get("annual") or {}
    q = (fin or {}).get("quarter") or {}
    akeys = sorted(k for k, v in a.items() if not v.get("cx"))
    ckeys = sorted(k for k, v in a.items() if v.get("cx"))
    qkeys = sorted(k for k, v in q.items() if not v.get("cx"))
    rev_a = [a[k].get("매출액") for k in akeys]
    g_cagr = cagr(rev_a[-4:]) if len(rev_a) >= 2 else None
    # 최근 분기 vs 4분기 전
    rev_q = [q[k].get("매출액") for k in qkeys]
    op_q = [q[k].get("영업이익") if q[k].get("영업이익") is not None else q[k].get("EBIT") for k in qkeys]  # US는 EBIT 행
    roe = None
    for k in reversed(qkeys):
        v = q[k].get("ROE") if q[k].get("ROE") is not None else q[k].get("ROA")  # US는 ROA
        if v is not None:
            roe = v
            break
    yoy = None
    d_opm = None
    opm_now = None
    if len(qkeys) >= 5 and rev_q[-1] and rev_q[-5]:
        yoy = (rev_q[-1] / rev_q[-5] - 1) * 100
        if op_q[-1] is not None and op_q[-5] is not None:
            opm_now = op_q[-1] / rev_q[-1] * 100
            d_opm = opm_now - op_q[-5] / rev_q[-5] * 100
    elif rev_q and rev_q[-1] and op_q and op_q[-1] is not None:
        opm_now = op_q[-1] / rev_q[-1] * 100
    if opm_now is None and rec.get("opm_now") is not None:
        opm_now = rec["opm_now"]
    # 선행 성장
    fwd = None
    if not rec["us"]:
        if ckeys and akeys and a[ckeys[0]].get("매출액") and a[akeys[-1]].get("매출액"):
            fwd = (a[ckeys[0]]["매출액"] / a[akeys[-1]]["매출액"] - 1) * 100
    else:
        fwd = rec.get("ebit_yoy")
    # 가격
    b = bench["US" if rec["us"] else "KR"]
    rs3 = (r.get("3M") - b["3M"]) if r.get("3M") is not None else None
    rs6 = (r.get("6M") - b["6M"]) if r.get("6M") is not None else None
    m1 = r.get("1M")
    guard = None if m1 is None else max(0.0, min(1.0, (m1 + 20) / 15))  # −5 이상 만점, −20 이하 0
    # 기대·자금
    if not rec["us"]:
        f = rec["fund"] or {}
        eps, feps = num(f.get("EPS")), num(f.get("추정EPS"))
        e1 = (feps / eps - 1) * 100 if eps and feps and eps > 0 else None
        fl = rec["flow"] or {}
        mc = mcap_krw(f.get("시총"))
        e2 = ((fl.get("foreign") or 0) + (fl.get("organ") or 0)) * (rec["price"] or 0) / mc * 100 if mc and rec["price"] else None
    else:
        e1 = (rec["tp"] / rec["price"] - 1) * 100 if rec.get("tp") and rec.get("price") else None
        e2 = rec.get("rating")
    # v2: 추정치 변화(1M) — KR 추정EPS · US 목표주가
    rev1m = None
    if prev:
        if not rec["us"]:
            pf = (prev.get("fundamentals") or {}).get(name) or {}
            p0, p1 = num(pf.get("추정EPS")), num((rec["fund"] or {}).get("추정EPS"))
            if p0 and p1 and p0 > 0:
                rev1m = (p1 / p0 - 1) * 100
        else:
            pu = (prev.get("us") or {}).get(name) or {}
            p0, p1 = num(pu.get("목표주가")), rec.get("tp")
            if p0 and p1 and p0 > 0:
                rev1m = (p1 / p0 - 1) * 100
    sbc_pen = 0
    ocf_warn = None
    if flags:
        sbc, ocf, judged, jblob = flags
        code_key = rec["code"].split(".")[0]
        if code_key in sbc and sbc[code_key] is not None and sbc[code_key] > 15:
            sbc_pen = 5
        if code_key in ocf and ocf[code_key] is not None and ocf[code_key] < 0.7:
            ocf_warn = ocf[code_key]
    return {"name": name, "code": rec["code"], "us": rec["us"], "price": rec["price"], "sector": sector, "rev1m": rev1m, "sbc_pen": sbc_pen, "ocf_warn": ocf_warn,
            "judged": bool(flags and (name in flags[2] or rec["code"].split(".")[0] in flags[2] or name in flags[3])),
            "cagr3": g_cagr, "rev_yoy_q": yoy, "fwd": fwd, "opm": opm_now, "d_opm": d_opm,
            "m1": m1, "m3": r.get("3M"), "m6": r.get("6M"), "y1": r.get("1Y"), "rs3": rs3, "rs6": rs6, "guard": guard,
            "e1": e1, "e2": e2, "roe": roe, "n_annual": len(akeys), "n_quarter": len(qkeys), "has_fin": bool(akeys or qkeys)}


def score(rows):
    """시장별 백분위 → 가중 합. 결측은 해당 항목 평균(50)으로 두고 결측 수를 기록."""
    for us in (False, True):
        grp = [x for x in rows if x["us"] == us]
        def col(k):
            return [x.get(k) for x in grp]
        # 섹터 내 상대강도(3M): 같은 섹터 종목 3M 중앙값 대비
        by_sec = {}
        for x in grp:
            x["sector_key"] = str(x.get("sector") or "?").split("(")[0]
            by_sec.setdefault(x["sector_key"], []).append(x.get("m3"))
        for x in grp:
            vals = sorted(v for v in by_sec.get(x["sector_key"], []) if v is not None)
            x["rs3_sector"] = (x["m3"] - vals[len(vals) // 2]) if (vals and x.get("m3") is not None and len(vals) >= 2) else None
        for x in grp:
            miss = 0
            def pr(k, w):
                nonlocal miss
                v = pct_rank(col(k), x.get(k))
                if v is None:
                    miss += 1
                    v = 50.0
                return v * w / 100
            g = pr("cagr3", 12) + pr("rev_yoy_q", 12) + pr("fwd", 6)
            p = pr("rs3", 10) + pr("rs3_sector", 6) + pr("rs6", 8) + (x["guard"] * 6 if x["guard"] is not None else 3)
            qv = pr("opm", 7) + pr("d_opm", 7) + pr("roe", 6) - x.get("sbc_pen", 0)  # KR ROE · US ROA · SBC 페널티
            e = pr("e1", 6) + pr("rev1m", 8) + pr("e2", 6)
            x.update({"G": round(g / 30 * 100, 1), "P": round(p / 30 * 100, 1), "Q": round(max(qv, 0) / 20 * 100, 1), "E": round(e / 20 * 100, 1),
                      "total": round(g + p + max(qv, 0) + e, 1), "missing": miss})
            hg, sp = x["G"] >= 50, x["P"] >= 50
            x["cell"] = "A" if hg and sp else "B" if hg else "C" if sp else "D"
            if not x.get("has_fin"):  # ETF·재무 없음 — 격자 밖(가격만으로 A가 되면 안 된다)
                x["cell"] = "—"
                x["total"] = None
            if x["cell"] == "B":
                keep = (x.get("d_opm") is None or x["d_opm"] >= 0) and (x.get("rev_yoy_q") is None or x["rev_yoy_q"] > 0)
                x["gate"] = "눌림목(이익 유지)" if keep else "탈락 후보(이익 하향)"
    return rows


def main(argv):
    day = date.today().isoformat()
    if "--date" in argv:
        day = argv[argv.index("--date") + 1]
    top = int(argv[argv.index("--top") + 1]) if "--top" in argv else 12
    P, kr, usd = load_universe()
    fdir = os.path.join(FIN_DIR, day)
    os.makedirs(fdir, exist_ok=True)
    fin = {}
    allrec = {**kr, **usd}
    for i, (name, rec) in enumerate(allrec.items()):
        fp = os.path.join(fdir, f"{rec['code']}.json")
        if os.path.exists(fp):
            fin[name] = json.load(io.open(fp, encoding="utf-8"))
            continue
        if "--no-fetch" in argv:
            fin[name] = None
            continue
        fin[name] = fetch_financials(rec["code"], rec["us"])
        io.open(fp, "w", encoding="utf-8").write(json.dumps(fin[name], ensure_ascii=False))
        if i % 20 == 0:
            print(f"  … {i}/{len(allrec)} 재무 수집", flush=True)
        time.sleep(0.15)
    bench = bench_returns()
    sectors = load_sectors(allrec)
    prev, prev_rev = load_prev_prices(30)
    flags = load_flags()
    rows = score([compute(n, r, fin.get(n), bench, sectors.get(n), prev, flags) for n, r in allrec.items()])
    out = {"asof": day, "prices_asof": P.get("updated"), "bench": bench, "prev_rev": prev_rev, "n": len(rows), "rows": rows,
           "weights": {"G": 30, "P": 30, "Q": 20, "E": 20}, "version": "v2",
           "note": "판단 아님 — 후보. 점수는 시장별 백분위. E는 KR/US proxy가 다르다. 섹터 캡 3/10"}
    io.open(os.path.join(ROOT, "intake", "files", f"leader_screen_{day}.json"), "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1))
    for us, lab in ((False, "KR"), (True, "US")):
        grp = sorted([x for x in rows if x["us"] == us and x["total"] is not None], key=lambda x: -x["total"])
        from collections import Counter
        print(f"\n═══ {lab} · {len(grp)}종목 · 벤치 3M {bench[lab]['3M']:+.1f} 6M {bench[lab]['6M']:+.1f} · 칸 {dict(Counter(x['cell'] for x in grp))} · 리비전 기준 {prev_rev}")
        print(f"{'종목':<16}{'총점':>6}{'G':>5}{'P':>5}{'Q':>5}{'E':>5}  칸  CAGR3  qYoY  ΔOPM   RS3  RS3s  Δ추정  판단 섹터")
        f = lambda v, w=6, d=0: (f"{v:{w}.{d}f}" if isinstance(v, (int, float)) else f"{'—':>{w}}")
        for x in grp[:top]:
            print(f"{x['name'][:15]:<16}{x['total']:>6.1f}{x['G']:>5.0f}{x['P']:>5.0f}{x['Q']:>5.0f}{x['E']:>5.0f}  {x['cell']}  {f(x['cagr3'],6)}{f(x['rev_yoy_q'],6)}{f(x['d_opm'],6,1)}{f(x['rs3'],6)}{f(x['rs3_sector'],6)}{f(x['rev1m'],6,1)}  {'●' if x['judged'] else '○'}  {str(x.get('sector') or '')[:14]}{' SBC' if x.get('sbc_pen') else ''}{' ' + x.get('gate','') if x.get('gate') else ''}")
        # 섹터 캡 3/10 균등비중 후보
        picked, cnt = [], {}
        for x in grp:
            sk = x.get("sector_key") or "?"
            if cnt.get(sk, 0) >= 3 or x["cell"] in ("D",) or x.get("gate", "").startswith("탈락"):
                continue
            picked.append(x); cnt[sk] = cnt.get(sk, 0) + 1
            if len(picked) == 10:
                break
        print(f"  ▶ 섹터 캡 3/10 · 균등비중 후보(D·탈락 제외): " + " · ".join(f"{x['name'][:10]}({x['total']:.0f})" for x in picked))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
