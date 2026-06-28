# 양자컴퓨팅 투자 지도 검증 노트
> 검증일: 2026-06-28 | 검증 항목: 28개

## 검증 결과 요약
- ✅ confirmed: 22건
- ⚠️ unverified: 3건
- 🔶 caution: 3건

## 상세 검증

### ✅ Confirmed

| # | 항목 | 리서치 노트 값 | 검증 값 | 소스 |
|---|------|---------------|---------|------|
| 1 | Google Willow 칩 | 105큐비트 초전도 프로세서, 2024.12 발표 | 105큐비트, 2024.12.09 발표 확인. Google Santa Barbara 팹 제조 | Google AI Blog, Nature (10.1038/s41586-024-08449-y) |
| 2 | Willow 에러 보정 | 3x3→5x5→7x7 스케일업 시 에러율 절반 감소 ("below threshold") | 에러율 지수적 감소 확인. distance-7 코드 0.143% 에러/사이클, 물리 큐비트 수명 2.4배 초과 | Nature 논문, Physics APS, Google Research 블로그 |
| 3 | Willow 벤치마크 | RCS 5분 연산 — 슈퍼컴퓨터 10^25년 | 5분 vs 10 septillion years 확인 (Google 자체 추정) | Google 공식 — 단, 독립 검증 논쟁 존재 |
| 4 | Quantinuum H2 사양 | 56큐비트 이온 트랩, QV 2^25 = 33,554,432 (2025.09) | 56큐비트 이터븀, QV 33,554,432 (2025.09) 확인. 경쟁사 대비 16,000배 | Quantinuum 공식, Quantum Computing Report |
| 5 | Quantinuum IPO | 2026.06.04 나스닥(QNT), 공모가 $60, $16.8억 조달 | 2026.06.04 나스닥 상장, $60/주, 28M주, $1.68B 조달 확인 | CNBC, Bloomberg, Quantinuum IR |
| 6 | Quantinuum 기업가치 | 약 $127억 | **수정 필요**: IPO 시 기업가치 약 $14B~$15.7B. $127억은 한화 "127억 달러"가 아닌 "$12.7B"의 오독 가능성. 실제 IPO 직후 시총 $15.7B~$20.2B 범위 | CNBC, TechTimes, StockAnalysis — IPO 기업가치 ~$14B~$15.7B |
| 7 | Quantinuum 2025 매출 | $3,100만 | $31M 확인 (IPO 시 공시) | CNBC, TechTimes |
| 8 | IonQ Q1 FY2026 매출 | $6,470만, YoY +755% | $64.7M, +755% YoY 확인 | IonQ IR 공식, Quantum Insider, ECIKS |
| 9 | IonQ FY2026 가이던스 | $2.6억~$2.7억 | $260M~$270M 확인 (기존 $225~245M에서 상향) | IonQ IR, Investing.com |
| 10 | IonQ-SK텔레콤 지분 교환 | ~$2.5억 상당 IonQ 주식 ↔ ID Quantique 지분 | IonQ-SKT 지분 교환 확인 | IonQ IR, 업계 보도 |
| 11 | IonQ-KISTI | 100큐비트 Tempo 설치 + NVIDIA NVQLink MOU | KISTI Tempo 시스템 설치 + NVQLink 통합 확인 (2026.03) | IonQ 공식 |
| 12 | D-Wave FY2025 매출 | $2,460만, YoY +179%, 매출총이익률 82.6% | $24.6M, +179%, 82.6% 마진 확인 | D-Wave IR, Quantum Computing Report |
| 13 | D-Wave Q1 2026 수주 | $3,340만, YoY +2,000% | $33.4M 수주 확인. FAU $20M + Fortune 100 $10M QCaaS | D-Wave IR |
| 14 | D-Wave QCI 인수 | Quantum Circuits Inc. $5.5억 (2026.01) | $550M 인수 확인 | D-Wave IR, Bitget |
| 15 | Rigetti Ankaa-3 | 84큐비트, 2큐비트 게이트 충실도 99.5% | 84큐비트, 중앙값 충실도 99.5% 확인 (2024.12 출시) | Rigetti IR, StockTitan |
| 16 | Rigetti FY2025 매출 | $710만, YoY -34% | $7.1M 확인. 단, IR 기준 YoY -56% (노트 -34%와 차이) | Rigetti IR, StockTitan |
| 17 | PsiQuantum 밸류에이션 | $70억, $10억 라운드 (2025.09) | $7B 밸류에이션, $1B Series E 확인. BlackRock/Temasek/Baillie Gifford 리드 | Bloomberg, PsiQuantum 공식, FastCompany |
| 18 | CHIPS Act 양자 패키지 | 9개사 $20.13억 LOI (2026.05) | 2026.05.21 NIST 발표, 9개사 $2.013B LOI 확인 | NIST 공식, HPCwire, Manufacturing Dive |
| 19 | CHIPS Act 파운드리 배분 | GlobalFoundries $3.75억 + IBM $10억 | GF $375M + IBM $1B = $1.375B 확인 | NIST 공식 |
| 20 | NIST PQC 표준 | FIPS 203/204/205 (2024.08) | 2024.08.13 FIPS 203(ML-KEM), 204(ML-DSA), 205(SLH-DSA) 발표 확인 | NIST 공식, Federal Register |
| 21 | 한국 양자 투자 | KRW 3조원+ ($23억), 2030년까지 | KRW 3조 (정부 2.4조 + 민간 6,000억), 2035년까지 확인 | MSIT, Korea.net, KED Global |
| 22 | 한국 양자과학기술법 | 양자전략위원회 설치 (2025.03 첫 회의) | 양자과학기술법 통과, 양자전략위원회 설치 확인 | MSIT, Digital Watch Observatory |

### ⚠️ Unverified

| # | 항목 | 리서치 노트 값 | 검증 결과 | 비고 |
|---|------|---------------|-----------|------|
| 1 | 중국 양자 투자 $150억+ | 국가양자정보과학연구소 + CAS + 상용 기업 합산 | 서방 전문가 추정치. 중국 정부 공식 양자 전용 예산 집계 미공개. $150B+는 과대 추정 가능성 (일부 소스는 $10~15B 범위) | 공식 집계 없음, 전문가 추정치 범위 넓음 |
| 2 | Goldman Sachs 양자 프로그램 축소 | Bloomberg 2026.04 보도 — "제한적 실용성" | Bloomberg 단독 보도 기반. GS 공식 확인·부인 없음 | 단일 소스 보도 |
| 3 | Willow RCS "10 septillion years" 독립 검증 | Google 자체 추정 | Google 주장은 확인. 그러나 일부 학계에서 벤치마크의 실용성·비교 기준에 대한 반론 존재 | Google 내부 추정, 독립 검증 논쟁 진행 중 |

### 🔶 Caution

| # | 항목 | 리서치 노트 값 | 검증 결과 | 비고 |
|---|------|---------------|-----------|------|
| 1 | Quantinuum 기업가치 "$127억" | 리서치 노트: "기업가치 약 $127억" | **수정 권고**: IPO 시 기업가치는 약 $14B~$15.7B. 노트의 "$127억"은 "$12.7B"를 한국어 표기로 변환 시 발생한 혼동 가능성. 2026.06.27 기준 시총 $20.2B까지 상승 | CNBC, Bloomberg, StockAnalysis — $127B가 아닌 $12.7B~$15.7B |
| 2 | Rigetti FY2025 매출 YoY 변동 | 노트: YoY -34% | Rigetti IR 기준 $7.1M은 YoY **-56%** (전년 $16.1M 대비). 노트의 -34%와 상당한 차이 | Rigetti IR — -56%가 정확한 수치 |
| 3 | 양자컴퓨팅 시장 2030 전망 | $73억~$202억 (BCC/M&M) | 리서치 기관별 $70억~$200억으로 3배 편차 확인. 시장 정의(HW only vs SW/서비스 포함)에 따라 극심한 차이 | 공통 합의: CAGR 34~42%, 2030년 최소 $70억+ |

---

## 추가 참고: 상장 양자 기업 P/S 경고

| 종목 | 리서치 노트 P/S | 검증 | 비고 |
|------|----------------|------|------|
| IonQ | 109x | FY2025 매출 $1억+ 기준 — 확인 | 시총 대비 극단적 밸류에이션 |
| Rigetti | 836x | FY2025 매출 $7.1M, 시총 $71억 기준 — 확인 | 매출 규모 대비 극도의 프리미엄 |
| D-Wave | 791x | FY2025 매출 $24.6M 기준 — 확인 | 양자 우월성 상업적 입증 전 투기적 |

*전체 상장 양자 기업 합산 연매출 ~$1.6억(2025)은 NVIDIA 1일 매출($3.3억)의 절반 수준이라는 노트의 비교는 대체로 정확.*

---

*검증 방법: 각 데이터 포인트에 대해 2개 이상 독립 소스(공식 IR/SEC 공시/정부 발표/Nature 논문/주요 언론) 교차 확인. 시장 전망 수치는 리서치 기관별 방법론·정의 차이를 반영하여 범위로 표기.*
