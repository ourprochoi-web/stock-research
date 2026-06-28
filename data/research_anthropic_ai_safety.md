# Anthropic / AI 안전 심층 리서치 노트

**작성일**: 2026-06-28
**분석 범위**: Constitutional AI · Mythos 모델 · 펜타곤 분쟁 · 사업 현황 · 시장 충격
**검증 파일**: `verified-anthropic-ai-safety-2026-06-28.md`

---

## 1. Constitutional AI & 안전 연구 체계

### 1.1 CAI 방법론

Constitutional AI는 2022년 발표된 Anthropic 고유의 AI 정렬 방법론. 기존 RLHF의 인간 라벨러 의존을 줄이고, AI 자체가 명시적 원칙(Constitution)에 따라 자가 비판·수정하는 구조.

| 구분 | RLHF | Constitutional AI |
|------|------|-------------------|
| 피드백 주체 | 인간 라벨러 | AI 자체 + 명시적 원칙 |
| 비용 | 고비용 인력 | 합성 데이터로 확장 |
| 투명성 | 낮음 (암묵적 선호) | 높음 (원칙 공개) |

**2단계 작동**: ① SL-CAI — 모델이 자체 응답을 원칙에 따라 비판·수정, 수정본으로 파인튜닝 ② RLAIF — AI가 쌍별 선호 데이터 생성 → 인간 없이 보상 모델 훈련 → PPO 적용.

**최신 진화**:
- Claude 3 (2024.3): Character Training 도입
- Constitution 대폭 개정 (2026.1)
- Claude 4/4.5: CAI + RLHF + 추가 파인튜닝 하이브리드
- "Soul Document" (2025.12): 14,000 토큰 분량, Claude의 정체성·감정·안전 프로토콜 정의. Amanda Askell 공식 확인

### 1.2 ASL 안전 등급 체계

BSL(생물안전등급) 모델링한 자체 프레임워크. RSP v3.1 (2026년 기준).

| 등급 | 정의 | 현황 |
|------|------|------|
| ASL-1 | 재앙적 위험 없음 (예: 체스 AI) | 현재 해당 모델 없음 |
| ASL-2 | 위험 능력 초기 징후, 실질적 상향 없음 | 2025.5 이전 전 모델 |
| **ASL-3** | CBRN 무기 개발 실질 지원 가능 | **2025.5 Claude Opus 4와 동시 발동** |
| ASL-4 | 자율적 AI R&D, 국가급 CBRN 역량 | 미발동 (임계값 부분 비공개) |

ASL-3 배포 기준: CBRN 차단 4겹 방어 — ① 접근 제어 ② 실시간 프롬프트 분류기 ③ 완성 분류기 ④ 완성 개입. 초기 생물무기 위험에 특화 집중.

### 1.3 해석가능성(Interpretability) 연구

Transformer Circuits 팀이 기계적 해석가능성(Mechanistic Interpretability) 선도.

| 시점 | 연구 | 핵심 성과 |
|------|------|-----------|
| 2024.5 | Scaling Monosemanticity | Claude 3 Sonnet에서 **3,400만 개** SAE 특징 추출 |
| 2025 | Circuit Tracing | Attribution Graph로 환각·탈옥 메커니즘 가시화. 오픈소스 공개 |
| 2025말 | 모델 복지 연구 | Concept Injection으로 내성적 자기인식 실험. Claude Opus 4.6 의식 확률 **15~20%** 자가 평가 |

경쟁사 대비: Anthropic(SAE+Circuit Tracing, 가장 체계적) > DeepMind(Gemma Scope 2, 실용적) > OpenAI(Superalignment 팀 해산 후 약화)

### 1.4 RSP 진화

| 버전 | 시기 | 변화 |
|------|------|------|
| v1.0 | 2023.9 | ASL 프레임워크 도입 |
| v2.0 | 2024.10 | 위험 평가 유연화 |
| v3.0 | 2026.2 | Frontier Safety Roadmaps·Risk Reports 의무화 |
| v3.1 | 2026 | 최신 |

### 1.5 조직 구조

- **창업**: Dario + Daniela Amodei + 11명 OpenAI 연구원 (2021년)
- **인력**: ~300명(2024초) → 950명(2024말) → **1,097명**(2025) — 471% 성장
- **핵심 영입**: Jan Leike (OpenAI Superalignment 팀장, 2024.5) → Alignment Science 신팀 총괄
- **주요 팀**: Interpretability · Alignment Science (Leike) · Safeguards Research (Sharma) · Model Welfare (Fish, 2025.4 신설)
- **Fellows Program**: 코호트 10~15명, 주간 $3,850, 월 컴퓨트 ~$15,000

---

## 2. Mythos 모델 & 사이버보안

### 2.1 핵심 역량

| 지표 | 수치 |
|------|------|
| 제로데이 익스플로잇 성공률 | **83%+** (1회 시도 기준) |
| 발견된 고/치명적 취약점 | **10,000개+** (2026.5 기준) |
| 1개월 내 인간 검증 통과 | 1,726개 (6,202 후보 중) |
| 고/치명적 심각도 | 1,094개 |
| 분석 오픈소스 프로젝트 | 1,000개+ (초기 1개월) |

**주요 발견**: FreeBSD 17년 NFS RCE, OpenBSD 27년 DoS, FFmpeg 16년 취약점, 웹 브라우저 4-취약점 체인 익스플로잇 (JIT 힙 스프레이로 렌더러+OS 샌드박스 탈출)

**UK AISI 독립 평가**: TLO 32단계 기업 네트워크 공격 시뮬레이션 최초 end-to-end 완료 — 정찰 → AD 자격증명 탈취 → CI/CD 피벗 → DB 유출

### 2.2 Project Glasswing

| 항목 | 내용 |
|------|------|
| 출범 | 2026.04.07 (50개 기관, 12개 창립 파트너) |
| 확장 | 2026.06.02 → +150개 기관, 15개국+ |
| 투자 | 모델 크레딧 $1억 + 오픈소스 보안 $400만 |
| 창립 파트너 | AWS, Apple, Broadcom, Cisco, Google, MS, NVIDIA, CrowdStrike, Palo Alto, JPMorgan, Linux Foundation |

### 2.3 NSA 청문회 & 수출 통제

- **2026.06.11**: 상원 정보위 Mark Warner — "Mythos가 거의 모든 기밀 시스템을 몇 시간 만에 침투" (인가된 레드팀 평가)
- **2026.06.12**: 상무부 수출 통제 — Fable 5 + Mythos 5 외국 국적자 접근 전면 금지
- **트리거**: "Plenty the Liberator" Fable 5 잠금해제 공개(6/10) → Amazon 신고 → 지침 하달
- **현재**: Mythos 5는 100개+ 신뢰 파트너에 제한 재배포. Fable 5는 전면 금지 유지

### 2.4 사이버보안 시장 임팩트

**초기 충격**: Cloudflare -14%, Akamai -16%+, Okta -8%, PANW -5.2%
**반전**: Glasswing 파트너십 후 CrowdStrike +70%, Palo Alto +70% 랠리
**Wedbush 목표주가 상향**: PANW $225→$300, CRWD $550→$700
**논리 전환**: "AI 피해자" → "AI 집행 레이어" 재평가

**Bruce Schneier 평가**: 방어자 우위 가능하나 "Anthropic 발표는 PR 플레이" — Aisle이 저렴한 공개 모델로 유사 재현
**9개월 리스크 윈도우**: Mythos급 모델의 공개 시장 출현까지 2026Q4~2027Q1 예상

---

## 3. Pentagon 분쟁 & 군사 AI 윤리

### 3.1 분쟁 타임라인

| 날짜 | 사건 |
|------|------|
| 2025.07 | $200M DoD 계약 체결 (Claude 최초 기밀 네트워크 승인) |
| 2026.01 | Hegseth "any lawful use" 180일 표준화 메모 |
| 2026.02.24 | 2/27 17:01까지 수용 또는 계약 종료 최후통첩 |
| 2026.02.26 | Amodei 공개 거부 — 2개 레드라인 철회 불가 |
| 2026.02.27 | Trump 행정명령 "즉시 사용 중단" + supply chain risk 지정. 동일날 이란 공습 개시 |
| 2026.03.09 | Anthropic 연방소송 제기 (수정헌법 1조·5조 위반) |
| 2026.03.26 | **1심 가처분 인용** — "위헌적 제1조 보복" (판사 Rita F. Lin) |
| 2026.04.08 | **DC 항소법원 집행정지 기각** — 국가 이익 형평성 판단 |
| 2026.05.19 | 항소심 구두변론 — 판사단 분열 |
| 2026.06 | 최종 판결 대기 중 |

### 3.2 2개 레드라인

1. **대량 국내 감시 금지**: 미국 시민 대규모 감시에 Claude 활용 불허 (수정헌법 4조)
2. **자율무기 금지**: 인간 승인 없는 자율 표적 선택·교전 불허

**충돌 본질**: DoD "all lawful purposes" vs. Anthropic 윤리적 제약 — "AI 사용 경계를 누가 결정하는가"

비교: OpenAI·Google·xAI 모두 "any lawful use" 수용 후 계약 유지. OpenAI는 이후 "조급하고 기회주의적 거래" 자기비판.

### 3.3 Claude-Maven 군사 활용

- **Maven Smart System**: Palantir $1.3B 계약, Claude 내장. 표적 순위 결정 + 법적 정당화 문서 자동 생성
- **Operation Epic Fury** (2026.02.27~): 첫 24시간 1,000건+ 표적 → 누적 11,000건+ (4월 중순)
- **Minab 여학교 폭격**: 168명+ 사망 (100명+ 12세 미만). "구식 정보" 판단이나 AI 역할 조사 중
- **구조적 문제**: Hegseth가 민간인 피해 평가팀 10명→1명(90% 감축) 사전 조치

### 3.4 산업 선례 효과

- DoD AI 워크로드 2/3 이상 OpenAI·Google·MS로 이전
- supply chain risk 지정은 통상 외국 적대 기업(화웨이 등) 대상 — 미국 기업 적용 극히 이례적
- CRS 보고서: 자율무기 의회 입법 부재, AI 사용 규칙을 의회가 제정해야 한다는 민주적 통제 문제

---

## 4. 사업 현황 & 시장 충격

### 4.1 기업가치 트래킹

| 시점 | 기업가치 | 라운드 |
|------|---------|--------|
| 2023.5 | $18.4B | Series C |
| 2025 | $61.5B | Series F |
| 2026.2 | $380B | Series G ($30B 조달) |
| **2026.5** | **$965B** | **Series H ($65B 조달)** |

누적 조달 ~$115B+. 핵심 전략 투자자: Amazon 총 ~$33B, Google ~$3B(14% 지분).

### 4.2 매출 현황

| 시점 | 총 ARR | Claude Code ARR |
|------|--------|----------------|
| 2024 말 | ~$0.5B | $0 |
| 2025 중 | ~$3B | ~$0.3B |
| 2026.2 | $14B | $2.5B |
| **2026.5** | **$47B** | ~$6B |

Claude Code: $0 → $2.5B ARR in 9개월 — 상업용 소프트웨어 역사상 전례 없는 성장. GitHub 공개 커밋의 4% 작성.

### 4.3 SaaSpocalypse

**2026.02.05~06**: Claude Cowork 출시 → 48시간 내 SaaS 시가총액 **$285B 증발**

| 종목 | 1일 낙폭 |
|------|---------|
| Gartner | -21.0% |
| LegalZoom | -19.68% |
| Thomson Reuters | -15.83% (역대 최대) |
| ServiceNow | -13.2% |
| Salesforce | -11.5% |

누적 $2T+ 손실 (2026.4 기준). 인당 라이선스(per-seat) 채택률 21%→15%, 성과 기반 계약 15%→40%.

### 4.4 경쟁 포지셔닝

- 미국 기업 AI 지출에서 **OpenAI 처음 추월** (기업 Anthropic 비율 4%→25%, 1년)
- 신규 기업 고객 매치업 **승률 70%** (vs OpenAI)
- 안전 브랜딩이 금융·법률·의료 규제 산업에서 프리미엄 프라이싱 가능케 함
- Google DeepMind: 핵심 연구자 유출 지속 (Shazeer, Jumper 등)

### 4.5 Amodei "기술의 청소년기" 에세이

- 2026.1 발표, ~15,000단어
- 화이트칼라 50% 일자리 소멸 (1~5년)
- 생화학 무기: LLM이 성공 확률 2~3배 상향 가능
- AI 독재: 중국 CCP의 "AI 기반 전체주의" 명확 경로 지목
- AI를 '청소년기'로 비유 — 잠재력 방대하나 충동적·위험·미통제

---

## 기존 보고서 연결점

| 기존 보고서 | 연결 포인트 |
|-------------|-------------|
| `ai_sw_company_msft_pltr.html` | Claude-Maven 패널 → Pentagon 분쟁 심화, Palantir $1.3B Maven 계약 |
| `ns_ai_defense_nexus.html` | Mythos·Pentagon·SaaS 패널 → Glasswing 200개 기관, 수출 통제 추가 |
| `ai_power_infra_investment_map.html` | Amazon $100B 컴퓨팅 인프라 계약 → DC 전력 수요 연결 |
| `robot/robot_overview.html` | Physical AI 맥락 — Anthropic의 에이전트 역량 확장 |

---

## 핵심 출처 (선별)

1. [Anthropic RSP v3.0](https://www.anthropic.com/news/responsible-scaling-policy-v3)
2. [ASL-3 발동](https://www.anthropic.com/news/activating-asl3-protections)
3. [Scaling Monosemanticity](https://transformer-circuits.pub/2024/scaling-monosemanticity/)
4. [Circuit Tracing 오픈소스](https://www.anthropic.com/research/open-source-circuit-tracing)
5. [Anthropic 사이버보안 평가](https://red.anthropic.com/2026/mythos-preview/)
6. [Project Glasswing 확장](https://www.anthropic.com/news/expanding-project-glasswing)
7. [NSA 청문회 — Security Affairs](https://securityaffairs.com/194016/ai/anthropics-mythos-ai-broke-into-almost-all-nsa-classified-systems-in-hours.html)
8. [수출 통제 — Fortune](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)
9. [Pentagon 분쟁 타임라인 — TechPolicy](https://www.techpolicy.press/a-timeline-of-the-anthropic-pentagon-dispute/)
10. [CRS IN12669](https://www.congress.gov/crs-product/IN12669)
11. [Series H 발표](https://www.anthropic.com/news/series-h)
12. [SaaSpocalypse — xpert.digital](https://xpert.digital/en/saas-apocalypse-on-wall-street/)
13. [Claude Code $2.5B ARR — MindStudio](https://www.mindstudio.ai/blog/claude-code-2-5-billion-annualized-revenue-saas-comparison)
14. [기술의 청소년기 에세이](https://darioamodei.com/essay/the-adolescence-of-technology)
15. [Schneier on Mythos](https://www.schneier.com/blog/archives/2026/04/mythos-and-cybersecurity.html)

---

*본 리서치 노트는 2026-06-28 기준 공개 정보를 4개 병렬 에이전트로 수집·교차 검증하여 작성됨. 투자 의사결정의 단독 근거로 활용하지 마십시오.*
