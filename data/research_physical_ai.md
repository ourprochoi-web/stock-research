# Physical AI 생태계 심층 리서치 노트

**작성일**: 2026-06-28
**분석 범위**: Foundation Model(VLA) · 시뮬레이션/디지털 트윈 · 자율 모빌리티 · 투자 생태계 · 지정학
**검증 파일**: `verified-physical-ai-2026-06-28.md`

---

## 1. Physical AI Foundation Model (VLA 아키텍처)

### 1.1 VLA 연구 폭발

ICLR 2026 VLA 논문: 9편(2025) → **164편**(2026), **18배** YoY 증가
Embodied AI가 학회 내 최고 성장 분야로 부상

### 1.2 주요 모델 비교

| 모델 | 기업 | 파라미터 | 핵심 특징 | 벤치마크 |
|------|------|---------|----------|----------|
| π0.5/π0.6 | Physical Intelligence | 비공개 | Flow-matching diffusion + MEM(장시간 태스크) | 43.7% RoboChallenge |
| GR00T N1.5 | NVIDIA | 2.2B (공개) | 듀얼 시스템 VLA, Apache 2.0 오픈 | 38.3% DreamGen (vs N1 13.1%) |
| GR00T N1.7 | NVIDIA | 2.2B+ | 20K시간 EgoScale 인간 비디오 사전학습 | 로봇 민첩성 최초 스케일링 법칙 발견 |
| Gemini Robotics 1.5 | Google DeepMind | 비공개 | 크로스 임바디먼트 전이, 15개 벤치마크 SOTA | >2x 일반화 벤치마크 |
| Helix 02 | Figure AI | 비공개 | 전신+개별 손가락 동시 제어 최초 VLA | ~500시간 텔레오퍼레이션 |
| Skild Brain | Skild AI | 비공개 | Omni-bodied: 형태 무관 단일 모델 | 비공개 |
| RFM-1 | Covariant | 8B | 비디오 생성 학습으로 물리 이해 창발 | 3,000만+ 상업 피킹 |

### 1.3 데이터 해자 비교

| 기업 | 실세계 데이터 규모 | 임바디먼트 커버리지 | 배치 맥락 |
|------|-------------------|-------------------|----------|
| Tesla | 80억+ 마일 주행 | 1 차량 + Optimus | 도로 + 공장 |
| Waymo | 수백만 유료 라이드 | AV 전용 | 구조화된 도로 |
| Google DeepMind | OXE 100만+ 궤적 | 22+ 임바디먼트 | 연구 + 랩 |
| NVIDIA | EgoScale 2만+ 시간 | 1,000+ 기업 생태계 | 에코시스템 어그리게이터 |
| Covariant | 3,000만+ 피킹 | 고정 암 창고 로봇 | 상업 3PL |

### 1.4 오픈 vs 프로프라이어터리

**오픈 생태계**: GR00T N1.7(Apache 2.0), OpenVLA(7B), π0(openpi), LeRobot Hub 58,000+ 데이터셋(1년 만에 0→58K)
**프로프라이어터리**: Skild Brain, Helix, RFM-1 — 상업 배치 데이터 우위

### 1.5 크로스 임바디먼트 전이

- 인간+로봇 공동 학습 데이터: 과제 전이 정확도 57% → **78%** (+37%)
- GR00T N1.7 인간 에고센트릭 비디오: 1K→20K 시간으로 민첩성 2배+
- X-VLA(ICLR 2026): 6개 시뮬레이션 + 3개 실제 로봇에서 SOTA

---

## 2. 시뮬레이션 & 디지털 트윈

### 2.1 NVIDIA 3-컴퓨터 아키텍처

| 레이어 | 제품 | 역할 |
|--------|------|------|
| 학습 | DGX GB300 / SuperPOD | 대규모 RL·VLA 모델 학습 |
| 시뮬레이션 | Omniverse + Isaac Sim + Cosmos | 합성 데이터·물리 시뮬·렌더링 |
| 엣지/로봇 | Jetson Thor | 로봇 온보드 밀리초 추론 |

- Omniverse **300만+** 등록 사용자, 기업용 $4,500/GPU/년
- Isaac Lab 2.2: 단일 RTX A6000에서 **~90,000 FPS** 학습 처리량
- Cosmos 3 (2026.06.01): **20조** 멀티모달 토큰, ~10억 이미지, 4억 비디오

### 2.2 디지털 트윈 시장

| 연구기관 | 2025 기준 | 2030 전망 | CAGR |
|---------|---------|---------|------|
| MarketsandMarkets | $21.14B | $149.81B | 47.9% |
| GrandView Research | $35.82B | — | 41.3% |
| Mordor Intelligence | — | $122.24B | 32.4% |

컨센서스 중간값: **$140~195B** (2030), CAGR **40~48%**

**산업별**: 제조 32.5%+(최대), 헬스케어 CAGR 52.7%(최고 성장)

### 2.3 산업 소프트웨어 통합

- **Siemens**: Altair $10B 인수(2025.03) — 역대 최대, DT 매출 추정 >$1.4B
- **Dassault**: 3DEXPERIENCE Cloud +41% YoY, NVIDIA 파트너십
- **Ansys(Synopsys)**: FY2026E ~$2.9B, Omniverse 통합
- ABB+FANUC+KUKA+Yaskawa: 합산 설치 200만+ 대 로봇, Isaac Sim 프레임워크 통합

### 2.4 Sim-to-Real 전이

**제로샷 성공 사례 (2025~2026)**:
- 문 열기: 인간 텔레오퍼레이터 대비 **+31.7%** 완료율
- DexFlyWheel: 3회 반복으로 16.5% → **78.3%** 실세계 성공률 (궤적 다양성 25배↑)
- 물체 도달: 적대적 지각 전이로 **97.8%** 성공

**미해결 과제**: 변형 가능 물체, 장기 다단계 태스크, 센서 노이즈 모델링

### 2.5 합성 데이터

- 시장: $600~765M (2025), CAGR **35~36%**
- InternData-A1: 합성 전용 VLA 사전학습이 최대 실세계 데이터셋과 **동등 성능** 달성
- Synthetica(NVIDIA): 270만 합성 이미지 → 객체 감지 SOTA, 9배 빠른 추론
- 3D Gaussian Splatting: **100+ FPS** 렌더링, FastGS 100초 내 학습

---

## 3. 자율 모빌리티 & 산업 AI

### 3.1 로보택시

| 기업 | 주간 라이드 | 도시 수 | 기업가치 | 핵심 |
|------|-----------|--------|---------|------|
| Waymo | **500K** | 10 US | $126B | 10x 안전 개선, $29.99/월 구독 |
| Baidu Apollo | **250K+** | ~20 중국 | — | Q3 2025 310만 완전 자율 주문 |
| Pony.ai | — | 20+ 글로벌 | — | 광저우·선전 도시 단위 BEP 달성 |

- Tesla FSD: 여전히 ADAS(L2+), 비감독 소비자 배치 Q4 2026으로 재연기
- Cruise: 2024.12 로보택시 사업 중단, 개인용 AV로 피벗
- 로보택시 TAM: $1.5B(2025) → $105~403B(2035E), CAGR 27~75%

### 3.2 드론

- **Skydio**: $4.4B 기업가치, 미 육군 $52M 계약(역대 최대 단일 sUAS)
- **DJI**: FCC 금지(2025.12), 글로벌 점유율 70~80%이나 미국 신규 진입 차단
- **드론 배송**: Wing 35만+, Zipline 100만+ 배송, Amazon Prime Air 휴스턴 진출
- 시장: $4.2B(2026) → $12B(2030), CAGR 38%

### 3.3 eVTOL / UAM

- **Joby**: FAA Stage **4/5** (최선두), $1.2B+ 현금, 2026 말 상업 운항 목표
- **Archer**: FAA Stage 3, UAE 상업 런칭 포지셔닝
- **Lilium**: 이중 파산(2024~2025), €1.5B 자본 소멸
- UAM 시장: $4.59B(2024) → $23.47B(2030), CAGR ~31%

### 3.4 창고 로보틱스

- Amazon: **100만+** 배치 로봇(2025.07 돌파), DeepFleet AI 피킹당 이동 10%↓
- Symbotic: Walmart ASR 부문 $200M 인수 + $520M 투자
- Locus Robotics: 30억+ 피킹 완료, 생산성 30~180%↑
- 시장: $9~15B(2026) → $24~65B(2031~2033)

### 3.5 자율 채광/농업/건설

- **채광**: $4.56B(2026), Caterpillar+Komatsu 혼합 차량단 자율 운반 200만+ 톤 8개월
- **농업**: $75.1B(2026), John Deere 전국 완전 자율 경운 런칭
- **건설**: $5.31B(2025) → $9.49B(2030), Caterpillar "차세대 자율" 발표

### 3.6 센서 스택

NVIDIA DRIVE Hyperion: 14 카메라 + 9 레이더 + 1 LiDAR(Aeva 4D) + 12 초음파
Tesla: 카메라 전용(8대) — L4+ 안전 필수 분야에서는 업계 컨센서스 부족
DRIVE AGX Thor: **2,000 TOPS** (Orin 254 TOPS 대비 7.9x)

---

## 4. Physical AI 투자 생태계

### 4.1 VC 펀딩

- 2025년: 로보틱스 $27.6B (전년 $13.7B의 2배)
- **H1 2026**: $18.8B (좁은 정의), $55.8B (넓은 정의) — 이미 역대 연간 기록 초과
- 로봇 FM 스타트업만 2025년 $2.2B+, Q1 2026 월드 모델 기업에 $6B 유입

### 4.2 주요 펀딩 라운드

| 기업 | 카테고리 | 총 조달 | 최근 기업가치 | 연도 |
|------|---------|--------|-------------|------|
| Waymo | AV L4 | $42B+ | $126B | 2026.02 |
| Figure AI | 휴머노이드 | ~$1.9B | $39B | 2025 |
| Skild AI | 로봇 FM | ~$1.7B+ | $14B | 2026.01 |
| Physical Intelligence | 로봇 FM | ~$1.07B+ | $11B | 2025~2026 |
| AgiBot | 휴머노이드 | ~$83.8M | $5.1~6.4B (IPO 목표) | 2025 |
| Galbot | 모바일 매니퓰레이터 | ~$800M | $3B | 2025.12 |

### 4.3 빅테크 전략

| 기업 | 전략 | 핵심 자산 |
|------|------|----------|
| NVIDIA | 풀스택 인프라 | Isaac+Omniverse+Cosmos+GR00T+Jetson |
| Google | FM 라이선싱 | Gemini Robotics+Genie 3+OXE |
| Amazon | 대량 배치 | 100만+ 창고 로봇+Agility 투자 |
| Tesla | 수직 통합 | FSD 데이터+Optimus+AI5 칩 |
| Microsoft | 클라우드 인프라 | Azure+Bonsai+Figure 투자 |
| Apple | 물리 AI 철수 | Titan $10B+ 소실, Vision Pro로 피벗 |
| Meta | 연구 중심 | Ego4D+Habitat, 상업 제품 미발표 |

### 4.4 가치 사슬 가치 포착

| 레이어 | 대표 기업 | 밸류에이션 멀티플 |
|--------|---------|-----------------|
| 칩/컴퓨트 | NVIDIA, Huawei | 최고 (70~80% GM) |
| 시뮬/합성 데이터 | NVIDIA Omniverse | 높음 (SW 멀티플) |
| FM 소프트웨어 | Skild, PI | 높음 (10~50x) |
| 시스템 통합 | Figure, Agility | 중~저 (2~5x) |
| 하드웨어/액추에이터 | Unitree, 범용 OEM | 저 |

### 4.5 중국 Physical AI 생태계

- 글로벌 휴머노이드 출하의 **~90%** (2025년 ~16,000대 중 ~14,400대)
- **AgiBot**: 5,168대(39% 점유), 2026.03 누적 10,000대, HK IPO 목표 $5~6B
- **Unitree**: ~5,500대, 2025 매출 ¥1.708B(+335%), G1 $16K, 상하이 IPO $610M
- **UBTech**: Walker S2 양산, 주문 >800M 위안, 시총 ~$7.93B
- **정부 지원**: NDRC $137B(20년), 직접 보조금 >$20B, 40+ 국가 로봇 훈련 센터

### 4.6 지정학

**미-중 비대칭 경쟁**:
- 미국: FM 품질 #1, 사적 자본 12x, 컴퓨트 용량 9x
- 중국: 출하량 #1(~90%), 정부 지원 #1, 제조 원가 우위(Unitree $16K vs 미국 $150K+)

**규제 분기**:
- EU AI Act(2026.08.02 전면 적용): 휴머노이드 = "고위험 AI 시스템"
- US Humanoid ROBOT Act(2025.11 제안): 중국 기업 연방 조달 금지
- 중국: 배치 우선, 안전 기준 후속

### 4.7 TAM 전망

Physical AI 통합 시장 (로봇+AV+드론+산업+시뮬): **$430~600B** (2030), **$1~1.6T** (2035~2040)

| IB | 휴머노이드 TAM | 시점 | 비고 |
|----|--------------|------|------|
| Goldman Sachs | $38B | 2035 | 하드웨어 매출 기준 |
| Morgan Stanley | $5T | 2050 | HW+공급망+서비스 포함 |
| Citi | $7T | 2050 | 650M 대 기준 |

Physical AI FM 시장(SW 레이어): $4.8B(2025) → $76.2B(2034), CAGR **37.6%**

---

## 기존 보고서 연결점

| 기존 보고서 | 연결 포인트 |
|-------------|------------|
| `robot/robot_overview.html` | 휴머노이드 TAM → FM 소프트웨어 레이어 부가 |
| `robot/robot_company_tsla_figure_agility.html` | Tesla FSD→Optimus 데이터 브리지, Figure Helix VLA |
| `robot/robot_company_kr.html` | K-Humanoid → 컴포넌트 공급망 전략 |
| `robot/robot_theme_supply_chain.html` | 가치 사슬 → SW가 HW 대비 5~50x 멀티플 |
| `robot/robot_investment_map.html` | VC 펀딩 → H1 2026 $18.8B 초슈퍼사이클 |
| `physical-ai/physical-ai-investment-map_1.html` | Omniverse+Cosmos+Isaac 인프라 스택 심층 |
| `ai-infra/ns_bigtech_capex_roi.html` | 빅테크 Physical AI 전략 비교 |
| `ai-infra/ns_ai_defense_nexus.html` | 군사 드론(Skydio), 자율 채광 연결 |

---

## 핵심 출처 (선별)

1. [NVIDIA GR00T N1.7 — Hugging Face](https://huggingface.co/blog/nvidia/gr00t-n1-7)
2. [NVIDIA Cosmos 3 Launch](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai)
3. [Physical Intelligence $11B — TechCrunch](https://techcrunch.com/2026/03/27/physical-intelligence-is-reportedly-in-talks-to-raise-1-billion-again/)
4. [Skild AI $14B — TechCrunch](https://techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/)
5. [Waymo $126B — CNBC](https://www.cnbc.com/2026/02/02/waymo-announced-16-billion-fundraising-round.html)
6. [Robotics VC H1 2026 — TechTimes](https://www.techtimes.com/articles/319037/20260625/robotics-vc-breaks-annual-records-midyear-why-physical-ai-commands-software-multiples.htm)
7. [Digital Twin Market — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/digital-twin-market-225269522.html)
8. [VLA at ICLR 2026 — Moritz Reuss](https://mbreuss.github.io/blog_post_iclr_26_vla.html)
9. [Gemini Robotics — DeepMind](https://deepmind.google/blog/gemini-robotics-brings-ai-into-the-physical-world/)
10. [A16Z Physical AI Deployment Gap](https://www.a16z.news/p/the-physical-ai-deployment-gap)

---

*본 리서치 노트는 2026-06-28 기준 4개 병렬 에이전트(Foundation Model, 시뮬레이션/디지털트윈, 자율모빌리티/산업AI, 투자생태계)로 수집·분석하여 작성됨.*
