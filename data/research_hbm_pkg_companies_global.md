# HBM·패키징 리서치 — 글로벌 기업 심화 분석 (비한국)

> 목적: HBM/패키징 밸류체인 글로벌 핵심 기업 12개사의 재무·기술·밸류에이션 심화 분석
> 작성일: 2026-06-22
> 최종 갱신: 2026-06-22
> 커버리지: 대만(TSMC, ASE/SPIL, Unimicron), 미국(Micron, Amkor, Applied Materials, Lam Research), 일본(Advantest, Disco, Ibiden, Ajinomoto), 네덜란드(BESI)
> 상태: 초안

---

## 1. 개요 — 글로벌 HBM/패키징 밸류체인 기업군

본 문서는 `research_hbm_pkg_part12_overview.md`에서 정리한 6단계 밸류체인 맵의 **비한국 글로벌 핵심 기업 12개사**에 대해 재무 실적, 기술 로드맵, 밸류에이션을 심화 분석한다. 한국 기업(SK하이닉스, 한미반도체, HPSP, 리노공업, 삼성전자, 삼성전기)은 별도 파일(`research_hbm_pkg_companies_kr.md`)에서 다룬다.

**밸류체인 내 커버리지 맵**:

```
STAGE 01: HBM 웨이퍼        → Micron (미국)
STAGE 02: 범핑              → ASE/SPIL (대만), Amkor (미국)
STAGE 03: 첨단 패키징        → TSMC (대만), ASE/SPIL, Amkor
STAGE 04: 본딩              → BESI (네덜란드)
STAGE 05: 테스트            → Advantest (일본)
STAGE 06: 기판·소재          → Unimicron (대만), Ibiden (일본), Ajinomoto (일본)
크로스 스테이지 장비          → Applied Materials (미국), Lam Research (미국)
다이싱/그라인딩 (전처리)      → Disco (일본)
```

---

## 2. 대만 기업 (Taiwan)

### 2.1 TSMC — 첨단 패키징의 절대 군주

#### 기본 실적

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **~$35B** (+40.6% YoY) | Manufacturing Dive |
| FY26 매출 성장 가이던스 | **+30%+ YoY** (USD 기준) | TSMC 어닝콜 |
| Q1'26 GM | ~59% | TSMC 6-K |
| FY26 CAPEX | **$52~56B** (70~80% 첨단 공정, 10~20% 첨단 패키징) | TSMC 어닝콜 |

#### 첨단 패키징 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| 첨단 패키징 매출 비중 | ~8% (2025) → **10%+ (2026E)** | TSMC |
| 첨단 패키징 매출 추정 | **~$14~15B** (FY26E, 전체 ~$140B 기준 10%) | 추정 |
| CoWoS CAPA (월) | 35K WPM (2024) → **120~130K WPM (2026 말)** → 170K WPM (2027) | TrendForce |
| OSAT 포함 총 CoWoS CAPA | ~200K WPM (TSMC 120~130K, 일부 추정 140K + OSAT 50~60K) | GuruFocus, TrendForce |
| CoWoS 수급갭 | 20% (2026 초) → **10% (2026 말)** | TrendForce |
| CoWoS 리드타임 | **52~78주** | 업계 |
| CoWoS Wafer ASP | **7nm 웨이퍼 수준** (~$17,000~20,000) | TrendForce |
| NVIDIA CoWoS 예약 | **50%+** (2026 할당) | SiliconAnalysts |
| 외주 물량 | 24~27만장/년 (Amkor 18~19만 + SPIL 6~8만) | TrendForce |

#### CoPoS (패널 레벨 패키징) 로드맵

| 일정 | 내용 | 출처 |
|------|------|------|
| 2026.06 | CoPoS 파일럿 라인 완공 (Visionchip 자회사) | TrendForce |
| 2026 H2 | 장비·소재 벤더 검증 (글로벌 vs 로컬 이중 평가) | TrendForce |
| 2027 | 파일럿 생산, 파트너 요건 충족 목표 | 업계 |
| 2028 H2 | **양산 개시** 목표 | TrendForce, All-About-Industries |
| 2028~2029 | 본격 램프업 | TrendForce |
| 2030+ | 글라스코어 기판 상용화 단계 | WCCFTech |

- **CoPoS 핵심**: 310 x 310mm 패널 → CoWoS 대비 **웨이퍼 활용율 90%+**, 비용 30% 절감 목표
- CoWoS-L 대체가 아닌 **보완·확장** — 초대형 AI 가속기(Rubin Ultra급)에 적용
- TSMC가 글로벌 장비사(AMAT, TEL 등) vs 대만 로컬 업체 **이중 평가** 진행 → 장비사 경합 치열

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$1.1T** | Yahoo Finance |
| Trailing P/E | **33.1x** | StockAnalysis |
| Forward P/E | **23.1~29.6x** | GuruFocus, TipRanks |
| EV/EBITDA | **18.1~21.4x** | Multiples.vc |
| P/B | **~9.5x** | MarketScreener |

- **밸류에이션 코멘트**: Forward P/E 23~30x는 글로벌 파운드리 독점 프리미엄 반영. 첨단 패키징이 CoWoS ASP 7nm급으로 상승하며 **고마진 사업부로 전환 중** — 향후 전체 GM 개선 동인
- **리스크**: 대만 해협 지정학, 인텔 EMIB 경쟁(현실적 위협 제한적), 미국 Arizona 팹 코스트 프리미엄

---

### 2.2 ASE/SPIL — OSAT 세계 1위, TSMC 첨단 패키징 외주 핵심

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| ASE Q1'26 매출 | **NT$173.7B** (+17.2% YoY, QoQ -2%) | Investing.com |
| ASE Q1'26 순이익 | NT$14.15B (+87% YoY), **EPS NT$3.24 (사상 최대)** | Investing.com |
| SPIL 1~5월 누적 매출 | **NT$298.9B** (+19.9% YoY, 동기간 사상 최대) | TrendForce |
| ATM 부문 비중 | 연결 매출의 ~65%, 영업이익의 **90%+** | BigGo Finance |

#### LEAP (첨단 패키징) 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| 2025 LEAP 매출 | ~$1.6B | ASE IR |
| 2026E LEAP 매출 가이던스 | **$3.5B+** (당초 $3.2B에서 +10% 상향) | AlphaPilot, BigGo Finance |
| LEAP YoY 성장률 | **+118%** | BigGo Finance |
| 2026 CAPEX | **$8.5B** (당초 $7B에서 2차 상향, +20%+) | BigGo Finance |
| SPIL 신규 공장 인수 | NT$2.8B — TSMC 첨단 패키징 overflow 대응 | TrendForce |
| CoWoS 외주 물량 (SPIL) | **6~8만장/년** | TrendForce |

- **전략 포지션**: TSMC CoWoS 외주의 핵심 파트너. TSMC가 CAPA 120~130K WPM까지 확대해도 수요 대비 10% 부족 → ASE/SPIL은 이 갭의 직접 수혜
- **SPIL 공장 인수 가속**: 2026.06 NT$2.8B 공장 인수 — TSMC 첨단 패키징 CAPA 부족분을 흡수하기 위한 선제적 투자
- **LEAP $3.5B+**: 2025년 $1.6B 대비 **2배 이상 성장** — AI 패키징 수요 폭증의 직접 증거

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$14.3B** (USD) | Simply Wall St |
| Trailing P/E | **42.8~54.8x** | MacroTrends, Simply Wall St |
| Forward P/E | **27.7~35.2x** | GuruFocus, StockAnalysis |
| 주가 YTD | +18%, 12개월 +92% | Yahoo Finance |
| EPS 성장 전망 | +33.9%/년 | Simply Wall St |

- **밸류에이션 코멘트**: Forward P/E 28~35x는 OSAT 업종 역사적 평균(15~20x) 대비 높지만, LEAP 118% 성장과 AI 패키징 구조적 수혜를 반영. TSMC 외주 확대가 지속되는 한 프리미엄 정당화 가능

---

### 2.3 Unimicron — ABF 기판 세계 1위

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| FY2025 매출 | **NT$131.2B** (~$4.2B, +13.7% YoY) | CompaniesMarketCap |
| 2026E 목표 | **사상 최대 매출** (2022 피크 초과) | DIGITIMES |
| 2026E EPS 전망 | **NT$20.34** (전년 NT$8.98 대비 +126%) | 애널리스트 컨센서스 |
| 2026 CAPEX | **NT$25B+** (~$790M, 전년 대비 +20%+) | DIGITIMES |

#### ABF 기판 포지션 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| ABF 기판 글로벌 M/S | **~22%** (1위) | QY Research |
| NVIDIA GPU용 ABF M/S | **~35%** | DIGITIMES |
| ASIC(Google TPU, AWS Trainium) ABF M/S | **50%+** | DIGITIMES |
| 2026 AI 매출 비중 | **~60%** (2025년 40%에서 상승) | DIGITIMES |
| ABF CAPA 변화 | **+40% 확대** (BT 기판 -15% 구조조정) | DIGITIMES |
| 가격 동향 | ABF 기판 **추가 가격 인상** (2026.03~) | DIGITIMES, X(Jukan) |
| 고객 LTA | 장기 계약(LTA) 체결 러시 — 내년 공급 부족 우려 | DIGITIMES |

- **핵심 드라이버**: AI 가속기(GPU+ASIC) 기판 수요 폭증. NVIDIA용 35%, ASIC용 50%+ → AI 매출 비중 60%
- **공급 병목**: 유리섬유 부족(2026) + ABF 필름 부족 → 가격 인상 + 고객사 LTA 체결 러시
- BofA 투자의견 Buy 상향, 2027 영업이익 전망 +27% 상향
- Bernstein: 대만 AI 노출도 최상위 — TSMC와 함께 Top pick

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~NT$430B** (~$13.5B) | CompaniesMarketCap |
| Trailing P/E | **44.9x** | CompaniesMarketCap |
| Forward P/E | ~**22x** (2026E EPS 기준) | 추정 |
| P/B | ~5.2x | MarketScreener |
| 주가 | TWD 902 (목표가 TWD 926) | 애널리스트 컨센서스 |

- **밸류에이션 코멘트**: EPS가 2025→2026 +126% 급증 → Forward P/E ~22x로 급락. ABF 기판 1위 + AI 60% 비중 + CAPA 40% 확대 → **밸류에이션 대비 성장률 매력적**

---

## 3. 미국 기업 (United States)

### 3.1 Micron — HBM 3위, Cloud BU 고마진 성장

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| Q2 FY26 매출 | **$23.86B** | SEC 8-K |
| Q2 FY26 순이익 | $13.79B (**EPS $12.07**) | Micron IR |
| Q3 FY26 EPS 가이던스 | **$19.15** (사상 최대, +$0.40) | Micron IR |
| Cloud BU 매출 | **$7,749M** | SEC 10-Q |
| Cloud BU GM | **74%** | SEC 10-Q |
| FY26 연간 매출 컨센서스 | **~$76B** (FY25 대비 2배) | Seeking Alpha |

#### HBM 전략 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| HBM 글로벌 M/S | **~21%** → 25% 목표 | 업계 |
| 2026 HBM 공급 | **전량 고정가 계약 매진** (HBM3E + HBM4) | Tickeron, Seeking Alpha |
| HBM4 양산 | **2026 H2 양산 개시** (NVIDIA Vera Rubin용) | Micron IR |
| HBM4 대역폭 | **2.8+ TB/s** | Micron IR |
| HBM4 전력효율 | HBM3E 대비 **20%+ 개선** | Micron IR |
| HBM4 수율 | HBM3E 12-Hi 대비 **빠른 램프** 기대 | Micron 어닝콜 |
| 차별화 | **30% 저전력** HBM4 스택 | Tech-Insider |

- **Cloud BU GM 74%**: HBM+서버 DRAM의 믹스 개선 효과. 회사 전체 GM을 끌어올리는 핵심 엔진
- **HBM4 조기 양산**: SK하이닉스와 함께 2026 양산 개시. 30% 저전력 차별화로 데이터센터 효율 중시 고객 공략
- **리스크**: M/S 3위 고착 가능성, SK하이닉스 대비 NVIDIA 종속도 낮음

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$250B+** | 추정 (주가 ~$950~1,050 x 발행주식) |
| Forward P/E (FY27) | **~5.7~10x** | Seeking Alpha, MarketDigests |
| P/B | ~4.5x | 추정 |

- **밸류에이션 코멘트**: Forward P/E 5.7~10x는 반도체 업종 평균 대비 **극단적 저평가**로 보이나, 메모리 사이클 주식 특성상 **PER 하락이 피크 신호**일 가능성. Cloud BU 74% GM이 지속 가능한지가 핵심 변수
- 어닝 모멘텀: Q3 FY26 EPS $19.15 가이던스 → 연율화 시 PER 추가 하락

---

### 3.2 Amkor Technology — CoWoS 외주의 핵심, TSMC 10년 파트너

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **$1,685M** (+27% YoY, Q1 사상 최대) | SEC 8-K |
| Q1'26 첨단 패키징 매출 | **$1.4B** (전년 $1.1B → +27%) | Amkor IR |
| Q1'26 GM | 14.2% | SEC 8-K |
| Q1'26 영업이익 | $100M | SEC 8-K |
| Q2'26 가이던스 | **$1.75~1.85B** | Amkor IR |
| 2026 CAPEX | **$2.5~3.0B** | Amkor Investor Day |
| 2030 목표 | 매출 **$11B+**, GM **22%+**, EPS **$5+** | Amkor CFO (Investor Day) |

#### TSMC 파트너십 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| 파트너십 | **10년 장기 계약** (2026.06.16 발표) | BusinessWire, Focus Taiwan |
| 대상 | Arizona 첨단 패키징 + 테스트 서비스 | BusinessWire |
| Arizona 투자 | **~$2B**, 고용 ~2,000명 | Amkor IR |
| CoWoS 외주 배분 | **~80K WPM** (TSMC 120K 대비) | 36Kr |

- **10년 파트너십**: 2026.06.16 TSMC와 10년 장기 첨단 패키징 파트너십 발표 → 주가 52주 신고가 $96.68 돌파
- **Arizona 허브**: TSMC Arizona 팹과 연계, 미국 내 첨단 패키징 공급망 구축. 미국 반도체 자국 내 완결형 생태계의 핵심 축
- **마진 딜레마**: GM 14.2%로 OSAT 중 낮은 편. Arizona 투자 초기 비용 → 2027 OPM 1~2%p 희석 전망

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$14.4B** (주가 ~$82~97) | MacroTrends |
| Trailing P/E | **38.2x** | Simply Wall St |
| NTM EV/EBITDA | **14.0x** | Simply Wall St |
| 2030 목표 EPS | $5+ (현재 ~$1.50) | Amkor Investor Day |

- **밸류에이션 코멘트**: NTM EV/EBITDA 14x는 OSAT 평균 대비 프리미엄이나, TSMC 10년 파트너십 + 미국 AI 패키징 허브 프리미엄 반영. 2030 EPS $5 달성 시 현 주가 대비 P/E 급격 하락

---

### 3.3 Applied Materials — 패키징 장비 최강자

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| Q2 FY26 매출 | **$7.91B** (사상 최대, +11% YoY, +13% QoQ) | SEC 8-K, StockTitan |
| Q2 FY26 Non-GAAP EPS | **$2.86** (+20% YoY, 컨센서스 $2.68 대비 +6.7% beat) | Investing.com |
| Q2 FY26 GAAP EPS | **$3.51** | SEC 8-K |
| Q2 FY26 GM | **50%** | TIKR |
| Q3 FY26 가이던스 | 매출 **$8.95B** (+$500M), EPS **$3.36** (+$0.20) | AMAT IR |

#### 패키징 장비 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| 2026 패키징 매출 성장 | **+50%+** (CY2026) | AMAT 어닝콜 |
| Kinex 시스템 | 업계 최초 **완전 통합형 Die-to-Wafer 하이브리드 본딩 시스템** | AMAT |
| Kinex 공동 개발 | **BESI와 파트너십** (본딩 정밀도 <10nm) | BALD Engineering |
| NEXX 인수 | ASMPT로부터 인수 — **패널 레벨 첨단 패키징 증착 장비** | AMAT IR |
| NEXX 용도 | 대면적 AI 가속기용 패키징 기술 강화 | AMAT IR |
| BESI 인수 경합 | Lam Research와 함께 **수십억 유로** 규모 입찰 | Tiger Brokers |

- **Kinex**: BESI와 공동 개발한 하이브리드 본딩 시스템. HVM(대량양산) 환경을 위해 설계 — 큐타임 제어, 시스템 청정도, 본딩 정밀도 통합
- **NEXX 인수**: 패널 레벨 패키징(CoPoS 등) 시대 대비. TSMC의 CoPoS 파일럿과 맞물려 장비 수요 선점
- **BESI 인수 시도**: Applied Materials가 BESI 최대 주주로 지분 확보 → 하이브리드 본딩 기술 내재화 의도. Morgan Stanley가 BESI 자문사로 선임

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$389B** | StockAnalysis |
| Trailing P/E | **46.1~55x** | MacroTrends, GuruFocus |
| Forward P/E | **33.5~50.3x** | GuruFocus |
| P/S | **16x+** (역사적 최고, 닷컴 버블 ~15x 초과) | GuruFocus |
| 주가 YTD | **+144%** | 업계 |

- **밸류에이션 코멘트**: P/S 16x+는 역사적 최고치. 패키징 장비 +50% 성장 + AI 반도체 수요 구조적 확대를 반영하나, **밸류에이션 부담 상당**. 닷컴 버블 수준 P/S → 단기 조정 리스크 존재

---

### 3.4 Lam Research — TSV/하이브리드 본딩 20년 베테랑

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| Q3 FY26 매출 | **$5.84B** (사상 최대, +24% YoY) | Simply Wall St |
| Q3 FY26 Adj. EPS | +41% YoY (4분기 연속 beat) | Simply Wall St |
| 주가 YTD | **+127.2%** | Yahoo Finance |
| 2026 패키징 매출 성장 | **+50%+** (CY2026) | Lam Research 어닝콜 |
| 2026 WFE 시장 전망 | **~$140B** (상향) | Lam Research 어닝콜 |

#### 첨단 패키징 포지션

| 분야 | 역할 | 비고 |
|------|------|------|
| TSV 식각 | **핵심 포지션** | HBM 다이 관통 비아, 실리콘 인터포저 |
| TGV (Through Glass Via) | 글라스 기판용 | 차세대 기판 대비 |
| RDL (재배선층) | 팬아웃 패키징 | CoWoS-L, InFO |
| 하이브리드 본딩 전처리 | 표면 활성화·세정 | BESI 본딩 전 공정 |
| 고종횡비 식각/증착 | 20년+ 경력 | 첨단 패키징 전공정 핵심 |

#### BESI 인수 경합

| 내용 | 상세 | 출처 |
|------|------|------|
| 인수 대상 | **BESI (BE Semiconductor)** | Reuters, Tiger Brokers |
| 경합 상대 | Applied Materials (BESI 최대 주주) | IndexBox |
| 인수 논의 | 2025 중반 시작 → 미-EU 지정학 이슈로 중단 → **2026 재개** | Digital Today |
| 전략적 의미 | TSV/식각 → 하이브리드 본딩 → 풀 패키징 장비 수직 통합 | Kavout |

- **전략 포지션**: AMAT과 함께 첨단 패키징 장비 양대 축. TSV/TGV 식각에서 압도적 포지션
- **BESI 인수 성공 시**: 식각(Lam) + 본딩(BESI) 통합 → 패키징 장비 풀라인업 완성. 패키징 매출 비중 급격 확대 기대
- **BESI 인수 불발 시**: 자체 하이브리드 본딩 기술 개발 필요 → 시간 소요

---

## 4. 일본 기업 (Japan)

### 4.1 Advantest — ATE의 "테스트계 ASML"

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| FY25 매출 (2026.03 결산) | **¥1.13T** (+44.8% YoY) | PitchBook |
| FY25 순이익 | **¥375.4B** (+132.9% YoY) | PitchBook |
| FY26E 매출 가이던스 | **¥1.42T** (~$9B, +26% YoY) | Advantest IR |
| FY26E 영업이익 | **¥627.5B** | Advantest IR |
| FY26E 순이익 | **¥465.5B** | Advantest IR |
| ATE 시장 규모 (CY2026) | **$12.5~13B** | Advantest |
| 테스트 유닛 생산 | 3,000대 → **5,000대** (2026 램프) | 업계 |
| ATE 리드타임 | **6개월+** | DIGITIMES |

#### HBM 테스트 수혜

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 ATE M/S | **~70%** | Apple Podcasts (업계 인용) |
| 메모리 테스트 M/S | **60~70%** | 업계 추정 |
| SoC 테스트 M/S | 35~45% | 업계 추정 |
| HBM 테스트 포지션 | **모든 HBM 모듈·패키지 GPU가 Advantest 장비 통과** | RCR Wireless |

- **구조적 수혜**: HBM 스택 8-Hi → 12-Hi → 16-Hi 증가 → 테스트 시간·복잡도 비례 증가 → ATE 수요 구조적 성장
- **경쟁 현황**: Teradyne(미국)가 2위이나 M/S 격차 압도적. 메모리 테스트에서는 사실상 독점
- 3,000대 → 5,000대 생산 램프: **+67% 증산** — 수요 초과 상태 방증

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **¥19.08T** (~$126~143B) | StockAnalysis |
| Trailing P/E | **125.9x** | CompaniesMarketCap |
| Forward P/E | ~**41x** (FY26E 순이익 기준) | 추정 |
| P/B | ~22x | 추정 |

- **밸류에이션 코멘트**: Trailing P/E 126x는 극도의 프리미엄. 그러나 FY26E 순이익 ¥465B 기준 Forward P/E ~41x로 급락. "테스트계 ASML" 포지션(M/S 70%, 대안 부재) + AI 반도체 전 칩 통과 → **구조적 독점 프리미엄** 정당화 여지. 단, 반도체 사이클 피크 시 P/E 수축 리스크

---

### 4.2 Disco Corporation — 다이싱/그라인딩의 절대 독점

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| TTM 매출 (2026.03) | **$2.9B** | PitchBook |
| Q1'26 매출 | **$838M** (+26.9% beat, QoQ +20%) | Meyka |
| Q1'26 EPS | **$2.49** (컨센서스 $2.39 대비 +4.2% beat) | Meyka |
| R&D 비중 | **33%** of 매출 | SemiAnalysis |
| 레이저 소 누적 출하 | **4,000대+** (2020 이후 3배) | 업계 |

#### HBM 수혜 분석

| 지표 | 수치 | 출처 |
|------|------|------|
| 정밀 다이싱·그라인딩 M/S | **70~80%** (사실상 독점) | SemiAnalysis |
| HBM 웨이퍼 극박화 | **30~50um** → Disco Taiko 그라인딩 필수 | SemiAnalysis |
| 스텔스 다이싱 | 레이저 기반 내부 가공 → 칩핑 제로, HBM 수율 핵심 | SemiAnalysis |
| 하이브리드 본딩 전처리 | 웨이퍼 표면 평탄화 → Disco 연마 장비 활용 | 업계 |

- **핵심 해자**: HBM 제조 시 DRAM 다이를 30~50um으로 극박화해야 하며, 이 공정은 Disco의 Taiko 그라인딩·스텔스 다이싱이 사실상 **유일한 솔루션**
- R&D 33%: 반도체 장비사 중 최고 수준 → 기술 해자 지속 강화
- HBM 스택 수 증가(12-Hi → 16-Hi) → 다이당 더 얇게 → Disco 장비 수요 증가

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **$48~55B** | PitchBook, Yahoo Finance |
| Trailing P/E | **64.3x** | Yahoo Finance |
| Forward P/E | **49.8x** | Yahoo Finance |
| Meyka AI 등급 | **B+** (견조한 펀더멘털, 밸류에이션 우려) | Meyka |

- **밸류에이션 코멘트**: Forward P/E 50x는 장비사 중 높은 편이나, M/S 70~80% 독점 + HBM 구조적 수혜 + R&D 33% 기술 해자로 프리미엄 정당화. 매출 $2.9B에 시총 $50B+ → 성장 기대가 상당 부분 반영

---

### 4.3 Ibiden — ABF 기판 2위, AI 서버 핵심 공급자

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| TTM 매출 (2026.03) | **$2.76B** | PitchBook |
| FY25 EPS | **¥236.73** | PitchBook |
| 시가총액 | **~$32.4B** | PitchBook |

#### ¥500B 투자 계획 상세

| 항목 | 내용 | 출처 |
|------|------|------|
| 총 투자 규모 | **¥500B (~$3.2B)** (FY26~28, 3년간) | Ibiden IR, Kantenna |
| 목표 | AI 서버·HPC용 고성능 IC 패키지 기판 **CAPA 2.5배 확대** | Ibiden IR |
| 1차 투자 | 가와마 공장(Cell 6) **¥220B (~$1.4B)** | DIGITIMES |
| 1차 양산 개시 | **FY2027** | DIGITIMES |
| 위치 | 오가키시, 기후현 | Ibiden IR |
| 주요 고객 | Intel, NVIDIA | 업계 |

- **$3.2B 투자의 의미**: 회사 역사상 최대 투자. TTM 매출 $2.76B의 **116%**에 해당 → AI 확신의 극단적 신호
- **ABF 필름 확보 리스크**: Ibiden은 "현재 가이던스 분의 ABF 필름은 확보했으나, 업사이드 대응 분은 미확보" — Ajinomoto 의존도 노출
- ABF 기판 글로벌 2위: Unimicron(22%)에 이어 M/S ~18~20% 추정

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$32.4B** | PitchBook |
| Trailing P/E | **63.4x** | GuruFocus |
| Forward P/E | ~**45~50x** (FY27E 기준) | 추정 |
| P/B | ~5.8x | 추정 |

- **밸류에이션 코멘트**: P/E 63x는 기판 업종 역사적 평균 대비 높으나, ¥500B 투자로 CAPA 2.5배 확대 + AI 서버 수혜 구조적 성장을 선반영. FY27 양산 본격화 시 이익 급증 기대

---

### 4.4 Ajinomoto — ABF 필름 95% 독점, "식품회사의 반도체 지배"

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| FY25 영업이익 (2026.03) | **¥181.1B** (+13% YoY, 사상 최대) | TrendForce |
| 전자소재 부문 매출 | **¥100.7B** (+31% YoY, 전체의 6%) | TrendForce |
| 전자소재 부문 영업이익 | **¥54.6B** (+35% YoY, 전체의 **30%**) | TrendForce |
| ABF 필름 마진 | **50%+** | TrendForce |

#### ABF 필름 독점 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| ABF 필름 글로벌 M/S | **95%+** (사실상 독점) | BigGo Finance |
| 가격 인상 | **+30%** (Q3 2026 적용) | DIGITIMES, BigGo Finance |
| 가격 인상 근거 | AI칩 기판 레이어: 3+3 → 11+11 → **13+13** 진화 → ABF 소요량 **4배+ 증가** | BigGo Finance |
| 수급 상황 | **2026 H1부터 다시 부족(shortage)** 진입 | BigGo Finance |
| 신공장 용지 매입 | **¥1.2B** (기후현, **2032년 가동** 목표) | TrendForce |

- **밸류체인 최강의 은밀한 해자**: 95% 독점 + 50%+ 마진 + 30% 가격 인상 + shortage 재진입. **대체재가 사실상 없는** 구조
- AI칩 기판 레이어 수 진화가 핵심: 기존 3+3층(PC용) → AI 서버용 11+11 → 차세대 13+13층. 레이어당 ABF 필름 사용 → 소요량 기하급수 증가
- "식품회사가 반도체를 지배한다": Ajinomoto 전체 매출의 6%에 불과한 전자소재가 영업이익의 30%를 차지 → **숨겨진 캐시카우**
- 신공장 2032년 가동: 장기적 수요 확대에 대한 경영진의 확신, 그러나 **2026~2031 공급 타이트** 지속 의미

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~$31B** | CompaniesMarketCap |
| Trailing P/E | **41.8x** | CompaniesMarketCap |
| 전체 매출 대비 전자소재 | **6%** (but 영업이익 30%) | TrendForce |

- **밸류에이션 코멘트**: P/E 42x는 식품회사 치고 높지만, 실질적으로 **반도체 소재 독점 기업**의 밸류에이션. ABF 필름만 분리 평가 시 ¥54.6B 영업이익에 반도체 소재 멀티플(20~30x) 적용 → **¥1.1~1.6T 가치**. 전체 시총 대비 ABF 사업의 가치 비중이 과소평가되어 있을 가능성

---

## 5. 네덜란드 (Netherlands)

### 5.1 BESI — 하이브리드 본딩의 왕, M&A 경합의 중심

#### 실적 상세

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **€184.9M** (+28.3% YoY) | BESI IR |
| Q1'26 수주 | **€269.7M** (YoY 2배+, **사상 최대**) | BESI IR |
| Q1'26 수주 QoQ | +7.7% (Q4'25 대비) | BESI IR |
| Q2'26 가이던스 | **+30~40% QoQ** (€240~259M) | BESI IR |
| 장기 매출 목표 | **€1.7~2.2B** (상향) | BESI IR |
| 장기 OPM 목표 | **45~55%** (하한 상향) | BESI IR |

#### 하이브리드 본딩 심화

| 지표 | 수치 | 출처 |
|------|------|------|
| 2023 하이브리드 본딩 매출 | €36M | TipRanks |
| 2026E 하이브리드 본딩 매출 | **€476M** | TipRanks |
| 하이브리드 본딩 비중 (2026E) | 전체 매출의 **~1/3** | TipRanks |
| 하이브리드 본딩 성장 (3년) | **13.2배** (€36M → €476M) | 산출 |
| 본딩 정밀도 | **<10nm** | 업계 |
| 하이브리드 본더 고객 수 | **20개사** (확대 중) | Bits&Chips |
| 적용 분야 | 로직, 메모리, 포토닉스, 모바일 | BESI IR |

#### 수주 추이 (분기별)

| 분기 | 수주 (€M) | QoQ | 비고 |
|------|-----------|-----|------|
| Q1'25 | ~€130M | — | 기준 |
| Q2'25 | ~€165M | +27% | 하이브리드 본딩 확대 |
| Q3'25 | ~€210M | +27% | 연속 성장 |
| Q4'25 | **€250M** | +19% | 사상 최대 (당시) |
| **Q1'26** | **€269.7M** | +7.7% | **신기록 경신** |

- **수주 트렌드**: 5분기 연속 성장, Q1'26 €269.7M 사상 최대. 하이브리드 본더 유닛 수주 전분기 대비 **2배+ 급증**
- **고객 확대**: 20개사 → 로직(TSMC, 인텔), 메모리(SK, 삼성, 마이크론), 포토닉스, 모바일 전방위 채택 진행

#### M&A 경합 최신 상황

| 시점 | 내용 | 출처 |
|------|------|------|
| 2025 중반 | Applied Materials·Lam Research **수십억 유로** 규모 인수 논의 시작 | Reuters |
| 2025 H2 | Applied Materials, BESI **최대 주주**로 지분 확보 | Tiger Brokers |
| 2026 초 | 미-EU 지정학 긴장(그린란드 이슈)으로 **논의 중단** | Digital Today |
| 2026 H1 | **논의 재개** | IndexBox |
| 현재 | BESI, **Morgan Stanley를 자문사로 선임** — 인수 제안 검토 | Bits&Chips |
| BESI 입장 | **독립 경영 유지** 선호 표명 | BESI |

- **M&A 시나리오**: (1) AMAT 인수 → Kinex + BESI 기술 완전 통합, (2) Lam 인수 → TSV+본딩 풀라인업, (3) 독립 유지 → 하이브리드 본딩 독립 플레이어로 성장
- **M&A 프리미엄**: 현재 기업가치에 30~50% 프리미엄 가능성 (업계 추정)

#### 밸류에이션

| 지표 | 수치 | 출처 |
|------|------|------|
| 시가총액 | **~€15~18B** | StockAnalysis |
| Trailing P/E | **~55~65x** | 추정 (분기 실적 기준) |
| Forward P/E | ~**35~40x** (장기 목표 매출 기준) | 추정 |
| OPM 목표 | 45~55% | BESI IR |
| M&A 프리미엄 잠재력 | +30~50% | 업계 추정 |

- **밸류에이션 코멘트**: 하이브리드 본딩 €476M(2026E)는 시작에 불과. 2028년 HBM 공정의 36%가 하이브리드 본딩 전환 시 시장 규모 **~$2B**. BESI가 이 시장의 지배적 플레이어 → 장기 매출 €1.7~2.2B 목표의 핵심 동인. M&A 프리미엄까지 감안 시 추가 업사이드 가능

---

## 6. 크로스 밸류에이션 비교 테이블

### 6.1 전체 기업 비교

| 기업 | 국가 | 밸류체인 위치 | 시가총액 | Trailing P/E | Forward P/E | 핵심 M/S | AI/HBM 노출도 |
|------|------|-------------|---------|-------------|-------------|---------|-------------|
| **TSMC** | 🇹🇼 | 첨단 패키징 | ~$1.1T | 33.1x | 23~30x | CoWoS 독점 | ★★★★★ |
| **ASE/SPIL** | 🇹🇼 | OSAT/패키징 | ~$14.3B | 43~55x | 28~35x | OSAT #1 | ★★★★☆ |
| **Unimicron** | 🇹🇼 | ABF 기판 | ~$13.5B | 44.9x | ~22x | ABF #1 (22%) | ★★★★☆ |
| **Micron** | 🇺🇸 | HBM 메모리 | ~$250B+ | ~12x | 5.7~10x | HBM #3 (21%) | ★★★★★ |
| **Amkor** | 🇺🇸 | OSAT/패키징 | ~$14.4B | 38.2x | ~25x | CoWoS 외주 핵심 | ★★★★☆ |
| **Applied Materials** | 🇺🇸 | 패키징 장비 | ~$389B | 46~55x | 33~50x | 패키징 장비 #1 | ★★★★☆ |
| **Lam Research** | 🇺🇸 | TSV/식각 장비 | ~$250B+ | ~45x | ~30x | TSV 식각 핵심 | ★★★☆☆ |
| **Advantest** | 🇯🇵 | ATE | ~$130B | 125.9x | ~41x | ATE #1 (70%) | ★★★★★ |
| **Disco** | 🇯🇵 | 다이싱/그라인딩 | ~$50B | 64.3x | 49.8x | 다이싱 70~80% | ★★★★☆ |
| **Ibiden** | 🇯🇵 | ABF 기판 | ~$32.4B | 63.4x | ~45x | ABF #2 | ★★★★☆ |
| **Ajinomoto** | 🇯🇵 | ABF 필름 | ~$31B | 41.8x | ~35x | ABF 필름 95% | ★★★☆☆ |
| **BESI** | 🇳🇱 | 하이브리드 본딩 | ~€16B | ~60x | ~38x | HB 본딩 #1 | ★★★★★ |

### 6.2 밸류에이션 매력도 순위 (Forward P/E 기준)

| 순위 | 기업 | Forward P/E | 이익 성장률 | PEG 추정 | 판단 |
|------|------|-------------|-----------|---------|------|
| 1 | **Micron** | 5.7~10x | +100%+ | **<0.1x** | 극단적 저평가 (but 사이클 주식 주의) |
| 2 | **Unimicron** | ~22x | +126% | **~0.17x** | 성장 대비 저평가 |
| 3 | **TSMC** | 23~30x | +30%+ | **~0.8x** | 합리적 프리미엄 |
| 4 | **Amkor** | ~25x | +33% | **~0.76x** | TSMC 파트너십 프리미엄 |
| 5 | **ASE/SPIL** | 28~35x | +34% | **~0.9x** | LEAP 성장 반영 |
| 6 | **Lam Research** | ~30x | +41% | **~0.73x** | 패키징 +50% 성장 잠재력 |
| 7 | **Applied Materials** | 33~50x | +20% | **~2.0x** | 밸류에이션 부담 |
| 8 | **Ajinomoto** | ~35x | +35% | **~1.0x** | 독점 프리미엄 적정 |
| 9 | **BESI** | ~38x | +50%+ | **~0.7x** | M&A 프리미엄 미반영 |
| 10 | **Advantest** | ~41x | +26% | **~1.6x** | 독점 프리미엄 but 높음 |
| 11 | **Ibiden** | ~45x | +30%E | **~1.5x** | 투자 사이클 초기, 이익 후행 |
| 12 | **Disco** | 49.8x | +20%E | **~2.5x** | 독점이나 밸류에이션 풀 |

---

## 7. 투자 시사점

### 7.1 밸류에이션-성장 매력 기업 (PEG < 1.0)

1. **Micron** (PEG <0.1x): 메모리 사이클 주식의 함정을 감안해도 Forward P/E 5.7~10x + HBM4 양산 + Cloud BU GM 74%는 매력적. **단, 사이클 피크 접근 시 P/E 하락은 '저평가'가 아닌 '정상화'**
2. **Unimicron** (PEG ~0.17x): EPS +126% 급증 + ABF 기판 1위 + AI 60% 비중 + CAPA 40% 확대. **비한국 기판 기업 중 가장 매력적인 성장-밸류에이션 조합**
3. **BESI** (PEG ~0.7x): 하이브리드 본딩 13.2배 성장(3년) + M&A 프리미엄 잠재력. **인수 성사 시 30~50% 업사이드, 불발 시에도 독립 성장 시나리오 유효**
4. **Lam Research** (PEG ~0.73x): 패키징 +50% 성장 + BESI 인수 시도 → 풀라인업 장비사 전환 가능성

### 7.2 구조적 독점 기업 — 프리미엄 정당화

1. **TSMC**: CoWoS 독점 + CoPoS 차세대 → 첨단 패키징의 유일한 대규모 공급자. Forward P/E 23~30x는 독점 프리미엄 감안 시 합리적
2. **Advantest**: ATE M/S 70%, 모든 AI칩·HBM이 통과 → "테스트 세금". P/E 높지만 대안 부재
3. **Disco**: 다이싱/그라인딩 M/S 70~80%, HBM 극박화 필수 장비. R&D 33%로 기술 해자 강화 중
4. **Ajinomoto**: ABF 필름 95% 독점, 50%+ 마진, 30% 가격 인상. 식품회사 밸류에이션 안에 **숨겨진 반도체 독점 사업**

### 7.3 주요 모니터링 변수

| 변수 | 영향 기업 | 시나리오 |
|------|----------|---------|
| CoWoS 수급갭 추이 | TSMC, ASE/SPIL, Amkor | 갭 축소 시 외주 물량 감소 → ASE/Amkor 주의 |
| HBM4 수율·양산 속도 | Micron, Advantest, Disco | 수율 빠른 램프 시 Micron M/S 확대 |
| 하이브리드 본딩 채택률 | BESI, AMAT, Lam | 2028년 36% 전환 시 BESI 매출 €1B+ |
| BESI M&A 결과 | BESI, AMAT, Lam | 인수가/독립 경영 여부에 따라 3사 밸류에이션 재조정 |
| ABF 필름 부족 심화 | Ajinomoto, Unimicron, Ibiden | 부족 심화 시 기판 가격 추가 인상 → 기판사 마진 압박 |
| AI CAPEX 사이클 | 전체 | 하이퍼스케일러 투자 둔화 시 전 기업 영향 |
| CoPoS 양산 시점 | TSMC, 장비사 전체 | 2028 양산 성공 시 패키징 비용 30% 절감 → 수요 확대 |

### 7.4 포트폴리오 관점 요약

- **밸류체인 상류 (메모리)**: Micron — 사이클 주의하되 HBM4 모멘텀 유효
- **밸류체인 중류 (패키징)**: TSMC(절대 독점), ASE/SPIL(외주 수혜), Amkor(미국 허브)
- **밸류체인 하류 (기판·소재)**: Unimicron(성장-밸류에이션 최적), Ibiden(투자 사이클 초기), Ajinomoto(은밀한 독점)
- **장비**: BESI(하이브리드 본딩 + M&A 옵션), Advantest(테스트 독점), Disco(다이싱 독점)
- **크로스 장비**: Applied Materials(밸류에이션 부담), Lam Research(BESI 인수 시 재평가)

---

## 8. 출처 목록

### TSMC
- TSMC Q1'26 실적 — [Manufacturing Dive](https://www.manufacturingdive.com/news/tsmc-q1-2026-revenue-q2-guidance-ai-arizona/817728/)
- TSMC 6-K FY2026 — [SEC](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000199/a1q26e_withguidancexfinal.htm)
- CoWoS ASP 7nm급 — [TrendForce](https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/)
- CoWoS CAPA/수급갭 — [TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- CoPoS 파일럿 라인 — [TrendForce](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)
- CoPoS 이중 평가 — [TrendForce](https://www.trendforce.com/news/2026/06/16/news-tsmc-reportedly-runs-dual-track-evaluation-on-copos-pilot-line-sparking-global-vs-local-vendor-competition/)
- CoPoS 글라스코어 — [WCCFTech](https://wccftech.com/tsmc-accelerates-copos-packaging-replace-cowos-as-glass-core-substrates-cut-costs-boost-wafer-utilizatio/)
- CoPoS 양산 타임라인 — [All-About-Industries](https://www.all-about-industries.com/panel-level-packaging-at-tsmc-first-copos-pilot-line-2026-mass-production-from-2029-a-46222908685203d0c28cea97fcf7557c/)
- TSMC 밸류에이션 — [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/TSM), [StockAnalysis](https://stockanalysis.com/stocks/tsm/statistics/), [TipRanks](https://www.tipranks.com/stocks/tsm/statistics)
- TSMC Foundry Allocation — [SiliconAnalysts](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026)

### ASE/SPIL
- ASE Q1'26 — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-ase-technology-q1-2026-results-miss-eps-forecasts-93CH-4643872)
- LEAP $3.5B+ — [AlphaPilot](https://www.alphapilot.tech/discover/ase-technology-forecasts-3-5-billion-advanced-packaging-revenue-by-2026-amid-ai-demand), [BigGo Finance](https://finance.biggo.com/news/Avov3J0BNl__-4_GwWaF)
- SPIL 공장 인수 — [TrendForce](https://www.trendforce.com/news/2026/06/11/news-ases-spil-acquires-nt2-8b-plant-amid-spillover-demand-from-tsmc-advanced-packaging-capacity-crunch/)
- ASE 밸류에이션 — [MacroTrends](https://www.macrotrends.net/stocks/charts/ASX/ase-technology-holding/pe-ratio), [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/ASX), [Simply Wall St](https://simplywall.st/stocks/us/semiconductors/nyse-asx/ase-technology-holding/valuation)

### Unimicron
- 사상 최대 매출 목표 — [Taiwan News](https://www.taiwannews.com.tw/news/6373911), [DIGITIMES](https://www.digitimes.com/news/a20260529PD239/unimicron-revenue-2026-demand-substrate.html)
- ABF CAPA 확대/AI 비중 — [DIGITIMES](https://www.digitimes.com/news/a20260130PD220/unimicron-abf-substrate-ai-server-market-capacity.html)
- Bernstein 대만 AI Top Pick — [HeyGoTrade](https://www.heygotrade.com/en/news/tsmc-unimicron-bernstein-taiwan-stocks-strong-ai-exposure/)
- 고객 LTA — [X (Jukan)](https://x.com/jukan05/status/2029745136499114216)
- 밸류에이션 — [CompaniesMarketCap](https://companiesmarketcap.com/unimicron/pe-ratio/)

### Micron
- Q2 FY26 실적 — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000004/a2026q2ex991-pressrelease.htm), [Micron IR](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026)
- HBM 전략/밸류에이션 — [Tech-Insider](https://tech-insider.org/micron-q2-2026-earnings-ai-memory-market/), [MarketDigests](https://marketdigests.com/micron-technology-mu-stock-analysis-2026/), [Seeking Alpha](https://seekingalpha.com/article/4881338-micron-technology-hbm-sold-out-for-2026-wall-street-is-still-underpricing)
- HBM4 양산 — [IndMoney](https://www.indmoney.com/blog/us-stocks/micron-earnings-preview-hbm-ai-memory-mu-stock)

### Amkor
- Q1'26 실적 — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000017/amkr3312026erex-991.htm), [Amkor IR](https://ir.amkor.com/news-releases/news-release-details/amkor-technology-reports-financial-results-first-quarter-2026)
- TSMC 10년 파트너십 — [BusinessWire](https://www.businesswire.com/news/home/20260616574153/en/TSMC-and-Amkor-Technology-Announce-Long-Term-Partnership-to-Accelerate-Advanced-Packaging-in-the-United-States), [Focus Taiwan](https://focustaiwan.tw/sci-tech/202606180014)
- 밸류에이션/Investor Day — [Simply Wall St](https://simplywall.st/stocks/us/semiconductors/nasdaq-amkr/amkor-technology/valuation), [TIKR](https://www.tikr.com/blog/amkor-technology-stock-rises-to-an-all-time-high-can-it-keep-going)

### Applied Materials
- Q2 FY26 실적 — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000006951/000162828026035071/exhibit991q22026earningsre.htm), [StockTitan](https://www.stocktitan.net/news/AMAT/applied-materials-announces-second-quarter-2026-y205hrnxvpxb.html)
- Kinex 하이브리드 본딩 — [Applied Materials](https://www.appliedmaterials.com/us/en/product-library/kinex-integrated-die-to-wafer-hybrid-bonding-system.html), [BALD Engineering](https://www.blog.baldengineering.com/2025/11/applied-materials-deepens-partnership.html)
- NEXX 인수 — [Futurum Group](https://futurumgroup.com/insights/applied-materials-q2-fy-2026-ai-capacity-expansion-fuels-equipment-demand/)
- 밸류에이션 — [GuruFocus](https://www.gurufocus.com/term/forward-pe-ratio/AMAT), [MacroTrends](https://www.macrotrends.net/stocks/charts/AMAT/applied-materials/pe-ratio), [TIKR](https://www.tikr.com/blog/applied-materials-stock-posts-record-revenue-and-50-gross-margin-in-q2-fy2026)

### Lam Research
- Q3 FY26 실적 — [Simply Wall St](https://simplywall.st/stocks/us/semiconductors/nasdaq-lrcx/lam-research), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/lam-research-lrcx-betting-advanced-200933179.html)
- 패키징 +50% 성장 — [Futurum Group](https://futurumgroup.com/insights/lam-research-q2-fy-2026-highlights-ai-driven-demand-and-packaging-gains/)
- BESI 인수 — [Tiger Brokers](https://www.itiger.com/news/1159006392), [Kavout](https://www.kavout.com/market-lens/why-is-lam-research-eyeing-be-semiconductor), [Digital Today](https://www.digitaltoday.co.kr/en/view/36925/lam-research-applied-materials-consider-acquiring-dutch-chip-equipment-maker-besi)

### Advantest
- FY25/FY26 실적 — [PitchBook](https://pitchbook.com/profiles/company/42013-36), [Advantest IR](https://www.advantest.com/en/investors/financial-highlights/forecast/), [DIGITIMES](https://www.digitimes.com/news/a20260501VL206/advantest-earnings-outlook-revenue-testing.html)
- ATE M/S 70% — [Apple Podcasts](https://podcasts.apple.com/ca/podcast/advantest-controls-70-of-ai-chip-testing-up-450-in/id1690533965?i=1000765514636), [RCR Wireless](https://www.rcrwireless.com/20260130/test-measurement/advantest-rises-with-the-ai-tide)
- 밸류에이션 — [CompaniesMarketCap](https://companiesmarketcap.com/advantest/pe-ratio/), [StockAnalysis](https://stockanalysis.com/quote/tyo/6857/market-cap/)

### Disco
- Q1'26 실적 — [Meyka](https://meyka.com/blog/dispf-disco-corporation-earnings-beat-q1-2026-results-2304/)
- 기술/M/S 분석 — [SemiAnalysis](https://newsletter.semianalysis.com/p/disco-corporation-the-world-leader)
- 밸류에이션 — [PitchBook](https://pitchbook.com/profiles/company/62278-03), [Yahoo Finance](https://finance.yahoo.com/quote/DSCSY/)

### Ibiden
- ¥500B 투자 — [Ibiden IR](https://www.ibiden.com/company/2026/02/notice-regarding-capital-investment-plan-for-high-performance-ic-package-substrates.html), [Kantenna](https://kantenna.com/topic/ibiden-5-billion-dollar-investment-ai-ic-package-substrate), [DIGITIMES](https://www.digitimes.com/news/a20260204PD227/ibiden-expansion-capacity-production-plant.html)
- 밸류에이션 — [PitchBook](https://pitchbook.com/profiles/company/62921-44), [GuruFocus](https://www.gurufocus.com/stock/IBIDF/data/pe-ratio)

### Ajinomoto
- ABF 필름 실적/가격인상 — [TrendForce](https://www.trendforce.com/news/2026/05/08/news-ajinomoto-ramps-chip-packaging-push-with-%C2%A51-2b-land-buy-for-new-plant-in-2032-abf-margins-top-50-on-ai-boom/), [BigGo Finance](https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE), [DIGITIMES](https://www.digitimes.com/news/a20260513PD230/ic-substrate-abf-substrate-demand-substrate-2026.html)
- ABF 독점 분석 — [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261783966-abf-ajinomoto-nvidia-ai-supply-chain-tradingkey), [Substack (Nikhs)](https://nikhs.substack.com/p/abf-the-material-beneath-the-model)
- 밸류에이션 — [CompaniesMarketCap](https://companiesmarketcap.com/ajinomoto/marketcap/)

### BESI
- Q1'26 실적 — [BESI IR](https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q1-26-results/), [TipRanks](https://www.tipranks.com/news/company-announcements/be-semiconductor-rides-hybrid-bonding-wave-in-earnings)
- 하이브리드 본딩 — [Bits&Chips](https://bits-chips.com/article/besi-sees-orders-double-on-hybrid-bonding-demand/), [TradingView](https://www.tradingview.com/news/urn:summary_document_transcript:quartr.com:3255461:0-besi-revenue-and-orders-surged-on-ai-and-hybrid-bonding-demand-with-margins-and-cash-flow-sharply-higher/)
- M&A 경합 — [Tiger Brokers](https://www.itiger.com/news/1159006392), [IndexBox](https://www.indexbox.io/blog/besi-receives-acquisition-interest-from-lam-research-and-applied-materials/), [AInvest](https://www.ainvest.com/aime/share/applied-materials-lam-research-eye-semiconductor-acquisition-reshape-chip-packaging-industry-landscape-73516b/)
- 하이브리드 본딩 시장 규모 — [TrendForce](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)

### 시장 전체
- ABF 기판 시장 — [Semiconductor Insight](https://semiconductorinsight.com/report/abf-substrate-market/), [Business Research Insights](https://www.businessresearchinsights.com/market-reports/ajinomoto-build-up-film-abf-market-122893)
- 첨단 패키징 시장 — [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/advanced-packaging-market)
- HBM 가격 — [SiliconAnalysts](https://siliconanalysts.com/tools/hbm-analysis)

---

## 9. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-22 | 초안 작성 — 글로벌 12개사(TSMC, ASE/SPIL, Unimicron, Micron, Amkor, Applied Materials, Lam Research, Advantest, Disco, Ibiden, Ajinomoto, BESI) 재무·기술·밸류에이션 심화 분석, 크로스 밸류에이션 비교, 투자 시사점 |
