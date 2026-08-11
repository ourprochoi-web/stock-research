#!/usr/bin/env python3
"""포트폴리오 현재가 업데이트 스크립트.

네이버 금융 API에서 종가를 가져와 prices.json을 갱신합니다.
사용법: python3 update_prices.py
GitHub Actions cron으로 자동화 가능.
"""
import json
import urllib.request
import os
import sys
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
    "Arista Networks": "ANET.K",
    "Cisco Systems": "CSCO.O",
    "Credo Technology": "CRDO.O",
}

# 기간 수익률을 계산할 구간. "최근 순환매가 왔는가"는 52주 고저만으로는
# 판정되지 않는다 — 저점 시점이 종목마다 다르기 때문이다(A7-0).
PERIODS = (("1W", 7), ("1M", 30), ("3M", 91), ("6M", 182), ("1Y", 365))

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
        us[name] = rec
        mc = f"  시총 ${rec['mcapB']:,}B" if "mcapB" in rec else ""
        print(f"  \u2713 {name} ({sym}) \u2192 ${px:>10,.2f}{mc}")

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
              "returns": returns, "us": us}
    if existing_holdings:
        result["etfHoldings"] = existing_holdings

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    total = len({**TICKERS, **WATCH}) + len(WATCH_US)
    print(f"\n완료: {OUTPUT}")
    print(f"기준일: {updated} {updated_time}")
    print(f"수집: 국내 시세 {len(prices)} · 컨센 {len(fundamentals)} · "
          f"해외 {len(us)} · 기간수익률 {len(returns)}/{total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
