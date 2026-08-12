# AI 전력 인프라 리서치 — 테마 E·F·G·H 심화: 지정학·ESS·PPA·한국 전력정책

> 목적: 기존 테마 A~D를 보완하는 4개 추가 테마 — 지정학과 공급망(E), ESS와 배터리(F), 전력 PPA 구조(G), 한국 전력정책(H) 심화 리서치
> 기반 데이터: `research_ai_power_part12_overview.md`, `research_ai_power_themes_AB.md`, `research_ai_power_themes_CD.md`
> 작성일: 2026-06-23
> 상태: 심화 리서치 완성본

---

# 테마 E — 지정학과 공급망 리스크 (Geopolitics & Supply Chain Risk)

## E-1. 미중 에너지 기술 디커플링

### E-1-1. 희토류 수출 통제 — 에너지 장비의 아킬레스건

| 항목 | 내용 | 출처 |
|------|------|------|
| 중국 글로벌 점유율 | 채굴 **61%**, 정련 **91%**, 고강도 자석 **93%** | IEA / S&P Global |
| 수출 통제 시행 | 2025.10.09 발표, 2026.11.10까지 **1년 유예** 후 시행 | China-Briefing |
| 통제 대상 원소 | 사마륨·가돌리늄·루테튬·테르븀·디스프로슘·스칸듐·이트륨 (7개 중희토류) | IEA |
| 영향 제품 | SmCo 영구자석, NdFeB 자석(Tb/Dy 함유), 희토류 0.1%+ 포함 부품·조립품 | CSIS |
| 풍력 터빈 영향 | 대형 풍력 발전기 영구자석에 NdFeB 필수. 중국 풍력터빈 글로벌 점유율 **66%** | Heritage Foundation |
| 가격 프리미엄 | 2026년 내내 지속 전망 — 비중국 정련 CAPA 제약 | S&P Global |

- **AI 전력 인프라 연결고리**: 희토류 통제는 직접적으로 풍력 터빈·고성능 모터·ESS 자석에 영향. 간접적으로 변압기 코어의 방향성 전기강판(GOES) 공급에도 파급
- 중국은 수출 라이선스 제도를 통해 **"수출은 가능하되 통제권을 쥐고 있다"**는 전략적 모호성 유지
- G7 2026년 초 워싱턴 각료회의에서 희토류 공급망 복원력 전용 세션 개최 — 가격 하한제·국제 인센티브 논의

**출처:**
- [IEA: 핵심광물 수출 통제와 공급 집중 리스크](https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality)
- [S&P Global: 희토류 공급 병목 2026년 지속](https://www.spglobal.com/energy/en/news-research/latest-news/metals/012726-rare-earth-supply-bottlenecks-set-to-persist-in-2026)
- [CSIS: 중국 희토류 수출제한의 결과](https://www.csis.org/analysis/consequences-chinas-new-rare-earths-export-restrictions)
- [Arnold Magnetics: 중국 희토류 수출 지연과 자석 공급망 전망](https://www.arnoldmagnetics.com/blog/chinas-rare-earth-export-delays-2025-2026-magnet-supply-chain-outlook/)

---

### E-1-2. 변압기·터빈 부품의 공급망 리스크

| 부품 | 중국 의존도 | 리스크 | 대안 |
|------|-----------|--------|------|
| 방향성 전기강판(GOES) | 중국 생산 **~30%**, 일본·한국 대체 가능 | 관세·물류비 상승 | POSCO·Nippon Steel |
| 변압기 부싱·절연유 | 중국산 비중 증가 추세 | 품질·납기 리스크 | ABB·Hitachi Energy 내재화 |
| 가스터빈 초내열합금 | 니켈·코발트 정련 중국 의존 | 원자재 가격 변동 | 캐나다·호주 광산 다변화 |
| 초고압 부싱 세라믹 | 글로벌 소수 공급사 | 특수 부품 병목 | HD현대·LS일렉 내재화 확대 |

- 미국 전력 변압기의 **80%**, 배전 변압기의 **50%**가 수입산 (Wood Mackenzie) → **테마 C 참조**
- 변압기·터빈 자체는 한국·일본·유럽이 주도하나, 핵심 원자재(GOES, 니켈합금, 희토류)에서 중국 의존 잔존

---

## E-2. 미국 관세 정책과 AI 인프라 비용 영향

### E-2-1. 관세 영향 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| AI 인프라 추가 비용 (5년) | **$75~100B** (15~20개 하이퍼스케일 시설 건설 불가 규모) | CSIS |
| 반도체 관세 적용 시 연간 GDP 손실 | **$90B/년** (~GDP 0.29%), 24.3만 고용 위협 | CCIA |
| McKinsey DC 투자 전망 (US) | **$2.7T** (2025~2030) | McKinsey |
| 반도체 비중 | DC 투자의 **54%** | CSIS |
| 25% 철강 관세 | 시설 건설 $/sqft 상승 → 개발사·최종 사용자에 전가 | ConstructConnect |

- 2026년 2월 미 대법원이 일부 관세 조치를 위법 판결 → 수정 관세 발표 → **불확실성 장기화**
- GPU 보드·가속기 카드는 Section 232에서 **명시적 제외** (2026.04 수정)
- 서버 랙도 제외 → **AI 컴퓨팅 핵심 장비는 관세 회피**, 그러나 **전력 인프라(변압기·케이블·철강 구조물)는 직격**

### E-2-2. 한국산 전기기기 관세 현황

| 구분 | 세율 | 기간 | 비고 |
|------|------|------|------|
| Section 232 한국산 전기기기 | 최대 **15%** (기본 관세 포함) | 2026.06.08~2027.12.31 | 무역협정 파트너국 우대 적용 |
| 적용 대상 | 변압기·차단기 등 금속 집약 전기 그리드 장비 | — | HTS Annex C 분류 |
| 한국 지위 | **무역협정 파트너국** (일본·EU·영국·대만과 동일) | — | 일반국 대비 우대 세율 |

- **핵심**: 한국산 변압기에 25% 관세가 아닌 **15% 우대세율** 적용 — 미국의 변압기 수입 의존도(80%)가 역설적으로 한국산 보호 구조
- 2027년 12월 이후 세율 재협상 불확실성 잔존

**출처:**
- [CSIS: 관세가 AI DC 건설에 미치는 영향](https://www.csis.org/analysis/impact-tariffs-ai-data-center-buildout-balancing-supply-chain-security-and-ai)
- [CSIS: 관세가 $3T AI 건설을 위험에 빠뜨리는 방법](https://www.csis.org/analysis/how-tariffs-could-derail-united-states-3-trillion-ai-buildout)
- [CCIA: 반도체 관세 적용 시 연간 $90B 비용](https://ccianet.org/articles/applying-semiconductor-tariffs-to-data-centers-would-cost-the-u-s-90-billion-a-year/)
- [Dimerco: US 관세 업데이트 2026](https://dimerco.com/us-tariff-update-2026/)

---

## E-3. 글로벌 에너지 공급망 재편

### E-3-1. 핵심광물 Friendshoring 전략

| 전략 | 내용 | 주도국 |
|------|------|--------|
| 미국 $1.6B 직접 투자 | USA Rare Earth 등 비중국 정련 CAPA 확보 | 미국 DOD |
| DLA $1B 비축 | 코발트·안티몬·탄탈럼·스칸듐 전략 비축 | 미국 DLA |
| MP Materials 10년 오프테이크 | DOD와 장기 구매 계약 — 비중국 영구자석 공급망 | 미국 |
| 양자 핵심광물 파트너십 | 호주·일본·캐나다·DR콩고·말레이시아·태국·우크라이나 | G7 |
| IRA Section 30D 한계 | '동맹국' 정의가 협소 — 아르헨티나·인도·인도네시아 등 주요 산출국 제외 | 미국 |

### E-3-2. 에너지 장비 Nearshoring — 한국 기업의 미국 현지 생산

| 기업 | 미국 시설 | 규모 | 가동 시점 |
|------|----------|------|----------|
| **HD현대일렉트릭** | 앨라배마 제1·2공장 | 미국 최대 전력변압기 공장. 2공장 $200M 투자, CAPA **+50%** | 1공장 2011~, 2공장 **2027.04** |
| **효성중공업** | 멤피스, 테네시 | 연 130기 → 200기(2026 초) → **250기+**(2027). 미국 최대 규모 목표 | 증설 진행 중 |
| **LS일렉트릭** | 배스트롭, 텍사스 | 중저압 배전기기·변압기·스위치기어 생산. DC 전력 인프라 거점 | **2026년 완공** |

- HD현대일렉트릭 미국 매출: $100M(2017) → **$400M(2025)**, 8년간 **4배** 성장
- 한국 전력기기 4사(HD현대·LS·효성·대한전선) 수주잔고 합산 2031년까지 확보 — 관세 리스크를 현지 생산으로 상당 부분 헤지

**출처:**
- [ODI: 2026 핵심광물 지정학](https://odi.org/en/insights/critical-minerals-geopolitics-in-2026-risks-supply-chains-and-global-power-shifts/)
- [EnkiAI: 미국 희토류 공급망 $1.7B 투자](https://enkiai.com/critical-minerals/rare-earth-supply-chain-us/)
- [HD현대일렉트릭 앨라배마 확장 PRNewswire](https://www.prnewswire.com/news-releases/hd-hyundai-electric-expands-us-production-subsidiary-solidifies-leadership-in-north-american-extra-high-voltage-power-transformer-market-302707507.html)
- [LS Electric 배스트롭 캠퍼스](https://powersystems.technology/news/ls-electric-launches-bastrop-campus-for-u-s-production-of-transformers-and-power-gear-transformer-technology-news.html)
- [효성중공업 멤피스 증설 — Korea Herald](https://www.koreaherald.com/article/10618541)
- [Transformer Magazine: 한국 전력기기 업체 미국 확장](https://transformers-magazine.com/tm-news/korean-power-equipment-makers-expand-amid-us-boom/)

---

## E-4. 테마 E 투자 시사점

### 지정학 리스크 매트릭스

| 리스크 | 확률 | 영향 | 수혜 기업 | 피해 기업 |
|--------|------|------|----------|----------|
| 중국 희토류 수출 통제 본격화 (2026.11 이후) | 높음 | 중간 | MP Materials, USA Rare Earth, 비중국 자석 공급사 | 풍력터빈 제조사, ESS 모터 |
| 미국 변압기 관세 강화 (15%→25%) | 중간 | 높음 | HD현대(앨라배마), 효성(멤피스) — 현지 CAPA | 한국 수출 의존 기업 |
| 미중 에너지 기술 완전 디커플링 | 낮음 | 극대 | 서방 장비·소재 대체 공급사 전체 | 중국산 부품 의존 기업 |
| GOES 공급 차질 | 중간 | 높음 | POSCO (방향성 전기강판 국내 생산) | 수입 GOES 의존 변압기 제조사 |

### 핵심 투자 테제

1. **"현지 생산 = 관세 헤지 + 수요 근접"**: HD현대일렉트릭·효성중공업의 미국 현지 공장은 관세 리스크를 구조적으로 회피하면서 북미 수요에 직접 대응 → **테마 C의 공급자 우위를 지정학적으로 강화**
2. **희토류 디커플링은 ESS·풍력에 더 큰 영향**: AI 전력 인프라의 핵심(변압기·가스터빈)은 희토류 의존도가 상대적으로 낮음. ESS 모터·풍력 발전기가 직접 타격 → **테마 F(ESS)의 원자재 리스크로 연결**
3. **관세 불확실성 자체가 투자 프레임워크**: 2027년 12월까지 15% 우대세율 보장 → 그 이후 재협상 변수. 투자 시계(time horizon)에 관세 시나리오 반영 필요

---

## E-5. 테마 E 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| 중국 희토류 수출 라이선스 발급 건수 | 월간 | 발급 감소 = 공급 긴축 신호 |
| 2026.11 유예 기간 종료 후 정책 변화 | 즉시 | 본격 시행 시 자석 가격 급등 |
| US Section 232 한국 우대세율 연장 여부 | 반기 | 2027.12 만료 전 재협상 동향 |
| HD현대 앨라배마 2공장 건설 진행도 | 분기 | 2027.04 준공 일정 준수 여부 |
| MP Materials·USA Rare Earth 생산량 | 분기 | 비중국 정련 CAPA 확대 속도 |
| POSCO 방향성 전기강판 증설 | 반기 | 변압기 핵심 소재 자급률 |

---

---

# 테마 F — ESS와 배터리 스토리지 (Energy Storage Systems)

## F-1. AI 데이터센터와 ESS 통합 트렌드

### F-1-1. 통합의 구조적 필요성

AI 데이터센터의 전력 수요는 두 가지 근본 특성을 가진다: (1) **상시 가동** (인퍼런스 전환으로 24/7 베이스로드 — 테마 D 참조), (2) **피크 버스트** (학습 클러스터의 간헐적 초과 수요). ESS는 이 두 특성 모두에 대응하는 핵심 인프라다.

| 통합 모델 | 역할 | 사례 |
|----------|------|------|
| 그리드 피크 셰이빙 | 피크 시간 전력 비용 절감, 수요 응답 참여 | 유틸리티 + DC 공동 운영 |
| BTM 백업 전원 | UPS 대체·보완. 정전 시 수시간 백업 | Tesla Megapack + DC |
| 재생에너지 통합 | 태양광·풍력 간헐성 보완, 24/7 클린 에너지 달성 | Google + Form Energy 30 GWh |
| 주파수 조정 | 그리드 안정화 보조서비스 참여 → 추가 수익 | Tesla Autobidder 플랫폼 |

- **Form Energy + Crusoe**: AI 데이터센터 전용 **12 GWh** 철공기전지(iron-air) 계약 — ESS가 AI DC 전력의 일부로 직접 편입되는 최초의 대규모 사례
- **Google + Form Energy**: **30 GWh** 프로젝트 (Xcel Energy 경유) — 100시간 장주기 저장으로 AI DC 탈탄소화
- 데이터센터 운영사의 **61~73%**가 온사이트 전력 전략 채택 중 (Bloom Energy 2026) → ESS는 BTM 전략의 필수 구성요소

**출처:**
- [Form Energy + Crusoe 12 GWh 계약](https://www.crusoe.ai/resources/newsroom/form-energy-crusoe-announce-agreement-for-12-gigawatt-hours-of-iron-air-batteries-for-ai-data-centers)
- [Google + Form Energy 30 GWh](https://www.energy-storage.news/google-bets-big-on-30gwh-of-form-energys-iron-air-battery-storage-despite-efficiency-trade-offs/)
- [EnkiAI: Form Energy 2026](https://enkiai.com/battery-storage/form-energy-iron-air-xcel/)

---

## F-2. 그리드 스케일 BESS 시장 전망

### F-2-1. 시장 규모

| 출처 | 2026 규모 | 목표연도 규모 | CAGR |
|------|----------|-------------|------|
| Persistence Market Research | $16.9B | $90.6B (2033) | **27.1%** |
| Fortune Business Insights | $19.09B | — (2034) | **11.07%** |
| MarketsandMarkets | — | — (2030) | **15.8%** |
| Future Market Insights (BESS 전체) | $81.6B | $198.88B (2031) | **17.21%** |
| Mordor Intelligence (BESS 전체) | $89.89B | — (2031) | — |

### F-2-2. 설치 용량 전망

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 배터리 저장 설치 용량 | ~88.4 GW by 2027 (현재 대비 **2배**) | GreentechLead |
| 미국 에너지 저장 시장 | ESS가 북미 배터리 수요의 **~절반** (2026) | LG에너지솔루션 |
| 2025 글로벌 신규 설치 | 기록적 성장, 전년 대비 **+70%+** | Energy Industry Review |

- **핵심 성장 동력**: AI DC 전력 수요 + 재생에너지 간헐성 보완 + 그리드 안정화 + IRA 세액공제(ITC 30~50%)
- BESS 시장 정의에 따라 규모가 크게 다름 — 그리드 스케일($16~19B) vs BESS 전체($80~90B). 투자 분석 시 세그먼트 구분 필수

**출처:**
- [Fortune Business Insights: 그리드 스케일 배터리 시장](https://www.fortunebusinessinsights.com/industry-reports/grid-scale-battery-market-101304)
- [MarketsandMarkets: BESS 시장](https://www.marketsandmarkets.com/Market-Reports/battery-energy-storage-system-market-112809494.html)
- [Persistence Market Research: 그리드 스케일 배터리](https://www.persistencemarketresearch.com/market-research/grid-scale-battery-storage-market.asp)
- [GreentechLead: 배터리 저장 시장 88.4 GW by 2027](https://greentechlead.com/renewable-energy/battery-storage-market-set-to-double-to-88-4-gw-by-2027-as-tesla-byd-catl-and-fluence-accelerate-investments-53589)

---

## F-3. 주요 기업 분석

### F-3-1. CATL — 글로벌 BESS #1

| 항목 | 수치 | 출처 |
|------|------|------|
| 글로벌 BESS 시장 점유율 | **30.4%** (2025), ~**40%** (2026 추정) | BESSfinder / SNE Research |
| 2025 총 배터리 판매 | **661 GWh** | ESS-News |
| ESS 출하 성장 | YoY **+160%+** | CATL |
| 주력 제품 | **EnerD 3.0** (6.25 MWh/컨테이너), Tener (5년 무열화) | CATL |
| 생산 CAPA 전망 | **1.2 TWh** 파이프라인 by 2030 | 업계 |

- **제로 열화(Zero-Degradation)** 기술: LCOS(Levelized Cost of Storage) 혁신적 절감. Tener 시스템 5년간 용량 손실 0%
- CTP(Cell-to-Pack) 기술 + 액체냉각으로 에너지 밀도 업계 최고
- **리스크**: 미국 FEOC(Foreign Entity of Concern) 규정으로 IRA 세액공제 대상에서 제외 가능성. 미국 시장 직접 진출 제한

### F-3-2. BYD — 글로벌 BESS #2 (2025 출하 기준)

| 항목 | 수치 | 출처 |
|------|------|------|
| 2025 ESS 출하 | CATL 다음 2위 → Tesla 추월 | Benchmark Minerals / Electrek |
| 주력 제품 | MC Cube (LFP, 컨테이너형) | BYD |
| 수직통합 | 셀 → 모듈 → 시스템 → EMS 소프트웨어 자체 생산 | BYD |

- BYD가 2025년 출하량 기준으로 **Tesla를 추월하여 글로벌 2위** 달성 (Electrek, 2026.05)
- CATL과 마찬가지로 FEOC 규정 리스크 — 미국 시장 직접 영업 제한

### F-3-3. Tesla Energy — Megapack 생태계

| 항목 | 수치 | 출처 |
|------|------|------|
| 2025 ESS 배포 | **46.7 GWh** (역대 최대) | Tesla 8-K |
| 2025 에너지 부문 매출 | **$12.8B** | Tesla 8-K |
| 에너지 부문 총마진 | **29.8%** (분기 신기록) | Tesla |
| Q1 2026 배포 | **8.8 GWh** (잠정) | Tesla |
| 2026 CAPEX | **$20B+** 계획 | Tesla |
| 휴스턴 신공장 | Megapack 3 연 **50 GWh** 생산능력 | TESMAG |
| Autobidder | AI 기반 에너지 거래 플랫폼 — 자율 입찰 | Tesla |

- **Megapack 3 + 20 MWh Megablock**: 차세대 제품으로 유틸리티 스케일 확장
- **수직통합 + Autobidder**: 하드웨어(Megapack) + 소프트웨어(Autobidder AI 거래 플랫폼) = 유틸리티가 에너지 시장에 자율 참여 가능
- Tesla Energy가 자동차 부문 성장 둔화를 상쇄하는 핵심 성장 엔진으로 부상

### F-3-4. LG에너지솔루션 — 미국 ESS 시장 공략

| 항목 | 수치 | 출처 |
|------|------|------|
| 2025 매출 | **23.7조 원** (YoY -7.6%), 영업이익 1.3조 원 (+2배) | LGES |
| 2026 ESS 셀 생산 목표 | **60 GWh+** (연말까지) | Energy-Storage.News |
| 2026 ESS 신규 수주 목표 | **90 GWh** 추가 수주 | Energy-Storage.News |
| ESS 수요 성장 전망 | 전년비 **+40%+** | LGES |
| 미국 ESS 시장 점유율 목표 | **50%** | Energy-Storage.News |
| 제품 | LFP + NMC 하이브리드 포트폴리오 | LGES |

- ESS 매출 급증이 EV 수요 둔화를 상쇄 — **BESS가 배터리 3사의 새 성장축**
- 미국 FEOC 규정 준수 → IRA 세액공제 수혜 가능 (CATL·BYD 대비 핵심 경쟁우위)

### F-3-5. 삼성SDI

| 항목 | 수치 | 출처 |
|------|------|------|
| 2025 매출 | **13.27조 원** (YoY -19.8%), 영업손실 1.72조 원 | ESS-News |
| 2026 전략 | ESS 풀 가동. SBB 2.0 LFP 미국 양산 개시 | Samsung SDI |
| 포지션 | 데이터센터 확장 + 미국 정책 지원 수혜 기대 | Samsung SDI |

- 2025년 적자 전환이나 ESS 매출 급증으로 **손실 폭 축소** 추세
- SBB 2.0(Standard Battery Block) LFP 라인업으로 미국 그리드 스케일 시장 공략

### F-3-6. Fluence Energy — 서방 유일의 BESS 통합 플레이어

| 항목 | 수치 | 출처 |
|------|------|------|
| FY2026 매출 가이던스 | **$3.2~3.6B** | Fluence 8-K |
| Q2 FY2026 백로그 | **$5.6B** (사상 최대) | ESS-News |
| ESS 파이프라인 | **147 GWh** (+20% / 6개월) | Fluence |
| 2026년 5월까지 수주 | **~$2B** (전년 동기 대비 2배) | Fluence |
| 매출 구성 | Gridstack Pro BESS가 **70%** | Fluence |
| 주주 구조 | Siemens + AES 합작 | — |

- **서방 유일의 Top 5 BESS 업체** (CATL·BYD·Tesla·LGES에 이어 유일한 비중국·비한국 대형 통합사)
- FEOC 규정 준수 → 미국 IRA 세액공제 수혜 가능
- 하이퍼스케일러 직접 계약 확대 중 (주가 +30% 반등)

### F-3-7. Form Energy — 장주기 ESS 게임체인저

| 항목 | 수치 | 출처 |
|------|------|------|
| 기술 | **철공기전지(Iron-Air)** — 100시간 방전 가능 | Form Energy |
| 목표 비용 | **<$20/kWh** (리튬이온의 1/5 수준) | Energy Solutions Intelligence |
| 계약 용량 | **75 GWh+** 프로젝트 합의 | Form Energy |
| 주요 계약 | Google/Xcel 30 GWh + Crusoe 12 GWh + 아일랜드 1 GWh | 다수 |
| 제조 | 웨스트버지니아 웨어턴 양산 시설 가동 | Form Energy |
| 첫 상용 파일럿 | 미네소타, **2026년 가동** 예정 | Discovery Alert |

- **"가역적 녹슬기"**: 철 펠릿이 공기 중 산소와 반응(방전) → 충전 시 역반응. 지구상 5번째로 풍부한 원소(철) 사용 → 원자재 비용 극저
- AI DC용 ESS: Crusoe 12 GWh 계약이 AI 데이터센터 전용 장주기 ESS의 첫 대규모 사례

**출처:**
- [BYD, Tesla 추월 — Electrek](https://electrek.co/2026/05/13/byd-surpasses-tesla-energy-storage-bess-benchmark-2025/)
- [Tesla 2025 46.7 GWh — Battery-Tech Network](https://battery-tech.net/battery-markets-news/tesla-energy-posts-46-7-gwh-storage-deployments-in-2025/)
- [LGES 90 GWh 수주 목표 — Energy-Storage.News](https://www.energy-storage.news/lg-energy-solution-targets-50-percent-share-of-us-energy-storage-market-in-2026/)
- [Fluence $5.6B 백로그 — ESS-News](https://www.ess-news.com/2026/05/08/fluence-reports-5-6-billion-order-backlog-as-battery-pipeline-swells/)
- [BESSfinder: Top 10 BESS 제조사 2026](https://www.bessfinder.com/ranking.html)
- [Form Energy Crusoe 12 GWh](https://www.crusoe.ai/resources/newsroom/form-energy-crusoe-announce-agreement-for-12-gigawatt-hours-of-iron-air-batteries-for-ai-data-centers)

---

## F-4. 장주기 에너지저장 기술 비교

### F-4-1. 기술 프로파일

| 기술 | 방전 시간 | 비용 목표 | 성숙도 | 대표 기업 |
|------|----------|----------|--------|----------|
| **철공기전지(Iron-Air)** | 100시간+ | <$20/kWh | TRL 6~7 (첫 상용 파일럿) | Form Energy |
| **바나듐 레독스 플로우** | 8~12시간 | $200~400/kWh | TRL 7~8 (상용화 초기) | ESS Tech, Sumitomo |
| **압축공기(CAES)** | 8~100시간+ | 100 MW+ 스케일 유리 | TRL 8 (지하공동 필요) | Hydrostor |
| **중력 저장(Gravity)** | 8~12시간 | — | TRL 5~6 | Energy Vault |
| **수소 기반** | 수백 시간 | 효율 30~40% (왕복) | TRL 5~7 | — |

### F-4-2. 장주기 ESS 시장 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 장주기 ESS 시장 | $3.9B (2026) → **$9.5B (2035)** | GM Insights |
| Top 5 점유율 | **30%** (Sumitomo, ESS Tech, Form Energy, Energy Vault, GE Vernova) | GM Insights |

- 장주기 ESS는 리튬이온의 4~8시간 한계를 넘어 **24~100시간+ 저장**이 가능 → 재생에너지의 **수일간** 간헐성 보완
- AI DC와의 접점: 100시간 저장은 **비상 백업 + 그리드 독립**을 동시에 가능하게 하는 유일한 기술

**출처:**
- [GM Insights: 장주기 에너지 저장 시장](https://www.gminsights.com/industry-analysis/long-duration-energy-storage-market)
- [PatSnap: 철공기전지 기술 전망 2026](https://www.patsnap.com/resources/blog/articles/iron-air-battery-technology-landscape-2026/)
- [Energy Solutions Intelligence: 철공기전지 $20/kWh](https://energy-solutions.co/articles/sub/aqueous-iron-air-batteries-long-duration-storage)

---

## F-5. 테마 F 투자 시사점

### 종목별 투자 포지션

| 종목 | 단기 (6개월) | 중기 (2년) | 핵심 테제 | 리스크 |
|------|------------|----------|----------|--------|
| **Tesla Energy** | ★★★★★ | ★★★★★ | Megapack 3 + Autobidder. 매출 $12.8B, 마진 30% | 자동차 부문 리스크 전이, Megapack 마진 압축 전망 |
| **LG에너지솔루션** | ★★★★☆ | ★★★★★ | 미국 50% 점유 목표, FEOC 준수. ESS가 EV 둔화 상쇄 | EV 부문 적자 지속, 환율 |
| **Fluence** | ★★★★☆ | ★★★★☆ | 서방 유일 대형 BESS 통합사, $5.6B 백로그 | 수익성 미확립, 셀 공급 의존 |
| **삼성SDI** | ★★★☆☆ | ★★★★☆ | SBB 2.0 LFP 미국 양산. ESS 매출 성장 | 2025 대규모 적자, 재무 회복 시간 필요 |
| **Form Energy** | — (비상장) | ★★★★☆ | 장주기 ESS 독점적 기술. 75 GWh 계약 | 상용화 리스크, 효율 trade-off |

### 테마 A~D 연결고리

- **테마 B(가스터빈)와의 관계**: ESS가 충분히 성숙하면 가스터빈의 "피크 셰이빙" 역할 대체 가능. 그러나 100~500 MW급 AI 클러스터의 24/7 베이스로드를 ESS만으로 커버하는 것은 **2030년대 중반 이전에는 비경제적** → 가스터빈 브릿지 수요 유지
- **테마 D(DC 전력혁명)와의 관계**: 800V DC 아키텍처에 ESS 직결 시 AC/DC 변환 손실 제거 → Bloom Energy SOFC + ESS + 800V DC가 **완전 오프그리드 DC**의 기술적 조합
- **테마 E(지정학)와의 관계**: 중국 CATL·BYD의 FEOC 규정 제한 → LG에너지솔루션·삼성SDI·Fluence에 **미국 시장 반사이익**

---

## F-6. 테마 F 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| Tesla Megapack 분기 배포 GWh | 분기 | 10 GWh+/분기 = 연간 40 GWh+ 궤적 유지 |
| LGES ESS 수주 잔고 | 분기 | 90 GWh 목표 달성 여부 |
| Fluence 백로그 변화 | 분기 | $5.6B 이상 유지 = 수요 지속 확인 |
| Form Energy 미네소타 파일럿 가동 | 즉시 | 상용화 마일스톤 — 2026년 내 확인 |
| FEOC 규정 변경 (CATL·BYD 미국 진출) | 상시 | 규정 완화 시 한국 배터리 3사 반사이익 감소 |
| 리튬 가격 ($/ton) | 월간 | $15K 이하 = BESS LCOS 추가 개선 |
| IRA ITC ESS 세액공제 유지 여부 | 상시 | 폐지·축소 시 BESS 설치 성장 둔화 |

---

---

# 테마 G — 전력 PPA 구조와 에너지 계약 (Power Purchase Agreements)

## G-1. 데이터센터 PPA 구조 변화

### G-1-1. PPA 시장의 패러다임 전환

AI 데이터센터가 전력 수요의 중심으로 부상하면서 PPA 구조가 근본적으로 변하고 있다. 기존의 "가격 헤지" 목적에서 **"물리적 전력 확보"** 목적으로 전환되었다.

| 시기 | PPA 특성 | 목적 |
|------|---------|------|
| 2015~2022 | Virtual PPA 중심, 소규모(100~300 MW) | ESG·RE100 달성, 가격 헤지 |
| 2023~2025 | Physical PPA 비중 증가, GW급 등장 | 물리적 전력 확보, 24/7 CFE |
| **2026~** | **GW급 멀티소스 PPA**, BTM·원전·가스 혼합 | 그리드 우회, 전력 주권 확보 |

- 2025년 미국 기업 청정에너지 계약 **48 GW** (역대 최대) — 상위 4사(Meta·Amazon·Google·Microsoft)가 전체의 **49%** (BloombergNEF)
- Microsoft: 누적 계약 **34.7 GW** (2025.09 기준) — 세계 최대 기업 전력 구매자
- PPA 구조화·중개 시장: $28.5B 절대 수수료 기회 by 2036, CAGR **34.9%** (Fact.MR)

**출처:**
- [EnkiAI: GW급 PPA가 하이퍼스케일러 에너지를 재정의하는 방법](https://enkiai.com/solar/gigawatt-ppas-how-ai-redefined-hyperscaler-energy-in-2026/)
- [BloombergNEF: 기업 청정에너지 구매 2025](https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/)
- [Fact.MR: DC 전력 중개 서비스 시장](https://www.factmr.com/report/data-center-power-brokerage-services-market)

---

## G-2. PPA 유형 비교: Virtual vs Physical vs BTM

### G-2-1. 3가지 PPA 구조 비교

| 구분 | Virtual PPA | Physical PPA | Behind-the-Meter (BTM) |
|------|------------|-------------|----------------------|
| **전력 전달** | 금융 정산만 (물리적 전달 없음) | 실제 전자(electron) 전달 | 현장 발전소에서 직접 공급 |
| **그리드 사용** | 기존 그리드 사용 | 전용선(private wire) 가능 | **그리드 불필요** |
| **그리드 요금** | 전액 부담 (일부 국가 전기료의 **50%+**) | 감면 가능 | **면제** |
| **계통연계** | 필요 | 필요 | **불필요** — 큐 회피 |
| **지리적 제약** | 없음 (금융 헤지) | 발전소 인근 | 데이터센터 부지 내 |
| **24/7 전력** | 보장 불가 (간헐성) | 계약 구조에 따라 보장 | 가스터빈·연료전지로 **24/7 보장** |
| **주요 사용처** | ESG 보고, RE100 달성 | 대규모 단일 테넌트 DC | AI 캠퍼스, 메가 클러스터 |
| **2026 트렌드** | 비중 감소 | 비중 증가 | **가장 빠른 성장** |

### G-2-2. 2026년 PPA 구조 전환의 동인

1. **계통연계 큐 병목 (테마 C 참조)**: 평균 5년 대기 → Physical PPA도 실행 불가 → BTM 전환 가속
2. **24/7 CFE(Carbon-Free Energy) 요구**: 시간대별 100% 클린 전력 매칭 필요 → 단일 소스 PPA 불충분 → 멀티소스 포트폴리오
3. **전력 가격 확실성**: AI 인프라 투자 $2.7T(McKinsey) → 전력 비용 예측 가능성이 프로젝트 파이낸싱의 전제 조건
4. **규모의 변화**: 2015년 100~300 MW → 2026년 **1~6.6 GW** — 단일 기업이 중소국가 수준의 전력 계약

**출처:**
- [PV Magazine: AI DC가 태양광 PPA 플레이북을 재작성](https://pv-magazine-usa.com/2026/03/13/ai-datacenters-rewrite-the-solar-ppa-playbook/)
- [DCD: DC 운영자를 위한 PPA 완전 가이드](https://www.datacenterdynamics.com/en/analysis/everything-data-center-operators-need-to-know-about-power-purchase-agreements-ppas/)
- [Introl: AI DC를 위한 PPA 전략](https://introl.com/blog/power-purchase-agreements-ai-data-centers-renewable-energy-strategies)
- [Pillsbury: DC를 위한 PPA 및 계통연계 계약](https://www.pillsburylaw.com/en/news-and-insights/power-purchase-interconnection-agreements-data-centers.html)

---

## G-3. 하이퍼스케일러별 전력 조달 전략

### G-3-1. 5대 하이퍼스케일러 비교 (2026.06 기준)

| 기업 | 누적 클린에너지 계약 | 2025 신규 계약 | 전략 특징 | 원전 포지션 |
|------|-------------------|-------------|----------|-----------|
| **Microsoft** | **34.7 GW** (세계 1위) | 대규모 | 원전(TMI 835 MW) + 태양광 + 풍력 포트폴리오 | Constellation TMI 재가동 20년 PPA |
| **Amazon** | ~22 GW+ | 태양광 4 GW + 풍력 2 GW + 원전 4 GW | 포트폴리오 최대 다각화. 원전+태양광+풍력 | X-energy 5 GW, Talen 1.92 GW |
| **Google** | **22 GW+** (170개 계약) | 4.18 GW | 24/7 CFE 리더. 장주기 ESS(Form Energy 30 GWh) | Kairos Power 500 MW SMR |
| **Meta** | **6.6 GW** (원전 단독) | 6.6 GW 원전 포트폴리오 | 가장 공격적 원전 포지션. BTM 가스 병행 | TerraPower+Oklo+Vistra+Constellation |
| **Oracle** | — | Bloom Energy **2.8 GW** SOFC | 연료전지 BTM 집중 전략 | — |

### G-3-2. 전략별 분류

```
가장 공격적 원전:  Meta (6.6 GW) > Amazon (5 GW) > Google (500 MW) > Microsoft (835 MW)
가장 큰 총 포트폴리오:  Microsoft (34.7 GW) > Amazon (~22 GW) > Google (22 GW) > Meta
가장 혁신적 계약:  Google (Form Energy 30 GWh 장주기) + Oracle (Bloom 2.8 GW SOFC)
BTM 집중:  Oracle > Meta > Amazon > Google > Microsoft
```

- **공통 트렌드**: Virtual PPA에서 Physical PPA·BTM·원전 PPA로 전환. "전력 확보가 부동산 확보보다 먼저"라는 새 패러다임
- **핵심 시사점**: 하이퍼스케일러의 PPA 전략이 **에너지 산업 자체를 재편** — Constellation·Vistra 등 유틸리티의 밸류에이션이 "AI 전력 프록시"로 재평가

**출처:**
- [S&P Global: 하이퍼스케일러 조달이 미국 전력 투자를 형성](https://www.spglobal.com/sustainable1/en/insights/special-editorial/hyperscaler-procurement-to-shape-us-power-investment)
- [EnkiAI: Microsoft Constellation AI DC](https://enkiai.com/nuclear/microsoft-constellation-ai-data-centers/)
- [Saurenergy: 글로벌 클린에너지 Top 5 기업 구매자](https://www.saurenergy.com/solar-energy-blog/the-top-5-global-corporate-buyers-of-clean-energy-11457509)

---

## G-4. 전력 중개·거래 플랫폼 기업

### G-4-1. 시장 개요

| 지표 | 수치 | 출처 |
|------|------|------|
| DC 전력 중개 서비스 시장 CAGR | **34.9%** (2026~2036) | Fact.MR |
| 2036년 절대 수수료 기회 | **$28.5B** | Fact.MR |
| 최대 세그먼트 | PPA 구조화·소싱 (**36%**, 2026) | Fact.MR |
| AI 학습 캠퍼스 비중 | **37%** (최대 전력 블록 필요) | Fact.MR |
| 미국 CAGR | **38.8%** (2026~2036) | Fact.MR |

### G-4-2. 주요 플레이어

| 유형 | 기업 | 역할 |
|------|------|------|
| **PPA 플랫폼** | LevelTen Energy | PPA 가격 인덱스 발행, 마켓플레이스 운영. 2026 Q1 기준 291개 가격 오퍼/207개 프로젝트 |
| **에너지 거래** | Yes Energy | 전력 시장 데이터·분석·트레이딩 솔루션 |
| **AI 자율거래** | Tesla Autobidder | Megapack + AI 입찰 알고리즘. 유틸리티 자율 에너지 거래 |
| **유틸리티** | Constellation Energy | 60 GW 발전 포트폴리오. PPA 직접 제공 + 유틸리티 서비스 |
| **유틸리티** | Vistra Corp | Meta 6.6 GW 원전 포트폴리오 일부. 전력 도매·소매 |
| **BTM 통합** | Williams Companies | 파이프라인 + 온사이트 발전 + 장기 PPA. $9.6B 포트폴리오 |

- **새로운 가치사슬**: AI DC가 전력 시장의 최대 구매자로 부상 → 전력 중개·구조화·리스크 관리가 독립적 비즈니스 레이어로 성장
- **한국 시사점**: 한국 직접 PPA 제도가 2022년부터 시행되었으나 활용 사례 제한적 → **테마 H**에서 상세 분석

---

## G-5. 테마 G 투자 시사점

### PPA 구조 전환이 만드는 투자 기회

| 기회 | 수혜 기업 | 근거 |
|------|----------|------|
| 원전 PPA 가치 재평가 | **Constellation**, Vistra | 24/7 베이스로드 → 프리미엄 PPA 가격 가능. TMI 2027년 첫 전력 |
| BTM 가스 발전 PPA | **Williams**, **Bloom Energy** | 계통연계 우회 = 즉시 전력 확보. 10~12.5년 장기 계약 |
| ESS+재생에너지 번들 PPA | **Tesla Energy**, **NextEra** | Megapack + 태양광 = BTM 클린 전력. Autobidder로 차익 거래 |
| PPA 중개·플랫폼 | **LevelTen**, Constellation | DC 전력 중개 CAGR 34.9%. 수수료 수익 모델 |
| 유틸리티 AI 프록시 | **Constellation**, **Vistra** | 하이퍼스케일러 PPA로 장기 현금흐름 가시성 극대화 |

### 테마 A~D 연결고리

- **테마 A(원전)**: 원전 PPA가 가장 높은 프리미엄 → Constellation·Vistra 밸류에이션 재평가의 직접 원인
- **테마 B(가스터빈)**: BTM 가스 발전이 PPA 구조의 핵심 축 → Williams $9.6B, Bloom $20B 백로그
- **테마 C(송배전)**: 계통연계 병목이 Physical PPA → BTM 전환을 가속하는 구조적 원인
- **테마 F(ESS)**: ESS + 재생에너지 번들이 새로운 PPA 상품 → Tesla Megapack + Autobidder

---

## G-6. 테마 G 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| 하이퍼스케일러 신규 PPA 발표 | 월간 | GW급 계약 속도 → 전체 전력 시장 수급 영향 |
| LevelTen PPA Price Index | 분기 | 태양광·풍력 PPA 가격 추이 ($/MWh) |
| BTM 프로젝트 착공 건수 | 분기 | Williams·Bloom 프로젝트 진척 |
| 원전 PPA 프리미엄 (vs 가스 PPA) | 반기 | 프리미엄 확대 = 원전 자산 가치 상승 |
| DC 전력 중개 시장 규모 | 연간 | CAGR 34.9% 유지 여부 |
| Constellation·Vistra 신규 PPA 체결 | 분기 | AI 전력 프록시 밸류에이션 지속 확인 |

---

---

# 테마 H — 한국 전력정책과 전력시장 개편

## H-1. 한전(KEPCO) 재무 구조와 전기요금 정상화

### H-1-1. 한전 재무 위기 현황

| 지표 | 수치 | 출처 |
|------|------|------|
| 총 부채 | **206.2조 원** ($139.2B) | Korea Herald |
| 일일 이자 비용 | **~114억 원** | Korea Herald |
| 부채 감축 목표 | **42.2조 원** 감축 by 2026 | 정부 |
| 감축 수단 | 비핵심 자산 매각 + 비용 절감 | 정부 |
| 위기 원인 | 2021~2023 글로벌 에너지 가격 급등 시 원가 이하 공급 지속 | S&P Global |

### H-1-2. 전기요금 동결 현황

| 분기 | 연료비 조정단가 | 결정 내용 | 배경 |
|------|-------------|----------|------|
| 2026 Q1 | +5원/kWh (최대치) | **동결** | 한전 재무 고려, 미반영 연료비 누적분 |
| 2026 Q2 | +5원/kWh | **동결** | 동일 |
| 2026 Q3 | +5원/kWh | **동결** (최신) | 연료비 하락 요인 있으나 한전 부채 고려 |

- **구조적 모순**: 연료비는 하락 추세이나 한전 부채 200조 원으로 인해 요금 인하 불가 → 소비자·산업계 모두 불만
- **산업용 전기요금**: 가정용은 동결하되 산업용은 **단계적 인상** 추진 (S&P Global)
- **정상화 전망**: 2026년 내 요금 인상은 정치적으로 어려움. **2027년 이후** 점진적 정상화 예상 (유안타증권)

**출처:**
- [Korea Herald: KEPCO Q3 전기요금 동결](https://www.koreaherald.com/article/10783299)
- [아시아경제: Q1 연료비 조정단가 +5원 유지](https://cm.asiae.co.kr/en/article/2025122208535329107)
- [S&P Global: KEPCO 및 5개 발전자회사 신용등급](https://www.spglobal.com/ratings/en/regulatory/article/-/view/sourceId/101652085)

---

## H-2. 전력시장 개편 로드맵

### H-2-1. 현행 구조와 개편 방향

| 구분 | 현행 | 개편 방향 |
|------|------|----------|
| **시장 구조** | 한전 중심 수직통합 (발전 60% + 송배전·판매 독점) | 단계적 경쟁 도입 |
| **가격 결정** | 변동비 반영 시장(CBP) — 원가 이하 판매 구조 | 실질 비용 반영 요금 체계 |
| **용량시장** | 2025년 첫 중앙계약경매 실시 | 확대 (2025: 540 MW → 2026~: 규모 확대) |
| **보조서비스시장** | 전력거래소 설계 중 | 주파수 조정·예비력 별도 시장 상품화 |
| **직접 PPA** | 2022년 전기사업법 개정으로 허용 | 활용 확대 유도 (현재 실적 미미) |

### H-2-2. 용량시장 (Capacity Market)

| 항목 | 내용 | 출처 |
|------|------|------|
| 제1차 경매 (2025) | 540 MW 확보 (본토 500 + 제주 40) — 2026년 수요 대응 | IEA Korea 2025 |
| 제2차 경매 | 2027년 수요 대상 | 전력거래소 |
| 입찰 대상 | 유연성 자원 (ESS, DR, 첨두 발전기) | IEA |
| 목적 | 재생에너지 간헐성 보완, 공급 안정성 확보 | IEA |

### H-2-3. 보조서비스시장 설계

- 전력거래소가 **계통운영 보조서비스**(주파수 조정, 전압 조정)와 **예비력**을 별도 시장 상품으로 거래 가능하도록 설계 중
- 현재는 발전사에 의무 부과 방식 → **시장 기반 인센티브**로 전환 목표
- ESS·DR·분산전원이 보조서비스 시장에 참여 시 **새로운 수익원** 창출 가능

**출처:**
- [IEA: 한국 전력시장 넷제로 개혁](https://www.iea.org/reports/reforming-koreas-electricity-market-for-net-zero/executive-summary)
- [RAP: 전력 부문 개혁과 에너지 전환 2026](https://www.raponline.org/wp-content/uploads/2026/02/sfoc-rap-power-sector-reform-energy-transition-2026-feb.pdf)
- [arxiv: 한국 전력시장 가격 왜곡과 개혁 경로](https://arxiv.org/html/2605.09318)

---

## H-3. 한국형 데이터센터 전력 공급 규제

### H-3-1. AI 데이터센터 특별법 (2026.05.07 국회 통과)

| 항목 | 내용 | 출처 |
|------|------|------|
| 법안명 | **인공지능 데이터센터 진흥에 대한 특별법** | 국회 |
| 통과일 | **2026년 5월 7일** 국회 본회의 의결 | ZDNet Korea |
| 시행일 | 공포 후 9개월 경과 → **2027년 2월** 시행 예정 | News1 |
| 핵심 내용 1 | AI DC를 **국가전략시설** 지정 → 통합 인허가 절차 | 과기정통부 |
| 핵심 내용 2 | **타임아웃제**: 일정 기간 내 인허가 미완료 시 자동 승인 | ZDNet Korea |
| 핵심 내용 3 | **비수도권 전력계통영향평가 면제** (일정 규모 이하) | ZDNet Korea |
| 제외된 조항 | **LNG 직접 PPA 조항 삭제** — 가장 큰 아쉬움 | Seoulz |

### H-3-2. 특별법의 한계

| 한계 | 설명 | 영향 |
|------|------|------|
| LNG 직접 PPA 미포함 | 국가전략시설로 지정되어도 LNG 직접 구매 불가 | BTM 가스발전 활성화 제한 |
| 전력 인프라 부족 | 국가전략시설 지정 후에도 실제 전력 공급까지 수년 | 인허가 단축 효과 제한적 |
| 수도권 제외 | 전력계통영향평가 면제는 **비수도권만** | 수도권 DC 신설 여전히 어려움 |
| 하위법령 미비 | 2026.06 하위법령 착수 단계 — 구체적 세부 기준 미확정 | 시행(2027.02)까지 불확실성 |

### H-3-3. 한국 데이터센터 시장 규모

| 지표 | 수치 | 출처 |
|------|------|------|
| 시장 규모 | $1.99B (2026) → **$5.02B (2031)**, CAGR **20.38%** | Mordor Intelligence |
| IT 부하 용량 | 1.96 GW (2025) → **6.32 GW (2030)**, CAGR **26.29%** | Mordor Intelligence |

**출처:**
- [ZDNet Korea: AI 데이터센터 특별법 통과](https://zdnet.co.kr/view/?no=20260508173106)
- [News1: AIDC 특별법 하위법령 착수](https://www.news1.kr/it-science/general-it/6201051)
- [Seoulz: 한국 DC 전력 — AI 붐 뒤의 그리드 위기](https://www.seoulz.com/korea-data-center-power/)
- [Mordor Intelligence: 한국 데이터센터 시장](https://www.mordorintelligence.com/industry-reports/south-korea-data-center-market)
- [KWM: 한국 DC PPA 이해와 활용](https://www.kwm.com/global/en/insights/latest-thinking/powering-data-centres-in-south-korea-understanding-and-using-ppas.html)

---

## H-4. 분산전원·마이크로그리드 정책

### H-4-1. 정책 프레임워크

| 정책 | 내용 | 시행 |
|------|------|------|
| **분산에너지법** | 분산전원 활성화 특별법 — 지산지소(地產地消) 기반 전력 체계 전환 | 시행 중 |
| **차세대 전력망** | 재생에너지·ESS·수요관리를 AI로 통합 제어하는 마이크로그리드 체계 | 2025년 착수 |
| **출력제어 조건부 접속** | 재생에너지 계통 접속 시 출력제어 수용 조건부 허용 | 2026년 시행 |
| **ESS 활용 신제도** | ESS 기반 새로운 전력 거래·서비스 제도 도입 | 2026년 도입 |
| **재생에너지 허수 관리** | 지연·미이행 사업자 관리 강화 | 2026년 강화 |

### H-4-2. 재생에너지 100 GW 목표와 전력망

| 지표 | 수치 | 출처 |
|------|------|------|
| 재생에너지 목표 | **100 GW** (정부 목표) | 파이낸셜뉴스 |
| 현재 재생에너지 설치 | ~30 GW (2025) | IEEFA |
| 전력망 확충 필요 규모 | 대규모 — 송변전 설비 확대가 관건 | 파이낸셜뉴스 |
| 직접 PPA 제도 | 2022년 전기사업법 개정으로 허용. 활용 미미 | KWM |

- **직접 PPA의 현실적 한계**: 한국에서는 한전의 단일 구매자(Single Buyer) 모델이 여전히 지배적. 2022년 직접 PPA 허용 이후에도 실제 계약 사례는 소수 → DC 전력 조달 유연성 제한
- **마이크로그리드 + AI DC**: 비수도권에 AI DC + 분산전원(태양광·ESS·연료전지) + 마이크로그리드를 통합하는 모델이 특별법의 실질적 혜택을 최대화하는 전략

**출처:**
- [파이낸셜뉴스: 재생에너지 100 GW, 전력망 확충이 관건](https://www.fnnews.com/news/202606121352454488)
- [IEEFA: 한국 재생에너지 성장의 그리드·PPA·RPS 개혁 의존](https://ieefa.org/articles/south-koreas-renewables-growth-depends-grid-power-purchase-agreements-ppas-and-renewable)
- [뉴스탭: 2026 전력시장 변화와 기업 대응 전략](https://www.newstap.co.kr/news/articleView.html?idxno=319685)

---

## H-5. 테마 H 투자 시사점

### H-5-1. 한전 관련 투자 판단

| 시나리오 | 확률 | 한전 영향 | 투자 함의 |
|---------|------|---------|----------|
| 2027년 이후 단계적 요금 정상화 | 높음 | 재무 개선 시작 | 장기적 긍정. 단기 모멘텀 제한 |
| 전력시장 구조 개편 (단일구매자 모델 완화) | 중간 | 한전 독점 약화, 신사업 기회 | 한전 자회사·민간 발전사 수혜 |
| AI DC 특별법 본격 시행 (2027.02~) | 높음 | DC 전력 수요 증가 → 한전 인프라 투자 | 한전기술·한전KDN 수혜 |
| LNG 직접 PPA 허용 (향후 개정) | 낮음 (단기) | 한전 판매 독점 침해 | 가스발전사·BTM 기업 수혜 |

### H-5-2. 정책 수혜 기업

| 기업 | 수혜 테마 | 근거 |
|------|----------|------|
| **한전기술** | AI DC 특별법 → 전력 인프라 설계·시공 | 국가전략시설 전력 공급 설계 |
| **한전KDN** | 디지털 그리드·스마트 미터링 | 차세대 전력망 구축 IT 인프라 |
| **LS일렉트릭** | 분산전원·마이크로그리드 장비 | DC 전력 솔루션 + 배전기기 (테마 C·D 동시 수혜) |
| **HD현대일렉트릭** | 비수도권 DC 전력 인프라 | 초고압 변압기 국내 수요 + 북미 수출 |
| **두산퓨얼셀** | BTM 연료전지 | AI DC 자가발전용 SOFC·PAFC |
| **SK E&S** | LNG 직접 PPA 허용 시 최대 수혜 | 국내 최대 민간 LNG 발전사 |
| **LG에너지솔루션** | ESS 신제도 + 용량시장 | 그리드 ESS + DC 백업 ESS |

### H-5-3. 핵심 투자 테제

1. **"특별법은 시작일 뿐"**: AI DC 특별법 통과는 긍정적이나 LNG 직접 PPA 미포함 + 하위법령 미비 → 실질 효과는 **2027년 하반기 이후**
2. **한전 요금 정상화는 점진적**: 200조 부채 해소에 **최소 5년+**. 급격한 요금 인상은 정치적으로 불가 → 한전 주가 리레이팅은 장기 스토리
3. **분산전원이 진짜 기회**: 마이크로그리드·ESS·연료전지를 통합한 분산형 DC 전력이 특별법의 실질 수혜 → LS일렉트릭·두산퓨얼셀·LG에너지솔루션
4. **용량시장·보조서비스시장 개설**: ESS 사업자에게 **새로운 수익 모델** 제공 → ESS 설치 가속화의 정책적 촉매

---

## H-6. 테마 H 모니터링 지표

| 지표 | 빈도 | 임계값 / 의미 |
|------|------|-------------|
| 한전 분기 부채 잔고 | 분기 | 200조 원 → 180조 원 이하 = 재무 개선 시그널 |
| 전기요금 연료비 조정단가 | 분기 | +5원/kWh 유지 vs 인상 전환 |
| AIDC 특별법 하위법령 제정 | 상시 | 2027.02 시행 전 세부 기준 확정 여부 |
| LNG 직접 PPA 허용 논의 | 상시 | 국회 개정안 발의 여부 |
| 용량시장 경매 규모 | 연간 | 540 MW → 확대 속도 |
| 한국 DC IT 부하 용량 (GW) | 반기 | 1.96 GW(2025) → 6.32 GW(2030) 궤적 |
| 비수도권 DC 인허가 건수 | 분기 | 특별법 효과의 실질 지표 |

---

---

## 테마 E~H 통합 — 4개 테마의 교차점

### 테마 간 상호 작용 맵

```
테마 E (지정학)     ←──→     테마 F (ESS)
│ 희토류 통제 → ESS 모터·자석 원자재 리스크    │
│ FEOC 규정 → LG·삼성SDI 미국 반사이익        │
│ 관세 15% → 현지 생산 헤지                    │
↕                                              ↕
테마 G (PPA)       ←──→     테마 H (한국 정책)
│ BTM PPA → 가스터빈·연료전지 수요              │
│ 원전 PPA → Constellation·Vistra 재평가        │
│ 한국 직접 PPA 제한 → 한전 독점 지속            │
```

### 핵심 교차 투자 테제

1. **지정학 + ESS**: 중국 FEOC 규정이 한국 배터리 3사(LGES·삼성SDI·SK온)의 미국 ESS 시장 점유율을 구조적으로 보호. CATL·BYD의 미국 직접 진출 제한이 한국 기업의 최대 비관세 해자
2. **PPA + 한국 정책**: 한국의 단일구매자 모델과 LNG 직접 PPA 미허용이 AI DC 전력 조달의 구조적 제약 → 비수도권 분산전원 모델이 현실적 대안
3. **지정학 + PPA**: 미국 관세·FEOC가 글로벌 에너지 장비 공급망을 재편 → 한국 기업의 미국 현지 생산이 PPA 체결 시 "로컬 콘텐츠" 가산점
4. **ESS + 한국 정책**: 용량시장·보조서비스시장 개설이 ESS 사업자에게 새 수익원 → 한국 ESS 설치 가속화 → LGES·삼성SDI 국내 수요 확보

### 테마 A~H 전체 연결 요약

```
[테마 A: 원전 SMR]     [테마 E: 지정학]       [테마 G: PPA]
      │                       │                      │
  장기 베이스로드        희토류·관세·공급망        원전 PPA 프리미엄
      │                       │                      │
      └──── 가스 브릿지 ──────┼──── BTM 가속 ────────┘
                              │
[테마 B: 가스터빈]     [테마 F: ESS]          [테마 H: 한국 정책]
      │                       │                      │
  슈퍼사이클 지속        BESS 통합·장주기       전기요금·용량시장
      │                       │                      │
      └──── 전력 인프라 ──────┼──── DC 전력 혁명 ─────┘
                              │
[테마 C: 송배전]       [테마 D: DC/냉각]
      │                       │
  변압기 병목·HVDC       800V DC·액체냉각
```

---

## 출처 종합

### 테마 E — 지정학
- [IEA: 핵심광물 수출 통제](https://www.iea.org/commentaries/with-new-export-controls-on-critical-minerals-supply-concentration-risks-become-reality)
- [S&P Global: 희토류 공급 병목 2026](https://www.spglobal.com/energy/en/news-research/latest-news/metals/012726-rare-earth-supply-bottlenecks-set-to-persist-in-2026)
- [CSIS: 관세와 AI DC 건설](https://www.csis.org/analysis/impact-tariffs-ai-data-center-buildout-balancing-supply-chain-security-and-ai)
- [CSIS: $3T AI 건설 위험](https://www.csis.org/analysis/how-tariffs-could-derail-united-states-3-trillion-ai-buildout)
- [CCIA: 반도체 관세 $90B/년](https://ccianet.org/articles/applying-semiconductor-tariffs-to-data-centers-would-cost-the-u-s-90-billion-a-year/)
- [ODI: 핵심광물 지정학 2026](https://odi.org/en/insights/critical-minerals-geopolitics-in-2026-risks-supply-chains-and-global-power-shifts/)
- [HD현대일렉트릭 앨라배마 — PRNewswire](https://www.prnewswire.com/news-releases/hd-hyundai-electric-expands-us-production-subsidiary-solidifies-leadership-in-north-american-extra-high-voltage-power-transformer-market-302707507.html)
- [LS Electric 배스트롭 캠퍼스](https://powersystems.technology/news/ls-electric-launches-bastrop-campus-for-u-s-production-of-transformers-and-power-gear-transformer-technology-news.html)
- [효성중공업 멤피스 — Korea Herald](https://www.koreaherald.com/article/10618541)
- [Transformer Magazine: 한국 전력기기](https://transformers-magazine.com/tm-news/korean-power-equipment-makers-expand-amid-us-boom/)

### 테마 F — ESS
- [Fortune BI: 그리드 스케일 배터리](https://www.fortunebusinessinsights.com/industry-reports/grid-scale-battery-market-101304)
- [MarketsandMarkets: BESS](https://www.marketsandmarkets.com/Market-Reports/battery-energy-storage-system-market-112809494.html)
- [GreentechLead: 88.4 GW by 2027](https://greentechlead.com/renewable-energy/battery-storage-market-set-to-double-to-88-4-gw-by-2027-as-tesla-byd-catl-and-fluence-accelerate-investments-53589)
- [Tesla 46.7 GWh — Battery-Tech](https://battery-tech.net/battery-markets-news/tesla-energy-posts-46-7-gwh-storage-deployments-in-2025/)
- [LGES 90 GWh 목표](https://www.energy-storage.news/lg-energy-solution-targets-50-percent-share-of-us-energy-storage-market-in-2026/)
- [Fluence $5.6B 백로그](https://www.ess-news.com/2026/05/08/fluence-reports-5-6-billion-order-backlog-as-battery-pipeline-swells/)
- [BYD Tesla 추월 — Electrek](https://electrek.co/2026/05/13/byd-surpasses-tesla-energy-storage-bess-benchmark-2025/)
- [Form Energy Crusoe 12 GWh](https://www.crusoe.ai/resources/newsroom/form-energy-crusoe-announce-agreement-for-12-gigawatt-hours-of-iron-air-batteries-for-ai-data-centers)
- [GM Insights: 장주기 ESS](https://www.gminsights.com/industry-analysis/long-duration-energy-storage-market)

### 테마 G — PPA
- [EnkiAI: GW급 PPA](https://enkiai.com/solar/gigawatt-ppas-how-ai-redefined-hyperscaler-energy-in-2026/)
- [BloombergNEF: 기업 청정에너지 구매](https://about.bnef.com/insights/clean-energy/corporate-clean-energy-buying-fell-in-2025-after-nearly-a-decade-of-growth/)
- [Fact.MR: DC 전력 중개 시장](https://www.factmr.com/report/data-center-power-brokerage-services-market)
- [PV Magazine: AI DC 태양광 PPA](https://pv-magazine-usa.com/2026/03/13/ai-datacenters-rewrite-the-solar-ppa-playbook/)
- [S&P Global: 하이퍼스케일러 전력 조달](https://www.spglobal.com/sustainable1/en/insights/special-editorial/hyperscaler-procurement-to-shape-us-power-investment)
- [Power Magazine: 하이퍼스케일러 그리드 투자 서약](https://www.powermag.com/hyperscalers-sign-white-house-pledge-to-fund-data-center-power-grid-upgrades/)

### 테마 H — 한국 정책
- [Korea Herald: KEPCO Q3 동결](https://www.koreaherald.com/article/10783299)
- [IEA: 한국 전력시장 넷제로 개혁](https://www.iea.org/reports/reforming-koreas-electricity-market-for-net-zero/executive-summary)
- [ZDNet Korea: AI DC 특별법 통과](https://zdnet.co.kr/view/?no=20260508173106)
- [News1: 특별법 하위법령 착수](https://www.news1.kr/it-science/general-it/6201051)
- [Seoulz: 한국 DC 전력 그리드 위기](https://www.seoulz.com/korea-data-center-power/)
- [Mordor Intelligence: 한국 DC 시장](https://www.mordorintelligence.com/industry-reports/south-korea-data-center-market)
- [KWM: 한국 DC PPA](https://www.kwm.com/global/en/insights/latest-thinking/powering-data-centres-in-south-korea-understanding-and-using-ppas.html)
- [IEEFA: 한국 재생에너지 성장](https://ieefa.org/articles/south-koreas-renewables-growth-depends-grid-power-purchase-agreements-ppas-and-renewable)

### 기존 참조
- `data/research_ai_power_part12_overview.md` — Part 1-2 기본 데이터
- `data/research_ai_power_themes_AB.md` — 테마 A(원전 SMR) + B(가스터빈)
- `data/research_ai_power_themes_CD.md` — 테마 C(송배전 병목) + D(DC 전력/냉각)
