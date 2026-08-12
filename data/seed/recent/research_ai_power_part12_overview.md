# AI 전력 인프라 리서치 — Part 1-2: 산업구조와 투자 좌표

> 목적: AI 데이터센터 전력 수요의 매크로 전망, 4단계 밸류체인 맵, 병목·해자·비대칭성 투자 프레임워크
> 작성일: 2026-06-22
> 커버리지: Part 1-2 (ai_power_infra_overview.html) 리서치 데이터
> 상태: 초안

---

## 1. 매크로 수요 전망 — AI가 만드는 전력 수요의 규모

### 1.1 글로벌 데이터센터 전력 소비 전망

| 연도 | 전력 소비 (TWh) | 출처 | 비고 |
|------|----------------|------|------|
| 2024 | 415 | IEA | 전 세계 전력의 ~1.5% |
| 2025 (실적) | 447–485 | Gartner 447 / IEA 485 | IEA: 전년비 +17%, AI DC만 +50% |
| 2026E | 565 | Gartner (Jun'26) | YoY +26% |
| 2030E (IEA Base) | ~950 | IEA (Apr'25) | 전 세계 전력의 ~3% |
| 2030E (Gartner) | >1,200 | Gartner (Jun'26, 상향) | Nov'25 980 → Jun'26 >1,200 (7개월 만에 +22% 상향) |
| 2030E (Goldman Sachs) | 1,350 | Goldman Sachs (Apr'26) | US ~750 + RoW ~600 TWh |
| 2035E (IEA Lift-Off) | >1,700 | IEA (Apr'26) | Base Case 대비 +45% |

- **CAGR**: 2024–2030 약 15%/yr — 전체 전력 수요 증가의 4배 속도 (IEA)
- **AI 서버 단독**: 93 TWh (2025) → 432 TWh (2030), ~5배 증가 (Gartner Nov'25)
- **글로벌 전력 비중**: 2030년 전체 전력의 ~3% (IEA Base), 4%+ (Goldman Sachs)
- **2030 전망 불확실성**: IEA 950 → Gartner >1,200 → Goldman 1,350 TWh. 전망사 간 40%+ 편차. **상향 조정 추세** — Gartner가 7개월 만에 22% 상향한 점이 시사적
- **AI가 핵심 드라이버**: 2025년 AI DC 전력 성장률 +50% YoY (IEA Apr'26 실측). AI 서버가 2027년에 일반 서버 전력 추월 전망 (Gartner)

### 1.2 미국 데이터센터 수요 — 집중과 병목

| 지표 | 수치 | 출처 |
|------|------|------|
| 2023 US DC 전력 (실적) | 176 TWh (US 전력의 4.4%) | DOE/LBNL (Dec'24) |
| 2024 US DC 전력 | 183 TWh | Pew/DOE |
| 2026 US DC 전력 전망 | 260 TWh | IEA Electricity 2026 |
| 2028 US DC 전망 (Low) | 325 TWh (US 전력의 6.7%) | DOE/LBNL |
| 2028 US DC 전망 (High) | 580 TWh (US 전력의 12%) | DOE/LBNL |
| 2030 US DC (McKinsey) | 606 TWh (US 전력의 11.7%) | McKinsey |
| 2030 US DC (Goldman Sachs) | ~750 TWh | Goldman Sachs (Apr'26) |
| 2030 US DC 전망 범위 | 200–1,050 TWh (중앙 300–430) | WRI/DOE/IEA/SemiAnalysis |
| 2030 US 전체 전력 중 AI 비중 | ~9% (2023년 4%에서) | Morgan Stanley |
| 글로벌 DC 전력 용량 (GW) | 104 (2025) → 132 (2026) → 290 (2030) | Gartner (Jun'26) |
| US 전력 수급 부족 전망 | 9–18 GW (12–25% 부족) through 2028 | Morgan Stanley |
| US DC 수요 (GW) 전망 | 74 GW by 2028, 49 GW 공급 부족 | Morgan Stanley |

- 전망사 간 편차가 매우 크다 (200–1,050 TWh by 2030). **불확실성 자체가 투자 시사점** — 상단 시나리오에 베팅하는 기업과 보수적으로 접근하는 기업의 격차가 수익으로 연결
- Goldman Sachs가 가장 공격적 (~750 TWh US), McKinsey 중간 (606 TWh), LBNL Low가 가장 보수적 (325 TWh by 2028)
- 85%+ 신규 DC 설비가 미국·중국·EU에 집중 (IEA)
- **용량 성장**: 글로벌 DC 전력 용량 104 GW (2025) → 290 GW (2030), ~2.8배 (Gartner Jun'26)

### 1.3 투자 규모와 자금 흐름

| 지표 | 수치 | 출처 |
|------|------|------|
| 2025 DC 투자 | $580B | IEA — 글로벌 석유공급 투자($540B) 초과 |
| AI 인프라 누적 투자 전망 | ~$3T by 2028 (80%+ 아직 미집행) | Morgan Stanley |
| 하이퍼스케일러 2026 AI 지출 | $600B+ (2026 단독) | Morgan Stanley |
| AI 인프라 파이낸싱 갭 | $1.5T ($2.9T 중 하이퍼스케일러 $1.4T만 부담) | Morgan Stanley |
| 2026 AI 관련 부채 발행 전망 | ~$570B (전년 대비 2배+) | Morgan Stanley |
| US 유틸리티 그리드 투자 | $1.4T over 5년 | Morgan Stanley / CBS News |
| DC 투자 슈퍼사이클 | ~$3T by 2030 | JLL |
| Stargate 프로젝트 | $500B (4년), 1GW급 DC 5개 | OpenAI·SoftBank |

- **"15-15-15" 동학**: 15년 DC 임대, 15% 수익률, $15/W 순가치 창출 (Morgan Stanley)
- **파이낸싱 구조 변화**: $2.9T 건설비 중 하이퍼스케일러 자체 부담 $1.4T, 나머지 $1.5T은 은행·PE·국부펀드·채권시장에서 조달 필요 → 자본시장 전체에 영향

### 1.4 핵심 숫자 — 랙 밀도의 폭발

| 지표 | 수치 | 출처 |
|------|------|------|
| 산업 평균 랙 밀도 | 7 kW (2021) → 16 kW (2025) → **27 kW (2026)** | AFCOM 2026 (10년 추적 사상 최대 YoY 증가) |
| NVIDIA GB200 NVL72 | 130–132 kW/rack (액체냉각 115 kW + 공냉 17 kW) | NVIDIA/HPE |
| AI 전용 랙 | 60–150 kW (현재), ~300 kW (차세대), ~1 MW (그 다음) | Bloom Energy 2026 |
| 극단 밀도 랙 | 200 kW+ | Ramboll |
| 평균 시설 규모 | 32 MW (2025) → **38 MW (2026)** | AFCOM 2026 |
| 단일 AI 클러스터 (xAI Colossus) | 2 GW (GPU 55.5만개) | 2025.12–2026.01 |
| 액체냉각 도입률 | 19% (2025) → **36% (2026)**, +28%가 12–24개월 내 도입 계획 | AFCOM 2026 |
| 냉각 불충분 인식 | ~40%가 현재 냉각이 운영 니즈 미충족 | AFCOM 2026 |

- **인퍼런스 전환**: AI 컴퓨트 워크로드 중 인퍼런스 비중 50%+ 도달 (학습에서 추론으로 전환) — 상시 가동, 전력 수요 지속성 강화 (Bloom Energy Mid-Year Jun'26)

### 1.5 SemiAnalysis 데이터

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 DC IT 전력 | 49 GW (2023) → 96 GW (2026) | SemiAnalysis |
| 그 중 AI | ~40 GW (2026) | SemiAnalysis |
| US AI 전력 | ~3 GW (2023) → 28+ GW (2026) | SemiAnalysis |
| DC 전력 CAGR | 12–15% → 25% (가속 중) | SemiAnalysis |
| 90%의 성장이 AI에서 발생 | — | SemiAnalysis |

---

## 2. 밸류체인 맵 — 발전에서 칩까지, 전류를 따라가기

### 2.1 4단계 밸류체인 구조

```
STAGE 01: 발전         STAGE 02: 송배전        STAGE 03: DC 전력 인프라    STAGE 04: 냉각
──────────────── ─→ ──────────────── ─→ ──────────────────── ─→ ────────────
원전·SMR            초고압 변압기         UPS·배전반               공냉 → 수냉
가스터빈·LNG        전력케이블·HVDC       전력반도체(SiC/GaN)      → 액침냉각
재생(보완재)         차단기               HVDC busway·800V DC      냉각 유체
자가발전(BTM)        계통연계             연료전지(BTM)
```

### 2.2 STAGE 01 — 발전 (Generation)

#### 가스터빈 슈퍼사이클

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **GE Vernova** | 백로그 100 GW (Q1'26), 83→100 GW QoQ. 110 GW+ YE26 목표. 총 백로그 $163B. Q1 DC향 전동화 수주 $2.4B (전년 연간 초과). 가스터빈 25기 출하 (+32% YoY), 판가 +10–20% vs Q4'25. 1Q26 순이익 $4.7B. **판가 궤적: 2027년 말 ~$600/kW 전망 (2019 대비 ~3배, Wood Mackenzie)**. 연간 생산능력: ~10 GW → 20 GW (Q3'26) → 24 GW (2028 목표). 백로그 소화 기간 ~10년 | SEC Filing, Utility Dive, Wood Mackenzie |
| **Siemens Energy** | FY26 Q1 수주 €17.6B (+34%), 6주간 8 GW 신규 수주. 백로그 €146B (사상 최대). 2028년까지 매진, 2029년 이후 슬롯 판매. Q1 순이익 €746M (~3x YoY). 판매 대수: 100기 (FY24) → **194기 (FY25)**, ~2배. AI/DC 비중: 신규 수주의 ~25%. FY26 가이던스: 매출 +14–16%, OPM 12%, 순이익 ~€4B. 지역: 40% US, 35% EU, 15% 중동/중국 | Siemens Energy, Enlit, StocksFoundry |
| **두산에너빌리티** | US 빅테크(xAI 추정)에 380MW급 가스터빈 7기 수주 (~₩1.2T, 회사 역대 최대). 미국 총 12기, 글로벌 누적 23기 (2019년 이후). **2038년 105기 목표**. 인도: 2029.05부터 월 1기. Q1'26 수주잔고 $16.2B (+62%). Rolls-Royce SMR 합류 (Wylfa·Temelín). 체코 두코바니 원전 스팀터빈 ₩320B. 북미 첫 스팀터빈 수주 확보. **2026년 외국인 순매수 1위** | TechTimes, Seoul Economic Daily, 서울신문 |

- **공급 병목**: CCGT 리드타임 5–7년. 고효율 터빈 부족 시 효율 50–60% 낮은 대안 사용 → 가스 수요 구조적 증폭
- **글로벌 가스터빈 시장**: $23–30B (2025) → $43–65B (2034–35), CAGR 7–11% (Fortune BI, GM Insights, Precedence Research)
- **온사이트 발전 전환**: 2025년부터 대형 AI 시설의 기본 전략. Williams $5.1B "파워 이노베이션" 포트폴리오 ($3.1B DC 전력 프로젝트 2건, $1.6B Project Socrates 2H26 완공 예정)

#### 원전·SMR (Nuclear Renaissance)

| 기업/프로젝트 | 핵심 데이터 | 출처 |
|--------------|------------|------|
| **Constellation Energy** | TMI Unit 1 재가동 (835 MW), Microsoft 20년 PPA. $1.6B 투자 + DOE $1B 대출. **2027년 첫 전력 공급** (퇴역 원전 재가동 최초 사례). Calpine **$21.84B** 인수(SEC 8-K) → 합산 **60 GW** 발전 (원전 32.4 GW + 가스 26 GW). PJM 계통연계 2031년 지연 리스크. FY26 EPS +20% 전망. 52주 고가 $412.70, 현재 ~$320 | Yahoo Finance, Motley Fool, SEC 8-K |
| **NuScale Power** | NRC 설계인증 1호. 모듈 77 MWe. Romania VOYGR: 2029–30 → **2033–34로 4년 지연** (FID 2026.02 승인). Standard Power: 24모듈 1,848 MWe (OH/PA DC용). 주가 -26.5% (Feb'26), UBS PT $38→$20. 시가총액 ~$4.4B. 매출 없음, 적자 지속 | SEC, Motley Fool, IBTimes |
| **TerraPower** | Natrium SFR 345 MW. **NRC 건설허가 2026.03** (상용 비경수로 최초). Kemmerer WY 착공 2026.04. Meta 6.6 GW 포트폴리오 일부 | Canary Media, DOE |
| **Kairos Power** | 불소염냉각 고온로. Hermes 테스트로 건설 착수 2025.05 (Oak Ridge). **Hermes 2 착공 2026.04** (Google 상용 데모). Google 500 MW 계약 | Canary Media, DOE |
| **X-energy** | Xe-100 HTGR 320 MW. **IPO 2026.04.24** ($23 공모 → $30.33 시초가). Amazon $700M 투자, 최대 12기 Xe-100. Dow Seadrift TX 건설허가 NRC 심사 중 | AccessIPOs, DOE |
| **SMR 시장 전체** | $6.3B (2026) → $8.1B (2033), CAGR 3.6%. 설치 용량: 312.5 MW (2025) → 912.5 MW (2030), CAGR 23.9% | MarketsandMarkets, Mordor Intelligence |
| **일-미 원자력 투자** | $550B 대미 투자 중 원자력 최대 $200B (웨스팅하우스+GE히타치). 2·3차 트랜치 구체화 중. "일본 기업 우선 납품" 조건 | U.S. Commerce, AAF |

#### 하이퍼스케일러 원전 커밋먼트 (2026.05 기준)

| 기업 | 규모 | 파트너 |
|------|------|--------|
| **Meta** | 최대 6.6 GW | TerraPower + Oklo + Vistra + Constellation |
| **Microsoft** | 835 MW | Constellation (TMI 재가동) |
| **Google** | 500 MW | Kairos Power |
| **Amazon** | $700M / 12기 Xe-100 | X-energy |
| **합계** | 13개 프로젝트, **9.8+ GW** | — |

- **핵심 시사점**: 하이퍼스케일러의 원전 투자 총량은 인상적(9.8+ GW)이나, 가장 빠른 신규 전력은 2027년(TMI 재가동). 차세대 SMR은 2029–2034년 목표. **가스터빈이 5–10년간 브릿지 역할** 확실

#### 재생에너지의 자리

- 태양광·풍력: 가장 저렴하나 간헐성으로 24시간 AI 클러스터 단독 해법 불가
- 역할: 전력믹스 보완, HVDC·해저케이블 등 송전 인프라 수요 간접 창출
- 빅테크: 자체 발전(가스·연료전지·원전 PPA) + ESS 병행이 기본 전략

### 2.3 STAGE 02 — 송배전 (T&D)

#### 변압기 공급 부족 — 구조적 병목

| 지표 | 수치 | 출처 |
|------|------|------|
| 전력 변압기 리드타임 | **128주** (~2.5년) 평균 | Wood Mackenzie Q2'25 Survey |
| GSU(Generator Step-Up) 리드타임 | **144주** (~2.8년) | Wood Mackenzie |
| 리드타임 변화 | 6–12개월 (pre-2020) → **24–48개월** (2026) | Power Magazine, IEEE Spectrum |
| 전력 변압기 공급 부족률 | **30%** (2025) → **5%** (2030E) | Wood Mackenzie |
| GSU 공급 부족률 | **47%** (2025) → **14%** (2030E) | Wood Mackenzie |
| 배전 변압기 공급 부족률 | **10%** (2025) | Wood Mackenzie |
| 수요 증가 (2019년 대비) | 전력 변압기 +119%, 배전 변압기 +34% | Wood Mackenzie |
| 가격 상승 | +60–80% | Electrical Trader |
| 미국 노후 배전 변압기 | ~**4,000만대**가 수명 초과 | Wood Mackenzie |
| 미국 전력망 노후 | 70%가 1960년대 | DOE |

- **패드마운트 3상 변압기**: DC·제조·EV 충전 수요 급증으로 부족 **악화** 전망 (Wood Mackenzie)
- **공급 부족 해소 전망**: 전력 변압기 부족은 2030년까지 30%→5%로 완화 전망이나, 현 시점에서는 공급자 우위 지속
- **"만들 수 있는 곳이 가격을 정한다"**: 한국 3사(HD현대일렉트릭·LS일렉트릭·대한전선)의 북미 사상 최대 실적의 배경

#### 한국 3사 기존 데이터 (기존 HTML 기준, 2025~1Q26)

| 기업 | 핵심 수치 | 비고 |
|------|----------|------|
| HD현대일렉트릭 | 수주잔고 9.6조, 1–3Q25 영익 6,744억, OPM 24.8% | 765kV 과점, 앨라배마 증설 2027 |
| LS일렉트릭 | 2025 매출 4.96조, 수주잔고 5조, DC 수주 1조+ | 토탈 솔루션(송·배전·연료전지 설비) |
| 대한전선 | 2025 매출 3.64조, 수주잔고 3.66조, 영익 1,286억 | HVDC·해저케이블, 당진 2공장 2027 |

#### HVDC와 그리드 인프라

| 지표 | 수치 | 출처 |
|------|------|------|
| AI DC HVDC 전력 시스템 시장 | $1.53B (2025) → $4.59B (2035), CAGR 12.5% | Precedence Research |
| 800V HVDC DC 시장 | ~$5.4B by 2031, CAGR ~132% (2026–2031) | Mobility Foresights |
| DC 전력 시스템 시장 전체 | $35B (2025) → $50–70B (2034) | MarketsandMarkets |
| 글로벌 그리드 투자 | $5.8T (2026–2035), 디지털 그리드 ~$700B | 업계 |
| Grain Belt Express 송전선 | $11B, 800마일 HVDC, 5,000 MW 용량, 2026 착공 | ConstructConnect |

### 2.4 STAGE 03 — DC 전력 인프라

#### 800V DC 전환

| 지표 | 수치 | 출처 |
|------|------|------|
| 효율 개선 | AC 415V 대비 같은 도체에 85% 더 많은 전력 전송 | IEEE Spectrum |
| 전류 감소 | ~15배 (고전압), 1 GW 스케일에서 ~50 MW+ 절감 | YK Investment Research |
| 전체 효율 향상 | end-to-end 최대 5% | Power Electronics News |
| 유지보수 비용 절감 | 최대 70% | NAND Research |
| 타겟 랙 전력 | 600 kW+/rack | YK Investment Research |
| DC 도입 계획 | 45%가 2028년까지 DC 도입 계획 | Bloom Energy 2026 Report |
| 고압 중앙 버스웨이 | 60%가 2028년까지 도입 계획 | Bloom Energy 2026 Report |
| 800VDC 누적 용량 전망 | ~39 GW by 2030 | SemiAnalysis |
| 신규 DC의 DC 기반 비중 | 58% by 2030 | Bloom Energy 2026 |
| 오프그리드 DC 비중 | 1/3 by 2030 | Bloom Energy 2026 |

- **NVIDIA 주도**: Rubin Ultra 플랫폼용 800V DC 아키텍처. Texas Instruments·Renesas·Navitas 등 파워 반도체 협력
- **Vertiv**: 800V DC 풀 제품라인 **2H 2026 상용 출시 예정**. Delta Electronics는 이미 배치 시작
- **SolarEdge**: 99% 효율 SST (Solid-State Transformer) 개발 중
- **과제**: UL 인증, 안전 코드, 지자체 승인이 느림 → 하이퍼스케일러 파일럿에 머무는 단계
- **배치 시기**: Phase 1-2 배포 **2026 말~2027 초** (하이퍼스케일러 주도)

#### 계통연계 큐 병목 (Grid Interconnection Queue)

| 지표 | 수치 | 출처 |
|------|------|------|
| 미국 계통연계 대기 프로젝트 | ~11,600건, 2,600 GW (발전 1,570 + 저장 1,030) | LBNL Queued Up |
| 미국 현재 설치 용량 대비 | 대기 용량이 설치 용량(1,279 GW)의 **2배 이상** | Utility Dive |
| 중앙 대기기간 | **~5년** (상용 운영까지) | LBNL |
| 북부 버지니아·피닉스·댈러스 | 4–7년 대기, 2026.05 큐 진입 시 전력 확보 **2030–2033** | EnkiAI |
| 대기 → 상용운영 기간 | 2017년 이후 ~60% 증가, 평균 **2,100일+** | Enverus |
| 프로젝트 철회율 | **~80%** (비용·지연으로 포기) | LBNL/PV Tech |
| 계통연계 비용 | 철회 프로젝트의 총 예산 중 **30–37%** | LBNL |

- **핵심**: 계통연계 병목이 BTM(자가발전) 트렌드를 가속하는 구조적 원인

#### 자가발전 (Behind-the-Meter)

| 지표 | 수치 | 출처 |
|------|------|------|
| 현재 온라인 BTM 용량 | ~2 GW (4개 프로젝트), 2026 말 2.8–3.2 GW 전망 | Build.inc |
| 계획 중 온사이트 가스 발전 | **100 GW** | BNEF / Latitude Media |
| 개발사 BTM 탐색 비율 | 56% (2026 Foley Survey) | datacenterHawk |
| 온사이트 전력 전략 비율 | 61–73% of operators (Bloom Energy) | Bloom Energy |

- 전력망을 기다리지 못하는 빅테크의 해법: 연료전지(Bloom Energy), 가스 발전소(Williams), 원전 PPA(Constellation)
- 2026년이 **가스 발전 프로젝트 기록의 해** 될 수 있음 — 계획 용량 가동 시 2002년 기록(100 GW) 초과 전망 (Global Energy Monitor)
- Bloom Energy: 백로그 ~$20B, FY26 가이던스 $3.4–3.8B, Q1'26 매출 +130% YoY, 파이프라인 4 GW (+267% QoQ)

#### 전력반도체 (SiC/GaN)

| 지표 | 수치 | 출처 |
|------|------|------|
| SiC 전력반도체 시장 | $2.2B (2025) → $11.3B (2033), CAGR 22.5% | DataM Intelligence |
| 글로벌 SiC 시장 | $6.28B (2026) → $12.36B (2034), CAGR 8.83% | Fortune BI |
| 수요 구성 | 자동차 45%, 산업 전력 25%, 에너지/유틸리티 20%, DC ~10% (급성장) | 업계 |
| DC 연관 | 800VDC 아키텍처에 SiC/GaN 필수 — 효율·열관리 직결 | IDTechEx |
| **Infineon** | NVIDIA MGX 에코시스템 합류 (2026.05), 800VDC 랙용 Si/SiC/GaN. 3.3kV CoolSiC 양산. PSS 부문 €1.5B (2026) → €2.5B (2027E, +67%) | Infineon, Power Semi Weekly |
| **Wolfspeed** | 세계 최초 10kV SiC MOSFET (2026.03.06). DC 매출 QoQ +50%. 200mm Mohawk Valley 팹 전환 | Wolfspeed 8-K |
| **시장 점유율** | STMicro 32.6% (#1), onsemi (#2), Infineon (#3), Wolfspeed, ROHM — Top 5가 90%+ | Semiconductor Today |

### 2.5 STAGE 04 — 냉각 (Cooling)

#### 액체냉각 시장

| 지표 | 수치 | 출처 |
|------|------|------|
| DC 액체냉각 시장 전체 | $6B (2026) → $27.1B (2035), CAGR 18.2% | GM Insights |
| 또는 | $8.17B (2026) → $27.65B (2033) | MarketsandMarkets |
| 액침냉각(Immersion) 단독 | $348M–$5.72B (2026, 정의 차이) | 다수 |
| 성장 동력 | 30 kW+ 랙, GPU 고밀도, 탄소 규제 | 업계 |

- 3M 냉각유체 생산 중단 (2025 말) → **SK엔무브·GS칼텍스** 등 국내 유체 공급사에 기회
- Eaton: Boyd Thermal 인수 (액체냉각), NVIDIA Rubin 플랫폼용 Eaton Beam Rubin DSX 출시

#### 글로벌 인프라 기업 실적 (Q1 2026)

| 기업 | Q1'26 매출 | 성장률 | DC 관련 하이라이트 | 출처 |
|------|-----------|--------|-------------------|------|
| **Vertiv** | $2,650M | +30% YoY (미주 +44%) | Q4'25 수주 +252% YoY (B/B 2.9x). Q1'26 백로그 $12.45B (+81% YoY). Adj OPM 20.8% (+430bps). FY26 가이던스 **$13.25–13.75B** (+30%), Adj EPS $6.30–6.40 (+51%). 800V DC 에코시스템 H2 2026 | SEC, TechJack |
| **Eaton** | $7,451M | +10% organic (EA +20%) | DC 수주 **+240%**, DC 매출 +50% YoY. EA 마진 25.6%. 전기 백로그 +48%. **Boyd Thermal $9.55B 인수** (2026.03, 액체냉각 $1.5B 매출). DC = 2025 매출의 21%. FY26 유기 성장 **10%로 상향** | BusinessWire, DCD |
| **Schneider** | €9.8B ($10,600M) | +11.2% organic | 에너지관리 +13%, DC = 매출의 **24%**, DC/네트워크 = 주문의 ~30%. **Motivair $850M 인수** (75% 지분, 2025.02, 액체냉각 풀 포트폴리오). FY26 +7–10%, EBITA 마진 +50–80bps | Investing.com, Facilities Dive |

---

## 3. 투자 프레임워크 — 병목·해자·비대칭성

> 참조: `data/note-ai-money-flow_20260618.md` (투자 사고 프레임워크 메모)

### 3.1 조건 1: 병목(Bottleneck) 구간인가?

공급이 수요를 못 따라가는 구간에 돈이 몰린다.

| 밸류체인 단계 | 병목 요소 | 심각도 | 근거 |
|-------------|---------|--------|------|
| 발전 | 가스터빈 슬롯 | ★★★★★ | GEV 2029년 이후 슬롯 밀림, 리드타임 5–7년, Siemens 2028까지 매진 |
| 발전 | 원전 건설 일정 | ★★★★☆ | NuScale 4년 지연, SMR 상용화는 2030년대 |
| 송배전 | 초고압 변압기 | ★★★★★ | 리드타임 24–48개월, 공급 30% 부족, 가격 +60–80% |
| 송배전 | 계통연계 큐 | ★★★★☆ | 미국 DC 절반이 전력 확보 실패로 지연·중단 |
| DC 인프라 | 800V DC 표준화 | ★★★☆☆ | 45% 도입 계획, 인증·안전코드가 속도 제약 |
| 냉각 | 액침냉각 유체 | ★★★☆☆ | 3M 철수로 공급공백, 표준 미확립 |

### 3.2 조건 2: 독점적 해자(Moat)를 가졌는가?

| 기업/구간 | 해자 유형 | 설명 |
|----------|---------|------|
| GE Vernova | 기술 독점 + 규모 | HA급 가스터빈 과점, 연간 20→24 GW 생산, 서비스 매출 락인 |
| HD현대일렉트릭 | 기술 인증 | 765kV 초고압 변압기 글로벌 소수 공급. 인증 장벽 수년 |
| Vertiv | 생태계 락인 | NVIDIA 레퍼런스 아키텍처 기본 파트너, 전력+냉각 원스톱 |
| Bloom Energy | 기술 차별화 | SOFC + 800V DC 레디 이중 포지션. 자가발전 순수 플레이 |
| 대한전선 | 진입장벽 | HVDC 해저케이블 기술 + 신공장(2027). 기술인증 수년 소요 |

### 3.3 조건 3: 비대칭성 — 하방은 막히고 상방은 열린가?

| 구간 | 상방 시나리오 | 하방 리스크 | 비대칭 판단 |
|------|-------------|-----------|-----------|
| 가스터빈 (GEV, 두산) | 슈퍼사이클 지속, 판가 상승, 서비스 매출 | 이미 높은 밸류에이션 | 중립–긍정 (판가 상승이 EPS 레버리지) |
| 초고압 변압기 (HD현대) | 공급 우위 지속, 앨라배마 증설 | 증설 물량 일시 출회 | 긍정 (2027 증설까지 공급자 마켓) |
| Bloom Energy | 백로그 $20B 매출 전환, DC 표준 채택 | 고객 집중, 희석, Crusoe 보류 | 고위험-고수익 (극단적 밸류) |
| SMR (NuScale) | TVA 6 GW 구속계약, 첫 모듈 착공 | 반복적 지연, 매출 없음, 적자 | 옵션 (성공 시 10x, 실패 시 -50%+) |
| 냉각 (Vertiv, Eaton) | 30%+/yr 성장, 수주잔고 가시성 | Forward P/E 49x(Vertiv), CAPEX 사이클 | 긍정 (실적 성장이 뒷받침) |

---

## 4. 리스크 체크리스트 (R1–R5 확장)

### R1 — AI CAPEX 사이클 조정
- 하이퍼스케일러 투자 둔화·연기 시 전력 발주가 가장 먼저 흔들린다
- 모니터링: MSFT/GOOGL/META/AMZN 분기 CAPEX 가이던스, DC 착공 건수

### R2 — 효율 개선의 역설 (Jevons Paradox)
- IEA: AI 작업당 에너지는 매년 큰 폭으로 하락
- 효율이 수요 전망을 깎을 수 있으나, 역으로 사용량 폭증으로 총 수요는 증가할 가능성 (Jevons)
- 모니터링: GPU 에너지 효율 개선 속도 vs DC 전력 실질 소비 증가율

### R3 — 공급부족 해소
- 변압기·가스터빈 증설이 한꺼번에 풀리면 공급자 우위와 판가가 정상화
- GEV 앨라배마 변압기 공장, HD현대 증설, Siemens 확장 등 2027–2028년 집중
- 모니터링: 글로벌 변압기/터빈 증설 CAPA 가동 시점, 리드타임 추이

### R4 — 정책·관세·금리
- 전력요금 규제, 미국 관세 (한국산 변압기 등), 환율 변동
- 높아진 밸류에이션을 누르는 금리 환경
- 모니터링: US 관세 정책 변화, 한국 전력 규제, Fed 금리

### R5 — 지역 수용성·인허가 (Data Center NIMBY)
- **$64B** DC 프로젝트 차단·지연 ($18B 차단 + $46B 지연) — Data Center Watch
- **69개 지자체** 모라토리엄 시행 중 (4건은 영구), 다른 트래커로 **222건 / 30개 주** — Tom's Hardware, Moratorium Nation
- 증가 속도: 8건 (2025.05) → **78건+ (2026.05)**, 1년간 ~10배 — Tom's Hardware
- **142개 시민단체** / 24개 주 조직화, 버지니아만 42개 — Data Center Watch
- 주요 법안: Maine 주지사 거부권(2026.04.24), **뉴욕 1년 모라토리엄 통과** (2026.06.04), Virginia HB 1515 2027으로 이월
- Spokane 500 MW DC: 5,000+ 주민 민원으로 Avista 처리 중단
- 계획된 미국 DC 건설의 **~절반**이 전력 확보 실패·리드타임으로 지연·중단 — DIGITIMES
- **수요가 아니라 건설 '속도'를 깎아 기자재 매출 인식 타이밍을 늦추는 리스크**
- 모니터링: 모라토리엄 건수 추이 (10x/yr 증가 중), 주요 주(TX, VA, GA, NY) 인허가 진행률

---

## 5. 투자 시간축 — 단기 vs 중기

### 5.1 단기 (향후 6개월) — 증명된 현금흐름: 송배전

- HD현대일렉트릭, LS일렉트릭, 대한전선, GE Vernova
- 수주잔고와 분기 실적이 숫자로 확인되는 구간
- 북미 변압기·배전·케이블은 공급자 우위 지속
- 리스크: 가파른 주가 상승에 따른 밸류에이션 부담

### 5.2 중기 (향후 2년) — 매출 인식 본격화: 발전·냉각

- 두산에너빌리티: 가스터빈 + 체코 원전 매출 인식 시작
- 대한전선: 해저 2공장 가동 (2027)
- Bloom Energy: 백로그 $20B 매출 전환 (고변동)
- 냉각·DC 인프라: 양산 단계 진입
- NuScale: 2030년대를 보는 장기 옵션 (TVA 구속계약 전환 여부가 관건)

---

## 6. 밸류체인 맵 — 종목 배치 요약

```
STAGE 01: 발전                              STAGE 02: 송배전
├─ GE Vernova (글로벌 #1 가스터빈)            ├─ HD현대일렉트릭 (765kV 변압기)
├─ 두산에너빌리티 (가스터빈+원전+SMR)          ├─ LS일렉트릭 (배전 토탈 솔루션)
├─ Siemens Energy (가스터빈 #2)              ├─ 대한전선 (HVDC·해저케이블)
├─ Constellation (기존 원전 PPA)             ├─ 한전·한전기술 (그리드 뿌리)
├─ NuScale (SMR 옵션)                       └─ Eaton (배전·그리드 장비)
└─ Vistra (발전 유틸리티)

STAGE 03: DC 전력 인프라                     STAGE 04: 냉각
├─ Bloom Energy (SOFC 자가발전)              ├─ Vertiv (전력+냉각 원스톱)
├─ Vertiv (UPS·배전·전력관리)                ├─ Schneider (DC 인프라 통합)
├─ LS일렉트릭 (연료전지 배전설비)             ├─ SK엔무브 (액침냉각 유체)
├─ Eaton (800V DC 파워)                     ├─ 삼화콘덴서 (전력반도체)
└─ Schneider (전력 분배)                    └─ 고영테크놀로지 (냉각 검사)
```

---

## 7. 출처 목록

### 기관 리포트
- IEA, *Electricity 2026: Demand* (2026) — [링크](https://www.iea.org/reports/electricity-2026/demand)
- IEA, *Energy and AI: Energy Demand from AI* (Apr 2025) — [링크](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai)
- IEA, *Key Questions on Energy and AI* (Apr 2026) — [링크](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary)
- IEA, *Data Centre Electricity Use Surged in 2025* (Apr 2026) — [링크](https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions)
- IEA, *World Energy Outlook 2025* (2025) — [링크](https://www.iea.org/reports/world-energy-outlook-2025/overview-and-key-findings)
- IEA, *Electricity 2024* (Jan 2024) — [PDF](https://iea.blob.core.windows.net/assets/6b2fd954-2017-408e-bf08-952fdd62118a/Electricity2024-Analysisandforecastto2026.pdf)
- Gartner, *Data Center Electricity Demand to Grow 26% in 2026* (2026-06-10) — [링크](https://www.gartner.com/en/newsroom/press-releases/2026-06-10-gartner-says-data-center-electricity-demand-to-grow-26-percent-in-2026)
- Gartner, *Electricity Demand for Data Centers to Grow 16% in 2025 and Double by 2030* (2025-11-17) — [링크](https://www.gartner.com/en/newsroom/press-releases/2025-11-17-gartner-says-electricity-demand-for-data-centers-to-grow-16-percent-in-2025-and-double-by-2030)
- Goldman Sachs, *Data Center Power Demand: The 6 Ps Driving Growth and Constraints* (Apr 2026) — [링크](https://www.goldmansachs.com/insights/goldman-sachs-research/data-center-power-demand-the-6-ps-driving-growth-and-constraints)
- DOE/LBNL, *US Data Center Energy Usage Report* (Dec 2024) — [링크](https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers)
- McKinsey, *AI's Power Binge* (2025) — [링크](https://www.mckinsey.com/featured-insights/week-in-charts/ais-power-binge)
- Morgan Stanley, *Powering AI: Markets Race to Invest in AI Energy Solutions* (2026)
- Morgan Stanley, *AI Market Trends 2026: Global Investment, Risks, and Buildout* (2026)
- SemiAnalysis, *AI Datacenter Energy Dilemma* (2024–2026 연속)
- Bloom Energy, *2026 Data Center Power Report: Mid-Year Pulse* (2026-06)

### 산업 분석
- Wood Mackenzie (변압기 공급 부족 분석)
- AFCOM, *State of the Data Center Report 2026* (랙 밀도)
- WRI, *Powering the US Data Center Boom* (2025) — [링크](https://www.wri.org/insights/us-data-centers-electricity-demand)
- Data Center Watch (모라토리엄·커뮤니티 반대 데이터)
- Data Center Frontier — [링크](https://www.datacenterfrontier.com/energy/article/33038469/iea-study-sees-ai-cryptocurrency-doubling-data-center-energy-consumption-by-2026)
- Power Magazine, *Transformers in 2026: Shortage, Scramble, or Self-Inflicted Crisis?*
- IEEE Spectrum (800VDC, 변압기 부족)
- TrendForce (HVDC 시프트)
- S&P Global, *Data Center Power Demand to Double by 2030* — [링크](https://www.spglobal.com/energy/en/news-research/latest-news/electric-power/041025-global-data-center-power-demand-to-double-by-2030-on-ai-surge-iea)

### 기업 공시
- GE Vernova 1Q26 8-K (SEC)
- Siemens Energy Q1 FY26 실적 (Bloomberg)
- Vertiv 1Q26 8-K (SEC)
- Eaton Q1 2026 실적 (BusinessWire)
- Schneider Electric Q1 2026 (Investing.com)
- NuScale Power 1Q26 8-K (SEC)
- 두산에너빌리티 — Seoul Economic Daily, TechTimes 보도

### 기존 참조 메모
- `data/note-ai-money-flow_20260618.md` — 투자 프레임워크 (병목/해자/비대칭성)
- `data/note-ai-power-infra-update_20260618.md` — 기존 페이지 업데이트 이력

---

## 8. 향후 과제 (다음 리서치 파일에서)

- [ ] `research_ai_power_part3_investment.md`: 16개+ 종목 크로스 밸류에이션, 멀티플 비교, 포트폴리오
- [ ] `research_ai_power_companies_kr.md`: 한국 기업 재무 심화 (DART 기반)
- [ ] `research_ai_power_companies_global.md`: GEV·Constellation·Vistra·Vertiv·Bloom·Eaton·Schneider 재무
- [ ] `research_ai_power_themes_AB.md`: SMR/원전 르네상스 + 가스터빈 슈퍼사이클 심화
- [ ] `research_ai_power_themes_CD.md`: 송배전 병목 + DC 전력/냉각 전환 심화
