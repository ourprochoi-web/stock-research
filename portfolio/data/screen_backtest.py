#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""스크린 팩터 검증 v1 (2026-09-15 밤) — 「이 모델이 맞는지」를 우리 유니버스의 과거로 잰다.

무엇을 재나: 모멘텀(1M·3M·6M·12M 상대강도)이 다음 1M·3M 수익률을 설명했는가. 섹터 ETF 국면 규칙이 다음 3M을 갈랐는가.
어떻게: 네이버 일봉 2년(189종목 + ETF 36 + 지수 2) → 월말마다 횡단면 → 스피어만 IC · 상위-하위 5분위 스프레드 · 승률.
한계: 재무 팩터(G·Q·E)는 시점별(point-in-time) 재무가 없어 못 잰다 — 가격 축(P)만. 표본은 우리 유니버스(생존 편향: 지금 추적하는 종목 = 이미 오른 종목이 많다).
용법: screen_backtest.py [--fetch] [--months 18]
출력: intake/files/backtest_{date}.json + 표. 판단 아님.
"""
import io
import json
import os
import sys
import time
import urllib.request
from datetime import date, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DAILY = os.path.join(ROOT, "intake", "files", "prices_daily")
UA = {"User-Agent": "Mozilla/5.0"}
sys.path.insert(0, os.path.join(ROOT, "portfolio", "data"))


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=12) as r:
            return json.loads(r.read())
    except Exception:  # noqa: BLE001
        return None


def fetch_daily(code, us, start, end):
    base = "https://api.stock.naver.com/chart/foreign/item/" if us else "https://api.stock.naver.com/chart/domestic/item/"
    d = get(f"{base}{code}/day?startDateTime={start}&endDateTime={end}")
    if not d:
        return None
    return [(x["localDate"], float(x["closePrice"])) for x in d if x.get("closePrice")]


def fetch_index(sym, us, start, end):
    base = "https://api.stock.naver.com/chart/foreign/index/" if us else "https://api.stock.naver.com/chart/domestic/index/"
    d = get(f"{base}{sym}/day?startDateTime={start}&endDateTime={end}")
    return [(x["localDate"], float(x["closePrice"])) for x in d if x.get("closePrice")] if d else None


def universe():
    import update_prices as up
    u = {}
    for n, c in {**up.TICKERS, **up.WATCH}.items():
        u[n] = (c, False, "stock")
    for n, c in getattr(up, "WATCH_KR_ETF", {}).items():
        u[n] = (c, False, "etf")
    for n, c in up.WATCH_US.items():
        u[n] = (c, True, "stock")
    for n, c in getattr(up, "WATCH_US_ETF", {}).items():
        u[n] = (c, True, "etf")
    return u


def load_or_fetch(u, start, end, fetch):
    os.makedirs(DAILY, exist_ok=True)
    out = {}
    for i, (n, (c, us, kind)) in enumerate(u.items()):
        fp = os.path.join(DAILY, f"{c}.json")
        if os.path.exists(fp) and not fetch:
            out[n] = json.load(io.open(fp, encoding="utf-8"))
            continue
        s = fetch_daily(c, us, start, end)
        if s:
            out[n] = s
            io.open(fp, "w", encoding="utf-8").write(json.dumps(s))
        if i % 25 == 0:
            print(f"  … {i}/{len(u)}", flush=True)
        time.sleep(0.12)
    return out


def px_on(series, d):
    """d 이전 마지막 종가"""
    last = None
    for dd, p in series:
        if dd <= d:
            last = p
        else:
            break
    return last


def ret(series, d0, d1):
    a, b = px_on(series, d0), px_on(series, d1)
    return (b / a - 1) if a and b else None


def spearman(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    if n < 8:
        return None, n
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for k, i in enumerate(s):
            r[i] = k + 1
        return r
    rx, ry = rank([p[0] for p in pairs]), rank([p[1] for p in pairs])
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1)), n


def quintile_spread(xs, ys):
    pairs = sorted([(x, y) for x, y in zip(xs, ys) if x is not None and y is not None], key=lambda p: p[0])
    n = len(pairs)
    if n < 10:
        return None
    q = max(1, n // 5)
    lo = sum(p[1] for p in pairs[:q]) / q
    hi = sum(p[1] for p in pairs[-q:]) / q
    return hi - lo


def month_ends(start, end):
    d = date.fromisoformat(start[:4] + "-" + start[4:6] + "-" + start[6:])
    e = date.fromisoformat(end[:4] + "-" + end[4:6] + "-" + end[6:])
    out = []
    cur = date(d.year, d.month, 1)
    while cur <= e:
        nxt = date(cur.year + (cur.month // 12), cur.month % 12 + 1, 1)
        me = nxt - timedelta(days=1)
        if me <= e:
            out.append(me.strftime("%Y%m%d"))
        cur = nxt
    return out


def main(argv):
    fetch = "--fetch" in argv
    months = int(argv[argv.index("--months") + 1]) if "--months" in argv else 18
    today = date.today()
    end = today.strftime("%Y%m%d")
    start = (today - timedelta(days=int(365 * 3.6))).strftime("%Y%m%d")
    u = universe()
    print(f"유니버스 {len(u)} · {start}~{end}")
    S = load_or_fetch(u, start, end, fetch)
    idx = {"KR": fetch_index("KOSPI", False, start, end), "US": fetch_index(".INX", True, start, end)}
    mes = month_ends(start, end)
    # 마지막 3개월은 forward 3M이 없으므로 제외
    signal_dates = [m for m in mes if (today - date(int(m[:4]), int(m[4:6]), int(m[6:]))).days >= 31][-months:]
    W = {"1M": 21, "3M": 63, "6M": 126, "12M": 252}
    results = {"asof": today.isoformat(), "n_dates": len(signal_dates), "dates": signal_dates, "by_market": {}, "phase": {}}
    for mk in ("KR", "US"):
        names = [n for n, (c, us, k) in u.items() if (us == (mk == "US")) and k == "stock" and n in S]
        ix = idx[mk]
        rows = {f"{w}_{h}": {"ic": [], "spread": [], "n": []} for w in ("1M", "3M", "6M", "12M", "RS3", "RS6", "RS12", "VOLADJ3", "VOLADJ6", "HI52", "MOM6_1") for h in ("f1", "f3")}
        for d in signal_dates:
            dd = date(int(d[:4]), int(d[4:6]), int(d[6:]))
            def shift(days):
                return (dd - timedelta(days=days)).strftime("%Y%m%d")
            fwd1 = (dd + timedelta(days=31)).strftime("%Y%m%d")
            fwd3 = (dd + timedelta(days=92)).strftime("%Y%m%d")
            has_f3 = (today - dd).days >= 92
            sig = {w: [] for w in ("1M", "3M", "6M", "12M", "RS3", "RS6", "RS12", "VOLADJ3", "VOLADJ6", "HI52", "MOM6_1")}
            f1, f3 = [], []
            bi = {w: ret(ix, shift(int(W[w] * 1.45)), d) for w in ("3M", "6M", "12M")} if ix else {}
            for n in names:
                s = S[n]
                r1 = ret(s, shift(30), d); r3 = ret(s, shift(91), d); r6 = ret(s, shift(182), d); r12 = ret(s, shift(365), d)
                sig["1M"].append(r1); sig["3M"].append(r3); sig["6M"].append(r6); sig["12M"].append(r12)
                # 변동성 조정: 수익률 / 일별 수익률 표준편차(같은 창)
                win = [pp for dd_, pp in s if shift(91) <= dd_ <= d]
                if len(win) > 20:
                    dr = [win[i] / win[i - 1] - 1 for i in range(1, len(win))]
                    mu = sum(dr) / len(dr); sd = (sum((x - mu) ** 2 for x in dr) / (len(dr) - 1)) ** 0.5
                    sig["VOLADJ3"].append((r3 / sd) if (sd and r3 is not None) else None)
                else:
                    sig["VOLADJ3"].append(None)
                win6 = [pp for dd_, pp in s if shift(182) <= dd_ <= d]
                if len(win6) > 40:
                    dr = [win6[i] / win6[i - 1] - 1 for i in range(1, len(win6))]
                    mu = sum(dr) / len(dr); sd = (sum((x - mu) ** 2 for x in dr) / (len(dr) - 1)) ** 0.5
                    sig["VOLADJ6"].append((r6 / sd) if (sd and r6 is not None) else None)
                else:
                    sig["VOLADJ6"].append(None)
                # 52주 고점 근접도(George-Hwang): 현재가 / 52주 최고
                w52 = [pp for dd_, pp in s if shift(365) <= dd_ <= d]
                sig["HI52"].append((px_on(s, d) / max(w52)) if (w52 and px_on(s, d)) else None)
                # 6-1 모멘텀(최근 1개월 제외): (1+r6)/(1+r1) − 1
                sig["MOM6_1"].append(((1 + r6) / (1 + r1) - 1) if (r6 is not None and r1 is not None) else None)
                sig["RS3"].append((r3 - bi["3M"]) if (r3 is not None and bi.get("3M") is not None) else None)
                sig["RS6"].append((r6 - bi["6M"]) if (r6 is not None and bi.get("6M") is not None) else None)
                sig["RS12"].append((r12 - bi["12M"]) if (r12 is not None and bi.get("12M") is not None) else None)
                f1.append(ret(s, d, fwd1))
                f3.append(ret(s, d, fwd3) if has_f3 else None)
            for w in sig:
                for h, fv in (("f1", f1), ("f3", f3)):
                    ic, n = spearman(sig[w], fv)
                    if ic is not None:
                        rows[f"{w}_{h}"]["ic"].append(ic); rows[f"{w}_{h}"]["n"].append(n)
                        sp = quintile_spread(sig[w], fv)
                        if sp is not None:
                            rows[f"{w}_{h}"]["spread"].append(sp)
        # 전반/후반 분할 — 가중이 표본 전체로 골라진 in-sample 이므로 절반씩의 IC 부호가 같은지 본다
        half = {}
        for k, v in rows.items():
            if len(v["ic"]) >= 8:
                h = len(v["ic"]) // 2
                a_, b_ = v["ic"][:h], v["ic"][h:]
                half[k] = (round(sum(a_) / len(a_), 3), round(sum(b_) / len(b_), 3))
        results.setdefault("split", {})[mk] = half
        summ = {}
        for k, v in rows.items():
            if v["ic"]:
                m = sum(v["ic"]) / len(v["ic"])
                sd = (sum((x - m) ** 2 for x in v["ic"]) / max(1, len(v["ic"]) - 1)) ** 0.5
                summ[k] = {"ic_mean": round(m, 3), "ic_t": round(m / (sd / len(v["ic"]) ** 0.5), 2) if sd > 0 else None, "hit": round(sum(1 for x in v["ic"] if x > 0) / len(v["ic"]), 2),
                           "spread_mean_pct": round(100 * sum(v["spread"]) / len(v["spread"]), 2) if v["spread"] else None, "months": len(v["ic"]), "n_avg": round(sum(v["n"]) / len(v["n"]))}
        results["by_market"][mk] = summ
        print(f"\n═══ {mk} · 종목 {len(names)} · 시점 {len(signal_dates)} — 신호 → 다음 1M(f1)·3M(f3) · 스피어만 IC 평균 / t / 양의 비율 / 상위−하위 5분위 스프레드")
        for k in ("1M_f1", "3M_f1", "6M_f1", "12M_f1", "RS3_f1", "RS6_f1", "VOLADJ3_f1", "HI52_f1", "MOM6_1_f1", "1M_f3", "3M_f3", "6M_f3", "12M_f3", "RS3_f3", "RS6_f3", "RS12_f3", "VOLADJ3_f3", "VOLADJ6_f3", "HI52_f3", "MOM6_1_f3"):
            v = summ.get(k)
            if v:
                hs = half.get(k)
                print(f"  {k:<10} IC {v['ic_mean']:+.3f}  t {v['ic_t']!s:>5}  양 {v['hit']:.0%}  스프레드 {v['spread_mean_pct']!s:>6}%  ({v['months']}개월 · n≈{v['n_avg']})  전반/후반 {hs[0]:+.3f}/{hs[1]:+.3f}" if hs else f"  {k:<10} IC {v['ic_mean']:+.3f}  t {v['ic_t']!s:>5}  양 {v['hit']:.0%}  ({v['months']}개월)")
    # 섹터 ETF 유니버스(생존 편향 없음)에서 모멘텀 IC — 표본 작음(시장당 18)
    for mk in ("KR", "US"):
        names = [n for n, (c, us, k) in u.items() if (us == (mk == "US")) and k == "etf" and n in S]
        ics = {"3M": [], "6M": [], "12M": [], "1M": []}
        for d in signal_dates:
            dd = date(int(d[:4]), int(d[4:6]), int(d[6:]))
            if (today - dd).days < 92:
                continue
            def shift(days):
                return (dd - timedelta(days=days)).strftime("%Y%m%d")
            fwd3 = (dd + timedelta(days=92)).strftime("%Y%m%d")
            xs = {"1M": [], "3M": [], "6M": [], "12M": []}; ys = []
            for n in names:
                xs["1M"].append(ret(S[n], shift(30), d)); xs["3M"].append(ret(S[n], shift(91), d)); xs["6M"].append(ret(S[n], shift(182), d)); xs["12M"].append(ret(S[n], shift(365), d)); ys.append(ret(S[n], d, fwd3))
            for w in ics:
                ic, n_ = spearman(xs[w], ys)
                if ic is not None:
                    ics[w].append(ic)
        results.setdefault("etf_ic", {})[mk] = {w: {"ic_mean": round(sum(v) / len(v), 3), "hit": round(sum(1 for x in v if x > 0) / len(v), 2), "months": len(v)} for w, v in ics.items() if v}
        print(f"\n═══ {mk} 섹터 ETF 유니버스(생존편향 없음) 모멘텀→f3 IC: " + " · ".join(f"{w} {v['ic_mean']:+.3f}({v['hit']:.0%}, {v['months']}m)" for w, v in results["etf_ic"][mk].items()))
    # 섹터 ETF 국면 규칙 — 벤치마크 둘(지수 · 섹터 ETF 동일가중 평균) → 다음 3M 상대수익 · 절대수익
    sys.path.insert(0, os.path.join(ROOT, "portfolio", "data"))
    from leader_screen import sector_phase
    for mk in ("KR", "US"):
        names = [n for n, (c, us, k) in u.items() if (us == (mk == "US")) and k == "etf" and n in S]
        ix = idx[mk]
        buckets = {"idx": {}, "ew": {}, "abs": {}}
        for d in signal_dates:
            dd = date(int(d[:4]), int(d[4:6]), int(d[6:]))
            if (today - dd).days < 92:
                continue
            def shift(days):
                return (dd - timedelta(days=days)).strftime("%Y%m%d")
            fwd3 = (dd + timedelta(days=92)).strftime("%Y%m%d")
            b1, b3, b6, bf = ret(ix, shift(30), d), ret(ix, shift(91), d), ret(ix, shift(182), d), ret(ix, d, fwd3)
            if None in (b1, b3, b6, bf):
                continue
            rr = {n: (ret(S[n], shift(30), d), ret(S[n], shift(91), d), ret(S[n], shift(182), d), ret(S[n], d, fwd3)) for n in names}
            rr = {n: v for n, v in rr.items() if None not in v}
            if len(rr) < 6:
                continue
            ew = [sum(v[i] for v in rr.values()) / len(rr) for i in range(4)]
            for n, (r1, r3, r6, rf) in rr.items():
                ph_idx = sector_phase((r6 - b6) * 100, (r3 - b3) * 100, (r1 - b1) * 100)
                ph_ew = sector_phase((r6 - ew[2]) * 100, (r3 - ew[1]) * 100, (r1 - ew[0]) * 100)
                buckets["idx"].setdefault(ph_idx, []).append((rf - bf) * 100)
                buckets["ew"].setdefault(ph_ew, []).append((rf - ew[3]) * 100)
                buckets["abs"].setdefault(ph_ew, []).append(rf * 100)
        results["phase"][mk] = {}
        for bk, lab in (("idx", "지수 대비(국면도 지수 기준)"), ("ew", "섹터 동일가중 대비(국면도 EW 기준)"), ("abs", "절대수익(국면 EW 기준)")):
            results["phase"][mk][bk] = {k: {"n": len(v), "fwd3": round(sum(v) / len(v), 2), "hit": round(sum(1 for x in v if x > 0) / len(v), 2)} for k, v in buckets[bk].items()}
            print(f"\n═══ {mk} 섹터 ETF 국면 → 다음 3M · {lab}")
            for k, v in sorted(results["phase"][mk][bk].items(), key=lambda kv: -kv[1]["fwd3"]):
                print(f"  {k:<10} {v['fwd3']:+6.2f}%  양 {v['hit']:.0%}  n={v['n']}")
    # 레짐 분할 — 지수 3M 부호별 IC(3M RS → f3) · 복합(3M+6M 평균 순위) · 재무 QoQ point-in-time
    for mk in ("KR", "US"):
        names = [n for n, (c, us, k) in u.items() if (us == (mk == "US")) and k == "stock" and n in S]
        ix = idx[mk]
        reg = {"up": [], "down": []}; comp = []; fund = []
        fdir = os.path.join(ROOT, "intake", "files", "financials")
        latest = sorted(os.listdir(fdir))[-1] if os.path.exists(fdir) else None
        for d in signal_dates:
            dd = date(int(d[:4]), int(d[4:6]), int(d[6:]))
            if (today - dd).days < 92:
                continue
            def shift(days):
                return (dd - timedelta(days=days)).strftime("%Y%m%d")
            fwd3 = (dd + timedelta(days=92)).strftime("%Y%m%d")
            b3, b6 = ret(ix, shift(91), d), ret(ix, shift(182), d)
            if b3 is None or b6 is None:
                continue
            s3, s6, sc, f3 = [], [], [], []
            for n in names:
                r3, r6, rf = ret(S[n], shift(91), d), ret(S[n], shift(182), d), ret(S[n], d, fwd3)
                s3.append((r3 - b3) if r3 is not None else None); s6.append((r6 - b6) if r6 is not None else None); f3.append(rf)
            ic3, _ = spearman(s3, f3)
            if ic3 is not None:
                reg["up" if b3 > 0 else "down"].append(ic3)
            # HI52 · VOLADJ6 도 레짐별로
            hi, va = [], []
            for n in names:
                sr = S[n]; px = [pp for dd_, pp in sr if dd_ <= d]
                w52 = px[-252:] if len(px) >= 252 else px
                hi.append((px[-1] / max(w52)) if px else None)
                w6 = px[-126:]
                if len(w6) > 40:
                    dr = [w6[i] / w6[i - 1] - 1 for i in range(1, len(w6))]
                    mu = sum(dr) / len(dr); sd = (sum((x - mu) ** 2 for x in dr) / (len(dr) - 1)) ** 0.5
                    va.append(((w6[-1] / w6[0] - 1) / sd) if sd else None)
                else:
                    va.append(None)
            for key, sig_ in (("hi52", hi), ("voladj6", va)):
                icx, _ = spearman(sig_, f3)
                if icx is not None:
                    reg.setdefault(f"{key}_{'up' if b3 > 0 else 'down'}", []).append(icx)
            # 복합 = 3M RS 순위 + 6M RS 순위
            def rk(v):
                idxs = [i for i, x in enumerate(v) if x is not None]
                order = sorted(idxs, key=lambda i: v[i]); r = [None] * len(v)
                for k, i in enumerate(order):
                    r[i] = k
                return r
            r3, r6 = rk(s3), rk(s6)
            sc = [((a or 0) + (b or 0)) if (a is not None and b is not None) else None for a, b in zip(r3, r6)]
            icc, _ = spearman(sc, f3)
            if icc is not None:
                comp.append(icc)
        # 재무 QoQ(매출·OPM) point-in-time: 분기말 + 60일을 「알려진 날」로
        if latest:
            import update_prices as up
            code_of = {n: c for n, (c, us, k) in u.items()}
            per_q = {}
            for n in names:
                fp = os.path.join(fdir, latest, f"{code_of[n]}.json")
                if not os.path.exists(fp):
                    continue
                fin = json.load(io.open(fp, encoding="utf-8"))
                q = (fin or {}).get("quarter") or {}
                ks = sorted(k for k, v in q.items() if not v.get("cx"))
                for i in range(1, len(ks)):
                    r0, r1 = q[ks[i - 1]].get("매출액"), q[ks[i]].get("매출액")
                    o0, o1 = q[ks[i - 1]].get("영업이익", q[ks[i - 1]].get("EBIT")), q[ks[i]].get("영업이익", q[ks[i]].get("EBIT"))
                    if not (r0 and r1) or o0 is None or o1 is None:
                        continue
                    per_q.setdefault(ks[i], []).append((n, r1 / r0 - 1, o1 / r1 - o0 / r0))
            fund_rows = []
            for k, lst in sorted(per_q.items()):
                # 분기말 → 알려진 날 = +60일 · 그날부터 3M forward
                y, m = int(k[:4]), int(k[4:6]) if len(k) == 6 else int(k[5:7])
                pe = date(y, m, 28) + timedelta(days=4); pe = pe - timedelta(days=pe.day)
                known = (pe + timedelta(days=60)).strftime("%Y%m%d"); fwd = (pe + timedelta(days=152)).strftime("%Y%m%d")
                if (today - (pe + timedelta(days=152))).days < 0:
                    continue
                xs_r, xs_o, ys = [], [], []
                for n, gr, dop in lst:
                    rf = ret(S[n], known, fwd)
                    xs_r.append(gr); xs_o.append(dop); ys.append(rf)
                ic_r, n1 = spearman(xs_r, ys); ic_o, _ = spearman(xs_o, ys)
                if ic_r is not None:
                    fund_rows.append((k, ic_r, ic_o, n1, quintile_spread(xs_r, ys), quintile_spread(xs_o, ys)))
            results.setdefault("fund", {})[mk] = [{"q": r[0], "ic_rev_qoq": round(r[1], 3), "ic_opm_qoq": round(r[2], 3) if r[2] is not None else None, "n": r[3], "spread_rev": round(100 * r[4], 2) if r[4] is not None else None, "spread_opm": round(100 * r[5], 2) if r[5] is not None else None} for r in fund_rows]
            print(f"\n═══ {mk} 재무 QoQ(분기말+60일 시점) → 다음 3M · 분기별 IC(매출 QoQ · ΔOPM QoQ) · 5분위 스프레드")
            for r in fund_rows:
                print(f"  {r[0]:<10} IC 매출 {r[1]:+.3f} · ΔOPM {r[2] if r[2] is None else round(r[2],3):+}  n={r[3]}  스프레드 매출 {r[4] and round(100*r[4],1)}% · ΔOPM {r[5] and round(100*r[5],1)}%")
        results.setdefault("regime", {})[mk] = {k: {"ic_mean": round(sum(v) / len(v), 3) if v else None, "months": len(v)} for k, v in reg.items()}
        print(f"\n═══ {mk} 레짐별 IC(→f3): " + " · ".join(f"{k} {v['ic_mean']}({v['months']}m)" for k, v in results['regime'][mk].items()))
        results.setdefault("composite", {})[mk] = {"ic_mean": round(sum(comp) / len(comp), 3) if comp else None, "hit": round(sum(1 for x in comp if x > 0) / len(comp), 2) if comp else None}
        print(f"\n═══ {mk} 레짐 분할 — 3M RS→f3 IC: 지수 3M 상승기 {results['regime'][mk]['up']} · 하락기 {results['regime'][mk]['down']} | 복합(3M+6M RS 순위) IC {results['composite'][mk]}")
    io.open(os.path.join(ROOT, "intake", "files", f"backtest_{today.isoformat()}.json"), "w", encoding="utf-8").write(json.dumps(results, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
