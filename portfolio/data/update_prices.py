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
    # 2026-08-13 — 투자자가 실제 편입해 추적을 붙인다(§J1: 포지션 조회가 첫 단계).
    # ⚠ 현대백화점은 아카이브 인용 0편이다 — 판단 없는 포지션이므로 테제부터 세워야 한다.
    "현대백화점": "069960",
    # 달바글로벌 — 시총 3.3조로 K뷰티 주요 종목인데 아카이브 1편·추적 0이었다.
    # 2Q26 OPM 25.3%로 브랜드 중 최상위권이며 T2(ODM 주도) 대조에 필요하다.
    "달바글로벌": "483650",
    "LIG디펜스앤에어로스페이스": "079550",
    "풍산": "103140",
    "한국항공우주": "047810",
}

# 해외 종목 — 리서치 페이지에서 배수·기준가를 인용하는 종목.
# 2026-08-08 추가. 엔드포인트가 국내(m.stock)와 다르다: api.stock.naver.com/stock/{SYM}/basic
# 접미사는 NASDAQ=.O, NYSE=무접미사 또는 .K (심볼별로 다르므로 검증된 값만 넣는다)
WATCH_US = {
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
