#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""시총 상위 N종목 수급 수집 — 「시장」을 말할 때 쓰는 표본.

2026-09-22 신설. 그날 「외국인이 많이 판 사분위가 가장 많이 올랐다」를 추적 유니버스
173종목으로 재고 판단을 냈는데, 시총 상위 549종목으로 넓히자 격차가 5.97%p → 0.80%p로
7.5배 줄었다. **추적 유니버스(update_prices.py WATCH)는 AI·반도체·테마 편향 표본**이고
「시장」을 말하는 데 쓰면 안 된다.

커버리지(2026-09-22 실측): 상위 100 = 85.7% · 200 = 91.2% · 300 = 93.7%
· **500 = 96.0%** · 800 = 97.6%. 549종목 수집에 50초.

⚠ 이 소스가 못 주는 것 — 기타법인·연기금 분해(naver는 개인·외국인·기관 셋뿐).
그래서 10일 누적 합이 −17.1조 어긋나는데 메우는 주체를 못 찾는다(open: flow-mismatch).
"""

def fetch_all_list():
    """KOSPI+KOSDAQ 전종목 리스트(시총·등락·거래대금). pageSize 최대 100."""
    H={"User-Agent":"Mozilla/5.0","Referer":"https://m.stock.naver.com/"}
    def g(u,retry=3):
        for i in range(retry):
            try: return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=H),timeout=20).read())
            except Exception:
                if i==retry-1: raise
                time.sleep(0.5)
    def num(x):
        try: return float(str(x).replace(',',''))
        except: return None
    ALL={}
    for mkt in ['KOSPI','KOSDAQ']:
        p=1
        while True:
            d=g(f"https://m.stock.naver.com/api/stocks/marketValue/{mkt}?page={p}&pageSize=100")
            for s in d['stocks']:
                ALL[s['itemCode']]={'name':s['stockName'],'mkt':mkt,'code':s['itemCode'],
                  'close':num(s.get('closePriceRaw') or s.get('closePrice')),
                  'chg':num(s.get('fluctuationsRatio')),
                  'mcap':num(s.get('marketValueRaw') or s.get('marketValue')),
                  'tval':num(s.get('accumulatedTradingValueRaw') or s.get('accumulatedTradingValue')),
                  'type':s.get('stockEndType')}
            if len(d['stocks'])<100 or p*100>=d['totalCount']: break
            p+=1
    return ALL

import json, urllib.request, re, time
import os
S=os.path.dirname(os.path.abspath(__file__))+'/'
B=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+'/'
ALL=fetch_all_list()
stk=[v for v in ALL.values() if v['type']=='stock' and v['mcap']]
stk.sort(key=lambda x:-x['mcap'])
top=stk[:500]
# 추적 유니버스 합집합
src=open(B+'portfolio/data/update_prices.py',encoding='utf-8').read()
watch=set()
for m in re.finditer(r'"([^"]+)"\s*:\s*"([0-9A-Z]{6})"', src):
    if re.match(r'^[0-9]{6}$|^[0-9]{4}[A-Z][0-9]$',m.group(2)): watch.add(m.group(2))
codes={v['code']:v for v in top}
add=0
for c in watch:
    if c not in codes and c in ALL:
        codes[c]=ALL[c]; add+=1
print('대상 %d종목 (상위500 + 추적 추가 %d)'%(len(codes),add))
H={"User-Agent":"Mozilla/5.0","Referer":"https://m.stock.naver.com/"}
def num(s):
    try: return int(str(s).replace(',','').replace('+',''))
    except: return None
def hr(x):
    try: return float(str(x).replace('%',''))
    except: return None
out={}; fail=[]
t0=time.time()
for i,(c,meta) in enumerate(codes.items()):
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(
          f"https://m.stock.naver.com/api/stock/{c}/trend",headers=H),timeout=12).read())
        if not isinstance(d,list) or not d: fail.append(c); continue
        rows=[{'d':r['bizdate'],'f':num(r.get('foreignerPureBuyQuant')),'o':num(r.get('organPureBuyQuant')),
               'i':num(r.get('individualPureBuyQuant')),'hr':hr(r.get('foreignerHoldRatio')),
               'px':num(r.get('closePrice'))} for r in d]
        out[c]={**meta,'rows':rows}
    except Exception:
        fail.append(c)
    if i and i%50==0: print('  %d/%d  %.0fs'%(i,len(codes),time.time()-t0),flush=True)
print('완료 %d · 실패 %d · %.0fs'%(len(out),len(fail),time.time()-t0))
json.dump(out,open(S+'top500_trend.json','w'),ensure_ascii=False)
