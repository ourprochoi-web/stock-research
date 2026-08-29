#!/usr/bin/env python3
"""포트폴리오 현재가 업데이트 스크립트.

네이버 금융 API에서 종가를 가져와 prices.json을 갱신합니다.
사용법: python3 update_prices.py
GitHub Actions cron으로 자동화 가능.
"""
import json
import urllib.request
import os
import re
import sys
import time
from datetime import datetime, timedelta

# 보유 종목 (portfolio_tracker.html 이 이 이름들을 참조한다 — 이름 변경 금지)
TICKERS = {
    "SK하이닉스": "000660",
    "삼성전자": "005930",
    "SOL AI반도체TOP2+": "0167A0",
    "TIME 글로벌AI": "456600",
    "KODEX AI전력핵심설비": "487240",
}

# 리서치 페이지에서 주가·목표주가·배수를 인용하는 종목.
# 2026-08-08 추가 — 본문 산문에 박힌 가격이 낡는 것을 대조하기 위한 참조용이며,
# 보유 여부와 무관하다. 종목코드는 전부 API 응답의 stockName 과 대조해 검증했다.
WATCH = {
    "한화에어로스페이스": "012450",
    "삼성전기": "009150",
    "한미반도체": "042700",
    "HPSP": "403870",
    "HD현대일렉트릭": "267260",
    "효성중공업": "298040",
    "LS ELECTRIC": "010120",
    "두산에너빌리티": "034020",
    "대한전선": "001440",
    "일진전기": "103590",
    "현대로템": "064350",
    "에이피알": "278470",
    "삼성바이오로직스": "207940",
    "심텍": "222800",
    "대덕전자": "353200",
    "LG에너지솔루션": "373220",
    "포스코퓨처엠": "003670",
    "엘앤에프": "066970",
    "KB금융": "105560",
    # 2026-08-11 추가 — 이 둘은 오늘 KILL 조건·판정 이벤트가 걸린 종목이다.
    # HD현대중공업: Corban 선수금 20%(약 1,912억) 수령 여부가 1차 관문.
    # HD현대마린솔루션: 육상발전 LTSA(2031년~ 연 500억 근접)가 붙는 쪽.
    "HD현대중공업": "329180",
    "HD현대마린솔루션": "443060",
    # 2026-08-12 추가 — 보유 ETF(KODEX AI전력핵심설비) 구성의 17%가 추적 밖에 있었다.
    # LS 10% · 산일전기 4% · 가온전선 3%. 산일전기는 OPM 37%대로 섹터 최고인데
    # 수집 대상이 아니어서 실적 대조에서 빠져 있었다.
    "LS": "006260",
    "산일전기": "062040",
    "가온전선": "000500",
    # 2026-08-12 추가 — 아카이브 커버리지를 세어보니 113편 중 현재 판단이 36편(32%)뿐이고
    # AI 인프라·SW·HBM에 몰려 있었다. 편은 쌓였는데 가격 대조가 불가능한 섹터가 있었다
    # (바이오·GLP-1·K뷰티 19편). 전용 페이지가 있거나 본문 인용이 많은 종목만 넣는다(§B4).
    # 종목코드는 전부 API 응답의 stockName 과 대조해 검증했다.
    # ── K-뷰티 (k-beauty/ 5편)
    "코스맥스": "192820",
    "한국콜마": "161890",
    "실리콘투": "257720",
    "파마리서치": "214450",
    "아모레퍼시픽": "090430",
    "LG생활건강": "051900",
    # ── 바이오·GLP-1 (glp1/ 8편 + ai-bio/ 6편)
    "셀트리온": "068270",
    "알테오젠": "196170",
    "펩트론": "087010",
    "유한양행": "000100",
    "리가켐바이오": "141080",
    "SK바이오팜": "326030",
    # ── 방산 (defense/ 16편) — 2026-08-12 추가.
    # 본문 인용은 한화시스템 104회 · LIG 92회 · 풍산 51회인데 추적이 없었다.
    # ⚠ LIG넥스원은 사명이 "LIG디펜스앤에어로스페이스"로 바뀌어 있다(079550).
    #    아카이브 16편은 전부 옛 사명으로 쓰여 있다 — §A3 계열(조직 정보는 재사용 금지).
    "한화시스템": "272210",
    "한화오션": "042660",
    # ── 조선 — 2026-08-17 추가. 조사에서 공백이 드러나 붙인다.
    # 8/17에 "조선 3사 비교표"를 만들면서 삼성중공업 값을 임시로 뽑아 썼는데,
    # 정작 추적에 없어 그 표가 재현되지 않았다. 비교를 하려면 분모가 상시 있어야 한다.
    # 🔴 HD한국조선해양은 지주라 배수를 그대로 쓸 수 없다 —
    #    추정PER 7.12배인데 자회사 HD현대중공업은 16.58배로 절반 이하다(2026-08-17).
    #    LS에서 겪은 것과 같은 형태이며, 할인율 가정이 결론을 좌우한다(§A7-0).
    # ✅ HD현대미포 조회 실패의 원인이 확인됐다 — 코드 변경이 아니라 상장폐지다.
    #    2025-12-01 HD현대중공업에 흡수합병됐다. 따라서 조사 대상은 5사가 아니라 4사다.
    #    🔴 그리고 이것이 숫자 하나를 다시 읽게 만든다 — HHI의 4Q25 수주잔고 +25.2%는
    #    자생 성장이 아니라 사업결합 +11.38조다. 합병을 걸치는 시계열은 이 단절을 상속한다.
    "삼성중공업": "010140",
    "HD한국조선해양": "009540",
    # ── 조선 기자재 — 완성업체만 보면 마진이 어디서 나는지 안 보인다.
    # LNG 화물창(한국카본·동성화인텍)은 LNG선 발주에, 엔진(한화엔진)은
    # 상선·함정 양쪽에 걸린다. 세진중공업은 블록·데크하우스.
    # ── 반도체 소부장 — 2026-08-18 추가. 어제 AMAT 라우팅에서 "국내 소부장 실적이
    # 컨센을 크게 상회했다"를 논거로 쓰면서 [추론]("조기 인도라면 3Q에 공백")까지
    # 세웠는데, 정작 그 소부장이 한 종목도 추적에 없었다 — 분모 없이 추론을 세운 것이다.
    # 🔑 그리고 오늘 SK증권이 반증 데이터를 냈다: 분기 수주잔고가 3분기 연속 우상향
    # (테스 412 → 1,455 → 2,069억 · 원익IPS 2,982 → 4,004 → 6,346억).
    # 조기 인도였다면 잔고가 줄어야 하는데 늘고 있다.
    # ⚠ 단 둘 다 참일 수 있다 — "조기 인도"는 매출 인식 시점이고 잔고는 미래 물량이다.
    "테스": "095610",
    "원익IPS": "240810",
    "파크시스템스": "140860",
    "피에스케이": "319660",
    "코미코": "183300",
    # 티엘비 — SoCAMM 수주잔고가 2Q26에 1,318억(+364% YoY)으로 사상 첫 1,000억 돌파.
    # KX하이텍 — eSSD 케이스 공급 숏티지. 2026F P/E 3.9배로 제시되나 추정PER 미공시.
    "티엘비": "356860",
    "KX하이텍": "052900",
    "한화엔진": "082740",
    "한국카본": "017960",
    "동성화인텍": "033500",
    "세진중공업": "075580",
    # 2026-08-13 — 투자자가 실제 편입해 추적을 붙인다(§J1: 포지션 조회가 첫 단계).
    # ⚠ 현대백화점은 아카이브 인용 0편이다 — 판단 없는 포지션이므로 테제부터 세워야 한다.
    "현대백화점": "069960",
    # 달바글로벌 — 시총 3.3조로 K뷰티 주요 종목인데 아카이브 1편·추적 0이었다.
    # 2Q26 OPM 25.3%로 브랜드 중 최상위권이며 T2(ODM 주도) 대조에 필요하다.
    "달바글로벌": "483650",
    "LIG디펜스앤에어로스페이스": "079550",
    # ── 2026-08-19 추가. 룩스루 버킷에 있는데 추적이 없던 국내 3종목.
    # 이수페타시스는 2Q26 실적(매출 +57.4% · 영업이익 +83.3%)이 오늘 들어왔는데
    # 시세가 없어 배수를 붙일 수 없었다 — 보유 종목에서 이런 공백이 가장 비싸다.
    # 스피어(347700)는 보유가 아니지만 우주 편에 판단이 0편이라 조건부로 붙인다(§A6-1).
    "이수페타시스": "007660",
    "브이엠": "089970",   # 🔴 2026-08-19 정정: 084370은 유진테크였다. 60종목 전수 검증에서 유일한 불일치.

    # ═══ 2026-08-29 추가 — 소부장 11사 판정을 냈는데 4종목이 추적 밖이었다 ═══
    # 「소부장 6사 개별 판단」·「팹 증설 지도」를 만들면서 11사를 DART 확정값으로 판정했는데,
    # 그중 넷은 가격을 볼 수 없었다. §J4의 시세 버전 — "판단을 내는 순간이 추적에 넣을 순간".
    # 🔑 에스티아이가 가장 급하다 — 팹 지도 T1(발주는 인프라 → 장비 → 소재 순)의 <유일한 시험대>인데
    #    1H26 매출이 −14.6%다. M17(2027.02 착공)·테일러 Fab2(2026 연말)가 시작되면 다시 늘어야 하고,
    #    안 늘면 T1을 철회한다. 그 판정을 하려면 가격과 실적을 같이 봐야 한다.
    # · 주성엔지니어링 — 11사 중 유일한 영업적자(1H26 −56억 · ΔOPM −25.16%p). 증착·식각 양쪽에서
    #   겹치는 자리라 T1(점유율 싸움)이 가장 불리하게 작동한 사례.
    # · 이오테크닉스 — 레이저 단독 자리, 매출 +35.6% · ΔOPM +5.85%p인데 아카이브 판단이 얕다.
    # · 피에스케이홀딩스 — 후공정(Descum·Reflow). 🔴 08-29 C1급 정정의 당사자이므로
    #   피에스케이(319660)와 <반드시 코드로 구분>한다. 부분 문자열 매칭으로 두 번 사고가 났다.
    # 코드는 OpenDART corpCode.xml(상장 3,988개) + 네이버 stockName 양쪽으로 대조했다(§A4).
    "주성엔지니어링": "036930",
    "이오테크닉스": "039030",
    "에스티아이": "039440",
    "피에스케이홀딩스": "031980",
    "SK스퀘어": "402340",
    "스피어": "347700",
    "풍산": "103140",
    "한국항공우주": "047810",

    # ═══ 2026-08-25 추가 — 판단을 냈는데 추적에 없던 것을 닫는다 ═══
    # 로봇 Part 9(한국 16사 전수)를 만들고도 한 종목도 추적에 없었다.
    # §J4의 시세 버전 — "판단을 내는 순간이 추적에 넣을 순간"이다.
    # 코드는 네이버 stockName 과 전수 대조했다(§A4 — 08-19 브이엠/유진테크 사고 이후).
    # ⚠ 사명 변경 2건: 씨메스 → 씨메스로보틱스 · 에스에프에이 → SFA
    "레인보우로보틱스": "277810",
    "두산로보틱스": "454910",
    "로보티즈": "108490",
    "에스피지": "058610",
    "삼현": "437730",
    "에스비비테크": "389500",
    "현대무벡스": "319400",
    "뉴로메카": "348340",
    "유일로보틱스": "388720",
    "로보스타": "090360",
    "클로봇": "466100",
    "유진로봇": "056080",
    "엔젤로보틱스": "455900",
    "씨메스로보틱스": "475400",
    "티로보틱스": "117730",
    "SFA": "056190",
    # JP모건 T6 — 「부품사보다 로봇 OEM」. 로봇 접근 경로가 자동차 OEM으로 분류돼 있다
    "현대차": "005380",
    "기아": "000270",
}

# 해외 종목 — 리서치 페이지에서 배수·기준가를 인용하는 종목.
# 2026-08-08 추가. 엔드포인트가 국내(m.stock)와 다르다: api.stock.naver.com/stock/{SYM}/basic
# 접미사는 NASDAQ=.O, NYSE=무접미사 또는 .K (심볼별로 다르므로 검증된 값만 넣는다)
WATCH_US = {
    "Talen": "TLN.O",
    "AEP": "AEP.O",
    "NiSource": "NI",
    "Xcel Energy": "XEL.O",
    "Constellation Energy": "CEG.O",

    "Palantir": "PLTR.O",
    "CrowdStrike": "CRWD.O",
    "Datadog": "DDOG.O",
    "Snowflake": "SNOW.K",
    "Microsoft": "MSFT.O",
    "Eli Lilly": "LLY",
    "Novo Nordisk ADR": "NVO",
    "Salesforce": "CRM",
    "ServiceNow": "NOW",
    # 2026-08-11 추가 — 이 셋은 채점표가 걸려 있다.
    # AI 밸류체인 T7 / 메모리 사이클 C3급 철회의 범위 축소를 판정하는 조건이
    # "FY27 매출 ANET +56% · CSCO +21% · CRDO +106%" 이므로 기준가가 필요하다.
    # 2026-08-17 추가 — 광 계층 미결 ③을 "판단 보류"에서 "조사 착수"로 바꾸면서
    # 후보 12사를 실측했고, 그 결과가 같은 날 오전 결론을 뒤집었다.
    # 오전엔 "세 하우스 중 둘이 광 순수 플레이를 피한다"고 정리했는데,
    # 실측하니 순수 플레이 3사(루멘텀 OPM -14.8%→+21.7% / 시에나 3.1%→15.2% /
    # 코히어런트 9.8%→15.1%)가 가장 극적으로 개선 중이었다.
    # 하우스의 "입장"과 실적의 "상태"를 구분하지 않은 것이 원인이고, 원인의 원인은
    # 조사하지 않고 의견만 모은 것이다. 그래서 추적에 넣는다 — 값이 화면에 없으면
    # 다음에도 같은 실수를 한다(§H: 사람이 보는 것만 산다).
    #
    # 선정 기준: 직전 분기 매출 규모가 판정 대상이 되고(나비타스 $11M·IonQ $65M 제외),
    # 광/커넥터/DC 하드웨어 계층에서 실제로 비교 대상이 되는 것만 넣었다.
    "Vertiv": "VRT",
    "Marvell": "MRVL.O",
    "Corning": "GLW",
    "Amphenol": "APH",
    "TE Connectivity": "TEL",
    "Eaton": "ETN",
    "Ciena": "CIEN.K",
    "Lumentum": "LITE.O",
    "Coherent": "COHR.K",
    "Palo Alto Networks": "PANW.O",
    "Arista Networks": "ANET.K",
    "Cisco Systems": "CSCO.O",
    "Credo Technology": "CRDO.O",
    # 2026-08-12 — AI 바이오 편(6편)이 본문에서 56회 인용하는데 가격 추적이 없었다.
    "Recursion Pharma": "RXRX.O",
    # 2026-08-12 — 메모리 테제의 핵심 비교 대상인데 추적이 없었다.
    # "한국 낙폭이 미국의 2배"라는 주장을 검증하려면 이 종목이 필요하다.
    "Micron": "MU.O",
    # ── 2026-08-12 추가. 셋 다 아카이브가 이미 판단을 걸어둔 곳이다.
    # CoreWeave는 AI 밸류체인 T4의 정본 사례(이자비용 = 조정 영업이익의 5.0배)인데
    # 4편이 인용하면서 추적이 없었다. Nebius는 MW당 ACV를 공개한 유일한 비교군이라
    # HD현대 온사이트 건의 MW당 단가와 같은 축에서 볼 수 있다(§A7-0).
    "CoreWeave": "CRWV.O",
    "Nebius": "NBIS.O",
    # SpaceX — 우주 편에 현재 판단(T1~T5)이 있는데 추적이 없었다.
    # T1이 "우주주가 아니라 AI 인프라주"로 재분류했으므로 AI 우산 안이다.
    "SpaceX": "SPCX.O",
    # ── 2026-08-19 추가. 🔴 룩스루 전수 대조에서 28개 중 12개(43%)가 추적 밖임이 드러났다.
    # §I는 2026-08-12에 "보유 자산 구성 추적률 83% → 100%"로 기록했는데 틀렸다 —
    # 그때 고친 것은 "ETF 구성을 파악했다"이지 "그 종목을 추적한다"가 아니었다.
    # 둘은 다른 작업이고, 비중 계산은 etfHoldings로 되지만 실적·배수 대조는 안 된다.
    # 특히 NVIDIA·SanDisk가 빠져 있었다 — AI 밸류체인 T1과 메모리 사이클 T4의 핵심인데
    # 본문에서 수십 회 인용하면서 기준가가 없었다.
    "NVIDIA": "NVDA.O",
    "AMD": "AMD.O",
    "Intel": "INTC.O",
    "ASML": "ASML.O",
    "SanDisk": "SNDK.O",
    "Seagate": "STX.O",
    # ── 2026-08-19 추가. 🔴 마벨-구글 커스텀 실리콘 8-K를 라우팅하다가
    # 「마벨의 정확한 반대편이 추적에 없다」는 것이 드러났다.
    # 구글 TPU의 커스텀 실리콘은 브로드컴이 맡아 왔고, 마벨이 「TPU 생태계에
    # 붙는」 영역으로 들어온 그 날 브로드컴이 −5.37%였다. 제로섬 재배치를
    # 관측하려면 양쪽이 다 있어야 한다(§A7-0 — 한쪽만 보면 방향만 알고 크기를 모른다).
    "Broadcom": "AVGO.O",
    "Western Digital": "WDC.O",
    # ── 2026-08-23 추가 (§J13 미국 배정 검토) ──
    # 판단은 있는데 시세 추적 밖이던 14종목. 비교표를 만들려면 같은 창의
    # 가격·실적이 있어야 하는데 오늘 만든 판단(Vistra·NRG·Hut8·Bitdeer·
    # Cerebras·ST마이크로·X-Energy)이 전부 수집 밖이었고 메가캡 6개도 없었다.
    "Cerebras": "CBRS.O",
    "Alphabet": "GOOGL.O",
    "Meta Platforms": "META.O",
    "Amazon": "AMZN.O",
    "TSMC ADR": "TSM",
    "Oracle": "ORCL.K",
    "Vistra": "VST",
    "NRG Energy": "NRG",
    "Hut 8": "HUT.O",
    "Bitdeer": "BTDR.O",
    "STMicroelectronics": "STM",
    "Astera Labs": "ALAB.O",
    "Tesla": "TSLA.O",
    "X-Energy": "XE.O",
    # ── 2026-08-23 (2) 층별 비교용 — AI 내부의 <비어 있는 층> + 비AI 후보 ──
    # 「메모리 말고 AI 안에서 어디를 볼까」에 답하려면 층마다 실측이 있어야 한다.
    # 구리·EPC·가스 상류는 아카이브가 수요 측 근거만 갖고 공급 측이 비어 있었다.
    "Freeport-McMoRan": "FCX",      # 구리 — 아카이브 「1MW당 27톤·부족 33만톤」의 상류
    "GE Vernova": "GEV",            # 가스터빈·그리드
    "Quanta Services": "PWR",       # 전력 EPC(송배전 시공)
    "Comfort Systems": "FIX",       # 데이터센터 기계설비 시공
    "Vulcan Materials": "VMC",      # 골재 — DC 건설 상류(비AI 대조군)
    "Targa Resources": "TRGP.K",    # 미드스트림 가스
    "Cheniere Energy": "LNG",       # LNG
    "Williams": "WMB",              # 가스 파이프라인
    "Lockheed Martin": "LMT",       # 방산 — 진짜 AI 밖 대조군
    "Visa": "V",                    # 결제 — 비AI 대조군
    "Mastercard": "MA",
    "Berkshire Hathaway B": "BRKb",
    # 2026-08-23 (3) — AI 바이오 T3(파이프라인 이벤트가 지표) 사례
    "Moderna": "MRNA.O",
    # 2026-08-23 (4) — 방산 4사 비교 완성(록히드만 있었다)
    "Northrop Grumman": "NOC",
    "RTX Corp": "RTX",
    "General Dynamics": "GD",

    # ═══ 2026-08-25 추가 ═══
    "Bloom Energy": "BE",        # 딥리서치 신설 — 온사이트 발전(규제형·상인형과 다른 제3의 층)
    # 태양광·ESS 3사 — 「다 애매하다」에 답하며 재무를 열었는데 추적에 없었다
    "First Solar": "FSLR.O",
    "Nextracker": "NXT.O",
    "Shoals": "SHLS.O",
}

# 기간 수익률을 계산할 구간. "최근 순환매가 왔는가"는 52주 고저만으로는
# 판정되지 않는다 — 저점 시점이 종목마다 다르기 때문이다(A7-0).
PERIODS = (("1W", 7), ("1M", 30), ("3M", 91), ("6M", 182), ("1Y", 365))

# 호출 간격(초). 2026-08-12에 같은 스크립트를 짧은 간격으로 여러 번 돌렸더니
# 레이트리밋에 걸려 returns 29/38 · flows 0 으로 **부분 실패**했다.
PAUSE = 0.15

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, "prices.json")


def fetch_price(code):
    url = f"https://m.stock.naver.com/api/stock/{code}/basic"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  ✗ {code} — {e}")
        return None


def fetch_fundamentals(code):
    """국내 종목의 컨센서스 지표 — basic 과 다른 엔드포인트다.

    2026-08-08: '해외 시세는 확보할 수 없다'고 적었다가 재시도해서 찾았다.
    integration 은 시총·추정PER·추정EPS·52주 최고/최저를 준다.
    배수 검증(A7)의 분모가 여기서 나온다 — basic 만으로는 가격밖에 없어
    '배수가 맞는지'를 판정할 수 없었다.
    """
    url = f"https://m.stock.naver.com/api/stock/{code}/integration"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read())
    except Exception:
        return None
    info = {i.get("key"): i.get("value")
            for i in (d.get("totalInfos") or []) if isinstance(i, dict)}
    want = ("시총", "추정PER", "추정EPS", "PER", "EPS", "52주 최고", "52주 최저")
    return {k: info[k] for k in want if k in info} or None


def fetch_returns(code, foreign=False):
    """기간 수익률 — 차트 엔드포인트 한 번으로 1W~1Y 를 전부 만든다.

    2026-08-11 추가. 그날 "최근 순환매가 안 온 섹터"를 물었는데 답할 수 없었다.
    prices.json 에는 현재가·당일등락·52주 고저만 있었고, 52주 고저로는
    판정되지 않는다 — **저점이 언제였는지가 종목마다 다르기 때문**이다(A7-0).
    같은 "저점 대비 +30%"라도 저점이 지난달이면 순환매가 온 것이고
    작년이면 안 온 것인데, 그 구분이 데이터에 없었다.

    엔드포인트는 국내/해외가 다르다(domestic/foreign). 둘 다 일봉 배열을
    주므로 기준일 종가 대비로 계산한다. 거래일이 아닌 날은 그 이전
    마지막 거래일로 대체한다 — 휴장일에 None 이 되는 것을 막는다.
    """
    kind = "foreign" if foreign else "domestic"
    end = datetime.now()
    start = end - timedelta(days=420)
    url = (f"https://api.stock.naver.com/chart/{kind}/item/{code}/day"
           f"?startDateTime={start:%Y%m%d}0000&endDateTime={end:%Y%m%d}0000")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            rows = json.loads(resp.read())
    except Exception:
        return None
    series = []
    for r in rows:
        try:
            series.append((str(r["localDate"]), float(r["closePrice"])))
        except (KeyError, TypeError, ValueError):
            continue
    if len(series) < 2:
        return None
    series.sort()
    last_date, last_close = series[-1]

    out = {"asOf": f"{last_date[:4]}-{last_date[4:6]}-{last_date[6:]}"}
    base = datetime.strptime(last_date, "%Y%m%d")
    for label, days in PERIODS:
        target = (base - timedelta(days=days)).strftime("%Y%m%d")
        prior = [c for d, c in series if d <= target]
        if not prior:  # 상장 기간이 그 구간보다 짧다 — 없는 것을 0으로 적지 않는다
            continue
        out[label] = round((last_close / prior[-1] - 1) * 100, 1)

    ytd = [c for d, c in series if d < f"{last_date[:4]}0101"]
    if ytd:
        out["YTD"] = round((last_close / ytd[-1] - 1) * 100, 1)
    return out


def mcap_won(text):
    """'74조 5,284억' 같은 표기를 원 단위 숫자로. 못 읽으면 None."""
    if not text:
        return None
    s = str(text).replace(",", "").replace(" ", "")
    m = re.match(r"(?:(\d+)조)?(?:(\d+)억)?", s)
    if not m or not (m.group(1) or m.group(2)):
        return None
    return int(m.group(1) or 0) * 10**12 + int(m.group(2) or 0) * 10**8


def fetch_flows(code):
    """투자자별 순매수와 외국인 보유율 — 국내 종목만 제공된다.

    2026-08-11 추가. **쓰는 규칙을 먼저 정해 두고 넣는다.**

    아카이브는 "무엇이 참인가"(테제)만 판정하고 **"왜 아직 가격에 없는가"를
    판정할 축이 없었다.** 2026-08-11 방산이 정확히 그 공백이었다 — 실적이
    컨센 36% 상회인데 3M -15.6%였고, 인용할 수 있는 것은 "자금이 먼저 다른
    섹터로 간다"는 ③ 전문가 판단뿐이었다. 수급은 그것을 ①로 바꾼다.

    **그러나 수급을 테제로 승격시키면 안 된다(§E3).** "외국인이 팔았다"는
    ① 사실이지만 "그래서 하락한다"는 ③이고 대부분 **사후 서사**가 된다.
    판정할 수 없는 트리거는 만들지 않기로 했으므로 용도를 좁힌다:

        수급은 T(테제)에 넣지 않는다.
        이미 판정된 테제가 **가격과 어긋날 때만** 기록한다.
        가격과 수급이 같은 방향이면 적지 않는다 — 정보가 없다(§B4와 같은 논리).

    실측이 그 이유를 보여준다(2026-08-11, 10거래일):
      SK하이닉스 1M -33.7% / 외국인 -268만주·보유율 -1.34%p  → 방향 일치, 정보 없음
      한화에어로 1M +12.1% / 외국인 +6만주·보유율 +0.21%p    → 방향 일치, 정보 없음
      현대로템   1M -19.6% / 외국인 **+87만주·보유율 +0.83%p** → **어긋남. 여기가 정보다**

    이 함수는 사실만 모은다. 무엇을 의미하는지는 사람이 판정한다.
    """
    url = f"https://m.stock.naver.com/api/stock/{code}/trend"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        time.sleep(PAUSE)
        with urllib.request.urlopen(req, timeout=10) as resp:
            rows = json.loads(resp.read())
    except Exception:
        return None
    if not rows:
        return None

    def q(v):
        try:
            return int(str(v).replace(",", "").replace("+", ""))
        except (TypeError, ValueError):
            return 0

    def pct(v):
        try:
            return float(str(v).replace("%", ""))
        except (TypeError, ValueError):
            return None

    dates = sorted(str(r.get("bizdate", "")) for r in rows if r.get("bizdate"))
    if not dates:
        return None
    newest = max(rows, key=lambda r: str(r.get("bizdate", "")))
    oldest = min(rows, key=lambda r: str(r.get("bizdate", "")))
    hr_new, hr_old = pct(newest.get("foreignerHoldRatio")), pct(oldest.get("foreignerHoldRatio"))

    out = {
        "days": len(rows),
        "from": f"{dates[0][:4]}-{dates[0][4:6]}-{dates[0][6:]}",
        "to": f"{dates[-1][:4]}-{dates[-1][4:6]}-{dates[-1][6:]}",
        "foreign": sum(q(r.get("foreignerPureBuyQuant")) for r in rows),
        "organ": sum(q(r.get("organPureBuyQuant")) for r in rows),
        "individual": sum(q(r.get("individualPureBuyQuant")) for r in rows),
    }
    if hr_new is not None:
        out["holdRatio"] = hr_new
        if hr_old is not None:
            out["holdRatioChange"] = round(hr_new - hr_old, 2)
    return out


def fetch_rates():
    """미국 금리 — 할인율 축(CLAUDE.md §J13-1).

    2026-08-23 추가. 아카이브가 금리를 211회 언급하면서 판단 블록에는
    0편이었다. DR Horton NPM(13.5%→8.6%→9.8%)도, 코어위브 조달금리
    9.25~9.75%도 기준점 없이 적혀 있었다 — 무위험 금리가 없으면
    스프레드를 못 낸다.

    ⚠ 모기지는 주간(목요일), 국채·연방기금은 일간이라 관측 빈도가 다르다.
    창(window)은 인덱스가 아니라 <날짜>로 잡아야 한다 — 인덱스로 잡으면
    모기지 1개월이 국채 1주일이 된다(§A5).
    """
    import datetime as _dt
    series = {"DGS10": "10년 국채", "DGS2": "2년 국채",
              "MORTGAGE30US": "30년 모기지", "DFF": "연방기금(실효)"}
    # ⚠ FRED는 "Mozilla/5.0"을 차단한다(타임아웃). 연락처가 든 UA만 통과한다.
    #    2026-08-23 실측 — 같은 URL이 UA만 바꾸면 성공/타임아웃으로 갈렸다.
    hdr = {"User-Agent": "ourprochoi Research kenchoi@keywestaim.com"}
    out = {"asof": "", "levels": {}, "changes": {}, "spreads": {}}
    rows_by_id = {}
    for sid in series:
        try:
            req = urllib.request.Request(
                f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", headers=hdr)
            with urllib.request.urlopen(req, timeout=25) as resp:
                text = resp.read().decode()
        except Exception as e:
            print(f"  \u2717 FRED {sid} — {e}")
            continue
        rows = []
        for line in text.strip().split("\n")[1:]:
            parts = line.split(",")
            if len(parts) == 2 and parts[1] not in (".", ""):
                rows.append((parts[0], float(parts[1])))
        if rows:
            rows_by_id[sid] = rows

    if "DGS10" not in rows_by_id:
        return None

    def value_on_or_before(rows, target):
        best = None
        for d, v in rows:
            if d <= target:
                best = v
            else:
                break
        return best

    for sid, rows in rows_by_id.items():
        end = _dt.date.fromisoformat(rows[-1][0])
        out["asof"] = max(out["asof"], rows[-1][0])
        out["levels"][sid] = rows[-1][1]
        ch = {}
        for label, days in (("1M", 30), ("3M", 91), ("6M", 182), ("1Y", 365)):
            prior = value_on_or_before(rows, (end - _dt.timedelta(days=days)).isoformat())
            if prior is not None:
                ch[label] = round(rows[-1][1] - prior, 2)
        out["changes"][sid] = ch

    L = out["levels"]
    if "DGS2" in L:
        out["spreads"]["curve_10y_2y"] = round(L["DGS10"] - L["DGS2"], 2)
    if "MORTGAGE30US" in L:
        out["spreads"]["mortgage_over_10y"] = round(L["MORTGAGE30US"] - L["DGS10"], 2)
    if "DFF" in L:
        out["spreads"]["term_10y_over_ff"] = round(L["DGS10"] - L["DFF"], 2)

    print(f"  \u2713 금리 → 10y {L.get('DGS10')}% · 모기지 {L.get('MORTGAGE30US')}% · "
          f"FF {L.get('DFF')}%  (커브 {out['spreads'].get('curve_10y_2y'):+.2f}%p, {out['asof']})")
    return out


def fetch_fx():
    """USD/KRW 종가 시계열 — 해외 배정의 환 노출을 재기 위한 축(CLAUDE.md §J13).

    2026-08-23 추가. 그전까지 prices.json에 환율이 없어서 "미국 주식에
    얼마를 넣을까"를 물었을 때 종목만 답하고 환은 답할 수 없었다.
    5억 기준 3년 실측 폭(1,290~1,560)이 원화 손익 −3,530만~+6,178만이므로
    웬만한 종목 알파보다 크다.

    ⚠ closePrice(매매기준율)와 cashBuyValue(현찰 살 때)는 다른 값이다.
    섞으면 §A5 위반이므로 둘 다 담되 이름을 구분해 둔다.
    """
    base = "https://api.stock.naver.com/marketindex/exchange/FX_USDKRW/prices"
    hdr = {"User-Agent": "Mozilla/5.0", "Referer": "https://m.stock.naver.com/"}
    rows = []
    for page in range(1, 13):          # 60 × 12 ≈ 3년
        try:
            req = urllib.request.Request(f"{base}?page={page}&pageSize=60", headers=hdr)
            with urllib.request.urlopen(req, timeout=15) as resp:
                chunk = json.loads(resp.read())
        except Exception as e:
            print(f"  \u2717 FX page {page} — {e}")
            break
        if not chunk:
            break
        for x in chunk:
            try:
                rows.append((x["localTradedAt"][:10], float(x["closePrice"].replace(",", ""))))
            except (KeyError, ValueError):
                continue
    if not rows:
        return None
    rows = sorted(set(rows))
    cur_date, cur = rows[-1]

    def back(n):
        return rows[max(0, len(rows) - 1 - n)][1]

    vals = [v for _, v in rows]
    out = {
        "pair": "USD/KRW",
        "close": cur,
        "asof": cur_date,
        "days": len(rows),
        "returns": {},
        "range": {"min": min(vals), "max": max(vals),
                  "median": sorted(vals)[len(vals) // 2]},
    }
    for label, n in (("1W", 5), ("1M", 22), ("3M", 66), ("6M", 132), ("1Y", 252)):
        if len(rows) > n:
            out["returns"][label] = round(cur / back(n) - 1, 4)
    print(f"  \u2713 USD/KRW → {cur:,.2f}원 ({cur_date}, {len(rows)}일)  "
          f"1M {out['returns'].get('1M', 0):+.2%} · 1Y {out['returns'].get('1Y', 0):+.2%}")
    return out


def fetch_us(sym):
    """해외 종목 — 국내와 엔드포인트가 다르다."""
    url = f"https://api.stock.naver.com/stock/{sym}/basic"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  \u2717 {sym} — {e}")
        return None


def fetch_us_fundamentals(sym):
    """해외 종목의 분기 실적 + 컨센서스.

    2026-08-12 추가. 그전까지 해외는 price/shares/mcap 3필드뿐이라
    배수도 마진도 계산할 수 없었고, 그래서 스크리닝에서 미국이 통째로
    빠졌다. "해외는 데이터가 없다"고 전제했으나 실제로는 열려 있었다
    (CLAUDE.md §G — 확인하지 않은 것을 확인할 수 없는 것처럼 적지 않는다).

    ⚠ columns 딕셔너리의 키 순서는 trTitleList 순서와 다르다.
    반드시 trTitleList의 key로 뽑아야 분기가 어긋나지 않는다(§A5).
    """
    base = f"https://api.stock.naver.com/stock/{sym}"
    hdr = {"User-Agent": "Mozilla/5.0"}

    def get(path):
        try:
            req = urllib.request.Request(base + path, headers=hdr)
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read())
        except Exception:
            return None

    out = {}
    q = get("/finance/quarter")
    if q and q.get("trTitleList") and q.get("rowList"):
        keys = [x["key"] for x in q["trTitleList"]]
        titles = [x["title"] for x in q["trTitleList"]]
        rows = {r["title"]: r["columns"] for r in q["rowList"]}

        def series(label):
            vals = []
            for k in keys:
                c = rows.get(label, {}).get(k)
                if not c:
                    vals.append(None)
                    continue
                try:
                    vals.append(float(str(c["value"]).replace(",", "")))
                except ValueError:
                    vals.append(None)
            return vals

        ebit, rev = series("EBIT"), series("매출액")
        out["unit"] = q.get("unit")
        out["quarters"] = titles
        if ebit[-1] is not None:
            out["EBIT"] = ebit[-1]
        if rev[-1] is not None:
            out["매출액"] = rev[-1]
        if ebit[-1] is not None and rev[-1]:
            out["OPM"] = round(ebit[-1] / rev[-1] * 100, 1)
        # 같은 분기 4개 전 = 전년 동기. 흑자 전환은 배수가 무의미하므로 뺀다.
        if len(ebit) >= 5 and ebit[0] and ebit[-1] is not None and ebit[0] > 0:
            out["EBIT_YoY"] = round((ebit[-1] / ebit[0] - 1) * 100, 1)

    c = get("/consensus")
    if c:
        for src, dst in (("priceTargetMean", "목표주가"),
                         ("priceTargetHigh", "목표주가_최고"),
                         ("priceTargetLow", "목표주가_최저"),
                         ("recommMean", "투자의견")):
            if c.get(src):
                out[dst] = c[src]
    return out or None


def main():
    print("포트폴리오 현재가 업데이트 중...\n")
    prices = {}
    updated = ""
    updated_time = ""

    for name, code in {**TICKERS, **WATCH}.items():
        data = fetch_price(code)
        if not data:
            continue
        close = int(data["closePrice"].replace(",", ""))
        date = data.get("localTradedAt", "")[:10]
        change = data.get("compareToPreviousClosePrice", "?")
        ratio = data.get("fluctuationsRatio", "?")
        direction = data.get("compareToPreviousPrice", {}).get("text", "")

        prices[name] = close
        if not updated:
            updated = date
            t = data.get("localTradedAt", "")  # "2026-08-11T16:10:20+09:00"
            updated_time = t[11:16] + " KST" if len(t) > 16 else ""
        print(f"  ✓ {name} ({code}) → {close:>12,}원  {direction} {change} ({ratio}%)")

    # 국내 종목 컨센서스 지표 — 배수(A7) 검증의 분모
    fundamentals = {}
    for name, code in {**TICKERS, **WATCH}.items():
        fd = fetch_fundamentals(code)
        if fd:
            fundamentals[name] = fd

    # 환율 — 해외 배정의 환 노출 축 (§J13)
    fx = fetch_fx()
    rates = fetch_rates()

    # 해외 종목 — 배수 검증용 (가격 + 상장주식수로 시총까지 산출)
    us = {}
    for name, sym in WATCH_US.items():
        d = fetch_us(sym)
        if not d:
            continue
        try:
            px = float(str(d["closePrice"]).replace(",", ""))
        except (KeyError, ValueError):
            continue
        cnt = d.get("countOfListedStock")
        rec = {"price": px, "symbol": sym}
        if cnt:
            rec["shares"] = int(cnt)
            rec["mcapB"] = round(px * int(cnt) / 1e9, 1)
        fd = fetch_us_fundamentals(sym)
        if fd:
            rec.update(fd)
        us[name] = rec
        mc = f"  시총 ${rec['mcapB']:,}B" if "mcapB" in rec else ""
        opm = f"  OPM {rec['OPM']}%" if "OPM" in rec else ""
        tp = f"  TP {rec['목표주가']}" if "목표주가" in rec else ""
        print(f"  \u2713 {name} ({sym}) \u2192 ${px:>10,.2f}{mc}{opm}{tp}")
        time.sleep(PAUSE)

    # 기간 수익률 — 52주 고저로는 "언제 올랐는가"를 알 수 없다(A7-0)
    returns = {}
    for name, code in {**TICKERS, **WATCH}.items():
        r = fetch_returns(code)
        if r:
            returns[name] = r
    for name, sym in WATCH_US.items():
        r = fetch_returns(sym, foreign=True)
        if r:
            returns[name] = r

    # 수급 — 국내만 제공된다. 쓰는 규칙은 fetch_flows 주석에 있다.
    flows = {}
    for name, code in {**TICKERS, **WATCH}.items():
        fl = fetch_flows(code)
        if fl:
            flows[name] = fl

    # 순매수의 **크기**를 시총 대비로 환산한다.
    # 2026-08-12 추가 — 주수만으로는 크기를 비교할 수 없다. 삼성전자 208만 주와
    # 심텍 208만 주는 같은 숫자이지 같은 크기가 아니다(A7-0: 분모를 붙인다).
    # 보유율 변화를 쓰지 않는 이유는 **분모가 함께 움직이기 때문**이다 —
    # 실제로 삼성전자는 외국인 순매도인데 보유율은 올랐다(2026-08-12 실측).
    for name, fl in flows.items():
        px = prices.get(name)
        mc = mcap_won((fundamentals.get(name) or {}).get("시총"))
        if px and mc:
            fl["netPctOfMcap"] = round(fl["foreign"] * px / mc * 100, 3)

    # Preserve existing etfHoldings if present
    existing_holdings = {}
    if os.path.exists(OUTPUT):
        try:
            with open(OUTPUT, "r", encoding="utf-8") as f:
                existing = json.load(f)
                existing_holdings = existing.get("etfHoldings", {})
        except Exception:
            pass

    # ── 빈 결과 방어 ──────────────────────────────────────────────
    # 2026-08-11 추가. 2026-08-10 봇 커밋이 prices 24→0 · fundamentals 24→0 ·
    # us 9→0 으로 파일을 통째로 비웠고, updated 도 빈 문자열이었는데
    # **그대로 커밋됐다**. 스크립트가 실패를 exit 0 으로 삼켰기 때문이다.
    # 워크플로는 멀쩡했다 — 고장난 것은 "무조건 쓴다"는 이 자리였다.
    #
    # 보유 종목은 portfolio_tracker.html 이 직접 참조하므로 하나라도 빠지면
    # 쓰지 않고 실패시킨다. **낡은 파일이 남는 편이 빈 파일보다 낫다** —
    # 낡은 것은 기준일로 드러나지만 빈 것은 화면에서 그냥 사라진다.
    # 섹션이 기존보다 크게 줄면 그 섹션만 기존 값을 유지한다.
    # 2026-08-12 추가 — 어제 만든 가드는 "전부 실패"만 막았고 **부분 실패는
    # 그대로 통과했다**. 레이트리밋으로 returns 29/38 · flows 0 이 됐는데
    # 보유 종목 시세는 멀쩡해서 파일이 덮였다. 같은 원칙을 섹션마다 적용한다 —
    # **낡은 값이 남는 편이 사라지는 것보다 낫다.** 단 어느 섹션이 낡았는지
    # 파일에 남긴다. 낡은 것을 최신인 척 두는 것이 §A5 가 금지하는 것이다.
    stale = {}
    if os.path.exists(OUTPUT):
        try:
            with open(OUTPUT, "r", encoding="utf-8") as fh:
                prev = json.load(fh)
        except Exception:
            prev = {}
        for key, fresh in (("returns", returns), ("flows", flows),
                           ("fundamentals", fundamentals), ("us", us)):
            old = prev.get(key) or {}
            if len(old) > len(fresh) * 1.2 and len(old) > 0:
                print(f"  ⚠ {key}: {len(fresh)}건만 수집됨(기존 {len(old)}건) "
                      f"— 기존 값을 유지합니다")
                if key == "returns":
                    returns = old
                elif key == "flows":
                    flows = old
                elif key == "fundamentals":
                    fundamentals = old
                else:
                    us = old
                stale[key] = prev.get("updated", "?")

    missing = [n for n in TICKERS if n not in prices]
    if missing or not updated:
        print(f"\n✗ 중단 — 파일을 쓰지 않습니다.")
        if missing:
            print(f"  보유 종목 수집 실패 {len(missing)}건: {', '.join(missing)}")
        if not updated:
            print("  기준일을 확보하지 못했습니다.")
        print("  기존 prices.json 은 그대로 둡니다(빈 파일로 덮지 않는다).")
        return 1

    result = {"updated": updated, "updatedTime": updated_time,
              "prices": prices, "fundamentals": fundamentals,
              "returns": returns, "flows": flows, "us": us}
    if fx:
        result["fx"] = fx    # §J13 — 해외 배정의 환 노출 축
    if rates:
        result["rates"] = rates    # §J13-1 — 할인율 축
    if stale:
        result["staleSections"] = stale  # 이 섹션들은 updated 날짜가 아니다
    if existing_holdings:
        result["etfHoldings"] = existing_holdings

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    total = len({**TICKERS, **WATCH}) + len(WATCH_US)
    print(f"\n완료: {OUTPUT}")
    print(f"기준일: {updated} {updated_time}")
    print(f"수집: 국내 시세 {len(prices)} · 컨센 {len(fundamentals)} · "
          f"해외 {len(us)} · 기간수익률 {len(returns)}/{total} · 수급 {len(flows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
