#!/usr/bin/env python3
"""포트폴리오 현재가 업데이트 스크립트.

네이버 금융 API에서 종가를 가져와 prices.json을 갱신합니다.
사용법: python3 update_prices.py
GitHub Actions cron으로 자동화 가능.
"""
import json
import urllib.request
import os

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
}

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
        print(f"  ✓ {name} ({code}) → {close:>12,}원  {direction} {change} ({ratio}%)")

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

    # Preserve existing etfHoldings if present
    existing_holdings = {}
    if os.path.exists(OUTPUT):
        try:
            with open(OUTPUT, "r", encoding="utf-8") as f:
                existing = json.load(f)
                existing_holdings = existing.get("etfHoldings", {})
        except Exception:
            pass

    # Extract update time from first ticker's localTradedAt
    updated_time = ""
    for name, code in TICKERS.items():
        data = fetch_price(code)
        if data and data.get("localTradedAt"):
            t = data["localTradedAt"]  # e.g. "2026-07-15T16:10:20+09:00"
            updated_time = t[11:16] + " KST" if len(t) > 16 else ""
            break

    result = {"updated": updated, "updatedTime": updated_time, "prices": prices, "us": us}
    if existing_holdings:
        result["etfHoldings"] = existing_holdings

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"\n완료: {OUTPUT}")
    print(f"기준일: {updated}")


if __name__ == "__main__":
    main()
