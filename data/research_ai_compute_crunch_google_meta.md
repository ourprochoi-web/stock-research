# AI 컴퓨트 크런치 — Google × Meta Gemini 제한 × SpaceX GPU 임대

> **작성일**: 2026.06.30
> **출처**: FT, Bloomberg, TechCrunch, Seeking Alpha, The Next Web, Yahoo Finance 등

---

## 1. 개요 — 세계 최대 AI 인프라 보유자도 수요를 감당 못한다

2026년 6월, 두 가지 사건이 AI 인프라 병목의 심각성을 선명하게 보여줬다:

1. **Google이 Meta의 Gemini 사용량을 제한** (FT, 2026.06.28)
2. **Google이 SpaceX DC에서 GPU 11만장을 월 $9.2억에 임대** (TechCrunch, 2026.06.05)

Google은 세계 최대 AI 인프라를 보유하고, 2026년 capex를 **$180B~$190B**(2025년 $91.4B의 2배+)까지 늘렸음에도 불구하고 수요를 충족하지 못하고 있다.

---

## 2. Google × Meta — Gemini 사용량 제한

### 핵심 팩트 (FT, 2026.06.28)

| 항목 | 내용 |
|---|---|
| 시점 | **2026년 3월** Google이 Meta에 통보 |
| 내용 | Meta가 요청한 Gemini 컴퓨트 용량 전량 공급 불가 |
| Meta 영향 | 내부 프로젝트 지연, **토큰 절약령** 하달 |
| Meta의 Gemini 용도 | 콘텐츠 모더레이션, 스캠 탐지, 유해 콘텐츠 제거 |
| 이유 | 자체 Llama보다 Gemini가 이 작업에서 **성능 우위** |
| Meta 대응 | 자체 **Muse Spark** 모델로 워크로드 이전 중 |
| 다른 고객 | 여러 고객도 영향 받았으나 Meta가 가장 큰 타격 |

### Pichai 발언

> "Obviously, we are compute constrained in the near-term. And as an example, our cloud revenue would have been higher if we were able to meet that demand."

### 시사점

- **세계 최대 AI 인프라 보유자**가 자사 고객 수요를 충족 못함
- Meta 같은 **$700B+ 시가총액 기업**조차 외부 AI 모델에 의존하며, 공급 제한에 직면
- AI 인프라 병목이 **"칩이 아니라 전력·냉각·물리 설비"**라는 테제의 가장 직접적인 실증 사례

---

## 3. Google × SpaceX — 월 $9.2억 GPU 임대

### 계약 구조

| 항목 | 내용 |
|---|---|
| GPU 수량 | Nvidia GPU **11만장** (+ CPU, 메모리 포함) |
| 월 비용 | **$920M** (풀레이트 기준) |
| 총 계약 규모 | **~$30B** (2026.10 ~ 2029.06) |
| 램프업 기간 | 2026.06~09 할인 요금 |
| 풀레이트 시작 | **2026년 10월 1일** |
| 해지 조건 | 2026.12.31 이후 **90일 통보**로 해지 가능 |
| 미달 시 | SpaceX가 2026.09.30까지 GPU 미배치 시 → 1개월 유예 후 해지 또는 비례 감액 |

### Google의 설명

> "short-term, timely agreement to ensure we have **bridge capacity**" for Gemini Enterprise

### 시사점

1. **Bridge capacity** — Google 자체 DC 확장까지의 시간벌기
2. **해지 가능 구조** — 자체 캐파 확보 시 종료 가능 (2027 Q1~Q2 관측 윈도우)
3. **SpaceX IPO** 맥락 — 시장이 90일 해지가능 매출에 부여하는 멀티플 = "브리지 수요 듀레이션"의 가격 신호

---

## 4. Google Capex — $180B~$190B의 의미

| 연도 | Capex | YoY |
|---|---|---|
| 2024 | ~$52B | — |
| 2025 | $91.4B | +76% |
| 2026E | **$180B~$190B** | **+97~108%** |

### 맥락

- **2026 Q1 단독** capex: **$35.7B** (분기 기준 역대 최대)
- 4분기 가이던스 상단 기준 Q2~Q4 평균 **$48~$51B/분기** 필요
- $190B는 **웬만한 국가 GDP** 규모 (크로아티아, 리투아니아 수준)
- 이만큼 투자하고도 수요를 못 맞춤 → **수요 성장 속도 > 공급 확장 속도**

---

## 5. 연결 구조 — AI 인프라 병목의 3중 고리

```
[고리 1: 컴퓨트]
Google capex $190B → SpaceX GPU 11만장 임대 → Meta Gemini 제한
   → "칩은 있는데 전기·냉각·부지가 없다"

[고리 2: 전력]
가스터빈 2031년 완판, 단가 300%↑, behind-the-meter 82GW
   → 발전소를 직접 짓는 빅테크 (MS 2.7GW, xAI 1.5GW)

[고리 3: 메모리]
HBM 3~4배 수익성 → 범용 DRAM 공급 25%↓ → Apple LPDDR 부족
   → CXMT 로비 + 반독점 소송
```

**세 고리의 공통점**: AI 수요가 기존 공급 인프라의 한계를 초과했으며, 확장에는 물리적 시간이 필요하다.

---

## 6. 투자 시사점

### 수혜 섹터

| 섹터 | 논리 | 주요 종목 |
|---|---|---|
| 전력 인프라 | 컴퓨트 병목의 근본 원인 = 전력 | GE Vernova, 두산에너빌리티, HD현대일렉트릭 |
| HBM | 공급 부족 구조 지속, 가격 방어 | SK하이닉스, 삼성전자, Micron |
| 냉각 | 전력과 함께 DC 가동의 필수 조건 | Vertiv, Modine, LG전자 |
| 클라우드 | 수요 > 공급 → 가격결정력 유지 | Google, Microsoft, Amazon |

### 리스크 모니터링

1. **SpaceX-Google 해지 여부** (2027 Q1~Q2) — 자체 캐파 전환 vs 장기화 신호
2. **Meta Muse Spark 성능** — Gemini 대체 성공 시 외부 의존도 축소
3. **DRAM 가격 반전 시점** — CXMT 캐파 확대 + 소송 압박 = 2027 하반기?
4. **규제 환경** — AI 전력 소비 ESG 이슈 + 반독점

---

## 7. 기존 리포트 연관

| 리포트 | 반영 포인트 |
|---|---|
| `ai_power_infra_investment_map.html` | Google $190B capex + SpaceX 임대 = 전력 병목 실증 |
| `ns_bottleneck_map.html` | "칩이 아니라 전력이 병목" 테제의 2026.06 실증 사례 |
| `ai_value_chain_guide_v2.html` | 7F 전력층 "GPU는 샀는데 전기가 없다" 테제 강화 |
| `ai_chip_company_kr.html` | HBM crowding-out → 범용 DRAM 공급 위기 연결 |

---

*이 문서는 투자 판단을 위한 참고 자료이며, 특정 종목의 매수·매도를 권유하지 않습니다.*
