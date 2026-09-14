# Market-data source scout — tested 2026-09-14 23:40 KST → 2026-09-15 00:05 KST

All tests: Python 3 stdlib `urllib` from this machine through the proxy. Fetch functions in `fetchers.py` (same directory); every function except `yahoo_chart` was executed end-to-end in a smoke test after writing (Yahoo succeeded earlier in the session, then hit a 429 rate-limit — see caveat).

## Headline answer — SK하이닉스 000660, 2026-09-14

| Session | Open | High | Low | Close | Volume | Source |
|---|---|---|---|---|---|---|
| **KRX regular (09:00–15:30)** | 1,707,000 | 1,740,000 | 1,678,000 | **1,697,000 (−115,000, −6.35 %)** | 4,000,232 | naver 1-min bar `20260914153000` currentPrice, closing-auction volume 250,333; naver PC tick page 15:44–15:57 prints at 1,697,000; Yahoo `000660.KS` close 1,697,000 |
| NXT after-market (15:30–20:00) | 1,750,000 | 1,770,000 | 1,678,000 | 1,683,000 (−129,000, −7.12 %) | 2,008,900 | `polling.finance.naver.com` `overMarketPriceInfo` (tradingSessionType AFTER_MARKET) |
| naver "closePrice" everywhere | | | | 1,683,000 | 6,009,132 (`/price`) | overwritten with the after-market close from 15:30 on |

Prev close 1,812,000. Samsung 005930 regular close 09-14: 249,000 (naver 15:30 bar; naver basic shows 248,500 after-market).

**Which naver fields are regular vs after-market (as of 09-14):**
- `api.stock.naver.com/chart/domestic/item/{code}/day`, `fchart sise.nhn`, `siseJson.naver`, `finance.naver.com/item/sise_day.naver`, `m.stock.naver.com/api/stock/{code}/trend`: open/high/low/volume = **regular**, closePrice = **after-market** on the current day (volume 4,000,232 confirms regular). Unknown whether the stored close reverts to 1,697,000 tomorrow — check on 09-15 (`fetchers.naver_stock_daily('000660','20260914','20260914')`).
- `m.stock.naver.com/api/stock/{code}/price` and `/basic`: OHLC and volume are all after-market/combined (6,009,132). `tradingSessionType=REGULAR`, `marketType=KRX` params are ignored (identical output).
- Daum `finance.daum.net/api/quotes/A000660` also shows tradeTime 19:59, tradePrice 1,683,000 (after-market).
- **Robust regular close:** `api.stock.naver.com/chart/domestic/item/{code}/minute?startDateTime=YYYYMMDD1520&endDateTime=YYYYMMDD1535` → bar `localDateTime == YYYYMMDD153000`. Minute history depth ≈ current + a few days (09-11 ok, 08-14 empty), so collect daily. Fallback: `finance.naver.com/item/sise_time.naver?code=&thistime=YYYYMMDD153100` (EUC-KR HTML; T-1 ok, T-30 empty).

## Status table

| # | Source | URL | Status | Cadence | Sample |
|---|---|---|---|---|---|
| 1 | naver minute chart (regular close) | `api.stock.naver.com/chart/domestic/item/000660/minute?startDateTime=202609141520&endDateTime=202609141535` | ok | intraday, bar per minute; 15:30 bar = closing auction | `{"localDateTime":"20260914153000","currentPrice":1697000.0,"accumulatedTradingVolume":250333}` |
| 1 | naver 5-min chart | `.../item/000660/minute5?...` | ok | same | 15:30 bar currentPrice 1697000 |
| 1 | naver PC tick page | `finance.naver.com/item/sise_time.naver?code=000660&thistime=20260914153100&page=1` | ok (EUC-KR HTML) | T+0, ~few days depth | `15:30 1,812,000 … 255,299` (09-11) |
| 1 | naver day chart | `api.stock.naver.com/chart/domestic/item/000660/day?startDateTime=20260901&endDateTime=20260914` | ok, close=after-mkt on T+0 | daily, history to 1996 | `{"localDate":"20260914","closePrice":1683000.0,"openPrice":1707000.0,"highPrice":1740000.0,"lowPrice":1678000.0,"accumulatedTradingVolume":4000232,"foreignRetentionRate":50.47}` |
| 1 | naver polling realtime | `polling.finance.naver.com/api/realtime/domestic/stock/000660` | ok | 70 s poll | regular OHLV + `overMarketPriceInfo{tradingSessionType:AFTER_MARKET, overPrice:"1,683,000", openPrice:"1,750,000", …}` |
| 1 | naver /price, /basic, /integration | `m.stock.naver.com/api/stock/000660/price?pageSize=3` | ok but after-market | daily | close 1,683,000 vol 6,009,132 |
| 1 | naver /overview /timePrice /tick /overMarketPrice /nxtPrice /investor | m.stock.naver.com/api/stock/000660/… | 404 | | |
| 1 | Yahoo chart | `query1.finance.yahoo.com/v8/finance/chart/000660.KS?range=7d&interval=1d` | ok → **429 after ~17 rapid calls, still 429 after 60 s+** | daily/intraday | `('2026-09-14', 1707000.0, 1740000.0, 1686000.0, 1697000.0, 4165093)` (regular close; low/volume differ from KRX — Yahoo vol includes 시간외) |
| 1 | Daum quote | `finance.daum.net/api/quotes/A000660` (Referer finance.daum.net) | ok, after-market | realtime | tradePrice 1683000 tradeTime 195900 accTradeVolume 3999262 |
| 1 | Daum daily | `finance.daum.net/api/quote/A000660/days?symbolCode=A000660&page=1&perPage=3&pagination=true` (singular `quote`) | ok, after-market close | daily | includes listedSharesCount 730492365 |
| 1 | **KRX data portal** | `data.krx.co.kr/comm/bldAttendant/getJsonData.cmd` (POST bld=dbms/MDC/STAT/standard/MDCSTAT01501/01701/00301/02203, Referer+Origin+X-Requested-With, http & https, with JSESSIONID from index.cmd) | **blocked by KRX: HTTP 400 body `LOGOUT`**; `index.cmd?menuId=…` returns JS `alert('로그인 또는 회원가입이 필요합니다.')` → redirect to `/contents/MDC/COMS/client/MDCCOMS001.cmd` (login); OTP route `comm/fileDn/GenerateOTP/generate.cmd` also returns `LOGOUT`, `download.cmd` 403 | | KRX now requires a member login for the stats portal. Not a proxy block (200 on the page). |
| 2 | naver index chart | `api.stock.naver.com/chart/domestic/index/KOSPI/day?startDateTime=20260901&endDateTime=20260914` | ok | daily, history to 1990 | `{"localDate":"20260914","closePrice":6684.37,"openPrice":6692.61,"highPrice":6773.97,"lowPrice":6654.82,"accumulatedTradingVolume":297171}` (volume 천주; KOSDAQ same path) |
| 2 | naver index price pages | `m.stock.naver.com/api/index/KOSPI/price?pageSize=5&page=1` | ok | daily | same values, string-formatted |
| 2 | naver index trend | `m.stock.naver.com/api/index/KOSPI/trend` | ok, **today only** (pageSize ignored) | daily | `{"bizdate":"20260914","personalValue":"+30,351","foreignValue":"-33,363","institutionalValue":"-11,869"}` (억원) |
| 2 | **Daum index + flows history** | `finance.daum.net/api/market_index/days?market=KOSPI&page=1&perPage=20&pagination=true` (Referer) | ok | daily, paged | `{"date":"2026-09-14 00:00:00","tradePrice":6684.370,"accTradeVolume":297171,"accTradePrice":21584368.000,"individualStraightPurchasePrice":3035111621789.000,"foreignStraightPurchasePrice":-3337504400011.000,"institutionStraightPurchasePrice":-1186864099559.000}` — values in **원**; ÷1e8 → 억. `market=KOSDAQ` works. Foreign −33,375억 vs naver −33,363억 (Daum probably includes 기타외국인). |
| 2 | **naver PC 일자별 순매수** | `finance.naver.com/sise/investorDealTrendDay.naver?bizdate=20260914&sosok=01&page=1` (sosok 01 KOSPI / 02 KOSDAQ; EUC-KR HTML) | ok | daily, paged, long history | `26.09.14 30,351 -33,363 -11,869 -5,524 259 -6,105 9 195 -703 14,880` = 개인 외국인 기관계 금융투자 보험 투신(사모) 은행 기타금융 연기금등 기타법인 (억원). Sub-columns sum to 기관계. |
| 2 | naver per-stock flows | `m.stock.naver.com/api/stock/000660/trend?pageSize=20&page=1` | ok | daily, paged | `foreignerPureBuyQuant "-1,215,512", organPureBuyQuant "-266,205", individualPureBuyQuant "+906,398", foreignerHoldRatio "50.30%"` (shares) |
| 2 | Daum per-stock flows | `finance.daum.net/api/investor/days?symbolCode=A000660&page=1&perPage=20` | ok | daily | `foreignOwnShares 368666841, foreignOwnSharesRate 0.5047, foreignStraightPurchaseVolume -1219445, institutionStraightPurchaseVolume -266205` |
| 2 | Daum `/api/quotes/…/days`, `/api/investor/days?market=`, `/api/market_index/KOSPI`, `/quote/…/investors` | | 500 Internal Server Error | | wrong paths |
| 3 | naver marketindex energy list | `api.stock.naver.com/marketindex/energy` | ok | 10-min delayed intraday | `CLcv1 WTI 103.87 USD/BBL · LCOcv1 브렌트유 108.86 · NGcv1 천연가스 2.83 USD/MMBTU (Henry Hub front) · DCBc1 두바이유 114.91 · RBcv1 HOcv1 LGOcv1 QMcv1 QGcv1 + 국내 유가` |
| 3 | naver marketindex history | `api.stock.naver.com/marketindex/energy/CLcv1/prices?page=1&pageSize=10` (also LCOcv1, DCBc1, NGcv1; `exchange/.DXY`, `bond/US10YT=RR`) | ok | daily settle, paged | `{"localTradedAt":"2026-09-11T16:00:00-05:00","closePrice":"100.05","openPrice":"104.32","highPrice":"104.46","lowPrice":"98.48"}` |
| 3 | naver marketindex categories | `/marketindex/{metals,agricultural,exchange}` ok; `/bond` (list) 404 but `/bond/{code}` and `/bond/{code}/prices` ok; `/marketindex`, `/category`, `/major`, `/commodity`, `/materials`, `/bondAndInterest` 404; `m.stock.naver.com/api/marketindex/*` 404; `chart/marketindex/*` 404 | | | bond codes seen in page HTML: KR2YT=RR KR10YT=RR KR30YT=RR US2YT=RR US10YT=RR US30YT=RR |
| 3 | **TTF** naver | | **not on naver** (energy list has no TTF/JKM) | | |
| 3 | **TTF** Yahoo | `query1.finance.yahoo.com/v8/finance/chart/TTF=F?range=5d&interval=1d` | ok (before 429) | daily (ICE Endex front-month, EUR/MWh) | `('2026-09-14', 83.5, 83.78, 83.4, 83.78, 32)`; 09-11 close 79.52 |
| 3 | **TTF** tradingeconomics | `tradingeconomics.com/commodity/eu-natural-gas` (browser UA) — page 200, value parsed from `<meta name=description>` | ok (HTML scrape, fragile) | daily headline | `EU Gas rose to 83.55 EUR/MWh on September 14, 2026, up 5.06%…`; `/commodity/natural-gas` 2.89 USD/MMBtu; `/commodity/uk-natural-gas` 207.64 GBp/thm |
| 3 | **TTF** FRED monthly | `fredgraph.csv?id=PNGASEUUSDM` | ok | monthly (USD/MMBtu, IMF) | `2026-07-01,17.93` |
| 3 | **JKM** Yahoo | `chart/JKM=F?range=5d` | ok but **sparse**: only 09-11 has a value (24.885), 09-13/14 null, volume 0 | irregular | not usable as a daily series |
| 3 | **JKM** FRED | `PNGASJPUSDM` (Japan LNG import price, IMF) | ok | monthly | `2026-07-01,19.562` — proxy only |
| 3 | **JKM** CME | `cmegroup.com/CmeWS/mvc/Quotes/Future/8390/G`, `/Settlements/…`, `/ProductSlate/V2/List?searchString=JKM` | **403**: `"This IP address is blocked due to suspected web scraping activity…"` | | |
| 3 | **JKM/TTF** ICE | `ice.com/marketdata/DelayedMarkets.shtml?getContractsAsJson=&productId=4331&hubId=7979`, `getProductsAsJson=&hubId=7979` | 403 (HTML) | | `ice.com/marketdata/reports/10` page itself is 200 |
| 3 | JKM others | tradingeconomics `/commodity/jkm`, `/commodity/lng` → generic page (no series); spglobal JKM page 403; marketwatch `jkm00` 401; cnbc `@JKM.1` 404; barchart `proxies/core-api/v1/quotes/get` 403 `{"error":"Forbidden"}` | **no free daily JKM found** | | |
| 3 | investing.com | `investing.com/commodities/dutch-ttf-gas-c1-futures-historical-data` | 403 | | |
| 3 | stooq | `stooq.com/q/d/l/?s=dx.f&i=d`, `stooq.pl/…ng.f` | 200 but JS browser-verification page, no CSV | | |
| 3 | EIA API | `api.eia.gov/v2/natural-gas/pri/fut/data/…` | 403 `API_KEY_MISSING` (free key would fix) | | `eia.gov/dnav/ng/hist/rngwhhdD.htm` HTML table is 200 (weekly refresh) |
| 3 | Henry Hub / Brent / WTI FRED | `DHHNGSP` `DCOILBRENTEU` `DCOILWTICO` | ok | daily, ~2-3 business-day lag | `2026-09-09,2.81` / `2026-09-09,109.51` / `2026-09-09,97.26` |
| 4 | DXY naver intraday | `api.stock.naver.com/marketindex/exchange` (`.DXY` in normalList) or `/marketindex/exchange/.DXY` | ok | 10-min delayed | `99.62 (+0.50%) 2026-09-14T10:40:54-04:00` |
| 4 | DXY naver daily | `/marketindex/exchange/.DXY/prices?pageSize=10` or `api.stock.naver.com/chart/foreign/index/.DXY/day?startDateTime=&endDateTime=` | ok | daily | `2026-09-11 close 99.12` / chart `{"localDate":"20260911","closePrice":99.12…}` |
| 4 | DXY FRED | `DTWEXBGS` (broad dollar index, not DXY) | ok | daily, ~1-week lag | `2026-09-04,118.0732` |
| 4 | DXY Yahoo | `DX-Y.NYB` | ok (before 429) | daily/intraday | 09-14 99.596 |
| 4 | US 30Y FRED | `DGS30` | ok | daily, T+1 (last 09-10 5.37) | `2026-09-10,5.37` |
| 4 | US 30Y/10Y naver | `api.stock.naver.com/marketindex/bond/US30YT=RR/prices?pageSize=10`; `/bond/US10YT=RR` snapshot "실시간" | ok | daily history + realtime snapshot | `2026-09-11 5.3540` ; US10Y live 4.9960 at 10:50 ET 09-14 |
| 4 | KR yields naver | `/bond/KR10YT=RR/prices` (also KR2YT, KR30YT) | ok | daily | `2026-09-14 4.5320` |
| 4 | 10Y breakeven FRED | `T10YIE` (also `DFII10`, `DGS10`) | ok | daily, T+1 | `2026-09-11,2.36` |
| 4 | Yahoo yields | `^TYX` `^TNX` | ok (before 429) | intraday | 09-14 5.375 / 5.002 |
| 5 | VIX naver | `api.stock.naver.com/index/.VIX/basic`; `chart/foreign/index/.VIX/day?…` | ok | 15-min delayed / daily | 09-14 close 17.46 |
| 5 | VIX FRED / CBOE | `VIXCLS`; `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` | ok | daily | `2026-09-11,15.84` / full OHLC history from 1990 |
| 5 | CNN Fear & Greed | `production.dataviz.cnn.io/index/fearandgreed/graphdata` (needs Chrome UA + Referer/Origin cnn.com; bare `Mozilla/5.0` → **418 "I'm a teapot. You're a bot."**) | ok | intraday, includes ~1y daily history | `{"score":30.86,"rating":"fear","previous_close":33.34,"previous_1_week":45.23,"previous_1_month":64.31}` |
| 5 | CBOE put/call | `cdn.cboe.com/data/us/options/market_statistics/daily/2026-09-11_daily_options` | ok (403 until day's file is published; 09-14 was 403 at 23:50 KST) | daily, US evening | `TOTAL 0.86 · INDEX 1.06 · EQUITY 0.58 · SPX+SPXW 1.23` |
| 5 | AAII | `aaii.com/files/surveys/sentiment.xls` 403 (Cloudflare block page); `aaii.com/sentimentsurvey/sent_results` 200 but JS challenge shell | **blocked (bot challenge)** | weekly | |
| 5 | KR breadth naver | `m.stock.naver.com/api/stocks/up/KOSPI?page=1&pageSize=1` → `totalCount` 802; `/down/KOSPI` 1,473; KOSDAQ up 676 | ok | T+0 | **caveat**: 802+1473 > KOSPI stock count → list includes ETF/ETN. `newHigh/newLow/upperLimit/high52…` 404. |
| 5 | KR 52-week highs/lows | `finance.naver.com/sise/sise_new_high.naver?sosok=0` → naver 404 error page (287 B); `sise_rise.naver` 200 but zero `code=` links (new design, JS-rendered); `sise_index.naver?code=KOSPI` no 상승/하락 counts in HTML; KRX blocked (above) | **not found** | | Workaround: compute from naver `chart/domestic/item/{code}/day` per symbol (52w high in `/integration` totalInfos `highPriceOf52Weeks`). |
| 6 | KR ETF universe | `finance.naver.com/api/sise/etfItemList.nhn` (**cp949** JSON) | ok | intraday | 1,168 ETFs: `itemcode itemname nav nowVal marketSum(억) quant etfTabCode` |
| 6 | **KR single-stock 2x ETFs (exist)** | `m.stock.naver.com/api/etf/{code}/basic` | ok | daily NAV (prev close), iNav intraday, `totalNav` = AUM | `0193T0 KODEX SK하이닉스단일종목레버리지: close 9,915 · nav 11,442.59 · iNav 10,007.43 · totalNav 2조 4,788억 · marketValue 2조 1,478억 · vol 24,902,074` ; `0195S0 TIGER SK하이닉스단일종목레버리지 AUM 1조 5,160억` ; `0193W0 KODEX 삼성전자단일종목레버리지 1조 4,246억` ; `0195R0 TIGER 삼성전자단일종목레버리지 9,539억` ; also ACE 0194T0, SOL 0197W0, RISE 0192L0, 1Q 0198D0, KIWOOM 0194R0 (하이닉스); inverse −2X: SOL 0197X0 (1,277억), PLUS 0193L0 (삼성). `nav` here looks like the previous official NAV (11,442 vs close 9,915 on a −13 % day); `iNav` is the live one. |
| 6 | KR ETF constituents | `m.stock.naver.com/api/etf/0193T0/constituent` | ok | daily | `2026-10 SK하이닉스개별선물 110.18 % · SK하이닉스 89.94 % · 원화현금 10.05 %` |
| 6 | KR ETF NAV history | `/api/etf/{code}/price|nav|navHistory|trend|integration` 404 | **no NAV history endpoint found** — collect `etf/basic` daily | | per-ETF flows: `m.stock.naver.com/api/stock/0193T0/trend` ok (개인 +4,736,331주 on 09-14) |
| 6 | **HK CSOP SK Hynix 2x = 7709.HK** (not 7522.HK) | `api.stock.naver.com/stock/7709.HK/basic`; `chart/foreign/item/7709.HK/day?…` | ok | 15-min delayed / daily | `close 37.020 HKD (−13.7 %), vol 133,957,816, 대금 50.6억 HKD, 시총 299억 HKD (≈5조 1,335억원)`; no NAV/AUM field → use 시총 (units × price) as AUM proxy. **7522.HK on naver = "ChinaAMC NASDAQ-100 Index Daily (-2x) Inverse Product"** — the ticker in the brief is wrong. |
| 6 | CSOP site / HKEX widget | `csopasset.com/*` 403 (redirect shell); `www1.hkex.com.hk/hkexwidget/data/getequityquote?sym=7522` 403 | blocked | | |
| 7 | CFTC Socrata | `publicreporting.cftc.gov/resource/72hh-3qpy.json?cftc_contract_market_code=023651&$order=report_date_as_yyyy_mm_dd DESC&$limit=2` | ok | weekly (Tue positions, Fri release) | NG 023651 2026-09-08: OI 1,823,243 · MM long 262,109 / short 358,851 (net −96,742); WTI 067651: MM long 218,960 / short 107,229 (net +111,731) |
| 7 | CFTC flat file | `cftc.gov/dea/newcot/f_disagg.txt` | ok | weekly | CSV, all markets, current week |
| 7 | CFTC legacy | `resource/6dca-aqww.json` | ok | weekly | noncomm_positions_long/short_all |

## Details and caveats per item

### 1. Regular vs after-market close
- After 15:30 naver's `closePrice` = NXT after-market price in every JSON route (`basic`, `price`, `integration`, `trend`, day chart, polling `closePrice`, Daum). The `tradingSessionType`/`marketType` query params do nothing.
- The regular session survives in three places: (a) the **15:30 minute bar** (`minute`/`minute5` chart) — the closing-auction print and volume; (b) the regular OHLV block of `polling.finance.naver.com` (`openPrice/highPrice/lowPrice/accumulatedTradingVolume` were 1,707,000/1,740,000/1,678,000/4,000,232 while `overMarketPriceInfo` carried the after-market block); (c) the PC tick page. `fetchers.krx_regular_close(code, yyyymmdd)` uses (a) then (c).
- Open question to check on 09-15: whether the day chart's stored close for 09-14 stays 1,683,000 (after-market) or is rewritten to 1,697,000. If it stays, the whole daily history from 09-14 onward is after-market closes and the collector must keep its own regular series from the 15:30 bar.
- KRX's own portal is closed to anonymous requests (login redirect), so there is no free KRX-official regular close from this machine.

### 2. Index history + flows
- History with investor flows in one call: Daum `market_index/days` (원, three investor classes, paged, KOSPI and KOSDAQ). Sub-categories (금융투자/보험/투신/은행/기타금융/연기금/기타법인): naver PC `investorDealTrendDay` HTML (억원). `fetchers.naver_investor_deal_trend_day` returns both and its column mapping is sum-checked.
- naver `index/KOSPI/trend` is today-only; keep it as the T+0 quick read.

### 3. Gas and oil
- TTF daily: Yahoo `TTF=F` (EUR/MWh, front month) is the only free daily JSON found; tradingeconomics headline scrape gives the same day's number as a cross-check; FRED monthly `PNGASEUUSDM` in USD/MMBtu.
- JKM daily: **not available free** from this machine. CME (403 explicit scraping block), ICE (403), S&P (403), barchart (403), Yahoo `JKM=F` sparse. FRED `PNGASJPUSDM` is a monthly Japan LNG import price (lagging proxy). EIA does not carry JKM either. JKM needs a paid feed or a manual weekly entry.
- Henry Hub: naver `NGcv1` (front-month settle, daily history) vs FRED `DHHNGSP` (spot, 2–3 day lag). Brent/WTI/Dubai daily settles: naver `LCOcv1`/`CLcv1`/`DCBc1` (Dubai is a single daily print, OHLC identical). Intraday 10-min delayed via the `energy` list.

### 4. Dollar and rates
- DXY: naver `.DXY` (intraday list, daily `prices`, daily chart) — three routes agree (99.12 on 09-11). FRED `DTWEXBGS` is the Fed broad index, not DXY, and lags a week.
- US 30Y: FRED `DGS30` (T+1) and naver `US30YT=RR` (daily history + realtime snapshot). 10Y breakeven only on FRED (`T10YIE`; `DFII10` real yield also works). naver has no breakeven series.

### 5. Sentiment
- CNN works only with browser-like headers. CBOE daily file is 403 until published. AAII blocked by Cloudflare bot challenge (both the xls and the results page). KR advance/decline available (with ETF contamination); KR 52-week high/low counts not found on naver's current pages and KRX is login-walled.

### 6. Leveraged ETFs
- Korea now lists single-stock leveraged ETFs (`단일종목레버리지`, base index "KRX SK하이닉스 레버리지 지수", holdings = single-stock futures 110 % + stock 90 % + cash). `etf/{code}/basic` gives `totalNav` (AUM) daily; no history endpoint, so snapshot daily. `fetchers.naver_etf_basic` converts `'2조 4,788억'` → 24788 (억).
- HK: the CSOP SK Hynix Daily Max (2x) product is **7709.HK**; naver gives price/volume/market cap (≈ AUM for an ETP) and daily chart; CSOP's own site and HKEX widget are blocked.

### 7. CFTC
- Socrata API and flat files both reachable, no key. Contract codes: NG Henry Hub 023651, WTI physical 067651. Disaggregated futures-only dataset `72hh-3qpy`; combined futures+options is `kh3c-gbw2` (not tested).

## Blocked / failed — host, path, exact error
- `data.krx.co.kr` `/comm/bldAttendant/getJsonData.cmd` (POST, http+https, with and without JSESSIONID, Referer/Origin/X-Requested-With) → `400` body `LOGOUT`; `/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020103` → 200 HTML `alert('로그인 또는 회원가입이 필요합니다.')` + redirect to `/contents/MDC/COMS/client/MDCCOMS001.cmd`; `/comm/fileDn/GenerateOTP/generate.cmd` → 200 `LOGOUT`; `/comm/fileDn/download_csv/download.cmd` → 403.
- `api.eia.gov` `/v2/natural-gas/pri/fut/data/` → 403 `{"error":{"code":"API_KEY_MISSING"}}`.
- `www.cmegroup.com` `/CmeWS/mvc/Quotes/Future/8390/G`, `/CmeWS/mvc/Settlements/Futures/Settlements/8390/FUT`, `/CmeWS/mvc/ProductSlate/V2/List` → 403 `"This IP address is blocked due to suspected web scraping activity…"`.
- `www.ice.com` `/marketdata/DelayedMarkets.shtml?getContractsAsJson=…` and `?getProductsAsJson=…` → 403 HTML.
- `www.investing.com` `/commodities/dutch-ttf-gas-c1-futures-historical-data` → 403.
- `www.aaii.com` `/files/surveys/sentiment.xls` → 403 (bot page); `/sentimentsurvey/sent_results` → 200 JS-challenge shell, no data.
- `www.csopasset.com` `/en/products/*`, `/api/fund/7522` → 403 redirect shell.
- `www1.hkex.com.hk` `/hkexwidget/data/getequityquote?sym=7522` → 403.
- `www.barchart.com` `/proxies/core-api/v1/quotes/get?symbols=JKM*0` → 403 `{"error":"Forbidden"}`; `/futures/quotes/JKMV26/overview` → 202 empty.
- `www.spglobal.com` JKM product page → 403; `www.marketwatch.com/investing/future/jkm00` → 401; `www.cnbc.com/quotes/@JKM.1` → 404.
- `stooq.com`, `stooq.pl` `/q/d/l/?s=…` → 200 JS verification page (no CSV).
- `query1/query2.finance.yahoo.com` `/v8/finance/chart/*` → 200 for the first ~17 calls in 30 s, then `429 Too Many Requests` persisting > 5 min. Usable at low rate (space calls, few symbols per run); treat as best-effort.
- `production.dataviz.cnn.io` with UA `Mozilla/5.0` only → 418 `I'm a teapot. You're a bot.` (works with Chrome UA + Referer/Origin).
- `cdn.cboe.com` `/data/us/options/market_statistics/daily/2026-09-14_daily_options` → 403 (not yet published at test time; 09-11 file 200).
- naver 404s: `m.stock.naver.com/api/stock/{code}/{overview,timePrice,tick,overMarketPrice,nxtPrice,investor,etfInfo}`, `/api/index/KOSPI/{investor,dealTrend,marketSum,marketStatus,upDownCount}`, `/api/etf/{code}/{price,nav,navHistory,trend,integration}`, `/api/stocks/{newHigh,newLow,upperLimit,…}/KOSPI`, `api.stock.naver.com/marketindex/{category,major,commodity,materials,bond,bondAndInterest,…}`, `api.stock.naver.com/chart/marketindex/*`, `api.stock.naver.com/stock/000660/basic` (409 "Not Exist Master" — domestic codes are only on m.stock.naver.com), `finance.naver.com/sise/sise_new_high.naver` (naver error page).
- Daum 500s: `/api/quotes/{sym}/days`, `/api/quotes/{sym}/investors`, `/api/investor/days?market=`, `/api/market_index/KOSPI`, `/api/market_index/investors`.

## Not tried
- EIA with a registered key; CFTC `kh3c-gbw2` (futures+options); KIS/eBest broker APIs (need keys); Yahoo `v7/finance/quote` (needs crumb); Google Finance; Bloomberg/Reuters public pages.
