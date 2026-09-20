#!/usr/bin/env python3
"""수집된 하원 PTR 텍스트를 거래 단위로 판다 — intake/files/congress/{년}/*.txt → 구조화.

수집 층의 파서. 판단은 하지 않는다(금액은 구간 그대로 · 비중 환산 금지 §J12-2).
2026-09-20 1차 측정: 26건 중 텍스트 추출 12건(46%) · 나머지는 구형 DocID(8자리) 스캔본.
용법: parse_ptr.py [연도]   (기본 올해 · 결과는 stdout JSON)
"""
import re, io, os, json, glob, sys
from datetime import date
YEAR=next((a for a in sys.argv[1:] if re.fullmatch(r'20\d\d',a)), str(date.today().year))
DIR='intake/files/congress/'+YEAR
meta={}
for l in open('intake/collected.jsonl'):
    if not l.strip(): continue
    d=json.loads(l)
    if d.get('kind')=='congress' and d.get('doc_id'): meta[str(d['doc_id'])]=d

TX=re.compile(r'^(SP|JT|DC)?\s*(.+?)\s*\[(\w{2,3})\]\s*\n\s*(P|S|S \(partial\)|E)\s+(\d{2}/\d{2}/\d{4})\s+(\d{2}/\d{2}/\d{4})\s+\$([\d,]+)\s*-?\s*\n?\$?([\d,]+)?',re.M)
rows=[]
for f in sorted(glob.glob(DIR+'/*.txt')):
    doc=os.path.basename(f)[:-4]; m=meta.get(doc,{})
    # 2022년 이후 PDF 는 텍스트 레이어의 공백이 NUL(\x00) 로 나온다 — 그대로 두면 \s+ 가 접지 못해
    # 자산명 병합과 DESCRIPTION 추출이 통째로 실패한다(2026-09-20 측정에서 발견)
    t=io.open(f,encoding='utf8').read().replace('\x00',' ')
    # 자산명이 여러 줄로 쪼개진다 — [XX] 앞까지를 한 덩어리로 합친다
    flat=re.sub(r'\n(?![A-Z]{2}\s|\s*(P|S|E)\s+\d{2}/)',' ',t)
    for mt in TX.finditer(flat):
        own,asset,atype,tx,d1,d2,a1,a2=mt.groups()
        asset=re.sub(r'\s+',' ',asset).strip()
        tick=(re.search(r'\(([A-Z\.]{1,6})\)\s*$',asset) or [None,None])[1]
        rows.append({"doc":doc,"member":m.get('member','?'),"filed":m.get('filed'),
                     "owner":own or "—","asset":asset,"ticker":tick,"asset_type":atype,
                     "tx":tx,"date":d1,"amt_lo":int(a1.replace(',','')),
                     "amt_hi":int(a2.replace(',','')) if a2 else None})
out=os.environ.get('OUT')
if out: json.dump(rows,open(out,'w'),ensure_ascii=False,indent=1)
print('파싱 거래',len(rows),'/ 파일',len(glob.glob(DIR+'/*.txt')))
from collections import Counter
c=Counter(r['member'] for r in rows); print('의원별:',dict(c))
print('유형:',dict(Counter(r['asset_type'] for r in rows)))
print('매수/매도:',dict(Counter(r['tx'] for r in rows)))
