# HBM·패키징 리서치 — 4대 테마 심화: 기술·전환·사이클·소재

> 목적: HBM/패키징 밸류체인의 4대 핵심 테마(첨단 패키징 기술 전쟁, 하이브리드 본딩 전환, 메모리 사이클과 CXMT, 기판과 소재) 심화 분석
> 작성일: 2026-06-22
> 최종 갱신: 2026-06-22
> 커버리지: research_hbm_pkg_themes (Part 1-2 시리즈 테마 Deep Dive)
> 상태: 초안

---

## 1. 개요 — 4대 테마 소개

본 문서는 `research_hbm_pkg_part12_overview.md`에서 도출한 4대 투자 테마를 심화 분석한다.

| 테마 | 핵심 질문 | 시간축 |
|------|----------|--------|
| **A. 첨단 패키징 기술 전쟁** | CoWoS vs EMIB vs I-Cube — 누가 AI 패키징의 표준이 되는가? | 2024→2029 |
| **B. 하이브리드 본딩 전환** | TCB에서 하이브리드 본딩으로의 전환이 언제, 어떤 세대에서 일어나는가? | 2025→2028+ |
| **C. 메모리 사이클과 CXMT** | 이 사이클은 과거와 구조적으로 다른가? CXMT 진입은 언제 현실화되는가? | 2018~2028 |
| **D. 기판과 소재** | ABF 독점과 글라스코어 전환 — 소재 병목은 얼마나 지속되는가? | 2025→2032 |

**테마 간 연결**: A(패키징 CAPA 부족) → B(본딩 전환으로 CAPA 효율 변화) → C(수요/가격 사이클이 CAPEX를 좌우) → D(기판/소재가 최종 병목). 이 4개 테마는 독립적이 아니라 순환적 인과 구조를 형성한다.

---

## 2. Theme A: CoWoS/InFO/SoIC — 첨단 패키징 기술 전쟁

### 2.1 TSMC 패키징 기술 비교: CoWoS-S vs CoWoS-L vs CoWoS-R

| 항목 | CoWoS-S (Standard) | CoWoS-L (Large) | CoWoS-R (Redistribution) |
|------|-------------------|-----------------|-------------------------|
| **구조** | 단일 실리콘 인터포저 위에 다이 배치 | LSI 기술로 복수 인터포저 세그먼트 접합 (3,000mm²+) | RDL 인터포저 + 유기 기판 기반 |
| **인터포저 크기** | 1~2 레티클 | 5.5 레티클 (2026) → 9.5 레티클 (2027) → 14 레티클 (2028) | 2~3 레티클 |
| **적용 칩** | NVIDIA H100, AMD MI300X | NVIDIA Blackwell (B200/GB200), Rubin (R100) | Broadcom, 통신/엣지 컴퓨팅 |
| **비용** | 중간 ($300~500/칩) | 고가 ($900~1,000/칩, Rubin급) | 저가 (유기 기판 기반) |
| **핵심 장점** | 검증된 양산성, 높은 수율 | 초대면적, 다수 HBM 스택 통합 | 비용 효율, 범용성 |
| **2026 비중** | 레거시 유지 (축소 추세) | 본격 양산 (Blackwell/Rubin) | 통신/ASIC 중심 유지 |

**출처**: [LoveChip](https://www.lovechip.com/blog/cowos-vs-copos-vs-cowop-tsmc-advanced-packaging-explained), [AMI Next](https://www.aminext.blog/en/post/tsmc-cowos-s-r-l-differences), [ChipStrat](https://www.chipstrat.com/p/advanced-packaging-intels-emib-vs)

- **CoWoS-L이 주류로 부상**: 2026년부터 NVIDIA Blackwell/Rubin 플랫폼이 CoWoS-L을 채택하면서, TSMC 첨단 패키징 매출의 주력이 CoWoS-S에서 CoWoS-L로 전환 중
- **비용 급등**: CoWoS-L 웨이퍼 ASP가 7nm 파운드리 웨이퍼에 근접 — 패키징이 단순 후공정이 아닌 "고부가 제조 공정"으로 격상 ([TrendForce](https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/))
- **수율 이슈**: 초기 CoWoS-L 수율 난항이 2026년 들어 대부분 해소, 그러나 정밀도 요구 수준이 파운드리급으로 상승

### 2.2 인텔 EMIB/Foveros — 경쟁 기술 비교

| 비교 항목 | TSMC CoWoS | Intel EMIB | Intel Foveros |
|----------|-----------|-----------|--------------|
| **유형** | 2.5D (실리콘 인터포저) | 2.5D (임베디드 실리콘 브릿지) | 3D (다이-투-다이 직접 본딩) |
| **비용** | $900~1,000 (Rubin급) | 수백 달러 (CoWoS 대비 크게 저가) | 고가 (3D 적층) |
| **웨이퍼 이용률** | ~60% (대형 인터포저) | ~90% (브릿지 다이 소형) | — |
| **레티클 스케일** | 5.5x (2026) → 14x (2028) | 6x→8x (2026) → 12x+ (2028) | 다이 크기 의존 |
| **시장 점유율** | 사실상 독점 (NVIDIA, AMD) | 급성장 중 (Amazon, Cisco, SpaceX, Tesla) | 니치 (Intel CPU Meteor Lake 등) |
| **2026 CAPA** | 110~130K WPM | 비공개 (수십억 달러 고객 커밋) | 소규모 |

**출처**: [ChipStrat](https://www.chipstrat.com/p/advanced-packaging-intels-emib-vs), [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year), [TrendForce](https://www.trendforce.com/news/2026/05/12/news-mediatek-reportedly-adopts-dual-packaging-strategy-with-intel-emib-tsmc-cowos-for-ai-asic-push/)

- **EMIB의 부상**: TSMC CoWoS CAPA 부족이 장기화되면서, **인텔 EMIB이 대안으로 급부상**. MediaTek이 CoWoS + EMIB 이중 전략을 채택한 것이 대표 사례
- **비용 우위**: EMIB는 CoWoS 대비 비용이 크게 낮고 웨이퍼 이용률이 90%로 높아, ASIC/커스텀칩 시장에서 가격 경쟁력 보유
- **한계**: NVIDIA/AMD와 같은 최고성능 AI 가속기는 여전히 CoWoS-L 선호 — 초대면적 인터포저 + HBM 다수 스택 통합에서 EMIB 대비 우위
- **Intel 18A 패키징 전략**: EMIB-T(Thick)를 2026년 팹 롤아웃하며, Intel 18A 파운드리 고객에게 패키징 번들 제공 추진

### 2.3 삼성 I-Cube4/FOPLP — 삼성의 첨단 패키징 로드맵

| 기술 | 설명 | 현황 (2026.06) |
|------|------|---------------|
| **I-Cube4** | 2.5D 실리콘 인터포저 기반, HBM 4개 스택 통합 | HBM3E/HBM4 적용, 자사 Exynos + 고객칩 |
| **FOPLP** | 팬아웃 패널 레벨 패키징, 플라스틱 기반 | 모바일 칩 경험 활용, 대면적 전환 추진 |
| **SAINT (3D)** | 삼성 독자 3D 적층 기술 | 개발 중, SoIC 대항 |

**출처**: [DIGITIMES](https://www.digitimes.com/news/a20241225PD212/samsung-tsmc-foplp-packaging-materials.html), [SemiconductorX](https://semiconductorx.com/packaging-matrix.html)

- **TSMC 대비 격차**: 삼성 I-Cube는 기술적으로 CoWoS와 유사하나, **CAPA·수율·고객 기반에서 현저한 격차**. NVIDIA·AMD가 TSMC CoWoS에 집중하면서 삼성은 자사 HBM 패키징과 2·3티어 고객 대응에 집중
- **FOPLP 차별화**: 삼성은 플라스틱 패널을 고수하는 반면, TSMC는 유리 패널(CoPoS)을 추진 — 소재 접근법의 차이가 수율·비용에 미치는 영향은 아직 미검증
- **파운드리 시너지**: 삼성 파운드리(GAA 2nm) + I-Cube 패키징 번들 전략으로 Intel과 유사한 '원스톱' 제공 시도

### 2.4 CoPoS (Chip-on-Panel-on-Substrate) — 차세대 패키징

| 항목 | 내용 |
|------|------|
| **정의** | 유리 패널 위에 칩을 배치하고 기판에 실장하는 패널 레벨 패키징 |
| **TSMC 파일럿** | 2026년 6월 파일럿 라인 완공 |
| **양산 목표** | 2028~2029년 |
| **핵심 장점** | CoWoS 대비 대면적 확장 용이, 비용 효율, 유리 패널의 치수 안정성 |
| **적용 전망** | 14 레티클 이상 초대면적 패키지, 차세대 GPU/ASIC |

**출처**: [TrendForce](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)

- CoPoS는 CoWoS의 CAPA·비용 한계를 극복하기 위한 TSMC의 중장기 해법
- 유리 패널은 실리콘 웨이퍼 대비 면적 효율이 높아 단위 비용 절감 가능
- **2028~2029 양산 시 패키징 CAPA 병목이 구조적으로 완화**될 가능성 — 투자 타이밍 주의

### 2.5 CoWoS 용량 전쟁 타임라인

| 시점 | CoWoS CAPA (WPM) | 주요 이벤트 | 수급 상황 | 출처 |
|------|------------------|-----------|----------|------|
| 2024 말 | 35K | Blackwell 양산 시작 | 심각한 부족 | TrendForce |
| 2025 말 | ~70~80K | CAPA 2배 확대, 외주 가속 | 20%+ 부족 | TrendForce |
| **2026 초** | ~110K | Rubin 양산 준비, NVIDIA 50%+ 예약 | **20% 부족** | TrendForce (2026.06) |
| **2026 말** | **120~130K** | 신규 라인 가동, Amkor/SPIL 외주 확대 | **10% 부족으로 축소** | TrendForce (2026.06) |
| 2027 | 170K | CoPoS 파일럿 → 양산 준비 | 균형 접근 | SemiWiki, 업계 |
| 2028~2029 | 200K+ (추정) | CoPoS 양산, 패널 레벨 전환 | 균형~소폭 과잉 가능 | 업계 추정 |

**출처**: [TrendForce](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/), [36Kr](https://eu.36kr.com/en/p/3580962946874242), [FinancialContent](https://markets.financialcontent.com/stocks/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026)

- **외주 비중 확대**: Amkor ~80K WPM, SPIL 6~8만장 — TSMC 자체 CAPA만으로는 수요를 감당할 수 없어 외주 비중이 구조적으로 증가
- **NVIDIA 독점 예약**: NVIDIA가 CoWoS CAPA의 **50%+** 예약 (SiliconAnalysts) → 나머지 고객(AMD, Broadcom, Google)은 EMIB 등 대안 모색 불가피
- **리드타임**: 52~78주로 여전히 길어, 2026년 발주 물량이 2027~2028년에야 납품 → 선행 지표로서 2025 발주 데이터가 핵심

### 2.6 Theme A 투자 시사점

1. **TSMC(CoWoS)**: 대안 부재 + 수급갭 지속 → 가장 강한 해자. 다만 2028~2029 CoPoS 양산 시 CAPA 병목 완화 가능성
2. **인텔(EMIB)**: CoWoS 대안으로 부상, 비용 우위. Intel 18A 파운드리 성공 여부가 EMIB 가치의 핵심 변수
3. **삼성(I-Cube)**: 자사 HBM 패키징에 특화, 글로벌 범용 시장에서의 경쟁력은 제한적
4. **OSAT(ASE/SPIL, Amkor)**: CoWoS 외주 확대의 직접 수혜. SPIL의 NT$2.8B 공장 인수가 신호

---

## 3. Theme B: 하이브리드 본딩 — TCB에서 하이브리드 본딩으로의 전환

### 3.1 TCB→하이브리드 본딩 전환 타임라인

| 시점 | 본딩 기술 | HBM 세대 | 비중 | 출처 |
|------|----------|---------|------|------|
| 2024~2025 | **TCB 주류** (솔더 범프) | HBM3/HBM3E | 솔더 범프 58.9% | TrendForce |
| 2026 | TCB 주류, 하이브리드 본딩 도입 시작 | HBM4 (12-Hi) | TCB 80%+, HB 파일럿 | BESI IR |
| **2027** | TCB + 하이브리드 본딩 혼재 | HBM4E (12-Hi→16-Hi) | HB 비중 증가 시작 | TrendForce |
| **2028** | 하이브리드 본딩 본격화 | HBM4E/HBM5 (16-Hi→20-Hi) | **HB ~36~50%** | TrendForce, 업계 |
| 2029+ | 하이브리드 본딩 주류 | HBM5 (20-Hi+) | HB 50%+ | Semi Engineering |

**출처**: [TrendForce](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/), [Semi Engineering](https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/)

- **HBM4는 마이크로범프 유지**: JEDEC 두께 규격 완화 검토로 인해 HBM4에서는 TCB(마이크로범프)가 계속 사용될 가능성이 높아짐 — 하이브리드 본딩 본격 채택은 **HBM4E(2027~2028)부터**
- **20-Hi 이상 스택이 전환점**: 16-Hi까지는 TCB로 대응 가능하나, 20-Hi 이상에서는 피치 한계로 하이브리드 본딩이 사실상 필수

### 3.2 기술 비교: TCB vs 하이브리드 본딩

| 비교 항목 | TCB (열압착 본딩) | 하이브리드 본딩 |
|----------|-----------------|---------------|
| **접합 방식** | 솔더 범프(Cu 필러 + Sn) | Cu-Cu 직접 접합 (범프리스) |
| **피치** | 28~30μm (HBM3E) → 20~25μm (HBM4) | 15μm → <10μm (HBM4E → HBM5) |
| **정밀도** | ±1~2μm | **<10nm** (BESI 기준) |
| **장점** | 검증된 양산성, 낮은 비용, 높은 처리량 | 미세 피치, 고밀도 인터커넥트, 전기적 성능 |
| **단점** | 피치 한계 (~15μm 벽), 열적 스트레스 | 높은 비용, 낮은 처리량(UPH), 표면 평탄도 요구 |
| **비용** | 기준 (1x) | ~3~5x (장비+공정 비용) |
| **적용 세대** | HBM3 ~ HBM4E (16-Hi) | HBM4E (일부) ~ HBM5+ |

### 3.3 피치 로드맵

| HBM 세대 | 범프 피치 | 본딩 방식 | 시점 |
|----------|----------|----------|------|
| HBM3 | 35~40μm | TCB | 2024 양산 |
| HBM3E | 28~30μm | TCB | 2024 H2~ 양산 |
| HBM4 | 20~25μm | TCB (주류) | 2026.02 양산 |
| **HBM4E** | **15μm 이하** | **TCB + HB 혼재** | 2027~2028 |
| **HBM5** | **<10μm** | **하이브리드 본딩 주류** | 2028~2029 |

- **15μm 피치가 전환 임계점**: 솔더 범프 기반 TCB의 물리적 한계가 ~15μm이며, 이 피치에서 브릿징(단락) 리스크가 급증 → 하이브리드 본딩 전환의 기술적 필연성

### 3.4 주요 업체 경쟁

| 업체 | 기술 | 시장 포지션 | 핵심 데이터 | 출처 |
|------|------|-----------|------------|------|
| **한미반도체** | TC본더 | 글로벌 M/S **71.2%** (2025) | 2026E 매출 ₩1.08T (+64%), SK하이닉스 M/S 50→60%, 인천 하이브리드 본더 공장 ₩1,000억 투자 (2026 H2 가동) | EBN뉴스, 소뮤어 |
| **BESI** | 하이브리드 본더 | 하이브리드 본딩 **선두** | Q1'26 매출 €184.9M (+28%), 수주 €269.7M (2x YoY), 하이브리드 본딩 매출 €476M (2026E, 전체의 1/3), 정밀도 <10nm | BESI IR, TipRanks |
| **Applied Materials** | Kinex 하이브리드 본딩 시스템 | **도전자** | BESI 인수 입찰 참여, 패널 레벨 패키징 증착 장비 확장 | SEC 8-K |
| **Lam Research** | TSV 식각 + 하이브리드 본딩 전처리 | **도전자** | BESI 인수 입찰 참여, 20년+ 첨단 패키징 경력 | Tiger Brokers |
| **ASMPT** | TCB + 하이브리드 본더 | **추격자** | HBM 본딩 수요 증가 수혜 | TrendForce |

**출처**: [TrendForce](https://www.trendforce.com/news/2026/03/13/news-hybrid-bonding-leader-besi-reportedly-draws-takeover-interest-lam-applied-materials-rumored/), [EBN뉴스](https://www.ebn.co.kr/news/articleView.html?idxno=1700474)

### 3.5 하이브리드 본더 시장 규모 전망

| 시점 | 하이브리드 본더 시장 | 비고 | 출처 |
|------|-------------------|------|------|
| 2025 | ~$0.5B | BESI 중심 초기 시장 | TrendForce |
| 2026E | ~$0.8~1.0B | BESI €476M + 경쟁사 | TipRanks |
| **2028E** | **~$2.0B (₩2.8T)** | HBM 생산의 50%에 적용 시 | TrendForce (2025.10) |

### 3.6 HBM4E/HBM5 적용 전망 — 하이브리드 본딩 의무화 시점

- **HBM4 (2026)**: 마이크로범프 유지 확정적. JEDEC 두께 규격 완화 검토로 TCB 수명 연장
- **HBM4E (2027~2028)**: 하이브리드 본딩이 **16-Hi 이상 고스택 제품의 일부**에 적용 시작. 그러나 한미반도체는 HBM4E 16-Hi까지 TC본더로 대응 가능하다고 주장
- **HBM5 (2028~2029)**: 20-Hi 스택, <10μm 피치 → 하이브리드 본딩이 사실상 **의무화**되는 세대
- **결론**: "의무화" 시점은 **HBM5(2028~2029)**이나, **HBM4E(2027~2028)부터 혼재** 구간 진입

### 3.7 Theme B 투자 시사점

| 업체 | 시나리오 | 판단 |
|------|---------|------|
| **한미반도체** | TCB 해자가 HBM4E 16-Hi까지 유효 (2027~2028). Wide TC Bonder(HBM5/6용) 2026 H2 출시로 차세대 대응. 인천 하이브리드 본더 공장 투자로 전환 대비 | **2027년까지 강세, 2028년부터 전환 리스크** — 하이브리드 본딩 내재화 성공 여부가 중장기 해자의 핵심 |
| **BESI** | 하이브리드 본딩 시장의 구조적 수혜자. 2028년 시장 $2B 도달 시 최대 수혜. 다만 Applied Materials·Lam Research의 인수 경합(수십억 유로)이 불확실성 | **중장기 강세** — 하이브리드 본딩 채택 지연 리스크 있으나, 방향성은 확정적 |
| **Applied Materials** | Kinex 시스템 + BESI 인수 시 하이브리드 본딩 시장 지배 가능. 패키징 장비 포트폴리오 완성 | **인수 성공 시 게임 체인저** |

---

## 4. Theme C: 메모리 사이클과 CXMT

### 4.1 DRAM 사이클 역사 — 2018 피크 vs 현재 사이클 비교

| 비교 항목 | 2017~2019 사이클 | 2024~2026 현재 사이클 |
|----------|----------------|-------------------|
| **피크 시점** | 2018 H2 | 2026 (진행 중) |
| **주요 수요 동인** | 서버 업그레이드, 클라우드 확장 | **AI 훈련·추론** (HBM), 데이터센터 |
| **피크 후 하락** | 2019년 ASP **-47%** | ? (아직 미도래) |
| **하락 촉발 요인** | 과잉 공급 + 스마트폰 수요 둔화 | 잠재: 공급 확대 + AI CAPEX 둔화 |
| **제품 구조** | 범용 DRAM 중심 (DDR4) | **HBM 특화** (DRAM 내 비중 20%→50%) |
| **가격 결정 방식** | 스팟 시장 주도 | **장기 계약(LTA) 주도** |
| **공급 유연성** | 빠른 전환 가능 | HBM 전환에 3~4x 웨이퍼 소요, 전환 느림 |

**출처**: [Uncover Alpha](https://www.uncoveralpha.com/p/every-memory-cycle-ends-the-same), [Luminix](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators), [Silicon Analysts](https://siliconanalysts.com/market-data)

### 4.2 HBM ASP 추이

| 시점 | HBM3 ($/GB) | HBM3E ($/GB) | HBM4 ($/GB) | 출처 |
|------|------------|-------------|-------------|------|
| 2024 H2 | — | $17~20 (피크) | — | Silicon Analysts |
| 2025 H1 | $8~10 ($200/24GB) | $15~17 | — | Silicon Analysts |
| 2025 H2 | $8~10 | $13~17 | — | Silicon Analysts |
| 2026 계약가 | — | **+20% 인상 합의** | HBM3E 대비 **+30%+ 프리미엄** | TrendForce (2025.12) |
| 2026 스팟 | 하락 압력 | 하락 압력 | 계약 중심 (스팟 제한) | 업계 |

**출처**: [TrendForce](https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/), [Silicon Analysts](https://siliconanalysts.com/market-data/hbm-pricing)

- **계약가 vs 스팟가 괴리**: 2026년 HBM3E 계약가는 +20% 인상이 합의되었으나, 스팟 시장에서는 삼성의 30% 할인 공세로 실질 가격 하락 압력 존재. 이 괴리는 시장이 "계약 기반 안정 구간"과 "스팟 기반 변동 구간"으로 이원화되었음을 시사
- **HBM4 프리미엄**: 제조 복잡성(TSV·본딩·테스트 난이도 증가)으로 HBM3E 대비 30%+ ASP 프리미엄 → 믹스 개선으로 전체 매출 성장 견인

### 4.3 범용 DRAM 가격 동향 (2025~2026)

| 지표 | 수치 | 출처 |
|------|------|------|
| DDR5 스팟 가격 변동 (2025 H2) | 분기별 +30~50% | TrendForce |
| DRAM 계약가 인상 (2026 Q2) | **+58~63%** (일부 세그먼트 2배) | Luminix |
| DRAM 스팟 가격 (2025 Q4 vs 전년) | **~3배** 상승 | Avnet |

**출처**: [TrendForce](https://www.trendforce.com/price/dram/dram_spot), [Avnet](https://www.avnet.com/integrated/resources/article/2026-memory-shortage-ai-supercycle/)

- **HBM 생산 확대 → 범용 DRAM 공급 감소**: HBM 1GB 생산에 범용 DRAM 대비 ~4배 웨이퍼 면적 소요 (Micron 기준 3:1 변환비). HBM 램프가 범용 DRAM 공급을 구조적으로 압축
- **SemiAnalysis**: "40년 만의 한 번 있을 메모리 부족"으로 표현 — AI 수요 + HBM 전환 + 공급 비탄력성의 삼중 구조

### 4.4 공급/수요 밸런스 전환 시점

| 시나리오 | 전환 시점 | 전제 조건 |
|---------|----------|----------|
| **기본(Base)** | 2027 H2~2028 H1 | 삼성 CAPA +47%, SK하이닉스 M15X, Micron 확대 정상 진행 |
| **강세(Bull)** | 2028 H2+ | AI 모델 스케일링 지속, 추론 워크로드 폭증, 공급 확대 지연 |
| **약세(Bear)** | 2027 H1 | AI CAPEX 둔화, 모델 경량화 가속, 삼성 할인 확대 |

- **구조적 차이**: 과거 사이클은 스팟 시장 의존도가 높아 가격 변동성이 컸으나, 현재는 **다년 장기 계약(LTA)**이 일반화. SK하이닉스는 2027년까지 공급 계약 완료, Micron은 2026년 HBM 전량 고정가 매진 → **스팟 시장의 영향력 구조적 축소**
- **판단**: 공급 > 수요 전환은 2027 H2~2028 H1이 기본 시나리오이나, LTA 구조로 인해 **ASP 급락(-47% 급)은 발생하기 어려움** — 2018~2019년 사이클과의 핵심적 차이

### 4.5 CXMT 진입 타임라인과 영향

#### CXMT 현황 (2026.06)

| 항목 | 내용 | 출처 |
|------|------|------|
| **HBM3 양산 목표** | 2026년 말 → **일정 밀림, 2026 양산 불확실** | DIGITIMES |
| **현실적 양산 시점** | HBM3: 2027~2028, HBM3E: 2028+ | 업계 종합 |
| **12-Hi HBM 목표** | 2027년 | DIGITIMES |
| **HBM 전용 CAPA** | 월 **6만장** (총 CAPA의 20%) 전환 계획 | Tom's Hardware |
| **IPO 규모** | **$4.2B** (추진 중) | FinancialContent |
| **핵심 난제** | TSV 스태킹 수율, 본딩 워피지, 열관리, 패키지 수율 학습 곡선 | 업계 |

**출처**: [DIGITIMES](https://www.digitimes.com/news/a20260421PD230/cxmt-hbm3-dram-production-2026.html), [Tom's Hardware](https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly), [DIGITIMES](https://www.digitimes.com/news/a20260409PD229/cxmt-hbm-production-2027-market.html)

#### CXMT 가격 파괴 시나리오

| 시나리오 | 시점 | 영향 |
|---------|------|------|
| **시나리오 1: DDR4 반복** | 2028+ | CXMT가 HBM3를 반값에 출시 → 저사양 AI 가속기 시장(Huawei, Biren) 잠식. 한국 업체 HBM3/3E 마진 압박 |
| **시나리오 2: 제한적 성공** | 2027~2028 | 수율 50% 이하로 경쟁력 없는 가격. 중국 내수 시장만 타겟 |
| **시나리오 3: 규제 강화** | 불확정 | 미국 수출 규제 확대로 장비 조달 차질 → 일정 추가 지연 |

- **현실적 평가**: CXMT의 HBM3 양산은 2026년 내 불가능에 가까움. TSV 스태킹에서 단 하나의 다이 불량이 전체 스택을 폐기시키는 구조적 수율 문제가 핵심 난제
- **중기 리스크**: 2028년 이후 HBM3 수준의 저사양 HBM 시장에서 가격 파괴 가능성은 열려 있음. DDR4에서 이미 반값 공세 사례가 있어, 기술 성숙 시 반복 가능
- **한국 업체 영향**: SK하이닉스·삼성은 HBM4/HBM4E로 이미 세대 이동 중이므로, **HBM3 수준의 CXMT 진입은 직접 경쟁보다 저가 시장 분리를 촉발**

### 4.6 사이클 판정 심화 — 과거 vs 현재의 구조적 차이

| 차이점 | 2017~2019 사이클 | 2024~2026 현재 사이클 |
|--------|----------------|-------------------|
| **수요 구조** | PC/모바일 업그레이드 (일회성) | AI 추론·훈련 (구조적, 지속적 스케일링) |
| **가격 결정** | 스팟 시장 지배 | **장기 계약(LTA)** 지배 — 변동성 축소 |
| **공급 전환 비용** | DDR3→DDR4 (상대적 용이) | DDR5→HBM (4x 웨이퍼, 후공정 복잡) |
| **생산자 행동** | 과잉 투자 → 과잉 공급 | **CAPEX 규율 강화** (학습 효과) |
| **고객 커밋** | 단기 발주 | **3년+ 장기 계약** (SK하이닉스, Micron) |
| **새 진입자** | 없음 | CXMT (but 기술 격차 2~3세대) |
| **DRAM 내 HBM 비중** | 0% | **20% (2024) → 50% (2030E)** |

**결론**: 현 사이클은 과거와 **구조적으로 다른 특징**(LTA, AI 수요, 전환 비용)을 보유. "사이클 피크 → 급락" 패턴의 반복 확률은 과거보다 낮으나, **완전 면역은 아님**. AI CAPEX 둔화 + 공급 확대 + 삼성 가격 경쟁이 동시 발생할 경우, 완만한 하락(soft landing)은 가능.

---

## 5. Theme D: 기판과 소재 — ABF 필름에서 글라스코어까지

### 5.1 ABF 필름 독점 구조

| 지표 | 수치 | 출처 |
|------|------|------|
| Ajinomoto ABF 필름 글로벌 M/S | **95%+** (사실상 독점) | BigGo Finance |
| ABF 필름 마진 | **50%+** | TrendForce |
| 2026 가격 인상 | **+30%** (Q3 2026 적용) | DIGITIMES, BigGo Finance |
| 부족 시점 | **2026 H1부터 재진입** | BigGo Finance |
| AI칩 기판 레이어 진화 | 3+3 → 11+11 → **13+13** | TrendForce |
| ABF 소요량 변화 | 레이어 진화로 **4배+ 증가** | 업계 |
| 신공장 용지 매입 | ¥1.2B (기후현) | TrendForce |
| 신공장 가동 목표 | **2032년** | TrendForce |

**출처**: [BigGo Finance](https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE), [TrendForce](https://www.trendforce.com/news/2026/05/08/news-ajinomoto-ramps-chip-packaging-push-with-%C2%A51-2b-land-buy-for-new-plant-in-2032-abf-margins-top-50-on-ai-boom/), [DIGITIMES](https://www.digitimes.com/news/a20260513PD230/ic-substrate-abf-substrate-demand-substrate-2026.html)

- **독점의 배경**: ABF 필름은 Ajinomoto가 아미노산 발효 기술에서 파생한 정밀 화학 소재. 경쟁사가 진입하려면 소재 배합·코팅·경화 공정의 수십 년 노하우가 필요
- **대체재 부재**: ABF 필름의 유전 특성(low Dk/Df)이 기판 성능의 핵심이며, 현재 동등 성능의 대체 소재가 부재
- **가격결정력**: 95% 독점 + 50%+ 마진 + 30% 가격 인상 → **밸류체인에서 가장 은밀하고 강력한 해자**
- **공급 불안**: 신공장 가동이 2032년이므로, 2026~2031년까지 **6년간 공급 타이트 구간** 지속

### 5.2 글라스코어(Glass Core) 기판 전환

#### 기술 비교: 글라스코어 vs 유기(ABF) 기판

| 비교 항목 | 유기 기판 (ABF) | 글라스코어 기판 |
|----------|---------------|--------------|
| **열팽창계수 (CTE)** | 12~17 ppm/°C | **3~5 ppm/°C** (실리콘 2.6에 근접) |
| **유전율 (Dk)** | 3.5~4.5 | **4.5~5.0** |
| **유전 손실 (Df)** | 0.005~0.015 | **0.002~0.005** |
| **신호 손실** | 기준 (1x) | **~40% 감소** |
| **열팽창 불일치** | 실리콘 대비 큰 불일치 (워피지 원인) | **~90% 개선** (실리콘에 근접) |
| **대면적 적합성** | 대면적 시 워피지 심화 | 대면적에서도 치수 안정 |
| **비용** | 성숙 (저가) | 고가 (초기 단계) |
| **양산 성숙도** | 수십 년 양산 경력 | 2026~2027 양산 시작 단계 |

**출처**: [FinancialContent](https://markets.financialcontent.com/wral/article/tokenring-2025-12-23-glass-substrates-the-new-frontier-for-high-performance-computing), [TechTicker](https://techticker.fyi/glass-core-substrate-explained-the-5b-packaging-tech-making-abf-obsolete/), [SDxCentral](https://www.sdxcentral.com/news/intel-announces-glass-core-substrate-expected-before-2030/)

#### 글라스코어 양산 타임라인

| 업체 | 시점 | 내용 | 출처 |
|------|------|------|------|
| **Intel** | 2026.01 (NEPCON Japan) | EMIB + 글라스코어 결합 샘플 공개 (78x77mm, 10-2-10 스택) | TrendForce |
| **Intel** | 2026 H2~2027 초 | Rio Rancho 공장에서 세계 최초 글라스코어 양산 목표 | TrendForce |
| **삼성전기** | **2027년** (기존 2026→조정) | 글라스코어 기판 양산 개시 — 기술 완성도 확보에 시간 소요 | 대신증권, 더빅데이터 |
| **Unimicron** | 2027 Q2 | Corning과 JV로 글라스 기판 파일럿 (2nm 샘플 제작) | 업계 |
| **2030 전망** | — | 모든 칩렛 기반 아키텍처에서 글라스가 **표준 기판**이 될 것 | FinancialContent |

**출처**: [TrendForce](https://www.trendforce.com/news/2026/05/26/news-intel-reportedly-eyes-worlds-first-glass-substrate-output-at-rio-rancho-offers-silicon-photonics-to-customers/), [Photon Cap](https://photoncap.net/p/investment-map-15-companies-in-the)

- **핵심 인사이트**: 글라스코어는 ABF 필름의 "대체재"가 아니라 **"보완재"** 가능성이 높음. 글라스코어 + ABF 빌드업 레이어의 하이브리드 구조가 유력 — Ajinomoto에게는 오히려 **긍정적**
- **2030 이후**: 고성능 AI칩에서는 글라스코어가 표준이 되되, ABF 빌드업 레이어는 계속 사용 → ABF 수요 감소보다 구조 변화에 가까움

### 5.3 ABF 기판 Big 5 경쟁

| 순위 | 업체 | 국가 | ABF 기판 M/S | 핵심 CAPA/투자 | 출처 |
|------|------|------|------------|--------------|------|
| 1 | **Unimicron** | 대만 | **~22%** | NVIDIA GPU ABF 35%, ASIC 50%+, AI 매출 비중 60% (2026), CAPA +40%, Corning JV | DIGITIMES |
| 2 | **Ibiden** | 일본 | ~18% (추정) | **¥500B ($3.2B) 3년 투자** (CAPA 2.5배), Phoenix 신공장 $1.2B (30K 패널/월, 2027 말), 고층수(20+) 기판 70~80% 점유 | Kantenna, Nikhs |
| 3 | **AT&S** | 오스트리아 | ~12% (추정) | EU Chips JU €500M ($565M) 지원, Leoben 공장 +20K 패널/월 (2027) | 업계 |
| 4 | **Nan Ya PCB** | 대만 | ~11% (추정) | Formosa Plastics 그룹, CAPA 확대 중 | 업계 |
| 5 | **Shinko** | 일본 | ~11% (추정) | Fujitsu 계열, Intel 패키징 핵심 벤더 | 업계 |
| — | **합산** | — | **~74%** | — | QY Research |

**출처**: [DIGITIMES](https://www.digitimes.com/news/a20260529PD239/unimicron-revenue-2026-demand-substrate.html), [Kantenna](https://kantenna.com/topic/ibiden-5-billion-dollar-investment-ai-ic-package-substrate), [Nikhs Substack](https://nikhs.substack.com/p/ibiden-the-hidden-bottleneck-beneath)

#### ABF 기판 시장 전망

| 시점 | ABF 기판 시장 | 성장률 | 출처 |
|------|-------------|-------|------|
| 2024 | $4.9B | — | Semiconductor Insight |
| **2026E** | **$7.2B** | +47% (2년) | Semiconductor Insight |
| 2030E | $10.2B | CAGR 9.9% | Semiconductor Insight |
| 2032E | $9.5B | CAGR 10.6% | Business Research Insights |

- **3년 슈퍼 확장 사이클**: 업계는 2026 H1부터 ABF 기판이 다시 수급 불균형에 진입하며, 2027~2028년까지 갭이 확대될 것으로 전망 — AI 고객들의 장기 계약(LTA) 체결 러시 중
- **투자 규모 비교**: Ibiden $3.2B (3년), AT&S $565M (EU 지원), Unimicron (CAPA +40%) — 과거 사이클 대비 역대급 투자, AI 수요에 대한 확신의 신호

### 5.4 한국 기업: 삼성전기 FC-BGA

| 지표 | 수치 | 출처 |
|------|------|------|
| 2026E 매출 | ₩13.1T | 더빅데이터 |
| 2026E 영업이익 | ₩1.48T (+62.5% YoY) | 데일리머니 |
| FC-BGA 매출 | **₩2T+ 돌파** 전망 | 더빅데이터 |
| 서버 매출 비중 | 36% | 삼성전기 IR |
| 고부가 FC-BGA 비중 목표 | 50%+ | 삼성전기 |
| 베트남 투자 | ₩1.8T | 업계 |
| **글라스코어 기판** | **2027 양산 개시** (기존 2026→조정) | 대신증권, 더빅데이터 |

**출처**: [더빅데이터](https://www.thebigdata.co.kr/view.php?ud=202603271001066483bbceadc3c9_23), [데일리머니](http://www.thedailymoney.com/news/articleView.html?idxno=1138174)

- **글로벌 유일한 복합 해자**: 삼성전기는 FC-BGA 기판 + MLCC를 동시에 공급할 수 있는 세계 유일 기업 → AI 서버 패키지 모듈 번들 제안 가능
- **글라스코어 선점**: 2027년 양산 개시로 Intel/Unimicron과 함께 글라스코어 초기 시장 진입. 유기 기판→글라스코어 전환에서 한국 기업 중 유일한 플레이어
- **국내 4사 FC-BGA**: ₩1.6T (2025) → **₩2.4T (2026, +48%)** → ₩3.1T (2027, +32%)

### 5.5 CCL(동박적층판)/동박 소재

| 소재 | 역할 | 현황 (2026) |
|------|------|------------|
| **CCL (Copper Clad Laminate)** | ABF 기판의 기초 원재료 — 동박 + 유리섬유 + 수지 적층 | AI 기판 고층수화로 CCL 소요량 증가 |
| **동박 (Copper Foil)** | CCL의 핵심 소재 — 전기 전도층 | 일진머티리얼즈, SK넥실리스 등 한국 업체 강세 |
| **유리섬유 (Glass Fiber)** | CCL/ABF 기판의 보강 소재 | **2026년 부족 발생** — 기판 가격 인상 요인 |

- **유리섬유 부족 (2026)**: AI 패키징 수요 급증 + 기판 고층수화로 유리섬유 소요량 폭증. Unimicron 등 기판 업체들이 유리섬유 부족을 기판 가격 인상의 근거로 활용 중
- **CCL 공급망**: 범용 CCL은 중국 업체(Shengyi Technology 등)가 가격 경쟁 중이나, 고성능 CCL(low-Dk/Df)은 일본/대만 업체의 기술 장벽 존재

### 5.6 Theme D 투자 시사점

| 업체/소재 | 해자 강도 | 투자 판단 |
|---------|---------|----------|
| **Ajinomoto (ABF 필름)** | ★★★★★ — 95% 독점, 대체재 부재, 50%+ 마진, 30% 가격 인상 | **최강 해자** — 글라스코어 전환 시에도 ABF 빌드업 레이어 수요 유지. 2026~2031 공급 타이트 구간. 식품 사업 혼재로 퓨어플레이 아닌 점이 투자 시 고려사항 |
| **Unimicron (#1)** | ★★★★☆ — NVIDIA GPU/ASIC 핵심 벤더, AI 60% 비중 | **강세** — AI 기판 사이클의 직접 수혜. 글라스 기판 JV로 차세대 대비. BofA 목표가 상향 |
| **Ibiden (#2)** | ★★★★☆ — $3.2B 역대급 투자, 고층수 기판 70~80% 점유 | **강세** — 고층수(20+) 기판의 과점적 지위. AI 확신의 투자 규모 |
| **삼성전기** | ★★★★☆ — FC-BGA+MLCC 유일, 글라스코어 2027 양산 | **강세** — 기판+MLCC 번들 해자 + 글라스코어 선점. 국내 최선호주 |
| **AT&S (#3)** | ★★★☆☆ — EU 지원, 유럽 유일 | **중립~긍정** — 지역 다변화 수혜, EU 보조금 |
| **유리섬유/CCL** | ★★☆☆☆ — 범용 소재, 경쟁 치열 | **선별적** — 2026 부족 구간 단기 수혜, 구조적 해자 약함 |

---

## 6. 테마 간 교차 시사점 — 테마 연결 분석

### 6.1 A↔B: 패키징 기술 전쟁과 본딩 전환의 상호작용

- CoWoS-L의 초대면적화(5.5x→14x 레티클)는 **더 많은 HBM 스택을 탑재**하게 하며, 이는 곧 **더 많은 본딩 공정**을 요구
- 하이브리드 본딩은 미세 피치로 **단위 면적당 인터커넥트 밀도를 높여** CoWoS-L의 면적 효율을 극대화 → 두 기술은 **상호 강화 관계**
- CoPoS(패널 레벨)가 2028~2029 양산 시, 하이브리드 본딩과 결합하면 **패키징 CAPA 병목과 본딩 병목을 동시에 해소**할 가능성

### 6.2 B↔C: 본딩 전환과 메모리 사이클의 타이밍

- HBM4E/HBM5에서 하이브리드 본딩이 의무화되는 시점(2028~2029)은 **메모리 사이클이 공급 > 수요로 전환될 수 있는 시점과 겹침**
- 시나리오: 수요 둔화 + 신규 본딩 장비 투자(CAPEX 부담) → 메모리 업체 수익성 이중 압박 가능
- 반대 시나리오: HBM5 20-Hi의 성능 점프가 새로운 수요 웨이브를 만들어 사이클 연장

### 6.3 C↔D: CXMT 진입과 기판/소재 공급

- CXMT가 HBM3 양산에 성공하더라도, **ABF 기판과 ABF 필름은 일본·대만 업체 독점** → 소재 조달이 CXMT의 추가 병목
- 미국 수출 규제가 장비에 집중되어 있으나, 향후 **소재 규제로 확대될 경우** CXMT 일정이 더욱 지연
- CXMT의 현실적 대안: 중국 국산 소재(低사양) + 기존 DDR5 기판 활용 → 성능 타협

### 6.4 A↔D: 패키징 기술과 기판의 공진화

- CoWoS-L의 대면적화 → ABF 기판도 대형화 필요 → **ABF 필름 소요량 비례 증가**
- 글라스코어 기판은 CoWoS-L의 워피지 문제를 근본적으로 해결 → **패키징 수율 개선 + 비용 절감**의 핵심 인에이블러
- 2028~2030 시나리오: CoPoS(유리 패널) + 글라스코어 기판 + 하이브리드 본딩 = **차세대 패키징 트라이앵글**

### 6.5 종합: 시간축별 투자 우선순위

| 시간축 | 최우선 테마 | 핵심 종목/섹터 | 근거 |
|--------|-----------|-------------|------|
| **2026 H2~2027** | A (CoWoS CAPA) + D (ABF 부족) | TSMC, Amkor/SPIL, Unimicron, Ajinomoto, 삼성전기 | 패키징+기판 수급갭 최대 구간 |
| **2027~2028** | B (하이브리드 본딩) + C (사이클 전환점) | BESI, 한미반도체 (전환 대비), SK하이닉스 (LTA 보호) | 본딩 기술 전환 + 수급 밸런스 접근 |
| **2028~2030** | A→CoPoS 전환 + D→글라스코어 | 삼성전기 (글라스), Intel (EMIB+글라스), Applied Materials | 차세대 기술 표준 확립기 |

---

## 7. 출처 목록

### TSMC 패키징 기술
- LoveChip, *CoWoS vs CoPoS vs CoWoP: TSMC Advanced Packaging Explained* — [링크](https://www.lovechip.com/blog/cowos-vs-copos-vs-cowop-tsmc-advanced-packaging-explained)
- AMI Next, *CoWoS-S, R, L Explained* — [링크](https://www.aminext.blog/en/post/tsmc-cowos-s-r-l-differences)
- ChipStrat, *Advanced Packaging: Intel's EMIB vs TSMC's CoWoS* — [링크](https://www.chipstrat.com/p/advanced-packaging-intels-emib-vs)
- TrendForce, *CoWoS Wafer ASP Nears 7nm* (2026.04) — [링크](https://www.trendforce.com/news/2026/04/28/news-tsmc-cowos-wafer-asp-reportedly-nears-7nm-levels-advanced-packaging-poised-to-become-a-key-profit-driver/)
- TrendForce, *CoWoS Supply-Demand Gap 20%→10%* (2026.06) — [링크](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- TrendForce, *CoPoS Pilot Line June Completion* (2026.04) — [링크](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)
- 36Kr, *Who Will Divide Up CoWoS Production Capacity in 2026?* — [링크](https://eu.36kr.com/en/p/3580962946874242)
- FinancialContent, *TSMC Doubling CoWoS Capacity* — [링크](https://markets.financialcontent.com/stocks/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026)
- SemiconductorX, *Advanced Packaging Comparison Matrix* — [링크](https://semiconductorx.com/packaging-matrix.html)

### 인텔 EMIB/Foveros
- Tom's Hardware, *Intel EMIB-T Heads for Fab Rollout* — [링크](https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-t-heads-for-fab-rollout-this-year)
- Tom's Hardware, *Intel Gains Ground in AI Packaging* — [링크](https://www.tomshardware.com/tech-industry/semiconductors/intel-gains-ground-in-ai-packaging-as-cowos-capacity-remains-stretched)
- TrendForce, *MediaTek Dual Packaging Strategy* (2026.05) — [링크](https://www.trendforce.com/news/2026/05/12/news-mediatek-reportedly-adopts-dual-packaging-strategy-with-intel-emib-tsmc-cowos-for-ai-asic-push/)
- EE Times, *Intel's Embarrassment of Riches: Advanced Packaging* — [링크](https://www.eetimes.com/intels-embarrassment-of-riches-advanced-packaging/)

### 삼성 패키징
- DIGITIMES, *Samsung, TSMC Diverge on Panel Materials* — [링크](https://www.digitimes.com/news/a20241225PD212/samsung-tsmc-foplp-packaging-materials.html)
- TrendForce, *Samsung Eyes 2029 CPO Turnkey* — [링크](https://www.trendforce.com/news/2026/04/01/news-silicon-photonics-race-intensifies-as-tsmc-targets-2026-coupe-production-samsung-eyes-2029-cpo-turnkey/)

### 하이브리드 본딩
- TrendForce, *Hybrid Bonder Market Near $2B by 2028* (2025.10) — [링크](https://www.trendforce.com/news/2025/10/07/news-hybrid-bonder-equipment-market-reportedly-near-2b-by-2028-as-korean-makers-race-to-next-gen-hbm-tools/)
- TrendForce, *BESI Draws Takeover Interest* (2026.03) — [링크](https://www.trendforce.com/news/2026/03/13/news-hybrid-bonding-leader-besi-reportedly-draws-takeover-interest-lam-applied-materials-rumored/)
- Semi Engineering, *HBM4 Sticks With Microbumps* — [링크](https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/)
- EBN뉴스, *한미반도체 2028년 겨냥 재평가* — [링크](https://www.ebn.co.kr/news/articleView.html?idxno=1700474)
- BESI IR, *Q1'26 Results* — [링크](https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q1-26-results/)
- TipRanks, *BESI Rides Hybrid Bonding Wave* — [링크](https://www.tipranks.com/news/company-announcements/be-semiconductor-rides-hybrid-bonding-wave-in-earnings)
- Photon Cap, *7 Bonding Equipment Companies Behind HBM4* — [링크](https://photoncap.net/p/7-bonding-equipment-companies-behind)
- TSPA Semiconductor, *Hybrid Bonding at Scale: BESI's Vision* — [링크](https://tspasemiconductor.substack.com/p/hybrid-bonding-at-scale-besis-vision)

### 메모리 사이클/HBM 가격
- Uncover Alpha, *Every Memory Cycle Ends the Same. Until It Doesn't.* — [링크](https://www.uncoveralpha.com/p/every-memory-cycle-ends-the-same)
- Luminix, *DRAM Cycle Analysis 2026* — [링크](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)
- Silicon Analysts, *Historical Semiconductor Market Data* — [링크](https://siliconanalysts.com/market-data)
- SemiAnalysis, *Memory Mania: Once-in-Four-Decades Shortage* — [링크](https://newsletter.semianalysis.com/p/memory-mania-how-a-once-in-four-decades)
- Avnet, *Riding the AI Supercycle: 2026 Memory & Storage Market* — [링크](https://www.avnet.com/integrated/resources/article/2026-memory-shortage-ai-supercycle/)
- TrendForce, *Samsung·SK hynix HBM3E Price Hike +20%* (2025.12) — [링크](https://www.trendforce.com/news/2025/12/24/news-samsung-sk-hynix-reportedly-plan-20-hbm3e-price-hike-for-2026-as-nvidia-h200-asic-demand-rises/)
- Silicon Analysts, *HBM Pricing* — [링크](https://siliconanalysts.com/market-data/hbm-pricing)

### CXMT/중국 메모리
- DIGITIMES, *CXMT HBM3 Timeline Slips* — [링크](https://www.digitimes.com/news/a20260421PD230/cxmt-hbm3-dram-production-2026.html)
- DIGITIMES, *CXMT Targets 12-Layer HBM by 2027* — [링크](https://www.digitimes.com/news/a20260409PD229/cxmt-hbm-production-2027-market.html)
- Tom's Hardware, *Chinese HBM3 Production Gears Up* — [링크](https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly)
- FinancialContent, *CXMT $4.2B IPO* — [링크](https://markets.financialcontent.com/stocks/article/tokenring-2026-1-23-chinas-cxmt-targets-2026-hbm3-production-with-42-billion-ipo)
- Digital Today, *China Low-Spec HBM Front Expands* — [링크](https://www.digitaltoday.co.kr/en/view/57201/china-led-low-spec-hbm-front-expands-raising-concerns-over-impact-on-korean-memory-profits)
- ChinaTalk, *Mapping China's HBM Advances* — [링크](https://www.chinatalk.media/p/mapping-chinas-hbm-advancement)

### ABF 필름/Ajinomoto
- BigGo Finance, *Ajinomoto ABF Film 95% M/S, 30% Price Hike* — [링크](https://finance.biggo.com/news/ZU2KJZ4BpwxG186NIOsE)
- TrendForce, *Ajinomoto ¥1.2B Land Buy for New Plant* (2026.05) — [링크](https://www.trendforce.com/news/2026/05/08/news-ajinomoto-ramps-chip-packaging-push-with-%C2%A51-2b-land-buy-for-new-plant-in-2032-abf-margins-top-50-on-ai-boom/)
- DIGITIMES, *Ajinomoto Raises ABF Film Prices 30%* — [링크](https://www.digitimes.com/news/a20260513PD230/ic-substrate-abf-substrate-demand-substrate-2026.html)
- Nikhs Substack, *ABF: The Material Beneath the Model* — [링크](https://nikhs.substack.com/p/abf-the-material-beneath-the-model)

### 글라스코어 기판
- FinancialContent, *Glass Substrates: New Frontier for HPC* — [링크](https://markets.financialcontent.com/wral/article/tokenring-2025-12-23-glass-substrates-the-new-frontier-for-high-performance-computing)
- TechTicker, *Glass Core Substrate Explained* — [링크](https://techticker.fyi/glass-core-substrate-explained-the-5b-packaging-tech-making-abf-obsolete/)
- TrendForce, *Intel Eyes World's First Glass Substrate Output* (2026.05) — [링크](https://www.trendforce.com/news/2026/05/26/news-intel-reportedly-eyes-worlds-first-glass-substrate-output-at-rio-rancho-offers-silicon-photonics-to-customers/)
- SDxCentral, *Intel Glass Core Substrate Before 2030* — [링크](https://www.sdxcentral.com/news/intel-announces-glass-core-substrate-expected-before-2030/)
- Photon Cap, *15 Companies in the Glass Substrate Cycle* — [링크](https://photoncap.net/p/investment-map-15-companies-in-the)
- TrendForce Insights, *Glass Substrates Breaking Through AI Packaging Bottleneck* — [링크](https://insights.trendforce.com/p/glass-substrate-development)

### ABF 기판 시장/Big 5
- DIGITIMES, *Unimicron Revenue 2026 Demand* — [링크](https://www.digitimes.com/news/a20260529PD239/unimicron-revenue-2026-demand-substrate.html)
- DIGITIMES, *Unimicron ABF Substrate AI Server Capacity* — [링크](https://www.digitimes.com/news/a20260130PD220/unimicron-abf-substrate-ai-server-market-capacity.html)
- Kantenna, *Ibiden $5B Investment AI IC Package Substrate* — [링크](https://kantenna.com/topic/ibiden-5-billion-dollar-investment-ai-ic-package-substrate)
- Nikhs Substack, *Ibiden: The Hidden Bottleneck Beneath AI* — [링크](https://nikhs.substack.com/p/ibiden-the-hidden-bottleneck-beneath)
- Semiconductor Insight, *ABF Substrate Market* — [링크](https://semiconductorinsight.com/report/abf-substrate-market/)
- Business Research Insights, *ABF Market 2026-2035* — [링크](https://www.businessresearchinsights.com/market-reports/ajinomoto-build-up-film-abf-market-122893)
- Intel Market Research, *ABF Substrate Market Outlook 2026-2032* — [링크](https://www.intelmarketresearch.com/abf-substrate-market-21855)

### 한국 기업
- 더빅데이터, *삼성전기 FC-BGA* — [링크](https://www.thebigdata.co.kr/view.php?ud=202603271001066483bbceadc3c9_23)
- 데일리머니, *삼성전기 실적 전망* — [링크](http://www.thedailymoney.com/news/articleView.html?idxno=1138174)
- 소뮤어, *한미반도체 TC본더 M/S* — [링크](https://somsap.somsap.com/2026/05/01/한미반도체-hbm-tc본더-시장-점유율-2026/)

### 기존 시리즈 참조
- `data/research_hbm_pkg_part12_overview.md` — Part 1-2 산업구조와 투자 좌표
- `data/note-ai-money-flow_20260618.md` — 투자 사고 프레임워크 (병목/해자/비대칭성)

---

## 8. 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-06-22 | 초안 작성 — 4대 테마(A: 첨단 패키징 기술 전쟁, B: 하이브리드 본딩 전환, C: 메모리 사이클과 CXMT, D: 기판과 소재) 심화 분석. 테마 간 교차 시사점 포함. 시간축별 투자 우선순위 도출 |
