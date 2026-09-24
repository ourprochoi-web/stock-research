# CW 레이저 공급사 도셔 — SEI · 위안제 (+ InP peers)

| 항목 | 값 |
|---|---|
| Archive gap | `brain/open.json` → `cw-laser-leaders` (judgment **0** · since 2026-09-14) |
| As-of | 2026-09-23 KST (시세 스냅샷은 거래소 마감일 표기) |
| Scope | Sumitomo Electric (SEI) · Yuanjie(源杰) · 기타 CW/InP 약식 · COHR/LITE 대비 · KR 접근 |
| Grade legend | ① 회사 IR/공시 · ② 거래소·1차 시세 · ③ 브로커/업계(미즈호·TrendForce 등) · [추론] 명시 |
| Rule | **숫자 발명 금지** — 출처 없는 점유·ASP·마진은 비움 또는 「미확인」 |

> Parent merge 노트: 이 파일은 `cw-laser-leaders` 판단 0 메우기용 intake. `brain/*.json` 비파괴. 미즈호 09-14 CW 점유(③)와 TrendForce CW **캐파** 리더십(③)은 **지표가 다름**(매출 점유 ≠ 캐파) — 교차 확인 전 한 숫자로 합치지 말 것.

---

## 0. 한 줄 (Lead)

AI 광원 층에서 **CW-DFB는 SiPho 플러거블·OCS·CPO 경로**로 EML과 병행 확대 중. **SEI(5802.T)**는 수직(InP 기판→디바이스) + 정보통신 OP 급증으로 「순수 CW 플레이」가 아니라 **복합 일본 소재/와이어 거인 안의 광 병목 노출**. **위안제(688498.SS)**는 CW 70/100mW 양산으로 AI 데이터센터 매출이 이미 과반이지만 **STAR 고배수·KR 접근 난이도·중국 공급망 리스크**가 동시에 큼. COHR/LITE 대비: LITE=고속 EML·UHP CW 쪽 내러티브, COHR=모듈+InP 수직·CW 400mW/6″ 전환, SEI=일본 기판 병목+CW 캐파 선두권, 위안제=중국 상용 CW(70–100mW) 스케일.

---

## 1. Sumitomo Electric Industries — SEI

### 1.1 티커 · 법인

| | |
|---|---|
| 정식 | 住友電気工業株式会社 / Sumitomo Electric Industries, Ltd. |
| 상장 | **TSE Prime `5802`** (Yahoo `5802.T`) ①② |
| 광디바이스 자회사 | Sumitomo Electric Device Innovations (SEDI) — EML·CW-LD 설계/양산 서술 ① [SE IR project v27] |
| InP 기판 | Sumiden Semiconductor Materials · Itami Works ①③ |

⚠ OTC ADR 등 병행 티커는 증권사별로 다르며, 본 도셔의 정본 티커는 **5802.T**.

### 1.2 사업 (CW · 고객 · 점유 클레임)

**제품 구조 (회사 ①)**  
- **EML**: 레이저+EA 변조기 일체. 고속·저전력·차동구동(differential drive) EML 양산 목표.  
- **CW-LD**: 내부 변조기 없음 → 외부 변조(SiPho/외부 EAM 등). 「데이터센터에서 주요 플레이어가 되고 있다」·고출력·저누설·활성층 폭 확대 → **양산 준비 단계**(Aoyama, SEDI) ① [sumitomoelectric.com/id/project/v27/03].  
- **4인치 InP 웨이퍼**: 레이저칩 양산 전환 완료 · 고출력 CW-LD 양산 라인 론칭 서술 ① [v27/04].

**업스트림 InP 기판 (①③)**  
- Nikkei→TrendForce(2026-07-13): InP 기판 CAPEX **약 ¥180억**, FY2028까지 FY2024 대비 **3.1배** 캐파(이전 로드맵은 FY2023 대비 2.4배·2025-11 발표를 상향) ③. JX Advanced Metals와 함께 고순도 광통신용 InP 기판 **지배적 점유**(정량 %는 기사 미기재 → 숫자 기입 금지) ③.  
- 투자 범위는 **InP 기판만**(광섬유·커넥터 증설 제외) ③.

**시장 점유 / 캐파 클레임 (교차)**  

| 클레임 | 내용 | Grade | 출처 |
|---|---|---|---|
| 미즈호 09-14 | CW 점유 **SEI ~32%** · 위안제 ~24% · AVGO ~18% · LITE ~11%; EML: LITE~33%·SEI~22%·AVGO~21%·Mitsubishi~8%·COHR~7% | ③ | `intake/user.jsonl` u-20260914-01 (원문 PDF 미첨부) |
| TrendForce 2026-06-03 | CW-DFB LD **캐파** 선두: **Broadcom·Sumitomo Electric**, 이어 Coherent·LandMark/LuxNet → 합쳐 **~74%** | ③ | trendforce.com press |
| TrendForce 동보 | EML+CW 합산 월캐파 2026 **~50.7M** units(약 2배); top3 AVGO+LITE+SEI **~55%**(합산 시장) | ③ | 동일 |
| COHR ECOC(아카이브) | 「의미 있는 InP 레이저 경쟁사는 한 곳뿐」·중국은 고속 EML·광대역 가변 없고 CW는 **70–100mW** 수준 — open.json이 「그 한 곳 = SEI」[추론]로 읽음 | ③+[추론] | `brain/open.json` cw-laser-leaders |

**고객**  
- 회사 IR 서술: 데이터센터·생성 AI 수요로 광배선·광디바이스·광케이블·InP 증가 ①.  
- TrendForce: NVIDIA/Google/Meta 등이 EML·CW 캐파 락인 ③ — **SEI 개별 고객 리스트·매출 비중은 공시에서 미확인**(이름 발명 금지).

### 1.3 재무 (공개 · FY = 3월 결산)

출처: SE Fact Book FY2025 Result (as of 2026-05-12) · Supplementary · CEO briefing ①.

| 지표 | FY2024 | FY2025 | FY2026E (가이던스) |
|---|---:|---:|---:|
| 연결 매출 | ¥4,679.8B | **¥5,110.2B** (+9.2%) | ¥5,300B |
| 연결 OP | ¥320.7B | **¥418.2B** (+30.4%) | ¥425B |
| 연결 순이익(모회사) | ¥193.8B | **¥369.5B** | ¥320B (가이던스; 특별손익 베이스 주의) |
| **정보통신 매출** | ¥223.3B | **¥326.6B** (+46.3%) | **¥500B** |
| **정보통신 OP** | ¥19.9B | **¥77.4B** | **¥130B** |
| 정보통신 OPM | ~8.9% | **23.7%** | 26% (130/500) |
| 그중 Optical & Electronic Devices | ¥70.7B | **¥95.2B** | **¥139.7B** E |
| Fiber·Cable/Accessories | ¥89.0B | **¥162.5B** | ¥285.3B E |
| Infocomms CAPEX | ¥18.0B | ¥23.7B | **¥72.0B** (연결 CAPEX ¥350B 중) |

ROE FY2025 **14.7%**, ROIC(投下資産 OP) **12.2%** ① Fact Book.

⚠ Optical & Electronic Devices ¥95.2B는 EML+CW+기타 전자디바이스 **합산** — **CW 단독 매출은 미공시**.

### 1.4 밸류에이션 (시세 ②)

| | |
|---|---|
| 종가 | **¥2,080.50** (2026-09-18 TSE 마감) ② Yahoo |
| 시총 | **~¥6.49T** ② |
| Trailing P/E | **~17.6×** (EPS TTM ¥118.38 — 분할 반영된 Yahoo 기준; Fact Book FY2025 EPS ¥473.78은 **분할 전/다른 주수 기준**일 수 있음 → 혼용 금지) ②① |
| Fwd dividend yield | ~1.9% (¥39 / ¥2,080) ② |
| 애널리스트 평균 TP | ~¥3,447 (Yahoo 1y Target Est) ③·집계 |
| 52주 | ¥1,023.75 – ¥3,712.50 ② |

**해석 (발명 없이):** 연결 PER 10대 후반은 「오토와이어 거인」 배수. AI 광 노출은 **정보통신 세그먼트·디바이스 서브라인에 농축**되어 있어, 시총 대비 CW 순수 플레이 배수는 **분리 불가**(sum-of-parts 미공시).

### 1.5 AI-optical vs COHR / LITE

| 축 | SEI | LITE (아카이브·③) | COHR (아카이브·③) |
|---|---|---|---|
| 주력 레이저 | EML+CW · InP 기판 수직 | 고속 EML 점유 내러티브(~50% 고속) · CW는 하위 점유·UHP ELS | 모듈+InP · CW 400mW·6″ epi 전환(TrendForce) |
| 마진 스토리 | Infocomms OPM 23.7%(FY25) — 전사 OPM은 8.2% | GPM 경로 50%초반·OPM 상승 내러티브(미즈호 ③) | 연결 OPM이 Industrial·상각에 눌림(T4) |
| 병목 위치 | **기판+디바이스** 동시 | 디바이스·ELS | 디바이스+조립 |
| CW 캐파(TrendForce ③) | 선두권(AVGO와) | EML top3 · CW는 미즈호 점유 4위 클레임 | CW 캐파 3–4위권 |

### 1.6 리스크

1. **용량 과잉 / ASP**: EML+CW 합산 캐파 급증(TrendForce) → 상용 70–100mW ASP 하락 압력. 미즈호 ASP 밴드($7–9 상용 / $50–75 UHP)는 **③·원문 PDF 없음**.  
2. **중국**: 연결 해외매출 중 China 비중 FY25 **12.5%**(¥640.7B) ① — 광 세그먼트 전용 비중은 미공시. 지정학·고객 디리스킹.  
3. **복합기업 희석**: 자동차 와이어가 매출 과반 → 주가 드라이버가 Infocomms여도 밸류는 자동차 사이클로 흔들림.  
4. **증설 실행**: InP 단결정·인증 사이클 길어 근기 공급 부족 지속 가능(TrendForce ③) — 반대로 실행 지연 시 점유 상실.  
5. **FX**: JPY 실적 · KR 투자자 KRW/JPY.

### 1.7 Edge card (판단 프로토콜 형식)

| field | content |
|---|---|
| **priced_in** | Infocomms 폭증·AI DC 광배선/디바이스가 이미 FY25 실적·FY26 ¥500B/¥130B OP 가이던스에 반영. 시총 ~¥6.5T·연결 PER~18×는 「오토+에너지+광」 번들로 가격됨. 52주 고점(¥3.7k) 대비 현재는 크게 낮음 → 시장이 성장 지속성·자동차 둔화 중 하나를 재가격 중일 수 있음(원인 단정 금지). |
| **variant** | 순수 LITE/COHR 비교가 아니라 **「InP 기판 병목 + CW/EML 디바이스」일본 수직**이 CW 캐파 5배(미즈호 2029E ③) 국면에서 **가장 오래 남는 병목 옵션**. 위안제·대만 epi와 다른 품질/자격 층. |
| **breaks_if** | (a) Optical & Electronic Devices 매출/정보통신 OP가 가이던스 대비 뚜렷한 미스, (b) TrendForce·고객 측에서 SEI CW 캐파 순위가 AVGO·COHR에 지속 밀림이 **복수 소스**로 확인, (c) InP 기판 3.1× 계획이 연기·축소 공시. |

---

## 2. Yuanjie Semiconductor — 源杰科技

### 2.1 티커 · 법인

| | |
|---|---|
| 정식 | 陕西源杰半导体科技股份有限公司 / Yuanjie Semiconductor Technology Co., Ltd. |
| A주 | **SSE STAR `688498`** (Yahoo `688498.SS`) ①② — 사용자 표기 `.SS` 맞음 (`.SH` 동의어) |
| 설립 | 2013-01-28 · Xi’an · InP 광칩(에피→칩 테스트) 수직 ① [en.yj-semitech.com] |
| H주 | 2026-03 홍콩 主板 H주 신청/예비 — **상장 완료·가격 미확인**(신청 단계 보도) ②③ [HKEX filing / 신화·재경 보도] |

### 2.2 사업 (CW · 고객 · 점유 클레임)

**제품 (2025 연보·요약 ①)**  
- DFB/EML: 2.5G–200G PAM4 계열.  
- **CW**: 50/70/100mW급 1310nm · CWDM4/LWDM4 등 — **실리콘광 플러거블 외장 광원**.  
- 2025: **CW 70mW 대량 납품**(데이터센터 주력) · **CW 100mW 배치 납품**.  
- 개발: **300mW CW**(CPO/NPO) · OIO 예비연구 · 100G PAM4 EML 고객 검증 완료 · 200G PAM4 EML 검증 진행 ①.  
- LiDAR: 1550nm InP 칩 라인업 언급 ①.

**매출 믹스 FY2025 ①**  
- 총매출 **RMB 601.43M** (+138.5% YoY).  
- **데이터센터 RMB 393.26M** (+719%) — CW 대량 출하가 주원인.  
- 텔레콤 RMB 206.47M (+2.06%).  
- 순이익 **RMB 190.92M** (2024 −6.13M에서 흑자 전환) · 비경상 제외 RMB 167.22M.

**점유 클레임**  
- 미즈호: CW **~24%**(③, PDF 없음).  
- 회사/홍콩 관련 보도: 灼识咨询 기준 2025 외부매출로 **글로벌 레이저칩 6위 · 실리콘광 고속 광상호연결용 레이저칩 2위** · 「천만 개 단위 CW 양산 가능 소수」 ③ (컨설팅→모집문서 경로 — ① 여부는 홍콩 모집설명서 원문 대조 필요).  
- TrendForce CW **캐파** top 리스트에는 **위안제 미언급** → 미즈호 점유와 **충돌 가능** — 교차 확인 과제.

**고객**  
- 연보: 해외 장비사와 25G/50G PON DFB/EML 배치 납품 · AI DC 「판매 돌파」 서술. **구체 고객명·비중은 공개 요약에서 미확인**.

**증설**  
- 光電通訊 반도체 칩·디바이스 R&D/생산기지 **2기** 투자총액 약 **RMB 12.51억** 공시(보도) ②③.

### 2.3 재무 · 밸류 (②+①)

| | |
|---|---|
| FY2025 매출 / 순이익 | RMB **6.01억 / 1.91억** ① |
| 종가 | **CNY 1,753.10** (2026-09-22 SSE 마감) ② |
| 시총 | **~CNY 218.3B** (~$30B대 — FX는 당일 환율로 환산할 것, 여기 고정 환율 미사용) ② |
| Trailing P/E | **~289×** (EPS TTM 6.07) ② |
| P/S (TTM rev ~1.32B) | 시총/매출 **~165×** 수준(粗算 · ②) — 초고성장 반영 |
| 52주 | 233.10 – 1,968.14 ② |
| Yahoo 1y Target Est 평균 | ~1,573 (현재가 **하회** — 컨센서스 분산·시차 주의) ③집계 |
| 종업원 | ~908 ② |

⚠ 2025년 연간 이익 대비 시총이 매우 큼 → **선행 성장·희소 스토리가 이미 깊게 priced-in**. 분기 가속(2025 Q4 매출 ~2.18억)과 TTM 매출 1.32B는 2026 상반 성장이 반영된 ② 수치.

### 2.4 AI-optical vs COHR / LITE

- **동일 층:** 상용 CW 광원(SiPho 플러거블) — LITE/AVGO/SEI와 경쟁·보완.  
- **출력 층:** 회사 양산은 70–100mW; 300mW는 R&D. COHR·LITE UHP(~400mW / ELS $50–75 ③)와 **같은 칸이 아님**.  
- **마진:** 연보 「데이터센터 제품 마진 > 텔레콤」 정성 ① — **구체 GPM%는 요약본에서 미기재**(본문 PDF 전체 미추출 시 숫자 기입 금지).  
- **지정학:** 중국 공급사 → 미·동맹 hyperscaler 자격·원산지 리스크가 SEI/LITE 대비 큼.

### 2.5 리스크

1. **중국 / 수출통제·고객 디리스킹**  
2. **캐파·수율**: 전사 증설·클린룸; CW는 수율·간접비 이슈(미즈호 ③ 일반론)  
3. **ASP**: 상용 CW 구간에 집중 → 단가 하락에 민감  
4. **밸류에이션 압축**: ~289× TTM — 성장 둔화 한 분기에 배수 붕괴 가능  
5. **H주 희석·이중상장 오버행**(실행 시)  
6. **KR 접근성** (아래 §4)

### 2.6 Edge card

| field | content |
|---|---|
| **priced_in** | AI SiPho CW 70mW 양산·DC 매출 7배+·흑자전환·「중국 CW 스케일」 스토리가 STAR 초고배수(~289×)·시총 ~CNY 218B에 이미 큼. YTD +~300%대(②). |
| **variant** | 미즈호 CW 2위(24% ③)가 **사실**이고 TrendForce 캐파 리스트 누락이 「중국 캐파 저집계」라면, 글로벌 모듈(Inno/Eopto 등) 경로의 **필수 중국 CW 노드**. 반대로 점유가 과대라면 스토리 붕괴. **핵심 과제는 점유 교차검증**. |
| **breaks_if** | (a) DC/CW 매출 QoQ 둔화+가이던스 컷, (b) 100mW/300mW·EML 인증 실패 공시, (c) 미즈호·灼识 점유가 독립 소스와 크게 불일치로 판명, (d) STAR 유동성/규제 충격. |

---

## 3. 기타 CW / InP (약식)

| 이름 | 티커 | 노트 | Grade |
|---|---|---|---|
| **Broadcom** | AVGO | TrendForce: CW-DFB **캐파 공동 선두**; EML top3. SiPho/CPO·OCS 수요측과도 겹침 | ③ |
| **Lumentum** | LITE | EML 강자(고속·OFC 400G/lane 데모 ③). CW는 미즈호 점유 ~11%·UHP/ELS 쪽 | ③ |
| **Coherent** | COHR | CW 캐파 후속 · **6″ InP epi** · **400mW CW-DFB** for SiPho/CPO ③. 모듈 수직. ECOC 「경쟁사 한 곳」 발언은 SEI 지목 [추론] | ③ |
| **LandMark Optoelectronics** | **3081.TWO** (TPEX) | InP/GaAs **에피웨이퍼** · TrendForce가 LuxNet과 묶어 CW 캐파 언급 | ③ |
| **LuxNet** | **4979.TWO** | InP 레이저(CW 포함) · 대만 모듈/칩. TrendForce CW 캐파 4사 묶음 | ③ |
| **Mitsubishi Electric** | 6503.T | EML top3(TrendForce ~72% 중 하나) — **CW 선두 리스트에는 없음** | ③ |
| **JX Advanced Metals** | (비상장 사업부/그룹) | SEI와 InP **기판** 과점 ③ — 디바이스사 아님 |

---

## 4. KR 투자자 접근 · FX · 상장

### 4.1 SEI `5802.T`

- **접근:** 국내 주요 증권사 해외주식(일본)으로 TSE 주문 가능(사별 신청·최소단위·수수료 상이).  
- **FX:** **KRW/JPY** — 엔화 약세 시 원화 환산 수익↑, 강세 시↓. 실적도 JPY.  
- **시간대:** 도쿄 장중 ≈ KST.  
- **세금/결제:** 해외주식 일반 과세·T+2 등 사별. ADR 경로는 유동성·스프레드 확인 필요.  
- **공시 언어:** 일어/영어 IR 양호 ①.

### 4.2 Yuanjie `688498.SS`

- **본토 STAR(커창판):** 한국 개인이 **직접 상해 커창판을 사는 경로는 일반적으로 막혀 있거나 매우 제한적**(증권사·적격 여부·Stock Connect 편입 여부 확인 필수). Stock Connect Northbound는 **적격 A주 유니버스**이며 STAR 전 종목 자동 포함이 아님.  
- **현실적 경로(확인 전제):** ① 홍콩 H주 상장 완료 후 HKEX 주문 ② 운용사/전문 역외 상품 ③(해당 시) Connect 편입 종목만. **2026-09 기준 H주는 신청·예비 단계 보도 — 거래 가능 H주 아님**.  
- **FX:** CNY (또는 H주 시 HKD) ↔ KRW.  
- **유동성·변동성:** 고단가·테마주 · 일일 제한폭·스타보드 규칙.  
- **정보:** 중문 공시 중심 · 영문 IR 제한적.

### 4.3 실무 함의

| | SEI | Yuanjie |
|---|---|---|
| KR 리테일 실행성 | **높음**(일주) | **낮음**(A) / H주 대기 |
| FX | JPY | CNY(/HKD) |
| 공시 추적 | 용이 | 중문·커창 규칙 |
| 포지션 형태 | 직접주 | 상장 전엔 간접·관측만 |

---

## 5. 미확인 · 다음 수집 (judgment 승격용)

1. 미즈호 09-14 **원문 PDF** → CW/EML 점유·ASP·캐파 표 ①/③ 재등급.  
2. TrendForce 유료 리포트 vs 미즈호: **매출 점유 vs 캐파** 정의 정렬.  
3. SE Optical & Electronic Devices 내 **EML vs CW 매출 분해**(IR Q&A·세그먼트 노트).  
4. 위안제 2025 연보 **전문 PDF** → 고객 집중도·GPM·수출 비중.  
5. 위안제 **HKEX 모집설명서** 灼识 점유 표 원문.  
6. LandMark/LuxNet 최근 분기 CW 출하 코멘트.  
7. 시세 재스냅샷(SEI 09-18 · 위안제 09-22) — merge 시 당일 ②로 갱신.

---

## 6. 소스 목록 (라벨)

| ID | 문서 | Grade |
|---|---|---|
| S1 | Sumitomo Electric Fact Book FY2025 Result (2026-05-12) | ① |
| S2 | SE Supplementary FY2025 / CEO 20260522 실적·가이던스 | ① |
| S3 | SE 「Evolving AI Infrastructure…」 v27/03–04 (SEDI EML·CW·4″) | ① |
| S4 | TrendForce 2026-06-03 EML/CW capacity press | ③ |
| S5 | TrendForce/Nikkei 2026-07-13 InP ¥18B · 3.1× | ③ |
| S6 | Yahoo Finance 5802.T (2026-09-18 close) | ② |
| S7 | 源杰 2025 연보·연보요약 (cninfo / 상증보 2026-03-25) | ① |
| S8 | 財联社·新浪 등 2025실적·H주·시총 보도 (2026-03) | ②③ |
| S9 | Yahoo Finance 688498.SS (2026-09-22 close) | ② |
| S10 | Yuanjie EN company profile (yj-semitech) | ① |
| S11 | Mizuho laser-chip note via `u-20260914-01` | ③ |
| S12 | `brain/open.json` cw-laser-leaders · optical_valuechain_9 T2–T5 | archive |
| S13 | LuxNet 4979.TWO / LandMark 3081.TWO 공개 프로필·보도 | ②③ |

---

## 7. Parent merge용 초압축 요약

- **Gap `cw-laser-leaders`:** 도셔 작성 완료 → 판단문은 parent가 edge card로 승격.  
- **SEI 5802.T:** Infocomms FY25 ¥327B/OP ¥77B → FY26E ¥500B/¥130B; Devices ¥95B→¥140B E; CW 양산·4″·InP 3.1×; 시총 ~¥6.5T · P/E~18× (09-18). KR 접근 OK · JPY.  
- **Yuanjie 688498.SS:** FY25 매출 6.01억·순익 1.91억 · DC 3.93억(+719%) · CW70 양산/100 배치; 시총 ~CNY 218B · P/E~289× (09-22). H주 미상장 · KR 직접 매매 난.  
- **Peers:** AVGO·SEI CW 캐파 선두(TF) · COHR 400mW/6″ · LandMark 3081 + LuxNet 4979 · LITE EML.  
- **충돌:** 미즈호 CW 점유(SEI32/위안제24) vs TrendForce 캐파 리스트(위안제 없음) — **미해결**.  
- **Edge:** SEI=기판+디바이스 병목 옵션(복합기업 희석) / 위안제=스케일·배수·중국·접근 삼중 리스크. breaks_if는 §1.7·§2.6.
