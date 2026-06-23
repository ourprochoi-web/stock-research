# AI 소프트웨어 레이어 3대 투자 테마 심층 분석
**작성일: 2026년 6월 23일 | 리서치 등급: 심층 분석**

---

## 목차

- [Theme A — AI 에이전트 / Agentic AI 혁명](#theme-a)
- [Theme B — Vertical AI SaaS: 산업별 AI 침투](#theme-b)
- [Theme C — AI 보안 / 사이버보안 AI](#theme-c)
- [통합 투자 시사점 및 테마 상호작용 맵](#통합)

---

## <a id="theme-a"></a>Theme A — AI 에이전트 / Agentic AI 혁명

### 시장 개요 및 규모

| 구분 | 2024 | 2025E | 2028E | 2030E | CAGR |
|------|------|-------|-------|-------|------|
| AI 에이전트 시장 전체 | $4.1B | $7.8B | $28~32B | $47~53B | ~44~46% |
| 엔터프라이즈 Agentic AI | $2.6B | $4.5B | — | $24.5B | ~46% |
| Agentic AI 프레임워크 | — | $1.2B | — | $8.4B | ~42% |
| SCM Agentic AI (Gartner) | — | — | — | $53B | — |

출처: [MarketsandMarkets — AI Agents Market](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html), [Grand View Research — Enterprise Agentic AI](https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report), [Precedence Research — AI Agents $294B by 2035](https://www.precedenceresearch.com/ai-agents-market), [Gartner — SCM Agentic AI $53B](https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-forecasts-supply-chain-management-software-with-agentic-ai-will-grow-to-53-billion-in-spend-by-2030)

**핵심 포인트**: 2025년 $7.8B → 2030년 $47~53B로 약 **6~7배 성장** 전망. AI 소프트웨어 하위 섹터 중 가장 빠른 성장률.

**성장 드라이버:**
1. **엔터프라이즈 자동화 수요 폭증**: 반복적 비즈니스 프로세스(보험 심사, 고객 응대, 문서 처리 등)의 에이전트화가 가속
2. **LLM 성능 향상**: GPT-4o, Claude Opus, Gemini 2.5 등 추론 능력이 에이전트 수준의 자율성을 지탱
3. **프레임워크 성숙**: LangGraph, CrewAI 등이 프로덕션 품질에 도달하며 도입 장벽 하락
4. **빅테크 경쟁**: Microsoft·Salesforce·Google이 에이전트를 핵심 전략으로 채택 → 고객 교육·마케팅 효과
5. **ROI 검증**: 초기 도입 기업들이 평균 171% ROI를 보고하며 후발 기업의 도입을 촉진

---

### 핵심 기술/트렌드 분석

#### 1. Agentic AI 아키텍처의 진화: 단일 에이전트에서 멀티에이전트 시스템으로

2024년까지 AI 에이전트는 단일 LLM 기반의 "챗봇 플러스" 수준이었다. 2025~2026년 들어 핵심 패러다임이 전환되고 있다. 특정 도메인에 특화된 에이전트 여러 개가 협업하여 복잡한 비즈니스 워크플로우를 자율적으로 처리하는 **멀티에이전트 시스템(Multi-Agent System)** 이 엔터프라이즈 표준으로 부상했다.

**멀티에이전트 아키텍처 핵심 구성 요소:**

| 구성 요소 | 역할 | 사례 |
|-----------|------|------|
| 오케스트레이터(Orchestrator) | 작업 분해, 에이전트 라우팅, 결과 합성 | Microsoft Copilot Studio, Palantir AIP |
| 도구 사용(Tool Use) | 외부 API, DB, SaaS 연동 실행 | Salesforce Agentforce MCP 연동 |
| 메모리/상태 관리(Memory) | 세션 간 컨텍스트 유지, 장기 기억 | LangGraph 체크포인트, CrewAI v1.10 메모리 |
| 가드레일(Guardrails) | 실행 범위 제한, 인간 승인 루프 | ServiceNow Now Assist 승인 워크플로우 |
| 에이전트 하네스(Agent Harness) | 도구 실행, 메모리, 상태 조정 인프라 | 신규 인프라 카테고리로 부상 |

**에이전트 프레임워크 3강 구도:**

| 기업/프로젝트 | 포지션 | GitHub Stars | 주요 특성 |
|--------------|--------|-------------|----------|
| **LangChain/LangGraph** | 프로덕션 에이전트 플랫폼 | 1위 | LangSmith 관측성, 750+ 도구, 타입 안전 상태 관리 |
| **CrewAI** | 멀티에이전트 프레임워크 | 45,900+ | 역할 기반 추상화, MCP/A2A 네이티브, 12M+ 일간 실행 |
| **AutoGen (MS)** | 대화형 멀티에이전트 | 상위권 | 다중 LLM 협업, Azure 통합 |

**핵심 인사이트:** Gartner는 2026년까지 엔터프라이즈 애플리케이션의 40%가 태스크별 AI 에이전트를 탑재할 것으로 전망한다(2025년 5% 미만 대비). 다만 동시에 2027년 말까지 Agentic AI 프로젝트의 40% 이상이 비용 초과, 불분명한 비즈니스 가치, 리스크 통제 미비로 취소될 것으로 경고한다. 이는 "모든 것을 에이전트화"하려는 과잉 투자 구간에서 옥석 가리기가 필수임을 시사한다.

출처: [Gartner — 40% Enterprise Apps with AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025), [Gartner — 40% Agentic AI Projects Canceled](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)

#### 2. MCP/A2A: 에이전트 생태계의 표준 인프라

- **MCP (Model Context Protocol)**: Anthropic이 제안한 개방형 프로토콜이 사실상 표준(de facto standard)으로 부상. 에이전트가 다양한 도구·데이터소스에 통일된 인터페이스로 접근
- **A2A (Agent-to-Agent)**: Google이 제안한 에이전트 간 통신 프로토콜. MCP가 에이전트↔도구 연결이라면, A2A는 에이전트↔에이전트 연결
- **Computer Use**: 에이전트가 웹사이트·데스크톱 앱의 UI를 직접 조작. Microsoft Copilot Studio 2026년 5월 업데이트에서 Computer-Using Agent 정식 지원

출처: [Microsoft — Copilot Studio May 2026 Updates](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/)

#### 3. 주요 Agentic AI 플랫폼 현황 (2026년 기준)

**Microsoft Copilot Studio**

- 10만 개 이상 조직이 커스텀 Copilot 에이전트 구축 (2025년 중반 기준)
- Microsoft 365 Copilot 유료 구독자 기반으로 에이전트 빌더 확산
- Azure AI Agent Service를 통한 엔터프라이즈급 멀티에이전트 오케스트레이션
- Copilot Studio → Dynamics 365, Power Platform 전 제품군 에이전트 연동
- 2026년 주요 업데이트: 에이전트 거버넌스, Computer-Using Agent, AgentOps, 워크플로 비주얼 디자이너

**Salesforce Agentforce**

- 출시 이후 8,000건 이상 딜 클로즈, 그 중 절반 유료
- help.salesforce.com에서 75만 건 이상 요청 처리, 케이스 볼륨 7% YoY 감소
- GA 출시 6개월 내 **10억 건 이상의 에이전트 액션** 처리
- Data Cloud + AI ARR $10억 이상 돌파 (YoY +120% 이상)
- Atlas Reasoning Engine 기반 산업별 사전 구축 에이전트: Sales Coach, Service Agent, Commerce Agent 등

**ServiceNow Now Assist / AI Specialists**

- AI 관련 매출 YoY 40% 이상 성장 (FY2025)
- Now Assist → IT Service Management, HR, Customer Service, Security Operations 전 도메인 확장
- AI Specialists: 특정 워크플로우에 특화된 에이전트 사전 빌트 제공
- Now Platform 위에서 커스텀 에이전트 빌드 가능 (Creator Workflows)

**Palantir AIP (Artificial Intelligence Platform)**

- US Commercial Revenue +137% YoY 성장 (Q4 2025)
- 571개 엔터프라이즈 고객 (BP, Walgreens, Lockheed Martin, HCA Healthcare 등 21+ 산업)
- Q3 2025 Total Contract Value $27.6억 (YoY +151%), US Commercial TCV $13.1억 (YoY +342%)
- 12-레이어 에이전트 아키텍처: 데이터 온톨로지 → LLM 오케스트레이션 → 액션 실행까지 엔드투엔드
- AIP Logic, AIP Chatbot Studio, AIP Evals를 통한 프로덕션 에이전트 개발
- 5일간 집중 부트캠프로 고객 온보딩 → 빠른 파일럿-본계약 전환

출처: [Salesforce FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001108524/000110852425000027/crm-q1fy26xexhibit991.htm), [Palantir AIP Architecture](https://anandbg.com/blog/palantir-aip-end-to-end-agentic-architecture), [Achieva AI — Salesforce vs Microsoft vs ServiceNow](https://achieva.ai/blogs/ai-agents-battle-salesforce-vs-microsoft-vs-servicenow/)

#### 4. Gartner 핵심 예측: 2028년 Agentic AI 임팩트

| 예측 | 시점 | 출처 |
|------|------|------|
| 엔터프라이즈 앱 40%가 AI 에이전트 탑재 | 2026년 | Gartner |
| 소프트웨어 앱 33%가 Agentic AI 내장 | 2028년 | Gartner |
| 일상 업무 의사결정 15%가 에이전트에 의해 자율 수행 | 2028년 | Gartner |
| AI 에이전트가 B2B 지출 $15조 이상 중개 | 2028년 | Gartner |
| 브랜드 60%가 Agentic AI로 1:1 고객 인터랙션 제공 | 2028년 | Gartner |
| Agentic AI 프로젝트 40%+ 취소 (비용·ROI·리스크) | 2027년 말 | Gartner |

출처: [Gartner — $15T B2B via AI Agents](https://www.digitalcommerce360.com/2025/11/28/gartner-ai-agents-15-trillion-in-b2b-purchases-by-2028/), [Gartner — 60% Brands Use Agentic AI by 2028](https://www.gartner.com/en/newsroom/press-releases/2026-01-15-gartner-predicts-60-percent-of-brands-will-use-agentic-ai-to-deliver-streamlined-one-to-one-interactions-by-2028)

#### 5. 산업별 에이전틱 AI 적용 사례

에이전틱 AI를 도입한 기업들의 평균 ROI는 **171%**이며, 미국 기업의 경우 **192%**에 달한다.

| 산업 | 적용 영역 | 효과 |
|------|-----------|------|
| **금융** | 사기 탐지, 포트폴리오 리밸런싱, 보험 심사, KYC/AML 자동화 | 처리 속도·정확도 동시 개선 |
| **제조** | 예측 정비, 품질 관리(비전 AI), 공급망 최적화 | 비계획 다운타임 **30~40% 감소** |
| **헬스케어** | 임상 문서화, 케어 코디네이션, 신약 스크리닝 | 문서 작성 시간 **42% 감소** |
| **법률** | 계약 분석, 판례 리서치, M&A 실사 자동화 | 리서치 시간 대폭 단축 |

출처: [AI Monk — Agentic AI Enterprise ROI](https://aimonk.com/agentic-ai-examples-enterprise-roi-case-studies/)

#### 6. 에이전트 도입의 3단계 성숙도 모델

| 단계 | 설명 | 현재 위치 |
|------|------|-----------|
| Phase 1: 작업 자동화 | 단일 에이전트가 반복 작업 자동 처리 (이메일 분류, 데이터 입력) | 대다수 기업 |
| Phase 2: 워크플로우 오케스트레이션 | 멀티에이전트가 부서 간 프로세스를 자율 조정 (주문→재고→배송) | 선도 기업 파일럿 |
| Phase 3: 자율 의사결정 | 에이전트 네트워크가 전략적 의사결정 참여 (가격 최적화, 공급망 리밸런싱) | 연구/초기 PoC |

**핵심 인사이트:** 현재 대부분 엔터프라이즈는 Phase 1에서 Phase 2로의 전환 구간에 있다. Phase 2 → Phase 3 전환이 Agentic AI 시장의 다음 대규모 가치 창출 구간이며, 이를 선도하는 플랫폼 기업이 프리미엄 밸류에이션을 정당화할 수 있다.

출처: [Symphony Solutions — AI Agents 2026](https://symphony-solutions.com/insights/ai-agents-in-2026), [DRUID AI — Agentic AI Trends 2026](https://www.druidai.com/blog/agentic-ai-trends-in-2026)

---

### 기업별 포지션 분석

| 기업 | 티커 | 포지션 | 핵심 자산 | 현황 |
|------|------|--------|-----------|------|
| Microsoft | MSFT | 플랫폼 지배 | Copilot Studio, Azure AI Agent Service | 10만+ 조직 에이전트 빌드 |
| Salesforce | CRM | CRM 에이전트화 | Agentforce, Data Cloud | ARR $1B+ (AI+Data Cloud) |
| ServiceNow | NOW | IT/HR 워크플로우 에이전트 | Now Assist, AI Specialists | AI 매출 +40% YoY |
| Palantir | PLTR | 데이터 온톨로지 기반 | AIP, 12-레이어 아키텍처 | US Commercial +137% YoY |
| Google | GOOGL | 클라우드 에이전트 | Vertex AI Agent Builder, Gemini | GCP 서비스 딥 통합 |
| IBM | IBM | 엔터프라이즈 워크플로 | watsonx Orchestrate | AI 에이전트 오케스트레이션 강화 |

**한국 기업:**

| 기업 | 티커 | 포지션 | 현황 |
|------|------|--------|------|
| 네이버 | 035420.KS | 에이전트 N, HyperCLOVA X | 2026년 '에이전틱 AI 원년' 선언, 검색·쇼핑·결제 통합 에이전트. 매출 12조(2025, YoY +12.1%) |
| 카카오 | 035720.KS | 카나나 Agent | 카카오톡 기반 초개인화 AI, 행안부 'AI 국민비서' 기술 공급 |
| 코난테크놀로지 | 402030.KQ | 공공/국방 AI 검색·분석 | 법제처 AI 법령검색 65.5억 수주, 2025년 전체 수주 327억(공공 81%) |
| 솔트룩스 | — | 대화형 AI·지식그래프 | 한전원자력연료 전사 AI 구축 51억 수주, 공공·에너지 분야 공략 가속 |

출처: [이지경제 — 네이버·카카오 AI 에이전트](https://www.ezyeconomy.com/news/articleView.html?idxno=229034), [ZDNet — 코난테크놀로지 공공 AI](https://zdnet.co.kr/view/?no=20260331105226)

---

### 투자 시사점

**단기 (6~12개월)**
- Salesforce Agentforce 유료 전환율 추이: 8,000딜 중 유료 절반 → 전환율 가속 여부가 FY26 실적 핵심
- Palantir US Commercial 성장 지속성: +137% YoY 성장이 분기별 유지되는지 확인
- Microsoft Copilot Studio MAU: 에이전트 빌더 10만 조직 → 실제 프로덕션 배포 전환율 모니터링

**중기 (1~3년)**
- Phase 2→3 전환 선도 기업 식별: 자율 의사결정 에이전트 상용화 선도 기업에 프리미엄 부여
- Gartner 경고의 현실화: Agentic AI 프로젝트 취소율 모니터링 → 버블 붕괴 vs 옥석 가리기 판단
- 에이전트 인프라 레이어 투자: Agent Harness, 가드레일, 관찰가능성(Observability) 솔루션 기업

---

### 리스크 요인

| 리스크 | 수준 | 설명 |
|--------|------|------|
| 프로젝트 취소 리스크 | 高 | Gartner: 2027년 말까지 40%+ 취소 전망 → 과잉 기대 보정 |
| 환각(Hallucination) | 高 | 에이전트가 잘못된 정보 기반으로 자율 행동 시 피해 확대 가능 |
| ROI 증명 부재 | 高 | 에이전트 도입 비용 대비 생산성 향상 정량적 증거 아직 제한적 |
| 보안·거버넌스 이슈 | 中 | 프롬프트 인젝션 등 에이전트 특유의 공격 벡터 존재 |
| 플랫폼 종속(Lock-in) | 中 | Microsoft/Salesforce/ServiceNow 생태계 종속 → 전환 비용 증가 |
| 오픈소스 경쟁 | 中 | LangChain, CrewAI, AutoGen 등 오픈소스 프레임워크의 엔터프라이즈 침투 |
| 규제 불확실성 | 中 | EU AI Act 등 AI 규제가 에이전트의 자율성 범위를 제한할 가능성 |

---

### 모니터링 지표 (주기 포함)

| 지표 | 모니터링 주기 | 의미 |
|------|--------------|------|
| Salesforce Agentforce 유료 딜 수 / 에이전트 액션 수 | 분기 | 에이전트 상업화 속도 |
| Palantir US Commercial Revenue YoY | 분기 | AIP 플랫폼 채택 가속 |
| Microsoft Copilot Studio 조직 수 | 분기 | 에이전트 빌더 생태계 확장 |
| MCP/A2A 프로토콜 채택 기업 수 | 반기 | 에이전트 인터옵 표준화 |
| 에이전트 ROI 사례 / 산업별 도입률 | 분기 | 실질 수요 검증 |
| Gartner Agentic AI 프로젝트 취소율 | 연간 | 버블 vs 실질 성장 판단 |
| 오픈소스 에이전트 프레임워크 GitHub Stars | 월간 | 개발자 생태계 방향성 |
| Gartner Hype Cycle 위치 | 연간 | 에이전틱 AI 성숙도 단계 |

---

---

## <a id="theme-b"></a>Theme B — Vertical AI SaaS: 산업별 AI 침투

### 시장 개요 및 규모

| 구분 | 2024 | 2025E | 2030E | 2035E | CAGR |
|------|------|-------|-------|-------|------|
| Vertical SaaS 전체 | $118B | $130~143B | $290~330B | $499B | ~16~18% |
| Vertical AI SaaS 플랫폼 | — | $94.9B | — | $1,424B | ~36.5% |
| 엔터프라이즈 AI 시장 | — | $40.4B | — | $570B | ~34.2% |
| Horizontal SaaS 전체 | — | — | — | — | ~12~15% |

출처: [Business Research Insights — Vertical SaaS $499B by 2035](https://www.businessresearchinsights.com/market-reports/vertical-saas-market-117289), [SaaS Mag — Vertical SaaS Outperforming 2026](https://www.saasmag.com/vertical-saas-outperforming-horizontal-2026/), [MarketIntelo — Vertical AI SaaS Platform 2034](https://marketintelo.com/report/vertical-ai-saas-platform-market/amp), [Research Nester — Enterprise AI Market](https://www.researchnester.com/reports/enterprise-ai-market/8096)

**핵심 포인트**: a16z에 따르면 전체 Vertical SaaS 시장($450B)의 **30~40%가 2026~2028년 사이 AI 에이전트에 의해 재편**될 것으로 전망. 산업별 AI 솔루션 CAGR 36.5%는 범용 AI(18.9%) 대비 약 2배.

**AI 도입률 추이:**
- 2023년: 미국 Top 500 기업 중 11%가 SaaS → Vertical AI 에이전트 전환
- 2024~25년: 전환율 **47%**로 급증 (Stanford HAI AI Index Report 2025)
- 2026년: Gartner 전망 — 기업의 **80%**가 GenAI 기반 애플리케이션 배포 완료

---

### 핵심 기술/트렌드 분석

#### 1. Horizontal vs. Vertical AI SaaS: 전략 비교

AI가 SaaS 산업에 미치는 영향은 수평(Horizontal)과 수직(Vertical) 모델에서 근본적으로 다르게 나타난다.

| 비교 항목 | Horizontal AI SaaS | Vertical AI SaaS |
|-----------|--------------------|--------------------|
| **핵심 강점** | 범용성, 대규모 벤치마크 데이터 | 도메인 전문성, 규제 대응 |
| **데이터 해자** | 수백만 사용자 교차 산업 벤치마크 | 산업별 운영 데이터 독점적 축적 |
| **AI 모델 정확도** | 범용 높으나 도메인 특화 한계 | 도메인 특화 모델 40%+ 효율 우위 |
| **전환 비용** | 상대적 낮음 (편의성 기반) | 매우 높음 (미션 크리티컬) |
| **매출 확장** | 시트 기반 과금 | 구독 + 임베디드 파이낸스 (ARPU 2~5배) |
| **Gross Retention** | 보통 | 구조적으로 높음 (3x 상위) |
| **위협 요인** | Vertical AI의 침식 | 파운데이션 모델 기업의 수직 진출 |

**핵심 인사이트:** Vertical AI SaaS의 진정한 해자는 "AI 모델" 자체가 아니라 **산업별 운영 데이터의 독점적 축적**에 있다. 규제 산업(헬스케어, 금융, 법률)에서 워크플로우 깊이와 컴플라이언스 복잡성은 파운데이션 모델 기업이 복제하기 어려운 구조적 방어벽이다. 다만 2026년 1월 OpenAI가 "OpenAI for Healthcare"를 출시하며 AdventHealth, Cedars-Sinai, Memorial Sloan Kettering 등에 배포한 사례는 이 방어벽이 절대적이지 않음을 경고한다.

출처: [SaaS Mag — Niche Beats Horizontal 2026](https://www.saasmag.com/vertical-saas-niche-beats-horizontal-2026/), [BuildMVPFast — Vertical AI Eating Horizontal SaaS](https://www.buildmvpfast.com/blog/vertical-ai-eating-horizontal-saas-2026), [Tech Insider — Vertical SaaS 3x Higher Retention](https://tech-insider.org/the-rise-of-vertical-saas-why-industry-specific-software-is-winning/)

#### 2. 데이터 플라이휠과 해자의 메커니즘

Vertical AI SaaS 기업이 구축하는 경쟁우위의 핵심은 **데이터 플라이휠(Data Flywheel)** 이다.

```
┌─────────────────────────────────────────────────────────┐
│              Vertical AI SaaS 데이터 플라이휠              │
└─────────────────────────────────────────────────────────┘

    [1. 도메인 워크플로우 임베딩]
         │
         │  고객이 일상 업무에서 플랫폼 사용
         │
         ▼
    [2. 산업 특화 운영 데이터 축적]
         │
         │  의료 청구, 법률 판례, 제조 센서 로그 등
         │
         ▼
    [3. AI 모델 성능 향상]  ←── 더 많은 데이터 = 더 정확한 예측
         │
         │  도메인 특화 모델 40%+ 효율 우위
         │
         ▼
    [4. 고객 성과 개선 → 리텐션 강화]
         │
         │  전환 비용 ↑, NRR(순수익유지율) ↑
         │
         └──► [5. 신규 고객 유치] ──► [1]로 순환
```

임베디드 파이낸스를 결합한 Vertical SaaS 플랫폼은 구독 수익 외에 트랜잭션 수익까지 확보하며, 미국 임베디드 파이낸스 수익 풀은 2021년 $22B → 2026년 $51B로 성장 전망이다.

#### 3. 핵심 기술 축: RAG + Fine-tuning + Domain LLM

| 기술 | 역할 | 2026 트렌드 |
|------|------|-------------|
| **RAG** | 외부 지식 검색 → LLM 생성 결합 | Agentic RAG, Graph RAG, Hybrid RAG로 진화. CAGR 44.2% |
| **Fine-tuning** | 범용 LLM에 도메인 전문성 부여 | PEFT/LoRA로 비용 90%+ 절감, SFT+DPO 조합 |
| **Domain LLM** | 산업 전문 데이터로 사전학습 | Bloomberg GPT(금융), Med-PaLM(의료) 등 |

**핵심 인사이트:** 2026년에는 생성(Generation)이 아닌 **검색(Retrieval)이 핵심 병목** — RAG 아키텍처의 품질은 검색 정확도에 의해 결정된다.

출처: [WiFi Talents — RAG Industry Statistics](https://wifitalents.com/retrieval-augmented-generation-industry-statistics/), [Squirro — State of RAG](https://squirro.com/squirro-blog/state-of-rag-genai)

#### 4. 산업별 Vertical AI SaaS 시장 현황

**의료 AI SaaS** — Healthcare Administration AI: CAGR 38.2%로 가장 빠른 성장
- 앰비언트 임상 AI(Nuance DAX, Abridge), RCM 자동화, 임상 의사결정 지원
- Tempus AI: Q1 2026 매출 $348M (YoY +36%), FY2026 가이던스 $1.59~1.60B
- OpenAI for Healthcare 출시 (2026.1): AdventHealth, Cedars-Sinai, MSK, Stanford, UCSF 배포

**법률 AI SaaS** — 시장 규모 2025년 $3.1B → 2030년 $10.8B (CAGR 28.3%)
- Harvey AI: 기업가치 **$11B** (2026.03, $200M 시리즈), 100,000+ 변호사, 1,300+ 기관
- CoCounsel (Thomson Reuters): Westlaw 통합 AI 리서치 어시스턴트

**금융 AI SaaS**
- Bloomberg GPT: 금융 데이터 40년 학습, 터미널 통합 AI
- Alphasense: 시장 인텔리전스 AI, 기업가치 $4B+

**AI 코딩 자동화** — 2026년 **$12.8B** 시장, 개발자 95%가 주 1회 이상 AI 코딩 도구 사용

| 기업 | 제품 | 채택률 | 핵심 지표 |
|------|------|--------|-----------|
| GitHub (MS) | Copilot | **29%** (1위) | 26M+ 사용자, 엔터프라이즈 기본 배포 |
| Anysphere | Cursor | **18%** | $1M→**$2B ARR** ~28개월 (역대 최빠른 SaaS 성장) |
| Anthropic | Claude Code | **18%** | 0→**$2.5B 런레이트** 9개월 (역대 최빠른 개발자 제품) |

출처: [CNBC — Harvey AI $11B](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html), [SEC — Tempus AI FY2026](https://www.sec.gov/Archives/edgar/data/0001717115/000119312526206317/tem-ex99_1.htm), [IdeaPlan — AI Coding Market Share 2026](https://www.ideaplan.io/blog/ai-coding-assistant-market-share-2026), [Cosmic JS — Claude Code vs Copilot vs Cursor](https://www.cosmicjs.com/blog/claude-code-vs-github-copilot-vs-cursor-which-ai-coding-agent-should-you-use-2026)

---

### 기업별 포지션 분석

| 기업 | 티커 | 포지션 | 핵심 역량 | AI 관련 성과 (최신) |
|------|------|--------|-----------|---------------------|
| ServiceNow | NOW | IT 워크플로우 지배 | Now Platform + Now Assist | AI 매출 +40% YoY |
| Salesforce | CRM | CRM 에이전트화 | Agentforce + Data Cloud | AI+Data ARR $1B+ (+120% YoY) |
| CrowdStrike | CRWD | 보안 플랫폼 | Falcon + Charlotte AI | $4.81B 매출 (+22% YoY) |
| Datadog | DDOG | 클라우드 옵저버빌리티 | LLM 모니터링, 1000+ 연동 | AI 네이티브 650 고객, LLM 스팬 6개월간 10배 증가 |
| Snowflake | SNOW | 데이터 레이크하우스 | Cortex AI, Snowflake Intelligence | 9,100+ AI 채택 계정, 제품 매출 +34%, RPO $97.7B (+42%) |
| Tempus AI | TEM | 정밀의료 AI | 멀티모달 데이터 플랫폼 | Q1 2026 $348M (+36%), FY가이던스 $1.6B |

**한국 기업:**

| 기업 | 티커 | 포지션 | 핵심 역량 | 현황 |
|------|------|--------|-----------|------|
| 네이버 클라우드 | 035420.KS | 한국어 AI 클라우드 | HyperCLOVA X B2B AI API | 2026년 구독형 정식 출시, 매출 12조(2025) |
| 코난테크놀로지 | 402030.KQ | 공공 AI | 비정형 데이터 검색·분석 AI | 법제처 AI 65.5억, 수주 327억(2025) |
| 솔트룩스 | — | 대화형 AI | 지식그래프 기반 AI 플랫폼 | 한전원자력연료 51억 수주, 공공·에너지 |
| 루닛 | 328130.KQ | 의료영상 AI | INSIGHT CXR, 병리 AI | Q1 매출 239.5억(+25%), 해외 97% |
| 업스테이지 | IPO 예정 | 엔터프라이즈 LLM | Solar LLM, Document AI | 기업가치 5조원, IPO 추진 |

출처: [GuruFocus — Snowflake and Datadog AI](https://www.gurufocus.com/news/4095698/snowflake-and-datadog-poised-for-aidriven-success-by-2026), [ZDNet — 코난테크놀로지](https://zdnet.co.kr/view/?no=20260331105226), [Investing.com — 루닛 Q1](https://kr.investing.com/news/global-filings/article-93CH-1939707)

---

### 투자 시사점

**단기 (6~12개월)**
- Snowflake AI 기능 채택 가속: 9,100+ 계정의 실제 소비량 증가 여부 → 제품 매출 재가속(+30% Q4) 지속 확인
- Datadog LLM Observability: AI 네이티브 고객 650개의 ARPU 확대 → AI 인프라 모니터링 시장 선점
- ServiceNow Now Assist 침투율: 기존 고객 내 AI 모듈 크로스셀 → NRR 130%+ 유지 여부
- Harvey AI IPO 가능성: $11B 밸류에이션의 법률 AI 리더 IPO 시 Vertical AI SaaS 섹터 재평가

**중기 (1~3년)**
- 임베디드 파이낸스 수익화: Vertical SaaS 기업의 트랜잭션 수익 비중 확대 → ARPU 2~5배 점프
- 파운데이션 모델 기업의 수직 진출 리스크: OpenAI, Anthropic의 산업별 솔루션 출시 → Vertical 기업 밸류에이션 재평가
- 한국 공공 AI 시장: 정부 AI·AX 예산 ~10조원(전년비 ~3배) → 코난테크놀로지, 솔트룩스 수혜

---

### 리스크 요인

| 리스크 | 수준 | 설명 |
|--------|------|------|
| 파운데이션 모델 수직 진출 | 高 | OpenAI for Healthcare 등 빅테크가 직접 산업별 솔루션 출시 |
| 밸류에이션 프리미엄 축소 | 中 | AI SaaS 고밸류에이션(PSR 20~40x) 지속 가능성 불확실 |
| 경기 둔화 IT 투자 감소 | 中 | 기업 IT 예산 축소 시 AI 투자도 영향 |
| 데이터 규제 강화 | 中 | GDPR, AI Act 등 산업 데이터 활용 규제 → 데이터 해자 약화 가능 |
| 한국 공공 예산 변동성 | 中 | 정부 AI 사업 예산 배정의 정치적 변동성 |

---

### 모니터링 지표 (주기 포함)

| 지표 | 모니터링 주기 | 의미 |
|------|--------------|------|
| Snowflake 제품 매출 성장률 / AI 채택 계정 수 | 분기 | AI 데이터 인프라 수요 |
| Datadog AI 네이티브 고객 수 / LLM 스팬 볼륨 | 분기 | AI 옵저버빌리티 시장 확장 |
| ServiceNow NRR(순수익유지율) | 분기 | AI 크로스셀 효과 |
| Vertical AI 도입률 (Fortune 500) | 연간 | Stanford HAI 연례 보고서 |
| AI 코딩 도구 침투율 | 연간 | JetBrains·Stack Overflow 조사 |
| Vertical AI 펀딩 동향 | 분기 | PitchBook·CB Insights |
| 파운데이션 모델 기업 산업별 솔루션 출시 | 상시 | 경쟁 구조 변화 |
| 한국 공공 AI 예산 및 수주 현황 | 분기 | 국내 Vertical AI 기업 성장 |

---

---

## <a id="theme-c"></a>Theme C — AI 보안 / 사이버보안 AI

### 시장 개요 및 규모

| 구분 | 2024 | 2025E | 2030E | 2035E | CAGR |
|------|------|-------|-------|-------|------|
| AI in Cybersecurity 전체 | $24B | $30.9B | $86~134B | — | ~23~28% |
| AI 보안 플랫폼 (Security for AI) | — | $3.5B | — | $25.6B | ~22% |
| 자율대응(Autonomous Response) | — | $0.8B | $4.2B(2028) | — | — |
| 한국 사이버보안 시장 | — | 3조4529억원 | — | — | ~13~16% |

출처: [Mordor Intelligence — AI Cybersecurity Solutions](https://www.mordorintelligence.com/industry-reports/ai-cybersecurity-solutions-market), [Grand View Research — AI in Cybersecurity](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-cybersecurity-market-report), [Future Market Insights — AI Security Platforms $25.6B](https://www.futuremarketinsights.com/reports/ai-security-platforms-market), [보안뉴스 — 2026 사이버보안 시장 4조원 전망](https://m.boannews.com/html/detail.html?idx=141098)

**핵심 포인트**: CIO 대상 Morgan Stanley 조사에서 사이버보안 지출 증가율이 전체 소프트웨어 지출 증가율 대비 **50% 빠른** 것으로 나타남. AI 보안은 경기 방어적(defensive) 특성을 가진 AI 성장 섹터.

**구조적 성장 근거:**
1. **공격 표면 확대**: 클라우드·IoT·원격 근무 확산으로 보호 대상이 기하급수적 증가
2. **규제 강화**: EU NIS2, 미국 SEC 사이버보안 공시 의무화, 한국 개인정보보호법 개정
3. **인력 부족**: 글로벌 사이버보안 인력 부족 약 400만 명 → AI 자동화가 유일한 해법
4. **공격 AI 진화**: 공격자의 AI 활용이 방어 AI 투자를 강제 → 보안 지출의 비자발적·구조적 성장
5. **보험 요건**: 사이버 보험사가 AI 기반 보안 솔루션 도입을 보험 조건으로 요구하는 사례 증가

---

### 핵심 기술/트렌드 분석

#### 1. AI for Security vs. Security for AI: 두 시장의 분리

AI와 보안의 관계는 두 개의 명확히 구분되는 시장으로 분리되고 있다.

**AI for Security (AI가 보안을 강화) — 시장 규모 $30.9B (2025E)**

| 핵심 기능 | 기술 | 주요 기업 |
|-----------|------|-----------|
| 엔드포인트 탐지·대응(EDR/XDR) | 행동 기반 ML, 제로데이 탐지 | CrowdStrike, SentinelOne |
| 네트워크 트래픽 분석(NTA) | 이상 탐지 AI, DPI 연동 | Palo Alto Networks, Fortinet |
| 보안 운영 자동화(SOAR) | AI 트리아지, 자동 대응 플레이북 | Palo Alto XSOAR, Splunk |
| 위협 인텔리전스(CTI) | NLP 기반 다크웹 분석, 패턴 예측 | CrowdStrike, 샌즈랩 |
| 보안 Copilot/에이전트 | 자연어 위협 쿼리, 자동 조사 | Charlotte AI, MS Security Copilot |

**Security for AI (AI 모델·시스템 보안) — 시장 규모 $3.5B (2025E), $25.6B (2035E)**

| 위협 유형 | 설명 | 방어 솔루션 |
|-----------|------|-------------|
| 프롬프트 인젝션 | LLM에 악의적 명령 삽입 → 데이터 유출, 행동 조작 | Lakera Guard, Robust Intelligence |
| 모델 포이즈닝 | 훈련 데이터 오염 → 편향된/취약한 모델 생성 | 데이터 검증 파이프라인 |
| 섀도우 에이전트 | 비인가 AI 에이전트의 기업 시스템 접근 | AI 거버넌스 플랫폼 |
| 간접 프롬프트 인젝션 | RAG 시스템의 검색 데이터 조작 | 입력 검증, 샌드박싱 |
| 모델 도난/지적재산 유출 | 파인튜닝된 모델 파라미터 탈취 | 모델 암호화, 접근 통제 |

**핵심 인사이트:** 93%의 보안 전문가가 AI가 사이버보안을 강화할 수 있다고 답한 반면, 77%의 조직이 AI 위협 방어에 준비되지 않았다고 응답했다. 87%의 조직이 AI 관련 취약점이 다른 어떤 사이버 리스크보다 빠르게 증가하고 있다고 보고한다. 90%의 조직이 LLM 활용을 계획하지만, 5%만이 AI 보안에 높은 자신감을 보인다. 이 비대칭이 "Security for AI" 시장의 폭발적 성장 동력이다.

출처: [Lakera — AI Security Trends 2025](https://www.lakera.ai/blog/ai-security-trends), [SentinelOne — 9 AI Cybersecurity Trends 2026](https://www.sentinelone.com/cybersecurity-101/data-and-ai/ai-cybersecurity-trends/), [Vanta — Top 6 AI Security Trends 2026](https://www.vanta.com/resources/top-ai-security-trends-for-2026)

#### 2. 공격 측 AI vs 방어 측 AI — 군비 경쟁

2026년 사이버보안은 **AI vs AI 군비 경쟁**으로 정의된다. 침투→피해 소요 시간이 **51초**까지 단축되어 인간의 수동 대응은 구조적으로 불가능하다.

**공격 측 AI:**

| 공격 유형 | AI 활용 방식 | 위협 수준 |
|----------|-------------|----------|
| **AI 피싱** | LLM으로 타겟별 초개인화 피싱 메일 대량 생성 | 매우 높음 |
| **딥페이크** | CEO 사칭 합성 음성·영상으로 송금 유도 | 매우 높음 |
| **자율 악성코드** | AI가 자동으로 취약점 탐색·익스플로잇 생성·회피 기법 적용 | 높음 |
| **합성 신원** | AI 생성 가짜 신원으로 금융 사기·계정 탈취 | 높음 |

**방어 측 AI:**

| 방어 수단 | AI 활용 방식 | 효과 |
|----------|-------------|------|
| **자율 SOC** | AI 에이전트가 알림 분류·조사·대응을 자율 수행 | 기존 4일 → 수 분 |
| **행동 분석(UEBA)** | 사용자/엔터티 행동 학습 → 이상 탐지 | 내부 위협·제로데이 탐지 |
| **AI 레드팀** | 방어용 AI가 공격을 시뮬레이션하여 취약점 사전 발견 | 사전 예방 강화 |
| **딥페이크 탐지** | AI로 딥페이크 영상·음성의 미세 패턴 분석 | 딥페이크 사기 차단 |

**군비 경쟁의 구조적 특성:** 공격자는 한 번만 성공하면 되고, 방어자는 모든 공격을 막아야 한다 → 방어 측 AI 투자의 필연적 증가. AI가 공격 규모를 무한 확장할 수 있으므로 방어도 AI 스케일링이 필수다.

출처: [VentureBeat — SOC 51-Second Breach](https://venturebeat.com/security/soc-teams-face-51-second-breach-reality-manual-response-times-are-officially), [Dark Reading — AI Arms Race 2026](https://www.darkreading.com/cyber-risk/cybersecurity-predictions-2026-an-ai-arms-race-and-malware-autonomy)

#### 3. 자율 대응 대결: CrowdStrike vs Palo Alto (2026.03)

2026년 3월, CrowdStrike와 Palo Alto Networks가 며칠 간격으로 프로덕션 레디 자율 위협 대응 에이전트 시스템을 동시 출시했다.

| 구분 | CrowdStrike "Charlotte AI Agent" | Palo Alto "XSIAM Autonomous Response" |
|------|----------------------------------|--------------------------------------|
| 접근법 | 단일 에이전트 심화 — Falcon 플랫폼 내 통합 | 멀티소스 데이터 통합 — 네트워크·엔드포인트·클라우드 |
| 차별점 | 고객 맞춤형 킬스위치, 완전 감사 추적 | 네트워크 레벨 자율 차단, 포렌식 패킷 캡처 |
| 타겟 | EDR/XDR 중심 기업 | 대규모 SOC 운영 기업 |

출처: [CallSphere — CrowdStrike vs Palo Alto Autonomous Response](https://callsphere.ai/blog/cybersecurity-ai-agents-crowdstrike-palo-alto-autonomous-threat-response)

#### 4. 주요 AI 보안 기업 상세 분석

**CrowdStrike (CRWD) — Charlotte AI + AgentWorks**

- FY2026 매출: $4.81B (+22% YoY)
- Net New ARR: +73% YoY 성장, ARR 성장 가이던스 23% 상향
- Charlotte AI: 자연어 기반 위협 쿼리, 자율 분류·조사·대응 에이전트
- AgentWorks: 보안 운영을 위한 Agentic AI 프레임워크 출시 (2026.04)
- Falcon 플랫폼: 단일 에이전트로 EDR, XDR, CNAPP, 아이덴티티 보안 통합
- Forward P/E: 91x (프리미엄)

**Palo Alto Networks (PANW) — Cortex XSIAM 플랫포미제이션**

- FY2026 Q3 매출: $3.0B (+31% YoY)
- 비GAAP 순이익: $662M (+21% YoY)
- 플랫포미제이션(Platformization) 전략: 네트워크 보안 + 클라우드 보안 + SOC 통합
- Prisma Cloud, Cortex XSIAM: AI 기반 보안 운영 통합 플랫폼
- Forward P/E: 45x (합리적)

**SentinelOne (S) — Purple AI**

- FY2026 Q2 매출: $242.2M (+22% YoY)
- ARR $1B 돌파, 기록적 순신규 ARR 달성
- Purple AI: 자연어 위협 헌팅, 자동 조사·대응
- Singularity 플랫폼: AI 기반 자율 보안 운영
- M&A 타겟 거론

**Fortinet (FTNT) — FortiAI 수트**

- FY2025 매출: $6.80B (+14.2% YoY)
- FY2026 Q1 매출: $1.85B (+20% YoY), 연간 가이던스 상향 $7.71~7.87B
- FortiAI-Protect: 실시간 제로데이 탐지, 취약점 우선순위화
- FortiAI-Assist: 네트워크·보안 운영 자동화
- FortiAI-SecureAI: LLM 애플리케이션 런타임 보안
- 500건 이상 AI 특허 보유, 15년 이상 AI 혁신 이력, 20개+ AI 솔루션 제품화
- 밸류에이션 가장 합리적 (순마진 27.3%, ROE 149.8%)

출처: [Fortinet Q1 2026](https://www.fortinet.com/corporate/about-us/newsroom/press-releases/2026/fortinet-reports-first-quarter-2026-financial-results), [Seeking Alpha — CrowdStrike](https://seekingalpha.com/article/4855165-crowdstrike-my-cybersecurity-pick-for-2026), [Motley Fool — CrowdStrike vs Palo Alto](https://www.fool.com/investing/2026/03/13/crowdstrike-vs-palo-alto-networks-which-cybersecur/)

---

### 한국 AI 보안 기업

| 기업 | 티커 | 포지션 | 핵심 역량 | 현황 |
|------|------|--------|-----------|------|
| 안랩 | 053800.KS | 한국 최대 보안 기업 | V3·MDS·XDR, 30년+ 보안 데이터 | RSAC 2026 참가, 에이전틱 AI 보안 데모 |
| 이글루코퍼레이션 | 067920.KQ | SIEM/SOAR | AI 기반 보안 운영·분석 | KISA 지원 Autonomous SOC 개발 착수 |
| 시큐레터 | — | CDR(콘텐츠 무해화) | AI 기반 비실행형 파일 위협 분석 | 공공·금융기관 납품 확대 |
| 샌즈랩 | — | CTI(사이버 위협 인텔리전스) | AI·빅데이터 악성코드 자동 분류 | 매출 +160.7% YoY(2025 H1), CES 2026 성료 |

**한국 시장 인사이트:** 한국 사이버보안 시장은 2025년 3.45조원 → 2026년 4.01조원 (+16.1%)으로 성장 전망. AI 보안 기업은 글로벌 대비 매출 규모가 극히 작으나(샌즈랩 연매출 42억원 vs CrowdStrike $4.8B), 공공·국방 수요 기반의 안정적 성장과 CES 등 글로벌 진출 가능성에 주목. 샌즈랩의 2025년 H1 매출 +160.7%는 AI 보안 수요 급증을 반영한다.

출처: [보안뉴스 — 사이버보안 상장사 리포트](https://m.boannews.com/html/detail.html?idx=140055), [데일리시큐 — 샌즈랩 CES 2026](https://www.dailysecu.com/news/articleView.html?idxno=204316), [안랩 — RSAC 2026](https://www.ahnlab.com/ko/contents/content-center/36126), [데일리시큐 — 이글루코퍼레이션 KISA](https://www.dailysecu.com/news/articleView.html?idxno=207036)

---

### 투자 시사점

**단기 (6~12개월)**
- CrowdStrike AgentWorks 상용화 모니터링: Agentic AI + 보안의 결합이 새로운 매출 동력으로 작용하는지 확인
- Palo Alto Networks 플랫포미제이션 효과: 매출 성장 가속(Q3 +31%)이 지속되는지 모니터링
- SentinelOne ARR $1B 돌파 후 수익성 전환 시점: 매출 성장과 수익성의 균형점 확인
- Fortinet FortiAI 매출 기여도: 20개+ AI 솔루션의 실제 매출 기여 정량화

**중기 (1~3년)**
- Security for AI 시장 폭발: AI 에이전트 보안, LLM 보안, 프롬프트 인젝션 방어 시장 $3.5B → $25B+ 성장
- 보안 플랫폼 통합(Consolidation): 포인트 솔루션에서 통합 플랫폼으로 이동 → CrowdStrike, Palo Alto 수혜
- AI 공격의 진화에 따른 방어 투자 확대: AI 기반 공격 고도화가 보안 예산 확대의 구조적 동력

---

### 리스크 요인

| 리스크 | 수준 | 설명 |
|--------|------|------|
| 밸류에이션 부담 | 高 | CRWD Forward P/E 91x, PANW 45x — 성장 둔화 시 멀티플 압축 |
| 보안 사고 신뢰도 리스크 | 高 | CrowdStrike 2024년 7월 글로벌 장애 선례 → 반복 시 신뢰 타격 |
| 가격 경쟁 심화 | 中 | 통합 플랫폼 vs 포인트 솔루션 간 가격 전쟁 |
| AI 보안 위협 속도 > 방어 속도 | 中 | 공격 AI의 진화가 방어 AI보다 빠를 가능성 |
| 한국 기업 규모 한계 | 中 | 글로벌 대비 극소 규모 → M&A 타겟 또는 성장 한계 |

---

### 모니터링 지표 (주기 포함)

| 지표 | 모니터링 주기 | 의미 |
|------|--------------|------|
| CrowdStrike Net New ARR / 고객당 모듈 수 | 분기 | 플랫폼 확장 깊이 |
| Palo Alto 플랫포미제이션 전환 고객 수 | 분기 | 통합 트렌드 속도 |
| SentinelOne ARR 및 순신규 ARR | 분기 | 자율 보안 시장 수요 |
| Fortinet FortiAI 채택률 / 매출 기여 | 분기 | AI 보안 상업화 속도 |
| Security for AI 시장 규모 업데이트 | 연간 | 신규 시장 성장 확인 |
| AI 기반 사이버 공격 건수/피해 규모 | 월간 | 방어 투자 동력 |
| 사이버보안 M&A 건수·금액 | 월간 | 산업 통합 동향 |
| 한국 사이버보안 예산 (공공+민간) | 반기 | 국내 시장 성장 |
| 샌즈랩/안랩 분기 실적 | 분기 | 한국 AI 보안 성장 추적 |

---

---

## <a id="통합"></a>A+B+C 통합 투자 시사점 및 테마 상호작용 맵

### 통합 시장 규모 요약

| 테마 | 2025E 시장 | 2030E 시장 | CAGR | 성격 |
|------|------------|------------|------|------|
| A — AI 에이전트 / Agentic AI | ~$7.8B | $47~53B | ~44~46% | 공격적 성장 (초기 단계) |
| B — Vertical AI SaaS | ~$130~143B | $290~330B | ~16~18% | 광범위 침투 (본격 성장기) |
| C — AI 보안 / 사이버보안 | ~$30.9B | $86~134B | ~23~28% | 방어적 성장 (구조적 수요) |
| **3개 테마 합산** | **~$170~182B** | **~$420~520B** | **~20~25%** | — |

---

### 테마 상호작용 맵

```
┌─────────────────────────────────────────────────────────────┐
│           AI 소프트웨어 레이어 테마 상호작용 맵               │
└─────────────────────────────────────────────────────────────┘

    [Theme A — Agentic AI]
          │
          │ ① 에이전트가 Vertical SaaS의 핵심 UX 레이어로 진입
          │    (Salesforce Agentforce → CRM, ServiceNow → ITSM)
          │
          ▼
    [Theme B — Vertical AI SaaS]  ←── ② 도메인 데이터가 에이전트 성능 결정
          │                            (Vertical 데이터 해자 → 에이전트 정확도)
          │
          │ ③ AI SaaS 확산이 공격 표면(Attack Surface) 확대
          │    (더 많은 AI 엔드포인트 = 더 큰 보안 수요)
          │
          ▼
    [Theme C — AI 보안]
          │
          │ ④ 보안 AI가 에이전트의 가드레일·거버넌스 담당
          │    (CrowdStrike AgentWorks → 에이전트 보안 모니터링)
          │
          └──► ⑤ 보안 신뢰가 AI SaaS 기업 도입 가속의 전제 조건
                   (보안 인증 → 엔터프라이즈 AI 도입 속도 결정)
```

**5대 상호작용 설명:**

1. **에이전트 → Vertical SaaS UX (A→B):** Agentic AI는 Vertical SaaS의 사용자 경험을 근본적으로 변화시킨다. 기존의 대시보드·폼 입력 방식에서 자연어 명령 기반의 에이전트 인터페이스로 전환되며, Salesforce Agentforce, ServiceNow Now Assist가 이 전환을 선도한다. 2028년까지 사용자 경험의 1/3이 네이티브 앱에서 에이전트 프론트엔드로 이동할 전망이다(Gartner).

2. **도메인 데이터 → 에이전트 성능 (B→A):** Vertical AI SaaS 기업이 축적한 산업별 운영 데이터는 에이전트의 정확도와 실용성을 결정한다. 도메인 특화 에이전트는 범용 에이전트 대비 40% 이상 높은 효율을 보이며, 이 격차는 데이터 플라이휠이 회전할수록 확대된다.

3. **AI SaaS 확산 → 공격 표면 확대 (B→C):** 기업 내 AI SaaS 도입이 가속될수록 AI 엔드포인트, API, 데이터 파이프라인이 증가하며, 이는 사이버 공격의 표적이 된다. AI 에이전트의 자율적 시스템 접근은 새로운 보안 위협 벡터를 생성한다.

4. **보안 AI → 에이전트 가드레일 (C→A):** CrowdStrike AgentWorks, Microsoft Security Copilot 등 보안 AI는 Agentic AI의 가드레일·거버넌스 인프라 역할을 담당한다. 에이전트의 행동 범위 제한, 비인가 접근 차단, 실행 로그 감사가 핵심 기능이다.

5. **보안 신뢰 → AI 도입 가속 전제 (C→A,B):** 엔터프라이즈의 AI 도입 속도는 보안 신뢰 수준에 의해 결정된다. 90%의 조직이 LLM 활용을 계획하지만 5%만이 AI 보안에 높은 자신감을 가지고 있다. 이 신뢰 격차를 해소하는 보안 솔루션이 AI SaaS 시장 전체의 성장을 가속하는 "인에이블러(Enabler)" 역할을 한다.

---

### 크로스-테마 키워드

- **에이전틱 AI**는 3대 테마 모두를 관통하는 핵심 기술 트렌드: 에이전트 플랫폼(테마 A), Vertical AI 에이전트(테마 B), SOC 자율 에이전트(테마 C)
- **MCP/A2A 프로토콜**: 에이전트 생태계의 표준 인프라 — 도구·에이전트 간 상호운용성 확보
- **RAG + 에이전트**: Vertical AI의 핵심 아키텍처 — 도메인 지식 검색과 에이전트 행동을 결합
- **AI 코딩 자동화**: AI 소프트웨어 개발 자체를 가속 — AI가 AI를 만드는 재귀적 성장 루프

---

### 포트폴리오 구성 제언

| 리스크 프로파일 | 배분 전략 | 추천 비중 |
|----------------|-----------|-----------|
| 보수적 | C(AI 보안) 중심 + B(Vertical SaaS) 앵커 | A 10% / B 40% / C 50% |
| 중립적 | 균형 배분 | A 25% / B 40% / C 35% |
| 공격적 | A(Agentic AI) + B(Vertical AI SaaS) | A 40% / B 35% / C 25% |

**투자 전략 매트릭스:**

| 특성 | 에이전틱 AI | Vertical AI SaaS | AI 사이버보안 |
|------|-----------|-----------------|-------------|
| **성장률** | 최고 (44~46%) | 높음 (16~36%) | 안정적 (22~28%) |
| **리스크** | 높음 (초기 시장) | 중간 (검증된 모델) | 낮음 (구조적 수요) |
| **수익성** | 대부분 적자/초기 | 혼재 (흑자~적자) | 대부분 흑자 |
| **밸류에이션** | 매우 높음 | 높음~합리적 | 높음 |
| **경기 민감도** | 높음 | 중간 | 낮음 (방어적) |
| **대표 종목** | MSFT, CRM, PLTR | NOW, SNOW, DDOG, TEM | CRWD, PANW, FTNT |
| **한국 대표** | 네이버, 카카오, 코난테크 | 루닛, 업스테이지, 솔트룩스 | 안랩, 이글루코퍼레이션, 샌즈랩 |

**시기별 배분 조정 시나리오:**
- **2026 H2:** Agentforce/Copilot Studio 유료 전환 데이터 확인 후 → A 비중 조정
- **2027 전반:** Security for AI 시장 폭발 시 → C 비중 확대 (특히 AI 에이전트 보안)
- **2027 후반:** Gartner 예측대로 Agentic AI 프로젝트 40% 취소 현실화 시 → A 비중 축소, B/C 재배분

---

### 핵심 통합 리스크

| 통합 리스크 | 설명 |
|-------------|------|
| AI 에이전트 보안 사고 | Agentic AI 에이전트가 대규모 데이터 유출·오작동 시 A+B+C 테마 전반 신뢰 타격 |
| 파운데이션 모델 기업 수직 통합 | OpenAI/Anthropic/Google이 에이전트+Vertical+보안을 수직 통합 시 독립 기업 가치 희석 |
| 기업 IT 투자 경기 민감도 | 경기 침체 시 AI 투자 우선순위 재조정 → 3개 테마 동시 성장 둔화 가능 |
| AI 규제 강화 | EU AI Act 완전 시행(2027 H2), 미국 AI 행정명령 등 규제가 AI 도입 속도를 제한 |
| 오픈소스 대체 위협 | LangChain, CrewAI 등 오픈소스가 유료 에이전트 플랫폼을 대체할 가능성 |

---

### 최종 투자 결론

세 테마는 AI 소프트웨어 레이어의 서로 다른 가치 구간을 커버하면서도 상호 강화하는 생태계를 구성한다.

- **Theme A(Agentic AI)** 는 가장 높은 성장률(CAGR ~45%)과 가장 큰 불확실성을 동시에 가진다. Gartner의 "40% 프로젝트 취소" 경고는 현 시점에서 전 종목 매수보다 **플랫폼 선도 기업(Microsoft, Salesforce, Palantir) 집중 + 실적 확인 후 확대** 전략이 유리함을 시사한다. Palantir의 US Commercial +137% 성장은 실질적 수요를 증명하나 밸류에이션 프리미엄이 극도로 높다.

- **Theme B(Vertical AI SaaS)** 는 가장 넓은 시장(2025년 $130~143B)과 가장 견고한 방어벽을 가진다. 데이터 플라이휠이 작동하는 기업(ServiceNow, Snowflake, Datadog)은 NRR 130%+ 유지가 핵심 검증 지표다. 다만 OpenAI for Healthcare 출시 등 파운데이션 모델 기업의 수직 진출이 가장 큰 구조적 위협이다.

- **Theme C(AI 보안)** 는 가장 안정적인 성장 궤적을 가지며, AI 도입 가속의 필수 전제 조건이라는 구조적 수혜 포지션에 있다. CrowdStrike와 Palo Alto Networks의 플랫폼 통합 경쟁이 시장 구조를 결정하며, "Security for AI"라는 신규 시장 카테고리가 $3.5B → $25.6B로 성장할 전망이다. 경기 방어적 특성으로 포트폴리오 안정성 기여도가 높다.

세 테마를 아우르는 공통 핵심 변수는 **엔터프라이즈 AI 도입 속도와 보안 신뢰 수준**이다. Gartner가 전망하는 "2028년 엔터프라이즈 앱 33%가 Agentic AI 내장"이 현실화되려면, 보안(Theme C)이 해결되고, 도메인 데이터(Theme B)가 축적되어야 한다. 이 세 테마는 독립적 투자가 아닌 **상호 의존적 생태계**로 접근해야 한다.

---

### 테마별 핵심 촉매 캘린더 (2026~2027)

| 시기 | 테마 | 예상 이벤트 | 영향 |
|------|------|-------------|------|
| 2026 Q3 | A | Salesforce Agentforce FY27 Q1 실적 — 유료 전환 지표 | 에이전트 상업화 검증 |
| 2026 Q3 | B | Snowflake Summit 2026 — AI 기능 로드맵 발표 | 데이터 AI 플랫폼 방향성 |
| 2026 Q3 | C | CrowdStrike Fal.Con — AgentWorks 상용화 발표 | Agentic 보안 시장 개시 |
| 2026 Q4 | A | Palantir AIP 연간 실적 — US Commercial 성장 지속 여부 | 데이터 기반 에이전트 수요 |
| 2026 Q4 | B | Datadog DASH 2026 — AI 옵저버빌리티 업데이트 | LLM 모니터링 시장 규모 |
| 2027 Q1 | A+B | Gartner Agentic AI 프로젝트 취소율 첫 집계 | 버블 vs 실질 성장 판단 |
| 2027 Q1 | C | Palo Alto Networks Ignite — 플랫포미제이션 성과 | 보안 통합 트렌드 |
| 2027 Q2 | B | ServiceNow Knowledge 2027 — AI Specialists 확장 | IT 워크플로우 AI 전환 속도 |
| 2027 Q2 | C | Security for AI 시장 규모 연간 업데이트 | 신규 시장 성장 추적 |
| 2027 H2 | A+B+C | EU AI Act 완전 시행 | 유럽 AI 도입 속도 변화 |

---

### 투자자별 접근 전략

#### 장기 성장 투자자 (3~5년 관점)

- **핵심 보유 (Core Hold):** Microsoft(MSFT), CrowdStrike(CRWD) — 에이전트 플랫폼 + 보안의 교차점에서 양면 수혜
- **전략적 추가 (Tactical Add):** Palantir(PLTR), Snowflake(SNOW) — 데이터 기반 에이전트 + AI 인프라의 구조적 성장
- **성장 가속 (Growth Tilt):** ServiceNow(NOW), Datadog(DDOG), Tempus AI(TEM) — Vertical AI SaaS 전환 선도주
- **모니터링 (Watch List):** SentinelOne(S) — ARR $1B 돌파 후 수익성 전환 확인 필요

#### 단기 트레이더 (6~12개월 관점)

- **어닝 서프라이즈:** Palo Alto Networks 분기 실적 — 플랫포미제이션 전환 고객 수 + 매출 가속(Q3 +31%)
- **이벤트 드리븐:** CrowdStrike Fal.Con(연례 컨퍼런스) 전후 AgentWorks 발표 모멘텀
- **밸류에이션 리밸런싱:** Palantir PSR 극단적 프리미엄 → 실적 미달 시 멀티플 압축 리스크

#### 한국 투자자 특화

- **대형주 간접 수혜:** 삼성전자·SK하이닉스 (AI 인프라 HBM·반도체) — Theme A+B+C 성장의 하드웨어 수혜
- **중소형 직접 수혜:** 코난테크놀로지(공공 AI, 수주 327억), 샌즈랩(AI 보안, 매출 +160%), 루닛(의료 AI, 해외 97%)
- **IPO 모니터링:** 업스테이지(기업가치 5조원) — Solar LLM 기반 엔터프라이즈 AI, IPO 모멘텀

---

### 한국 기업 종합 요약

| 테마 | 기업 | 종목 코드 | 핵심 포지션 | 2026 핵심 모멘텀 |
|------|------|----------|-----------|----------------|
| A | 네이버 | 035420.KS | 에이전트 N, HyperCLOVA X | 온서비스 AI 전략, B2B AI API 출시 |
| A | 카카오 | 035720.KS | 카나나 Agent | 카카오톡 AI 에이전트, AI 국민비서 |
| A/B | 코난테크놀로지 | 402030.KQ | 공공·국방 AI | 법제처 AI 65.5억, 정부 AX 예산 10조원 |
| A/B | 솔트룩스 | — | 대화형 AI | 한전원자력연료 51억, 공공·에너지 |
| B | 루닛 | 328130.KQ | 의료영상 AI | 해외 매출 97%, Q1 역대 최고 실적 |
| B | 뷰노 | 338220.KQ | 의료 AI 진단 | 제품 라인업 확대, 흑자 전환 과제 |
| B | 업스테이지 | IPO 예정 | Solar LLM | 기업가치 5조원, IPO 추진 |
| C | 안랩 | 053800.KS | 엔드포인트 보안 | XDR/에이전틱 AI 보안, RSAC 2026 |
| C | 이글루코퍼레이션 | 067920.KQ | SIEM/SOAR | Autonomous SOC 개발, KISA 지원 |
| C | 샌즈랩 | — | CTI | AI 악성코드 분석, 매출 +160.7%, CES 2026 |

---

### 주요 용어 설명

| 용어 | 설명 |
|------|------|
| Agentic AI | 사전 정의된 명령 없이 목표를 기반으로 자율적으로 계획·실행·학습하는 AI 시스템 |
| 멀티에이전트 시스템 | 특화된 역할을 가진 여러 AI 에이전트가 협업하여 복잡한 작업을 수행하는 아키텍처 |
| MCP | Model Context Protocol. Anthropic이 제안한 에이전트↔도구 연결 표준 프로토콜 |
| A2A | Agent-to-Agent. Google이 제안한 에이전트↔에이전트 통신 프로토콜 |
| Agent Harness | 에이전트의 도구 실행, 메모리, 상태를 조정하는 소프트웨어 인프라 레이어 |
| 데이터 플라이휠 | 더 많은 사용자 → 더 많은 데이터 → 더 나은 AI → 더 많은 사용자의 자기 강화 순환 |
| Vertical AI SaaS | 특정 산업(의료, 법률, 금융 등)에 특화된 AI 기반 SaaS 소프트웨어 |
| 임베디드 파이낸스 | SaaS 플랫폼 내에 결제, 대출, 보험 등 금융 서비스를 내장하는 수익 모델 |
| NRR | Net Revenue Retention. 기존 고객의 확장·축소·이탈을 반영한 순수익유지율. 130%+ = 강한 플랫폼 |
| RAG | Retrieval-Augmented Generation. 외부 지식 검색 후 LLM이 생성하는 아키텍처 |
| PEFT/LoRA | Parameter-Efficient Fine-Tuning / Low-Rank Adaptation. 모델 일부만 조정하여 비용 90%+ 절감 |
| 플랫포미제이션 | 포인트 솔루션을 통합 플랫폼으로 전환하여 고객당 모듈 수를 확대하는 전략 |
| EDR/XDR | Endpoint/Extended Detection & Response. 엔드포인트·네트워크·클라우드 통합 위협 탐지·대응 |
| Security for AI | AI 모델·시스템 자체를 보호하는 보안 영역 (프롬프트 인젝션 방어, 모델 보안 등) |
| 섀도우 에이전트 | 기업 내에서 IT 부서 승인 없이 운영되는 비인가 AI 에이전트 |
| SOAR | Security Orchestration, Automation and Response. 보안 이벤트 자동 대응 플랫폼 |
| CTI | Cyber Threat Intelligence. 사이버 위협 정보를 수집·분석·배포하는 인텔리전스 체계 |

---

## 참고 자료 종합

### 시장 조사 보고서
- [MarketsandMarkets — AI Agents Market 2025-2030](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html)
- [Mordor Intelligence — Agentic AI Market](https://www.mordorintelligence.com/industry-reports/agentic-ai-market)
- [Grand View Research — Enterprise Agentic AI Market](https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report)
- [Grand View Research — AI in Cybersecurity Market](https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-cybersecurity-market-report)
- [Fortune Business Insights — AI in Cybersecurity Market](https://www.fortunebusinessinsights.com/artificial-intelligence-in-cybersecurity-market-113125)
- [Business Research Insights — Vertical SaaS Market](https://www.businessresearchinsights.com/market-reports/vertical-saas-market-117289)
- [Future Market Insights — AI Security Platforms](https://www.futuremarketinsights.com/reports/ai-security-platforms-market)

### Gartner 예측
- [40% Enterprise Apps with AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)
- [40% Agentic AI Projects Canceled by 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)
- [$15T B2B via AI Agents by 2028](https://www.digitalcommerce360.com/2025/11/28/gartner-ai-agents-15-trillion-in-b2b-purchases-by-2028/)
- [SCM Agentic AI $53B by 2030](https://www.gartner.com/en/newsroom/press-releases/2026-04-07-gartner-forecasts-supply-chain-management-software-with-agentic-ai-will-grow-to-53-billion-in-spend-by-2030)

### 기업 공시 및 언론 보도
- [Salesforce FY2025 8-K](https://www.sec.gov/Archives/edgar/data/0001108524/000110852425000027/crm-q1fy26xexhibit991.htm)
- [Palo Alto Networks Q3 FY2026](https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000012/ex991q326earningsrelease.htm)
- [Fortinet Q1 2026](https://www.fortinet.com/corporate/about-us/newsroom/press-releases/2026/fortinet-reports-first-quarter-2026-financial-results)
- [Tempus AI FY2026](https://www.sec.gov/Archives/edgar/data/0001717115/000119312526206317/tem-ex99_1.htm)
- [CNBC — Harvey AI $11B](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html)
- [Palantir AIP Architecture](https://anandbg.com/blog/palantir-aip-end-to-end-agentic-architecture)

### 한국 기업 관련
- [이지경제 — 네이버·카카오 에이전틱 AI](https://www.ezyeconomy.com/news/articleView.html?idxno=229034)
- [ZDNet — 코난테크놀로지 공공 AI](https://zdnet.co.kr/view/?no=20260331105226)
- [보안뉴스 — 2026 사이버보안 시장 백서](https://m.boannews.com/html/detail.html?idx=141098)
- [안랩 — RSAC 2026](https://www.ahnlab.com/ko/contents/content-center/36126)
- [데일리시큐 — 이글루코퍼레이션 KISA](https://www.dailysecu.com/news/articleView.html?idxno=207036)
- [데일리시큐 — 샌즈랩 CES 2026](https://www.dailysecu.com/news/articleView.html?idxno=204316)

---

*본 리서치는 공개된 정보 및 웹 검색 데이터를 기반으로 작성되었으며 투자 권고가 아닙니다.*
*주요 출처: [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/ai-agents-market-15761548.html) | [Grand View Research](https://www.grandviewresearch.com/industry-analysis/enterprise-agentic-ai-market-report) | [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025) | [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/ai-cybersecurity-solutions-market) | [Lakera AI Security](https://www.lakera.ai/blog/ai-security-trends) | [SaaS Mag](https://www.saasmag.com/vertical-saas-outperforming-horizontal-2026/) | [Fortinet IR](https://www.fortinet.com/corporate/about-us/newsroom/press-releases/2026/fortinet-reports-first-quarter-2026-financial-results) | [보안뉴스](https://m.boannews.com/html/detail.html?idx=141098)*
