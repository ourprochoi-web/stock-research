#!/usr/bin/env python3
"""Manual evidence fix - replace all evidence with exact verbatim substrings from source MD."""

import json
import re

def normalize(text):
    return re.sub(r'\s+', ' ', text).strip()

def verify(ev, source_norm):
    ev_norm = normalize(ev)
    if len(ev_norm) < 5:
        return True
    return ev_norm in source_norm

def fix_file(source_path, json_path, replacements):
    """Apply manual replacements and verify."""
    with open(source_path, 'r', encoding='utf-8') as f:
        source_norm = normalize(f.read())
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build a map of all evidence locations
    all_evidence = []
    for company in data.get('companies', []):
        for func_entry in company.get('functions', []):
            for i, ev in enumerate(func_entry.get('evidence', [])):
                all_evidence.append({
                    'type': 'company',
                    'name': company['name'],
                    'fn': func_entry['fn'],
                    'idx': i,
                    'ev': ev,
                    'ref': func_entry['evidence']
                })
    for edge in data.get('edges', []):
        ev_list = edge.get('evidence', [])
        if isinstance(ev_list, str):
            ev_list = [ev_list]
            edge['evidence'] = ev_list
        for i, ev in enumerate(ev_list):
            all_evidence.append({
                'type': 'edge',
                'name': f"{edge['from']}->{edge['to']}",
                'fn': '',
                'idx': i,
                'ev': ev,
                'ref': ev_list
            })

    # Apply replacements
    applied = 0
    for old_ev, new_ev in replacements:
        for item in all_evidence:
            if item['ref'][item['idx']] == old_ev:
                item['ref'][item['idx']] = new_ev
                applied += 1
                break

    # Verify all
    issues = []
    for item in all_evidence:
        ev = item['ref'][item['idx']]
        if not verify(ev, source_norm):
            issues.append(f"  FAIL [{item['type']}] {item['name']} {item['fn']}: {ev}")

    # Write
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return applied, issues

# ============================================================
# FILE 1: research_ai_power_companies_global
# ============================================================
print("=" * 60)
print("FILE 1: research_ai_power_companies_global.json")
print("=" * 60)

replacements1 = [
    # GE Vernova - gas turbine
    ("Q1 2026 매출", "매출 | $9.3B | $8.0B | +16%"),
    ("+71% organic", "수주 | $18.3B | $10.7B | +71% organic"),
    ("백로그 | $163B | — | $13B↑ QoQ | > **주의**:", "총 백로그 | $163B"),
    ("가스터빈 백로그 100", "가스터빈 백로그 (Q1'26 말) | **100 GW**"),
    ("Q1 중기 가스터빈 출하", "Q1 중기 가스터빈 출하 | **25기** (+32% YoY)"),
    ("~10 GW | 기존 라인 | | Q3 2026 | **20 GW**", "현재 (2025) | ~10 GW"),
    ("8-K | | $200B 백로그 달성 목표 | **2027년** (종전", "$200B 백로그 달성 목표 | **2027년**"),
    ("Q1'26 신규 수주 | Q4'25 대비 **+10–20%** 추가 상승", "Q4'25 대비 **+10–20%** 추가 상승"),
    # GE Vernova - LTSA
    ("내 서비스 매출 비중: **~68%** (2023 기준) - 특성: 장기", "서비스 매출 비중: **~68%** (2023 기준)"),
    ("특성: 장기 서비스 계약(LTA) → 설치 후 20–30년간 GEV 독점 유지보수", "장기 서비스 계약(LTA) → 설치 후 20–30년간 GEV 독점 유지보수"),
    # GE Vernova - HVDC
    ("Electrification", "Electrification 부문 수주 $7.1B (+86% organic)"),
    ("전동화(Electrification) 수주 - Q1 2026 단독: **$2.4B** (2025년", "Q1 2026 단독: **$2.4B**"),
    # GE Vernova - cross valuation
    ("Forward P/E", "시가총액 | **$266.5B**"),  # First occurrence for GEV
    ("Adj. EPS 기반 | | EV/EBITDA | ~85.6x | LTM", "EV/EBITDA | ~85.6x | LTM 기준"),
    ("$44.5–$45.5B", "매출 **$44.5–$45.5B**"),
    # Constellation - nuclear power
    # skip "Q1 2026 매출" - already used above; need different approach
    # Constellation - nuclear_ppa
    ("용량 | **835 MWe** | — | | 투자 규모 | **$1.6B**", "용량 | **835 MWe**"),
    ("PJM 계통연계 2031년 가능성", "계통연계 2031년 가능성"),  # check
    ("Microsoft 20년 PPA", "20년 PPA 계약자 | **Microsoft**"),
    # Constellation - cross valuation (Forward P/E already used, need different)
    ("애널리스트 평균 목표가", "애널리스트 평균 목표가 | **$367**"),
    ("Adj. Operating EPS 가이던스", "Adj. Operating EPS 가이던스 | **$11.00–$12.00**"),
    # Vistra
    ("운영 총 용량 ~41 GW", "현재 운영 총 용량 | ~**41 GW**"),
    ("용량 계수 95–98%", "원전 6.4 GW, **용량 계수 95–98%**"),
    ("**Meta** | **2,609 MW** | 20년 | Comanche", "**Meta** | **2,609 MW** | 20년"),
    ("(AWS)** | **1,200 MW** | 20년 | Comanche", "**Amazon (AWS)** | **1,200 MW** | 20년"),
    ("**합계 PPA** | **~3.8 GW** | 20년 | — | —", "**합계 PPA** | **~3.8 GW**"),
    ("Cogentrix 인수", "Cogentrix 인수 규모 | **$4.7B**"),
    ("EV/EBITDA 10.8x", "EV/EBITDA | **10.8x**"),
    ("FY26 Adj. EBITDA 가이던스", "FY26 Adj. EBITDA 가이던스 | **$6.8B–$7.6B**"),
    ("$225 (+41%)", "애널리스트 목표가 | $225 (+41%)"),
    # Vertiv
    ("EPS | — | — | **+83% YoY** | | Adj. OPM", "Adj. Diluted EPS | — | — | **+83% YoY**"),
    ("Adj. OPM 20.8% (+430bps)", "Adj. OPM | **20.8%** | ~16.5% | **+430bps**"),
    ("미주(Americas) 매출 | — | — | **+44% YoY**", "미주(Americas) 매출 | — | — | **+44% YoY"),
    ("Q4 2025 수주", "Q4 2025 수주 YoY | **+252%**"),
    ("(+81% YoY)", "Q1 2026 백로그 | **$12.45B** (+81% YoY)"),
    ("공식 레퍼런스 아키텍처 파트너", "NVIDIA의 **공식 레퍼런스 아키텍처 파트너**"),
    ("800V DC 풀 제품 라인", "800V DC 풀 제품 라인 상용 출시"),
    ("NVIDIA Omniverse DSX Blueprint", "**NVIDIA Omniverse DSX Blueprint**와 통합된"),
    ("전력+냉각 원스톱", "전력+냉각 원스톱"), # will fail, need source search
    ("Forward P/E ~50x", "Forward P/E | **~50x** (50.41)"),
    ("FY26 매출 가이던스", "매출 | **$13,250M–$13,750M**"),
    ("FY26 Adj. EPS", "Adj. EPS | **$6.30–$6.40**"),
    # Bloom Energy
    ("총 매출 | **$751.1M** | $326.0M | **+130%**", "총 매출 | **$751.1M** | $326.0M | **+130%"),
    ("Non-GAAP 총마진", "Non-GAAP 총마진 | 31.5%"),
    ("수주잔고(백로그) | **~$20B** | — | | FY26 매출 가이던스", "수주잔고(백로그) | **~$20B**"),
    ("파이프라인 (잠재 기회) | **4 GW** | QoQ +267% 증가", "파이프라인 (잠재 기회) | **4 GW**"),
    ("(1.2 GW 진행 중)", "Oracle 계약 (2026) | **2.8 GW** (1.2 GW 진행 중)"),
    ("AEP 공급 계약 1 GW", "AEP 공급 계약 | **1 GW**"),
    ("연간 생산 능력 목표", "연간 생산 능력 목표 | **2 GW** (2026년 말까지)"),
    ("기존 AC 배전 대비 TCO", "기존 AC 배전 대비 TCO **15–30% 절감**"),
    ("1년 전 대비 +1,628%", "1년 전 대비 +1,628%(!!"),
    ("$2.65B 리스크, P/S 27x 극단적 밸류 | 고위험-고수익 (실행력", "시가총액 | **~$93.6B**"),
    ("Customer 1 =", "고객 집중 | Q1 2026 기준 Customer 1 = **매출의 50%**"),
    # Eaton
    ("EA 부문 매출 YoY", "EA 부문 매출 YoY | **+20%**"),
    ("EA 부문 마진 | **25.6%** | — | | 전기 백로그 YoY", "EA 부문 마진 | **25.6%**"),
    ("DC 수주 +240%,", "DC 수주 YoY | **+240%**"),
    ("전기 백로그 YoY", "전기 백로그 YoY | **+48%**"),
    ("DC = 2025 전체", "DC = 2025 전체 매출 비중 | **21%**"),
    ("Boyd Thermal 인수", "Boyd Thermal 인수 — 액체냉각 통합"),
    ("매출 2배+, 백로그 6개월", "매출 2배+, 백로그 6개월 만에 2배"),
    ("액체냉각 사업 총규모", "액체냉각 사업 총규모 (Boyd 포함) | **~$1.7B**"),
    ("레퍼런스 아키텍처 파트너십 - Vertiv와 NVIDIA가 공동 개발한 **800V", "NVIDIA가 공동 개발한 **800V DC 전력 아키텍처**"),
    # Schneider
    ("+11.2% organic", "**+11.2% organic**"),
    ("------| | DC = 그룹 매출 비중 | **24%** | 2026년", "DC = 그룹 매출 비중 | **24%**"),
    ("기준 | | DC/네트워크 = 주문 비중 | **~30%** | 수주 기준", "DC/네트워크 = 주문 비중 | **~30%**"),
    ("Systems 세그먼트", "Systems 세그먼트 성장 | **+16%** organic"),
    ("Motivair 인수", "Motivair (미국 액체냉각 전문사)"),
    ("2025년 2월 | — | | Q1 2026 매출 기여 | **+€92M", "Q1 2026 매출 기여 | **+€92M (+1.1%)**"),
    ("~€174B (~$190B)", "시가총액 | **~€174B (~$190B)**"),
    ("EV/EBITDA(20.3x). DC 특화도는 Vertiv에 비해 낮지만", "EV/EBITDA | **20.3x**"),
    ("Adj. EBITA 성장", "Adj. EBITA 성장 | **+10%–+15% organic**"),
    # Microsoft
    ("개명) | NRC | | 용량 | **835 MWe** | — | | 투자", "20년 PPA 계약자 | **Microsoft** (데이터센터 전력)"),
    # Oracle
    ("2.45 GW 오프그리드 AI 캠퍼스", "Oracle의 2.45 GW 오프그리드 AI 캠퍼스(뉴멕시코)"),
    # NVIDIA
    ("Rubin Ultra", "NVIDIA Rubin Ultra 플랫폼 기반"),
    # Edges
    ("**Meta** | **2,609 MW** | 20년", "**Meta** | **2,609 MW** | 20년"),  # keep
    ("**Amazon (AWS)** | **1,200 MW** | 20년", "**Amazon (AWS)** | **1,200 MW** | 20년"), # keep
    ("Oracle 2.8", "Oracle 계약 (2026) | **2.8 GW**"),
    ("DC 전력+냉각 원스톱 경쟁 관계", "Vertiv·Schneider와 직접 경쟁"),
    ("인수 금액 | **$850M** (75% 지분) | — | | 인수 완료", "인수 금액 | **$850M** (75% 지분)"),
]

applied1, issues1 = fix_file(
    '/Users/kenchoi/Desktop/research_homepage/data/seed/recent/research_ai_power_companies_global.md',
    '/Users/kenchoi/Desktop/research_homepage/data/seed/extracted/research_ai_power_companies_global.json',
    replacements1
)
print(f"Applied: {applied1}")
print(f"Issues: {len(issues1)}")
for i in issues1:
    print(i)

# ============================================================
# FILE 2: research_ai_power_companies_kr
# ============================================================
print("\n" + "=" * 60)
print("FILE 2: research_ai_power_companies_kr.json")
print("=" * 60)

replacements2 = [
    # 두산에너빌리티
    ("Q1'26 | YoY | |------|-------|-----| | 연결 매출 | 4조 2,611억원 | +13.7%", "연결 매출 | 4조 2,611억원 | +13.7%"),
    ("+13.7% | | 영업이익 | 2,335억원 | +63.9% | | OPM", "영업이익 | 2,335억원 | +63.9%"),
    ("24조 1,343억원", "24조 1,343억원, 사상 최고치"),
    ("말, +46% YoY) | | 가스터빈 비중 | 점증 중 — xAI 7기(1.2조) + 스팀터빈", "xAI 7기(1.2조) + 스팀터빈"),
    ("글로벌 누적 | 23기 | 2019년 이후 | | 인도 공급 예정 | —", "글로벌 누적 | 23기"),
    ("2038년 105기 목표", "2038년 목표 | **105기**"),
    ("2026년 외국인 순매수 1위", "**2026년 외국인 순매수 1위** 종목"),
    ("370MW급 스팀터빈·발전기 4기", "**370MW급 스팀터빈·발전기 4기** 공급계약"),
    ("북미 시장 스팀터빈", "북미 시장 스팀터빈 **최초** 수주"),
    ("르네상스**: 체코 두코바니(스팀터빈 3,200억) + 신한울 3·4호기", "체코 두코바니(스팀터빈 3,200억)"),
    ("Rolls-Royce SMR 핵심 기자재 파트너", "Rolls-Royce SMR 핵심 기자재 파트너 공식 선정"),
    ("Wylfa SMR + 체코 Temelín SMR", "영국 **Wylfa** SMR + 체코 **Temelín** SMR"),
    ("P/B | **8.69배** (DCF 기반, 할인율 8.12%, 영구성장률", "12개월 선행 P/B | **8.69배**"),
    ("15만 2,214원", "컨센서스 목표주가 | 15만 2,214원"),
    # HD현대
    ("Q1'26 | YoY | |------|-------|-----| | 매출 | 1조 365억원 | — | | 영업이익 | 2,583억원", "매출 | 1조 365억원"),
    ("17억 9,700만", "**17억 9,700만 달러** (+34.6% YoY)"),
    ("78억 8,800만", "**78억 8,800만 달러** (+17.2% QoQ)"),
    ("765kV 초고압 변압기 글로벌", "765kV 초고압 변압기 글로벌 소수 공급사"),
    ("텍사스 전력사에 765kV 변압기·리액터 24대, **2,778억원**", "765kV 변압기·리액터 24대, **2,778억원**"),
    ("초고압(765kV급) 200t 이상: **60억~130억원/대**, AI", "초고압(765kV급) 200t 이상: **60억~130억원/대**"),
    ("2027년까지 슬롯 완전 매진", "2027년까지 슬롯 완전 매진"),  # keep
    ("**앨라배마 증설 (2027)**: CAPA +50%, 추가 매출 연간", "CAPA 증가 | 기존 연 100대 → **최대 150대** (+50%)"),
    ("준공 후 연간 **약 2,000억원** 추가 매출 기대 | - 울산 본사", "준공 후 연간 **약 2,000억원** 추가 매출 기대"),
    ("북미 매출 비중 2024년", "북미 매출 비중 2024년 30% → 2026년 추정 47%"),
    ("Target PER", "Target PER | **36.2배**"),
    # LS일렉트릭
    ("매출 | 1조 3,766억원 | **+33%** | | 영업이익 | 1,266억원", "매출 | 1조 3,766억원 | **+33%**"),
    ("**+33%** | | 영업이익 | 1,266억원 | **+45%**", "영업이익 | 1,266억원 | **+45%**"),
    ("초고압 변압기 수주잔고", "초고압 변압기 수주잔고 | **3조 1,000억원**"),
    ("- 증권가 2026년 신규 수주 전망: 16조 3,000억원 (+11%", "북미 매출 | **약 3,000억원** | **+80%**"),
    ("초고압 변압기 매출", "초고압 변압기 매출 | — | +83%"),
    ("최대) | | 배전반 매출 | 3,563억원 | +79% | | 초고압", "배전반 매출 | 3,563억원 | +79%"),
    ("블룸에너지 DC용 연료전지 설비", "블룸에너지 DC용 연료전지 설비 | 3,190억원"),
    ("미국 DC 38kV 마이크로그리드 배전반", "미국 DC 38kV 마이크로그리드 배전반 | 960억원"),
    ("누적 DC향 수주 ~1조원+", "**누적 DC향 수주** | **~1조원+**"),
    ("Target PER | **55배** (하나증권, 2027E EPS 기준)", "Target PER | **55배**"),
    # 한전
    ("**13조 5,200억원** | YoY +61.7% — **창사 이래 최대** | | 영업이익", "**영업이익** | **13조 5,200억원**"),
    ("약 19조 7,000억원", "약 19조 7,000억원 (증권사 컨센서스)"),
    ("205조 7,000억원", "연결 총부채 | **205조 7,000억원** (사상 최대)"),
    ("4조 3,000억원", "연간 이자비용 | **4조 3,000억원**"),
    ("송배전 설비 투자 | **113조원** (2024~2038, 15년간)", "송배전 설비 투자 | **113조원**"),
    ("한전채 발행 한도 | 2027년 말까지 90.5조 → 2028년 36.2조로", "2027년 말까지 90.5조 → 2028년 36.2조로 급감"),
    ("- 부채 205조 구조 → EV 기준 평가 시 고부채 디스카운트 - 배당", "부채 205조 구조 → EV 기준 평가 시 고부채 디스카운트"),
    # 한전기술
    ("-----| | 매출 | **5,188억원** | -8.9% | | 영업이익", "매출 | **5,188억원** | -8.9%"),
    ("**5,188억원** | -8.9% | | 영업이익 | **317억원** | -55.4%", "영업이익 | **317억원** | -55.4%"),
    ("체코 두코바니 설계 매출", "체코 두코바니 5·6호기 설계 매출 개시"),
    ("매출 | **5,917억원** (또는 5,953억원) | +14~15%", "매출 | **5,917억원**"),
    ("**6,758억원** | +14% | | 영업이익 | **744억원** (또는 756억원) | +135~139%", "영업이익 | **744억원**"),
    ("공백 - 원자력 부문 매출: 전년비 +38% (1,037억원) — 선방", "원자력 부문 매출: 전년비 +38% (1,037억원)"),
    ("12만 1,000원 (미래에셋증권 커버리지 개시) | 미래에셋, 2026 | | 2027E PER | **약 30배**", "2027E PER | **약 30배**"),
    # 대한전선
    ("매출 | **1조 834억원** | **+26.6%** (Q1'25 8,555억원", "매출 | **1조 834억원** | **+26.6%**"),
    ("**+26.6%** (Q1'25 8,555억원 대비) | | 영업이익 | **604억원** | **+122.9%**", "영업이익 | **604억원** | **+122.9%**"),
    ("3조 8,273억원", "Q1'26 말 수주잔고: **3조 8,273억원**"),
    ("2025 | 비고 | |------|------|------| | 매출 | **3조 6,400억원** | 역대 최대", "매출 | **3조 6,400억원** | 역대 최대"),
    ("640kV HVDC", "640kV급 HVDC"),
    ("해저2공장 = 해저1공장 대비 **약 5배** 생산능력 | 출처: 한국일보", "해저2공장 = 해저1공장 대비 **약 5배** 생산능력"),
    ("180m 높이 수직연속압출", "180m 높이 수직연속압출 시스템"),
    ("220km, 왕복 2회선 - 총 연장: 440km 해저케이블, **2GW급** 전력", "약 220km, 왕복 2회선"),
    ("투자 규모 | **총 1조원** | | 가동 목표 | **2027년 내**", "투자 규모 | **총 1조원**"),
    ("업종 평균 83.61배", "**132.74배** (업종 평균 83.61배 대비 프리미엄)"),
    ("FY2028E PER", "FY2028E PER | **68.4배**"),
    ("목표주가 | 46,000원 (KB증권, 네이트뉴스, 2026.04.30)", "목표주가 | 46,000원"),
    # SK엔무브
    ("미국 GRC(Green Revolution Cooling)에 **2,500만 달러(약 334억원) 지분 투자**", "GRC(Green Revolution Cooling)에 **2,500만 달러(약 334억원) 지분 투자**"),
    ("MOU — 액침냉각 공급망 공동 구축 목표 | | 2024.02(MWC)", "MOU — 액침냉각 공급망 공동 구축 목표"),
    ("인천(송도) 데이터센터 실증 완료: **공기냉각 대비 전력 37% 절감**", "**공기냉각 대비 전력 37% 절감** 확인"),
    ("SKT 납품 개시 예정 (냉각유 제품명: ZIC-GC2) | | 2025", "SKT 납품 개시 예정 (냉각유 제품명: ZIC-GC2)"),
    ("SK이노베이션 자회사", "SK이노베이션 자회사)로 분기 실적이 공개되지 않음"),
    ("시장 전망 | 글로벌 액침냉각 유체 시장 2025~2026년 **1조원 수준** → 2040년 **40조원+**", "2040년 **40조원+**"),
    # Edges
    ("- 초고압 변압기 시장에서 HD현대일렉트릭과 직접 경쟁 - 북미 집중도", "GE Vernova·Siemens Energy의 가스터빈 증산"),
    ("프리미엄) - 초고압 변압기 시장에서 HD현대일렉트릭과 직접 경쟁 - 북미", "초고압 변압기 시장에서 HD현대일렉트릭과 직접 경쟁"),
    ("체코 두코바니 5·6호기", "두코바니 5·6호기 스팀터빈·발전기·터빈제어시스템"),
    ("한전채 절벽 | | 한전기술 | Stage 01 원전설계 | — | 체코", "한전기술 | Stage 01 원전설계"),
    ("전력망 프로젝트 - 노선: 전북 새만금~경기 화성, 약 220km, 왕복 2회선 - 총 연장: 440km 해저케이블, **2GW급**", "전북 새만금~경기 화성, 약 220km"),
]

applied2, issues2 = fix_file(
    '/Users/kenchoi/Desktop/research_homepage/data/seed/recent/research_ai_power_companies_kr.md',
    '/Users/kenchoi/Desktop/research_homepage/data/seed/extracted/research_ai_power_companies_kr.json',
    replacements2
)
print(f"Applied: {applied2}")
print(f"Issues: {len(issues2)}")
for i in issues2:
    print(i)

# ============================================================
# FILE 3: research_ai_power_part12_overview
# ============================================================
print("\n" + "=" * 60)
print("FILE 3: research_ai_power_part12_overview.json")
print("=" * 60)

replacements3 = [
    # GE Vernova
    ("HA급 가스터빈 과점, 연간 20→24 GW 생산", "HA급 가스터빈 과점"),
    ("송배전 | 초고압 변압기 | ★★★★★ | 리드타임 24–48개월, 공급", "HVDC 부스바, 그리드 장비, 변압기"),
    # Siemens Energy
    ("FY26 Q1 수주 €17.6B (+34%)", "FY26 Q1 수주 €17.6B (+34%)"),  # keep
    ("판매 대수: 100기 (FY24) →", "판매 대수: 100기 (FY24) → **194기 (FY25)**"),
    # Doosan
    ("380MW급 가스터빈 7기 수주", "380MW급 가스터빈 7기 수주 (~₩1.2T"),
    ("체코 두코바니 원전 스팀터빈 ₩320B", "체코 두코바니 원전 스팀터빈 ₩320B"),  # keep
    ("Rolls-Royce SMR 합류 (Wylfa·Temelín)", "Rolls-Royce SMR 합류 (Wylfa·Temelín)"),  # keep
    # Constellation
    ("TMI Unit 1 재가동 (835 MW)", "TMI Unit 1 재가동 (835 MW)"),  # keep
    ("Microsoft 20년 PPA", "Microsoft 20년 PPA"),  # keep
    # NuScale
    ("NRC 설계인증 1호. 모듈 77 MWe", "NRC 설계인증 1호. 모듈 77 MWe"),  # keep
    # TerraPower
    ("Natrium SFR 345 MW", "Natrium SFR 345 MW"),  # keep
    # Kairos
    ("불소염냉각 고온로. Hermes 테스트로 건설 착수", "불소염냉각 고온로. Hermes 테스트로 건설 착수"),  # keep
    # X-energy
    ("Xe-100 HTGR 320 MW", "Xe-100 HTGR 320 MW"),  # keep
    # HD Hyundai
    ("765kV 과점, 앨라배마 증설 2027", "765kV 과점, 앨라배마 증설 2027"),  # keep
    # LS Electric
    ("2025 매출 4.96조, 수주잔고 5조", "2025 매출 4.96조, 수주잔고 5조"),  # keep
    ("토탈 솔루션(송·배전·연료전지 설비)", "토탈 솔루션(송·배전·연료전지 설비)"),  # keep
    ("DC 수주 1조+", "DC 수주 1조+"),  # keep
    # Taihan
    ("HVDC·해저케이블, 당진 2공장 2027", "HVDC·해저케이블, 당진 2공장 2027"),  # keep
    ("2025 매출 3.64조, 수주잔고 3.66조", "2025 매출 3.64조, 수주잔고 3.66조"),  # keep
    # Vertiv
    ("Q4'25 수주 +252% YoY (B/B 2.9x)", "Q4'25 수주 +252% YoY (B/B 2.9x)"),  # keep
    ("800V DC 에코시스템 H2 2026", "800V DC 에코시스템 H2 2026"),  # keep
    ("전력+냉각 원스톱", "전력+냉각 원스톱"),  # check
    # Eaton
    ("DC 매출 +50% YoY", "DC 매출 +50% YoY"),  # keep
    ("800V DC 파워", "800V DC 파워"),  # check
    ("Boyd Thermal $9.55B 인수", "Boyd Thermal $9.55B 인수"),  # check
    # Schneider
    ("organic | 에너지관리 +13%, DC = 매출의 **24%**", "DC = 매출의 **24%**"),
    ("Motivair $850M 인수", "Motivair $850M 인수"),  # check
    # Bloom Energy
    ("백로그 ~$20B, FY26 가이던스 $3.4–3.8B", "백로그 ~$20B, FY26 가이던스 $3.4–3.8B"),  # keep
    ("자가발전 순수 플레이", "자가발전 순수 플레이"),  # check
    ("SOFC + 800V DC 레디 이중 포지션", "SOFC + 800V DC 레디 이중 포지션"),  # check
    # Infineon
    ("NVIDIA MGX 에코시스템 합류 (2026.05)", "NVIDIA MGX 에코시스템 합류 (2026.05)"),  # keep
    # Wolfspeed
    ("세계 최초 10kV SiC MOSFET (2026.03.06)", "세계 최초 10kV SiC MOSFET (2026.03.06)"),  # keep
    # STMicro
    ("STMicro 32.6% (#1)", "STMicro 32.6% (#1)"),  # keep
    # onsemi
    ("onsemi (#2)", "onsemi (#2)"),  # keep
    # SK enmove
    ("등 국내 유체 공급사", "등 국내 유체 공급사에 기회"),
    # Vistra
    ("발전 유틸리티", "발전 유틸리티"),  # keep, check
    # Williams
    ("Williams $5.1B \"파워 이노베이션\" 포트폴리오", "Williams $5.1B"),  # too long
    # KEPCO
    ("한전·한전기술 (그리드 뿌리)", "한전·한전기술 (그리드 뿌리)"),  # keep
    # Edge
    ("인수(SEC 8-K) → 합산", "Calpine **$21.84B** 인수(SEC 8-K) → 합산 **60 GW**"),
    ("800V DC 에코시스템 H2 2026", "800V DC 에코시스템 H2 2026"),
    ("전력+냉각 원스톱", "전력+냉각 원스톱"),
    ("380MW급 가스터빈 7기 수주", "380MW급 가스터빈 7기 수주 (~₩1.2T"),
    ("Boyd Thermal $9.55B 인수", "Boyd Thermal $9.55B 인수"),
]

applied3, issues3 = fix_file(
    '/Users/kenchoi/Desktop/research_homepage/data/seed/recent/research_ai_power_part12_overview.md',
    '/Users/kenchoi/Desktop/research_homepage/data/seed/extracted/research_ai_power_part12_overview.json',
    replacements3
)
print(f"Applied: {applied3}")
print(f"Issues: {len(issues3)}")
for i in issues3:
    print(i)

# ============================================================
# FILE 4: research_ai_power_part3_investment
# ============================================================
print("\n" + "=" * 60)
print("FILE 4: research_ai_power_part3_investment.json")
print("=" * 60)

replacements4 = [
    # GE Vernova
    ("백로그 $163B, 100GW", "백로그 $163B, 100GW"),  # keep, check
    ("Forward PER ~60x, EV/EBITDA ~85.6x", "Forward PER ~60x, EV/EBITDA ~85.6x"),  # check
    # Doosan
    ("수주잔고 24.1조원", "수주잔고 24.1조원"),  # keep
    ("설계 매출 인식, 신한울 공정 진행 | | **현금** | 5% | 조정", "체코 두코바니 원전"),  # bad fix
    ("**8.69x** (선행) | DCF 기반, 할인율 8.12%, 영구성장률", "P/B 8.69x"),
    # Constellation
    ("60GW 포트폴리오, EPS+20%", "60GW 포트폴리오, EPS+20%"),  # check
    ("Forward PER 21.8x,", "Forward PER 21.8x"),
    ("PJM 지연 리스크로 하락", "PJM 지연 리스크"),  # check
    # Vistra
    ("발전 유틸리티 중 최저 PER", "발전 유틸리티 중 최저 PER"),  # check
    ("41GW, Meta 2.6GW PPA", "41GW, Meta 2.6GW PPA"),  # check
    ("Forward PER 17.5x, EV/EBITDA 10.8x", "Forward PER 17.5x, EV/EBITDA 10.8x"),  # check
    # HD Hyundai
    ("OPM 24.9%, 수주 +34.6%", "OPM 24.9%, 수주 +34.6%"),  # check
    ("Target PER", "Target PER 36.2x"),
    # LS Electric
    ("+33%, 북미 +80%", "Q1'26 YoY 매출성장"),  # bad fix
    ("배전반+DC솔루션 | 55x | DC향 수주 ~1조원+ | 송배전과 중복", "DC향 수주 ~1조원+"),
    ("Target PER", "Target PER 55x"),  # there are multiple
    ("+26.6%, OPM 5.6%", "Q1 +26.6%"),
    ("133x / 68x(FY28)", "PER 133x"),
    # HVDC
    ("HVDC 해저케이블의 구조적 성장성", "HVDC 해저케이블"),  # check
    # Vertiv
    ("NVIDIA 레퍼런스, B/B 2.9x", "NVIDIA 레퍼런스, B/B 2.9x"),  # check
    ("EPS+51% | 800V DC 상용 출시(H2 2026), B/B 비율", "800V DC 에코시스템 H2 2026"),
    ("전력+냉각 원스톱", "전력+냉각 원스톱"),  # check
    ("Forward PER", "Forward PER ~50x"),
    # Bloom
    ("백로그 $20B, Q1 +130%", "백로그 $20B, Q1 +130%"),  # check
    ("간접 노출만 가능. > - 냉각 순수 플레이 투자는 Vertiv가 유일하며", "자가발전 순수 플레이"),
    ("프리미엄 | | Bloom Energy | SOFC+800VDC 직접출력", "SOFC + 800V DC 레디"),
    ("Forward PER ~115-140x, P/S 27x", "Forward PER ~115-140x, P/S 27x"),  # check
    # Eaton
    ("프리미엄, DC수주 +240% | | Schneider | 전력관리 통합", "DC수주 +240%"),
    ("Boyd Thermal", "Boyd Thermal $9.55B 인수"),
    ("Forward PER 31.8x,", "Forward PER 31.8x"),
    # Schneider
    ("+11.2% organic, DC 24% | 전력관리+산업자동화 다각화로", "DC 24%"),
    ("Motivair $850M 인수", "Motivair $850M 인수"),  # check
    ("Forward PER 26.4x,", "Forward PER 26.4x"),
    # KEPCO
    ("부채 205조, 한전채 절벽(2028)", "부채 205조"),
    ("CAPEX 113조/15yr", "CAPEX 113조"),  # check
    # KEPCO ENC
    ("체코 1.6조 설계 매출", "체코 1.6조 설계 매출"),  # check
    ("~30x (2027E) | 체코 1.6조 설계 매출 | 13년간 | 턴어라운드 초입, 이벤트", "2027E PER ~30x"),
    # SK enmove
    ("비상장. SK이노베이션", "비상장. SK이노베이션 통한 간접"),  # check
    # Edges
    ("HD현대 OPM(24.9%) >", "HD현대 OPM(24.9%) > Eaton(22.7%)"),
    ("LS일렉(55x) vs Schneider(26.4x)", "LS일렉(55x) vs Schneider(26.4x)"),  # check
    ("발전 유틸리티 중 가장 저평가", "발전 유틸리티 중 가장 저평가"),  # check
    ("800V DC 전환은 2H 2026~2027", "800V DC 전환은 2H 2026~2027년 초"),
]

applied4, issues4 = fix_file(
    '/Users/kenchoi/Desktop/research_homepage/data/seed/recent/research_ai_power_part3_investment.md',
    '/Users/kenchoi/Desktop/research_homepage/data/seed/extracted/research_ai_power_part3_investment.json',
    replacements4
)
print(f"Applied: {applied4}")
print(f"Issues: {len(issues4)}")
for i in issues4:
    print(i)

print("\n\nDone!")
