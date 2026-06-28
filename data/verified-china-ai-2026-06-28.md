# 중국 AI 생태계 검증 노트
> 검증일: 2026-06-28 | 검증 항목: 22개

## 검증 결과 요약
- ✅ confirmed: 16건
- ⚠️ unverified: 2건
- 🔶 caution: 4건

---

## 상세 검증

### ✅ Confirmed

| # | 항목 | 리서치 노트 값 | 검증 값 | 소스 |
|---|------|---------------|---------|------|
| 1 | DeepSeek R1 AIME 2024 정확도 | 86.7% | 86.7% 확인. Codeforces 96.3 퍼센타일도 일치 | [DeepSeek-R1 arXiv 논문](https://arxiv.org/html/2501.12948v1), [DataCamp](https://www.datacamp.com/blog/deepseek-r1) |
| 2 | DeepSeek V4 Pro 파라미터 | 1.6T (49B active), MoE | 1.6T 파라미터, 49B 활성, MoE 구조, MIT 라이선스 확인 | [BuildFastWithAI](https://www.buildfastwithai.com/blogs/deepseek-v4-pro-review-2026), [DataCamp](https://www.datacamp.com/blog/deepseek-v4) |
| 3 | DeepSeek V4 Pro SWE-bench | 80.6% (오픈 웨이트 최고점) | SWE-bench Verified 80.6% 확인. Claude Opus 4.6과 0.2pp 이내 | [AIMadeTools](https://www.aimadetools.com/blog/deepseek-v4-pro-complete-guide/), [MorphLLM](https://www.morphllm.com/deepseek-v4) |
| 4 | DeepSeek 자금조달 | ~$74억(500억 위안), 기업가치 $500~590억 | 50억+ 위안(~$7.4B) 조달, 기업가치 $50B+ 확인. 량원펑 개인 ~200억 위안 출자 | [TechFundingNews](https://techfundingnews.com/deepseek-raises-7-4b-at-50b-valuation-in-first-ever-external-funding-round/), [Seeking Alpha](https://seekingalpha.com/news/4603859-deepseek-completes-record-7b-plus-fundraising-valuation-tops-50b---report) |
| 5 | Qwen 다운로드 ~10억 회 | 2026.04 기준 약 10억 회, 오픈소스 50%+ 점유 | 2026.03 기준 ~9.42억, 2월 단월 1.536억 DL. 글로벌 오픈소스 50%+ 확인 | [SCMP](https://www.scmp.com/tech/big-tech/article/3349552/alibabas-qwen-family-captures-over-50-global-open-source-downloads-report-finds), [Gizmochina](https://www.gizmochina.com/2026/04/10/alibaba-qwen-ai-downloads-1-billion-leads-open-source-ai/) |
| 6 | Moonshot AI 기업가치 $200억 | 2026.05, 누적 조달 $39억 | $20B 밸류에이션, $2B 신규 조달(메이퇀 주도), 6개월 만에 $4.3B→$20B 확인 | [TechCrunch](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/), [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-07/kimi-chatbot-maker-moonshot-ai-valued-at-20-billion-in-meituan-led-round) |
| 7 | Moonshot ARR $2억 | 2026.04 돌파 | ARR $200M+ (2026.04) 확인. 유료 구독 + API 급성장 | [TechCrunch](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/) |
| 8 | Doubao MAU 2.26억 명 | 중국 AI 네이티브 앱 1위 | 2025년 말 ~2.26억, 2026.02 기준 2.27억 MAU 확인 | [Wikipedia - Doubao](https://en.wikipedia.org/wiki/Doubao), [DataGlobeHub](https://dataglobehub.com/doubao-statistics-and-insights/) |
| 9 | Zhipu AI 홍콩 IPO | HK$116.20/주, 조달 HK$41.7억, 기업가치 ~$70억 | 2026.01.08 상장, HK$116.20, HK$41.7억 조달, 기업가치 ~$7.1B 확인 | [SCMP](https://www.scmp.com/tech/article/3357858/zhipu-ai-market-cap-tops-hk1-trillion-shares-glm-52-developer-soar), [Caixin](https://www.caixinglobal.com/2026-01-08/chinas-zhipu-ai-jumps-in-hong-kong-debut-102401610.html) |
| 10 | Zhipu 2025 매출 | RMB 7.24억(~$1.05억), YoY +132% | RMB ~7.24억(~$105M), +132% YoY 확인. 순손실 RMB 47억 | [TheAIRankings](https://theairankings.com/zhipu/), [SCMP](https://www.scmp.com/tech/article/3357858/zhipu-ai-market-cap-tops-hk1-trillion-shares-glm-52-developer-soar) |
| 11 | 중국산 AI 칩 M/S 41% | 총 165만 개 출하 / 전체 400만 개 | 중국산 ~165만 개(41%), NVIDIA ~220만 개(55%) 확인. 정부 국산화 지침 반영 | [Tom's Hardware](https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips), [IndexBox](https://www.indexbox.io/blog/chinese-chipmakers-capture-41-of-domestic-ai-server-market-in-2025/) |
| 12 | NVIDIA 중국 M/S 하락 | ~95% → ~55% (40pp 하락) | 95% → 55% 확인. Jensen Huang 본인이 "95%에서 0%로" 언급(수출 금지 기준) | [Fortune](https://fortune.com/2025/10/19/jensen-huang-nvidia-china-market-share-ai-chips-trump-trade-war/), [KuCoin](https://www.kucoin.com/news/flash/nvidia-s-china-ai-chip-market-share-drops-to-55-as-domestic-brands-capture-41) |
| 13 | Huawei 출하량 81.2만 개 | ~20% M/S | ~81.2만 개, 전체 시장의 ~20%, 국산 칩의 거의 절반 확인 | [Tom's Hardware](https://www.tomshardware.com/tech-industry/nvidia-market-share-in-china-falls-to-less-than-60-percent-chinese-chip-makers-deliver-1-65-million-ai-gpus-as-the-government-pushes-data-centers-to-use-domestic-chips) |
| 14 | CloudMatrix 384 BF16 ~300 PFLOPS | 384 NPU + 192 CPU, HBM 48TB | BF16 ~300 PFLOPS, 384 Ascend 910C NPU + 192 Kunpeng CPU, HBM 48TB 확인. 전력 559kW | [SemiAnalysis](https://semianalysis.com/2025/04/16/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72/), [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/huaweis-new-ai-cloudmatrix-cluster-beats-nvidias-gb200-by-brute-force-uses-4x-the-power) |
| 15 | Cambricon 2025 매출 YoY +453% | 최초 흑전 | 매출 64.97억 위안(+453%), 순이익 20.59억 위안(첫 연간 흑자) 확인 | [Pandaily](https://pandaily.com/cambricon-posts-first-full-year-profit-since-listing-as-2025-revenue-surges-453), [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-12/cambricon-rides-china-ai-boom-to-post-its-first-annual-profit) |
| 16 | CXMT 월 캐파 추이 | 2024초 10만 → 2025말 29만 매 | 2024초 10만 → 2025말 ~28~29만 매 확인. 2026말 35만 매 전망도 업계 컨센서스 부합 | [SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram), [Digitimes](https://www.digitimes.com/news/a20250421PD218/cxmt-dram-samsung-sk-hynix-2025.html) |

### ⚠️ Unverified

| # | 항목 | 리서치 노트 값 | 검증 결과 | 비고 |
|---|------|---------------|----------|------|
| 17 | SMIC 5nm 수율 20% 미만 | 2026년 양산 목표 | 다수 테크 매체(WCCFTech, SemiAnalysis)에서 인용되나, SMIC 공식 발표 없음. 실제 수율 데이터는 기밀로 외부 확인 불가 | 방향성(EUV 부재로 인한 수율 제약)은 업계 공감대 |
| 18 | BYD 인텔리전트 드라이빙 투자 1,000억 위안 | CarNewsChina 보도 기반 | BYD IR 자료에서 구체 금액 직접 확인 실패. R&D 인력 5,000명+은 다수 매체 인용 | 대규모 ADAS 투자 방향성은 확인되나 정확한 금액 미검증 |

### 🔶 Caution

| # | 항목 | 리서치 노트 값 | 검증 결과 | 주의 사항 |
|---|------|---------------|----------|----------|
| 19 | Ascend 910C FP16 성능 | 320 TFLOPS | **대다수 출처에서 FP16 ~800 TFLOPS로 보고**. 320 TFLOPS는 단일 다이 기준 또는 구형 추정치일 가능성 높음. 910C는 듀얼다이 패키징으로 총 성능은 ~800 TFLOPS에 가까움 | [unite.ai](https://www.unite.ai/huaweis-ascend-910c-a-bold-challenge-to-nvidia-in-the-ai-chip-market/), [WareDB](https://www.waredb.com/processor/ascend-910c) |
| 20 | Ascend 910C vs H100 성능 | H100의 60~70% | 출처별 상이: "H100의 약 80%" (일부), "60~70%" (일부). FP16 기준 ~800 TFLOPS는 H100과 유사하나, 아키텍처 효율·소프트웨어 생태계에서 열위. **실측 벤치마크(MLPerf 등) 부재로 정확한 비교 어려움** | [nexgen-compute](https://www.nexgen-compute.com/blog/huawei-ascend-910c-vs-nvidia-h100-ai-chip-comparison) |
| 21 | DeepSeek V4 Pro 가격 | 입력 $0.435/M, 출력 $0.87/M | **프로모션 할인가(75% 할인)**. 정가는 입력 $1.74/M, 출력 $3.48/M. 2026.05.31 이후 할인가가 정식 가격으로 전환됨. 노트 작성 시점의 실효 가격은 맞으나, "GPT-5.2 대비 4배 저렴" 비교는 기준 가격에 따라 상이 | [DeepSeek API Docs](https://api-docs.deepseek.com/quick_start/pricing), [OpenRouter](https://openrouter.ai/deepseek/deepseek-v4-pro) |
| 22 | CXMT 글로벌 DRAM 캐파 17% | 2026년 말 35만 매/월 전망 시 | **17% 도달 시점은 2027년 말**(42만 매/월 기준) 전망. 2026년 말 35만 매/월 시점에서는 ~13~15% 수준으로 추정. 17%는 1년 정도 앞서 인용 | [SemiAnalysis](https://newsletter.semianalysis.com/p/chinas-cxmt-is-set-to-challenge-dram), [S&P Global](https://www.spglobal.com/automotive-insights/en/blogs/2026/02/mainland-china-dram-push) |

---

*검증 방법: 웹 검색 기반 교차 확인 (기업 공식 발표, arXiv 논문, 업계 분석 보고서, 주요 테크/금융 매체 대조)*
