# AI 전력 인프라 테마 심화 리서치 — 테마 A·B

> 목적: SMR·원전 르네상스(테마 A)와 가스터빈 슈퍼사이클(테마 B) 심화 분석
> 작성일: 2026-06-23
> 참조: `data/research_ai_power_part12_overview.md` (Part 1-2 기본 데이터)
> 상태: 초안

---

# 테마 A — SMR과 원전 르네상스 (Nuclear Renaissance)

## A-1. 배경: 왜 지금 원전인가

AI 데이터센터의 전력 수요는 24시간 365일 중단 없는 '클린 베이스로드'를 요구한다. 태양광·풍력은 간헐성으로 이를 충족하지 못하고, 가스는 탄소 중립 목표와 충돌한다. 이 구조적 갭이 원전·SMR 르네상스의 근본 원인이다.

- AI 데이터센터 전력 수요: 415 TWh(2024) → 950~1,350 TWh(2030E), CAGR ~15% (IEA·Goldman Sachs)
- 하이퍼스케일러의 원전 관심: 단순한 ESG 이미지 포지셔닝이 아닌, 전력 확보 수단으로서의 실용적 선택
- 계통연계 큐 병목: 미국 DC의 절반이 전력 확보 실패로 지연. BTM/원전 PPA가 우회로로 부상

---

## A-2. 글로벌 SMR 프로젝트 현황 (2026년 중반 기준)

### A-2-1. NuScale VOYGR — 루마니아 도이체스티 프로젝트

| 항목 | 내용 |
|------|------|
| 프로젝트명 | Doicești SMR, 루마니아 (다음바비차 주) |
| 기술 | NuScale VOYGR-6: 77 MWe × 6모듈 = **462 MWe 총 출력** |
| FID 승인 | 2026년 2월 12일 — Nuclearelectrica 주주총회 승인 |
| 전략 변화 | 6모듈 동시 착공 → **1모듈 선행 시범(77 MWe) 후 5모듈 추가** 방식으로 리스크 분산 |
| 현재 단계 | Pre-EPC 단계(~15개월): 지반 조사, 인허가 진행, 사전계약(pre-EPC) 체결, 장납기기자재 발주, 공급망 정의 |
| 완공 목표 | 당초 2029-30 → **2033-34로 약 4년 지연** (규제 심사·비용 재산정) |
| 재원 | EU·미국 지원 포함. €2.75억 미국 DFC 재정 지원 |
| Standard Power (미국 별도) | NuScale 기술로 오하이오·펜실베이니아 DC 전력용 SMR 2개소 계획 (24모듈, 1,848 MWe). 별도 프로젝트 |
| 주가 현황 | -26.5% (2026.02), UBS PT $38→$20 하향. 시총 ~$4.4B. 매출 0, 적자 지속 |

**출처**: [Power Magazine](https://www.powermag.com/romanias-coal-to-nuscale-smr-conversion-secures-fid-moves-into-implementation-with-caveats/), [World Nuclear News](https://world-nuclear-news.org/articles/final-investment-decision-taken-for-romanias-smrs), [Neutron Bytes](https://neutronbytes.com/2026/02/13/final-investment-decision-approved-for-six-nuscale-smrs-in-romania/)

---

### A-2-2. TerraPower Natrium — 케머러 프로젝트 (미국 최초 상용 비경수로)

| 항목 | 내용 |
|------|------|
| 기술 | Natrium SFR(소듐냉각고속로) **345 MWe** + 용융염 에너지저장(250 MWh) |
| NRC 건설허가 | **2026년 3월 4일** — 상용 비경수로 역사상 최초 NRC 건설허가 |
| 착공 | **2026년 4월 23일** — 미국 역사상 첫 유틸리티급 선진원전 착공 |
| 부지 | Kemmerer, Wyoming (폐쇄된 석탄발전소 인근) |
| 완공 목표 | **2030년** |
| 비용 | $4B+ (DOE $2B 지원 포함) |
| NRC 심사 | 2025년 12월 안전심사 완료 — 일정 내·예산 11% 절감 |
| 하이퍼스케일러 연계 | Meta의 6.6 GW 원전 포트폴리오 일부 |

**출처**: [TerraPower](https://www.terrapower.com/TerraPower-Commences-Construction-on-Americas-First-Utility-Scale-Advanced-Nuclear-Power-Plant), [DOE](https://www.energy.gov/ne/articles/nrc-issues-construction-permit-terrapowers-natrium-advanced-reactor), [ANS](https://www.ans.org/news/2026-04-24/article-7975/terrapower-begins-construction-on-natrium-power-plant-in-kemmerer/)

---

### A-2-3. Kairos Power Hermes 2 — Google 상용 데모로

| 항목 | 내용 |
|------|------|
| 기술 | FHR(불소염냉각고온로) — TRISO 연료 |
| Hermes 1 | 오크리지 테스트로 (2025.05 착공) |
| Hermes 2 | **2026년 4월 21일 착공** — 오크리지, 테네시. 최초 발전용 Gen IV 원자로 건설허가 |
| 출력 | ~50 MWe (Hermes 2 TVA 계통 공급) |
| Google 계약 | 6~7기 SMR로 **500 MW 전력 공급** (2030년 첫 완공, 2035년 전체) |
| TVA 협력 | TVA 전력망에 연결 → 테네시·앨라배마 Google DC 탈탄소화 |
| 공장제작 | 앨버커키 제조 캠퍼스에서 모듈 제작 후 오크리지 현장 조립 |

**출처**: [Kairos Power](https://www.kairospower.com/updates/kairos-power-breaks-ground-on-hermes-2-demonstration-plant), [Axios](https://www.axios.com/pro/climate-deals/2026/04/17/kairos-google-hermes-2-reactor-construction), [World Nuclear News](https://www.world-nuclear-news.org/articles/google-kairos-power-tva-announce-collaboration)

---

### A-2-4. X-energy Xe-100 — IPO·Amazon 투자

| 항목 | 내용 |
|------|------|
| 기술 | HTGR(고온가스냉각로) 80 MWe × 4모듈 = **320 MWe 플랜트** |
| IPO | **2026년 4월 24일** Nasdaq(XE) 상장. 공모가 $23 (희망범위 $16-19 상회) |
| IPO 규모 | **$1.02B** 조달 (업사이즈). 시초가 $30.11, 종가 $29.20 (+27%) |
| 현재 주가 | ~$21.40 (IPO 후 하락. 시장 관망) |
| Amazon 투자 | 시리즈C-1 $500M 주도. 총 사전 조달 $1.8B |
| Amazon 전력 계약 | 2039년까지 최대 **5 GW** 전력 구매 구속 약정 |
| NRC 심사 | Dow 시드리프트(TX) 플랜트 건설허가 NRC 심사 중 |

**출처**: [X-energy](https://x-energy.com/news/x-energy-announces-pricing-of-upsized-initial-public-offering/), [Seeking Alpha](https://seekingalpha.com/news/4579196-amazon-backed-nuclear-startup-x-energy-raises-102b-in-ipo), [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-24/amazon-backed-x-energy-climbs-31-after-1-02-billion-us-ipo)

---

### A-2-5. Rolls-Royce SMR — 영국 프로젝트 + 두산에너빌리티 합류

| 항목 | 내용 |
|------|------|
| 기술 | 470 MWe PWR. **90%를 공장 제작** 후 현장 조립 |
| 영국 계약 | 2026년 4월, Great British Energy-Nuclear(GBE-N)과 계약 체결. Wylfa(북웨일스) 3기 부지별 설계 착수 |
| FID 예정 | **2029년** Wylfa FID 목표 |
| 체코 Temelín | 루마니아에 이어 유럽 제2의 프로젝트로 추진 |
| 두산에너빌리티 합류 | **2026년 5월 28일** 핵심 기자재 파트너 선정. 체코 Škoda JS와 듀얼 서플라이어 체계 |
| 두산 역할 | 원자로 압력용기(RPV) 등 핵섬(Nuclear Island) 주요 기자재 사전제작 |

**출처**: [Korea Herald](https://www.koreaherald.com/article/10757884), [TechTimes](https://www.techtimes.com/articles/317469/20260531/doosan-enerbility-wins-rolls-royce-smr-work-q1-orders-jump-62-amid-data-center-push.htm), [World Nuclear News](https://www.world-nuclear-news.org/articles/skoda-js-doosan-enerbility-get-key-rolls-royce-smr-work)

---

### A-2-6. 한국 SMR — i-SMR 개발·SMART 수출 현황

| 항목 | 내용 |
|------|------|
| i-SMR | 한국수력원자력(KHNP) + 원자력연구원(KAERI) 컨소시엄. **170 MWe 일체형 PWR** (4기 조합 시 680 MW) |
| 개발 단계 | 2023-25년 개념·기본설계 완료. **2028년 표준설계인가(SDA) 신청** 목표 |
| 상업 운전 | 2035년 이후 (허가 2028, 건설허가 2030년대 초) |
| SMART 수출 | 캐나다 수출 사실상 중단 (현지 파트너 확보 실패·수요 부족). 정부, SMART 노선에서 i-SMR로 전략 전환 |
| SMR 특별법 | 한국 국회, SMR 전담법 통과 (2026년). 상업화 전담조직 구성 검토 중 |
| 두산에너빌리티 역할 | 한국 SMR 생태계의 핵심 기자재 제조사. 신한울 3·4호기 주기기(원자로·증기발생기·터빈발전기) ₩2.9조 계약 |

**출처**: [Seoul Economic Daily](https://en.sedaily.com/technology/2026/04/12/korea-pushes-next-gen-i-smr-as-smart-reactor-stalls), [World Nuclear News](https://www.world-nuclear-news.org/articles/standard-design-approval-sought-for-i-smr), [NEI Magazine](https://www.neimagazine.com/news/south-korea-smr-act-passed/)

---

## A-3. 기존 원전 재가동·신규 프로젝트

### A-3-1. Constellation Energy — TMI Unit 1 (Crane Clean Energy Center)

| 항목 | 내용 |
|------|------|
| 프로젝트명 | Crane Clean Energy Center (TMI Unit 1 재가동) |
| 출력 | **835 MWe** |
| PPA | Microsoft 20년 전력구매계약 (퇴역 원전 재가동 최초 사례) |
| 투자 | $1.6B + DOE $1B 대출 |
| 완공 | 당초 **2027년 말** 목표 → PJM이 계통연계 **2031년**까지 불가 통보 (송전망 업그레이드 필요). FERC 웨이버 획득했으나 실제 풀파워 지연 가능성 |
| 의의 | 하이퍼스케일러 AI DC에 핵전력이 공급되는 최초 사례. 단, PJM 계통연계 지연으로 2027년 첫 전자(first electrons) 목표 불확실 |

**출처**: [NEI Magazine](https://www.neimagazine.com/news/ferc-clears-tmi-restart/), [ANS](https://www.ans.org/news/article-6402/constellation-announces-tmi1-restart-power-purchase-agreement-with-microsoft/)

---

### A-3-2. Palisades 원전 재가동 (미시간)

| 항목 | 내용 |
|------|------|
| 운영사 | Holtec International |
| 출력 | 800 MWe |
| 재가동 목표 | 당초 2025년 말 → **2026년 초로 지연** → 추가 지연 가능성 |
| 지연 원인 | 증기발생기 튜브 균열(sleeve 수리), 원래 용접 기록 누락 등 NRC 추가 요구사항 |
| 의미 | 완전 폐로된 원전 재가동 최초 시도. 성공 시 미국 전역에 유사 사례 확산 가능 |

**출처**: [Michigan Public](https://www.michiganpublic.org/environment-climate-change/2025-12-17/palisades-nuclear-plant-restart-plans-pushed-back-to-early-2026), [E&E News](https://www.eenews.net/articles/michigan-nuclear-plant-operator-delays-restart/)

---

### A-3-3. 한국 신한울 3·4호기

| 항목 | 내용 |
|------|------|
| 기술 | APR1400 (한국형 가압경수로 1,400 MWe) |
| 건설허가 | 2024년 9월 취득 |
| 착공 | Unit 3: 2025년 5월 첫 콘크리트. Unit 4: 2025년 5월 29일 |
| 완공 목표 | Unit 3: **2032년**, Unit 4: **2033년** |
| 주기기 계약 | Doosan Enerbility — ₩2.9조 (원자로·증기발생기·터빈발전기) |

**출처**: [World Nuclear News](https://www.world-nuclear-news.org/articles/construction-starts-for-shin-hanul-unit-4)

---

### A-3-4. 체코 두코바니 (KHNP 수출)

| 항목 | 내용 |
|------|------|
| 기술 | APR1000 (1,055 MWe × 2기) |
| 계약 | KHNP 우선협상대상자 선정(2024.07). EPC 계약 체결. 총 **기당 $8.6B** |
| 착공 예정 | **2029년** |
| 첫 호기 운전 | **2036년** |
| 준비작업 비용 | 약 800~850억 코루나 (€3.2~3.4B) |
| 한국-체코 협력 | 장관급 운영위원회(Ministerial Steering Committee) 설치. KHNP CEO 2026.06 두코바니 방문 검토 |
| EU 조사 | 2025년 12월 EU, 체코 정부 지원방식 조사 착수 (국가보조금 심사) |
| Doosan 연계 | 두코바니 스팀터빈 ₩320B 수주 (별도) |

**출처**: [Czech MPO](https://mpo.gov.cz/en/guidepost/for-the-media/press-releases/epc-contract-for-completion-of-dukovany-has-been-signed--minister-of-industry-and-trade--lukas-vlcek-will-visit-korea-again-in-july--287912/), [CEEnergynews](https://ceenergynews.com/nuclear/czechia-south-korea-dukovany-nuclear-expansion/), [Korea Times](https://www.koreatimes.co.kr/amp/business/companies/20260618/khnp-ceo-reviews-dukovany-project-in-czech-republic)

---

### A-3-5. 프랑스 EDF — EPR2 신규 원전 계획

| 항목 | 내용 |
|------|------|
| 프로그램 | 6기 EPR2 신규 건설 (Penly·Gravelines·Bugey) |
| 비용 | **€72.8B** (약 $85.3B) — 이사회 예산 확정 |
| 2026 예산 배정 | €2.7B (2026년 프로그램 예산) |
| FID 목표 | **2026년 말** FID 채택 목표 |
| 착공 | 2024년 7월 Penly 부지 공사 시작. 핵심 콘크리트(first nuclear concrete) **2029년 3월** 예정 |
| 재원 | EU 보조금 심사 중 (국가지원 절반 이상 보조 대출 + 40년 CFD + 국가-EDF 리스크 분담) |
| 의미 | 프랑스의 원전 르네상스 재확인. 유럽 내 대형 원전 신규 발주의 유일한 사례 |

**출처**: [World Nuclear News — EPR2 비용](https://www.world-nuclear-news.org/articles/edf-estimates-epr2-programme-costs-at-eur728-billion), [NucNet](https://www.nucnet.org/news/edf-announces-eur100-million-investment-in-factory-for-epr2-equipment-4-2-2026)

---

## A-4. 하이퍼스케일러 원전 커밋먼트 (2026년 6월 기준)

| 기업 | 규모 | 파트너 | 첫 전력 예상 |
|------|------|--------|------------|
| **Meta** | 최대 **6.6 GW** | TerraPower(Natrium) + Oklo(Aurora) + Vistra + Constellation | 2030년대 |
| **Microsoft** | **835 MW** | Constellation (TMI/Crane Clean Energy Center) | **2027년** |
| **Google** | **500 MW** | Kairos Power (6~7기 SMR) | **2030년** (첫 기) |
| **Amazon** | 최대 **5 GW** | X-energy Xe-100 (최대 12기 → 5 GW 약정) | 2030년대 |
| **합계** | **13개 프로젝트, ~9.8+ GW** | — | 첫 전자: 2027 (TMI) |

- **구조적 시사점**: 총 ~9.8+ GW 커밋먼트는 인상적이나, 실제 AI DC에 핵전력이 도달하는 최초 시점은 2027년(TMI 재가동 835 MW). 그 외 SMR 신규 건설은 2030~2035년. **갭 구간 5~10년이 가스터빈 브릿지의 근거**
- **Carnegie Endowment 분석(2026.06)**: 하이퍼스케일러 원전 커밋먼트가 과대 포장되었다는 비판. 구속력 없는 MOU 다수, 실제 착공·FID는 소수

**출처**: [smrintel.com](https://smrintel.com/nuclear-data-center-deals/), [Carnegie Endowment](https://carnegieendowment.org/research/2026/06/beyond-the-hype-assessing-hyperscaler-nuclear-commitments-against-us-energy-realities)

---

## A-5. NRC 규제 환경 변화 (2026년)

| 항목 | 내용 |
|------|------|
| Part 53 시행 | **2026년 4월 29일** 발효 — 선진원자로용 위험정보 기반 기술중립 인허가 프레임워크 (비경수로 포함) |
| 마이크로원자로 규정 | 2026년 5월 연방관보 공표 — 소형·비교적 안전한 원자로 대상 간소화 경로 |
| NRC 가속 경로 제안 | DOE·DOW 승인 원자로 설계에 대한 가속 인허가 경로 제안 |
| 파이프라인 전망 | 2029년까지 25건 SMR 신청 예상 (FERC-NRC 합동회의 추정) |

**출처**: [NRC](https://www.nrc.gov/reactors/new-reactors/advanced), [Morgan Lewis](https://www.morganlewis.com/pubs/2026/04/nrc-launches-fresh-licensing-framework-for-new-reactors), [Federal Register](https://www.federalregister.gov/documents/2026/03/30/2026-06048/risk-informed-technology-inclusive-regulatory-framework-for-advanced-reactors)

---

## A-6. SMR 시장 규모 전망

| 지표 | 수치 | 출처 |
|------|------|------|
| 글로벌 SMR 시장 | $6.3B (2026) → $8.1B (2033), CAGR 3.6% | MarketsandMarkets |
| 설치 용량 | 312.5 MW (2025) → 912.5 MW (2030), CAGR 23.9% | Mordor Intelligence |
| NuScale 단독 시총 | ~$4.4B (시장 내 최대 상장사) | SEC/Bloomberg |
| NRC 인허가 파이프라인 | 2029년까지 25건 신청 전망 | FERC-NRC 합동회의 |
| X-energy IPO 시총 | $1.02B 조달, $23 공모 기준 | Nasdaq |
| TerraPower(비상장) | DOE $2B 지원, 총 $4B+ 프로젝트 | DOE |

---

## A-7. 일본의 SMR 국가 전략과 한-일 공급망 경쟁

### A-7-1. 일-미 $550B 전략투자 협정과 원자력 배분

| 항목 | 내용 |
|------|------|
| 배경 | 2025년 10월 일-미 전략투자 협정 (관세 25%→15% 교환) |
| 총 규모 | **$550B** 대미 투자, 에너지 부문 **$327B** |
| 원자력 배분 | 최대 **$200B** — 웨스팅하우스 AP1000+SMR **$100B** + GE Vernova-히타치 BWRX-300 **$100B** |
| 투자 방식 | 지분 투자 → 배당/전력 판매 수익 (민자 사업) |

**출처**: [U.S. Commerce Dept](https://www.commerce.gov/news/press-releases/2026/03/joint-announcement-japan-us-strategic-investment), [AAF](https://www.americanactionforum.org/insight/u-s-japan-trade-deal-investment-commitments-in-nuclear-energy/), [Japan Times](https://www.japantimes.co.jp/business/2026/03/20/us-japan-trade-pact/)

---

### A-7-2. 일본 원전 산업의 흥망성쇠

| 시기 | 상황 |
|------|------|
| 후쿠시마 이전 | 54기 운영, 세계 3위 원전 강국 |
| 후쿠시마 이후 | 전면 가동 중단 → 15년간 공급망·인력 붕괴 |
| 2026년 현재 | 15기만 재가동 (32기 중), 2040년 30기 목표 |
| 주요 이벤트 | 가시와자키-카리와 6호기 14년 만에 재가동 (2026.02) |

**출처**: [World Nuclear Association](https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-power), NBC News

---

### A-7-3. 도시바-웨스팅하우스 몰락의 교훈

| 항목 | 내용 |
|------|------|
| 인수 | 2006년 $54억에 웨스팅하우스 인수 |
| 파산 | AP1000 비용 폭등 → 2017년 Chapter 11 (손실 **$90억**) |
| 매각 | 2018년 브룩필드에 $46억 매각, 도시바 그룹 사실상 해체 |
| 교훈 | 대형 원전 건설의 비용·일정 리스크는 국가급 기업도 파괴 가능 |

**출처**: [CNBC](https://www.cnbc.com/2017/03/29/huge-nuclear-cost-overruns-push-toshibas-westinghouse-into-bankruptcy.html), [CSIS](https://www.csis.org/analysis/westinghouses-bankruptcy-and-its-implications)

---

### A-7-4. 일본의 해외 원전 수출 실패사

- 2010년대 베트남·영국 수주 시도 → 안전 기준 강화로 공사비 상승 → 줄줄이 백지화
- 대형 원전 수출 막힌 상황에서 SMR 초기 시장으로 전략 전환

---

### A-7-5. SMR 초도기 시장 선점 전략 — 자본의 힘

- **전략**: 표준화 덜 된 SMR 초기 시장을 대규모 자본으로 선점 → 공급망 부활
- **히타치**: BWRX-300용 원자로 내부구조물·제어봉 구동장치(FMCRD) 등 일본 내 제조·공급 (달링턴 1호기)
- **미쓰비시중공업, IHI**: 웨스팅하우스 SMR 프로젝트 참여
- **"일본 기업 우선 납품" 조건 부착** — 한국 기업 소외 리스크

**출처**: [Hitachi press release](https://www.hitachi.com/New/cnews/month/2025/05/250509.html), ANS Nuclear Newswire

---

### A-7-6. 한-일 공급망 경쟁 구도: 두산 vs 일본

#### 두산에너빌리티의 기술적 해자

| 항목 | 수치 |
|------|------|
| RPV 공급 실적 | **34기** |
| 증기발생기 | **124기** |
| 원전 공급 실적 | **80+기** |
| 생산 체계 | 창원 일관 생산 (원자재→최종 조립) |
| SMR 전용 공장 | 2026~2031 신설, **8,068억원**, 연 20기 생산 |
| SMR 파트너십 | NuScale·TerraPower·Rolls-Royce SMR·X-Energy 등 전방위 |

#### 일본의 현실적 역량

| 항목 | 평가 |
|------|------|
| 히타치 | BWRX-300 내부 부품 자국 공급 가능 (원자로 내부구조물, FMCRD) |
| 대형 주기기 | 압력용기 등 두산 대비 열위 |
| 인력·설비 | 15년 공백으로 숙련 인력·대형 단조 역량 약화 |

**핵심 판단**: 단기(3~5년)는 두산 대체 불가. 중장기(5~10년)는 일본 자본력으로 공급망 재건 시도 모니터링 필요

**출처**: NuScale-Doosan 계약, TechTimes, Hitachi press

---

### A-7-7. 투자 시사점 (일본 변수)

- **기회**: 일본 자본이 SMR 시장 전체 파이를 키움 → 두산 수주 물량 확대
- **리스크**: 일본 기업 우선 납품 조건이 장기적으로 한국 기업 비중 잠식 가능
- **모니터링**: 일-미 투자 트랜치별 일본 기업 실제 참여 비중, 히타치 대형 주기기 역량 재건 속도

---

## A-8. 투자 시사점 (테마 A)

### 단기 (2026~2027년)
- **Constellation Energy**: TMI 재가동 당초 2027년 목표이나 PJM 계통연계 2031년 지연 리스크. Calpine **$21.84B** 인수(SEC 8-K 기준)로 60 GW 발전포트폴리오(원전 32.4 GW + 가스 26 GW) 완성. FY26 EPS +20% 전망
- **두산에너빌리티**: 신한울 3·4 주기기 + 체코 두코바니 스팀터빈 + Rolls-Royce SMR RPV — 원전 기자재 수주잔고 다층적. 1Q26 수주잔고 $16.2B (+62%)

### 중기 (2028~2031년)
- **TerraPower/Kairos**: 비상장·초기 단계. TerraPower 2030 완공 목표가 실현되면 SMR 상업화 최초 사례. Google·Meta 대형 PPA와 연계
- **X-energy (XE)**: IPO 후 주가 하락($29→$21). 장기 성장 스토리이나 매출 없는 적자 기업. Amazon 5 GW 약정이 구체화되면 재평가

### 리스크 요인
1. **리드타임 리스크**: NuScale Romania 4년 지연 사례. 모든 SMR 프로젝트에 공통적인 규제·공급망·비용 지연 리스크
2. **비용 구조**: SMR의 $/kW 비용은 아직 대형 원전 대비 불리. 모듈화·공장제작이 이를 해소할지 불확실
3. **하이퍼스케일러 커밋먼트 실질성**: MOU와 구속력 있는 PPA 혼재. 실제 FID까지 이탈 가능성
4. **가스터빈 브릿지 지속**: SMR 지연이 길수록 가스터빈 수요 연장. 역설적으로 SMR 지연 = 가스터빈 강세

---

## A-9. 모니터링 지표 (테마 A)

| 지표 | 모니터링 포인트 | 빈도 |
|------|--------------|------|
| NuScale Romania | Pre-EPC 계약 체결 여부, 지반조사 완료 일정 | 분기 |
| TerraPower Kemmerer | 건설 진척도(월간 업데이트), 2030 완공 준수 여부 | 분기 |
| X-energy (XE) | NRC Dow Seadrift 허가 진행, Amazon 구속약정 구체화 | 분기 |
| Palisades | NRC 추가요구 충족 여부, 재가동 일정 확정 | 월간 |
| TMI/Crane Clean | 2027 완공 일정 준수 확인, FERC 계통연계 | 반기 |
| 두코바니 | EU 국가보조금 조사 결론, KHNP EPC 세부 계획 | 분기 |
| 한국 i-SMR | NSSC SDA 신청 준비 진행도 | 반기 |
| 하이퍼스케일러 | 신규 원전 PPA 발표, 기존 MOU → FID 전환 여부 | 월간 |
| NRC Part 53 | 신규 신청 건수, 심사 소요기간 단축 여부 | 반기 |
| 일-미 투자 트랜치 | 2차·3차 투자 구체화, 일본 기업 실제 참여 비중 | 분기 |
| 히타치 대형 주기기 | BWRX-300 후속기 주기기 자국 제조 전환 여부 | 반기 |
| 두산 일본 경쟁 | NuScale·GEH 프로젝트에서 두산 vs 일본 기업 점유율 변화 | 반기 |

---

---

# 테마 B — 가스터빈 슈퍼사이클 (Gas Turbine Supercycle)

## B-1. 배경: 왜 가스터빈이 슈퍼사이클인가

SMR·원전의 현실적 공급 시점은 2030~2035년. 계통연계 큐 병목으로 재생에너지도 즉각 연결이 불가. AI 데이터센터는 지금 당장 전력이 필요하다. 이 구조적 갭이 가스터빈 슈퍼사이클의 본질이다.

- 전력망 계통연계 대기: ~11,600건, 2,600 GW 대기. 평균 5년 대기 (LBNL)
- BTM(자가발전) 가속: 대형 AI 시설 61~73%가 온사이트 전력 전략 채택 (Bloom Energy 2026)
- 2026년이 기록의 해: 계획된 BTM 가스발전 착공 용량 ~100 GW 초과 전망 (Global Energy Monitor)

---

## B-2. 3강 비교: GE Vernova vs Siemens Energy vs 두산에너빌리티

### B-2-1. GE Vernova — 글로벌 가스터빈 1위

| 항목 | 수치 | 비고 |
|------|------|------|
| 가스터빈 백로그 | **100 GW** (1Q26 말) | 83 GW (2025말) → 100 GW QoQ. YE26 **110 GW+** 목표 |
| 총 백로그 | **$163B** | 서비스 $81.18B 포함 |
| 1Q26 수주 | DC향 전동화 **$2.4B** | 전년 연간 규모 1분기 만에 초과 |
| 1Q26 가스터빈 출하 | **25기** (+32% YoY) | |
| 판가 추이 | 1H26 신규주문, 4Q25 대비 **+10~20%** $/kW | 연간 지속 상승 |
| Wood Mackenzie 전망 | 2027년 말 **~$600/kW** | 2019년 ~$200/kW 대비 **195% 상승** (3배) |
| 생산 CAPA 확장 | ~10 GW(현재) → **20 GW** (3Q26) → **24 GW** (2028 목표) | $160M+ 투자, 연 50기 → 70~80기 |
| 백로그 소화 기간 | **~10년** | 2027년 이후 슬롯 밀림 |
| 서비스 매출(LTM) | **$16.85B** (~45% 비중) | LTSA 기반, 7,000기+ 설치베이스 |
| 서비스 백로그 | **$81.18B** | 10~25년 LTSA, 연간 매출의 2배+ |
| 1Q26 순이익 | **$4.7B** | |
| FY26→FY30 매출 전망 | ~$44B → ~$70B | |

**출처**: [Utility Dive — 백로그 100GW](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/), [Wood Mackenzie 가격](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/), [Koalagains — LTSA](https://koalagains.com/stocks/NYSE/GEV/business-and-moat)

---

### B-2-2. Siemens Energy — 글로벌 가스터빈 2위

| 항목 | 수치 | 비고 |
|------|------|------|
| 총 백로그 | **€146B** ($174B) — 사상 최대 | |
| 가스터빈 백로그 | **60 GW 확정** + 27 GW 예약 | 총 87 GW 파이프라인 |
| FY26 Q1 수주 | **€17.6B** (+34% YoY) — Gas Services 부문 사상 최대 | |
| DC 비중 | 신규 가스터빈 주문의 **60%가 DC 관련** | 미국 수요 주도 |
| 납기 대기 | 주문→납품 **4년 대기**. 납품일 2029~2030년 | |
| 판매 대수 | 100기 (FY24) → **194기 (FY25)** — 전년비 ~2배 | |
| Q1 순이익 | **€746M** (~3x YoY) | |
| FY26 가이던스 | 매출 +14~16%, OPM 12%, 순이익 **~€4B** | |
| 미국 투자 | **$1B+** — 노스캐롤라이나 터빈 제조 확장 + 미시시피 $300M 고압기기 공장 신설 | 2026.02 발표 |
| 지역 분포 | 미국 40%, EU 35%, 중동·중국 15% | |

**출처**: [Enlit](https://www.enlit.world/library/siemens-energy-boasts-record-gas-turbine-orders-in-response-to-demand-boom), [Yahoo Finance — €146B 백로그](https://finance.yahoo.com/news/siemens-energy-reaches-record-136bn-163000307.html), [AD-HOC-NEWS](https://www.ad-hoc-news.de/boerse/news/ueberblick/siemens-energy-s-60-gw-gas-turbine-backlog-prompts-a-political-warning/69531957)

---

### B-2-3. 두산에너빌리티 — 한국 유일 대형 가스터빈 제조사

| 항목 | 수치 | 비고 |
|------|------|------|
| 터빈 사양 | **380 MWe급** H-class 가스터빈 (DGT-6 기반) | |
| xAI 수주 | 총 **7기** (초기 2기+3기+2기) = 합산 **2.66 GW** | 약 ₩1.2T. 회사 역대 최대 단일 수주 |
| xAI 납품 | 1·2호기 **2026년 말** 납품 예정 | AI GPU 60만기+ 클러스터 전력 공급 |
| 미국 총 수주 | **12기** | |
| 글로벌 누적 수주 | **23기** (2019년 이후) | |
| 장기 목표 | 2030년 45기, **2038년 105기** | |
| 인도 생산 | 2029.05부터 **월 1기** | |
| 1Q26 수주잔고 | **$16.2B** (+62% YoY) | |
| 2026 외국인 순매수 | 한국 증시 **1위** | |
| Rolls-Royce SMR | 핵섬 기자재(RPV 등) 파트너 선정 (2026.05) | |
| 신한울 3·4 | 주기기 ₩2.9조 계약 | |
| 체코 두코바니 | 스팀터빈 **₩320B** 수주 | |

**출처**: [TechTimes — xAI 7기](https://www.techtimes.com/articles/317469/20260531/doosan-enerbility-wins-rolls-royce-smr-work-q1-orders-jump-62-amid-data-center-push.htm), [Gas to Power Journal](https://gastopowerjournal.com/news/projectsandfinance/musks-xai-buys-five-more-380-mw-gas-turbines-from-doosan/), [TechTimes — xAI 5기 추가](https://www.techtimes.com/articles/313840/20260107/elon-musks-xai-secures-massive-power-infrastructure-five-380-mw-natural-gas-turbines.htm)

---

### B-2-4. 3강 비교 요약

| 지표 | GE Vernova | Siemens Energy | 두산에너빌리티 |
|------|-----------|---------------|-------------|
| 시장점유율(추정) | ~**50%** | ~**35%** | ~5~7% (국내+틈새) |
| 터빈 등급 | HA급 (최고효율) | H급/J급 | H급(380 MW) |
| 백로그 (GW) | **100 GW** | **60 GW** + 27예약 | N/A (기 단위) |
| 납기 대기 | ~10년 소화 기간 | 4년 대기 | 2026말 첫 납품 |
| DC 비중 | 1Q26 수주의 핵심 | 신규수주의 60% | xAI 등 빅테크 직접 수주 |
| 서비스 매출 비중 | ~45% ($16.85B) | 높은 비중 | 낮음(신규 제조사) |
| 생산 확장 | 50기→70~80기/년 | 194기/FY25 | 월 1기(2029 인도) |

---

## B-3. 판가 궤적

### B-3-1. Wood Mackenzie 핵심 데이터

| 시점 | 가스터빈 가격 ($/kW) | 변화율 |
|------|-------------------|------|
| 2019 (기준점) | ~$200/kW | — |
| 2024 | ~$350~400/kW | +75~100% |
| 2026 (현재) | $400~500/kW (추정) | GEV 1H26: QoQ +10~20% |
| 2027E (WoodMac 전망) | **~$600/kW** | 2019 대비 **+195%** (약 3배) |

**출처**: [Wood Mackenzie](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/), [Utility Dive](https://www.utilitydive.com/news/gas-turbine-supply-crunch-set-to-raise-prices-195-by-2027-woodmac/816904/)

### B-3-2. 가격 상승 드라이버

1. **공급-수요 불균형**: 글로벌 주문잔고 110 GW vs. 제조능력 60~70 GW → 구조적 과잉수요
2. **리드타임 장기화**: 대형 터빈 5~6년, 소형 18~36개월. 2026년 주문 → 2031~2032년 납품
3. **핫섹션 병목**: 단결정 블레이드(single-crystal turbine blade) 제조는 글로벌 소수 공급사만 가능
4. **원자재·인건비**: 니켈합금·코발트 등 초내열합금 가격 상승, 숙련 용접사 부족
5. **관세·물류**: 미국 관세 정책으로 부품 비용 추가 상승
6. **CCGT 프로젝트 비중**: 가스터빈이 CCGT 총 프로젝트 비용의 **20~30%** → 터빈 가격이 프로젝트 경제성 직결

---

## B-4. 온사이트 발전(BTM) 트렌드

### B-4-1. Williams Companies — BTM 포트폴리오 업데이트

Williams는 미국 최대 가스 파이프라인 운영사 중 하나로, 파이프라인 인프라를 활용해 데이터센터에 직접 턴키 온사이트 발전소를 공급하는 "Power Innovation" 사업으로 전환 중.

| 항목 | 수치 | 비고 |
|------|------|------|
| 총 포트폴리오 규모 | **$9.6B** BTM 투자 (업데이트된 수치) | 당초 $5.1B에서 대폭 확장 |
| 완공 프로젝트 수 | **6개** 명명 프로젝트: Socrates, Apollo, Aquila, Socrates the Younger, Neo, Atlas | |
| 운전 개시 | 2026년 말 ~ 2028년 | |
| 총 합산 ISO 용량 | **2,500 MW+** | |
| 계약 기간 | 10~12.5년 장기 | |
| Project Socrates | $1.6B, **400 MW**, New Albany OH (Meta 계열 DC 추정). 2026 2H 완공 예정 | |
| Project Neo | **$2.3B, 682 MW**. 2026.05 고객계약 체결 | |
| 1Q26 매출 | 사상 최고 실적 | Socrates 가동 기여 |

**출처**: [Williams Power Innovation](https://www.williams.com/power-innovation/), [Power Engineering](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-demand-accelerates/), [Williams 1Q26 실적](https://www.williams.com/2026/05/04/williams-announces-record-first-quarter-2026-results/)

### B-4-2. BTM 구조적 가속 요인

| 요인 | 설명 |
|------|------|
| 계통연계 큐 | 미국 평균 5년 대기. 북부VA·피닉스·댈러스는 4~7년 → BTM이 유일한 빠른 해법 |
| 100 GW 계획 | 2026년 계획된 미국 가스발전 착공 용량 100 GW 이상 — 역사적 기록 (2002년 100 GW) 초과 전망 |
| 개발사 탐색 비율 | 56%가 BTM 옵션 탐색 (2026 Foley Survey) |
| 온사이트 전략 | 61~73% 데이터센터 운영사가 온사이트 전력 전략 채택 (Bloom Energy 2026) |

**출처**: [EnkiAI](https://enkiai.com/data-center/gas-to-power-boom-ai-drives-2026-on-site-energy-shift/), Bloom Energy Mid-Year 2026 Report

---

## B-5. 서비스 매출 락인 (LTSA 구조)

### B-5-1. GE Vernova LTSA 비즈니스

| 항목 | 수치 |
|------|------|
| 서비스 매출(LTM) | **$16.85B** (~45% 비중) |
| 서비스 백로그 | **$81.18B** (연간 매출의 2배+) |
| LTSA 기간 | **10~25년** 장기 계약 |
| 설치 베이스 | 7,000기+ 가스터빈 |
| 서비스 마진 | 장비 대비 구조적으로 높음 (독점 부품·데이터·운영 락인) |
| 전환 비용 | 독점 부품, 운영 데이터, 기술 인증으로 사실상 전환 불가 |

### B-5-2. 서비스 vs 장비 마진 구조

- **장비 마진**: 원자재·인건비·경쟁에 민감. 그러나 현재 판가 상승으로 장비 마진도 확대 중
- **서비스 마진**: 계약 체결 후 장기 고정. 스케일·독점 부품으로 구조적 우위. CEO Scott Strazik: "서비스 계약은 더 높은 마진으로 진입 중"
- **복합 효과**: 현재 고가에 팔리는 장비 → 10~25년 후 고마진 서비스 계약으로 전환. 슈퍼사이클 장비 판매가 미래 서비스 수익의 씨앗

**출처**: [GE Vernova LTSA](https://www.gevernova.com/gas-power/services/service-agreements), [Motley Fool](https://www.fool.com/investing/2026/05/07/heres-why-ge-vernova-stock-keeps-soaring-in-2026/), [Koalagains](https://koalagains.com/stocks/NYSE/GEV/business-and-moat)

---

## B-6. 시장 규모 전망

| 출처 | 기준연도 | 목표연도 | 규모 | CAGR |
|------|---------|---------|------|------|
| Fortune Business Insights | $24.70B (2026) | $43.50B (2034) | — | **7.33%** |
| Global Market Insights | $25.4B (2026) | $64.8B (2035) | — | **11.2%** |
| Intel Market Research (CCGT) | $30.8B (2026) | $45.2B (2034) | — | 5.7% |
| BusinessWebWire | — | $61.13B (2035) | — | — |
| Fact.MR | — | 2036년까지 지속 성장 | — | — |

- **컨센서스 범위**: $24~31B (2026) → $43~65B (2034~35), CAGR 7~11%
- **CCGT가 최대 세그먼트**: 가스+스팀 복합사이클. 효율 60%+ (단순사이클 40% vs CCGT 60%)
- **AI DC 드라이버**: 기존 전망 대비 상향 조정 지속. AI 전력 수요가 구조적 초과 수요 형성
- **지역 분포**: 미국 40%+, 중동 15~20%, 아시아(인도 중심) 성장 가속

**출처**: [Fortune BI](https://www.fortunebusinessinsights.com/gas-turbine-market-106255), [GM Insights](https://www.gminsights.com/industry-analysis/gas-turbine-market), [Intel MR](https://www.intelmarketresearch.com/combined-cycle-gas-turbine-market-39035)

---

## B-7. 리스크 분석

### R-1. LNG 가격 변동성

| 항목 | 내용 |
|------|------|
| 2026 전망 | 북미 LNG 수출 증가로 공급 +3,000만톤. Henry Hub ~$4/MMBtu (적정 수준) |
| 하락 시나리오 | LNG 공급 과잉 → 가스 발전 경제성 개선 → 가스터빈 수요 추가 증가 (역설적) |
| 급등 시나리오 | 지정학적 충격(중동·러시아) → LNG 급등 → DC 운영비 증가. 일부 프로젝트 경제성 악화 |
| 완충 요인 | 미국 BTM 프로젝트는 대부분 파이프라인 가스 직접 연결. LNG 가격보다 Henry Hub 연동 |

**출처**: [ADI Analytics](https://adi-analytics.com/2026/01/13/2026-adi-global-natural-gas-lng-outlook/), [Energy Tracker Asia](https://energytracker.asia/lng-prices-in-2026/)

### R-2. 탄소규제 강화 — 좌초자산 리스크

| 항목 | 내용 |
|------|------|
| 현황 | 미국: IRA 세액공제 지속 불확실. EU: 탄소 국경 조정 메커니즘(CBAM) 확대 |
| 중장기 리스크 | 2035~2040년 강한 탈탄소 규제 시 10~15년 내 건설된 가스 설비가 좌초자산화 |
| 완충 요인 1 | **수소 혼소(H2 co-firing)** 준비 설계. GEV HA터빈 100% 수소 연소 가능 (개발 중) |
| 완충 요인 2 | **CCS(탄소포집저장)** 연계 가능성. 미국 45Q 세액공제로 CCS 경제성 개선 |
| 완충 요인 3 | LTSA 계약 기간 내 탄소 중립 전환 비용을 계약에 반영하는 구조 증가 |
| 현실적 판단 | 2030년대 초까지는 규제보다 수요가 압도적. 2035년 이후 점진적 리스크 증가 |

### R-3. 재생에너지·배터리 가격 하락

| 항목 | 내용 |
|------|------|
| 현황 | 태양광 LCOE 지속 하락. ESS 배터리 가격 -15~20%/년 |
| 리스크 | 2030년 이후 배터리+재생에너지로 24시간 전력 공급이 경제적이 되면 가스 수요 대체 |
| 단기 현실 | 현재 기술로 AI 클러스터급(100~500 MW) 24/7 전력을 배터리로 공급하는 것은 경제적 불가. 최소 2030년대 중반까지 가스 의존 불가피 |

### R-4. 공급 과잉 전환 (Supply Normalization)

| 항목 | 내용 |
|------|------|
| 리스크 | GEV 24 GW, Siemens 증설, 중국 제조사(MHI·MHPS 라이선스) 등이 동시에 CAPA 증가 시 2029~2030년 공급 정상화 |
| 시그널 | 현재 리드타임 5~6년 → 3~4년으로 단축되면 판가 압박 신호 |
| 완충 요인 | 수요도 동시에 급증(AI 클러스터 가속). 공급 증가를 수요가 흡수할 가능성 높음 |

---

## B-8. 투자 시사점 (테마 B)

### 단기 최선호: GE Vernova (GEV)

- **근거**: 백로그 100 GW, LTSA $81B, 판가 +10~20% QoQ, 생산 확대 2026.3Q 20 GW
- **EPS 레버리지**: 판가 상승 × 출하 증가 × 서비스 마진 확대 = 삼중 EPS 복리
- **리스크**: 높은 밸류에이션(PER 60x+). 백로그 소화 지연 시 하방
- **FY26→FY30 매출**: ~$44B → ~$70B 로드맵 존재

### 중기 강세: 두산에너빌리티 (034020.KS)

- **근거**: 가스터빈 (xAI 7기 + 미국 12기 + 글로벌 23기) + 원전(신한울·두코바니·Rolls-Royce SMR) 이중 포지션
- **2038년 105기 목표**: 글로벌 가스터빈 슈퍼사이클의 직접 수혜. 한국 유일 H급 터빈 제조사
- **외국인 2026년 순매수 1위**: 글로벌 자금의 한국 원전·가스터빈 프록시
- **리스크**: 납기 집중(2026~2027년 xAI 7기 집중 납품), 환율 노출

### 고수익·고위험: Williams Companies (WMB)

- **근거**: BTM 포트폴리오 $9.6B, 6개 프로젝트 2,500 MW+. 파이프라인→전력으로 전환 중
- **수익 구조**: 10~12.5년 장기계약 = 안정적 현금흐름. 에너지 인프라 + DC 노출 복합
- **리스크**: 고객 집중, 규제, BTM 사업 규모 불확실성

---

## B-9. 모니터링 지표 (테마 B)

| 지표 | 모니터링 포인트 | 빈도 |
|------|--------------|------|
| GEV 가스터빈 백로그 | 분기 백로그 GW, 판가 $/kW 추이, 출하 기수 | 분기 |
| Siemens Energy 수주 | 분기 가스터빈 기가와트 수주, DC 비중 % | 분기 |
| 두산에너빌리티 수주 | 글로벌 가스터빈 누적 수주 기수, 신규 미국 빅테크 계약 | 분기 |
| 가스터빈 리드타임 | WoodMac 분기 조사: 리드타임 단축 여부 (5~6년 → 단축 시 경고) | 분기 |
| BTM 프로젝트 착공 | Williams Neo·Apollo 등 착공·완공 일정 준수 여부 | 분기 |
| 글로벌 가스발전 착공 | Global Energy Monitor: 연간 착공 GW (100 GW 돌파 확인) | 연간 |
| Henry Hub/LNG 가격 | $3/MMBtu 이하 → 수요 과잉 확인, $7+ → 경제성 우려 | 월간 |
| SMR 착공 진척 | TerraPower·Kairos 완공 일정 → 가스 브릿지 기간 산정 | 반기 |
| 하이퍼스케일러 CAPEX | MSFT·META·GOOGL·AMZN 분기 자본지출 가이던스 | 분기 |
| 미국 가스발전 허가 | FERC·주정부 발전소 건설허가 건수 및 용량 | 분기 |

---

---

## 종합 시사점: 테마 A와 B의 관계

```
[현재 2026~2027]          [중기 2028~2032]          [장기 2033~2040]
──────────────────────── → ────────────────────────── → ──────────────────
TMI 재가동(835 MW)          TerraPower 완공(345 MW)      NuScale Romania(462 MW)
가스터빈 슈퍼사이클 절정       Kairos Power 첫 납품(50 MW)  EPR2 Penly(2x1,650 MW)
BTM 100 GW 착공             SMR 수십 기 건설 중          SMR 본격 상업화
가스터빈 백로그 소화 기간      두코바니 완공(2x1,055 MW)    가스 비중 점진 감소
판가 $600/kW 도달            가스 브릿지 역할 유지         탄소중립 전환 가속
```

**핵심 명제**:
1. **원전·SMR이 늦어질수록 가스터빈 수요는 연장된다** — 두 테마는 경쟁 관계가 아닌 시간축 보완재
2. **두산에너빌리티는 두 테마의 교차점** — 가스터빈(슈퍼사이클 수혜) + 원전기자재(르네상스 수혜)
3. **하이퍼스케일러의 "원전 커밋먼트" 절반은 실질적 장기 의향서** — 실제 FID 기반 투자는 소수. 단기 주가 모멘텀과 실제 펀더멘털 괴리 주의
4. **가스터빈은 에너지 전환의 적이 아니라 가교** — 에너지 전환 기간의 필수 인프라. 규제 리스크보다 수요 드라이버가 압도적으로 강함 (2030년대 초까지)

---

## 출처 종합

### 기업·프로젝트
- [TerraPower 착공](https://www.terrapower.com/TerraPower-Commences-Construction-on-Americas-First-Utility-Scale-Advanced-Nuclear-Power-Plant)
- [DOE — NRC TerraPower 허가](https://www.energy.gov/ne/articles/nrc-issues-construction-permit-terrapowers-natrium-advanced-reactor)
- [X-energy IPO 공시](https://x-energy.com/news/x-energy-announces-pricing-of-upsized-initial-public-offering/)
- [Kairos Power Hermes 2 착공](https://www.kairospower.com/updates/kairos-power-breaks-ground-on-hermes-2-demonstration-plant)
- [NuScale Romania FID — Power Magazine](https://www.powermag.com/romanias-coal-to-nuscale-smr-conversion-secures-fid-moves-into-implementation-with-caveats/)
- [Rolls-Royce SMR + 두산 — Korea Herald](https://www.koreaherald.com/article/10757884)
- [두산 xAI 7기 — Gas to Power Journal](https://gastopowerjournal.com/news/projectsandfinance/musks-xai-buys-five-more-380-mw-gas-turbines-from-doosan/)
- [Williams Power Innovation](https://www.williams.com/power-innovation/)
- [U.S. Commerce Dept — 일-미 전략투자](https://www.commerce.gov/news/press-releases/2026/03/joint-announcement-japan-us-strategic-investment)
- [AAF — 일-미 원자력 투자](https://www.americanactionforum.org/insight/u-s-japan-trade-deal-investment-commitments-in-nuclear-energy/)
- [Japan Times — 일-미 무역협정](https://www.japantimes.co.jp/business/2026/03/20/us-japan-trade-pact/)
- [Hitachi — BWRX-300 부품 공급](https://www.hitachi.com/New/cnews/month/2025/05/250509.html)
- [CNBC — 도시바-웨스팅하우스 파산](https://www.cnbc.com/2017/03/29/huge-nuclear-cost-overruns-push-toshibas-westinghouse-into-bankruptcy.html)
- [CSIS — 웨스팅하우스 파산 분석](https://www.csis.org/analysis/westinghouses-bankruptcy-and-its-implications)
- [World Nuclear Association — 일본 원전](https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-power)

### 시장 분석
- [Wood Mackenzie — 가스터빈 가격 +195%](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis/)
- [GE Vernova 백로그 100 GW — Utility Dive](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-hits-100-gw-as-prices-rise/818332/)
- [Siemens Energy 백로그 €146B — Yahoo Finance](https://finance.yahoo.com/news/siemens-energy-reaches-record-136bn-163000307.html)
- [Fortune Business Insights — 가스터빈 시장](https://www.fortunebusinessinsights.com/gas-turbine-market-106255)
- [Global Market Insights — 가스터빈 시장](https://www.gminsights.com/industry-analysis/gas-turbine-market)
- [Carnegie Endowment — 하이퍼스케일러 원전 평가](https://carnegieendowment.org/research/2026/06/beyond-the-hype-assessing-hyperscaler-nuclear-commitments-against-us-energy-realities)
- [SMR Intel — 원전 DC 딜 트래커](https://smrintel.com/nuclear-data-center-deals/)

### 규제·정책
- [NRC Part 53 — Federal Register](https://www.federalregister.gov/documents/2026/03/30/2026-06048/risk-informed-technology-inclusive-regulatory-framework-for-advanced-reactors)
- [Korea SMR Act — NEI Magazine](https://www.neimagazine.com/news/south-korea-smr-act-passed/)
- [Czech Dukovany EPC — Czech MPO](https://mpo.gov.cz/en/guidepost/for-the-media/press-releases/epc-contract-for-completion-of-dukovany-has-been-signed--minister-of-industry-and-trade--lukas-vlcek-will-visit-korea-again-in-july--287912/)
- [EDF EPR2 비용 — World Nuclear News](https://www.world-nuclear-news.org/articles/edf-estimates-epr2-programme-costs-at-eur728-billion)

### 기존 참조
- `data/research_ai_power_part12_overview.md` — Part 1-2 기본 데이터 (밸류체인·수요 전망·기업 실적)
- `data/note-ai-money-flow_20260618.md` — 투자 프레임워크 메모
