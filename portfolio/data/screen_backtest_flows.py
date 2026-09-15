#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""수급·VCP 검증 (2026-09-16) — 사용자 「vcp니 수급이 모델에 들어가 있나」. KR 추적 99종목 · Daum investor/days 3년 · 우리 일봉 캐시.
수급 신호: 외국인·기관 순매수(20d·60d)/20d 평균 거래량 · 외국인 보유비율 변화(20d·60d). VCP 대리: 20d/120d 실현변동성 비(낮을수록 수축) · 20d 고저폭/가격.
→ 다음 3M 수익률과 스피어만 IC · 레짐 분할 · 전반/후반. 판단 아님."""
import io, json, os, sys, time
from datetime import date, timedelta
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "portfolio", "data")); sys.path.insert(0, os.path.join(ROOT, "intake"))
import screen_backtest as bt
import collect_sources as cs
import update_prices as up
FDIR = os.path.join(ROOT, "intake", "files", "flows_daily"); os.makedirs(FDIR, exist_ok=True)
today = date.today()
names = {n: c for n, c in {**up.TICKERS, **up.WATCH}.items()}
F = {}
for i, (n, c) in enumerate(names.items()):
    fp = os.path.join(FDIR, f"{c}.json")
    if os.path.exists(fp):
        F[n] = json.load(io.open(fp, encoding="utf-8")); continue
    rows = []
    for pg in (1, 2, 3, 4):
        try:
            r = cs.daum_stock_investor_days(c, pg, 200)
        except Exception:
            r = []
        if not r:
            break
        rows += r
        time.sleep(0.08)
    if rows:
        rows = sorted(rows, key=lambda x: x["date"])
        F[n] = [{"d": x["date"][:10].replace("-", ""), "f": x.get("foreignStraightPurchaseVolume") or 0, "i": x.get("institutionStraightPurchaseVolume") or 0,
                 "v": x.get("accTradeVolume") or 0, "fr": x.get("foreignOwnSharesRate")} for x in rows]
        io.open(fp, "w", encoding="utf-8").write(json.dumps(F[n]))
    if i % 20 == 0:
        print(f"  … {i}/{len(names)}", flush=True)
print("flows:", len(F))
S = {n: json.load(io.open(os.path.join(bt.DAILY, f"{c}.json"), encoding="utf-8")) for n, c in names.items() if os.path.exists(os.path.join(bt.DAILY, f"{c}.json"))}
ix = bt.fetch_index("KOSPI", False, (today - timedelta(days=int(365 * 3.6))).strftime("%Y%m%d"), today.strftime("%Y%m%d"))
mes = bt.month_ends((today - timedelta(days=int(365 * 3.2))).strftime("%Y%m%d"), today.strftime("%Y%m%d"))
dates = [m for m in mes if (today - date(int(m[:4]), int(m[4:6]), int(m[6:]))).days >= 92][-34:]
keys = ("F20", "F60", "I20", "I60", "FI20", "dFR20", "dFR60", "VOLRATIO", "RANGE20", "VCP_COMBO")
rows = {k: [] for k in keys}; reg = {}
for d in dates:
    dd = date(int(d[:4]), int(d[4:6]), int(d[6:])); fwd = (dd + timedelta(days=92)).strftime("%Y%m%d")
    b3 = bt.ret(ix, (dd - timedelta(days=91)).strftime("%Y%m%d"), d)
    sig = {k: [] for k in keys}; ys = []
    for n in names:
        fl = [x for x in F.get(n, []) if x["d"] <= d]
        s = S.get(n)
        if not s or len(fl) < 70:
            for k in keys: sig[k].append(None)
            ys.append(None); continue
        w20, w60 = fl[-20:], fl[-60:]
        av = sum(x["v"] for x in w20) / 20 or 1
        sig["F20"].append(sum(x["f"] for x in w20) / av); sig["F60"].append(sum(x["f"] for x in w60) / (3 * av))
        sig["I20"].append(sum(x["i"] for x in w20) / av); sig["I60"].append(sum(x["i"] for x in w60) / (3 * av))
        sig["FI20"].append(sum(x["f"] + x["i"] for x in w20) / av)
        fr = [x["fr"] for x in fl if x["fr"] is not None]
        sig["dFR20"].append((fr[-1] - fr[-21]) if len(fr) > 21 else None); sig["dFR60"].append((fr[-1] - fr[-61]) if len(fr) > 61 else None)
        px = [p for dd_, p in s if dd_ <= d]
        if len(px) > 130:
            r = [px[i] / px[i - 1] - 1 for i in range(1, len(px))]
            def sd(v):
                m = sum(v) / len(v); return (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5
            vr = sd(r[-20:]) / sd(r[-120:]) if sd(r[-120:]) else None
            rg = (max(px[-20:]) - min(px[-20:])) / px[-1]
            sig["VOLRATIO"].append(vr); sig["RANGE20"].append(rg)
            hi52 = px[-1] / max(px[-252:])
            sig["VCP_COMBO"].append(((1 - (vr or 1)) + (hi52 - 0.9) * 2) if vr is not None else None)  # 수축 + 고점 근접
        else:
            for k in ("VOLRATIO", "RANGE20", "VCP_COMBO"): sig[k].append(None)
        ys.append(bt.ret(s, d, fwd))
    for k in keys:
        ic, n_ = bt.spearman(sig[k], ys)
        if ic is not None:
            rows[k].append(ic); reg.setdefault((k, "up" if (b3 or 0) > 0 else "down"), []).append(ic)
print("═══ KR 99 · %d개월 · 신호→다음 3M IC (VOLRATIO·RANGE20 은 낮을수록 수축 = 음의 IC 가 「수축이 좋다」)" % len(dates))
out = {}
for k, v in rows.items():
    if not v: continue
    m = sum(v) / len(v); s_ = (sum((x - m) ** 2 for x in v) / max(1, len(v) - 1)) ** 0.5; h = len(v) // 2
    u_, d_ = reg.get((k, "up"), []), reg.get((k, "down"), [])
    out[k] = {"ic": round(m, 3), "t": round(m / (s_ / len(v) ** 0.5), 2) if s_ else None, "hit": round(sum(1 for x in v if x > 0) / len(v), 2), "half": (round(sum(v[:h]) / h, 3), round(sum(v[h:]) / (len(v) - h), 3)), "up": round(sum(u_) / len(u_), 3) if u_ else None, "down": round(sum(d_) / len(d_), 3) if d_ else None, "months": len(v)}
    print("  %-10s IC %+.3f  t %5s  양 %.0f%%  전반/후반 %+.3f/%+.3f  상승기 %s  하락기 %s  (%d)" % (k, out[k]["ic"], out[k]["t"], 100 * out[k]["hit"], *out[k]["half"], out[k]["up"], out[k]["down"], len(v)))
io.open(os.path.join(ROOT, "intake", "files", f"backtest_flows_kr_{today.isoformat()}.json"), "w", encoding="utf-8").write(json.dumps({"n": len(F), "months": len(dates), "ic": out}, ensure_ascii=False, indent=1))
