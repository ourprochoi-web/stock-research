# HBM·패키징 리서치 — Part 1-2: 산업구조와 투자 좌표

> 목적: HBM 메모리 매크로 수요 전망, 6단계 패키징 밸류체인 맵, 병목·해자·비대칭성 투자 프레임워크, 사이클 판정
> 작성일: 2026-06-22
> 최종 갱신: 2026-06-22
> 커버리지: Part 1-2 (hbm_pkg_overview.html) 리서치 데이터
> 상태: 초안

---

## 1. HBM 매크로 수요 전망 — AI가 만드는 메모리 수요의 규모

### 1.1 글로벌 HBM 시장 규모

| 연도 | HBM 매출 | 출처 | 비고 |
|------|---------|------|------|
| 2024 (실적) | ~$20B | TrendForce | HBM3/HBM3E 중심 |
| 2025E | ~$35B | BNP Paribas / Yole | YoY +75% |
| 2026E | ~$60–76B | BNP Paribas $76B / 업계 $60B | YoY +70~117% |
| 2027E | ~$156B | BNP Paribas | YoY +105% |
| 2030E | ~$98B | Yole Group | CAGR 33% (2024–2030) |
| 2035E | ~$69.75B | Precedence Research | CAGR 25.37% (2026–2035) |

- **전망사 간 편차 주의**: BNP Paribas $156B(2027)은 Yole $98B(2030)보다 60% 높다. 이 역전은 **정의 범위 차이** 때문: BNP Paribas는 HBM 모듈 매출+관련 DRAM 매출을 광의로 포함하는 반면, Yole/Precedence는 HBM 제품 매출만 산정. 또한 BNP Paribas $156B는 2024 글로벌 DRAM TAM(~$100B)의 1.5배로, 업계 컨센서스 대비 극단적 아웃라이어일 가능성이 있음. **본 시리즈에서는 Yole 기준($98B/2030, CAGR 33%)을 기본 전제로 사용하되, BNP 상단 시나리오를 병기**
- **DRAM 내 HBM 비중**: 2024 ~20% → 2030 ~50% 전망 (Yole). HBM이 DRAM 산업의 주력 제품으로 격상
- **HBM 비트 출하량**: 2.8B GB (2024) → 7.6B GB (2030), ~2.7배 성장 (Yole)
- **HBM 웨이퍼 생산량**: 350K WPM (2024) → 590K WPM (2030) (Yole)
- **BOM 비중**: GPU 서버 BOM의 **~30%**가 HBM — 과거 DC 비용의 10%에서 3배 폭증 (영상 메모 참조)

### 1.2 HBM 세대별 로드맵 (2026.06 기준)

| 세대 | 대역폭 | 용량 | 핀 속도 | 양산 시점 | 주요 고객칩 |
|------|--------|------|---------|----------|-----------|
| HBM3 | 819 GB/s | 24 GB (12-Hi) | 6.4 Gbps | 2024 양산 중 | H100, MI300X |
| HBM3E | 1.2 TB/s | 36 GB (12-Hi) | 9.6 Gbps | 2024 H2~ 양산 중 | H200, B200, GB200 |
| **HBM4** | **2+ TB/s** | **36 GB (12-Hi)** | 12 Gbps | **2026.02 양산 시작** | Rubin (R100) |
| **HBM4E** | **~4 TB/s** | **48 GB (12-Hi)** | 14→16 Gbps | **2026.05~06 샘플 출하** | Rubin Ultra |
| HBM5 (예정) | TBD | TBD | TBD | 2028E | 차세대 |

- **HBM4 양산**: 2026.02 삼성·SK하이닉스 동시 개시. NVIDIA Rubin(R100) 플랫폼에 탑재
- **HBM4E 샘플 경쟁**: 삼성 2026.05.29 업계 최초 HBM4E 샘플 출하 (3.6 TB/s), SK하이닉스 2026.06.18 12-Hi HBM4E 샘플 출하 (16Gbps, ~4TB/s, 전력효율 20%↑). **삼성이 6개월 선행** 주장 vs SK하이닉스 3일 후 따라잡기
- **HBM4E 핵심 스펙**: 48GB/스택(12-Hi), HBM4 대비 30%+ 용량 증가, 대역폭 2배
- **HBM4 vs HBM3E 가격**: HBM4 제조 복잡성으로 **ASP 30%+ 프리미엄** 전망

### 1.3 HBM 가격 동향 (ASP per GB)

| 시점 | HBM3 | HBM3E | 출처 |
|------|------|-------|------|
| H1 2025 (피크) | — | $17–20/GB | Silicon Analysts |
| H2 2025 | $8–10/GB ($200/24GB) | $13–17/GB | Silicon Analysts |
| 2026 계약가 | — | +20% 인상 합의 | TrendForce (2025.12) |
| 2026 실제 | 하락 압력 | 하락 압력 | 공급 확대 + 삼성 공격 |

- **가격 역학**: 삼성이 SK하이닉스 대비 ~30% 할인으로 M/S 탈환 시도 → 평균 ASP 하락 압력
- **but**: 2026 계약가는 +20% 인상 합의 완료 (NVIDIA H200/ASIC 수요). 스팟 가격과 계약 가격의 괴리가 확대 중
- **HBM4 프리미엄**: HBM3E 대비 30%+ 높은 ASP → 믹스 개선으로 전체 매출 성장 지속

### 1.4 HBM 시장 점유율 (2025 Q3 매출 기준, Q1'26 현재 유사 수준 추정)

| 기업 | 글로벌 HBM 매출 M/S | 비고 |
|------|-------------------|------|
| **SK하이닉스** | **57%** | HBM 선도, NVIDIA 1차 벤더 |
| 삼성전자 | 22% | HBM3E 수율 문제 → HBM4E 선행 전략 전환 |
| 마이크론 | 21% → 25% 목표 | HBM3E 양산 중, 2026 전량 고정가 계약 매진 (Micron IR) |

- SK하이닉스: 향후 3년간 HBM 수요가 생산능력 초과 (Q1'26 어닝콜)
- 삼성: 2026년 HBM 생산능력 +47% 확대 계획 (17만→25만 WPM)
- OpenAI Stargate: 삼성+SK하이닉스에 월 90만장 DRAM 웨이퍼 계약

---

## 2. 밸류체인 맵 — 웨이퍼에서 서버까지, 6단계 후공정

### 2.1 6단계 밸류체인 구조

```
STAGE 01: 웨이퍼     STAGE 02: 범핑        STAGE 03: 첨단 패키징
──────────────── ─→ ──────────────── ─→ ────────────────────
HBM DRAM 다이       마이크로 범프           CoWoS-S / CoWoS-L
전공정 (SK하이닉스    플립칩 범핑            InFO (Fan-Out)
삼성, 마이크론)      Cu 필러·솔더           SoIC (3D)
                                         I-Cube (삼성)

STAGE 04: TC 본딩    STAGE 05: 테스트       STAGE 06: 기판
──────────────── ─→ ──────────────── ─→ ────────────────────
열압착 본딩(TCB)      번인 테스트            ABF 기판 (FC-BGA)
하이브리드 본딩       핸들러                 글라스코어 기판
다이 스태킹 (12-Hi)   소켓 (러버/포고핀)     CCL·ABF 소재
고압수소어닐링        ATE (자동테스트장비)    실리콘 인터포저
```

### 2.2 STAGE 01 — HBM DRAM 웨이퍼 (전공정)

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **SK하이닉스** | Q1'26 **분기** 매출 ₩52.6T (사상 최대 분기 실적, QoQ +60%, YoY +198%), 영업이익 ₩37.6T (OPM 72%). 용인 M15X 팹 가속, HBM 수요 3년간 생산능력 초과. *주: HBM 슈퍼사이클 + DRAM ASP 급등으로 직전 Q4'25 대비 60% 성장한 분기 수치* | CNBC, StorageNewsletter |
| **삼성전자** | HBM4E 업계 최초 샘플 출하 (2026.05.29). 2026 HBM CAPA +47% (17만→25만 WPM). HBM 수율·신뢰성 문제 극복 중 | TechTimes, TrendForce |
| **마이크론** | Q2 FY26 매출 $23.9B, Cloud BU $7.7B (GM 74%). HBM M/S 21%→25% 목표. 2026 HBM 전량 고정가 매진. HBM4 **2026 H2 양산 개시** (기존 2027 목표에서 앞당김) | Micron IR, SEC 8-K |

- **공급 병목**: 3사 합산 HBM 웨이퍼 생산능력이 수요를 여전히 하회. 특히 HBM4 전환기에 수율 안정화까지 공급 타이트
- **CXMT 진입 위협**: 중국 CXMT가 HBM3 2026 양산 목표 → **일정 밀림, 양산 불확실** (수율·열관리 문제). HBM3 현실적으로 2027~2028 전망. 월 6만장(총 CAPA의 20%)을 HBM 전용 전환 계획

### 2.3 STAGE 02 — 범핑 (Bumping)

| 기업 | 역할 | 비고 |
|------|------|------|
| ASE/SPIL | 범핑 + 패키징 통합 | TSMC CoWoS 외주 파트너 |
| Amkor | 범핑 + 패키징 | TSMC 외주 18~19만장/년 |
| TSMC | 자체 범핑 + CoWoS | 수직 통합 |

- **마이크로 범프 피치**: HBM3E 28~30μm → HBM4 20~25μm → HBM4E 15μm 이하
- **하이브리드 본딩 전환**: 솔더 범프 58.9% 점유 (2025) → 하이브리드 본딩이 2028년 HBM 공정의 **36%** 차지 전망 (CAGR 10%)

### 2.4 STAGE 03 — 첨단 패키징 (CoWoS/InFO/SoIC)

#### 첨단 패키징 시장 전체

| 지표 | 수치 | 출처 |
|------|------|------|
| 첨단 패키징 시장 규모 | $57.5B (2026) → $90.1B (2031), CAGR 9.4% | Mordor Intelligence |
| 또는 | ~$45B (2024) → ~$80B (2030), CAGR 9.4% | IDC |
| 전체 패키징 대비 비중 | 40% (2020) → **50%+ (2026)** → ~65% (2030) | TechInsights |

#### TSMC CoWoS — 핵심 병목

| 지표 | 수치 | 출처 |
|------|------|------|
| CoWoS 생산능력 | 35K WPM (2024 말) → **120~130K WPM (2026 말)** → 170K WPM (2027) | TrendForce (일부 추정 140K, SemiWiki) |
| CoWoS 수요 | ~370K (2024) → ~670K (2025) → **~1.0M 웨이퍼 (2026)** | TrendForce |
| 수급 갭 | **20% 부족 (2026 초)** → 10% 부족 (2026 말) | TrendForce (2026.06.15) |
| 리드타임 | **52~78주** (2025 말 기준) | 업계 |
| TSMC 매출 중 첨단 패키징 비중 | ~8% (2025) → **10%+ (2026)** | TSMC |
| NVIDIA CoWoS 예약 비중 | **50%+** (2026 할당) | SiliconAnalysts |
| 외주 물량 | 24~27만장/년 → Amkor 18~19만장 + SPIL 6~8만장 | TrendForce |

- **CoWoS-L**: 대면적 패키징 (Blackwell/Rubin), 2026 본격 양산
- **CoPoS (Chip-on-Panel-on-Substrate)**: 패널 레벨 패키징 차세대. TSMC 파일럿 라인 **2026.06 완공**, 2028~29 양산 목표
- **SoIC**: Die-to-Wafer 3D 스태킹. AMD MI300 시리즈에 적용 (12 다이 스택)

### 2.5 STAGE 04 — TC 본딩 (Thermo-Compression Bonding)

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **한미반도체** | TC본더 글로벌 M/S **71.2%** (2025). 북미 고객 M/S **90%**. SK하이닉스 M/S 50%→60% (2026). 2026E 매출 ₩1.08T (+64% YoY), 영업이익 ₩564.5B (+52%). TC Bonder 4 (HBM4용) 2025.07 양산 개시. Wide TC Bonder (HBM5/6용) 2026 H2 출시 | 소뮤어, EBN뉴스 |
| **BESI (네덜란드)** | Q1'26 매출 €184.9M (+28%), 수주 €269.7M (YoY 2배+). 하이브리드 본딩 매출 €476M(2026E), 전체의 ~1/3. 정밀도 <10nm | BESI IR, TipRanks |
| **Shibaura (일본)** | TC본더 3위. HBM3E 레퍼런스 보유 | 업계 추정 (미확인) |

- **TC 본딩 시장**: HBM 스택 수 증가(8-Hi→12-Hi→16-Hi)에 따라 본더 수요 비례 증가
- **하이브리드 본딩 전환**: 2028년 이후 TCB → 하이브리드 본딩 전환 시 한미반도체의 해자 변화 모니터링 필요

#### 고압 수소 어닐링 (HPSP)

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **HPSP** | 고압수소어닐링 장비 **세계 독점**. 시가총액 ~$3.8B (2026.06). SK하이닉스 독점 공급. HBM 다이 적층 후 수소 어닐링이 수율·신뢰성 핵심 공정 | HPSP, PitchBook |

- SK하이닉스가 대체 벤더(YEST) 검토 보도 → HPSP 독점 해자에 대한 리스크 모니터링

### 2.6 STAGE 05 — 테스트

| 기업 | 역할 | 비고 |
|------|------|------|
| **리노공업** | 테스트 소켓 (포고핀) M/S 30%+ | 미세 피치 대응, 고마진 |
| **ISC** | 러버소켓 테스트 | HBM/메모리 번인 |
| **테크윙** | 핸들러 | 메모리 테스트 장비 |
| **Advantest** | ATE (자동테스트장비) 글로벌 #1 | HBM 전용 ATE 수요 증가 |

- HBM 스택 수 증가 → 테스트 시간 비례 증가 → 테스트 장비 수요 구조적 증가
- HBM4 미세 피치(15μm↓) 전환 시 테스트 소켓 정밀도 요구 상승 → 리노공업 수혜

### 2.7 STAGE 06 — 기판 (Substrate)

#### ABF 기판 시장

| 지표 | 수치 | 출처 |
|------|------|------|
| ABF 기판 시장 | $4.9B (2024) → **$7.2B (2026)** → $10.2B (2030), CAGR 9.9% | Semiconductor Insight |
| 또는 | $9.5B (2033), CAGR 10.6% | Business Research Insights |
| Top 5 M/S | Unimicron 22%, Ibiden, AT&S, Nan Ya, Shinko — 합산 **74%** | QY Research |
| 아시아 비중 | **75%** | 업계 |

#### FC-BGA 한국 기업

| 기업 | 핵심 데이터 | 출처 |
|------|------------|------|
| **삼성전기** | 2026E 매출 ₩13.1T, 영업이익 ₩1.48T (+62.5% YoY). FC-BGA 매출 **₩2T+ 돌파** 전망 (슈퍼 호황). 서버 비중 36%. 고부가 FCBGA 50%↑ 목표. 베트남 ₩1.8T 투자, **유리 기판 2027 양산 개시** (기존 2026→조정) | 더빅데이터, 대신증권 |
| **LG이노텍** | FC-BGA 후발. AI 서버 기판 수요 대응 | 비즈한국 |

- **국내 4사 FC-BGA 합산**: ₩1.6T (2025) → **₩2.4T (2026, +48%)** → ₩3.1T (2027, +32%)
- **글라스코어 기판**: 인텔 2026~2030 양산 계획. 삼성전기 **2027** 양산 개시 (기존 2026→조정). ABF 대비 신호 손실 40% 감소, 열팽창 90% 개선. **차세대 HBM/AI칩의 기판 표준 전환 가능성**

---

## 3. 투자 프레임워크 — 병목·해자·비대칭성

> 참조: `data/note-ai-money-flow_20260618.md` (투자 사고 프레임워크 메모)

### 3.1 조건 1: 병목(Bottleneck) 구간인가?

공급이 수요를 못 따라가는 구간에 돈이 몰린다.

| 밸류체인 단계 | 병목 요소 | 심각도 | 근거 |
|-------------|---------|--------|------|
| HBM 웨이퍼 | HBM 다이 공급 | ★★★★☆ | 3사 CAPA < 수요, 특히 HBM4 전환기 수율 불안정 |
| 첨단 패키징 | CoWoS CAPA | ★★★★★ | 수급갭 10~20%, 리드타임 52~78주, NVIDIA 50%+ 예약 |
| TC 본딩 | TC본더 장비 | ★★★★☆ | HBM 스택 수 증가에 비례, 한미반도체 71% 독점 |
| 테스트 | ATE·소켓 | ★★★☆☆ | 테스트 시간 비례 증가, 미세 피치 전환 |
| 기판 | ABF 기판 | ★★★★☆ | AI 서버 기판 수요 급증, Top 5가 74% 과점 |
| 소재 | ABF 필름 (Ajinomoto) | ★★★☆☆ | Ajinomoto 사실상 독점, 대체재 부재 |

### 3.2 조건 2: 독점적 해자(Moat)를 가졌는가?

| 기업/구간 | 해자 유형 | 설명 |
|----------|---------|------|
| SK하이닉스 | 기술 선도 + 고객 락인 | HBM M/S 57%, NVIDIA 1차 벤더, 3년 수요 > CAPA |
| TSMC (CoWoS) | 생산 규모 + 기술 독점 | 2.5D/3D 패키징 사실상 독점, 외주도 TSMC 생태계 |
| 한미반도체 | 장비 독점 | TC본더 71%, 북미 90%. 경쟁사(BESI, Shibaura) 추격 중이나 격차 유지 |
| HPSP | 공정 독점 | 고압수소어닐링 세계 유일. but 대체 벤더 리스크 |
| 리노공업 | 니치 마켓 독점 | 포고핀 소켓 30%+, 미세 피치 기술 장벽 |
| 삼성전기 | 포트폴리오 해자 | 글로벌 유일 기판+MLCC 동시 보유, 패키지 모듈 번들 가능 |

### 3.3 조건 3: 비대칭성 — 하방은 막히고 상방은 열린가?

| 구간 | 상방 시나리오 | 하방 리스크 | 비대칭 판단 |
|------|-------------|-----------|-----------|
| SK하이닉스 (HBM) | 3년 CAPA 초과 수요, HBM4 프리미엄, OPM 72% | 메모리 사이클 피크 우려, CXMT 장기 위협, 삼성 할인 공세 | **중립** (실적은 압도적이나 사이클 위치 부담) |
| 한미반도체 (TC본더) | HBM 스택 수 증가, Wide TC Bonder 차세대 | 하이브리드 본딩 전환 시 TCB 수요 감소 위험 | **긍정 (단, 조건부)** — 2028까지 TCB 64% 주류이나, 하이브리드 본딩 36% 전망 감안 시 2027~28경 전환 리스크 선반영 가능. HBM5/6 대응 Wide TC Bonder 수주가 핵심 변수 |
| HPSP | 독점 지속, HBM 생산량 비례 성장 | 대체 벤더(YEST) 진입, SK하이닉스 내재화 | **긍정** (단기 독점 유지, 중기 리스크 있음) |
| 삼성전기 (FC-BGA) | AI 서버 기판 슈퍼사이클, 유리 기판 선점 | 글로벌 Big 5 경쟁, AI 투자 둔화 | **긍정** (기판+MLCC 번들의 비대칭성) |
| TSMC (CoWoS) | AI 패키징 독점, CoPoS 차세대 | 인텔 EMIB 경쟁, 지정학 리스크 | **강긍정** (대안 부재, 수급갭 지속) |
| 삼성전자 (HBM) | HBM4E 선행, M/S 탈환, 파운드리 시너지 | HBM3E 수율 트라우마, 가격 할인 마진 압박 | **중립~부정** (할인 전략이 마진을 깎는 구조) |

---

## 4. 사이클 판정 — 지금은 어디인가?

### 4.1 HBM 사이클 현 위치

```
          ┌──────── 2026 현재 위치 ────────┐
          │                                │
          ▼                                │
도입기 → 성장 가속기 → [슈퍼사이클 vs 피크] → 성숙기 → 둔화
2022      2024         2026~2027           2028+?
HBM3     HBM3E        HBM4/HBM4E          HBM5?
```

### 4.2 슈퍼사이클 근거 (강세론)

1. **수요 측**: AI 모델 파라미터 매년 10배 성장, 추론 워크로드 50%+ → HBM 수요 구조적
2. **공급 측**: HBM4 전환 수율 불안정, CoWoS 10~20% 부족 → 공급 타이트 지속
3. **가격**: HBM4 ASP 30%+ 프리미엄, 계약가 +20% 인상
4. **실적**: SK하이닉스 OPM 72%, 사상 최대 분기실적 갱신 중
5. **고객 커밋**: NVIDIA·하이퍼스케일러 3년 이상 장기 계약

### 4.3 피크 우려 (약세론)

1. **공급 확대**: 삼성 CAPA +47%, SK하이닉스 용인 M15X, 마이크론 확대
2. **가격 하락 압력**: 삼성 30% 할인 공세, 2026 스팟 가격 하락
3. **CXMT 진입**: 중국 HBM3 생산 시작 시 저가 시장 잠식 (2027~2028)
4. **효율 개선**: AI 모델 경량화, 추론 최적화로 HBM 소요량 감소 가능성
5. **밸류에이션**: SK하이닉스 Forward P/E ~7x (낮아 보이나 사이클 주식 특성상 PER 하락이 피크 신호)

### 4.4 판정

**"피크는 아니지만 가속도는 둔화 구간"** — 중기 강세, 단기 변동성 확대

- HBM 수요는 2028~2029까지 구조적 성장 가능 (AI 추론 확산)
- 그러나 ASP 하락 + 공급 확대로 **"매출 성장은 되지만 마진 피크는 통과 중"**일 가능성
- 기존 Deep Dive의 "3군(보유 유효, 신규매수 NO)" 판단은 유지하되, **후공정 장비·소재 기업(한미반도체, HPSP, 삼성전기)에서 비대칭 기회** 탐색이 본 시리즈의 핵심

---

## 5. 리스크 체크리스트 (R1–R5)

### R1 — 메모리 사이클 역전
- HBM 공급이 수요를 초과하는 시점에서 ASP 급락
- 과거 DRAM 사이클: 2018 피크 → 2019 -47% ASP 하락 사례
- 모니터링: 삼성·SK하이닉스 분기 HBM ASP, TrendForce 월간 가격

### R2 — CXMT·중국 진입
- CXMT HBM3 양산 시 저가 시장 잠식, HBM3E까지 확장 가능성
- 현 상태: HBM3 수율·열관리 난항, 현실적으로 2027~2028
- but: DDR4에서 이미 반값 공세 사례 → HBM3에서도 반복 가능
- 모니터링: CXMT IPO 진행, 웨이퍼 출하량, 미국 수출 규제 강화 여부

### R3 — 하이브리드 본딩 전환
- 2028년 이후 TCB → 하이브리드 본딩 전환 시 한미반도체 해자 약화
- BESI가 하이브리드 본딩 선두 주자
- 모니터링: HBM4E/HBM5 본딩 공정 선택, 한미반도체 Wide TC Bonder 수주

### R4 — AI CAPEX 사이클 조정
- 하이퍼스케일러 투자 둔화 시 GPU 발주 → HBM 수요 → 패키징 순으로 타격
- 모니터링: MSFT/GOOGL/META/AMZN 분기 CAPEX, NVIDIA 가이던스

### R5 — 지정학·수출 규제
- 미국 대중 반도체 수출 규제 강화 시 CXMT 진입 지연 (한국 기업에 긍정)
- 반대로 한국 기업의 중국 메모리 팹 운영 규제 강화 시 공급 차질
- 모니터링: 미 상무부 BIS 규정, 한국 반도체 산업 지원 정책

---

## 6. 밸류체인 맵 — 종목 배치 요약

```
STAGE 01: HBM 웨이퍼 + 박형화              STAGE 02: 범핑
├─ SK하이닉스 (HBM M/S 57%)               ├─ ASE/SPIL (범핑+패키징)
├─ 삼성전자 (HBM 2위, 22%)                ├─ Amkor (TSMC 외주 파트너)
├─ 마이크론 (HBM 3위, 21%)                └─ TSMC (자체 범핑)
├─ CXMT (중국, HBM3 도전 중)
└─ Disco (다이싱/그라인딩 M/S 70~80%)

STAGE 03: 첨단 패키징                      STAGE 04: 본딩·어닐링
├─ TSMC (CoWoS/InFO/SoIC 독점)           ├─ 한미반도체 (TCB M/S 71%)
├─ ASE/SPIL (CoWoS 외주)                 ├─ BESI (하이브리드 본딩 선두)
├─ Amkor (CoWoS 외주)                    ├─ HPSP (고압수소어닐링 독점)
├─ 삼성 (I-Cube4/FOPLP)                  └─ 한화세미텍 (와이어본더 — 범용 패키징)
└─ 인텔 (EMIB/Foveros)
                                         크로스 스테이지 장비사
STAGE 05: 테스트                           ├─ Applied Materials (증착·CMP·Kinex·패널)
├─ Advantest (ATE 글로벌 #1, M/S 70%)     └─ Lam Research (TSV 식각·하이브리드 본딩)
├─ 리노공업 (포고핀 소켓 M/S 30%+)
├─ ISC (러버소켓)                          STAGE 06: 기판·소재
├─ 테크윙 (핸들러)                         ├─ Unimicron (ABF #1, 22%)
└─ Cohu (테스트 장비)                     ├─ Ibiden (ABF #2)
                                          ├─ 삼성전기 (FC-BGA + MLCC + 유리기판)
                                          ├─ AT&S (#3) / Shinko (#5) / Nan Ya (#4)
                                          └─ Ajinomoto (ABF 필름 M/S 95%)
```

---

## 7. 글로벌 기업 데이터 — 국가별 정리

### 7.1 대만 (Taiwan)

#### TSMC — 첨단 패키징의 절대 군주

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | ~$35B (+40.6% YoY) | Manufacturing Dive |
| FY26 매출 성장 가이던스 | **+30%+ YoY** (USD 기준) | TSMC 어닝콜 |
| 첨단 패키징 매출 비중 | ~8% (2025) → **10%+ (2026)** | TSMC |
| CoWoS CAPA | 35K WPM (2024) → **120~130K WPM (2026 말)** → 170K WPM (2027) | TrendForce |
| CoWoS 수급갭 | 20% (2026 초) → **10% (2026 말)** | TrendForce |
| CoWoS 외주 | 24~27만장/년 — Amkor 18~19만 + SPIL 6~8만 | TrendForce |
| CAPEX 중 첨단 패키징 비중 | **10~20%** | TSMC |
| CoPoS 파일럿 라인 | 2026.06 완공, 2028~29 양산 목표 | TrendForce |

- **해자**: 2.5D/3D 패키징 사실상 독점, NVIDIA 50%+ 예약, 52~78주 리드타임
- **리스크**: 지정학(대만 해협), 인텔 EMIB 경쟁, 미국 Arizona 팹 코스트 프리미엄

#### ASE/SPIL — OSAT 세계 1위

| 지표 | 수치 | 출처 |
|------|------|------|
| ASE Q1'26 매출 | NT$173.7B (+17.2% YoY) | Investing.com |
| SPIL 1~5월 매출 | NT$298.9B (+19.9% YoY, 동기간 사상 최대) | TrendForce |
| 2026 첨단 패키징(LEAP) 매출 가이던스 | **$3.5B+** (+10% 상향) | AlphaPilot |
| SPIL 신규 공장 인수 | NT$2.8B — TSMC 첨단 패키징 overflow 대응 | TrendForce |

- **포지션**: TSMC CoWoS 외주 핵심 파트너, 범핑+패키징 통합 서비스
- **SPIL**: 2026.06 TSMC 첨단 패키징 CAPA 부족분 흡수를 위해 공장 인수 가속

#### Unimicron — ABF 기판 세계 1위

| 지표 | 수치 | 출처 |
|------|------|------|
| ABF 기판 글로벌 M/S | **~22%** (1위) | QY Research |
| NVIDIA GPU용 ABF M/S | **~35%** | DIGITIMES |
| ASIC(Google TPU, AWS) ABF M/S | **50%+** | DIGITIMES |
| 2026 AI 매출 비중 | **~60%** (GPU+ASIC+서버 CPU) | DIGITIMES |
| ABF CAPA 확대 | **+40%** (BT 기판 -15% 구조조정) | DIGITIMES |
| 2026 목표 | 2022 피크 초과 **사상 최대 매출** | DIGITIMES |

- 유리섬유 부족(2026) → 기판 가격 인상 + 고객사 **장기 계약(LTA)** 체결 러시
- BofA 투자의견 상향 (Buy), 2027 영업이익 전망 +27% 상향

### 7.2 미국 (US)

#### 마이크론 — HBM 3위, 빠른 추격자

| 지표 | 수치 | 출처 |
|------|------|------|
| Q2 FY26 매출 | **$23.86B** | SEC 8-K |
| Q2 FY26 순이익 | $13.79B (EPS $12.07) | Micron IR |
| Q3 FY26 EPS 가이던스 | **$19.15** (사상 최대, ±$0.40) | Micron IR |
| Cloud BU 매출 | $7,749M (GM 74%) | SEC 10-Q |
| HBM M/S | **~21%** → 25% 목표 | 업계 |
| 2026 HBM 공급 | **전량 고정가 계약 매진** | Tickeron |
| HBM4 수율 | HBM3E 12-Hi 대비 **빠른 램프** 기대 | Micron 어닝콜 |

- HBM3E 12-Hi 36GB 양산 중, HBM4 **2026 H2 양산 개시** (기존 2027 목표에서 앞당김)
- 30% 저전력 HBM4 스택 — 차별화 포인트
- 리스크: M/S 3위 고착, SK하이닉스 대비 고객 다변화 부족

#### Applied Materials — 패키징 장비 최강자

| 지표 | 수치 | 출처 |
|------|------|------|
| 반도체 장비 사업 성장 | **+20~30% (CY2026)** | SEC 8-K |
| Kinex 하이브리드 본딩 시스템 | 신규 출시 — AI 프로세서 패키징 병목 해소 | Applied Materials |
| ASMPT NEXX 사업부 인수 | 패널 레벨 첨단 패키징 증착 장비 | 업계 |
| BESI 인수 경합 | Lam Research와 함께 **수십억 유로** 규모 입찰 | Tiger Brokers |

- 하이브리드 본딩·패널 레벨 패키징 장비 확장으로 BESI 대항마 구축 중
- HBM 웨이퍼 박형화, CMP, 증착 공정에서 핵심 장비 공급

#### Amkor Technology — CoWoS 외주의 핵심

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **$1,685M** (+27% YoY, Q1 사상 최대) | SEC 8-K |
| 첨단 패키징 매출 | $1.4B (전년 $1.1B → +27%) | Amkor IR |
| GM | 14.2%, 영업이익 $100M | SEC 8-K |
| Q2'26 가이던스 | $1.75~1.85B | Amkor IR |
| TSMC 10년 파트너십 | Arizona 첨단 패키징 + 테스트 | DIGITIMES |
| CoWoS 외주 배분 | **~80K WPM** (TSMC 120K 대비) | 36Kr |

- TSMC Arizona 팹과 연계한 미국 내 첨단 패키징 허브 구축
- CoWoS overflow 물량의 최대 수혜자

#### Lam Research — 첨단 패키징 20년 베테랑

| 지표 | 수치 | 출처 |
|------|------|------|
| 첨단 패키징 경력 | **20년+** (범프, RDL, TSV, TGV, 하이브리드 본딩) | Lam Research |
| BESI 인수 경합 | Applied Materials와 함께 입찰 | Tiger Brokers |

- TSV/TGV 식각, 하이브리드 본딩 전처리 장비에서 핵심 포지션

### 7.3 일본 (Japan)

#### Advantest — ATE의 "테스트계 ASML"

| 지표 | 수치 | 출처 |
|------|------|------|
| FY25 매출 (2026.03 결산) | **¥1.13T** (+44.8% YoY) | PitchBook |
| FY25 순이익 | ¥375.4B (+132.9% YoY) | PitchBook |
| FY26 매출 가이던스 | **~$9B** (+26% YoY) | DIGITIMES |
| 글로벌 ATE M/S | **~70%** | Apple Podcasts |
| 메모리 테스트 M/S | **60~70%** | 업계 |
| SoC 테스트 M/S | 35~45% | 업계 |
| ATE 시장 규모 | **$12.5~13B** (2026) | Advantest |
| 테스트 유닛 생산 | 3,000대 → **5,000대** (2026 램프) | 업계 |

- HBM 모듈과 패키지 GPU 출하 전 **모든 칩이 Advantest 장비를 통과**
- HBM 스택 증가 → 테스트 시간/복잡도 비례 증가 → 구조적 수혜

#### Disco Corporation — 웨이퍼 다이싱/그라인딩 독점

| 지표 | 수치 | 출처 |
|------|------|------|
| TTM 매출 (2026.03) | **$2.9B** | PitchBook |
| Q1'26 매출 | $838M (+26.9% beat) | Meyka |
| 정밀 다이싱·그라인딩 M/S | **70~80%** (사실상 독점) | SemiAnalysis |
| R&D 비중 | **33%** of 매출 | SemiAnalysis |
| 레이저 소 누적 출하 | **4,000대+** (2026.02, 2020 이후 3배) | 업계 |

- HBM은 웨이퍼를 30~50μm까지 극박화 → Disco의 Taiko 그라인딩/스텔스 다이싱 **필수 공정**
- 하이브리드 본딩, 3D 스태킹에서도 핵심 전처리 장비

#### Ibiden — ABF 기판 2위, AI 서버 핵심 공급자

| 지표 | 수치 | 출처 |
|------|------|------|
| 투자 계획 | **¥500B (~$3.2B)** (FY26~28, 3년간) | Kantenna |
| 용도 | AI 서버·HPC용 고성능 IC 패키지 기판 CAPA 2.5배 확대 | Kantenna |
| 기술 포지션 | Intel·NVIDIA 주요 기판 공급사 | 업계 |

- ABF 기판 글로벌 2위, AI 서버 수요 폭증에 대응한 대규모 투자
- $3.2B 투자는 회사 역사상 최대 — AI 확신의 신호

#### Ajinomoto — ABF 필름 95% 독점, "식품 회사의 반도체 지배"

| 지표 | 수치 | 출처 |
|------|------|------|
| ABF 필름 글로벌 M/S | **95%+** (사실상 독점) | BigGo Finance |
| FY25 영업이익 (2026.03) | ¥181.1B (+13% YoY, 사상 최대) | TrendForce |
| 전자소재 부문 영업이익 | ¥54.6B (+35% YoY, 전체의 **30%**) | TrendForce |
| ABF 필름 마진 | **50%+** | TrendForce |
| 가격 인상 | **+30%** (Q3 2026 적용) | BigGo Finance |
| 신공장 용지 매입 | ¥1.2B (2032년 가동 목표) | TrendForce |

- AI칩 기판 레이어: 3+3 → 11+11 → 13+13 진화 → ABF 소요량 4배+ 증가
- **2026 H1부터 다시 부족(shortage)** 진입 — AI 패키징 업그레이드가 원인
- 95% 독점 + 50%+ 마진 + 30% 가격 인상 = **밸류체인에서 가장 은밀한 해자**

#### Shinko Electric Industries — ABF 기판 5위

- Fujitsu 계열, 글로벌 Top 5 ABF 기판 공급사
- Intel 패키징 기판 핵심 벤더
- Ibiden과 함께 일본 기판 양대 축

### 7.1b 대만 추가

#### Nan Ya PCB — ABF 기판 4위

- Formosa Plastics 그룹 계열, ABF 기판 Top 5 (4위)
- 대만 내 Unimicron과 함께 ABF 양대 공급사
- AI 서버·HPC 수요 증가에 따라 CAPA 확대 중

### 7.4 네덜란드 (Netherlands)

#### BESI (BE Semiconductor Industries) — 하이브리드 본딩의 왕

| 지표 | 수치 | 출처 |
|------|------|------|
| Q1'26 매출 | **€184.9M** (+28.3% YoY) | BESI IR |
| Q1'26 수주 | **€269.7M** (YoY 2배+, 사상 최대) | BESI IR |
| Q2'26 가이던스 | +30~40% QoQ (€240~259M) | BESI IR |
| 하이브리드 본딩 매출 | €36M (2023) → **€476M (2026E)** | TipRanks |
| 하이브리드 본딩 비중 | 전체 매출의 **~1/3** (2026) | TipRanks |
| 정밀도 | **<10nm** 본딩 정렬 | 업계 |
| M&A 경합 | Applied Materials·Lam Research가 **수십억 유로** 인수 입찰 | Tiger Brokers |

- HBM4 이후 하이브리드 본딩 전환의 **최대 수혜자**
- 삼성·SK하이닉스·마이크론 모두 BESI 하이브리드 본더 채택 가능성 높음 (Bernstein)
- 하이브리드 본딩 시장: 2028년 HBM 공정의 36%, 시장 규모 **~$2B**

### 7.5 오스트리아 (Austria)

#### AT&S — ABF 기판 3위

- 글로벌 ABF 기판 Top 5 (M/S 74% 내)
- 유럽 유일의 주요 ABF 기판 제조사
- AI 서버·HPC 기판 수요 수혜

### 7.6 중국 (China)

#### CXMT — HBM 도전자, 현실과 야망의 괴리

| 지표 | 수치 | 출처 |
|------|------|------|
| HBM3 양산 목표 | 2026 → **밀림** (수율·열관리 문제) | DIGITIMES |
| 12-layer HBM 목표 | **2027** | DIGITIMES |
| HBM 전용 CAPA 전환 | 월 **6만장** (총 CAPA의 20%) | 업계 |
| IPO 규모 | **$4.2B** (추진 중) | FinancialContent |
| 현실적 HBM3 양산 | **2027~2028** | 업계 종합 |

- DDR4 반값 공세 사례 → HBM3에서도 가격 파괴 가능성
- but: 수율·열관리 난항, 미국 수출 규제, 장비 조달 제약
- **단기 위협은 제한적, 중기(2028+) 저가 시장 잠식 리스크**

#### Naura·Maxwell·U-Preseason — 중국 HBM 장비 생태계

- CXMT HBM3 양산을 위한 국산 장비 개발 중
- 본딩·어닐링·테스트 장비의 자급자족 시도
- 기술 수준은 글로벌 대비 2~3세대 뒤처짐

---

## 8. 밸류체인 맵 — 종목 배치 요약 (글로벌 확장판)

```
STAGE 01: HBM 웨이퍼 + 박형화               STAGE 02: 범핑
├─ SK하이닉스 🇰🇷 (M/S 57%)               ├─ ASE/SPIL 🇹🇼 (OSAT #1)
├─ 삼성전자 🇰🇷 (M/S 22%)                 ├─ Amkor 🇺🇸 (TSMC 외주 핵심)
├─ 마이크론 🇺🇸 (M/S 21%)                 └─ TSMC 🇹🇼 (자체 범핑)
├─ CXMT 🇨🇳 (도전 중)
└─ Disco 🇯🇵 (다이싱/그라인딩 M/S 70~80%)

STAGE 03: 첨단 패키징                      STAGE 04: 본딩·어닐링
├─ TSMC 🇹🇼 (CoWoS 독점)                 ├─ 한미반도체 🇰🇷 (TCB M/S 71%)
├─ ASE/SPIL 🇹🇼 (외주)                   ├─ BESI 🇳🇱 (하이브리드 본딩 선두)
├─ Amkor 🇺🇸 (외주)                      ├─ HPSP 🇰🇷 (수소어닐링 독점)
├─ 삼성 🇰🇷 (I-Cube4)                    └─ 한화세미텍 🇰🇷 (와이어본더 — 범용 패키징)
└─ 인텔 🇺🇸 (EMIB/Foveros)
                                          크로스 스테이지 장비사
STAGE 05: 테스트                           ├─ Applied Materials 🇺🇸 (증착·CMP·Kinex)
├─ Advantest 🇯🇵 (ATE M/S 70%)           └─ Lam Research 🇺🇸 (TSV 식각·본딩)
├─ 리노공업 🇰🇷 (소켓 M/S 30%+)
├─ ISC 🇰🇷 (러버소켓)                     STAGE 06: 기판·소재
├─ 테크윙 🇰🇷 (핸들러)                    ├─ Unimicron 🇹🇼 (ABF #1, 22%)
└─ Cohu 🇺🇸 (테스트 장비)                 ├─ Ibiden 🇯🇵 (ABF #2, $3.2B 투자)
                                          ├─ 삼성전기 🇰🇷 (FC-BGA + 유리기판)
                                          ├─ AT&S 🇦🇹 (#3) / Nan Ya 🇹🇼 (#4) / Shinko 🇯🇵 (#5)
                                          └─ Ajinomoto 🇯🇵 (ABF 필름 M/S 95%)
```

---

## 9. 출처 목록

### 기관·산업 리포트
- BNP Paribas, HBM 시장 전망 (2026) — $76B (2026), $156B (2027)
- Yole Group, *Memory Market Surges Beyond Expectations* (2025) — [링크](https://www.yolegroup.com/press-release/memory-market-surges-beyond-expectations-almost-200-billion-in-2025-driven-by-hbm-ai/)
- TrendForce, *HBM Industry Analysis 1Q26* — [링크](https://www.trendforce.com/research/download/RP260204DA3)
- TrendForce, *CoWoS Supply-Demand Gap Narrowing* (2026.06.15) — [링크](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- TrendForce, *SK hynix Ships 12-High HBM4E Samples* (2026.06.18) — [링크](https://www.trendforce.com/news/2026/06/18/news-sk-hynix-ships-12-high-hbm4e-samples-boosts-bandwidth-to-16gbps-and-power-efficiency-by-over-20/)
- TrendForce, *Samsung·SK hynix HBM3E Price Hike* (2025.12) — [링크](https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/)
- Precedence Research, *HBM Market Size* — [링크](https://www.precedenceresearch.com/high-bandwidth-memory-market)
- Mordor Intelligence, *Advanced Packaging Market* — [링크](https://www.mordorintelligence.com/industry-reports/advanced-packaging-market)
- Mordor Intelligence, *HBM Market* — [링크](https://www.mordorintelligence.com/industry-reports/high-bandwidth-memory-market)
- Semiconductor Insight, *ABF Substrate Market* — [링크](https://semiconductorinsight.com/report/abf-substrate-market/)
- Silicon Analysts, *HBM Pricing & Market Share 2026* — [링크](https://siliconanalysts.com/tools/hbm-analysis)
- Silicon Analysts, *HBM Price per GB* — [링크](https://siliconanalysts.com/market-data/hbm-pricing)

### 기업 실적·공시
- SK하이닉스 Q1'26 실적 — [CNBC](https://www.cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html), [StorageNewsletter](https://www.storagenewsletter.com/2026/04/29/sk-hynix-fiscal-1q26-financial-results/), [NineScrolls](https://ninescrolls.com/news/sk-hynix-q1-2026-record-52-6-trillion-won-revenue-72-operating-margin-m15x-fab)
- 삼성 HBM4E 샘플 출하 — [TechTimes](https://www.techtimes.com/articles/317400/20260530/samsung-ships-industry-first-hbm4e-samples-36-tb-s-bandwidth-beats-sk-hynix-six-months.htm)
- SK하이닉스 HBM4E 샘플 — [TechTimes](https://www.techtimes.com/articles/318633/20260619/sk-hynix-ships-12-layer-hbm4e-samples-ahead-schedule-tightening-race-samsung.htm)
- 한미반도체 TC본더 M/S — [소뮤어](https://somsap.somsap.com/2026/05/01/한미반도체-hbm-tc본더-시장-점유율-2026/), [EBN](https://www.ebn.co.kr/news/articleView.html?idxno=1700474)
- 삼성전기 FC-BGA — [더빅데이터](https://www.thebigdata.co.kr/view.php?ud=202603271001066483bbceadc3c9_23), [데일리머니](http://www.thedailymoney.com/news/articleView.html?idxno=1138174)
- HPSP — [PitchBook](https://pitchbook.com/profiles/company/496364-95), [HPSP IR](https://thehpsp.com/)

### CXMT·중국 동향
- DIGITIMES, *CXMT HBM3 Timeline Slips* — [링크](https://www.digitimes.com/news/a20260421PD230/cxmt-hbm3-dram-production-2026.html)
- DIGITIMES, *CXMT Targets 12-Layer HBM by 2027* — [링크](https://www.digitimes.com/news/a20260409PD229/cxmt-hbm-production-2027-market.html)
- Digital Today, *China Low-Spec HBM Front Expands* — [링크](https://www.digitaltoday.co.kr/en/view/57201/china-led-low-spec-hbm-front-expands-raising-concerns-over-impact-on-korean-memory-profits)
- Tom's Hardware, *Chinese HBM3 Production Gears Up* — [링크](https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly)

### TSMC 패키징
- TrendForce, *TSMC CoPoS Pilot Line* (2026.04) — [링크](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)
- SiliconAnalysts, *TSMC Foundry Allocation 2026* — [링크](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026)
- DIGITIMES, *TSMC Expands CoWoS and SoIC* — [링크](https://www.digitimes.com/news/a20260514PD237/tsmc-cowos-soic-capacity-packaging.html)
- Oplexa, *AI Chip Packaging Bottleneck 2026* — [링크](https://oplexa.com/ai-chip-packaging-bottleneck-2026/)

### 글로벌 기업 실적·공시 (추가)
- TSMC Q1'26 — [Manufacturing Dive](https://www.manufacturingdive.com/news/tsmc-q1-2026-revenue-q2-guidance-ai-arizona/817728/), [Kalkine](https://www.kalkine.com/news/technology/tsmc-q1-2026-surge-can-ai-demand-sustain-30-growth-outlook)
- ASE Q1'26 — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-ase-technology-q1-2026-results-miss-eps-forecasts-93CH-4643872), [AlphaPilot](https://www.alphapilot.tech/discover/ase-technology-forecasts-3-5-billion-advanced-packaging-revenue-by-2026-amid-ai-demand)
- SPIL 공장 인수 — [TrendForce](https://www.trendforce.com/news/2026/06/11/news-ases-spil-acquires-nt2-8b-plant-amid-spillover-demand-from-tsmc-advanced-packaging-capacity-crunch/)
- Amkor Q1'26 — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000017/amkr3312026erex-991.htm), [36Kr](https://eu.36kr.com/en/p/3580962946874242)
- Micron Q2 FY26 — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000004/a2026q2ex991-pressrelease.htm), [Micron IR](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026)
- Advantest FY25 — [DIGITIMES](https://www.digitimes.com/news/a20260501VL206/advantest-earnings-outlook-revenue-testing.html), [RCR Wireless](https://www.rcrwireless.com/20260130/test-measurement/advantest-rises-with-the-ai-tide)
- BESI Q1'26 — [BESI IR](https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q1-26-results/), [TipRanks](https://www.tipranks.com/news/company-announcements/be-semiconductor-rides-hybrid-bonding-wave-in-earnings)
- Disco FY25 — [Meyka](https://meyka.com/blog/dispf-disco-corporation-earnings-beat-q1-2026-results-2304/), [SemiAnalysis](https://newsletter.semianalysis.com/p/disco-corporation-the-world-leader)
- Applied Materials — [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0000006951/000162828026035071/exhibit991q22026earningsre.htm)
- Ibiden $3.2B 투자 — [Kantenna](https://kantenna.com/topic/ibiden-5-billion-dollar-investment-ai-ic-package-substrate)
- Ajinomoto ABF — [TrendForce](https://www.trendforce.com/news/2026/05/08/news-ajinomoto-ramps-chip-packaging-push-with-%C2%A51-2b-land-buy-for-new-plant-in-2032-abf-margins-top-50-on-ai-boom/), [BigGo Finance](https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE)
- Unimicron — [DIGITIMES](https://www.digitimes.com/news/a20260529PD239/unimicron-revenue-2026-demand-substrate.html), [DIGITIMES](https://www.digitimes.com/news/a20260130PD220/unimicron-abf-substrate-ai-server-market-capacity.html)
- BESI 인수 경합 — [Tiger Brokers](https://www.itiger.com/news/1159006392)
- 하이브리드 본딩 시장 — [TrendForce](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)

### 기존 참조 메모
- `data/note-ai-money-flow_20260618.md` — 투자 프레임워크 (병목/해자/비대칭성)
- `ai-infra/ai_valuechain_deep_dive_20260611.html` — SK하이닉스/마이크론 3군 분류

---

## 10. 향후 과제 (다음 리서치 파일에서)

- [x] `research_hbm_pkg_companies_kr.md`: SK하이닉스·한미반도체·HPSP·리노공업·삼성전자·삼성전기·테크윙·한화세미텍·ISC 재무 심화 (9사, 627줄)
- [x] `research_hbm_pkg_companies_global.md`: TSMC·ASE/SPIL·Unimicron·Micron·Amkor·Applied Materials·Lam Research·Advantest·Disco·Ibiden·Ajinomoto·BESI 재무 (12사, 716줄)
- [x] `research_hbm_pkg_themes.md`: (A) CoWoS 기술전쟁, (B) 하이브리드 본딩, (C) 메모리 사이클·CXMT, (D) 기판/소재 (540줄)

---

## 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-22 | 초안 작성 — 매크로 수요, 밸류체인 6단계, 투자 프레임워크, 사이클 판정, 리스크 R1~R5 |
| 2026-06-22 | 글로벌 기업 데이터 추가 — 대만(TSMC·ASE/SPIL·Unimicron·Nan Ya), 미국(Micron·AMAT·Amkor·Lam), 일본(Advantest·Disco·Ibiden·Ajinomoto·Shinko), 네덜란드(BESI), 오스트리아(AT&S), 중국(CXMT·Naura) |
| 2026-06-22 | 리뷰 반영 — CRITICAL 2건(CoWoS CAPA 통일, 시장규모 역전 설명), HIGH 4건(SK하이닉스 분기 명시, 섹션번호, 밸류체인 정합성, Disco 배치), MEDIUM 4건(한미반도체 조건부 판단, M/S 시점, 출처 보강, BESI 데이터) |
