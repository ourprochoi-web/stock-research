# -*- coding: utf-8 -*-
"""Minimal stdlib-only fetchers for the daily market-data collector.

Every function was exercised on 2026-09-14/15 from this machine (proxy present).
See REPORT.md for status, cadence and caveats per source.

Conventions
- Network: urllib only. Naver gets UA 'Mozilla/5.0'; FRED gets a contact UA.
- Return plain Python (list/dict of str/float/int). Callers decide persistence.
- Nothing here raises on HTTP errors except the helper; each fetcher lets the
  exception propagate so the collector can log host+path+error.
"""
import datetime as _dt
import gzip as _gzip
import io as _io
import json as _json
import re as _re
import urllib.parse as _up
import urllib.request as _ur

UA_BROWSER = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36')
UA_NAVER = 'Mozilla/5.0'
UA_FRED = 'research-archive contact kenchoi@keywestaim.com'


class FetchError(Exception):
    def __init__(self, url, status, body=b''):
        self.url, self.status, self.body = url, status, body
        super().__init__('%s -> %s %s' % (url, status, body[:200]))


def _get(url, headers=None, data=None, timeout=25):
    h = {'User-Agent': UA_NAVER}
    if headers:
        h.update(headers)
    req = _ur.Request(url, headers=h, data=data)
    try:
        with _ur.urlopen(req, timeout=timeout) as r:
            b = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                b = _gzip.GzipFile(fileobj=_io.BytesIO(b)).read()
            return b
    except _ur.HTTPError as e:
        raise FetchError(url, e.code, e.read()[:300])


def _json_get(url, headers=None):
    return _json.loads(_get(url, headers).decode('utf-8'))


def _num(s):
    """'1,683,000' -> 1683000 ; '-7.12' -> -7.12 ; '+906,398' -> 906398."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return s
    t = s.replace(',', '').replace('+', '').replace('%', '').strip()
    if t in ('', 'N/A', '-'):
        return None
    return float(t) if ('.' in t) else int(t)


def krw_units_to_eok(s):
    """'2조 4,788억' -> 24788 (억원). '9,539억' -> 9539. '1,000억' -> 1000."""
    if not s:
        return None
    total = 0
    m = _re.search(r'([\d,]+)조', s)
    if m:
        total += int(m.group(1).replace(',', '')) * 10000
    m = _re.search(r'([\d,]+)억', s)
    if m:
        total += int(m.group(1).replace(',', ''))
    return total


# ---------------------------------------------------------------------------
# 1. Korean stock: regular-session (15:30 KRX) close vs NXT after-market close
# ---------------------------------------------------------------------------

def naver_stock_minute(code, start_yyyymmddhhmm, end_yyyymmddhhmm):
    """1-minute bars (regular session only). Depth: recent days only (~1-2 wks)."""
    url = ('https://api.stock.naver.com/chart/domestic/item/%s/minute'
           '?startDateTime=%s&endDateTime=%s' % (code, start_yyyymmddhhmm, end_yyyymmddhhmm))
    return _json_get(url)


def krx_regular_close(code, yyyymmdd=None):
    """Regular-session close = price of the 15:30 closing-auction bar.

    Source A: naver minute chart bar localDateTime == <date>153000.
    Source B (fallback): naver PC tick page sise_time (row with 체결시각 15:30).
    Returns dict(date, close, source, closing_auction_volume) or None if the
    day has no 15:30 bar (holiday / not yet closed).
    """
    if yyyymmdd is None:
        yyyymmdd = _dt.date.today().strftime('%Y%m%d')
    bars = naver_stock_minute(code, yyyymmdd + '1520', yyyymmdd + '1535')
    for b in bars:
        if b['localDateTime'] == yyyymmdd + '153000':
            return {'date': yyyymmdd, 'close': b['currentPrice'], 'source': 'naver_minute_1530',
                    'closing_auction_volume': b['accumulatedTradingVolume']}
    # fallback: PC tick page (EUC-KR HTML)
    url = ('https://finance.naver.com/item/sise_time.naver?code=%s&thistime=%s153100&page=1'
           % (code, yyyymmdd))
    html = _get(url, {'Referer': 'https://finance.naver.com/item/sise.naver?code=%s' % code})
    text = _re.sub(r'<[^>]+>', ' ', html.decode('euc-kr', 'replace'))
    text = _re.sub(r'\s+', ' ', text)
    m = _re.search(r'15:30 ([\d,]+) ', text)
    if m:
        return {'date': yyyymmdd, 'close': _num(m.group(1)), 'source': 'naver_sise_time_1530',
                'closing_auction_volume': None}
    return None


def naver_stock_daily(code, start_yyyymmdd, end_yyyymmdd):
    """Daily OHLCV + foreignRetentionRate.
    CAVEAT (since 2026-09-14): on the current day open/high/low/volume are the
    regular session but closePrice is the NXT after-market (20:00) close.
    Use krx_regular_close() for the 15:30 print."""
    url = ('https://api.stock.naver.com/chart/domestic/item/%s/day'
           '?startDateTime=%s&endDateTime=%s' % (code, start_yyyymmdd, end_yyyymmdd))
    return _json_get(url)


def naver_stock_after_market(code):
    """NXT after-market block from polling endpoint: overPrice/open/high/low, session type."""
    j = _json_get('https://polling.finance.naver.com/api/realtime/domestic/stock/%s' % code)
    d = j['datas'][0]
    over = d.get('overMarketPriceInfo') or {}
    return {
        'regular_open': _num(d.get('openPrice')), 'regular_high': _num(d.get('highPrice')),
        'regular_low': _num(d.get('lowPrice')), 'regular_volume': _num(d.get('accumulatedTradingVolume')),
        'displayed_close': _num(d.get('closePrice')),  # == after-market close after 15:30
        'after_session_type': over.get('tradingSessionType'),
        'after_close': _num(over.get('overPrice')), 'after_open': _num(over.get('openPrice')),
        'after_high': _num(over.get('highPrice')), 'after_low': _num(over.get('lowPrice')),
        'after_traded_at': over.get('localTradedAt'), 'traded_at': d.get('localTradedAt'),
    }


def naver_stock_investor_trend(code, page_size=20, page=1):
    """Per-stock daily net buy in SHARES: foreigner/organ(institution)/individual + foreign hold ratio."""
    rows = _json_get('https://m.stock.naver.com/api/stock/%s/trend?pageSize=%d&page=%d' % (code, page_size, page))
    return [{'date': r['bizdate'], 'foreign_net_shares': _num(r['foreignerPureBuyQuant']),
             'inst_net_shares': _num(r['organPureBuyQuant']), 'indiv_net_shares': _num(r['individualPureBuyQuant']),
             'foreign_hold_pct': _num(r['foreignerHoldRatio']), 'close': _num(r['closePrice']),
             'volume': _num(r['accumulatedTradingVolume'])} for r in rows]


def daum_stock_investor_days(code6, page=1, per_page=20):
    """Daum per-stock daily foreign own shares + foreign/institution net buy volume."""
    url = ('https://finance.daum.net/api/investor/days?symbolCode=A%s&page=%d&perPage=%d'
           % (code6, page, per_page))
    return _json_get(url, {'Referer': 'https://finance.daum.net/'})['data']


# ---------------------------------------------------------------------------
# 2. KOSPI/KOSDAQ index history + daily investor flows
# ---------------------------------------------------------------------------

def naver_index_daily(index='KOSPI', start_yyyymmdd='20260101', end_yyyymmdd=None):
    """Daily OHLC + volume (천주) for KOSPI/KOSDAQ/KPI200."""
    if end_yyyymmdd is None:
        end_yyyymmdd = _dt.date.today().strftime('%Y%m%d')
    url = ('https://api.stock.naver.com/chart/domestic/index/%s/day'
           '?startDateTime=%s&endDateTime=%s' % (index, start_yyyymmdd, end_yyyymmdd))
    return _json_get(url)


def daum_index_investor_days(market='KOSPI', page=1, per_page=20):
    """Daily index close + individual/foreign/institution net buy VALUE in KRW (원).
    Returns rows with *_eok fields (억원) added."""
    url = ('https://finance.daum.net/api/market_index/days?market=%s&page=%d&perPage=%d&pagination=true'
           % (market, page, per_page))
    rows = _json_get(url, {'Referer': 'https://finance.daum.net/'})['data']
    out = []
    for r in rows:
        out.append({'date': r['date'][:10], 'close': r['tradePrice'], 'change': r['changePrice'],
                    'volume_k': r['accTradeVolume'], 'value_mn': r['accTradePrice'],
                    'indiv_eok': round(r['individualStraightPurchasePrice'] / 1e8),
                    'foreign_eok': round(r['foreignStraightPurchasePrice'] / 1e8),
                    'inst_eok': round(r['institutionStraightPurchasePrice'] / 1e8)})
    return out


def naver_investor_deal_trend_day(sosok='01', bizdate=None, page=1):
    """Naver PC 일자별 순매수 (단위: 억원) with institution sub-categories.
    sosok '01'=KOSPI, '02'=KOSDAQ. Columns: 개인 외국인 기관계 기관 기타법인 금융투자 보험 투신(사모) 은행 기타금융기관 연기금등."""
    if bizdate is None:
        bizdate = _dt.date.today().strftime('%Y%m%d')
    url = ('https://finance.naver.com/sise/investorDealTrendDay.naver?bizdate=%s&sosok=%s&page=%d'
           % (bizdate, sosok, page))
    html = _get(url).decode('euc-kr', 'replace')
    text = _re.sub(r'<script.*?</script>', '', html, flags=_re.S)
    text = _re.sub(r'\s+', ' ', _re.sub(r'<[^>]+>', ' ', text))
    # 11 cells per row. Header shows 12 labels because 기관 is a group header; verified
    # 2026-09-14: 금융투자+보험+투신+은행+기타금융+연기금 == 기관계, last cell is 기타법인.
    cols = ['indiv', 'foreign', 'inst_total', 'fin_invest', 'insurance', 'trust_private',
            'bank', 'other_fin', 'pension', 'other_corp']
    out = []
    for m in _re.finditer(r'(\d\d\.\d\d\.\d\d)((?: -?[\d,]+){10})(?= \d\d\.\d\d\.\d\d| |$)', text):
        vals = [_num(v) for v in m.group(2).split()]
        d = '20' + m.group(1).replace('.', '-')
        out.append(dict(zip(['date'] + cols, [d] + vals)))
    return out


def naver_breadth(market='KOSPI'):
    """Advancers/decliners count today. CAVEAT: category includes KOSPI-listed ETF/ETN,
    so up+down exceeds the number of common stocks."""
    up = _json_get('https://m.stock.naver.com/api/stocks/up/%s?page=1&pageSize=1' % market)
    dn = _json_get('https://m.stock.naver.com/api/stocks/down/%s?page=1&pageSize=1' % market)
    return {'market': market, 'up': up['totalCount'], 'down': dn['totalCount'],
            'marketStatus': up.get('marketStatus')}


# ---------------------------------------------------------------------------
# 3/4. Naver marketindex (energy, metals, agricultural, exchange, bond) + FRED
# ---------------------------------------------------------------------------

def naver_marketindex_list(category):
    """Snapshot list. category in energy|metals|agricultural|exchange.
    exchange returns {'normalList','majorList'}; others a list. 10-min delayed intraday."""
    return _json_get('https://api.stock.naver.com/marketindex/%s' % category)


def naver_marketindex_prices(category, reuters_code, page_size=10, page=1):
    """Daily history for one instrument.
    energy: CLcv1 (WTI) LCOcv1 (Brent) DCBc1 (Dubai) NGcv1 (Henry Hub) RBcv1 HOcv1 LGOcv1
    exchange: .DXY FX_USDKRW EURUSD ...   bond: US2YT=RR US10YT=RR US30YT=RR KR2YT=RR KR10YT=RR KR30YT=RR
    metals: GCcv1 ...  No TTF/JKM on naver."""
    url = ('https://api.stock.naver.com/marketindex/%s/%s/prices?page=%d&pageSize=%d'
           % (category, _up.quote(reuters_code, safe='=.'), page, page_size))
    rows = _json_get(url)
    return [{'traded_at': r['localTradedAt'], 'close': _num(r['closePrice']), 'open': _num(r.get('openPrice')),
             'high': _num(r.get('highPrice')), 'low': _num(r.get('lowPrice')),
             'chg': _num(r.get('fluctuations')), 'chg_pct': _num(r.get('fluctuationsRatio'))} for r in rows]


def naver_marketindex_basic(category, reuters_code):
    """Intraday snapshot for one instrument (bond is realtime; energy/exchange 10-min delayed)."""
    return _json_get('https://api.stock.naver.com/marketindex/%s/%s' % (category, _up.quote(reuters_code, safe='=.')))


def naver_foreign_index_daily(symbol, start_yyyymmdd, end_yyyymmdd):
    """Daily OHLC for foreign indices via chart API: .VIX .DXY .INX .DJI .IXIC .SOX ..."""
    url = ('https://api.stock.naver.com/chart/foreign/index/%s/day?startDateTime=%s&endDateTime=%s'
           % (symbol, start_yyyymmdd, end_yyyymmdd))
    return _json_get(url)


def fred_csv(series_id):
    """FRED daily CSV -> list of (date, float|None). Series confirmed:
    DGS30 DGS10 DFII10 T10YIE DTWEXBGS DTWEXAFEGS DHHNGSP DCOILBRENTEU DCOILWTICO VIXCLS
    BAMLH0A0HYM2 ; monthly: PNGASEUUSDM (TTF, USD/MMBtu) PNGASJPUSDM (Japan LNG import)."""
    b = _get('https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s' % series_id, {'User-Agent': UA_FRED})
    out = []
    for line in b.decode().strip().splitlines()[1:]:
        d, v = line.split(',', 1)
        out.append((d, float(v) if v not in ('', '.') else None))
    return out


def yahoo_chart(symbol, rng='1mo', interval='1d'):
    """Yahoo v8 chart. Works through the proxy but RATE-LIMITS after a burst
    (~15-20 rapid calls -> 429 for several minutes). Space calls >= 3-5 s apart.
    Confirmed symbols: 000660.KS 005930.KS ^KS11 ^KQ11 TTF=F NG=F BZ=F CL=F DX-Y.NYB ^TYX ^TNX ^VIX 7709.HK
    JKM=F exists but is sparse (many null closes, volume 0)."""
    url = ('https://query2.finance.yahoo.com/v8/finance/chart/%s?range=%s&interval=%s'
           % (_up.quote(symbol), rng, interval))
    j = _json_get(url, {'User-Agent': UA_BROWSER, 'Accept': '*/*'})
    r = j['chart']['result'][0]
    q = r['indicators']['quote'][0]
    rows = []
    for i, t in enumerate(r['timestamp']):
        rows.append({'date': _dt.datetime.utcfromtimestamp(t).strftime('%Y-%m-%d'),
                     'open': q['open'][i], 'high': q['high'][i], 'low': q['low'][i],
                     'close': q['close'][i], 'volume': q['volume'][i]})
    m = r['meta']
    return {'symbol': symbol, 'currency': m.get('currency'), 'exchange': m.get('exchangeName'),
            'last': m.get('regularMarketPrice'), 'rows': rows}


def tradingeconomics_headline(slug):
    """Scrapes the <meta name=description> sentence, e.g. slug 'eu-natural-gas' ->
    ('83.55', 'EUR/MWh', 'September 14, 2026'). Fragile HTML scrape; no JKM page exists."""
    html = _get('https://tradingeconomics.com/commodity/%s' % slug,
                {'User-Agent': UA_BROWSER, 'Accept': 'text/html'}).decode('utf-8', 'replace')
    m = _re.search(r'name="description" content="([^"]+)"', html)
    if not m:
        return None
    desc = m.group(1)
    v = _re.search(r'to ([\d.,]+) ([A-Za-z/]+) on ([A-Z][a-z]+ \d{1,2}, \d{4})', desc)
    return (v.group(1), v.group(2), v.group(3), desc) if v else (None, None, None, desc)


# ---------------------------------------------------------------------------
# 5. Sentiment
# ---------------------------------------------------------------------------

def cnn_fear_greed():
    """Needs browser-like headers (bare 'Mozilla/5.0' -> 418). Returns current + history list."""
    h = {'User-Agent': UA_BROWSER, 'Accept': 'application/json, text/plain, */*',
         'Referer': 'https://www.cnn.com/markets/fear-and-greed', 'Origin': 'https://www.cnn.com'}
    j = _json_get('https://production.dataviz.cnn.io/index/fearandgreed/graphdata', h)
    fg = j['fear_and_greed']
    hist = [(_dt.datetime.utcfromtimestamp(p['x'] / 1000).strftime('%Y-%m-%d'), p['y'])
            for p in j['fear_and_greed_historical']['data']]
    return {'score': fg['score'], 'rating': fg['rating'], 'timestamp': fg['timestamp'],
            'previous_close': fg['previous_close'], 'previous_1_week': fg['previous_1_week'],
            'previous_1_month': fg['previous_1_month'], 'history': hist}


def cboe_put_call(yyyy_mm_dd):
    """CBOE daily put/call ratios. 403 until the day's file is published (US evening)."""
    j = _json_get('https://cdn.cboe.com/data/us/options/market_statistics/daily/%s_daily_options' % yyyy_mm_dd,
                  {'User-Agent': UA_BROWSER})
    return {r['name']: float(r['value']) for r in j['ratios']}


def cboe_vix_history():
    """Full VIX OHLC history CSV since 1990 (DATE,OPEN,HIGH,LOW,CLOSE)."""
    b = _get('https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv', {'User-Agent': UA_BROWSER})
    return [l.split(',') for l in b.decode().strip().splitlines()[1:]]


# ---------------------------------------------------------------------------
# 6. ETFs (KR single-stock 2x; HK CSOP)
# ---------------------------------------------------------------------------

def naver_etf_list(keyword=None):
    """All KR ETFs (cp949 JSON): itemcode itemname nav nowVal marketSum(억) quant etfTabCode."""
    b = _get('https://finance.naver.com/api/sise/etfItemList.nhn')
    items = _json.loads(b.decode('cp949'))['result']['etfItemList']
    if keyword:
        items = [x for x in items if keyword in x['itemname']]
    return items


def naver_etf_basic(code):
    """KR ETF snapshot: nav (prev official NAV), iNav (intraday), totalNav (AUM, '2조 4,788억'),
    marketValue, deviationRate, etfBaseIndex, issuerName. Adds aum_eok/mcap_eok ints."""
    j = _json_get('https://m.stock.naver.com/api/etf/%s/basic' % code)
    return {'code': code, 'name': j['stockName'], 'close': _num(j['closePrice']), 'nav': _num(j.get('nav')),
            'iNav': _num(j.get('iNav')), 'aum_eok': krw_units_to_eok(j.get('totalNav')),
            'mcap_eok': krw_units_to_eok(j.get('marketValue')), 'deviation_pct': j.get('deviationRate'),
            'base_index': j.get('etfBaseIndex'), 'issuer': j.get('issuerName'),
            'volume': _num(j.get('accumulatedTradingVolume')), 'traded_at': j.get('localTradedAt'),
            'session': j.get('marketSessionType')}


def naver_etf_constituents(code):
    return _json_get('https://m.stock.naver.com/api/etf/%s/constituent' % code)


def naver_world_stock_basic(reuters_code):
    """e.g. '7709.HK' (CSOP SK Hynix Daily Max 2x). stockItemTotalInfos has 시총 (market cap in HKD),
    거래량, 대금. No NAV/AUM field for HK ETPs on naver; use 시총 as AUM proxy."""
    j = _json_get('https://api.stock.naver.com/stock/%s/basic' % reuters_code)
    info = {t['code']: t.get('value') for t in j.get('stockItemTotalInfos', [])}
    return {'name': j['stockName'], 'close': _num(j['closePrice']), 'traded_at': j['localTradedAt'],
            'currency': (j.get('currencyType') or {}).get('code'), 'info': info}


def naver_foreign_item_daily(reuters_code, start_yyyymmdd, end_yyyymmdd):
    url = ('https://api.stock.naver.com/chart/foreign/item/%s/day?startDateTime=%s&endDateTime=%s'
           % (reuters_code, start_yyyymmdd, end_yyyymmdd))
    return _json_get(url)


# ---------------------------------------------------------------------------
# 7. CFTC Commitments of Traders
# ---------------------------------------------------------------------------

CFTC_DISAGG_FUT = '72hh-3qpy'   # Disaggregated, futures only
CFTC_LEGACY_FUT = '6dca-aqww'   # Legacy, futures only
CFTC_CODES = {'NG_HENRY_HUB': '023651', 'WTI_PHYSICAL': '067651'}


def cftc_cot(contract_code, dataset=CFTC_DISAGG_FUT, limit=4):
    """Socrata JSON, newest first. Weekly (Tuesday positions, released Friday 15:30 ET).
    Disaggregated fields: m_money_positions_long_all/short_all, prod_merc_positions_long/short,
    swap_positions_long_all, other_rept_positions_long_all, open_interest_all."""
    url = ('https://publicreporting.cftc.gov/resource/%s.json?cftc_contract_market_code=%s'
           '&$order=report_date_as_yyyy_mm_dd%%20DESC&$limit=%d' % (dataset, contract_code, limit))
    return _json_get(url, {'User-Agent': UA_BROWSER, 'Accept': 'application/json'})


def cftc_cot_managed_money(contract_code, limit=4):
    rows = cftc_cot(contract_code, CFTC_DISAGG_FUT, limit)
    return [{'date': r['report_date_as_yyyy_mm_dd'][:10], 'market': r['market_and_exchange_names'],
             'oi': int(r['open_interest_all']),
             'mm_long': int(r['m_money_positions_long_all']), 'mm_short': int(r['m_money_positions_short_all']),
             'mm_net': int(r['m_money_positions_long_all']) - int(r['m_money_positions_short_all']),
             'prod_long': int(r.get('prod_merc_positions_long') or 0), 'prod_short': int(r.get('prod_merc_positions_short') or 0)}
            for r in rows]


if __name__ == '__main__':
    import pprint
    pprint.pprint(krx_regular_close('000660', '20260914'))
