# AI 반도체 설계: GPU vs ASIC vs NPU 심층 리서치 노트

**작성일**: 2026-06-28
**분석 범위**: NVIDIA GPU 로드맵 · Broadcom/Google/Amazon/Meta 커스텀 ASIC · 한국 NPU(FuriosaAI·Rebellions) · 중국 대안(Huawei Ascend) · 시장 구조
**검증 파일**: `verified-ai-semiconductor-2026-06-28.md`

---

## 1. NVIDIA GPU 아키텍처 & 로드맵

### 1.1 세대별 스펙 비교

| 항목 | H100 | B200 (Blackwell) | B300 | R100 (Rubin) | Rubin Ultra |
|------|------|-------------------|------|--------------|-------------|
| 공정 | TSMC 4nm | TSMC 4NP | TSMC 4NP | TSMC 3nm | TSMC 3nm |
| 트랜지스터 | 80B | 208B | — | 336B | — |
| HBM | HBM3 80GB | HBM3e 192GB | HBM3e 288GB | HBM4 288GB | HBM4E 1TB |
| 메모리 BW | 3.35 TB/s | 8.0 TB/s | 8.0 TB/s | 22 TB/s | 32 TB/s |
| FP8 | 4,000 TFLOPS | 9,000 TFLOPS | 7,000 TFLOPS | — | — |
| FP4 | — | 18,000 TFLOPS | 15,000 TFLOPS | 50 PFLOPS | ~100 PFLOPS |
| TDP | 700W | 1,000W | 1,400W | — | 3,600W |
| NVLink | 0.9 TB/s | 1.8 TB/s | 1.8 TB/s | 3.6 TB/s | 3.6 TB/s |

- **FP4 컴퓨트 경로**: B200 (9 PFLOPS) → R100 (50 PFLOPS) → Rubin Ultra (~100 PFLOPS) — **2세대 만에 11배**
- **메모리 BW**: B200→Rubin Ultra **4.0배** 증가
- **NVLink**: 세대마다 정확히 **2배** 스케일링

### 1.2 전력 효율

| 세대 | FP8 TFLOPS/W | vs H100 |
|------|-------------|---------|
| H100 | 5.71 | — |
| B200 | 9.00 | **+57.5%** |
| B300 (FP4) | 10.71 | +87.6% |

- GB200 NVL72: **132kW/랙**, 직접 수냉 필수
- Rubin Ultra Kyber 랙: **~600kW**, 800V DC 배전 필요 → 시설 Capex 장벽
- LLM 추론 기준 H100 대비 B200: **4.6배** 줄/토큰 효율 향상

### 1.3 NVIDIA 실적

- **Q1 FY27** (2026.04): 매출 $81.6B (+85% YoY), DC $75.2B (+92.3% YoY)
- DC = 전체 매출의 **92.2%**
- 영업마진 ~**66%** at $81.6B/분기
- 시총 **$4.663T**, trailing P/E **29.98x** (12개월 평균 45.95x 대비 -34.8% 압축)
- 상위 2개 고객 = 매출의 **39%** (Q2 FY26)

### 1.4 CUDA 에코시스템 해자

- 개발자 **~590만 명**, 20년 라이브러리 축적
- MFU(Model FLOPS Utilization): CUDA **50~55%** vs AMD ROCm ~45%
- 전환 비용: 워크로드 CUDA 의존도에 따라 **30~99% 성능 패널티**
- Triton(OpenAI) 등 추상화 시도 있으나 CUDA 생태계 대체 불가

---

## 2. 커스텀 ASIC & AI 실리콘

### 2.1 Broadcom

- **FY2026 AI 반도체 매출 $56B** (+180% YoY)
- Q3 FY2026 가이던스: $16B (+200%+ YoY)
- AI 백로그: **$73B** (이례적 가시성)
- 확인된 XPU 고객 6사: Google, Meta, OpenAI, Anthropic, Apple, ByteDance
- **3.5D F2F 패키징**: 4 컴퓨트 다이 + 1 I/O 다이 + HBM 12모듈, 6,000mm² 적층 — 업계 최초
- TSMC 3nm 현재, 2nm 이미 2개 하이퍼스케일러와 테이프아웃

### 2.2 Google TPU

| 세대 | 핵심 스펙 | 상태 |
|------|-----------|------|
| v6e (Trillium) | 918 BF16 TFLOPS, 32GB HBM, 1.6 TB/s | GA, 3개 리전 매진 |
| v7 (Ironwood) | 4,614 FP8 TFLOPS, 192GB HBM3E, 7.37 TB/s, 9,216칩 슈퍼팟 = 42.5 ExaFLOPS | 2025~2026 배치 |
| v8t/v8i | Training/Inference 분리; v8t 슈퍼팟 121 ExaFLOPS(FP4); v8i 384MB SRAM, 2nm | H2 2026 GA |

- TPU v6e: NVIDIA H100 추론 대비 **$/성능 4배** 우위
- **TPU 라인 최초로 Training(v8t)/Inference(v8i) 분리** — 구조적 전환 신호

### 2.3 Amazon Trainium

- **Trainium3** (GA 2025.12): 칩당 2.52 PFLOPS, 144GB HBM3e, 4.9 TB/s, TSMC N3P
- Trn3 UltraServer (144칩) = 362 PFLOPS
- **Project Rainier**: Anthropic Claude 훈련용 Trainium2 **50만 개** 배치

### 2.4 Meta MTIA

- 2년간 4세대(MTIA 300/400/450/500) — **6개월 케이던스** (업계 표준 18~24개월)
- MTIA v3 "Iris": TSMC 3nm, 8x HBM3E, >3.5 TB/s, 2026.02 브로드 DC 배치
- Broadcom과 2nm MTIA 450/500 위한 **1GW 계약**
- GPU 대비 TCO: **-44%**
- 전략: MTIA=추론, NVIDIA/AMD=프론티어 사전학습 (완전 대체 아님)

### 2.5 커스텀 실리콘 경제성

| 공정 | NRE 비용 | 웨이퍼 비용 |
|------|---------|-----------|
| 5nm | ~$449M | $16~18K |
| 3nm | ~$581M | $20~22K |
| 2nm | ~$725M | $28~30K |

- **손익분기점**: 연 GPU 지출 $500M+ 이상 시 커스텀 ASIC 경제적
- 페이백: 1.5~2.5년, TCO 우위 **40~65%**
- Time-to-market 불리: GPU 대비 **18~24개월** 늦음 (AI 칩레이아웃, 모듈러 칩렛으로 완화 중)

### 2.6 시장 구조

- JPMorgan 전망: **2027년 ASIC 출하량이 GPU 초과** (12.5M vs 10.9M)
- Broadcom **60~85%** + Marvell 10~25% = ASIC 설계 시장 **~95% 과점**
- TSMC CoWoS: 2026년 **85%+ 사전 약정**, NVIDIA가 60%+ 앵커 → 커스텀 ASIC은 나머지 15% 경쟁

---

## 3. 한국 AI 반도체 기업

### 3.1 FuriosaAI (퓨리오사AI)

- **RNGD(Renegade)**: 5nm TSMC, 512 TOPS INT8, 180W
- DGX H100 대비 랙 밀도 **3.5배** (3kW vs ~10kW/서버)
- LG AI Research(EXAONE) 앵커 고객 — EXAONE 추론 기준 **2.25배** 전력효율 우위
- Meta $800M 인수 제안 **거절** (2025.03)
- Series D ($300~500M) 진행 중, **2027년 IPO** 목표 ($1B+ 밸류에이션)
- 창업자 백준호: ex-AMD/Samsung

### 3.2 Rebellions (리벨리온, Sapeon 합병 완료)

- **Rebel100**: 2 PFLOPS, 쿼드 칩렛 NPU, Samsung SF4X, 144GB HBM3E, 4.8 TB/s
- H200 동급 성능, H100 대비 TPS/W **3.2배** 우위 (자체 발표)
- 총 투자: **$850M+**, Pre-IPO 밸류에이션 **$2.34B** (2026.03)
- 합병 후 밸류에이션 2.75배 상승 ($929M → $2.34B, 15개월)
- **KOSPI IPO** Q3 2026 예비심사 (JPMorgan 주관)
- 2nm REBEL: Samsung Foundry SF2로 개발 중

### 3.3 Samsung Foundry (삼성 파운드리)

- 글로벌 파운드리 점유율: **7.3%** vs TSMC **70.2%** (Q2 2025)
- **3nm 수율 ~50%** vs TSMC ~90% — **40pp 격차** → 고객 이탈
- **2nm(SF2)**: 2025.11 양산 개시, 수율 55~60% (개선 중)
- Tesla AI6 $16.5B 계약 — 헤드라인 고객 확보
- TSMC 대비 **62.7pp** 점유율 격차

### 3.4 DeepX

- **DX-M1**: 25 TOPS at 3~5W, Samsung 5nm, 물리적 AI(로봇·팩토리) 타겟
- 현대/기아 Robotics LAB 앵커 파트너
- **DX-M2**: 2nm Samsung SF2 (최초 상용 SF2 고객), 2027 양산 목표
- IPO 계획 2026, ~**$700M** 밸류에이션

### 3.5 정부 정책

- 2026년 AI 예산: **10.1조원** ($7.27B, +57.8% YoY)
- K-NVIDIA 이니셔티브: AI 30조 + 반도체 21조원 (국가성장펀드 150조 중)
- 반도체 생태계 총 **700조원** ($534B, ~2047년)
- 반도체 특별회계 2조원은 **2027년**부터 가동
- **한계**: 공공기관이 K-NVIDIA 정책에도 불구하고 여전히 NVIDIA 선택

---

## 4. NPU 생태계 & 중국 AI 반도체

### 4.1 시장 규모

- 글로벌 AI 가속기 시장: $140.55B(2024) → **$440.30B(2030)**, CAGR 25%
- DC 반도체가 전체 반도체의 **~48%** 도달 전망 (2030, $843B)
- 클라우드/DC가 2024년 AI 가속기 지출의 **75%**, 엣지가 CAGR **27%**로 최고 성장

### 4.2 엣지/모바일 NPU

| SoC | NPU TOPS | 세대 향상 |
|-----|----------|-----------|
| Qualcomm X2 Elite Extreme (Hexagon NPU 6) | **80 TOPS** | +78% vs X Elite |
| MediaTek Dimensity 9500 | **100 TOPS** | 안드로이드 최고 |
| Apple M5 | TOPS 비공개 | GPU 중심 전환, LLM 프롬프트 4배 |

- 온디바이스 AI 추론 시장: $26.14B(2025) → **$58.90B(2030)**, CAGR 17.6%

### 4.3 Huawei Ascend

- **Ascend 910C**: H100 추론 성능의 **~60%** (칩 단위)
- **CloudMatrix 384** (910C 384개): 300 PFLOPS BF16 — GB200 NVL72(180 PFLOPS) 대비 **시스템 레벨 +67%**, HBM 3.6배
- 중국 국산 AI칩 점유율: 2025년 유닛 기준 **41%** (사상 최초 돌파)
- Huawei Ascend **81.2만 대** (전체 20% 점유)
- NVIDIA 중국 점유율: ~95% → **~55%** 하락
- Jensen Huang(2026.05): "중국 AI칩 시장은 Huawei에 **사실상 양보**"

### 4.4 기타 중국 업체

- **Cambricon(寒武纪)**: MLU590 (7nm, 192GB HBM2e, ~780 TFLOPS FP8). 2025년 **7년 만에 첫 흑자**, 매출 +453% YoY. 2026년 50만대 목표
- **Biren(壁仞)**: 제재 영향으로 BR100 생산 차질
- **Enflame(燧原)**: CloudBlazer 시리즈, 국영기업 중심 납품
- **Moore Threads(摩尔线程)**: 게이밍+DC GPU, 제한적 AI 역할

### 4.5 수출 통제 영향

- H20 금지(2025.04): NVIDIA **$5.5B 감손** + $2.5B 매출 손실 = 단일 분기 ~**$8B** 영향
- SMIC N+2(7nm) 수율: **20~40%** vs TSMC EUV 7nm ~80~85% — **40~65pp 격차**
- SMIC 5nm 파일럿 수율 ~20% — **영구적 18~24개월 공정 격차**, 다이당 비용 2~3배

### 4.6 추론 vs 훈련 시장 전환

- 추론 지출 비중: 40%(2024) → **65~70%(2028E)** — +25~30pp 전환
- AI 추론 시장: $106.15B(2025) → **$254.98B(2030)**, CAGR 19.2%
- NVIDIA 훈련 점유율 **~90%**, 추론 **60~75%** — 추론에서 ASIC/NPU 침투 가속

### 4.7 차세대 아키텍처

| 분야 | 대표 기업 | 핵심 스펙 |
|------|-----------|-----------|
| 포토닉 컴퓨팅 | Lightmatter | Series D $400M, $4.4B 밸류에이션, Passage M1000 114Tbps |
| 뉴로모픽 | Intel Loihi 3 | 10M 뉴런, GPU 대비 **100배** 에너지 효율 (SNN 태스크) |
| 뉴로모픽 | IBM NorthPole | 256M 시냅스, H100 대비 **25배** 효율 (이미지 인식) |
| RISC-V AI | Tenstorrent | Series D $693M (삼성증권 리드), 삼성·LG·현대 라이선스 |

- **한계**: 뉴로모픽·포토닉은 트랜스포머 기반 LLM에 비효율 → 2026년 주류 워크로드 적용 제한적

---

## 5. 시장 구조 종합

### 5.1 NVIDIA 점유율 전망

| 세그먼트 | 2024 | 2026E | 2030E |
|----------|------|-------|-------|
| AI 훈련 | ~90% | ~88% | ~80% |
| AI 추론 | ~70% | ~65% | ~55% |
| 전체 AI 가속기 | ~85~90% | ~75% | ~65~70% |

### 5.2 ASIC 성장 vs GPU

- 2026년: ASIC 출하량 +45%, GPU 출하량 +16% → ASIC/GPU 성장비 **2.8배**
- 2027년 ASIC 출하량 GPU 초과 전망 (JPMorgan)
- 하이퍼스케일러 4사 AI CapEx 2026: 합산 **$695B** (+76.8% YoY)
  - Amazon $200B, Microsoft $190B, Google $180B, Meta $125B

### 5.3 한국 반도체 포지셔닝

| 기업 | 강점 | 약점 |
|------|------|------|
| FuriosaAI | 전력효율 3.5배, Meta 거절 = 독립 의지 | 고객 다변화 부족, CUDA 생태계 vs 자체 SDK |
| Rebellions | Rebel100 성능, IPO 모멘텀, 삼성 파운드리 연계 | 성능 자체 발표 (MLPerf 미검증) |
| Samsung Foundry | 2nm 선행, TSMC 대안 유일 | 3nm 수율 격차 40pp, 고객 신뢰 적자 |
| DeepX | 엣지 AI 특화, 현대/기아 파트너 | DC 시장 진입 무관, 규모 제한 |

---

## 기존 보고서 연결점

| 기존 보고서 | 연결 포인트 |
|-------------|-------------|
| `research_ai_framework_selection.md` | GPU/ASIC 스코어카드 → Broadcom $56B·TPU v8 분리 데이터 보강 |
| `research_ai_framework_money_flow.md` | NVIDIA DC $75.2B → Q1 FY27 업데이트 |
| `hbm-packaging/` 시리즈 (11편) | HBM4/HBM4E → Rubin 통합 + CoWoS 85% 사전약정 |
| `ns_semiconductor_war.html` | Samsung Foundry 3nm 수율 50%·2nm 선행 데이터 추가 |
| `ai-infra/` 시리즈 (5편) | GB200 NVL72 132kW·Rubin Ultra 600kW 전력 데이터 |

---

## 핵심 출처 (선별)

1. [NVIDIA Q1 FY27 Earnings — $81.6B Revenue](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-first-quarter-fiscal-2027)
2. [Broadcom FY2026 AI Revenue — $56B Guide](https://investors.broadcom.com/)
3. [Google TPU v7 Ironwood — 42.5 ExaFLOPS](https://cloud.google.com/blog/products/ai-machine-learning/introducing-ironwood-our-7th-generation-tpu)
4. [Amazon Trainium3 — 2.52 PFLOPS/chip](https://aws.amazon.com/machine-learning/trainium/)
5. [Meta MTIA v3 Iris — 6-Month Cadence](https://ai.meta.com/blog/meta-mtia-custom-silicon-chip-ai-inference/)
6. [FuriosaAI RNGD Specs](https://furiosa.ai/renegade-spec)
7. [Rebellions Rebel100 — ISSCC 2026](https://www.tomshardware.com/tech-industry/semiconductors/isscc-2026-rebellions-ucie-rebel-100)
8. [Samsung Foundry 3nm Yield 50% vs TSMC 90%](https://www.design-reuse.com/news/202528876)
9. [Huawei CloudMatrix 384 — SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72)
10. [NVIDIA H20 $5.5B Charge — CNN](https://www.cnn.com/2025/04/16/tech/nvidia-plunge-h20-chip-china-export-intl-hnk/)
11. [JPMorgan ASIC > GPU 2027 Forecast](https://www.jpmorgan.com/insights/technology/ai-infrastructure)
12. [Tenstorrent $693M Series D — Samsung Securities](https://tenstorrent.com/press-release/tenstorrent-series-d/)

---

*본 리서치 노트는 2026-06-28 기준 4개 병렬 에이전트(NVIDIA GPU, ASIC/커스텀실리콘, 한국AI반도체, NPU/중국)로 수집·분석하여 작성됨.*
