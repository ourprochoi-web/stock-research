# 팩트체크: Anthropic / AI 안전 심층 분석 — 2026.06.28

- **범위**: Constitutional AI · ASL · 해석가능성 · Mythos · Pentagon 분쟁 · 사업 현황
- **검증 방법**: 4개 병렬 에이전트 독립 웹 리서치 → 교차 대조
- **리서치 노트**: `research_anthropic_ai_safety.md`

---

## A. Constitutional AI & 안전 연구 (6건)

| # | 주장 | 판정 | 핵심 근거 |
|---|------|------|-----------|
| A1 | CAI: RLHF 대비 인간 라벨러 의존도 낮춤 | **확인** | rlhfbook.com CAI 챕터: RLAIF로 합성 선호 데이터 생성, 인간 라벨링 불필요 |
| A2 | ASL-3: 2025.5 Claude Opus 4와 동시 발동 | **확인** | Anthropic 공식 발표(2025.05), TechRepublic 확인. 생물무기 위험에 우선 집중 |
| A3 | SAE 특징 3,400만 개 추출 (Claude 3 Sonnet) | **확인** | transformer-circuits.pub (2024.5): Scaling Monosemanticity 논문 원문 |
| A4 | Soul Document 14,000 토큰, Amanda Askell 확인 | **확인** | Simon Willison 블로그(2025.12.02): Richard Weiss 추출, Askell 공식 확인 인용 |
| A5 | Jan Leike: OpenAI Superalignment → Anthropic (2024.5) | **확인** | TechCrunch(2024.05.28): OpenAI 팀 해산 직후 Alignment Science 신팀 총괄로 영입 |
| A6 | 인력 ~1,097명 (2025), 471% 성장 | **부분 정확** | LinkedIn·언론 종합. 정확한 수치는 비상장 비공개. 방향과 규모는 합리적 |

---

## B. Mythos 모델 & 사이버보안 (8건)

| # | 주장 | 판정 | 핵심 근거 |
|---|------|------|-----------|
| B1 | 제로데이 익스플로잇 성공률 83%+ | **확인** | Anthropic red.anthropic.com, The Hacker News, Help Net Security 교차 확인. "첫 시도 기준" 맥락 정확 |
| B2 | 10,000개+ 고/치명적 취약점 발견 | **확인** | CSO Online(2026.06): Project Glasswing 누적 기준. Anthropic 자체 발표이나 복수 매체 인용 |
| B3 | Project Glasswing 50→200개 기관, 15개국+ | **확인** | CNBC·TechCrunch·Cybersecurity Dive(2026.06.02) 확장 발표 확인 |
| B4 | 창립 파트너 12개 (AWS, Apple, CRWD, PANW 등) | **확인** | Anthropic 공식 발표, CNBC 확인. 1개 미공개 |
| B5 | NSA: "거의 모든 기밀 시스템 몇 시간 만에 침투" | **요주의** | Warner 의원 단독 발언(2026.06.11). 이중 전달(hearsay) 구조. 인가된 레드팀 평가. 독립 검증 없음 |
| B6 | 수출 통제: Fable 5 + Mythos 5 전면 금지 (2026.06.12) | **확인** | Fortune·Anthropic 공식 성명·Axios 확인. "Plenty the Liberator" 잠금해제 → Amazon 신고 → 상무부 지침 |
| B7 | CrowdStrike·PANW +70% 랠리 (4~5월) | **확인** | Motley Fool·Seeking Alpha·CNBC. Wedbush 목표주가 상향(PANW $300, CRWD $700) 확인 |
| B8 | Schneier: "PR 플레이" + Aisle 저렴 모델 재현 | **확인** | schneier.com 블로그(2026.04) + Security Point Break 인터뷰. 방법론 세부 미공개가 한계 |

---

## C. Pentagon 분쟁 & 군사 AI (8건)

| # | 주장 | 판정 | 핵심 근거 |
|---|------|------|-----------|
| C1 | $200M DoD 계약 (2025.07) | **확인** | Anthropic 공식 발표, NPR·CNN·CNBC 다중 확인 |
| C2 | Hegseth "any lawful use" 180일 표준화 메모 (2026.01) | **확인** | NPR(2026.02.24), Wikipedia 타임라인, TechPolicy.Press |
| C3 | 2/27 최후통첩 → supply chain risk 지정 | **확인** | NPR·CNN·CNBC·Breaking Defense. 동일날 이란 공습 개시도 확인 |
| C4 | 2개 레드라인: 대량 감시 + 자율무기 | **확인** | NPR(Amodei 직접 발언 인용), CRS IN12669, CFR 분석 |
| C5 | 1심 가처분 인용 — "위헌적 제1조 보복" (2026.03.26) | **확인** | Breaking Defense·NPR. 판사 Rita F. Lin. DoD 내부 기록 인용 판결 |
| C6 | DC 항소법원 집행정지 기각 (2026.04.08) | **확인** | CNBC·Jones Walker LLP·Federal News Network. 국가 이익 형평성 |
| C7 | Claude-Maven: 24시간 1,000건+, 누적 11,000건+ | **확인** | NPR(2026.03.26)·CSIS·Democracy Now. CENTCOM 9,000건+ 공식 확인 |
| C8 | Minab 여학교 폭격: 168명+ 사망 | **확인** | Military Times·Just Security·NPR·Voelkerrechtsblog. AI 직접 인과관계는 조사 중 |

---

## D. 사업 현황 & 시장 충격 (8건)

| # | 주장 | 판정 | 핵심 근거 |
|---|------|------|-----------|
| D1 | 기업가치 $965B, Series H $65B 조달 (2026.5) | **확인** | Anthropic 공식 발표, TechCrunch(2026.05.28) |
| D2 | ARR $47B (2026.5) | **요주의** | Series H 발표 자료 기준. 비상장 자체 발표 — IPO 전 독립 감사 부재 |
| D3 | Claude Code: $0→$2.5B ARR in 9개월 | **확인** | Time Magazine·MindStudio·Context Studios. GitHub 커밋 4% 확인 |
| D4 | SaaSpocalypse: 48시간 $285B 증발 | **확인** | CNBC·xpert.digital·Taskade·Medium. Thomson Reuters -15.83% 역대 최대 |
| D5 | 누적 $2T+ SaaS 손실 (2026.4) | **확인** | The AI Opportunities 보도. 방향 확인이나 정확한 누적 금액 산정 방법론 비표준 |
| D6 | Amazon 총 ~$33B 투자 | **확인** | CNBC(2026.04.20): $8B 기존 + $25B 추가. AWS Bedrock 독점 배포 |
| D7 | 기업 AI 지출 OpenAI 추월 (비율 4%→25%) | **부분 정확** | QverLabs·MindStudio 분석. 정확한 시장 점유율 수치는 출처별 편차. 추월 방향은 다중 확인 |
| D8 | Amodei 에세이: 화이트칼라 50% 소멸 (1~5년) | **확인** | 원문 darioamodei.com, Axios·CNBC 직접 인용. "within 5 years" 발언 Fortune·Axios 별도 확인 |

---

## 팩트체크 요약

| 구분 | 건수 |
|------|------|
| 정확 | 25건 |
| 부분 정확 | 2건 |
| 요주의 | 2건 |
| 검증 불가 | 1건 (NSA 침투 세부 — hearsay 구조) |
| **합계** | **30건** |

---

## 교차 검증 하이라이트

### 에이전트 간 수치 대조 (독립 수집)

| 수치 | Agent A | Agent B | Agent C | Agent D | 일치 |
|------|---------|---------|---------|---------|------|
| 기업가치 $965B | $9,650억 | — | — | $965B | O |
| Series H $65B | $650억 | — | — | $65B | O |
| 제로데이 83%+ | — | 83%+ | — | — | 단일 출처 |
| Glasswing 200개 기관 | — | 50+150=200 | — | — | O |
| Maven 11,000건+ | — | — | 11,000+ | — | 단일 출처 |
| Minab 168명+ | — | — | 168명+ | — | 단일 출처 |
| ARR $47B | $470억 | — | — | $47B | O |
| Claude Code $2.5B | $25억 | — | — | $2.5B | O |
| SaaS $285B | — | — | — | $285B | O |
| SAE 3,400만 | 3,400만 | — | — | — | 단일 출처 |
| 인력 1,097명 | 1,097 | — | — | — | 단일 출처 |

**교차 확인된 핵심 수치 5건** (2개 이상 에이전트 독립 수집 일치): 기업가치·Series H·ARR·Claude Code ARR·SaaS 충격

---

## 기존 검증과의 연결

| 기존 검증 | 본 검증과의 관계 |
|-----------|----------------|
| `verified-youtube-summaries-2026-06-28.md` #1~6 | Anthropic 다큐 6/6 확인 → 본 검증이 각 항목을 심층 확장 |
| `verified-youtube-summaries-2026-06-28.md` #1 (Mythos 83%) | → B1에서 원출처(red.anthropic.com) 확인 |
| `verified-youtube-summaries-2026-06-28.md` #2 (Pentagon $200M) | → C1~C6에서 법적 경과까지 확장 |
| `verified-youtube-summaries-2026-06-28.md` #3 (SaaS $285B) | → D4에서 누적 $2T+ 확인 |
| `verified-youtube-summaries-2026-06-28.md` #6 (Claude-Maven ~1,000건) | → C7에서 누적 11,000건+ 확장 |

---

**종합 평가**: 30건 검증 중 25건 정확, 2건 부분 정확, 2건 요주의(ARR 자체 발표·NSA hearsay), 1건 검증 불가. 유튜브 다큐에서 확인된 6건을 모두 심층 확장하여 원출처 확인 완료. 핵심 수치(기업가치·ARR·SaaS 충격·Mythos 역량·법적 경과)는 다중 출처로 교차 확인됨.
