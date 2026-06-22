# 로봇/휴머노이드 투자 테마 심층 리서치
**작성일**: 2026년 6월 23일
**분류**: 로봇 | 휴머노이드 | 부품 서플라이체인 | 체화 AI
**커버리지**: Theme A (경제학) · Theme B (두뇌/AI) · Theme C (부품 밸류체인)

---

## 목차

1. [Theme A — 휴머노이드 경제학: 단가 $20K는 가능한가](#theme-a)
2. [Theme B — 로봇 두뇌: Foundation Model과 Embodied AI](#theme-b)
3. [Theme C — 부품 서플라이체인: 감속기에서 액추에이터까지](#theme-c)
4. [통합 밸류체인 맵 및 종합 시사점](#integrated)

---

## Theme A — 휴머노이드 경제학: 단가 $20K는 가능한가 {#theme-a}

### 1. 시장 개요 및 규모

휴머노이드 로봇 시장은 2026년 현재 상용화 초입 단계다. 2025년 글로벌 출하량은 전년 대비 480% 급증한 13,318대를 기록했으나, 절대 규모는 여전히 미미하다. Goldman Sachs는 2035년 시장 규모를 $380억으로 전망하며, 이는 당초 예측($60억) 대비 6배 이상 상향 조정된 수치다.

| 지표 | 2025 (실적) | 2028E | 2030E | 2035E |
|------|------------|-------|-------|-------|
| 시장 규모 | <$10억 | ~$30억 | ~$100억 | $380억 (GS) |
| 출하량 (대) | ~13,318 | ~100K | ~250K (GS 기준) | 140만 (GS) |
| 평균 단가 (BOM 추정) | $32K–$80K | $25K–$40K | $17K 미만 | $10K 이하 |
| CAGR (2026→2035) | — | — | — | ~137% |

**출처**: Goldman Sachs Humanoid Robot Market Report, Yole Group (2025), RoboZaps (2026)

---

### 2. BOM(자재명세서) 구조 분석

현재 휴머노이드 로봇 BOM의 가장 큰 특징은 **액추에이터 비중의 압도적 우위**다. 2025년 기준 중국산 휴머노이드 BOM은 약 $35,000, 글로벌 평균은 $40,000~$80,000 범위로 추산된다.

| 부품 카테고리 | 비중 (2025) | 비중 (2030E) | 주요 내용 |
|-------------|------------|-------------|---------|
| 액추에이터 (회전+선형) | ~40–50% | ~51% (선형 27%+회전 24%) | 감속기+모터+드라이버 포함 |
| 센서 (비전/포스/IMU) | ~15% | ~12% | LiDAR, 카메라, 촉각 센서 |
| 배터리/전력 | ~12% | ~10% | 1~8시간 구동, 멀티시간 배터리 표준화 |
| 컴퓨트 (AI 칩/GPU) | ~8–10% | ~5% | AI 칩 원가 하락 기대 |
| 구조체/프레임 | ~8% | ~7% | 경량 알루미늄·탄소섬유 |
| 기타 (배선/소프트웨어 등) | ~15% | ~15% | 시스템 통합, 소프트웨어 |

**핵심**: 액추에이터 원가 절감이 전체 BOM 하락의 핵심 레버. Tesla Optimus는 대당 28개 액추에이터(회전 14개+선형 14개)를 탑재하며, 선형 액추에이터(행성 롤러 스크류) 단가는 개당 $1,350~$2,700 수준.

---

### 3. BOM 하락 경로: 3대 드라이버

#### (1) Tesla 내재화 전략
Tesla는 Optimus 액추에이터를 자체 설계하여 외부 공급망 의존도를 낮추고 있다. 회전형 액추에이터에는 프레임리스 토크 모터 + 하모닉 드라이브, 선형 액추에이터에는 행성 롤러 스크류를 채택했다. Tesla의 Dojo 슈퍼컴퓨터와 FSD 기술을 Optimus에 전용하여 AI 개발 비용을 자동차 사업과 분산(amortize)하는 구조다. 이로 인해 AI 컴퓨트 원가의 구조적 하락이 가능하다.

#### (2) 중국 공급망의 가격 경쟁
Suzhou Green Harmonic(绿的谐波, Leaderdrive)은 일본 하모닉드라이브 대비 30~40% 저렴한 가격으로 Tesla에 공급 중이며, Tesla Optimus 감속기 시장의 60% 점유를 목표로 한다. 2025년 Leaderdrive 매출은 전년 대비 47% 증가한 5억 7,070만 위안을 기록했다. 중국 내 저가 경쟁이 글로벌 부품 단가 하락을 견인한다.

#### (3) 규모의 경제
Goldman Sachs는 BOM 하락 속도가 연 40%(과거 예측 15~20% 대비 2배 이상)임을 확인했다. 2030년까지 BOM이 현재의 절반 이하인 $17,000 미만으로 하락할 것으로 전망된다. 이는 반도체 산업의 무어의 법칙 유사 패턴이다.

---

### 4. 단가 목표: $20K 달성 시나리오

| 주체 | 목표 단가 | 목표 시점 | 비고 |
|------|---------|---------|------|
| Tesla (Elon Musk 발언) | <$20,000 | 2028~2029 | 소비자 판매가 기준 |
| Tesla (초기 기업 판매) | ~$30,000 | 2026 말 예정 | 엔터프라이즈 우선 |
| BOM 원가 전망 (업계 컨센서스) | <$17,000 | 2030 | BOM 기준, 판매가 별도 |
| Goldman Sachs 기준 | $30K~$150K | 현재 | GS 최신 추정치 하향 (기존 $50K~$250K) |

**Goldman Sachs ROI 분석**: 제조업 도입 시 인건비 대비 ROI 1~2년 수준. 연간 $50,000 인건비 대체 시, $30,000짜리 로봇의 회수 기간은 약 8~12개월(유지보수·운영 비용 제외).

---

### 5. 상용화 지연의 역사: Announced vs. Actual

| 기업 | 발표 시점 | 당초 상용화 목표 | 실제 현황 (2026.6) |
|------|---------|--------------|----------------|
| Boston Dynamics (Atlas) | 2016~ | 2020년 상용화 주장 | 산업용 파일럿 단계, Hyundai 인수 후 재설계 |
| Tesla Optimus | 2022년 AI Day | 2023년 공장 투입 | 내부 공장 테스트 중, 외부 판매 미개시 |
| Figure AI | 2023 | 2024년 상용 배포 | BMW 파일럿 ~진행, Figure 03 출시 (2025.10) |
| Agility Robotics (Digit) | 2022 | 2024년 대규모 배포 | Amazon 창고 파일럿 단계 |
| 1X Technologies | 2024 | 2025년 가정용 출시 | 연구·파일럿 단계 |

**패턴**: 발표 후 실제 상용화까지 평균 3~5년 지연. 기술 준비도(TRL)와 실제 고객 요구 사이의 갭이 주요 원인.

---

### 6. 투자 시사점

**단기 (2026~2027)**
- Tesla Optimus 내부 배포 규모(Fremont/Giga Texas) 모니터링 → 연간 생산량 가이던스가 핵심 주가 트리거
- BOM 하락 속도 확인: 감속기·액추에이터 단가 분기별 추이 추적
- 중국 경쟁사 동향: AGIBOT, UBTech, Fourier Intelligence의 출하량·가격 정책

**중기 (2027~2030)**
- $20K 단가 달성 여부가 대중화 티핑포인트
- 제조업 → 물류 → 서비스업 순서로 도입 확대 예상
- 플랫폼 기업(Tesla, NVIDIA) vs 전문 로봇 기업(Figure, Agility) 경쟁 구도 형성

---

### 7. 리스크 요인

| 리스크 | 설명 | 영향도 |
|--------|------|--------|
| 기술 성숙도 지연 | 이족 보행 안정성·파지력 불충분 | 상 |
| 배터리 에너지 밀도 한계 | 1~8시간 구동, 연속 작업 제약 | 중 |
| 규제·안전 인증 | 인간과 공동 작업 환경의 법적 공백 | 중 |
| 가격 경쟁 심화 | 중국산 저가 제품의 품질 미검증 | 중 |
| 고객 채택 속도 지연 | ROI 증명 전 대규모 투자 기피 | 상 |

---

### 8. 모니터링 지표 (KPI)

- Tesla Optimus 분기별 생산 대수 및 내부 배포 현황
- Goldman Sachs/Bank of America 휴머노이드 출하량 분기 업데이트
- 주요 부품(하모닉 드라이브, 액추에이터) 평균 판매단가(ASP) 추이
- Figure AI, Agility Robotics 고객사 수·파일럿 규모 공시
- 중국 AGIBOT·UBTech 출하량 및 수출 현황

---

## Theme B — 로봇 두뇌: Foundation Model과 Embodied AI {#theme-b}

### 1. 시장 개요: 소프트웨어가 하드웨어를 정의하는 시대

2025~2026년 로봇 산업의 가장 큰 구조적 변화는 **범용 파운데이션 모델의 로봇 적용**이다. 과거 로봇은 단일 태스크 전용 프로그래밍 방식이었으나, 대규모 언어모델(LLM)과 비전-언어-액션(VLA) 모델이 범용 로봇 지능을 가능케 하고 있다. Physical Intelligence는 이 분야에서 $4억 이상 조달에 성공했고, NVIDIA는 Isaac GR00T N1을 세계 최초 오픈 휴머노이드 파운데이션 모델로 공개했다.

| 기업 | 모델/플랫폼 | 파라미터 | 특징 | 상태 (2026) |
|------|-----------|---------|------|-----------|
| NVIDIA | Isaac GR00T N1 | 미공개 | 오픈 소스, 시뮬레이션 통합 | 상용 출시 |
| NVIDIA | Cosmos 3.0 | 미공개 | 월드 파운데이션 모델, 합성 데이터 생성 | 발표 |
| Google DeepMind | RT-2 / Gemini Robotics | 55B (PaLI-X) | VLA, 제로샷 일반화 62% | 연구 단계 |
| Physical Intelligence | π0 (pi-zero) | 미공개 | Flow Matching, 양손 조작 SOTA | 상업 API 제공 |
| Figure AI | Helix 02 | 미공개 | 픽셀→토크 엔드투엔드, OpenAI 협업 종료 후 자체 개발 | 배포 중 |
| Tesla | FSD 기반 Optimus AI | 미공개 | 자동차 FSD 기술 전용, Dojo 슈퍼컴 활용 | 공장 내부 배포 |

---

### 2. NVIDIA Isaac/Omniverse 생태계

NVIDIA는 로봇 AI 인프라의 사실상 표준(de facto standard)으로 자리매김하고 있다. CES 2026에서 NVIDIA는 물리 AI 개발 전 주기를 커버하는 오픈 모델·프레임워크 제품군을 발표했다.

**핵심 구성 요소**:

| 컴포넌트 | 역할 | 주요 파트너 |
|---------|------|-----------|
| Isaac GR00T N1 | 휴머노이드 범용 파운데이션 모델 (오픈소스) | ABB, AGIBOT, Agility, Figure, YASKAWA 등 |
| Cosmos 3.0 | 월드 파운데이션 모델: 합성 데이터 생성 + 시뮬레이션 | 산업 전반 |
| Omniverse / OpenUSD | 3D 디지털 트윈 표준, 시뮬레이션→실제 전이 | 글로벌 제조사 |
| Isaac Sim | 고품질 물리 시뮬레이션 환경 | 로봇 개발사 |
| Jetson 플랫폼 | 엣지 AI 추론 하드웨어 | 모든 로봇 OEM |

**전략적 의미**: NVIDIA는 GPU 판매에서 나아가 로봇 AI 개발 플랫폼 전체를 장악하려는 전략을 실행 중이다. Omniverse를 통한 디지털 트윈 표준화는 Sim-to-Real 전이를 가속화한다.

---

### 3. 주요 파운데이션 모델 심층 분석

#### (A) Physical Intelligence π0 (pi-zero)
- **핵심 기술**: Flow Matching 기반 액션 생성. 노이즈에서 액션 분포로의 연속 벡터장 학습
- **강점**: 세탁물 접기·식탁 정리·샌드위치 제작 등 고난도 양손 조작 태스크에서 타 모델 미달성 수준 구현
- **비즈니스 모델**: 비오픈웨이트, 상업 API로 제공 (엔터프라이즈 가격 정책)
- **자금 조달**: $4억+ (Series B 포함)
- **한계**: 폐쇄형 모델로 커스터마이징 제약

#### (B) Google DeepMind RT-2 / Gemini Robotics
- **기반 모델**: PaLI-X (55B 파라미터) 파인튜닝
- **혁신**: 로봇 액션을 텍스트 토큰으로 변환 → 웹 데이터와 로봇 궤적 데이터를 동시 학습
- **성능**: 새로운 물체 62% 성공률, 새로운 배경 55% 성공률 (제로샷)
- **2026 현황**: Gemini Robotics로 업그레이드, 언어 명령 기반 조작 능력 대폭 향상

#### (C) NVIDIA Isaac GR00T N1
- **특징**: 세계 최초 오픈 휴머노이드 파운데이션 모델
- **능력**: 파지, 양팔 물체 이동, 팔 간 물체 전달, 멀티스텝 장기 태스크
- **생태계 통합**: Isaac Sim, Cosmos, Omniverse와 완전 통합
- **접근성**: 오픈소스로 업계 표준화 가속

#### (D) Figure AI Helix 02
- **배경**: 2025년 2월 OpenAI 협업 종료 후 자체 모델 개발로 전환
- **CEO 발언**: "체화 AI를 실제 세계에서 확장하려면 수직 통합이 필수" (Brett Adcock)
- **아키텍처**: 픽셀 입력 → 토크 명령 직접 출력, 내비게이션+조작 단일 신경망
- **학습 방법**: 1인칭 인간 행동 영상 수집 → Helix 학습 → 제로샷 전이
- **현황 (2026)**: Figure 03 출시, BotQ 제조 시설 가동, 기업가치 $390억

---

### 4. Sim-to-Real 전이학습: 핵심 인프라

Sim-to-Real은 시뮬레이션에서 학습한 정책을 실제 로봇에 전이하는 기술로, 데이터 부족 문제를 해결하는 핵심 수단이다.

| 기술 요소 | 설명 | 주요 플레이어 |
|---------|------|------------|
| 도메인 랜덤화 | 시뮬레이션 파라미터 무작위화로 실제 환경 변동성 학습 | NVIDIA, Google |
| 합성 데이터 생성 | Cosmos 등 월드 모델로 무한 훈련 데이터 생성 | NVIDIA Cosmos 3.0 |
| 디지털 트윈 | 실제 환경의 고정밀 가상 복제 | NVIDIA Omniverse |
| 모방 학습 | 인간 시연 데이터로부터 학습 | Physical Intelligence, Figure |
| 강화학습 (RL) | 시뮬레이션 환경에서 보상 기반 학습 | 전 산업 |

**투자 인프라 수요**: 시뮬레이션 인프라는 GPU 수요를 직접 창출한다. 1개 로봇 정책 학습에 수천~수만 GPU-시간이 소요되며, 이는 NVIDIA H100/B100 수요의 새로운 성장 동력이다.

---

### 5. Tesla FSD 기술의 Optimus 전이

Tesla는 자동차 FSD 기술을 Optimus에 전용하는 독특한 전략을 실행 중이다.

| 요소 | 자동차 FSD | Optimus 로봇 |
|-----|---------|------------|
| AI 칩 | FSD Computer | AI5 칩 (2026년 4월 테이프아웃, 로봇·슈퍼컴 우선 배포) |
| 데이터 수집 | 수백만 대 Tesla 차량 | 공장 내 Optimus 데이터 수집 |
| 슈퍼컴퓨터 | Dojo | 동일 Dojo (자원 공유) |
| AI 리더십 | Ashok Elluswamy (FSD VP) | 동일 인물이 Optimus AI도 총괄 (2025.6~) |
| 핵심 역량 | 비전 기반 환경 인식 | 동일 기술 체계 전용 |

**전략적 우위**: Tesla는 수억 달러의 FSD 개발 비용을 자동차와 로봇 사업에 분산시키는 구조로, 타 로봇 기업 대비 AI 개발 원가 구조가 유리하다.

---

### 6. 구조적 영향: Foundation Model의 로봇 산업 재편

**과거**: 로봇 = 하드웨어 집약 사업. SW는 태스크별 전용 코드.
**현재**: 로봇 = HW + 범용 AI 모델. 파운데이션 모델이 다수 태스크를 처리.
**미래**: 범용 로봇 정책 = 하나의 모델로 대부분의 태스크 수행.

이 변화는 **소프트웨어 플랫폼 기업**에 구조적 수혜를 제공한다. NVIDIA처럼 학습 인프라(GPU + 시뮬레이션 플랫폼)를 제공하는 기업이 로봇 AI 산업의 핵심 인프라 레이어를 장악하게 된다.

---

### 7. 투자 시사점

**단기 (2026~2027)**
- NVIDIA의 로봇 AI 플랫폼 매출 비중 확대 모니터링 (Robotics/Physical AI 세그먼트)
- Physical Intelligence, Skild AI 등 로봇 파운데이션 모델 스타트업 IPO 또는 M&A 가능성
- Figure AI $390억 기업가치 → 상장 시나리오 (2026~2027 예상)

**중기 (2027~2030)**
- 파운데이션 모델 API 시장 형성: OpenAI 유사 "로봇 두뇌 SaaS" 비즈니스 모델 등장
- 합성 데이터·시뮬레이션 인프라 수요 급증 → GPU 수요 추가 성장 동력
- 수직 통합 vs 오픈 플랫폼 전략 간 경쟁 결과에 따른 업계 재편

---

### 8. 리스크 요인

| 리스크 | 설명 | 영향도 |
|--------|------|--------|
| Sim-to-Real 갭 | 시뮬레이션 환경과 실제 물리 세계 간 불일치 | 상 |
| 데이터 부족 | 고품질 로봇 조작 데이터의 절대적 부족 | 상 |
| 수직 통합 리스크 | 자체 AI 개발 시 비용 급증, 기술 성숙 지연 | 중 |
| 경쟁 심화 | OpenAI, Google, Meta 등 빅테크의 로봇 AI 진입 | 중 |
| 특허·IP 분쟁 | 핵심 모델 아키텍처 관련 소송 가능성 | 중 |

---

### 9. 모니터링 지표 (KPI)

- NVIDIA 분기 실적: 로보틱스/Physical AI 수익 기여도
- Figure AI, Physical Intelligence 상업 고객 수·ARR 공시
- VLA 모델 벤치마크: 제로샷 성공률, 새로운 태스크 일반화 점수
- 로봇 학습 데이터셋 규모 (오픈소스 Open X-Embodiment 등)
- 시뮬레이션 GPU 수요: NVIDIA Omniverse Enterprise 라이선스 판매량

---

## Theme C — 부품 서플라이체인: 감속기에서 액추에이터까지 {#theme-c}

### 1. 시장 개요: 부품이 상용화를 결정한다

휴머노이드 로봇 상용화의 병목은 소프트웨어가 아니라 **하드웨어 부품의 원가·공급·품질**이다. 감속기(Reducer)는 전체 BOM의 최대 40~60%를 차지하며, 현재 일본 기업이 글로벌 시장을 과점하고 있다. 한국과 중국의 진입이 가속화되고 있으나, 기술 격차와 신뢰성 검증이 핵심 과제다.

**휴머노이드 로봇 감속기 시장 규모**:

| 지표 | 2025 | 2028E | 2032E |
|------|------|-------|-------|
| 시장 규모 | $5,230만 | ~$1.5억 | $5.8억 |
| CAGR | — | — | 46.3% |
| 일반 산업용 하모닉 드라이브 시장 | $18.5억 | — | $45억 (2034E) |

---

### 2. 핵심 부품 밸류체인 구조

```
원자재 (특수강·희토류 마그넷)
        ↓
감속기 (하모닉/사이클로이드/RV)
        ↓
모터 (프레임리스 토크 모터·서보모터)
        ↓
드라이버 (모터 컨트롤러·인버터)
        ↓
액추에이터 모듈 (감속기+모터+드라이버 통합)
        ↓
센서 (IMU·포스·토크·비전)
        ↓
배터리/전력 관리 시스템
        ↓
컴퓨트 보드 (AI 칩·엣지 GPU)
        ↓
로봇 완성품 OEM
```

**감속기 유형별 특성**:

| 유형 | 정밀도 | 토크 밀도 | 주요 용도 | 대표 기업 |
|------|--------|---------|---------|---------|
| 하모닉 드라이브 (Strain Wave) | 최고 | 중간 | 소형 관절, 휴머노이드 | Harmonic Drive SE (일본), Leaderdrive (중국) |
| 사이클로이드 | 높음 | 높음 | 산업용 로봇 대형 관절 | 나부테스코 (일본), 신코 (중국) |
| RV (Rotary Vector) | 높음 | 매우 높음 | 산업용 로봇 베이스 | 나부테스코 (일본), 중대력덕 (중국) |
| 행성 감속기 | 중간 | 높음 | 범용 자동화 | 다수 |

---

### 3. 일본의 감속기 독점 구조

일본 기업은 수십 년의 기술 축적으로 로봇 감속기 시장을 과점한다.

| 기업 | 국가 | 주요 제품 | 시장 지위 | 특징 |
|------|------|---------|---------|------|
| Harmonic Drive SE | 일본 | 하모닉 드라이브 (변형파 감속기) | 글로벌 하모닉 1위 | 특허 기반 성능 벤치마크, 수십 년 OEM 관계 |
| 나부테스코 (Nabtesco) | 일본 | RV·사이클로이드 감속기 | 글로벌 RV 1위 | 글로벌 산업용 로봇 생산량의 약 60% 공급 |
| 스미토모 | 일본 | 다양한 감속기 | 3위권 | |

**Nabtesco + Harmonic Drive + 스미토모 합산 시장 점유율: 60% 이상** (2025 기준)

이 구조의 취약점:
- 공급 집중 리스크 (지진·자연재해 취약)
- 고가 정책 지속 → 로봇 BOM 상승 주범
- 납기 장기화 → 휴머노이드 생산 스케일업 병목

---

### 4. 중국의 추격: 가격 경쟁과 물량 전략

중국 감속기 기업들은 가격과 물량으로 일본을 추격하고 있다.

| 기업 | 영문명 | 제품 | 현황 (2025~2026) |
|------|--------|------|----------------|
| 绿的谐波 | Leaderdrive | 하모닉 드라이브 | 중국 1위, 글로벌 2위. 2025년 매출 5.7억 위안(+47% YoY), 순이익 1.2억 위안(+100%+). Tesla Optimus 주요 공급사. 일본 대비 30~40% 저가 |
| 南通振康 | Nantong Zhenkang | RV 감속기 | 중국 내 산업용 로봇 시장 점유율 30%+ (중대력덕 합산) |
| 中大力德 | Zhongda Leader | RV 감속기 | 중국 조립 산업용 로봇의 30%+ 공급 |
| 苏州绿的 (Suzhou Green) | Suzhou Green Harmonic | 하모닉 | Tesla Optimus 감속기 60% 목표, Leaderdrive와 별개 기업 혼동 주의 |

**Leaderdrive 투자 포인트**:
- 상장사 (중국 A주)
- 창업자 형제 Zuo Yuyu·Zuo Jing, 휴머노이드 수요 급증으로 억만장자 등극
- Agibot, UBTech 등 중국 주요 휴머노이드 기업 고객으로 확보
- 주가 1년 수익률 +40% (2025~2026)

---

### 5. 한국의 진입: 국산화와 대기업 내재화

한국은 감속기 원천 기술 부족을 인정하면서도, 대기업 내재화와 전문 부품사 육성으로 진입을 시도 중이다.

| 기업 | 분류 | 내용 |
|------|------|------|
| SBB테크놀로지 | 국내 감속기 전문사 | 7종 하모닉 감속기 개발. 현대 로보틱스랩에 공급 중. 일본산 대비 저가 |
| SPG | 국내 모터·감속기 | 현대 로보틱스랩 프로토타입에 감속기 공급 |
| 삼익THK | 국내 정밀기계 | THK(일본) 합작사 기반, 리니어 가이드·볼스크류 등 정밀부품 |
| 현대 모비스 | 현대차그룹 계열 | 차세대 Atlas 휴머노이드에 액추에이터 공급 (CES 2026 발표) |
| 현대 로보틱스 | 현대차그룹 | 국산 감속기(SBB테크·SPG 등) 탑재한 모바일 양팔 로봇 개발 중 |
| 삼성전자 | 대기업 | 휴머노이드 AI 및 부품 내재화 전략 추진 중 (구체 제품 미공개) |

**핵심 이슈**: 한국 CES 2026 이후 부품사들이 액추에이터를 '상용화의 관문'으로 인식하고 집중 투자 중. Korea Herald 보도(2026)에 따르면 CES 이후 국내 전자·부품 기업들이 액추에이터를 핵심 진입 포인트로 선택.

---

### 6. 액추에이터 통합 트렌드: 일체형 모듈화

최신 휴머노이드 로봇 트렌드는 감속기·모터·드라이버·센서를 하나의 모듈로 통합하는 것이다.

| 기업 | 액추에이터 전략 | 주요 특징 |
|------|-------------|---------|
| Tesla Optimus | 자체 설계 일체형 | 회전형 14개(프레임리스 토크모터+하모닉드라이브+센서), 선형 14개(행성 롤러 스크류) |
| Figure AI | 자체 설계 | Helix AI와 통합된 액추에이터 제어 |
| Boston Dynamics Atlas | 유압→전동 전환 | 현대 모비스 전동 액추에이터 채택 |
| AGIBOT | 중국 공급망 활용 | Leaderdrive 등 중국 부품사 활용 |
| Agility Robotics Digit | 자체 설계 | Amazon 창고 최적화 설계 |

**통합 트렌드의 의미**:
- 전통 부품 공급사(감속기 단품)의 협상력 약화
- 액추에이터 모듈 통합 기업이 부가가치 독점
- OEM이 자체 개발 시 외부 감속기 수요 감소 가능성

---

### 7. 센서 서플라이체인

| 센서 유형 | 용도 | 주요 공급사 | 트렌드 |
|---------|------|-----------|------|
| 비전 (RGB-D 카메라) | 환경 인식 | Intel RealSense, 소니, OAK-D | 스테레오 비전 + AI 통합 |
| LiDAR | 3D 공간 매핑 | Velodyne, Hesai (중국), Livox (DJI) | 소형화·저가화 |
| 포스/토크 센서 | 접촉력 감지 | ATI, OnRobot | 양손 조작 필수 |
| IMU (관성 측정) | 균형 유지 | Bosch, STMicro | 저가화, MEMS 기술 |
| 촉각 센서 | 손가락 파지 | GelSight, Tactile Robotics | 초기 단계 |

---

### 8. 투자 시사점

**부품 국산화 테마 (한국)**
- 단기: 현대 모비스(액추에이터 공급), SBB테크놀로지(감속기 국산화) 모니터링
- 중기: 삼성·현대그룹의 로봇 부품 내재화 투자 규모 추적
- 리스크: 국산 감속기의 신뢰성·내구성 검증 기간 (통상 2~3년 필요)

**일본 독점 구조 vs 한국·중국 진입**
- 단기: Harmonic Drive SE, Nabtesco의 실적에 영향 미미 (산업용 로봇 수요 안정)
- 중기: 휴머노이드 대량 생산 시 중국 저가 제품으로 점유율 잠식 가능
- 장기: 일본 기업의 고부가가치 정밀 분야 집중 vs 중국 대량 생산 분리

**중국 감속기 기업 (직접 투자 접근)**
- Leaderdrive (A주 상장): 휴머노이드 수혜 최직접 노출, 고평가 주의
- 나부테스코 (일본 상장): 산업용 로봇 안정 수요, 휴머노이드 전환 리스크

---

### 9. 리스크 요인

| 리스크 | 설명 | 영향도 |
|--------|------|--------|
| 기술 격차 | 국산·중국산 감속기의 정밀도·내구성 미검증 | 상 |
| 액추에이터 내재화 | Tesla·Figure 등 OEM의 자체 개발로 외부 수요 축소 | 중상 |
| 수출 규제 | 미·중 갈등으로 중국 부품의 글로벌 공급 제약 가능 | 중 |
| 원자재 (희토류 마그넷) | 중국 의존도 높은 희토류 가격 변동 | 중 |
| 과잉 투자 | 중국 정부 보조금 기반 과잉 생산으로 가격 붕괴 | 중 |

---

### 10. 모니터링 지표 (KPI)

- Leaderdrive 분기 매출·수주 잔고 및 Tesla 공급 비중
- Nabtesco·Harmonic Drive SE의 로봇용 감속기 출하량 YoY
- 현대 모비스 액추에이터 공급 대수 (Atlas 기준)
- SBB테크놀로지 수주 공시 및 국내 휴머노이드 납품 실적
- 한국 로봇 부품 국산화 정부 지원 예산 (2026 하반기 추경 포함)
- Tesla Optimus 대당 BOM 분기별 하락 추이 공시

---

## 통합 밸류체인 맵 및 종합 시사점 {#integrated}

### 로봇/휴머노이드 산업 통합 밸류체인 맵 (ASCII)

```
╔══════════════════════════════════════════════════════════════════╗
║           로봇/휴머노이드 산업 밸류체인 맵 (2026)                 ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  [Layer 0: 원자재]                                                ║
║  희토류 마그넷 (중국 독점) → 특수강 → 반도체 웨이퍼               ║
║                                                                  ║
║  [Layer 1: 핵심 부품 — Theme C]                                   ║
║  ┌─────────────────────────────────────────────────────────┐    ║
║  │ 감속기          │ 모터           │ 센서     │ 배터리     │    ║
║  │ Harmonic(일본)  │ 프레임리스     │ LiDAR    │ 파나소닉   │    ║
║  │ Nabtesco(일본)  │ 토크 모터      │ 포스/토크 │ CATL(중국) │    ║
║  │ Leaderdrive(중국│ 서보모터       │ IMU      │ 삼성SDI    │    ║
║  │ SBB테크(한국)   │               │ RGB-D    │           │    ║
║  └─────────────────────────────────────────────────────────┘    ║
║              ↓ 통합 (Actuator Module)                            ║
║  ┌─────────────────────────────────────────────────────────┐    ║
║  │    액추에이터 모듈 (감속기+모터+드라이버+센서 일체형)       │    ║
║  │    Tesla 자체설계 │ Figure 자체설계 │ 현대모비스 (한국)    │    ║
║  └─────────────────────────────────────────────────────────┘    ║
║              ↓                                                   ║
║  [Layer 2: 컴퓨트/AI 인프라 — Theme B]                           ║
║  ┌─────────────────────────────────────────────────────────┐    ║
║  │ AI 칩          │ 시뮬레이션      │ 파운데이션 모델        │    ║
║  │ NVIDIA H100/   │ NVIDIA         │ GR00T N1 (NVIDIA)    │    ║
║  │ B100/AI5       │ Omniverse/     │ π0 (Phys.Intel)      │    ║
║  │ Tesla AI5      │ Isaac Sim      │ RT-2/Gemini(Google)  │    ║
║  │                │ Cosmos 3.0     │ Helix 02 (Figure)    │    ║
║  │                │               │ FSD→Optimus (Tesla)   │    ║
║  └─────────────────────────────────────────────────────────┘    ║
║              ↓                                                   ║
║  [Layer 3: 로봇 OEM — Theme A]                                   ║
║  ┌─────────────────────────────────────────────────────────┐    ║
║  │ Tesla Optimus    │ Figure 03    │ AGIBOT (중국)          │    ║
║  │ (목표 $20K/대)  │ ($390억 가치) │ UBTech, Fourier       │    ║
║  │ Boston Dynamics  │ Agility      │ 현대 Atlas             │    ║
║  │ (현대 인수)      │ (Amazon 파일럿│ 삼성 (개발 중)         │    ║
║  └─────────────────────────────────────────────────────────┘    ║
║              ↓                                                   ║
║  [Layer 4: 최종 수요]                                             ║
║  ┌─────────────────────────────────────────────────────────┐    ║
║  │ 제조 (35%)  │ 물류/창고 (25%) │ 연구 (15%) │ 서비스 (25%)│    ║
║  └─────────────────────────────────────────────────────────┘    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

### A+B+C 통합 투자 프레임워크

#### 투자 시계열별 포지셔닝

| 시계 | 핵심 테마 | 선호 노출 | 근거 |
|------|---------|---------|------|
| 단기 (2026~2027) | Theme B (AI 인프라) | NVIDIA (GPU + Omniverse 생태계) | 로봇 파운데이션 모델 학습 GPU 수요 즉각 발생 |
| 단기 (2026~2027) | Theme C (부품) | Leaderdrive, 현대모비스 | 출하량 증가 직접 수혜, 감속기 ASP 안정 |
| 중기 (2027~2030) | Theme A (경제학) | Tesla (Optimus), Figure AI (상장 시) | BOM $20K 도달 구간, 대량 생산 임계점 |
| 중기 (2027~2030) | Theme C (부품) | 한국 감속기·액추에이터 국산화 테마 | 수입 대체 수혜, 정책 드라이버 |
| 장기 (2030+) | Theme A+B | 플랫폼 기업 (Tesla, NVIDIA) | 로봇 OS·AI 플랫폼 독점 가능성 |

---

#### 주의해야 할 투자 오류

1. **발표 = 실현 오류**: 휴머노이드는 발표 후 3~5년 지연이 역사적 패턴. 가이던스보다 실제 출하량 데이터 우선
2. **단일 종목 집중 리스크**: 상용화 지연 시 1~2년 주가 급락 가능. 밸류체인 전반 분산 필요
3. **중국 규제 리스크 과소평가**: 미·중 기술 패권 경쟁으로 중국 부품사 공급망 차단 시나리오 고려
4. **BOM vs 판매가 혼동**: BOM $17K != 판매가 $20K. 마진, 보증, SW 라이선스 추가

---

#### 로봇 산업 빅픽처: 3가지 수렴

```
Theme A (경제학)
    "BOM $20K 가능성"
         ↑
         │  규모의 경제가
         │  AI 개발 비용 흡수
         ↓
Theme B (AI 두뇌) ←——————→ Theme C (부품)
"Foundation Model이        "감속기·액추에이터
 로봇을 범용화"             원가 하락이 BOM 결정"

3가지 테마가 동시에 진행될 때 상용화 티핑포인트 도달
예상 시점: 2028~2030
```

---

### 최종 요약: 핵심 체크포인트 (2026 하반기~2027)

| 번호 | 체크포인트 | 의미 |
|------|----------|------|
| 1 | Tesla Optimus 외부 판매 개시 여부 (2026 말) | Theme A 상용화 시계 |
| 2 | NVIDIA GR00T N1 상업 채택 로봇 수 | Theme B 플랫폼 장악력 |
| 3 | Leaderdrive 분기 매출 성장률 유지 여부 | Theme C 수요 실체 |
| 4 | 현대 모비스 액추에이터 Atlas 공급 규모 | 한국 부품사 진입 증거 |
| 5 | Goldman Sachs 2030 출하량 전망 재상향 여부 | 시장 컨센서스 방향 |
| 6 | BOM 하락 속도: $32K → $25K 도달 시점 | 대중화 경로 가시성 |

---

## 참고 자료 및 출처

### 시장 데이터
- Goldman Sachs: *Humanoid Robot: The AI Accelerant* — [링크](https://www.goldmansachs.com/insights/goldman-sachs-research/global-automation-humanoid-robot-the-ai-accelerant)
- Goldman Sachs: *The global market for humanoid robots could reach $38 billion by 2035* — [링크](https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035)
- Yole Group: *Humanoid robots 2025: the race to useful intelligence* — [링크](https://www.yolegroup.com/press-release/humanoid-robots-2025-the-race-to-useful-intelligence/)
- Bank of America: *Transformation Physical AI, part 2: Humanoid robots* (March 2026)

### BOM / 원가 분석
- RoboZaps: *Humanoid Production Economics [2026]* — [링크](https://blog.robozaps.com/b/economics-of-humanoid-robot-production)
- Standard Bots: *Humanoid robots in 2026: Types, prices, and what's next* — [링크](https://standardbots.com/blog/humanoid-robot)
- Tesla Optimus Price & Availability: *SVRC* — [링크](https://www.roboticscenter.ai/blog/tesla-optimus-price-availability)
- Not a Tesla App: *Tesla Eyes $20K Price Target For Optimus* — [링크](https://www.notateslaapp.com/news/3314/tesla-eyes-20k-price-target-for-optimus-extremely-fast-production-ramp)

### AI / 파운데이션 모델
- NVIDIA Newsroom: *Isaac GR00T N1* — [링크](https://nvidianews.nvidia.com/news/nvidia-isaac-gr00t-n1-open-humanoid-robot-foundation-model-simulation-frameworks)
- NVIDIA Blog: *Physical AI Open Models and Frameworks* — [링크](https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse/)
- Physical Intelligence: *π0: Our First Generalist Policy* — [링크](https://www.pi.website/blog/pi0)
- SVRC: *Foundation Models for Robot Manipulation: RT-2, OpenVLA, Octo, and π0* — [링크](https://www.roboticscenter.ai/research/foundation-models-robot-manipulation-2025)
- TechCrunch: *Figure drops OpenAI in favor of in-house models* — [링크](https://techcrunch.com/2025/02/04/figure-drops-openai-in-favor-of-in-house-models/)

### 부품 서플라이체인
- The Elec: *Hyundai Motor to Adopt Korean-Made Gearboxes for Humanoid Robots* — [링크](https://www.thelec.net/news/articleView.html?idxno=5618)
- Korea Herald: *After CES spotlight, Korean firms pivot to humanoid actuators* — [링크](https://www.koreaherald.com/article/10655508)
- Humanoid.guide: *Leaderdrive harmonic reducers rise on humanoid demand* — [링크](https://humanoid.guide/leaderdrive-harmonic-reducers-surge-as-humanoid-demand-lifts-shares/)
- Gasgoo: *Minth Group, Leaderdrive to build joint venture in U.S.* — [링크](https://autonews.gasgoo.com/articles/news/minth-group-leaderdrive-to-build-joint-venture-in-us-for-key-humanoid-robotics-parts-2020746790486142976)
- Intel Market Research: *Humanoid Robot Speed Reducers Market Outlook 2026-2032* — [링크](https://www.intelmarketresearch.com/humanoid-robot-speed-reducers-market-23769)

### 기업 동향
- Figure AI: *Raises $675M at $2.6B Valuation* (2024 원본) — [링크](https://www.prnewswire.com/news-releases/figure-raises-675m-at-2-6b-valuation-and-signs-collaboration-agreement-with-openai-302074897.html)
- Tech Market Briefs: *Figure AI IPO 2026: $39B Valuation* — [링크](https://techmarketbriefs.com/pre-ipo/figure-ai/)
- Optimusk: *Tesla Optimus Hardware: Actuators, Hands & Sensors (2026)* — [링크](https://optimusk.blog/blog/tesla-optimus-hardware-specs/)

---

*본 리서치는 공개 자료 및 웹 검색 결과를 기반으로 작성되었습니다. 투자 판단은 독자 본인의 책임이며, 본 자료는 투자 권유가 아닙니다.*
*작성: 2026년 6월 23일 | 다음 업데이트 예정: 2026년 9월 (Q2 실적 시즌 후)*
