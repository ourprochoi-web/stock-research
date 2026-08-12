# AI 전력 인프라 리서치 — 테마 C+D 심화: 송배전 병목 & DC 전력혁명

> 목적: 테마 C(송배전 병목: 변압기·케이블·HVDC)와 테마 D(DC 전력혁명과 냉각 전환)의 심화 리서치
> 기반 데이터: `research_ai_power_part12_overview.md` (2026-06-22)
> 작성일: 2026-06-23
> 상태: 심화 리서치 완성본

---

# 테마 C — 송배전 병목: 변압기·케이블·HVDC

## C-1. 변압기 공급 부족 심화

### C-1-1. 리드타임 및 공급 부족 현황 (Wood Mackenzie Q2 2025)

| 지표 | 수치 | 출처 |
|------|------|------|
| 전력 변압기 평균 리드타임 | **128주** (~2.5년) | Wood Mackenzie Q2'25 Survey |
| GSU(Generator Step-Up) 리드타임 | **144주** (~2.8년) | Wood Mackenzie |
| 리드타임 변화 추이 | 6–12개월(pre-2020) → **24–48개월**(2026) | Power Magazine, IEEE Spectrum |
| 전력 변압기 공급 부족률 | **30%** (2025) → **5%** 미만 (2030E) | Wood Mackenzie |
| GSU 공급 부족률 | **47%** (2025) → **14%** (2030E) | Wood Mackenzie |
| 배전 변압기 공급 부족률 | **10%** (2025) | Wood Mackenzie |
| 수요 증가율 (2019 대비) | 전력 변압기 **+119%**, 배전 변압기 **+34%** | Wood Mackenzie |
| 가격 상승 | **+60–80%** (추가 상승 여지 지속) | Electrical Trader |
| 미국 노후 배전 변압기 | ~**4,000만대** 수명 초과 | Wood Mackenzie |
| 미국 전력망 노후화 | **70%가 1960년대** 건설 | DOE |
| 수입 의존도 (2025) | 전력 변압기 **80%**, 배전 변압기 **50%** 수입산 | Wood Mackenzie |

**구조적 진단:**
- 공급 부족은 2030년까지 점진적으로 완화될 전망이나, Wood Mackenzie는 변압기 가격이 **2030년까지 계속 상승**할 것으로 예측 — 수요 증가 속도가 공급 확대를 계속 앞서는 구조
- 패드마운트 3상 변압기: 데이터센터·제조·EV 충전 수요 급증으로 부족 **악화** 전망
- 공급자 우위 시장이 최소 2027–2028년까지 지속 → 한국 3사 판가 협상력 유지

**출처:**
- [Wood Mackenzie 공식 발표: 전력·배전 변압기 30%·10% 공급 부족](https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/)
- [Wood Mackenzie: 변압기 수급 위기 분석](https://www.woodmac.com/news/opinion/transformer-troubles-manufacturing-and-policy-constraints-hit-us-transformer-supply/)
- [Power Magazine: Transformers in 2026 — Shortage, Scramble, or Self-Inflicted Crisis?](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- [pv magazine USA: 그리드 변압기 공급 부족](https://pv-magazine-usa.com/2025/08/14/grid-transformers-face-significant-supply-deficits-says-wood-mackenzie/)

---

### C-1-2. 한국 3사 북미 실적 (Q1 2026 — 분기 최대 갱신)

#### HD현대일렉트릭

| 지표 | 수치 | 비고 |
|------|------|------|
| Q1 2026 매출 | 1조 365억 원 | YoY +2.1% |
| Q1 2026 영업이익 | **2,583억 원** | YoY +18.4% |
| Q1 2026 영업이익률 | **24.9%** | 전력기기 매출 +21.6% 주도 |
| Q1 2026 신규 수주 | **17억 9,700만 달러** | YoY +34.6%; 연간 목표의 42.6% |
| Q1 2026 수주잔고 | **78억 8,800만 달러** | QoQ +17.2% |
| 앨라배마 제2공장 | 투자 약 **2억 달러** (2,981억 원) | 2만 9,000㎡, 준공 2027년 4월 목표 |
| 앨라배마 증설 효과 | 생산능력 **+50%**, 추가 매출 ~2,000억 원/년 | 신규 고용 200여 명 |
| 765kV 초고압 변압기 | 북미 시장 **사실상 과점** | 인증 장벽 — 경쟁사 진입 수년 소요 |

- Q1 2026: 북미 전력변압기 매출 확대가 성장 주도. **1730억 원 규모 초고압 변압기 공급 계약** 추가 체결 (2026.05)
- 2026년 연간 신규 수주 목표 42억 2,200만 달러 → 북미 765kV 수요 본격화 시 **50억 달러**까지 확대 가능 전망 (유안타증권)

**출처:**
- [뉴스핌: HD현대일렉트릭 1분기 영업익 2583억](https://www.newspim.com/news/view/20260428000851)
- [HD현대일렉트릭 앨라배마 제2공장 착공](https://www.ftoday.co.kr/news/articleView.html?idxno=356158)
- [서울경제: 생산능력 50% 확대](https://www.sedaily.com/article/20016481)
- [한국경제: 앨라배마·울산 증설 분석](https://www.hankyung.com/article/202604282715i)

---

#### LS일렉트릭

| 지표 | 수치 | 비고 |
|------|------|------|
| Q1 2026 매출 | **1조 3,766억 원** | YoY +33% |
| Q1 2026 영업이익 | **1,266억 원** | YoY +45% |
| Q1 2026 수주잔고 | **5조 6,425억 원** | QoQ +13% |
| 초고압변압기 수주잔고 | **3조 1,024억 원** | 전체 수주잔고의 55% |
| Q1 2026 북미 매출 | 약 **3,000억 원** | YoY +80%; 분기 최대 |
| 북미 빅테크 수주 | **1억 1,497만 달러** (~1,703억 원) | 하이퍼스케일 DC 전력 인프라, 연내 매출 반영 |
| DC 솔루션 | 북미 DC 마이크로그리드향 직류(DC) 제품 수주 | DC 전력 전환 수혜 포지션 |

- 국내보다 해외 매출 비중이 더 높아진 첫 분기 달성 (2026 Q1)
- 연간 영업이익 **6,000억 원 시대** 진입 전망 (뉴시스)
- 초고압변압기 + DC 배전 토탈 솔루션 = 테마 C+D 동시 수혜

**출처:**
- [네이트뉴스: LS일렉트릭 1분기 역대 최대 실적](https://news.nate.com/view/20260421n19556)
- [뉴시스: LS일렉트릭 북미 빅테크 특수, 영업익 6000억 시대](https://www.newsis.com/view/NISX20260421_0003599950)
- [디일렉: LS일렉트릭 1분기 영업익 45% 증가](https://www.thelec.kr/news/articleView.html?idxno=55425)

---

#### 대한전선

| 지표 | 수치 | 비고 |
|------|------|------|
| Q1 2026 매출 | **1조 834억 원** | YoY +26.6%; 분기 최대 |
| Q1 2026 영업이익 | **604억 원** | YoY **+122.9%**; 분기 최대 |
| Q1 2026 신규 수주 | 7,340억 원 | — |
| Q1 2026 수주잔고 | **3조 8,273억 원** | 역대 최대; 2021년 말 대비 3.5배+ |
| 당진 해저케이블 2공장 | 525kV HVDC + 345kV 해저케이블 생산 | 2026년 건설 완료, **2027년 상반기 가동** |
| HVDC 레퍼런스 | 미국 수주 320kV HVDC 케이블 | 525kV급으로 확장 전략 |

- AI DC 수요(미국·싱가포르 등)가 초고압 프로젝트 매출 견인
- 2026 IEEE PES T&D 시카고 참가 — HVDC·해저케이블 솔루션 북미 마케팅 강화
- 하나증권 목표가 상향; PER 133배는 밸류에이션 부담으로 지적

**출처:**
- [이투데이: 대한전선 1분기 매출 1조834억·영업이익 604억](https://www.etoday.co.kr/news/view/2580441)
- [네이트뉴스: 대한전선 분기 최대 실적](https://news.nate.com/view/20260429n25390)
- [한국경제: 대한전선 분석](https://www.hankyung.com/article/202604307734i)
- [대한전선 당진 해저케이블 2공장 착공](https://www.taihan.com/news/pr/releaseDetail?idx=422)
- [대한전선 북미 HVDC 전략](https://news.nate.com/view/20260506n25155)

---

#### 한국 3사 통합 비교 (Q1 2026)

| 기업 | Q1 매출 | Q1 영업이익 | OPM | 수주잔고 | 핵심 포지션 |
|------|---------|------------|-----|---------|-----------|
| HD현대일렉트릭 | 1조 365억 원 | 2,583억 원 | **24.9%** | 78.9억 달러 | 765kV 초고압 변압기 북미 과점 |
| LS일렉트릭 | 1조 3,766억 원 | 1,266억 원 | 9.2% | 5조 6,425억 원 | 초고압변압기 + DC 솔루션 |
| 대한전선 | 1조 834억 원 | 604억 원 | 5.6% | 3조 8,273억 원 | HVDC·해저케이블 |

- **2026년 AI 대호황**: 3사 합산 분기 매출 ~3조 5,000억 원, 수주잔고 합산 ~20조 원 돌파 수준
- 공통 특징: 분기 최대 실적 경신, 수주잔고 역대 최고

**출처:**
- [파이낸셜뉴스: 전력인프라 7곳 1분기 10조 수주](https://www.fnnews.com/news/202606161817592402)
- [인베스트조선: K전력 빅3, 1분기 나란히 최대실적](https://www.investchosun.com/site/data/html_dir/2026/04/27/2026042780117.html)
- [디지털타임스: HD현대일렉·LS일렉·대한전선 북미 대격돌](https://www.dt.co.kr/article/12058434)

---

### C-1-3. 미국 관세 리스크 최신 동향

| 지표 | 내용 | 출처 |
|------|------|------|
| Section 232 한국산 철강·알루미늄 | 2025 하반기 미·한 무역협상 진행 | CFR, Congress.gov |
| 미·한 무역협정 (2025.07) | Section 232 자동차 관세 15%로 인하, 반도체·의약품 MFN 지위 부여 | USTR |
| 전기기기 관세 | 전력 변압기 직접 관세 명시는 미확정 — 협상 변수 | USTR |
| 현지 생산 헤지 | HD현대일렉트릭 앨라배마 현지 공장이 관세 리스크 완충 | 업계 |

- **핵심 포인트**: 한국산 변압기에 대한 관세 직접 부과 여부는 2026년 하반기 무역협상의 핵심 변수. 현지 생산 비중 확대(HD현대 앨라배마, LS일렉 현지화 검토)가 대응책
- 미국의 변압기 수입 의존도(전력 변압기 80%)가 역설적으로 한국산 수입을 보호하는 구조

---

## C-2. HVDC 시장

### C-2-1. 시장 규모 전망

| 지표 | 수치 | 출처 |
|------|------|------|
| AI DC HVDC 전력 시스템 시장 | **$1.53B (2025) → $4.59B (2035)**, CAGR **11.62%** | Precedence Research |
| AI DC HVDC 인프라 시장 (광의) | $18.6B (2025) → $109.4B (2034), CAGR **22.5%** | MarketIntelo |
| 800V HVDC DC 버스 시장 | ~**$5.4B by 2031**, CAGR ~**132%** (2026–2031) | Mobility Foresights |
| 글로벌 그리드 투자 | **$5.8T (2026–2035)**, 디지털 그리드 ~$700B | Morgan Stanley / IEA |
| 글로벌 연간 그리드 투자 | **$470B+ (2025)** — 사상 최초 $470B 돌파 | BloombergNEF |
| 지역별 비중 | 중국 ~1/3, 미국 ~$1T/10년, EU ~$1.1T/10년 | Morgan Stanley |

- **북미 시장 주도**: 2025년 기준 HVDC 시장의 **39%+** 점유. 재생에너지 장거리 송전 + AI DC 직류 아키텍처 전환이 동시에 HVDC 수요 자극
- **정의 차이 주의**: "AI DC HVDC"(협의, $1.53B)와 "AI DC HVDC 인프라"(광의, $18.6B)는 범위가 다름

**출처:**
- [Precedence Research: AI DC HVDC 시장 $4.59B by 2035](https://www.precedenceresearch.com/ai-data-center-hvdc-power-supply-system-market)
- [BloombergNEF: 글로벌 그리드 투자 $470B 돌파](https://about.bnef.com/insights/clean-energy/global-grid-investment-could-top-470-billion-for-the-first-time-in-2025-bloombergnef/)
- [EnkiAI: NVIDIA HVDC Power 2026](https://enkiai.com/ev/nvidia-hvdc-power-data-centers/)

---

### C-2-2. Grain Belt Express — 미국 역사상 최대 송전 프로젝트

| 지표 | 수치 | 출처 |
|------|------|------|
| 총 투자 규모 | **$11B** | ConstructConnect |
| 송전 거리 | **800마일** (캔자스 → 미주리 → 인디애나 → 오하이오) | Grain Belt Express |
| 용량 | **5,000 MW** | Grain Belt Express |
| 시공사 계약 | Quanta Services + Kiewit Energy에 **$1.7B** 계약 | Invenergy |
| 착공 | Phase 1 (캔자스-미주리): **2026년** | Grain Belt Express |
| 토지 확보 | Phase 1 주선로의 **95%+** 완료, 지역권 $105M+ 체결 | Grain Belt Express |
| DOE 대출보증 | 2025.07.23 **조건부 약정 철회** → 민간 금융으로 전환 | DOE |

- 미국 역사상 최대 규모 단일 송전선. DOE 대출 보증 철회에도 민간 파이낸싱으로 계속 추진
- 풍력 발전(캔자스·오클라호마)을 부하 집중지(인디애나·오하이오)로 연결 → 재생에너지 + AI DC 부하 동시 해소 목적

**출처:**
- [ConstructConnect: $11B Grain Belt Express 2026 착공](https://news.constructconnect.com/11b-grain-belt-express-transmission-line-slated-for-construction-in-2026)
- [Grain Belt Express: $1.7B 시공 계약 발표](https://grainbeltexpress.com/grain-belt-express-awards-1-7b-to-u-s-contractors-quanta-and-kiewit-to-build-largest-transmission-line-in-u-s-history/)
- [TD World: Grain Belt Express 기술·영향 분석](https://www.tdworld.com/overhead-transmission/article/55324933/transforming-the-us-grid-the-impact-and-engineering-of-the-grain-belt-express-hvdc-line)

---

## C-3. 계통연계 큐(Grid Interconnection Queue) 병목

### C-3-1. 병목 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| 미국 계통연계 대기 용량 | **2,600 GW** (2025년) | LBNL Queued Up 2025 |
| 대기 건수 | 활성 프로젝트 수천 건 (발전 1,570 + 저장 1,030 GW) | LBNL |
| 설치 용량 대비 | 현재 설치 용량(1,279 GW)의 **2배 이상** | Latitude Media |
| 2026년 말 COD 목표 | 대기 용량의 **49%** (1,271 GW)가 2026년 말 상업 운전 목표 | LBNL |
| 중앙 대기기간 | 상업 운전까지 **~5년** (2,100일+) | LBNL |
| 대기기간 증가 | 2017년 이후 **~60% 증가** | Enverus |
| 프로젝트 철회율 | **~80%** (비용·지연으로 포기) | LBNL / PV Tech |
| 계통연계 비용 | 철회 프로젝트 예산의 **30–37%** 차지 | LBNL |

**지역별 병목 심화:**
- 북버지니아·피닉스·댈러스: 큐 대기기간 **4–7년**, 2026.05 신청 시 전력 확보 예상: **2030–2033년**
- 빅테크가 BTM(자가발전) 전략으로 전환하는 가장 직접적 원인

**출처:**
- [LBNL Queued Up 2025 Edition](https://emp.lbl.gov/publications/queued-2025-edition-characteristics)
- [EnkiAI: 계통연계 지연 2026](https://enkiai.com/ai-market-intelligence/grid-interconnection-delays-2026-a-threat-to-us-energy/)
- [Latitude Media: 큐 용량이 설치 용량의 2배](https://www.latitudemedia.com/news/the-us-interconnection-queue-is-twice-its-installed-capacity/)
- [RMI: 계통연계 큐가 AI 데이터센터에 미치는 영향](https://rmi.org/interconnection-reform-ai-data-centers-generator-queues/)

---

## C-4. 데이터센터 NIMBY / 모라토리엄

### C-4-1. 프로젝트 차단·지연 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| 차단·지연 프로젝트 총액 | **$64B** | Data Center Watch |
| Q1 2026 분기 최고 피해 | **$130B** (Q1 2026 단독, 역대 최대) | Startup Fortune |
| 모라토리엄 시행 지자체 | **69개** (4건은 영구) | Tom's Hardware |
| 법안·결의 건수 | **222건 / 30개 주** | Moratorium Nation |
| 증가 속도 | 8건 (2025.05) → **78건+** (2026.05), 1년간 **~10배** | Tom's Hardware |
| 시민단체 조직화 | **142개 단체 / 24개 주** (버지니아만 42개) | Data Center Watch |

### C-4-2. 주요 입법 현황

| 법안/사건 | 내용 | 날짜 |
|----------|------|------|
| **뉴욕주 모라토리엄** | 피크 수요 **20MW 이상** DC에 1년 신규 허가 중단. Responsible Data Center Development Act. 주지사 Hochul 서명 대기 중 | 2026.06.05 통과 |
| 뉴욕주 규모 | 대기 중 DC 28개 프로젝트, 추가 전력 수요 **9,682 MW** 예상 | 뉴욕주 상원 |
| Maine 주지사 거부권 | DC 관련 법안 거부권 행사 | 2026.04.24 |
| Virginia HB 1515 | 2027년으로 이월 | 2026 회기 |
| Spokane 500 MW DC | 주민 5,000명+ 민원으로 Avista 검토 중단 | 2026 |

- **핵심 리스크**: 수요가 아니라 건설 **'속도'**를 늦혀 기자재 매출 인식 타이밍을 지연시키는 구조적 리스크
- 뉴욕 모라토리엄이 주지사 서명 시 **전국 최초** 주 단위 모라토리엄이 되며 파급효과 예상

**출처:**
- [Data Center Watch: $64B 프로젝트 차단·지연 보고서](https://www.datacenterwatch.org/report)
- [Startup Fortune: Q1 2026 반대 운동으로 $130B 지연](https://startupfortune.com/opposition-groups-halted-130-billion-in-data-center-projects-in-q1-2026/)
- [Inside Climate News: 뉴욕 모라토리엄 진행](https://insideclimatenews.org/news/04062026/new-york-data-center-moratorium-bill/)
- [NYSenate.gov: 뉴욕 모라토리엄 법안 통과 보도자료](https://www.nysenate.gov/newsroom/press-releases/2026/kristen-gonzalez/ny-state-senator-kristen-gonzalez-passes-data-center)
- [Mintz: 뉴욕주 데이터센터 모라토리엄 법률 분석](https://www.mintz.com/insights-center/viewpoints/55076/2026-06-12-new-york-legislature-passes-first-nation-data-center)

---

## C-5. 테마 C 투자 시사점

### 공급자 우위 유지 기간 추정

```
변압기 공급 부족:  2025 ──────────────────── 2030E (30%→5%로 점진 완화)
                  ↑현재 공급자 최대 우위     ↑수요·공급 균형 회복
가격 상승:        2025 ── 상승 지속 ──────── 2030E (가격 상승은 균형 후에도 지속 가능)
HD현대 증설:           ── 2026 ──── 2027.04 준공 (CAPA +50%, 매출 +2,000억/년)
대한전선 2공장:        ── 2026 ──── 2027H1 가동 (525kV HVDC 추가)
```

### 투자 등급별 평가

| 기업/자산 | 단기 (6개월) | 중기 (2년) | 리스크 |
|----------|------------|----------|--------|
| HD현대일렉트릭 | ★★★★★ — 수주잔고 가시성 최고, OPM 25% | ★★★★★ — 앨라배마 증설 후 매출 레버리지 | 밸류에이션 부담, 관세 |
| LS일렉트릭 | ★★★★☆ — DC+변압기 이중 수혜 | ★★★★★ — DC 전환 수혜 본격화 | 고객 집중 |
| 대한전선 | ★★★★☆ — 영업이익 YoY +123% | ★★★★☆ — 2공장 HVDC 증설 | PER 133배 밸류 부담 |
| Hitachi Energy | — | ★★★★☆ — 미국 $1B 투자 발표 | 글로벌 경쟁 |

---

## C-6. 테마 C 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| Wood Mackenzie 분기 변압기 리드타임 서베이 | 분기 | 128주 → 단축 시 공급자 우위 약화 신호 |
| 한국 3사 분기 수주 및 잔고 | 분기 | YoY 성장률 둔화 시 경보 |
| 뉴욕 주지사 모라토리엄 서명 여부 | 즉시 | 서명 시 타 주 도입 가속도 위험 |
| 모라토리엄 건수 (현재 222건) | 월간 | 300건 돌파 시 전체 DC 건설 속도 저하 |
| Grain Belt Express Phase 1 착공 진행 | 분기 | 착공 지연 시 HVDC 수요 후행 |
| 미·한 무역협상 전기기기 관세 조항 | 상시 | 변압기 직접 관세 도입 여부 |
| US 계통연계 큐 대기기간 변화 | 반기 | 대기기간 단축 시 BTM 수요 압력 완화 |

---

---

# 테마 D — DC 전력혁명과 냉각 전환

## D-1. 800V DC 아키텍처 전환

### D-1-1. 기술 구조와 효율 개선

| 지표 | 수치 | 출처 |
|------|------|------|
| 전력 전송 효율 | 480 VAC 대비 같은 도체에 **85% 더 많은 전력** 전송 | IEEE Spectrum |
| End-to-end 효율 향상 | 최대 **5%** (전체 효율 92%+ 달성) | Power Electronics News / NVIDIA |
| 전류 감소 | ~15배 감소 (열 손실 I²R 비례 감소) | YK Investment Research |
| 유지보수 비용 절감 | 최대 **70%** (UPS·PDU 단계 제거) | NAND Research |
| UPS·PDU 제거 | 랙 레벨 AC/DC 변환 단계 완전 제거 | NVIDIA Technical Blog |
| 타겟 랙 전력 | **600 kW+/rack** (Rubin Ultra 기준) | YK Investment Research |

**아키텍처 원리:**
- 기존: 중압 AC → 변압기 → 저압 AC → UPS → PDU → 랙 내 AC/DC 변환(여러 단계)
- 800V DC: 중압 → SST(Solid-State Transformer)로 **800V DC 직출력** → 랙까지 DC 단선. LLC 공진 변환 **단 1단계**

### D-1-2. 배포 일정 및 생태계

| 플레이어 | 내용 | 시기 |
|---------|------|------|
| **NVIDIA Rubin Ultra** | 800V DC 아키텍처 기반 Kyber 랙. **1MW/rack** 목표 | 2027 양산 배포 |
| **Vertiv** | 800V DC 풀 제품라인 (Vertiv + NVIDIA 공동 개발 완료) | **H2 2026** 상용 출시 |
| **Delta Electronics** | 800V DC 배치 이미 시작 | 2026 |
| **Eaton** | 800V DC 레퍼런스 아키텍처 출시 | 2025.10 |
| **SolarEdge** | 99% 효율 SST(Solid-State Transformer) 개발 | 개발 중 |
| **하이퍼스케일러 Phase 1-2** | 파일럿 → 본격 배포 | **2026 말~2027 초** |

### D-1-3. 시장 도입 전망

| 지표 | 수치 | 출처 |
|------|------|------|
| DC 도입 계획 (2028년까지) | **45%**의 데이터센터 운영사 | Bloom Energy 2026 |
| 고압 중앙 버스웨이 도입 계획 | **60%**가 2028년까지 | Bloom Energy 2026 |
| 신규 DC의 DC 기반 비중 | **58%** by 2030 | Bloom Energy 2026 |
| 800VDC 누적 용량 전망 | **~39 GW** by 2030 | SemiAnalysis |
| 오프그리드 DC 자가발전 비중 | **1/3** by 2030 | Bloom Energy 2026 |

**과제:**
- UL 인증, 안전 코드, 지자체 승인의 느린 속도 → 현재는 하이퍼스케일러 파일럿 단계
- 기존 AC 인프라와의 하이브리드 운영 필요 — 완전 전환은 2028년 이후

**출처:**
- [NVIDIA Technical Blog: 800V DC 아키텍처](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [Data Centre Magazine: Vertiv·NVIDIA 800 VDC 협력](https://datacentremagazine.com/news/vertiv-and-nvidia-advance-800-vdc-for-ai-data-centres)
- [Data Center Dynamics: NVIDIA Rubin 1MW 랙 준비](https://www.datacenterdynamics.com/en/news/nvidia-prepares-data-center-industry-for-1mw-racks-and-800-volt-dc-power-architectures/)
- [Vertiv·NVIDIA PRNewswire 공식 발표](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html)

---

## D-2. SiC/GaN 전력반도체

### D-2-1. 시장 규모

| 조사기관 | 2025 | 2033/2034 | CAGR |
|---------|------|----------|------|
| DataM Intelligence | $2.2B | $11.3B (2033) | **22.5%** |
| Fortune Business Insights | $3.12B | $9.84B (2033) | — |
| SiC 모듈 단독 (FortBI) | $980.7M | $9,817M (2034) | **29.2%** |

### D-2-2. 주요 플레이어 동향

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **STMicroelectronics** | 시장 점유율 **32.6%** (#1) | Semiconductor Today |
| **Infineon** | NVIDIA MGX 에코시스템 합류 (2026.05), 800VDC 랙용 Si/SiC/GaN 라인업. 3.3kV CoolSiC 양산. PSS 부문 €1.5B (2026) → €2.5B (2027E, +67%) | Infineon |
| **Wolfspeed** | 세계 최초 **10kV SiC MOSFET** 출시 (2026.03.06). DC 매출 QoQ +50%. 200mm Mohawk Valley 팹 전환 완료 | Wolfspeed 8-K |
| **onsemi** | #2 시장지위 | 업계 |
| **ROHM** | Top 5 내 | 업계 |
| **Top 5 합계** | 시장의 **90%+** 점유 — 극도로 집중된 과점 | 업계 |

### D-2-3. 데이터센터 SiC 수요

- 800VDC 아키텍처 도입에 SiC/GaN 필수: SST(고전압 변환), 랙 레벨 DC-DC 컨버터, 버스웨이
- DC 관련 SiC 수요: 2026–2031년 **$200M+ 추가 기회** (업계 추산)
- GaN: 2025년부터 DC 적용 가속. AI 시스템 고전력 밀도 수요에 GaN 스위칭 주파수 특성 적합

**출처:**
- [Fortune Business Insights: SiC 디바이스 시장](https://www.fortunebusinessinsights.com/silicon-carbide-sic-devices-market-112103)
- [DataM Intelligence: SiC 반도체 시장 $11.3B by 2033](https://www.datamintelligence.com/research-report/silicon-carbide-semiconductor-market)
- [Wolfspeed: 10kV SiC MOSFET 출시](https://enkiai.com/ev/nvidia-hvdc-power-data-centers/)

---

## D-3. 랙 밀도 폭발과 냉각 수요

### D-3-1. AFCOM 2026 — 사상 최대 YoY 밀도 증가

| 지표 | 수치 | 출처 |
|------|------|------|
| 산업 평균 랙 밀도 (2021) | 7 kW | AFCOM |
| 산업 평균 랙 밀도 (2025) | 16 kW | AFCOM |
| 산업 평균 랙 밀도 **(2026)** | **27 kW** — 10년 추적 사상 최대 YoY 증가 | AFCOM 2026 |
| NVIDIA GB200 NVL72 | **130–132 kW/rack** | NVIDIA/HPE |
| NVIDIA Rubin Ultra (목표) | **~1 MW/rack** | NVIDIA (2027+) |
| AI 전용 랙 현재 범위 | 60–150 kW | 업계 |
| 차세대 AI 랙 | ~300 kW | Bloom Energy 2026 |
| 그 다음 세대 | ~1 MW | Bloom Energy 2026 |

### D-3-2. 냉각 불충분 현황

| 지표 | 수치 | 출처 |
|------|------|------|
| 현재 냉각 불충분 인식 | **~40%**가 현재 냉각이 운영 니즈 미충족 | AFCOM 2026 |
| 액체냉각 현재 도입률 | **19%** (2025) → **36%** (2026) | AFCOM 2026 |
| 12–24개월 내 도입 계획 | **+28%** 추가 도입 예정 | AFCOM 2026 |
| AI 영향 예상 | **72%**가 AI로 DC 용량 요건 증가 전망 (그 중 48%: 큰 영향) | AFCOM 2026 |
| 밀도 추가 증가 예상 | **~70%**가 12–36개월 내 밀도 추가 증가 예상 | AFCOM 2026 |

**출처:**
- [Data Center Knowledge: AFCOM 2026 랙 밀도 급등](https://www.datacenterknowledge.com/data-center-construction/afcom-rack-density-and-build-outs-surge-as-ai-overhauls-data-center-design)
- [AFCOM: The Data Center Density Dilemma](https://afcom.com/news/720658/The-Data-Center-Density-Dilemma.htm)
- [JetCool: 파워 밀도 트렌드와 액체냉각 전환](https://jetcool.com/post/how-power-density-is-changing-in-data-centers/)

---

## D-4. 액체냉각 시장

### D-4-1. 시장 규모 전망

| 조사기관 | 2025/2026 | 2033/2035 | CAGR |
|---------|----------|----------|------|
| GM Insights | $6B (2026) | $27.1B (2035) | **18.2%** |
| Precedence Research | — | $25.80B (2035) | — |
| MarketsandMarkets | $8.17B (2026) | $27.65B (2033) | — |
| 액침냉각 단독 (MarkWide) | $685.4M (2026) | $4,997M (2035) | **24.7%** |
| 액침냉각 CAGR (일부 추정) | — | — | **32.4%** (가장 빠른 세그먼트) |

### D-4-2. 주요 M&A — 업계 재편 가속

| 거래 | 규모 | 날짜 | 의미 |
|------|------|------|------|
| **Eaton → Boyd Thermal 인수** | **$9.55B** | 2026.03 | 액체냉각 매출 $1.5B 즉시 추가. DC 전력+냉각 원스톱 |
| **Schneider → Motivair 인수** | **$850M** (75% 지분) | 2025.02 | DLC·침지냉각 풀 포트폴리오. DC 매출 24% |
| **Trane → LiquidStack 인수** | 미공개 | 2026.03 | DTC + 침지냉각 포트폴리오 |
| **Ecolab → CoolIT Systems 인수** | 미공개 | 2026.03 | AI DC용 유체관리+냉각 원스톱 |

- **2026년 M&A 빅뱅**: 3월에만 3건의 주요 냉각 M&A. 업계 통합 급속 진행

### D-4-3. 3M 철수와 대체 공급사

- **3M 냉각유체(Fluorinert·Novec)**: 2025년 말 생산 중단 발표 → 시장 공급 공백
- **대체 공급사 기회**: SK엔무브(PAO 기반 액침유), GS칼텍스, Solvay, Chemours
- 냉각유체 표준 미확립 상태 → 선점 업체에 장기 계약 기회

**출처:**
- [GM Insights: DC 액체냉각 시장 $27.1B by 2035](https://www.gminsights.com/industry-analysis/data-center-liquid-cooling-market)
- [Precedence Research: DC 액체냉각 $25.80B](https://www.precedenceresearch.com/data-center-liquid-cooling-market)
- [Manufacturing Dive: Eaton의 DC 집중 세그먼트 및 Boyd 인수](https://www.manufacturingdive.com/news/eaton-ai-data-center-focused-segment-angie-mcmillin-liquid-cooling-boyd/815896/)
- [Schneider Electric + Motivair 액체냉각 포트폴리오](https://www.arcweb.com/blog/schneider-electric-motivair-unveil-end-end-liquid-cooling-portfolio-ai-hpc-data-centers)
- [DCD: 2025년 데이터센터 냉각 동향](https://www.datacenterdynamics.com/en/analysis/chilling-out-in-2025-a-year-in-data-center-cooling/)

---

## D-5. Bloom Energy와 자가발전(BTM)

### D-5-1. Bloom Energy 비즈니스 현황 (2026)

| 지표 | 수치 | 출처 |
|------|------|------|
| 총 백로그 | **~$20B** | Bloom Energy |
| 90일 내 수주 (2026 초) | **$7.65B** (DC 관련) | EnkiAI |
| FY2026 매출 가이던스 | **$3.4–3.8B** | Bloom Energy |
| Q1 2026 매출 성장 | **+130% YoY** | Bloom Energy |
| 파이프라인 | **4 GW** (+267% QoQ) | Bloom Energy |
| Oracle 수주 | **2.8 GW** 연료전지 — 대규모 단일 계약 | TradingKey |
| Centrica 파트너십 | 400 MW | EnkiAI |

### D-5-2. SOFC 기술 특성

| 비교 항목 | SOFC (Bloom) | 가스터빈 (GEV 등) | 비고 |
|----------|-------------|----------------|------|
| 전기 효율 | **60–65%** (수소 기준) | 30–38% (단순 사이클) | SOFC가 소형 규모에서 압도 |
| 자본 비용 | **$3,000–6,000/kW** | $400–800/kW | 가스터빈이 대용량에서 유리 |
| 적정 규모 | **1–10 MW** (소형 분산) | 10 MW+ (대형 집중) | 용도별 보완 관계 |
| 배포 기간 | **1년 미만** | 5–7년 (주문~설치) | SOFC의 최대 경쟁 우위 |
| 소음·진동 | 없음 (전기화학 반응) | 높음 | DC 인근 설치 유리 |
| 800V DC 호환 | 네이티브 DC 출력 → 800V DC 아키텍처 직결 | AC 출력 → 변환 필요 | Bloom의 DC 전환 수혜 포인트 |

- **"시간 차익(Time Arbitrage)"**: 그리드 연결 5–7년, 가스터빈 주문 5–7년 대기 vs SOFC 1년 미만 배포
- **TRL 8–9**: 상업용 검증 완료 단계. 미션 크리티컬 베이스로드 전원으로 은행 파이낸싱 가능
- **DC 아키텍처 시너지**: SOFC가 본질적으로 DC 발전 → 800V DC 버스에 직결 시 변환 손실 최소화

### D-5-3. 자가발전(BTM) 트렌드

| 지표 | 수치 | 출처 |
|------|------|------|
| 현재 온라인 BTM 용량 | ~2 GW (4개 프로젝트) | Build.inc |
| 2026 말 BTM 전망 | 2.8–3.2 GW | Build.inc |
| 계획 중 온사이트 가스 발전 | **100 GW** | BNEF / Latitude Media |
| BTM 탐색 개발사 비율 | **56%** (2026 Foley Survey) | datacenterHawk |
| 온사이트 전력 전략 채택률 | **61–73%** of operators | Bloom Energy 2026 |
| 오프그리드 DC 비중 전망 | **1/3** by 2030 | Bloom Energy 2026 |

**출처:**
- [EnkiAI: Bloom Energy 2026 $7.65B 수주](https://enkiai.com/fuel-cells/bloom-energy-fuel-cell-2026-7-65b-in-90-day-pacts/)
- [EnkiAI: Bloom Energy DC 매출 $3.6B](https://enkiai.com/solid-oxide-fuel-cells/bloom-energy-sofc-data-centers/)
- [TradingKey: Oracle 2.8GW 연료전지 수주 분석](https://www.tradingkey.com/analysis/stocks/us-stocks/261779571-bloom-energy-oracle-fuel-cell-ai-datacenter-sofc-power-order-valuation-tradingkey)
- [Green Gas Turbines: 가스터빈 vs 연료전지 비교](https://www.greengasturbines.com/blog/gas-turbines-vs-fuel-cells-industrial-decarbonization)

---

## D-6. 인퍼런스 전환의 의미

### D-6-1. 학습 vs 추론 비중 변화

| 지표 | 수치 | 출처 |
|------|------|------|
| 인퍼런스 컴퓨트 비중 (2023) | ~1/3 (학습 중심) | McKinsey |
| 인퍼런스 컴퓨트 비중 (2025) | **50%+** | Bloom Energy Mid-Year Jun'26 |
| 인퍼런스 컴퓨트 비중 (2026) | **~2/3** | McKinsey / Introl |
| 인퍼런스 IaaS 지출 비중 (2026) | **55%** (Gartner) | Gartner |
| 인퍼런스 IaaS 지출 비중 (2029) | **65%+** (Gartner) | Gartner |

### D-6-2. 전력 소비 패턴 차이

| 항목 | 학습(Training) | 추론(Inference) | 투자 시사점 |
|------|--------------|----------------|-----------|
| 랙 당 전력 | **40–140 kW+** (GPU 클러스터) | **10–30 kW** (일반적) | 냉각 방식 다양화 |
| 전력 패턴 | 집중 burst (학습 기간) | **상시·지속적** (24/7) | 기저부하 전력 수요 증가 |
| 냉각 요구 | 직접액체냉각 필수 | 고급 공냉~직접액체냉각 | 공냉 수명 연장 가능 |
| 전력 인프라 | 초단기 피크 대비 | **베이스로드 안정 전력** 요구 | 연료전지·원전 PPA 수요 증가 |
| 전력 성장 전망 | 62.2 GW (2030) | **93.3 GW (2030)** (CAGR 35%) | 추론이 더 빠르게 성장 |

- **핵심 인사이트**: 인퍼런스는 학습 대비 랙당 전력은 낮지만 **상시 가동** 특성으로 베이스로드 전력 수요를 구조적으로 증가시킨다. 총 전력 수요 측면에서 인퍼런스 GW 성장(35% CAGR)이 학습(22% CAGR)을 추월
- **배전 인프라 수요**: 상시 가동 추론 워크로드가 증가할수록 안정적 전력 공급 인프라(변압기, UPS, 연료전지) 수요가 구조적으로 증가

**출처:**
- [McKinsey: AI 워크로드의 미래](https://www.mckinsey.com/featured-insights/week-in-charts/the-future-of-ai-workloads)
- [Introl: AI 추론 vs 학습 인프라 경제학](https://introl.com/blog/ai-inference-vs-training-infrastructure-economics-diverging)
- [Deloitte: AI 다음 단계의 컴퓨트 수요](https://www.deloitte.com/us/en/insights/industry/technology/technology-media-and-telecom-predictions/2026/compute-power-ai.html)
- [Gartner: 추론 IaaS 지출 55% 전망](https://www.gartner.com/en/newsroom/press-releases/2025-11-17-gartner-says-electricity-demand-for-data-centers-to-grow-16-percent-in-2025-and-double-by-2030)

---

## D-7. 글로벌 인프라 기업 실적 (Q1 2026)

| 기업 | Q1 2026 매출 | 성장률 | DC 관련 하이라이트 |
|------|------------|--------|-----------------|
| **Vertiv** | $2,650M | +30% YoY (미주 +44%) | 백로그 $12.45B (+81% YoY). Adj OPM 20.8% (+430bps). FY26 가이던스 $13.25–13.75B (+30%). 800V DC 에코시스템 H2 2026 출시 예정 |
| **Eaton** | $7,451M | +10% organic (EA +20%) | DC 수주 +240%, DC 매출 +50% YoY. Boyd Thermal $9.55B 인수 완료. DC = 매출의 21% |
| **Schneider** | €9.8B ($10,600M) | +11.2% organic | DC = 매출의 24%, DC/네트워크 = 주문의 ~30%. Motivair $850M 인수. FY26 +7–10% 가이던스 |

---

## D-8. 테마 D 투자 시사점

### 밸류체인별 수혜 강도

```
800V DC 아키텍처 도입 → SiC/GaN 전력반도체 수요 증가 (2026~2028)
                      → Vertiv 800V DC 제품 매출 (H2 2026~)
                      → 기존 UPS·PDU 교체 수요 (전환 비용)

랙 밀도 폭발 (27kW→130kW) → 액체냉각 수요 급증 (CAGR 18~32%)
                           → M&A로 업계 통합 (Eaton/Schneider/Trane)
                           → 냉각유체 공급사 (SK엔무브, GS칼텍스)

인퍼런스 전환 → 베이스로드 전력 수요 지속
             → Bloom Energy SOFC 수요 (1년 내 배포 장점)
             → 연료전지 > 가스터빈 (소형·분산·즉시 배포 우위)
```

### 종목별 평가

| 종목 | 수혜 포인트 | 리스크 |
|------|-----------|--------|
| **Vertiv** | 800V DC 에코시스템 기본 파트너, 전력+냉각 원스톱, 백로그 $12.45B | Forward P/E 49x 고평가 |
| **Eaton** | Boyd $9.55B 인수로 냉각 강화, DC 수주 +240% | 인수 통합 리스크, 높은 인수 프리미엄 |
| **Schneider** | DC 매출 24%, Motivair 인수, 마진 개선 지속 | 유럽 거버넌스 리스크 |
| **Bloom Energy** | BTM 수요 + 800V DC 네이티브 + 백로그 $20B | 고객 집중 (하이퍼스케일러 의존), 희석, 주가 변동성 |
| **Infineon** | NVIDIA MGX 합류, 800V DC용 SiC/GaN, PSS 부문 +67% | EV 수요 둔화가 SiC 사업 일부 상쇄 |
| **Wolfspeed** | 10kV SiC 세계 최초, DC 매출 +50% QoQ | 재무 취약 (적자·부채), Mohawk Valley 수율 리스크 |
| **SK엔무브** | 3M 철수로 액침냉각유체 공백 수혜 | 표준 미확립, 경쟁 심화 |

---

## D-9. 테마 D 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| Vertiv 분기 수주 및 백로그 | 분기 | 백로그 성장 둔화 시 수요 사이클 피크 신호 |
| AFCOM 연간 랙 밀도 조사 | 연간 | 27kW → 50kW+ 전환 속도 (액체냉각 수요 가속화) |
| NVIDIA Rubin Ultra 출하 시기 | 반기 | 1MW/rack 양산이 800V DC 도입 촉매 |
| Vertiv 800V DC 제품 실제 수주 | 분기 | H2 2026 출시 후 첫 대형 수주 = 전환 가속 신호 |
| Bloom Energy 분기 매출 인식 | 분기 | 백로그 $20B의 실제 전환율 추적 |
| 인퍼런스 비중 (Gartner 반기) | 반기 | 65%+ 도달 시 베이스로드 전력 수요 구조 변화 확인 |
| 액침냉각 채택률 (AFCOM) | 연간 | 10% → 20%+ 전환 시 냉각유체 공급사 수혜 급증 |
| 3M 대체 냉각유체 표준 채택 | 상시 | IEEE/ASHRAE 표준 제정 시 시장 개화 |
| SiC 시장 점유율 변화 | 반기 | STMicro 32.6% → Infineon 추격 속도 |

---

## 테마 C+D 통합 — 투자 프레임워크 업데이트

### 병목 지도 재확인 (2026.06 기준)

| 병목 구간 | 심각도 | 2026 업데이트 |
|---------|--------|-------------|
| 초고압 변압기 | ★★★★★ | Q1 수주 역대 최대 갱신. 가격 상승 지속 전망 |
| 계통연계 큐 | ★★★★★ | 2,600 GW 대기, 철회율 80%. BTM 전환 가속 |
| NIMBY 모라토리엄 | ★★★★☆ | Q1 $130B 피해 (역대 최대). 뉴욕 법안 통과 |
| 800V DC 표준화 | ★★★★☆ | Vertiv H2 2026, NVIDIA 2027. 파일럿→본격 전환 |
| 액체냉각 전환 | ★★★☆☆ | 36% 도입(2026). 3M 철수로 유체 공급 공백 |
| HVDC 기술·인증 | ★★★☆☆ | Grain Belt 착공, 리드타임 3–5년 |

### 최고 비대칭 기회

1. **HD현대일렉트릭**: 765kV 기술 해자 + 앨라배마 CAPA 2027 증설. 상방: 공급자 우위 연장. 하방: 이미 높은 밸류
2. **Bloom Energy**: 베이스로드 BTM 수요 + 800V DC 네이티브 + 90일 $7.65B 수주. 상방: 백로그 $20B 매출 전환. 하방: 고객 집중·희석
3. **LS일렉트릭**: DC 솔루션 + 초고압변압기 이중 수혜. 상방: 테마 C+D 동시 수혜. 하방: OPM 낮음
4. **SK엔무브**: 3M 공백 + 액침냉각 표준 확립 시 폭발. 상방: 독점적 시장 선점. 하방: 표준 확립 타이밍 불확실

---

## 출처 목록

### 기관/시장 조사
- [Wood Mackenzie: 변압기 공급 부족](https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/)
- [LBNL Queued Up 2025](https://emp.lbl.gov/publications/queued-2025-edition-characteristics)
- [BloombergNEF: 글로벌 그리드 투자 $470B](https://about.bnef.com/insights/clean-energy/global-energy/global-grid-investment-could-top-470-billion-for-the-first-time-in-2025-bloombergnef/)
- [Precedence Research: AI DC HVDC 시장](https://www.precedenceresearch.com/ai-data-center-hvdc-power-supply-system-market)
- [GM Insights: DC 액체냉각 시장](https://www.gminsights.com/industry-analysis/data-center-liquid-cooling-market)
- [Fortune Business Insights: SiC 디바이스 시장](https://www.fortunebusinessinsights.com/silicon-carbide-sic-devices-market-112103)
- [AFCOM 2026 State of the Data Center](https://afcom.com/news/720658/The-Data-Center-Density-Dilemma.htm)
- [Bloom Energy 2026 Mid-Year Pulse Report](https://enkiai.com/solid-oxide-fuel-cells/bloom-energy-sofc-data-centers/)

### 기술/산업 분석
- [NVIDIA Technical Blog: 800V DC 아키텍처](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [Data Centre Magazine: Vertiv·NVIDIA 800 VDC](https://datacentremagazine.com/news/vertiv-and-nvidia-advance-800-vdc-for-ai-data-centres)
- [Data Center Dynamics: NVIDIA Rubin 1MW 랙](https://www.datacenterdynamics.com/en/news/nvidia-prepares-data-center-industry-for-1mw-racks-and-800-volt-dc-power-architectures/)
- [RMI: 계통연계 큐와 AI DC](https://rmi.org/interconnection-reform-ai-data-centers-generator-queues/)
- [Data Center Knowledge: AFCOM 랙 밀도 분석](https://www.datacenterknowledge.com/data-center-construction/afcom-rack-density-and-build-outs-surge-as-ai-overhauls-data-center-design)

### 기업 공시/뉴스
- [HD현대일렉트릭 Q1 2026 실적](https://www.newspim.com/news/view/20260428000851)
- [LS일렉트릭 Q1 2026 실적](https://news.nate.com/view/20260421n19556)
- [대한전선 Q1 2026 실적](https://www.etoday.co.kr/news/view/2580441)
- [Grain Belt Express 시공계약 발표](https://grainbeltexpress.com/grain-belt-express-awards-1-7b-to-u-s-contractors-quanta-and-kiewit-to-build-largest-transmission-line-in-u-s-history/)
- [Eaton Boyd Thermal 인수](https://www.manufacturingdive.com/news/eaton-ai-data-center-focused-segment-angie-mcmillin-liquid-cooling-boyd/815896/)
- [뉴욕 모라토리엄 법안 통과](https://www.nysenate.gov/newsroom/press-releases/2026/kristen-gonzalez/ny-state-senator-kristen-gonzalez-passes-data-center)
- [Data Center Watch: $64B 프로젝트 차단](https://www.datacenterwatch.org/report)
- [McKinsey: AI 워크로드 미래](https://www.mckinsey.com/featured-insights/week-in-charts/the-future-of-ai-workloads)
