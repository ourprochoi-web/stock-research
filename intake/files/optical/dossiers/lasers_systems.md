# Optical lasers · systems dossier — LITE · COHR · CIEN · GLW

## Ledger deltas (newest first)

### 2026-09-24 — PhotonLink / ECOC (@dubidubabap factcheck → Lead digest-only)

**Grounded (merge):**
- **A1 / f-20260924-opt-01:** COHR PhotonLink — **10+ CPO** customer engagements + anchor **LTA** (company PR + ECOC transcript).
- **A2 / f-20260924-opt-02:** Eng on-stage names **NVIDIA** as the public CPO anchor agreement.
- **A4 / f-20260924-opt-03:** CPO **Scale-Out ramp Q4 CY2026**; **Scale-Up H2 2027**.
- **B5 / f-20260924-opt-04:** Mar 2026 NVIDIA–COHR multibillion purchase + **$2B** equity — **이미판정** (reappearance only).
- **C9 / f-20260924-opt-05:** LITE **8λ DWDM ELSFP** demo at ECOC; avail target **1H CY2027** (company IR).

**Partial / soft (do not harden into thesis):**
- **C7 / f-20260924-opt-07:** Spectrum-6 + 4Q26 UHP demand-up — secondary Stifel/Gate; soft park.
- **C8 / f-20260924-opt-08:** “Long-term NPO > CPO” / multi-λ ASP — slightly overstated vs primary near-term/50-50; soft park.
- *(Also soft: C6 UHP demand>supply — primary Aug–Sep strong, ECOC attribution secondary — `f-20260924-opt-06`.)*

**Disposition:** digest-only · no ticker add · SMTC residual retained · HTML papers untouched. Memo: `../2026-09-24/dubidubabap_photonlink_cpo_ecoc_factmap.md`.

> Living dossier seeded from `../2026-09-23/dossier_lasers_systems.md` (historical snapshot retained). Body below is the 2026-09-23 copy pending future merges.

---


- **As-of / staging date:** 2026-09-23 (KST)
- **Scope:** Lumentum (LITE), Coherent (COHR), Ciena (CIEN), Corning (GLW)
- **Primary sources:** archive `brain/facts.json` · `brain/entities.json` · `brain/theses.json` · `brain/routing.jsonl` · `ai-infra/optical_*` · `ai-infra/us_vertiv_corning_deep.html` · `data/13f/` · `intake/files/prices_daily/`
- **Supplement:** WEB / company IR / SEC press (labeled WEB). **Never invent** — blanks stay blank.
- **Rules:** no buy/sell share counts · no stops · edge cards only.

---

## Cross-layer map (읽기 전에)

| Ticker | Layer (archive) | AI-optical role (한 줄) |
|--------|-----------------|------------------------|
| **LITE** | 광원·부품 (EML·CW·펌프) | AI 트랜시버/CPO용 **레이저 병목** — “못 지우는 층” |
| **COHR** | 광원+모듈 수직계열 (구 II-VI) | InP/EML/VCSEL + 트랜시버 · DC&C가 전사 74% |
| **CIEN** | 시스템 · DCI·코히런트 (+Nubis AEC) | 캠퍼스/DCI·코히런트 시스템 · 클라우드 직접 매출 폭증 |
| **GLW** | 광섬유·케이블·커넥티비티 | 어떤 광 아키텍처든 **유리는 필요** · Springboard+하이퍼스케일러 LTA |

Archive thesis spine (`optical_valuechain_9`): 마진은 “층”이 아니라 **자기 제품 vs EMS**; 병목은 **지울 수 없는 물리 부품(레이저·드라이버·TIA)**; 변곡은 **광원(LITE OPM −31%→+28%)**; COHR은 **연결이 세그먼트를 가림**; 층 경계는 양방향 이동(CIEN→AEC, COHR→완성 어셈블리).

---

# 1. LITE — Lumentum Holdings

## 1. Business
- **Products:** EML(장거리 레이저+변조기), CW 레이저(SiPho/CPO 광원), 펌프 레이저(증폭), ROADM, 3D 센싱 VCSEL. (`entities` ②; primer/9사 편)
- **AI-optical role:** 800G/1.6T 플러거블·CPO 공급망의 **레이저**; NVIDIA CPO 공급망에 레이저로 거명(②). Ciena 경영진: 병목은 캐파가 아니라 **펌프 레이저·광 패키징**(routing r-20260912-01 ③).
- **Customers:** 하이퍼스케일/모듈 벤더향(구체 매출 비중 공시 미대조 — thin). Cloud Light 기여는 미즈호 추정(③: 2026E ~$0.9B / 2027E ~$1.2B) — 회사 공시 미대조.
- **Moat:** InP 기반 고속 EML 점유·양산; “레이저는 못 지운다”(T2). 미즈호(③): EML 1위 ~33%(고속 EML ~50%), 레이저 중심 사업.
- **Competitors:** Coherent(광원+모듈), Broadcom(레이저/부품), Sumitomo·Yuanjie 등 CW 점유(미즈호 ③: CW SEI 32% · Yuanjie 24% · AVGO 18% · **LITE 11%** — CW에서 뒤처짐이 구조 리스크). 중국 모듈(InnoLight 등)은 모듈 층 경쟁/고객.

## 2. Financials
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM / FY26 | **$3,014M** (+83.2% YoY on latest-Q basis in facts) | BRAIN facts ① SEC XBRL · asof **2026-09-11**; WEB IR FY26 rev **$3.01B** (+83% vs FY25 $1.6B) · **2026-08-11** |
| Latest Q rev | **$1,006M** (Q ended **2026-06-27** = FY26 Q4) | BRAIN ①; WEB confirms Q4 FY26 **$1.006B** (+109% YoY) |
| GPM TTM / latest Q | **41.7%** / **47.4%** | BRAIN ① |
| OPM TTM / latest Q | **17.4%** / **27.7%** (2년 전 −31.3% → 변곡 T3) | BRAIN ①; WEB GAAP OPM Q4 **27.8%**, non-GAAP **36.6%** |
| FY26 GAAP NI | WEB: **−$6.9B** — one-time non-cash convert equitization loss ~$7.8B (EPS 해석 시 주의) | WEB IR **2026-08-11** |
| Cash + STI | WEB: **~$2.74B** (↓$0.43B QoQ, ↑~$1.9B YoY) | WEB IR YE FY26 |
| Debt | WEB: **~$1.64B** book ($1.597B current + $40.5M LT) after equitization; was ~$2.57B YE FY25 | WEB |
| Segments | facts에 세그먼트 분해 **없음** (Cloud / Telecom 믹스는 ③·IR 추가 필요) | thin |
| Guide | WEB FY27 Q1 rev **$1.225–1.275B**, non-GAAP OPM **39.5–40.5%** | WEB **2026-08-11** |

## 3. Valuation snapshot
| | | |
|--|--|--|
| Mcap / P/S | BRAIN: **$83.2B** / **P/S 27.6×** (asof **2026-09-11**, px ~$927) | BRAIN ① |
| WEB refresh | Mcap ~**$89.6B**, trailing P/S ~**29.7×** (asof **2026-09-18**); Forward P/E ~**45.6×**, trailing P/E **n/a** (GAAP NI 왜곡) | WEB |
| 1y price | BRAIN: **+$599.4%** ($132.56→$927.03, asof 09-11) | BRAIN |
| YTD / recent | ARCHIVE prices: **YTD +118.3%** (2026-01-02 $386.11 → 2026-09-15 **$842.88**); 1Y from 2025-09-15 +399% | ARCHIVE prices_daily |
| WEB color | YTD ~**+156%** cited mid-Sep; volatile (09-14 ATM sector dump day LITE −~10% from 09-11 baseline per routing) | WEB / routing r-20260915-05 |

## 4. Supply/demand & positioning
- **13F:** Duquesne (Drucker) **2Q26 전량 청산** Lumentum 6,963주(1Q 포트 0.14%) — 소형 포지션 청산이지 “강한 short” 아님(`theses`/`routing` ①). Tiger 1Q26: LITE 136.8k주 보유 → 2Q26 아카이브 정규화에 **미확인(thin)**.
- **Analyst / routing:** 미즈호 09-14 — EML 캐파 2026E 2배, CW 2029E 5배; LITE GPM 경로 50%초반; **CW 4위 리스크**. JPM 09-17 광 노트(라우팅 배치). Semiconsight “적자” 주장 → archive가 OPM 28%로 **기각**(r-20260920-21).
- **Capacity / LTA:** “sold out”/펌프 병목 서술(③·Ciena); ELS 플러거블 수주 시작(미즈호 ③). 구체 LTA 금액 **미공시/미대조**.

## 5. Edge card
| | |
|--|--|
| **priced_in** | 변곡(마진·성장)·AI 광원 병목·1y ~6× 랠리. P/S ~28–30×에 “지속 고성장+GPM 유지”가 이미 큼. |
| **variant** | (a) FY27에도 GPM≥47%·OPM≥28% 유지 + CW/UHP·CPO 레이저 점유 회복 → 멀티플 유지. (b) EML→CW 믹스에서 점유 실패·증산으로 ASP/GPM 압축. |
| **breaks_if** | FY27 Q1(~11월) GPM **&lt;44%** 또는 OPM 두 자릿수 붕괴; 하이퍼스케일 광학 캡ex 급감; CW에서 영구 열위 고착. |
| **residual** | **Med-Low** — 펀더멘털 변곡은 확인됐으나 가격이 먼저 앎(T3). 잔여는 실행·믹스·배수 압축 리스크. |

## 6. Open questions / thin spots
- 고객 집중도·Cloud vs Telecom 매출 믹스 (10-K 세그 미적재)
- CW/UHP vs EML 매출 비중 실측 (③만)
- Convert equitization 이후 diluted share / GAAP P/E 정상화 시점
- Tiger 등 기타 13F 2Q26 LITE 변화 전수

---

# 2. COHR — Coherent Corp.

## 1. Business
- **Products:** 구 II-VI. InP 레이저·EML·VCSEL + **트랜시버 완제품** + 산업용 레이저·광학 소재. (`entities` ②)
- **AI-optical role:** Datacenter & Communications(DC&C) 세그 — AI 광학 수요의 수직계열 공급자. ECOC/Citi(③ 09-22): 고객이 **완성 어셈블리**를 요구 → PhotonLink 등 어셈블리 층으로 상향. 스케일아웃 CPO 램프 주장(회사 ③; 시점 아카이브 Wedbush와 **2–3년 어긋남** — 판정=4Q26 DC&C에 CPO 분리 여부).
- **Customers:** 하이퍼스케일/모듈·시스템; **NVIDIA ~$2B equity** 투자·장기 CPO/CW 관련 계약 서술(미즈호/WEB ③·② 혼재 — 금액·조건 세부는 thin).
- **Moat:** InP 수직계열·6인치 전환(회사: GaAs capex 4×, InP 6" 비중 분기말~50%→2027말~75%, Sherman 램프) — Ciena “펌프 공급 4×”와 **숫자 대조 완료**(theses). 다만 미즈호: **최첨단 레이저 일부 LITE 의존** → 구조적 원가 열위 가능.
- **Competitors:** Lumentum(레이저), Innolight/Eoptolink(모듈), Broadcom; Industrial 쪽 IPG 등(세그 역성장).

## 2. Financials
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM / FY26 | **$7,118M** | BRAIN ①; WEB FY26 **$7.118B** (+22.5%) · **2026-08-12** |
| Rev growth (facts latest-Q YoY) | **+33.7%** | BRAIN ① asof 09-11 |
| GPM TTM | **37.5%** | BRAIN ①; WEB FY GAAP GM **37.5%**, Q4 non-GAAP **40.2%** |
| OPM TTM / adj | **7.84%** / **12.67%** (무형상각 $280M + 구조조정 $63M 가산) | BRAIN ① — 상각 3년 반복이라 **병기**(§W3) |
| DC&C FY26 | **$5,275M** (+40.5%), 비중 **74.1%** (FY24 55.9%→) | BRAIN ① 10-K |
| Industrial FY26 | **$1,844M** (역성장, prior $2,076M) | BRAIN ① |
| Latest Q (cooling page) | Rev **$2,046M**, OPM **18.9%** (세그/조정 정의 주의) | kr_cooling_optical ① |
| Cash / investments | WEB YE FY26: cash **$1.16B** + STI **$0.825B** (+restricted 등) ≈ **$2.0–2.6B** 유동성 밴드 | WEB 8-K/earnings |
| Debt | WEB: **~$3.22B**; leverage 개선·상환 $513M 서술 | WEB |
| FCF | WEB: OCF **$79.5M**, capex **~$1.10B** → FCF ≈ **−$1.02B** (증설 중) | WEB |
| Guide | WEB FY27 Q1 rev **$2.2–2.4B**, non-GAAP GM 39.5–41.5%, EPS $1.85–2.05 | WEB **2026-08-12** |
| GPM path (company) | ECOC: GPM **42%+** 목표 열어둠 but **“향후 2–3분기 급개선 기대 말라”** → 판정 창 2027 중반으로 밀림 | routing/events ③ **2026-09-22** |

## 3. Valuation snapshot
| | | |
|--|--|--|
| Mcap / P/S | BRAIN: **$59.8B** / **8.4×** (09-11) | BRAIN |
| WEB | Mcap ~**$62.1B**, P/S ~**8.7×** (09-18); px WEB **~$308** (09-22) | WEB |
| P/E | 의미 있음(흑자). WEB/애널: FY2028 EPS~$14–16 × ~30× = TP~$420 가정(Citi/Stifel ③) — **가정 곱** | WEB/routing |
| 1y / YTD | ARCHIVE: 09-15 close **$273.31**; YTD **+40.6%**; ~1Y +157% | ARCHIVE prices |
| vs LITE | 같은 AI광학이어도 P/S **~1/3** — Industrial·상각·FCF 음수·모듈 믹스가 할인 | archive T4 |

## 4. Supply/demand & positioning
- **13F:** Duquesne 2Q26 **COHR 전량 청산**(1Q 40.4k주, 0.29%). **Whalerock** 2Q26 COHR **1,222,035주** ($482M) — 1Q 975k에서 **증액**. Appaloosa/Tiger 등 아카이브 정규화에 COHR **미히트**.
- **Analyst:** Citi ECOC 09-21/22 — 수직계열+LTA+어셈블리; Stifel/KIS TP **$420**(r-20260922-x4). 미즈호: OPM 2028E 20%중반 정체 가능.
- **Capacity:** 6" InP/GaAs 증설·Sherman; NVDA 연계 CPO 램프 주장. 캐파 4×는 **병목 완화 = 2년 뒤 수급 재균형**의 양면(Ciena backlog 감소 발언과 정합).

## 5. Edge card
| | |
|--|--|
| **priced_in** | DC&C +40%·AI 광학 내러티브·상대 저P/S. “조정하면 싸다”는 **상각·Industrial 역성장**을 가린 값. |
| **variant** | (a) Industrial 안정 + 상각 영향 축소 + GPM→42%+ + CPO 매출 분리 확인 → 리레이팅. (b) FCF− 지속·모듈 ASP 경쟁·LITE 레이저 의존으로 마진 정체. |
| **breaks_if** | FY27 Q1 DC&C 성장 급감; Industrial 재악화; 회사 말한 GPM 경로가 더 지연; 4Q26 CPO “램프”가 수사로 판명. |
| **residual** | **Med** — 상대가치·세그 스토리는 있으나 실행·FCF·마진 타임라인 불확실. |

## 6. Open questions / thin spots
- II-VI 무형상각 잔여 스케줄·현금 영향 0 여부
- LITE로부터의 레이저 구매 규모(원가 열위 실측)
- CPO 매출 분리 공시 여부(4Q26 판정)
- Preferred/mezz 정리 후 equity 구조(10-K 디테일)

---

# 3. CIEN — Ciena Corporation

## 1. Business
- **Products:** DCI·장거리 **코히런트 시스템**(WaveLogic DSP 내재), 플러거블/인터커넥트; **Nubis** 인수로 AEC·리타이머 등 DC 내부 구리/광 경계 진입. FY부터 Optical Systems / Interconnects / Global Services / Routing 보고 재편(theses — Interconnects 분리 예정).
- **AI-optical role:** 캠퍼스·건물간·DCI — 전력이 캠퍼스에 안 들어와 **여러 DC를 한 컴퓨터처럼** 묶는 수요. “광통신주” 중 **시스템 층** 대표(primer). Cloud 직접 매출 +80%대(cooling page/②).
- **Customers:** WEB Q3 FY26: cloud **53%** of sales, +82% YoY; **2 customers &gt;10%** each. DCOM ~30만대(Meta) 등 ③ 서술.
- **Moat:** 라인시스템 점유 ~70%, 고성능 코히런트 &gt;50%(2위 Nokia) — Citi ECOC ③. 수직계열 DSP + LTA로 공급 잠금. 다만 펌프/패키징은 **외부 부품 병목**에 노출(자사 발언).
- **Competitors:** Nokia, Cisco(800G 플러거블), Infinera/기타; 플러거블은 모듈사·InnoLight 등과 겹침; Nubis로 Credo/Astera 등과 AEC 경쟁 가능.

## 2. Financials
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Latest Q (BRAIN) | Rev **$1,571M**, OPM **15.2%**, EBIT YoY **+586%** (Q ended **2026-07-31**) | BRAIN ① — **Q2 FY26 창** |
| Latest Q (WEB 갱신) | **Q3 FY26** (ended **2026-08-01**): Rev **$1.67B** (+37% YoY); adj GM **46.4%**; adj OPM **22.5%** (GAAP OPM **18.0%**); adj EPS **$2.11** | WEB IR **2026-09-03** |
| FY26 guide | WEB: rev **$6.42B** ±50M (~+35% YoY); FY adj OPM **20–21%** | WEB |
| FY27 early view | WEB: rev growth **≥30%**, adj OPM **25–27%** (가정: cloud AI 지출·부품 공급 안정) | WEB ③/mgmt |
| Backlog | BRAIN: **$10B+** (② JPM 09-04); WEB Q3: **$8.5B** (+$0.8B QoQ), YE **&gt;$10B** 기대 | 혼재 — 시점 라벨 필수 |
| Cash | WEB 10-Q asof **2026-08-01**: cash **$2.446B** + investments **~$0.40B** ≈ **$2.84B** liquidity | WEB |
| Debt | WEB: LT debt **~$3.23B**, net debt small (~$0.4B) | WEB |
| Concentration | WEB: cloud 53%; top-2 &gt;10% each → **고객 집중 리스크** | WEB |

## 3. Valuation snapshot
| | | |
|--|--|--|
| BRAIN P/S·P/E | facts에 **미수록** (CIEN metrics = rev_q/opm/backlog 중심) | thin in facts |
| Price | ARCHIVE 09-15 **$327.43**; YTD **+33.1%**; ~1Y +141%; YE24→ +292% | ARCHIVE |
| WEB color | Evercore TP $375→**$550** (09-21, routing); 시스템 벤더로 자금 유입 서술 | WEB/③ |
| Note | 배수 비교 시 **시스템 층** vs 광원 층을 섞지 말 것(T5) | archive |

## 4. Supply/demand & positioning
- **13F:** Whalerock **1Q26** CIEN 231k주 ($90M) — **2Q26 정규화 파일에 CIEN 행 없음**(청산 또는 미포함 — **확인 필요**). Duquesne optical 3사 청산에 CIEN **미포함**.
- **Analyst:** Citi ECOC 09-22 — 공급 제약 없으면 올해 매출 $8B+ 가능했으나; 경영진 “잔고 과다 = 미충족 수요라 부정적, **향후 2년 잔고 감소** 예상”. JPM 09-12 병목=펌프/패키징. Nubis/XPO FY28 매출 인식 = T5 판정.
- **Capacity/LTA:** 핵심 부품 LTA through **2029**(WEB call); 증분 캐파로 성장 지원.

## 5. Edge card
| | |
|--|--|
| **priced_in** | Cloud/AI DCI 가속, 마진 레버리지, backlog 스토리, 애널 TP 상향. |
| **variant** | (a) FY27 ≥30% + OPM 25%+ + Interconnects(Nubis) 기여 → 시스템→칩 경계 성공. (b) 펌프 병목·2고객 집중·backlog 정상화가 “수요 피크”로 재해석. |
| **breaks_if** | FY27 cloud 성장 실종; Nubis AEC 매출 FY28 미인식; adj OPM이 20%대에서 되돌림; 공급 정상화 후 ASP 압박. |
| **residual** | **Med** — 실적 모멘텀 강하나 고객 집중·부품 병목·밸류에이션(facts 공백) 잔여. |

## 6. Open questions / thin spots
- facts에 TTM P/S·현금·세그먼트 **미적재** (우선 채움 대상)
- Whalerock 2Q26 CIEN 포지션 확정
- WaveLogic vs 플러거블 믹스·800G/1.6T 점유 실측
- Nubis 기여 타임라인·매출 인식 기준

---

# 4. GLW — Corning Incorporated

## 1. Business
- **Products:** 광섬유·광케이블·커넥티비티(Optical Communications) + Glass Innovations(디스플레이 등) + Solar(Hemlock 등) + Life Sciences. (`entities` ②; Vertiv·Corning deep)
- **AI-optical role:** 트랜시버 방식이 EML/SiPho/CPO 중 무엇이든 **유리는 필요**(primer). Enterprise/GenAI 파이버·케이블 수요; scale-out 중심, scale-up/photonics는 **아직 실적에 거의 없음**(call ③).
- **Customers:** **Amazon** 다년·수십억$ 광섬유·케이블·커넥티비티 공급(회사/Amazon 발표 ②); **NVIDIA** 장기 파트너십·Optical 캐펙스 확대와 연계(deep page). 10%+ 고객 공시 없음 계열(인접 섹터 편 — “안 밝힘”).
- **Moat:** Optical 1위 스케일 + **계약이 붙은** Springboard 공약($20B→$30B→$40B 연환산 매출). Optical 캐펙스 2Q $87M→$180M(+107%).
- **Competitors:** Prysmian 등 케이블; Amphenol/TE(커넥터 — 인접); 유리·디스플레이는 AGC 등. AI 테마 안에서는 VRT와 “낙폭 vs 논거” 페어로만 묶임.

## 2. Financials
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| BRAIN facts | **metrics 비어 있음** — “광통신 축 확정 지표 없음” | BRAIN note |
| 2Q26 Optical | Rev **$2,072M** (+32.3% YoY); seg NI **$438M** (+77%); NI margin **21.1%** (prior 15.8%); Optical = 매출 **46.6%** but 이익 **~50%+** | ARCHIVE deep ① 10-Q |
| 2Q26 Glass Innovations | **$1,463M** (+1.4%), NI $354M | ARCHIVE |
| 2Q26 Solar | **$438M** (+89.6%) but NI **−$7M**; H1 NI **$0**; assets $3.0B = 14.6% of co. | ARCHIVE — **구멍** |
| Life Sci / other | Rev −14.8%, NI +$6M→**−$21M** | ARCHIVE |
| Core (company) | 2Q core sales ~**$4.74B** (+17%), core OPM **20.9%**, core EPS +30% 등; GAAP sales **$4.505B** (core−GAAP gap ~$235M) | ARCHIVE / WEB IR **2026-07-28** |
| Cash / debt | WEB 06-30-2026: cash **~$2.50B**; debt **~$8.42B** ($0.67B current + $7.76B LT) | WEB 10-Q |
| FCF | WEB/IR: 2Q OCF ~$1.72B, adj FCF ~$1.42B (강한 현금창출력) | WEB |
| Springboard | $20B(2026말)→$30B(2028)→$40B(2030); 4y CAGR ~19% 공약 vs 3Q guide +16%로 **단기 &lt; 공약** | ARCHIVE T6/T7 |
| 판정 창 | 3Q26 core sales **≥$4.9B**; Optical capex ≥2Q 수준; Solar 흑자 여부 | events/theses **2026-10** |

## 3. Valuation snapshot
| | | |
|--|--|--|
| Price | ARCHIVE 09-15 **$144.02**; YTD **+58.8%**; ~1Y +85%; YE24→ +203% | ARCHIVE |
| Drawdown context | “고점 대비 −41.4%”는 06-29 **하루 스파이크 $255.69** 분모 — 스파이크 전≈$221 기준이면 ≈**−32%**(§A7-0) | ARCHIVE deep T1 |
| WEB | 시점 혼선 주의(일부 페이지 Jul px). Mid-Sep WEB ~**$145–152** band; trailing P/E 높은 편(디스플레이 믹스) | WEB — **라벨 WEB, 재확인 필요** |
| P/S | facts 없음; Optical-only 배수가 아님(다각화 할인/할증) | thin |

## 4. Supply/demand & positioning
- **13F:** Whalerock 2Q26 GLW **2.23M주** ($571M) — 1Q 대비 소폭 감소. Appaloosa 1Q26 Corning **1.13M주**. GS 포지셔닝(③): 2Q26 헤지펀드 GLW **순감소** 사분면.
- **ATM:** 09-14 Corning **$2B ATM** → 광통신 섹터 −8~−13% 데이(routing r-20260915-05) — 수요가 아니라 **주식 공급** 쇼크.
- **LTA:** Amazon multibillion multi-year fiber/cable/connectivity(②); NVIDIA partnership + Optical capex 증거.

## 5. Edge card
| | |
|--|--|
| **priced_in** | AI 파이버 내러티브·Springboard·Amazon/NVIDIA 계약 헤드라인. 낙폭은 “논거 약함”이 아니라 **기대>가이던스/스파이크 분모**. |
| **variant** | (a) 3Q26 core≥$4.9B + Optical capex 유지 + Solar 개선 → “두 축 갈림” 해소. (b) Optical만으로 기업가치 지탱, Solar/LifeSci 구멍 지속, ATM 추가 희석. |
| **breaks_if** | Optical 성장이 Enterprise GenAI 둔화로 꺾임; 계약이 capex로 안 뒷받침; Solar 적자 고착·자산손상. |
| **residual** | **Med** — Optical 질은 확인, 전사 구멍·밸류에이션 facts 공백·희석. |

## 6. Open questions / thin spots
- **facts.GLW metrics 전무** (open: optical-facts-7) — TTM rev/GPM/OPM/P/S 채우기
- Amazon/NVIDIA 계약 **금액 미공시**
- Optical vs non-optical 가치 분해(소엄 합산 함정)
- 3Q26(10월) 네 채점표 결과

---

# Comparative cheat sheet (archive-first)

| | LITE | COHR | CIEN | GLW |
|--|------|------|------|-----|
| Layer | 레이저 병목 | 광원+모듈 | 시스템/DCI | 파이버 |
| Rev scale | ~$3.0B FY | ~$7.1B FY | ~$6.4B FY guide | Optical Q ~$2.1B |
| Latest GPM/OPM | 47%/28% | 37.5%/7.8%(adj 12.7%) | adj 46%/22.5% (Q3) | Optical NI 21%; core OPM ~21% |
| P/S (brain/WEB) | ~28–30× | ~8–9× | facts thin | facts thin |
| Balance | Net cash-ish | Debt+FCF− | Near net-neutral | Levered but FCF+ |
| 13F flag | Duquesne out | Duquesne out; Whalerock in↑ | Whalerock ? | Whalerock hold↓ |
| Next gate | FY27 Q1 ~Nov GPM/OPM | FY27 Q1 DC&C/OPM; 4Q26 CPO | FY27 guide delivery; Nubis | **3Q26 Oct** core $4.9B |

---

# Source index
1. `brain/facts.json` companies LITE·COHR·CIEN·GLW — asof mostly **2026-09-11** (CIEN backlog 09-04)
2. `brain/entities.json`, `brain/theses.json` optical_valuechain_9 / kr_cooling / us_vertiv_corning_deep / us_ai_adjacent
3. `brain/routing.jsonl` r-20260912 → r-20260922 (Mizuho, Citi ECOC, Duquesne 13F, ATM)
4. `data/13f/2026Q1|Q2` Duquesne·Whalerock·Appaloosa·Tiger
5. `intake/files/prices_daily/{LITE.O,COHR.K,CIEN.K,GLW}.json` through **2026-09-15**
6. WEB: Lumentum IR 2026-08-11; Coherent IR 2026-08-12; Ciena IR 2026-09-03; Corning IR/10-Q 2026-07-28; secondary valuation pages Sep 2026

