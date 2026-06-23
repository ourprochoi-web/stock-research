# AI 밸류체인 "돈의 흐름" 종합 분석 프레임워크

> **목적**: 빅테크 CapEx에서 출발해 AI 밸류체인 5개 구간으로 자금이 흘러가는 구조를 분석하고, 기존 7개 리서치 시리즈(AI 전력, HBM/패키징, K-방산, AI 바이오, 로봇/휴머노이드, 우주 경제, AI SW)의 50+ 종목을 밸류체인에 크로스 매핑한 투자 프레임워크
> **작성일**: 2026-06-23
> **데이터 기준**: FY Q1 2026~Q1 FY2027 실적(2026년 4~6월 발표분), 2026년 6월 현재 밸류에이션
> **출처 유형**: SEC 공시(8-K, 10-Q), 기업 IR/어닝콜, IEA, Gartner, Morgan Stanley, Goldman Sachs, TrendForce, Precedence Research, UNCTAD, 각사 애널리스트 리포트
> **면책**: 본 문서는 투자 권유가 아닌 정보 제공 목적이며, 투자 결정은 독자 본인의 책임입니다. 수치는 발표 시점·환율·집계 방법에 따라 차이가 있을 수 있습니다.

---

## 목차

1. [AI 밸류체인 탑다운 구조 — 빅테크 CapEx에서 5개 구간으로](#1-ai-밸류체인-탑다운-구조)
2. [빅테크 CapEx: $7,250억 시대](#2-빅테크-capex)
3. [구간 1 — GPU/가속기: 돈의 첫 번째 종착지](#3-구간-1--gpu가속기)
4. [구간 2 — 메모리(HBM): BOM 30%의 힘](#4-구간-2--메모리hbm)
5. [구간 3 — 패키징/공정: 절대 병목](#5-구간-3--패키징공정)
6. [구간 4 — DC 인프라: 전력·냉각·송배전](#6-구간-4--dc-인프라)
7. [구간 5 — SW/서비스: 최종 소비 계층](#7-구간-5--sw서비스)
8. [구간별 마진 구조 비교](#8-구간별-마진-구조-비교)
9. [병목 포인트 랭킹](#9-병목-포인트-랭킹)
10. [7개 시리즈 기업 크로스맵 — 50+ 종목 밸류체인 배치](#10-7개-시리즈-기업-크로스맵)
11. [TAM 성장률 + 소버린 AI 중복투자 효과](#11-tam-성장률--소버린-ai-중복투자-효과)
12. [닷컴 버블 vs 현재 AI 사이클: 질적 차이](#12-닷컴-버블-vs-현재-ai-사이클)
13. [투자처를 찾는 3대 조건](#13-투자처를-찾는-3대-조건)
14. [투자 시사점](#14-투자-시사점)
15. [출처 및 참고 자료](#15-출처-및-참고-자료)

---

## 1. AI 밸류체인 탑다운 구조

### 1.1 자금의 흐름: 빅테크에서 최종 서비스까지

AI 밸류체인은 **하이퍼스케일러(빅테크)의 CapEx**에서 시작하여, 5개 구간을 거쳐 최종 소비자에게 도달하는 단방향 자금 흐름이다. 각 구간은 독립적이면서도 직렬(serial)로 연결되어 있어, **하나의 병목이 전체 체인의 속도를 결정**한다.

```
┌─────────────────────────────────────────────────────────────────┐
│                   빅테크 CapEx ($7,250억+ / 2026)                │
│       Microsoft · Google · Amazon · Meta · Oracle · etc.        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  구간 1: GPU/가속기                                               │
│  NVIDIA (GPU) · Broadcom (ASIC) · AMD · Intel                    │
│  FY27 Q1 NVIDIA DC 매출: $752억 (+92% YoY)                       │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  구간 2: 메모리 (HBM/DRAM/NAND)                                  │
│  SK하이닉스 · Samsung · Micron                                    │
│  GPU BOM의 ~30%가 HBM — 역대 최고 비중                             │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  구간 3: 패키징/공정                                               │
│  TSMC (CoWoS) · ASE/SPIL · 한미반도체 · HPSP                      │
│  CoWoS 수급갭: 20% → 10% (2026 말), 리드타임 52~78주               │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  구간 4: DC 인프라 (전력·냉각·송배전)                                │
│  GE Vernova · Vertiv · Eaton · Schneider · Bloom Energy           │
│  글로벌 DC 전력: 415 TWh(2024) → 1,200+ TWh(2030E)                │
└──────────────────────────┬───────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│  구간 5: SW/서비스 (최종 소비)                                      │
│  Microsoft · Palantir · ServiceNow · CrowdStrike                  │
│  AI 에이전틱 서비스 → B2B/B2C 추론 기반 수익화                        │
└──────────────────────────────────────────────────────────────────┘
```

### 1.2 핵심 원리: 직렬 구조의 의미

- **직렬 병목**: 5개 구간이 순차적으로 연결되어 있으므로, 가장 느린 구간이 전체 처리량을 결정. 현재 최대 병목은 **구간 3(CoWoS 패키징)**
- **마진 집중**: 병목 구간일수록 공급자의 가격 협상력이 강해져 마진이 높음. NVIDIA GPM 75%, SK하이닉스 OPM 72%, TSMC GM 59%
- **투자 시차**: 빅테크 CapEx 집행 → 구간 1~3 매출 인식(3~6개월) → 구간 4 매출 인식(6~18개월) → 구간 5 매출 인식(12~36개월)

---

## 2. 빅테크 CapEx

### 2.1 2026년 하이퍼스케일러 CapEx 전망

빅테크 4사(Microsoft, Google, Amazon, Meta)의 2026년 합산 CapEx는 **$7,250억**으로, 전년 대비 +77% 급증한다. 오라클, Apple, Tesla 등 기타 사업자를 포함하면 **$8,000억 이상**으로 추정된다.

| 기업 | 2025 CapEx | 2026E CapEx | YoY | 주요 투자처 |
|------|-----------|-------------|-----|-----------|
| Amazon (AWS) | ~$78B | **~$200B** | +156% | Custom Trainium, DC 건설 |
| Microsoft | ~$80B | **~$190B** | +138% | Azure AI, OpenAI 파트너십 |
| Alphabet (Google) | ~$75B | **$175~185B** | +133% | TPU, Gemini 학습 인프라 |
| Meta | ~$38B | **$115~135B** | +230% | Llama 학습, NVIDIA GPU |
| **4사 합계** | **~$271B** | **~$725B** | **+168%** | |
| Oracle + 기타 | ~$40B+ | ~$80B+ | — | Stargate 프로젝트 포함 |
| **전체 추정** | **~$310B+** | **~$800B+** | — | |

출처: [Statista — Big Tech CapEx $725B in 2026](https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/); [Tom's Hardware — $725B up 77%](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion); [CNBC — Tech AI spending approaches $700B](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html); [Value Add VC](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once)

### 2.2 장기 전망

| 지표 | 수치 | 출처 |
|------|------|------|
| 4사 누적 CapEx (FY2025~2030) | **$5.3T** | Goldman Sachs |
| 글로벌 AI 인프라 누적 투자 (by 2028) | **~$3T** (80%+ 미집행) | Morgan Stanley |
| 2025년 DC 투자 | $580B (글로벌 석유투자 $540B 초과) | IEA |
| AI 인프라 파이낸싱 갭 | $1.5T | Morgan Stanley |
| Stargate 프로젝트 | $500B / 4년, 1GW급 DC 5개 | OpenAI · SoftBank |

### 2.3 CapEx 재원의 건전성

현재 빅테크의 AI 투자가 닷컴 시대와 근본적으로 다른 이유:

| 비교 항목 | 닷컴 (2000) | 현재 빅테크 (2026) |
|----------|------------|------------------|
| 부채비율 | 매우 높음 (통신사 100%+) | **~20%** 내외 |
| 현금 창출 | 대부분 적자 | **막대한 영업CF** (Alphabet $120B+/yr) |
| 투자 주체 수익성 | 매출 없는 기업 다수 | 세계 최고 수익성 기업들 |
| CapEx 대비 FCF | 적자 | 양(+)의 FCF 유지 |

---

## 3. 구간 1 — GPU/가속기

### 3.1 NVIDIA: 독주 체제의 규모

NVIDIA는 AI 가속기 시장의 사실상 독점자로서, 빅테크 CapEx의 **첫 번째 종착지**이다.

| 지표 | 수치 | 기간/출처 |
|------|------|----------|
| Q1 FY27 매출 | **$81.6B** (+85% YoY) | 2026.04 분기, NVIDIA 8-K |
| Q1 FY27 데이터센터 매출 | **$75.2B** (+92% YoY) | NVIDIA 8-K |
| FY26 연간 매출 | **$215.9B** (+65% YoY) | FY26 전체 (2025.02~2026.01) |
| GPM (Non-GAAP) | **75.0%** | Q1 FY27 |
| 시가총액 | ~$3.6T | 2026.06 기준 |

출처: [NVIDIA Q1 FY2027 실적](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027); [TweakTown](https://www.tweaktown.com/news/111734/nvidias-record-data-center-revenue-for-fiscal-q1-2027-beat-estimates-as-the-ai-boom-continues/index.html)

### 3.2 Broadcom: ASIC의 부상

빅테크가 NVIDIA 의존도를 줄이기 위해 **커스텀 ASIC** 수요를 확대하면서, Broadcom이 두 번째 수혜자로 부상하고 있다.

| 지표 | 수치 | 기간/출처 |
|------|------|----------|
| Q2 FY26 AI 반도체 매출 | **$10.8B** (+143% YoY) | Broadcom 8-K |
| Q1 FY26 AI 반도체 매출 | $8.4B (+106% YoY) | Broadcom 8-K |
| FY26 AI 반도체 매출 가이던스 | **~$56B** (+180% YoY) | CEO Hock Tan |
| Q3 FY26 매출 가이던스 | $29.4B (+84% YoY) | Broadcom 8-K |

출처: [TechTimes — Broadcom $56B forecast](https://www.techtimes.com/articles/317846/20260605/nvidia-not-only-ai-chip-winner-broadcom-forecasts-56-billion-custom-silicon-demand-surges.htm); [tech-insider.org — AI Revenue $10.8B](https://tech-insider.org/broadcom-q2-2026-earnings-ai-revenue/)

### 3.3 GPU/가속기 구간 투자 키포인트

- **NVIDIA 생태계 해자**: CUDA 개발자 400만+, 소프트웨어 전환 비용이 ASIC 대비 압도적
- **ASIC vs GPU**: 빅테크 자체 칩(Google TPU, Amazon Trainium, Meta MTIA) 비중 증가, 그러나 범용성에서 NVIDIA GPU에 미달
- **Blackwell → Rubin 로드맵**: 2026 Blackwell 300 (B300) → 2027 Rubin (R100, HBM4 탑재) → 2028 Rubin Ultra (HBM4E)
- **중국 차단**: Q1 FY27에 중국향 Hopper 제품 출하량 $0 (전년 동기 $46억) — 미국 수출통제 영향

---

## 4. 구간 2 — 메모리(HBM)

### 4.1 GPU BOM 구조의 변화

AI 가속기에서 HBM이 차지하는 비중이 **전례 없이 폭증**하고 있다. 과거 데이터센터 비용의 ~10%에 불과했던 메모리가, Blackwell·Rubin 아키텍처로 가면서 **BOM의 ~30%**까지 급등했다.

### 4.2 HBM 시장 규모 전망

| 연도 | HBM 매출 | 출처 | YoY |
|------|---------|------|-----|
| 2024 (실적) | ~$20B | TrendForce | — |
| 2025E | ~$35B | BNP Paribas / Yole | +75% |
| 2026E | $60~76B | BNP Paribas / 업계 | +70~117% |
| 2027E | ~$156B | BNP Paribas (광의) | +105% |
| 2030E | ~$98B | Yole Group (협의) | CAGR 33% |

> 전망사 간 편차 주의: BNP Paribas는 HBM 모듈+관련 DRAM 매출 광의 포함, Yole/Precedence는 HBM 제품 매출만 산정. 본 프레임워크에서는 **Yole 기준(CAGR 33%)**을 기본 전제로 사용

### 4.3 핵심 기업

| 기업 | 글로벌 HBM M/S | Q1'26 핵심 지표 | 해자 |
|------|---------------|----------------|------|
| **SK하이닉스** | 57~58% | 매출 ₩52.6T, OPM **72%**, 순이익률 77% | HBM3E 수율 1위, NVIDIA 1차 공급 |
| **삼성전자** | ~22% | HBM3E 양산 + HBM4E 업계 최초 샘플 출하 | 파운드리+메모리 수직 통합 |
| **Micron** | ~20% | HBM3E 8-Hi 양산, HBM4 2027 목표 | 미국 유일 HBM 공급사, CHIPS Act 수혜 |

### 4.4 HBM 세대별 로드맵

| 세대 | 대역폭 | 양산 시점 | 탑재 칩 |
|------|--------|----------|--------|
| HBM3E | 1.2 TB/s | 양산 중 | H200, B200, GB200 |
| **HBM4** | 2+ TB/s | **2026.02 양산** | Rubin (R100) |
| **HBM4E** | ~4 TB/s | **2026.05~06 샘플** | Rubin Ultra |
| HBM5 | TBD | 2028E | 차세대 |

- HBM4 ASP는 HBM3E 대비 **30%+ 프리미엄** → 전체 매출 믹스 개선
- SK하이닉스 경영진: "향후 3년간 HBM 수요 > 생산능력" 재확인

---

## 5. 구간 3 — 패키징/공정

### 5.1 CoWoS: AI 밸류체인의 절대 병목

TSMC의 CoWoS(Chip-on-Wafer-on-Substrate)는 AI 칩 공급망에서 **가장 좁은 목(bottleneck)**이다. 실리콘 팹이 아니라 **패키징이 AI 칩 공급의 바인딩 제약조건**이다.

| 지표 | 수치 | 출처 |
|------|------|------|
| CoWoS CAPA (2024) | 35K WPM | TrendForce |
| CoWoS CAPA (2026 말 목표) | **120~130K WPM** | TrendForce |
| CoWoS CAPA (2027 목표) | 170K WPM | TrendForce |
| CAPA CAGR (2022~2027) | **80%+** | TSMC |
| 수급갭 (2026 초) | **20%** | TrendForce |
| 수급갭 (2026 말) | **~10%** | TrendForce |
| 리드타임 | **52~78주** (1~1.5년) | 업계 |
| NVIDIA CoWoS 예약 비중 | **50%+** (2026 할당) | SiliconAnalysts |
| Wafer ASP | **~$17,000~20,000** (7nm 수준) | TrendForce |

출처: [TrendForce — CoWoS gap narrowing](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/); [Oplexa — AI Chip Packaging Bottleneck](https://oplexa.com/ai-chip-packaging-bottleneck-2026/)

### 5.2 TSMC 실적

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **~$35B** (+40.6% YoY) | TSMC 6-K |
| FY26 매출 성장 가이던스 | +30%+ YoY (USD) | TSMC 어닝콜 |
| Q1'26 GM | ~59% | TSMC 6-K |
| FY26 CAPEX | **$52~56B** | TSMC 어닝콜 |
| 첨단 패키징 매출 비중 | ~8%(2025) → **10%+(2026E)** | TSMC |

### 5.3 CoPoS: 차세대 패키징

| 일정 | 내용 |
|------|------|
| 2026 H1 | CoPoS 파일럿 라인 완공 |
| 2027 | 파일럿 생산 |
| 2028 H2 | **양산 개시** 목표 |
| 특징 | 310x310mm 패널, 웨이퍼 활용률 90%+, 비용 30% 절감 |

### 5.4 한국 패키징 밸류체인

| 기업 | 역할 | 핵심 해자 |
|------|------|----------|
| **한미반도체** | TC 본딩 장비 | 글로벌 M/S **71.2%** |
| **HPSP** | 고압수소 어닐링 | **세계 유일** 고압수소 어닐링 장비 공급 |
| **삼성전기** | FC-BGA 기판 + MLCC | 글로벌 유일 기판·MLCC 동시 공급 |
| **리노공업** | 포고핀 테스트 소켓 | 글로벌 M/S **30%+** |
| **테크윙** | 반도체 핸들러 | HBM 테스트 전용 핸들러 |
| **ISC** | 러버 소켓 | HBM 테스트용 소켓 |
| **한화세미텍** | 와이어본더/TC본더 | 후발 진입, CAPA 확장 중 |

---

## 6. 구간 4 — DC 인프라

### 6.1 전력 수요의 폭발

AI 데이터센터의 전력 소비는 모든 전망사가 상향 조정하는 중이다.

| 연도 | 글로벌 DC 전력 (TWh) | 출처 |
|------|---------------------|------|
| 2024 (실적) | 415 | IEA |
| 2025 | 447~485 | Gartner / IEA |
| 2026E | 565 | Gartner |
| 2030E (IEA Base) | ~950 | IEA |
| 2030E (Gartner) | **>1,200** | Gartner (7개월 만에 22% 상향) |
| 2030E (Goldman Sachs) | 1,350 | Goldman Sachs |
| 2035E (IEA Lift-Off) | >1,700 | IEA |

- **랙 밀도**: 평균 7kW(2021) → 16kW(2025) → **27kW(2026)** — AFCOM 10년 추적 사상 최대 YoY 증가
- **AI 전용 랙**: GB200 NVL72 기준 **130~132kW/rack**, 차세대 ~300kW, 궁극적 ~1MW
- **액체냉각 도입률**: 19%(2025) → **36%(2026)**

### 6.2 글로벌 핵심 기업

| 기업 | 포지션 | Q1'26 핵심 | 마진 프로필 |
|------|--------|-----------|-----------|
| **GE Vernova** | 가스터빈 + 전력화 | 매출 $9.3B (+16%), 수주 $18.3B (+71%), 백로그 **$163B** | EBITDA 9.6% |
| **Constellation Energy** | 원전 + PPA | AI DC향 원전 PPA 확대 | OPM ~20%+ |
| **Vistra** | 발전 + 소매 | 가스/원전 포트폴리오 | OPM ~15% |
| **Vertiv** | 전력관리/냉각 | DC 열관리 + 전원 공급 장치 | OPM ~17% |
| **Bloom Energy** | SOFC 연료전지 | Q1'26 매출 +130% YoY, 파이프라인 **4GW** | 흑자 전환 진행 |
| **Eaton** | 전력 배전 | 데이터센터 + 유틸리티 | OPM ~22% |
| **Schneider Electric** | 전력 + 자동화 | DC 인프라 토탈 솔루션 | OPM ~18% |

### 6.3 한국 전력 인프라 기업

| 기업 | 밸류체인 단계 | 핵심 모멘텀 |
|------|------------|-----------|
| **두산에너빌리티** | 발전 (가스터빈/원전) | xAI 7기 1.2조 수주, 수주잔고 24.1조, 가스터빈 105기 로드맵 |
| **HD현대일렉트릭** | 송배전 | 765kV 글로벌 과점, OPM **24.9%**, 수주잔고 급증 |
| **LS일렉트릭** | 초고압+DC | 북미 매출 +80%, DC 전력기기 투트랙 |
| **한전 (KEPCO)** | 그리드 | 2025 영업익 13.5조 사상최대, but 부채 205조 |
| **대한전선** | 케이블 | HVDC 해저케이블, 당진 2공장 |
| **SK엔무브** | 냉각 (액침냉각유) | 3M 철수 후 시장 공백 선점 |

### 6.4 투자 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| 2025 글로벌 DC 투자 | **$580B** (석유투자 $540B 초과) | IEA |
| DC 투자 슈퍼사이클 | ~$3T by 2030 | JLL |
| US 유틸리티 그리드 투자 | $1.4T / 5년 | Morgan Stanley |
| US DC 수요-공급 부족 | 49 GW 부족 (2028) | Morgan Stanley |
| 글로벌 DC 전력 용량 | 104GW(2025) → **290GW(2030)** | Gartner |

---

## 7. 구간 5 — SW/서비스

### 7.1 최종 소비 계층

빅테크 CapEx가 만들어낸 AI 인프라 위에서, **소프트웨어·플랫폼·서비스 기업**이 최종 수익화를 수행한다. 이 구간은 인프라 구간 대비 **시간차(12~36개월)**가 존재하지만, 일단 수익화가 시작되면 **리커링(recurring) 매출 + 높은 GPM**이 특징이다.

### 7.2 핵심 기업

| 기업 | 포지션 | 최신 실적 | AI 매출 모멘텀 |
|------|--------|----------|--------------|
| **Microsoft** | Azure AI + Copilot | 2026 CapEx ~$190B | Azure AI 매출 YoY +60%+ |
| **Palantir** | AI 플랫폼 (AIP) | FY25 매출 $4.5B (+56%), FY26E $7.65B (상향) | 순달러유지율 139% |
| **ServiceNow** | 워크플로 AI (Now Assist) | Q1'26 구독 매출 $3,671M (+22%) | Now Assist ACV $1B 트래킹 |
| **CrowdStrike** | AI 사이버보안 | FY26 매출 $4.8B (+22%) | Falcon AI 위협 감지 자동화 |

출처: [Yahoo Finance — Palantir vs CrowdStrike](https://finance.yahoo.com/markets/stocks/articles/palantir-vs-crowdstrike-ai-powered-132000200.html); [SEC — ServiceNow Q1 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm)

### 7.3 AI SW 구간의 특성

| 항목 | 특징 |
|------|------|
| **매출 인식 시차** | 인프라 투자 후 12~36개월 뒤 본격 매출화 |
| **마진 구조** | GPM 70~85% (SW 특성), OPM 20~40% |
| **밸류에이션** | Forward P/E 40~100x+ (성장 프리미엄) |
| **리스크** | AI CapEx 사이클 둔화 시 수요 감소, 경쟁 심화 |
| **수익화 모델** | SaaS 구독, 사용량 기반(consumption), 에이전틱 과금 |

---

## 8. 구간별 마진 구조 비교

### 8.1 GPM(매출총이익률) 비교 — 병목 = 높은 마진

| 구간 | 대표 기업 | GPM | OPM | 핵심 드라이버 |
|------|----------|-----|-----|-------------|
| **1. GPU/가속기** | NVIDIA | **75.0%** | ~60% | CUDA 생태계 독점, 공급 < 수요 |
| **1. GPU/가속기** | Broadcom (AI 반도체) | ~65% | ~35% | 커스텀 ASIC 장기 계약 |
| **2. 메모리** | SK하이닉스 | ~55% | **72%** | HBM 프리미엄, 공급자 3사 과점 |
| **3. 패키징** | TSMC | **~59%** | ~49% | CoWoS 독점 + 첨단 공정 |
| **3. 패키징** | 한미반도체 | ~55% | ~45% | TC 본딩 M/S 71% |
| **4. DC 인프라** | GE Vernova | ~30% | ~10% | 가스터빈 슈퍼사이클 |
| **4. DC 인프라** | HD현대일렉트릭 | ~37% | **~25%** | 초고압 변압기 과점 |
| **4. DC 인프라** | Vertiv | ~38% | ~17% | 전력관리 + 냉각 |
| **5. SW/서비스** | Palantir | **~82%** | ~16% | AI 플랫폼 리커링 |
| **5. SW/서비스** | ServiceNow | **~80%** | ~30% | 워크플로 SaaS |
| **5. SW/서비스** | CrowdStrike | **~76%** | ~22% | AI 기반 보안 SaaS |

### 8.2 마진 해석

```
GPM 순위: SW/서비스(76~82%) > GPU(65~75%) > 패키징/메모리(55~59%) > DC 인프라(30~38%)
OPM 순위: SK하이닉스(72%) > NVIDIA(~60%) > TSMC(~49%) > ServiceNow(~30%) > HD현대일렉트릭(~25%)
```

- **GPU와 메모리**: 병목 + 과점 구조 → 가격 결정력 → 초고마진
- **DC 인프라**: GPM은 상대적으로 낮으나, **수주 백로그의 가시성이 극도로 높음** (GE Vernova $163B)
- **SW/서비스**: GPM은 최고이나, **OPM은 R&D/SGA 부담**으로 GPU/메모리보다 낮음. 스케일 도달 시 레버리지 극대화

---

## 9. 병목 포인트 랭킹

### 9.1 병목 심각도 순위 (2026년 6월 기준)

병목 구간에 투자하라는 것이 프레임워크의 핵심이다. **공급이 수요를 못 따라가는 구간에 돈이 몰리고, 해당 구간의 공급자에게 가격 결정력이 생긴다.**

| 순위 | 병목 구간 | 수급갭 | 리드타임 | 해소 시점 | 핵심 기업 |
|------|----------|--------|---------|----------|----------|
| **1** | **CoWoS 패키징** | 20%→10% (연말) | **52~78주** | 2028+ (CoPoS) | TSMC, 한미반도체, HPSP |
| **2** | **HBM 메모리** | 수요 > 공급 3년+ | 양산 리드 12~18개월 | 2028+ | SK하이닉스, 삼성, Micron |
| **3** | **전력 인프라** | US 49GW 부족(2028) | 변압기 36~60개월 | 2029+ | GE Vernova, HD현대일렉트릭 |
| **4** | **GPU 로직** | 물량 배정 경쟁 | 20~30주 | 상시 갱신 | NVIDIA, TSMC |
| **5** | **냉각 시스템** | 40% 불충분 인식 | 12~24개월 | 2027+ | Vertiv, SK엔무브 |

### 9.2 병목 심화의 구조적 원인

1. **CoWoS**: 웨이퍼가 아니라 **패키징 공정**이 바인딩 제약. TSMC가 CAPA를 4배 확장해도 수급갭 해소 불가
2. **HBM**: 공급사 3곳뿐 (SK하이닉스/삼성/Micron). CAPA 확장에 **1.5~2년** 소요
3. **전력**: 변압기 납기 **3~5년**. US 그리드 인프라가 1960~70년대 건설 이후 노후화
4. **소버린 AI**: 국가별 중복 투자가 동일 병목 구간에 추가 수요 누적

---

## 10. 7개 시리즈 기업 크로스맵

### 10.1 전체 밸류체인 배치 — 50+ 종목

기존 7개 리서치 시리즈의 핵심 종목을 AI 밸류체인 5개 구간 + 확장 영역에 크로스 매핑한다.

#### 구간 1: GPU/가속기

| 기업 | 시리즈 | 포지션 | 비고 |
|------|--------|--------|------|
| NVIDIA (NVDA) | AI SW/인프라 | GPU 독점, CUDA 생태계 | 시총 ~$3.6T |
| Broadcom (AVGO) | AI SW/인프라 | 커스텀 ASIC + 네트워킹 | FY26E AI 매출 $56B |
| AMD (AMD) | — | MI300X/MI350 GPU | NVIDIA 대비 SW 생태계 열위 |

#### 구간 2: 메모리 (HBM/DRAM)

| 기업 | 시리즈 | 포지션 | 비고 |
|------|--------|--------|------|
| **SK하이닉스** (000660) | HBM/패키징 | HBM M/S **57%**, OPM 72% | Q1'26 매출 ₩52.6T |
| **삼성전자** (005930) | HBM/패키징 | HBM M/S ~22%, HBM4E 최초 샘플 | 파운드리+메모리 수직통합 |
| Micron (MU) | HBM/패키징 | 미국 유일 HBM 공급사 | CHIPS Act $6.1B 수혜 |

#### 구간 3: 패키징/공정

| 기업 | 시리즈 | 포지션 | 비고 |
|------|--------|--------|------|
| TSMC (TSM) | HBM/패키징 | CoWoS 독점, 첨단 패키징 | 시총 ~$1.1T |
| **한미반도체** (042700) | HBM/패키징 | TC 본딩 장비 M/S **71.2%** | 글로벌 1위 |
| **HPSP** (403870) | HBM/패키징 | 고압수소 어닐링 **세계 유일** | 독점적 해자 |
| **리노공업** (058470) | HBM/패키징 | 포고핀 소켓 M/S 30%+ | HBM 테스트 필수 |
| **삼성전기** (009150) | HBM/패키징 | FC-BGA + MLCC + 실리콘커패시터 | 모듈 원팩 공급 잠재력 |
| ASE/SPIL (3711.TW) | HBM/패키징 | OSAT 1위, CoWoS 외주 | TSMC 보완 |
| Amkor (AMKR) | HBM/패키징 | OSAT 2위, 첨단 패키징 | 미국 내 CAPA 확장 |
| BESI (BESI.AS) | HBM/패키징 | 하이브리드 본딩 장비 | 차세대 본딩 기술 |
| Advantest (6857.T) | HBM/패키징 | 반도체 테스터 글로벌 1위 | HBM 테스트 수요 급증 |
| Disco (6146.T) | HBM/패키징 | 다이싱/그라인딩 1위 | HBM 웨이퍼 박화 필수 |
| Applied Materials (AMAT) | HBM/패키징 | 반도체 장비 1위 | CoWoS 장비 공급 |
| Lam Research (LRCX) | HBM/패키징 | 식각·증착 장비 | TSV 에칭 핵심 |
| **테크윙** (089030) | HBM/패키징 | HBM 전용 핸들러 | 검증 장비 |
| **ISC** (095340) | HBM/패키징 | 러버 소켓 | HBM 테스트용 |
| **한화세미텍** (272420) | HBM/패키징 | 와이어본더/TC본더 | 후발 진입 |
| Unimicron (3037.TW) | HBM/패키징 | ABF 기판 | 글로벌 1위 |
| Ibiden (4062.T) | HBM/패키징 | ABF 기판 | 글로벌 2위 |

#### 구간 4: DC 인프라 (전력·냉각·송배전)

| 기업 | 시리즈 | 포지션 | 비고 |
|------|--------|--------|------|
| **GE Vernova** (GEV) | AI 전력 | 가스터빈 + 전력화 | 백로그 $163B |
| **Constellation Energy** (CEG) | AI 전력 | 원전 PPA | AI DC향 원전 전력 |
| **Vistra** (VST) | AI 전력 | 가스/원전 발전 | 발전 포트폴리오 |
| **Vertiv** (VRT) | AI 전력 | 전력관리 + 냉각 | DC 열관리 토탈 |
| **Bloom Energy** (BE) | AI 전력 | SOFC 연료전지 | 파이프라인 4GW, 매출 +130% |
| **Eaton** (ETN) | AI 전력 | 전력 배전 장비 | DC + 유틸리티 |
| **Schneider Electric** (SU.PA) | AI 전력 | 전력 + 자동화 | DC 토탈 솔루션 |
| **두산에너빌리티** (034020) | AI 전력 | 가스터빈/원전 | xAI 7기 수주, 잔고 24.1조 |
| **HD현대일렉트릭** (267260) | AI 전력 | 초고압 변압기 | OPM 24.9%, 765kV 과점 |
| **LS일렉트릭** (010120) | AI 전력 | 초고압 + DC 전력기기 | 북미 +80% |
| **대한전선** (001440) | AI 전력 | HVDC 케이블 | 당진 2공장 |
| **한전 (KEPCO)** (015760) | AI 전력 | 그리드 운영 | 영업익 13.5조, 부채 205조 |
| **SK엔무브** | AI 전력 | 액침냉각유 | 3M 철수 후 시장 선점 |

#### 구간 5: SW/서비스

| 기업 | 시리즈 | 포지션 | 비고 |
|------|--------|--------|------|
| **Microsoft** (MSFT) | AI SW | Azure AI + Copilot | 2026 CapEx $190B |
| **Palantir** (PLTR) | AI SW | AI 플랫폼 AIP | FY26E 매출 $7.65B |
| **ServiceNow** (NOW) | AI SW | 워크플로 AI | 구독 매출 +22% |
| **CrowdStrike** (CRWD) | AI SW | AI 사이버보안 | FY26 매출 $4.8B |

#### 확장 영역: AI 수혜 인접 산업

| 기업 | 시리즈 | 포지션 | AI 밸류체인 연결점 |
|------|--------|--------|------------------|
| **한화에어로스페이스** (012450) | K-방산 / 우주 | K9 자주포, 항공엔진, 누리호 | 방산 AI 무인화 + 우주 인프라 |
| **LIG넥스원** (079550) | K-방산 | 정밀유도무기 | AI 유도·자율 무기 체계 |
| **한국항공우주 KAI** (047810) | K-방산 | KF-21, FA-50 | CCA(협력전투기) AI 자율비행 |
| **현대로템** (064350) | K-방산 | K2 전차 | MUM-T 유무인복합 |
| **한화시스템** (272210) | K-방산 / 우주 | C4ISR, 레이더 | 전장 AI, 위성통신 |
| **한화오션** (042660) | K-방산 | 함정·잠수함 | 자율 무인잠수함 |
| **풍산** (103140) | K-방산 | 탄약 | 스마트 탄약 AI 유도 |
| Recursion (RXRX) | AI 바이오 | AI 신약 발굴 | AI 모델 학습 → DC 수요 |
| Tempus AI (TEM) | AI 바이오 | 정밀의료 AI | 의료 데이터 + AI 추론 |
| **루닛** (328130) | AI 바이오 | AI 의료영상 | 인퍼런스 서비스 |
| **뷰노** (338220) | AI 바이오 | AI 진단 | 의료 AI SaaS |
| **삼성바이오로직스** (207940) | AI 바이오 | CDMO | AI 기반 공정 최적화 |
| **셀트리온** (068270) | AI 바이오 | 바이오시밀러 | AI 분자 설계 활용 |
| Tesla (TSLA) | 로봇 | Optimus 휴머노이드 | AI 학습 인프라 $25B CapEx |
| Figure AI (비상장) | 로봇 | 범용 휴머노이드 | OpenAI 기반 multimodal |
| **레인보우로보틱스** (277810) | 로봇 | 휴머노이드 RB-Y1 | 삼성 지분투자 |
| **두산로보틱스** (454910) | 로봇 | 협동 로봇 | 제조 자동화 |
| **뉴로메카** (348340) | 로봇 | 협동 로봇 | AI 비전 통합 |
| SpaceX (비상장) | 우주 | Starlink + Starship | DC 위성 백홀, 발사 $100/kg 목표 |
| Rocket Lab (RKLB) | 우주 | 소형 발사체 + 우주시스템 | Neutron 2026 Q4 첫 비행 |
| **이노스페이스** (462350) | 우주 | 소형 발사체 | 한국 민간 발사 1호 |
| **쎄트렉아이** (099320) | 우주 | 위성 제조 | 지구관측 위성 |
| **AP위성** (211270) | 우주 | 위성통신 장비 | 방산 + 해양 위성통신 |

### 10.2 크로스맵 요약 — 구간별 종목 수

| 구간 | 글로벌 | 한국 | 합계 |
|------|--------|------|------|
| 1. GPU/가속기 | 3 | 0 | 3 |
| 2. 메모리 | 1 | 2 | 3 |
| 3. 패키징/공정 | 9 | 7 | 16 |
| 4. DC 인프라 | 7 | 6 | 13 |
| 5. SW/서비스 | 4 | 0 | 4 |
| 확장 (방산/바이오/로봇/우주) | 6 | 15 | 21 |
| **합계** | **30** | **30** | **60** |

---

## 11. TAM 성장률 + 소버린 AI 중복투자 효과

### 11.1 AI TAM 전망

글로벌 AI 시장은 매년 약 **18~20% CAGR**로 성장하여, 2035년에는 **$4조 이상**에 도달할 전망이다.

| 연도 | AI 시장 규모 | CAGR | 출처 |
|------|-------------|------|------|
| 2025 (실적) | ~$758B | — | Precedence Research |
| 2026E | $1.1~1.2T | +44% YoY | Gartner |
| 2030E | $1.2~1.8T | 18~20% | Statista / Precedence |
| 2033E | $4.8T | ~25% | UNCTAD |
| 2035E | **$4,216B** ($4.2T) | 18.7% | Precedence Research |
| 장기 TAM (확장 정의) | **$40T** | — | Morgan Stanley (노동시장 포함) |

출처: [Precedence Research — AI Market $4,216B by 2035](https://www.precedenceresearch.com/artificial-intelligence-market); [UNCTAD — $4.8T by 2033](https://unctad.org/news/ai-market-projected-hit-48-trillion-2033-emerging-dominant-frontier-technology); [Morgan Stanley — $40T](https://www.morganstanley.com/insights/articles/ai-diffusion-tech-roundtable)

### 11.2 소버린 AI — 국가별 중복투자의 낙수효과

**소버린 AI(Sovereign AI)**란 각 국가가 자체 AI 역량(데이터, 모델, 컴퓨팅, 인프라)을 확보하려는 '각자도생' 흐름이다. 이는 글로벌 **중복 투자**를 유발하고, 그 낙수효과는 기술 병목을 쥔 핵심 기업에 귀결된다.

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 소버린 AI 지출 전망 (2026) | **$1,000억+** | 업계 추정 |
| 소버린 클라우드 인프라 (2026) | $800억 (+35.6% YoY) | Gartner |
| 2025 Q3 신규 인프라 프로젝트 | **23건** (세계) | WEF |
| 투자 집중 지역 | 중동·동아시아 (80%+) | CNAS |
| UAE+일본 비중 | 전체 공시 투자의 **2/3** | CNAS |

출처: [CNAS Sovereign AI Index](https://interactives.cnas.org/reports/sovereign-ai-index/); [WEF — Rethinking AI Sovereignty](https://www3.weforum.org/docs/WEF_Rethinking_AI_Sovereignty_Pathways_to_Competitiveness_through_Strategic_Investments_2026.pdf); [TheAIForest — Sovereign AI DC Boom](https://theaiforest.com/sovereign-ai-data-centers-whats-driving-the-2026-boom/)

#### 주요국 소버린 AI 투자

| 국가/지역 | 투자 규모 | 핵심 내용 |
|----------|----------|----------|
| **프랑스** | EUR 1,090억 | Macron 발표, AI 인프라 + France 2030 |
| **EU** | EUR 200억 | AI Gigafactory 프로그램 |
| **캐나다** | C$9.26억 / 5년 | 국가 소버린 컴퓨트 전략 |
| **일본** | 대규모 공적자금 | 국가 AI 인프라 + 국산 모델 개발 |
| **사우디/UAE** | 수백억 달러 | GPU 클러스터 + DC 대규모 건설 |
| **한국** | K-AI 이니셔티브 | GPU 공동구매, AI DC 확충 |

#### 낙수효과 메커니즘

```
국가별 AI 역량 확보 결정
    └→ 자국 DC 건설 (전력 + 냉각 + 변압기 수요 증가)
        └→ GPU 구매 (NVIDIA·Broadcom에 추가 수요)
            └→ HBM 수요 (SK하이닉스·삼성·Micron에 추가 수요)
                └→ 패키징 수요 (TSMC CoWoS에 추가 병목)
                    └→ 동일 병목 기업에 낙수 집중
```

핵심 시사점: 소버린 AI는 **수요의 중복 카운팅**이다. 미국 빅테크 CapEx $7,250억 위에, 각국 정부·국부펀드의 투자가 **추가로** 쌓인다. 이 추가 수요는 새로운 공급사를 만들어내기보다, **기존 병목 기업(NVIDIA, TSMC, SK하이닉스, GE Vernova 등)**에 집중된다.

---

## 12. 닷컴 버블 vs 현재 AI 사이클

### 12.1 공통점

| 항목 | 닷컴 (1998~2000) | AI (2023~2026) |
|------|----------------|----------------|
| 인프라 선행 투자 | 광케이블 $80B+ | DC + GPU $725B+ (2026 단독) |
| "이번엔 다르다" 내러티브 | "인터넷이 모든 것을 바꾼다" | "AI가 모든 것을 바꾼다" |
| 밸류에이션 확장 | Cisco P/E 200x+ | NVIDIA Forward P/E ~41x |
| 시장 참여자 열광 | 개인 투자자 폭증 | AI ETF·밈주 열풍 |

### 12.2 결정적 차이

| 비교 항목 | 닷컴 (2000) | 현재 빅테크 (2026) | 시사점 |
|----------|------------|------------------|--------|
| **부채비율** | 통신사 100%+ | **~20%** | 구조적 파산 리스크 극소 |
| **현금 창출** | 적자 기업 대다수 | Alphabet FCF $120B+/yr | 자체 자금으로 투자 가능 |
| **매출 실체** | 수익 없는 닷컴 기업 | NVIDIA $816억/분기 매출 | 검증된 수요 |
| **투자 대비 매출** | 인프라 과잉 → 수요 부재 | 수요 > 공급 (CoWoS 수급갭) | 공급 부족이 문제 |
| **해자** | 진입장벽 낮음 | CUDA, CoWoS, HBM 과점 | 기술 해자 강력 |
| **주가 고점 P/E** | Cisco 200x, Intel 40x | NVIDIA ~41x (Forward), TSMC ~30x | 상대적으로 합리적 |

### 12.3 위험 요인 (닷컴 유사성)

- **CapEx 대비 AI 매출 정당성**: $7,250억 CapEx가 만들어내는 AI 서비스 매출이 투자를 정당화하는가? → 아직 구간 5(SW/서비스)의 수익화 검증 진행 중
- **밸류에이션 기대감**: Palantir Forward P/E 100x+ 등 일부 AI SW 종목은 닷컴급 밸류에이션
- **CapEx 사이클 둔화 가능성**: 하이퍼스케일러가 ROI 미달 시 투자 속도 조절 → 밸류체인 전체에 충격

---

## 13. 투자처를 찾는 3대 조건

한정된 자금으로 AI 밸류체인에서 우선순위를 정할 때, 반드시 확인해야 할 3가지 조건이다.

### 조건 1: 병목(Bottleneck) 구간인가?

> 공급이 수요를 못 따라가는 구간에 돈이 몰린다.

| 병목 구간 | 해당 기업 | 근거 |
|----------|----------|------|
| CoWoS 패키징 | TSMC, 한미반도체, HPSP | 수급갭 20%, 리드타임 1년+ |
| HBM 메모리 | SK하이닉스, 삼성, Micron | 공급자 3사, 3년간 수요>공급 |
| 전력 인프라 | GE Vernova, HD현대일렉트릭 | 변압기 납기 3~5년 |
| GPU | NVIDIA | Blackwell 물량 배정 경쟁 |

### 조건 2: 독점적 해자(Moat)를 가졌는가?

> 경쟁자가 쉽게 들어올 수 없는 기술·생태계 장벽이 있는가?

| 기업 | 해자 유형 | 설명 |
|------|----------|------|
| NVIDIA | 소프트웨어 생태계 | CUDA 개발자 400만+, 전환 비용 극대 |
| SK하이닉스 | 기술 선행 | HBM3E 수율 1위, NVIDIA 1차 공급사 지위 |
| TSMC | 공정 독점 | CoWoS 유일 양산, 3nm 이하 과점 |
| 한미반도체 | 장비 독점 | TC 본딩 M/S 71.2% |
| HPSP | 기술 독점 | 고압수소 어닐링 **세계 유일** |
| GE Vernova | 규모 + 슬롯 | 가스터빈 백로그 100GW, 2028년까지 슬롯 매진 |

### 조건 3: 비대칭성(Asymmetry) — 하방은 막히고 상방은 열렸는가?

> 하락 리스크보다 상승 여력이 훨씬 큰 구조인가?

| 기업 | 하방 방어 | 상방 여력 |
|------|----------|----------|
| SK하이닉스 | Forward P/E 6.4x, 순현금 W35T | HBM4 프리미엄 + 3년간 수요 초과 |
| 삼성전기 | 글로벌 유일 기판+MLCC 동시 | 패키지 모듈(SiCap+MLCC+FC-BGA) 번들 → 빅테크 공급 |
| 두산에너빌리티 | 수주잔고 24조, xAI 7기 수주 확정 | 가스터빈 105기 로드맵, 외국인 순매수 1위 |
| Bloom Energy | 매출 +130%, 파이프라인 4GW | 온사이트 전원 + 800V DC 레디 듀얼 포지션 |

---

## 14. 투자 시사점

### 14.1 프레임워크 종합

1. **"돈의 흐름을 따라가라"**: 빅테크 CapEx $7,250억이 5개 구간을 통해 흘러내려간다. 투자 의사결정의 출발점은 항상 **빅테크 CapEx 추이**
2. **병목에 베팅하라**: 직렬 연결된 밸류체인에서 가장 좁은 목이 가격 결정력·마진·성장률 모두를 독식한다. 현재 1순위 병목은 **CoWoS 패키징**, 2순위 **HBM**, 3순위 **전력**
3. **해자 검증 후 비대칭성을 확인하라**: 병목이어도 해자 없이 경쟁자가 진입 가능하면 마진이 유지되지 않는다. 해자가 확인된 후, 현재 주가 수준에서 하방/상방 비대칭이 유리한지 점검
4. **소버린 AI가 수요를 중복 카운팅한다**: 빅테크 CapEx 위에 각국 정부 투자가 추가로 쌓인다. 이 중복 수요는 동일 병목 기업에 집중 → 수요 전망 상향 편향
5. **주도주는 쉽게 바뀌지 않는다**: 지금 좋은 주식의 '왜 좋은지'를 철저히 마스터하는 것이 '다음 오를 주식'을 찾는 것보다 우선. AI 트렌드 내에서 주도주 교체는 느림

### 14.2 구간별 투자 타이밍

| 구간 | 현재 단계 | 매출 가시성 | 리스크 |
|------|----------|-----------|--------|
| 1. GPU/가속기 | **피크 성장** 중 | 분기 $816억+ (NVIDIA) | 밸류에이션 프리미엄, ASIC 위협 |
| 2. 메모리 | **슈퍼사이클 진입** | HBM 수요 3년 초과 | 사이클 피크 논쟁 |
| 3. 패키징 | **절대 병목** | CoWoS CAPA 80% CAGR | 2028 CoPoS 리스크 |
| 4. DC 인프라 | **초기 슈퍼사이클** | 백로그 $163B (GEV) | 인허가·지역 반발 |
| 5. SW/서비스 | **수익화 초기** | 구독 매출 +22~56% | AI ROI 증명 필요 |

### 14.3 모니터링 핵심 지표

| 지표 | 의미 | 주기 |
|------|------|------|
| 빅테크 4사 CapEx 가이던스 | 전체 밸류체인 수요의 선행지표 | 분기 |
| CoWoS 수급갭 (%) | 병목 1순위의 해소/심화 | 분기 |
| HBM ASP 추이 | 메모리 사이클 피크 판단 | 분기 |
| DC 전력 용량 (GW) 증감 | 인프라 투자 속도 | 반기 |
| AI SW 기업 NRR/매출 성장률 | 최종 수익화 속도 | 분기 |
| 소버린 AI 신규 프로젝트 수 | 중복 수요 카운팅 | 분기 |

---

## 15. 출처 및 참고 자료

### 기업 공시 및 IR
- NVIDIA Q1 FY2027 실적: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)
- NVIDIA FY2026 연간 실적: [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- Broadcom Q2 FY26: [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm)
- Broadcom Q1 FY26: [Broadcom IR](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial)
- TSMC Q1'26: TSMC 6-K / Manufacturing Dive
- GE Vernova Q1'26: [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm)
- ServiceNow Q1 FY26: [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001373715/000137371526000054/erq1fy26.htm)
- SK하이닉스 Q1'26: SK하이닉스 IR / KRX

### 시장 데이터 및 전망
- 빅테크 CapEx $725B: [Statista](https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion), [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)
- Goldman Sachs $5.3T 누적 CapEx: [Value Add VC](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once)
- AI TAM $4,216B by 2035: [Precedence Research](https://www.precedenceresearch.com/artificial-intelligence-market)
- AI TAM $4.8T by 2033: [UNCTAD](https://unctad.org/news/ai-market-projected-hit-48-trillion-2033-emerging-dominant-frontier-technology)
- AI TAM $40T 확장 정의: [Morgan Stanley](https://www.morganstanley.com/insights/articles/ai-diffusion-tech-roundtable)
- HBM 시장 전망: TrendForce, BNP Paribas, Yole Group
- CoWoS 수급: [TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- DC 전력 전망: IEA, Gartner, Goldman Sachs, Morgan Stanley, SemiAnalysis

### 소버린 AI
- CNAS Sovereign AI Index: [CNAS](https://interactives.cnas.org/reports/sovereign-ai-index/)
- WEF Rethinking AI Sovereignty: [WEF](https://www3.weforum.org/docs/WEF_Rethinking_AI_Sovereignty_Pathways_to_Competitiveness_through_Strategic_Investments_2026.pdf)
- 소버린 AI DC 붐: [TheAIForest](https://theaiforest.com/sovereign-ai-data-centers-whats-driving-the-2026-boom/)
- EU Sovereign AI Stack: [TechPlusTrends](https://techplustrends.com/eu-sovereign-ai-infrastructure-stack-2026-guide/)

### 영상 메모 (프레임워크 원본)
- "AI 투자, 결국 돈은 여기로 모입니다": [YouTube](http://www.youtube.com/watch?v=yLzCL3q0c9k)

### 본 프로젝트 연결 리서치
- `data/note-ai-money-flow_20260618.md` — 영상 메모 원본
- `data/research_ai_power_part12_overview.md` — AI 전력 산업구조
- `data/research_ai_power_companies_global.md` — 글로벌 전력 기업 심화
- `data/research_ai_power_companies_kr.md` — 한국 전력 기업 심화
- `data/research_hbm_pkg_part12_overview.md` — HBM/패키징 산업구조
- `data/research_hbm_pkg_companies_global.md` — 글로벌 HBM/패키징 기업
- `data/research_hbm_pkg_companies_kr.md` — 한국 HBM/패키징 기업
- `data/research_ai_bio_companies_global.md` — 글로벌 AI 바이오 기업
- `data/research_ai_bio_companies_kr.md` — 한국 AI 바이오 기업
- `data/research_robot_companies_global.md` — 글로벌 로봇 기업
- `data/research_robot_companies_kr.md` — 한국 로봇 기업
- `data/research_space_companies_global.md` — 글로벌 우주 기업
- `data/research_space_companies_kr.md` — 한국 우주 기업
