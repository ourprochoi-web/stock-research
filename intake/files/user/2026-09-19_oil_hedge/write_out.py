import json, csv
R=json.load(open("results.json")); V=json.load(open("valuation.json")); C=json.load(open("conditional.json"))
FL=json.load(open("fetch_log.json")); SL=json.load(open("sec_log.json")); SL2=json.load(open("sec_log2.json"))
st=R["stats"]; sp=R["spike"]
names={"XLE":"XLE(에너지 섹터 ETF)","XOP":"XOP(E&P ETF)","USO":"USO(WTI 선물 ETF · 대조군)","BNO":"BNO(브렌트 선물 ETF · 대조군)","LNG":"Cheniere","WMB":"Williams","KMI":"Kinder Morgan","ET":"Energy Transfer","TRGP":"Targa","EPD":"Enterprise Products","FANG":"Diamondback","EOG":"EOG","COP":"ConocoPhillips","EQT":"EQT","CVX":"Chevron","XOM":"Exxon","VG":"Venture Global","S-Oil":"S-Oil(010950 · 대조군)","SKInnovation":"SK이노베이션(096770 · 대조군)","SPY":"SPY(대조군)"}
def g(sym,k,f="beta"): return (st[sym].get(k) or {}).get(f)
rows=[]
for sym in names:
    kc=g(sym,"kospi_2026war_lag1","r"); b=g(sym,"brent_2026war")
    if sym in ("S-Oil","SKInnovation"): kc=g(sym,"kospi_2026war","r")
    hq=round(b*(1-kc),3) if (b is not None and kc is not None) else None
    rows.append({"name":names[sym],"symbol":sym,"n_days":g(sym,"brent_2026war","n"),"n_days_250":g(sym,"brent_250d","n"),
      "beta_brent":b,"r2_brent":g(sym,"brent_2026war","r2"),"beta_brent_250d":g(sym,"brent_250d"),"r2_brent_250d":g(sym,"brent_250d","r2"),
      "beta_wti":g(sym,"wti_2026war"),"r2_wti":g(sym,"wti_2026war","r2"),
      "corr_kospi":kc,"corr_kospi_sameday":g(sym,"kospi_2026war","r"),"corr_skh":g(sym,"skh_2026war_lag1","r") if sym not in ("S-Oil","SKInnovation") else g(sym,"skh_2026war","r"),"corr_spy":g(sym,"spy_2026war","r"),
      "hedge_quality":hq,
      "spike_window_returns":{
        "up1_20260304-20260318_brent+44.8%":sp["up1"]["returns"][sym],
        "up2_20260709-20260723_brent+41.5%":sp["up2"]["returns"][sym],
        "down1_20260610-20260624_brent-24.7%":sp["down1"]["returns"][sym],
        "down2_20260407-20260421_brent-23.2%":sp["down2"]["returns"][sym],
        "war_onset_20260227-20260318_brent+65.6%":C["fixed_20260227-20260318"]["returns"][sym],
        "sep_spike_20260828-20260915_brent+45.7%":C["fixed_20260828-20260915"]["returns"][sym]},
      "kospi_worst_window_returns":{k.replace("kospi_worst_",""):v["returns"].get(sym) for k,v in C.items() if k.startswith("kospi_worst")},
      "px_chg_1y":V.get(sym,{}).get("px_chg_1y")})
rows.sort(key=lambda r:-(r["hedge_quality"] if r["hedge_quality"] is not None else -9))
with open("beta_table.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["symbol","n_days_2026war","beta_brent_2026war","r2","beta_brent_250d","r2_250d","beta_wti_2026war","corr_kospi_lag1","corr_skh_lag1","corr_spy","hedge_quality","up1","up2","down1","down2","war_onset","sep_spike","kospi_worst_0715-0730","kospi_worst_0630-0714","kospi_worst_0226-0313","px_chg_1y"])
    for r in rows:
        s=r["spike_window_returns"]; kw=r["kospi_worst_window_returns"]
        w.writerow([r["symbol"],r["n_days"],r["beta_brent"],r["r2_brent"],r["beta_brent_250d"],r["r2_brent_250d"],r["beta_wti"],r["corr_kospi"],r["corr_skh"],r["corr_spy"],r["hedge_quality"]]+list(s.values())+[kw.get("20260715-20260730"),kw.get("20260630-20260714"),kw.get("20260226-20260313"),r["px_chg_1y"]])
portfolio_side={
 "KOSPI_daily_lag1_2026war":{"beta":-0.116,"r":-0.13,"r2":0.017,"n":137},
 "SKH_daily_lag1_2026war":{"beta":-0.164,"r":-0.116,"r2":0.013,"n":137},
 "KOSPI_20d_blocks_since_2025-09":C["block20_since_2025-09"]["KOSPI"],
 "SKH_20d_blocks_since_2025-09":C["block20_since_2025-09"]["SKH"],
 "S-Oil_20d_blocks_since_2025-09":C["block20_since_2025-09"]["S-Oil"],
 "kospi_worst_windows_2026":{k.replace("kospi_worst_",""):{"kospi":v["kospi_move"],"skh":v["returns"]["SKH"],"brent":v["returns"]["DCOILBRENTEU"],"uso":v["returns"]["USO"],"vg":v["returns"]["VG"],"fang":v["returns"]["FANG"],"xop":v["returns"]["XOP"],"cop":v["returns"]["COP"],"xle":v["returns"]["XLE"],"lng":v["returns"]["LNG"],"wmb":v["returns"]["WMB"],"s_oil":v["returns"]["S-Oil"],"spy":v["returns"]["SPY"]} for k,v in C.items() if k.startswith("kospi_worst")},
 "read":"2026년 코스피 최악 10일 창 셋(−23%·−19%·−13%)에서 브렌트는 셋 다 올랐다(+10%·+14%·+45%). 유가 연동 수단은 셋 다 플러스였다 — 다만 E&P 주식은 +4~12%, USO·VG는 +8~48%. 반대로 유가 완화 창(6/10~24 브렌트 −25%)에선 USO·VG −21%, SKH +42% — 헤지의 대가는 큰데 포트 이득이 훨씬 크다. 일별 회귀는 코스피 R² 0.02(약함) · 20일 블록 r −0.28(n=13) — 유가는 코스피 하락의 원인 중 하나이지 전부가 아니다(7월 창은 FOMC·금리 축)."
}
contract=[
 {"name":"Cheniere(LNG)","fee_based_pct":"장기계약(SPA·IPM) ≈ 90% of anticipated production through mid-2030s · 가중잔여기간 ~15년 · 가격 = 고정 액화수수료 + 115%×HH","source":"10-Q 2026-08-06 (lng-20260630.htm) · 10-K 2026-02-26","grade":"①","note":"스팟 층: 1H26 LNG 매출 $11,362M 중 단기(마케팅) $3,206M = 28% · 물량 1,339 TBtu 중 233 = 17% (①). 브렌트 베타 0.19(R² 0.18) — 「물량 층 + 스팟 옵션 17%」. 유가 헤지 아님, 가스 스프레드 부분 노출","remaining_commodity_exposure":"단기 판매 물량 ~17% (TTF/JKM 연동) + IPM 마진"},
 {"name":"Venture Global(VG)","fee_based_pct":"체결 SPA 47.0 mtpa 중 96%가 20년 고정 액화수수료(take-or-pay) · 45.2 mtpa 20년 + 1.8 mtpa 단·중기","source":"10-K 2026-03-02 (vg-20251231.htm) · 10-Q 2026-08-11 표지: Class A 531,488,393 + Class B 1,968,604,458주","grade":"①","note":"🔑 계약은 96% 고정인데 <지금 현금은> 커미셔닝·초과캐파 카고를 TTF/JKM 연동 DES로 파는 데서 나온다(Plaquemines COD 전 · ①). 그래서 브렌트 베타 0.65(R² 0.40)로 USO와 같은 급 — 단계의 값이지 구조의 값이 아니다. SPA 개시(Plaquemines Ph2 COD · CP2 2027)로 베타는 떨어진다. ND/EBITDA 5.3 · FCF −$70억","remaining_commodity_exposure":"현재 매출의 대부분(커미셔닝·초과캐파 카고 · 비율은 10-Q 본문에 미공시 → [미검증])"},
 {"name":"Kinder Morgan(KMI)","fee_based_pct":"10-K 본문에 %-of-EBITDA 미기재. 잔여이행의무(take-or-pay·MVC 고정대가) 2026잔여 $3B · 2027 $5B · 2028+ $28B","source":"10-Q 2026-07-24 (kmi-20260630.htm) · 10-K 2026-02-13","grade":"①","note":"CO2 세그먼트 원유 헤지 2026 $64.54 · 2027 $63.92 · 2028 $67.x/bbl(①) — 유가 상방을 이미 팔았다. 베타 0.03. 「~64% take-or-pay / 26% fee」는 IR 자료(② · 본 편 미확인)","remaining_commodity_exposure":"CO2 세그먼트 원유(헤지 $64) · G&P의 POP/keep-whole 일부"},
 {"name":"Williams(WMB)","fee_based_pct":"NGL 생산 물량의 93%가 fee-based 계약(2025) · 7% noncash commodity-based(keep-whole·POL) · Transco/NWP 규제 수송(예약요금)","source":"10-K 2026-02-24 (wmb-20251231.htm)","grade":"①","note":"베타 0.03 · FCF 수익률 −0.1%(CapEx/OCF 102%). 순수 물량·데이터센터 가스 수요 층. 유가 헤지 아님","remaining_commodity_exposure":"NGL 마진 노출 ~7% 물량 + G&P 일부"},
 {"name":"Energy Transfer(ET)","fee_based_pct":"10-K는 개별 저장자산에 「100% fee-based」만 명시 · 회사 전체 「~90% fee-based」는 IR 자료(② · 10-K 본문에 없음)","source":"10-K 2026-02-19 (et-20251231.htm) 시장위험 표","grade":"①(민감도)/②(비율)","note":"가상 10% 가격 변동 시 파생 FV 효과: 원유·NGL·제품 $131M · 가스 $9M(①) vs TTM EBITDA $168.7억 → 유가 민감도 미미. 베타 0.06. MLP 과세(T5) 미측정","remaining_commodity_exposure":"마케팅·최적화 마진 · G&P POP 일부"},
 {"name":"Targa(TRGP)","fee_based_pct":"「predominantly fee-based」 · G&P는 POP + fee floor 혼합, Downstream은 fee-based(비율 수치 10-K 본문 미기재)","source":"10-K 2026-02-19 (trgp-20251231.htm) 시장위험 표","grade":"①","note":"가상 10% 가격 상승 시 파생 FV: 가스 −$228M · NGL −$22M · 원유 +$15M(①) — 헤지가 상방을 일부 판다. 베타 0.15 · FCF 수익률 1.2%(재투자 사이클)","remaining_commodity_exposure":"G&P POP 계약(헤지 후 잔여)"},
 {"name":"Enterprise Products(EPD)","fee_based_pct":"fee/commodity 혼합 비율 수치 10-K 본문 미기재(가공은 fee·keepwhole·margin-band·POL·POP 혼합)","source":"10-K 2026-02-27 (epd-20251231.htm) 시장위험 표","grade":"①","note":"마케팅 포트폴리오 10% 가격 변동 시 FV ±$10~20M(①) — 미미. 베타 0.08 · 코스피 상관 −0.22(가장 낮음)이지만 베타가 없어 헤지 품질 0.10. MLP 과세 미측정","remaining_commodity_exposure":"가공 스프레드(NGL $0.59/gal 2025) · 옥탄 · 마케팅"},
 {"name":"Diamondback(FANG)","fee_based_pct":"해당 없음(업스트림). 원유 헤지 = 풋(행사가 $50~55 · 2026 3Q~2027 1Q) + 베이시스/롤 스왑만 · <상한(collar ceiling) 없음>","source":"10-Q 2026-08-05 (fang-20260630.htm) 파생 표","grade":"①","note":"유가 상방이 온전히 열려 있는 유일하게 확인된 E&P. 가스는 HH 2-way collar $2.87~6.35(①). 베타 0.29(R² 0.44) · FCF 수익률 12.1% · ND/EBITDA 1.9. 감액(T4)은 유가 <하락> 때 문제","remaining_commodity_exposure":"원유 ~100% 상방 노출(하방만 $50 풋)"},
 {"name":"ConocoPhillips(COP)","fee_based_pct":"해당 없음. 10-Q 텍스트에서 원유 collar·swap 헤지 표 검출 0건(정책상 무헤지)","source":"10-Q 2026-08-06 (cop-20260630.htm) grep","grade":"①(부재 확인)","note":"베타 0.26(R² 0.41) · P/OCF 7.2 · FCF 수익률 7.3%","remaining_commodity_exposure":"원유·가스 ~100%"},
 {"name":"EQT","fee_based_pct":"해당 없음(가스 E&P). 2026 헤지 25%·2027 16%(hegemony_17 T3 ②)","source":"10-Q 2026-07-22 실현가 표 (eqt-20260630.htm)","grade":"①","note":"브렌트 베타 0.06 — 유가 헤지 아님. HH·데이터센터 가스 테제의 종목","remaining_commodity_exposure":"HH 가스(브렌트 무관)"}
]
valuation=[]
for sym in ["FANG","EOG","COP","CVX","XOM","XOP","XLE","LNG","VG","ET","EPD","KMI","WMB","TRGP","EQT","S-Oil","SKInnovation","USO","BNO"]:
    v=V[sym]; d={"name":names[sym],"symbol":sym,"price_0918":v.get("price_0918"),"px_chg_1y":v.get("px_chg_1y"),"mcap_usd_b":v.get("mcap_usd_b_at_0918"),"ev_ebitda_ttm":v.get("ev_ebitda"),"p_ocf_ttm":v.get("p_ocf"),"fcf_yield":v.get("fcf_yield_at_0918"),"capex_ocf":v.get("capex_ocf"),"net_debt_b":v.get("net_debt_b"),"ttm_asof":"2026-06-30","src":v.get("src") or v.get("note")}
    if sym=="XOM": d["note"]="창이 1H26(TTM 아님) — P/OCF 20.8은 반기 기준이라 연환산 ≈10.4 · FCF 수익률 2.9% → 연환산 ≈5.7%"
    if sym in ("COP","CVX","EPD"): d["note"]="캐시 파일에 영업이익 태그 없음 → EBITDA·EV/EBITDA 미산출(P/OCF·FCF 수익률만)"
    if sym=="FANG": d["note"]="EV/EBITDA 10.4는 감액 포함 보고치 · 감액 조정 시 6.1(페이지 값 09-13)"
    if sym=="VG": d["note"]="시총 = 09-18 $14.02 × 25.0억주(10-Q 표지 ①) = $351억 · 캐시 $388억(② 09월)보다 작음. FCF −$70억 → 수익률 −19.9%"
    if sym in ("S-Oil","SKInnovation"): d.update({"naver_per":v["naver_totalInfos"].get("per"),"naver_cns_per":v["naver_totalInfos"].get("cnsPer"),"pbr":v["naver_totalInfos"].get("pbr"),"mcap_krw":v["naver_totalInfos"].get("marketValue"),"52w":(v["naver_totalInfos"].get("lowPriceOf52Weeks"),v["naver_totalInfos"].get("highPriceOf52Weeks"))})
    valuation.append(d)
out={
 "asof":"2026-09-19 (가격 09-18 종가 · 브렌트/WTI FRED 09-15 · TTM 2026-06-30)",
 "question":"포트(주식 40%·현금 60% · 유가 헤지 0)에 대해 「석유가스」 후보 중 무엇이 호르무즈형 유가 급등의 헤지인가 — 각 수단이 전제하는 것과 반증",
 "data_sources":FL+SL+[{"host":l[0],"path":l[1],"status":str(l[2])} for l in SL2]+[{"host":"m.stock.naver.com","path":"/api/stock/{010950|096770}/integration","status":"ok (PER·시총 ②)"},{"host":"data.sec.gov","path":"/api/xbrl/companyfacts/CIK{1506307|821189|2007855}.json","status":"ok (KMI·EOG TTM 산출 · VG는 dei 주식수 없음 → 10-Q 표지로 대체)"},{"host":"repo","path":"intake/files/sec/_energy17_ttm.json · _ttm_summary.json","status":"ok (11사 TTM ①)"}],
 "method":{"returns":"일별 로그수익률 · 브렌트 = FRED DCOILBRENTEU(Dated 현물) · WTI = DCOILWTICO · 창 = 2026war(2026-03-01~09-18 · n≈137) 및 250d(2025-09-15~ · n≈254)","kospi_corr":"한국 장은 미국 종가에 다음 날 반응 → corr_kospi는 미국 수단 t일 vs 코스피 t+1일(lag1) · 같은 날 값도 병기 · 한국 종목은 같은 날","hedge_quality":"beta_brent(2026war) × (1 − corr_kospi_lag1) · 동률은 FCF 수익률","spike_windows":"2026년 브렌트 10일 최대 상승 창 2개(비중첩) + 최대 하락 창 2개 + 전쟁 개시 창(02-27~03-18) + 9월 급등 창(08-28~09-15) · 한국 지수·종목은 종료일 +1거래일","conditional":"코스피 최악 10일 창 3개에서 각 수단의 수익률(미국 수단은 전일 종가 기준) — 「필요할 때 지불했는가」"},
 "portfolio_side":portfolio_side,
 "beta_table":rows,
 "contract_structure":contract,
 "valuation":valuation,
 "valuation_vs_1y_ago":"배수의 1년 전 값은 미산출(2025-06 TTM 재구성 필요) — 대신 가격 1년 변화(2025-09-25→2026-09-18)를 px_chg_1y로 병기: USO +106% · BNO +99% · S-Oil +155% · TRGP +72% · XLE/XOP +43% · COP +41% · FANG +37% · CVX +32% · VG +1% · EQT +1%",
 "verdict":{
  "ranking_by_hedge_quality":[(r["symbol"],r["hedge_quality"]) for r in rows],
  "hedges":[
   {"name":"USO/BNO(선물 ETF)","beta":"0.67/0.64 · R² 0.73","what_it_presumes":"유가 자체. 다만 <선물>이라 현물 급등(9/15 Dated 130.8 vs 선물 ~106 · +$29 백워데이션 · regime ①)을 다 못 받는다 — 9월 창 브렌트 현물 +46% vs USO +25%. 휴전 시 −20~35%(regime baseline)를 그대로 맞는다","role":"가격 층 · 순수"},
   {"name":"VG","beta":"0.65 · R² 0.40","what_it_presumes":"커미셔닝·초과캐파 카고가 TTF/JKM 스팟에 팔리는 <단계>(①)가 계속된다는 것. 96% 고정 SPA(①)가 개시되면 베타는 구조적으로 떨어진다. ND/EBITDA 5.3·FCF −$70억이라 금리·신용에도 걸린다","role":"가격 층(가스 스프레드 경유) · 단계 의존"},
   {"name":"FANG","beta":"0.29 · R² 0.44","what_it_presumes":"유가 상방 무헤지(풋 $50~55만 · ①) + FCF 수익률 12.1% · ND/EBITDA 1.9 · 코스피 상관 +0.03(독립). 베타가 USO의 43%라 같은 손실을 덮으려면 2.3배 명목이 든다","role":"가격 층 · 현금 창출 E&P 중 최상"},
   {"name":"COP · XOP · EOG","beta":"0.26 / 0.27 / 0.24","what_it_presumes":"COP 무헤지(①) · XOP는 E&P 등가중 · EOG EV/EBITDA 5.7·FCF 9.5%. FANG과 같은 급이나 FCF 수익률에서 밀린다(COP 7.3%)","role":"가격 층 · 분산형"},
   {"name":"XLE · CVX · XOM","beta":"0.18 / 0.20 / 0.21","what_it_presumes":"메이저는 다운스트림·화학이 유가 상방을 희석 · XLE는 XOM+CVX 비중이 커서 같은 성질. 명목이 USO의 3.5배 든다","role":"가격 층 · 희석"}
  ],
  "volume_plays":[
   {"name":"WMB","beta":0.025,"why":"NGL 물량 93% fee-based(①) · 규제 수송 · FCF −0.1%. 유가와 무관 — 데이터센터 가스 수요 테제(T6 짝 축)의 종목"},
   {"name":"KMI","beta":0.032,"why":"take-or-pay 잔여이행의무 $36B(①) · CO2 원유는 $64에 헤지(①) → 유가 $130이 현금에 안 닿는다"},
   {"name":"ET","beta":0.059,"why":"10% 가격 변동 → 파생 $131M vs EBITDA $168.7억(①). FCF 7.2%는 좋지만 헤지는 아니다 · MLP 과세 미측정"},
   {"name":"EPD","beta":0.082,"why":"코스피 상관이 가장 낮으나(−0.22) 베타가 없다. 4.1% FCF · MLP"},
   {"name":"TRGP","beta":0.147,"why":"POP 계약이 약간의 상방을 주지만 헤지가 상방을 일부 판다(가스 +10% → −$228M ①) · FCF 1.2% · 1년 +72%는 물량·재투자의 값"},
   {"name":"LNG(Cheniere)","beta":0.185,"why":"90% 장기계약(①) · 스팟 층 물량 17%(①). 9월 급등 창에서 −4%. 가스 스프레드의 부분 옵션이지 유가 헤지 아님"}
  ],
  "neither":[
   {"name":"EQT","why":"브렌트 베타 0.06 · HH 종목. 유가 헤지가 아니라 다른 테제"},
   {"name":"S-Oil(대조군)","why":"브렌트 베타 0.19(R² 0.04) · 20일 블록 상관 −0.07 → 유가 <가격> 헤지 아님(아카이브 hedge_map 유지). 🔴 그런데 1년 +155%·전쟁 중 YTD +86%로 모든 후보를 이겼다 — 원인은 유가가 아니라 아시아 복합마진(open refiner-hedge의 ③ 목소리 쪽 데이터 한 점). 코스피 최악 창에선 −7%·+24%·−5%로 불안정 → 헤지가 아니라 「전쟁 레짐 수혜주」. refiner-hedge 항목에 이 측정을 붙일 것"},
   {"name":"SK이노베이션(대조군)","why":"같은 날 베타 0.25이지만 코스피 상관 +0.32(코스피 베타 종목 · 배터리) · 1년 +28% · 코스피 최악 창 셋 중 둘에서 하락 → 헤지 아님"}
  ],
  "sizing_rule":{
   "formula":"H = E_eq × |β_p| × k ÷ β_h  (H 헤지 명목 · E_eq 주식 평가액 · β_p 포트의 브렌트 베타 · k 중화할 비율 0~1 · β_h 수단의 브렌트 베타)",
   "inputs":{"E_eq":"≈8.2억(20.6억 × 40% · 팀장 제시 ②)","β_p":"−0.17(코스피 20일 블록 · n=13 · r −0.28) ~ −0.27(SKH 블록 · 메모리 75%) → 중간 −0.2","β_h":"USO 0.67 · VG 0.65 · FANG 0.29 · XOP 0.27 · COP 0.26 · XLE 0.18"},
   "arithmetic_k=0.5":"8.2억 × 0.2 × 0.5 = 0.82억의 유가 손실 베타를 덮는 명목 → USO 1.2억(주식의 15% · 포트의 6%) · VG 1.3억 · FANG 2.8억(주식의 35%) · XLE 4.6억(불가능) — 주식 수단으로 <전량> 중화는 산술적으로 안 된다",
   "tail_check":"코스피 최악 창(7/15~30 −23% · SKH −36.5%)에서 USO +7.6% · FANG +4.4%였다 — 그 창은 금리·FOMC 축이라 유가 헤지가 덮는 범위 밖. 유가 헤지는 <유가 축>만 덮는다는 것을 전제로 크기를 정한다",
   "cost_of_being_wrong":"regime breaks_if(휴전·파이프라인 복구 10월 말) 시 브렌트 −20~35% → USO/VG −20~25%(6/10~24 실측 −21%) · FANG −7% · XLE −8%. 같은 창에서 SKH +42% · 코스피 +15.5%",
   "no_execution":"수량·비중 지시 없음(§J3)"
  },
  "top3":[
   {"name":"FANG","why":"현금 창출 E&P 중 유가 베타 최고(0.29 · R² 0.44) + 상방 무헤지(①) + FCF 12.1% + 코스피 독립(+0.03). 헤지이면서 그 자체로 5사 편 T4의 종목","falsifier":"① 다음 브렌트 +30% 창에서 FANG 수익률 < +5%(베타 0.2 미달) ② 3Q26 감액 재발(유가 하락 국면 아닌데 감액이면 T4 전제 흔들림) ③ 10-Q에 원유 collar/swap 상한 신설(상방 매각)","event":"3Q26 실적 10월 말~11월 초(회사 확정일 미확인 ②) · 10-Q 파생 표 · 유가 창 실측"},
   {"name":"VG","why":"주식 중 유일하게 USO급 베타(0.65 · R² 0.40) — 호르무즈가 카타르 LNG와 원유를 동시에 끊는 경로를 스팟 카고로 직접 받는다(T6). 대가: 레버리지 5.3배·FCF −$70억·1월 $7까지 −49% 전력","falsifier":"① T6 그대로: TTF <$15인데 VG 안 빠지면 「스팟 옵션 값」 읽기 기각 ② Plaquemines Ph2 COD·SPA 개시 후 베타 <0.3 → 헤지 자격 상실(정상 전환) ③ 코스피 상관이 −0.13에서 +0.2 위로(금리 종목화)","event":"3Q26 실적(10월 말~11월 초 ②) · 스팟 카고 수·실현 마진 · Plaquemines Ph2 COD 시점 · CP2 2027"},
   {"name":"USO/BNO","why":"순수 가격 층(R² 0.73) · 가장 적은 명목으로 덮는다 · 사업 리스크 0","falsifier":"헤지로선 반증 불요 — 출구 조건 = regime breaks_if(휴전·회담 재개·동서 파이프라인 복구 10월 말). 현물-선물 갭 $29(9/15)이 좁혀지면 ETF는 현물 급등의 나머지를 못 받는다","event":"9/22 유엔총회 걸프 회동 · 9/24 미중 · 사우디 송유관 복구(10월 말) · OPEC+ · 주간 EIA"}
  ]
 },
 "page_recommendation":{
  "decision":"새 페이지",
  "why":"① us_energy_five는 이미 테제 6개(T1~T6)로 상한 5를 넘어 있어 T7 추가 불가(§W1) ② 이 질문의 포지션은 「포트폴리오 헤지」로 5사 편(종목 현금 줄 세우기)·hegemony_17(수출 물량)과 다른 포지션 — 「서로 다른 포지션 2개의 근거」 분리 조건 ③ portfolio.exposures.oil_up의 names가 비어 있는데 그 칸을 채우는 정본이 필요하다",
  "file":"energy/oil_hedge_vehicles.html (제안)",
  "outline":[
   "hero: 「석유가스는 테마가 아니라 층이다 — 유가를 받는 것은 셋(선물·VG·FANG)뿐이고 미드스트림은 0.03이다」",
   "카드 T1: 유가 베타 서열 — USO 0.67 · VG 0.65 · FANG 0.29 · XOP 0.27 · COP 0.26 · XLE 0.18 · LNG 0.19 · TRGP 0.15 · EPD 0.08 · ET 0.06 · KMI 0.03 · WMB 0.03(2026-03~09 일별 · FRED Dated 브렌트 ①) — 반증: 다음 +30% 창에서 서열 역전",
   "카드 T2: 미드스트림은 계약이 유가를 차단한다 — WMB NGL 93% fee · KMI take-or-pay $36B + CO2 원유 $64 헤지 · LNG 90% 장기계약 · VG 96% 고정 SPA인데 <지금은> 스팟 단계(모두 ① 10-K/10-Q) — 반증: 10% 가격 민감도가 EBITDA의 5%를 넘는 회사가 나온다",
   "카드 T3: 포트의 유가 베타는 −0.17~−0.27(20일 블록)이고 코스피 최악 창 셋에서 유가는 셋 다 올랐다 — 유가 헤지는 유가 축만 덮고 금리 축(7월)은 못 덮는다 — 반증: 다음 코스피 −10% 창에서 브렌트 하락",
   "카드 T4(대조군): 정유는 유가 가격 헤지가 아니다(S-Oil 베타 0.19·R² 0.04) — 그런데 1년 +155%는 유가가 아닌 아시아 복합마진의 값 → refiner-hedge 항목으로 판정 이관 — 반증: 아시아 복합마진 실측이 미 크랙과 같이 붕괴",
   "본문 1: 방법(일별 로그수익률 · lag1 · 창) + 베타 표(CSV) + 급등/급락 창 6개 수익률 표",
   "본문 2: 계약 구조 표(7사 · 인용 문장 · 등급) + FANG/COP 헤지 표(상한 유무)",
   "본문 3: 가격이 전제하는 것 — EV/EBITDA·P/OCF·FCF 수익률(09-18) + 1년 가격 변화 · VG 시총 정정($351억)",
   "본문 4: 크기의 산술 — H = E×|β_p|×k÷β_h · 주식 수단으론 전량 중화 불가 · 틀렸을 때(휴전) −20~35%의 대가 · 집행 지시 없음",
   "다음 판정 — 3Q26 실적(FANG 감액·VG 스팟 마진·LNG 단기 비중) · 9/22·9/24 · 10월 말 파이프라인 · portfolio.exposures.oil_up.names 채움 + open.refiner-hedge 갱신"
  ],
  "brain_updates_suggested":["portfolio.json exposures.oil_up: names에 후보(USO/BNO · VG · FANG) 및 hedge_beta 필드","open.json refiner-hedge: S-Oil 측정(베타 0.19 · 1년 +155% · 블록 상관 −0.07) 한 줄","theses.json us_energy_five T6 log: VG 브렌트 베타 0.65·R² 0.40(ⓐ · 스팟 옵션 읽기 지지)","facts.json: VG 시총 $351억(09-18 · 25.0억주 ①) — 캐시 $388억 ② 대체"]
 },
 "caveats":[
  "브렌트는 FRED Dated 현물이고 09-15까지만 있다(3영업일 지연). ETF는 선물을 추종해 현물 급등(백워데이션 +$29 · 9/15)을 다 못 받는다 — USO 베타 0.67은 <현물 대비>이고 선물 대비는 더 높을 것[추론]",
  "일별 회귀의 R²는 주식 0.18~0.47, 코스피 0.02 — 코스피 유가 베타(−0.12~−0.27)는 약한 추정치. 블록 상관은 n=13",
  "한국 장 lag 처리: 미국 t일 → 코스피 t+1일. 같은 날 상관은 병기했고 두 값이 갈리는 종목(EPD·LNG·VG·USO)은 lag1이 더 음(−)",
  "TTM은 2026-06-30 기준, 가격은 09-18 — 3Q26 실적 전 값. XOM은 1H26 창(TTM 아님). COP·CVX·EPD는 영업이익 태그 없어 EV/EBITDA 미산출",
  "배수의 1년 전 값은 미산출 — 가격 변화만 병기",
  "미드스트림의 「fee-based % of EBITDA」 회사 전체 수치는 10-K 본문에 없고 IR 자료(②)에만 있다 — ①로 잡힌 것은 WMB NGL 93%·KMI 이행의무·LNG 90%·VG 96%·ET/TRGP/EPD 민감도 표",
  "VG 커미셔닝 카고의 매출 비중은 10-Q 본문에서 수치를 못 찾았다 [미검증] — 스팟 노출의 크기는 T6 이벤트(3Q26)에서 판정",
  "ET·EPD MLP 분배금 과세(5사 편 T5)는 여전히 미측정 — 이 둘의 세후 수익률은 표의 값보다 낮을 수 있다",
  "S-Oil 시총·PER은 네이버 집계(②) · 1년 수익률 +155%는 naver 일봉 ①",
  "3Q26 실적 확정일은 회사 IR에서 미확인(②) — 「10월 말~11월 초」로 표기",
  "총 20.6억·주식 40%는 팀장 제시값(②) — 정본은 portfolio.json holdings·cash(현금 12.28억 08-24)"
 ],
 "files":{"series":"scratchpad/eh/series.json","results":"scratchpad/eh/results.json","conditional":"scratchpad/eh/conditional.json","valuation":"scratchpad/eh/valuation.json","beta_csv":"scratchpad/eh/beta_table.csv","sec_hits":"scratchpad/eh/sec_hits.json","filings_text":"scratchpad/eh/10k_*.txt"}
}
json.dump(out,open("../deep_energy_hedge.json","w"),ensure_ascii=False,indent=1)
print("ranking:",[(r["symbol"],r["hedge_quality"]) for r in rows])
