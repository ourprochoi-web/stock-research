import json, urllib.request, time, re, html
UA={"User-Agent":"ourprochoi Research (kenchoi@keywestaim.com)","Accept-Encoding":"identity"}
def get(url,timeout=60):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout) as r: return r.read().decode("utf-8","replace"),None
    except Exception as e: return None,repr(e)
log=[]
txt,err=get("https://www.sec.gov/files/company_tickers.json")
log.append({"host":"www.sec.gov","path":"/files/company_tickers.json","status":"ok" if txt else f"fail {err}"})
ct=json.loads(txt); tick={v["ticker"]:v["cik_str"] for v in ct.values()}
want=["WMB","KMI","ET","TRGP","EPD","LNG","VG","EOG"]
ciks={w:tick.get(w) for w in want}; print(ciks)
KEYS=[r"fee[- ]based",r"take[- ]or[- ]pay",r"minimum volume commitment",r"commodity price exposure",r"commodity[- ]based",r"percent of (?:our )?(?:adjusted )?(?:EBITDA|gross margin|segment margin|margin)",r"% of (?:our )?(?:adjusted )?(?:EBITDA|gross margin|segment margin|margin)",r"long-term (?:SPA|sale and purchase agreement)",r"fixed fee",r"contracted"]
out={}
for t in want:
    cik=ciks[t]
    if not cik: continue
    s,err=get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    log.append({"host":"data.sec.gov","path":f"/submissions/CIK{cik:010d}.json","status":"ok" if s else f"fail {err}"})
    if not s: continue
    sub=json.loads(s); f=sub["filings"]["recent"]
    picks=[]
    for form,acc,doc,date in zip(f["form"],f["accessionNumber"],f["primaryDocument"],f["filingDate"]):
        if form in ("10-K","10-Q") and len(picks)<2 and not any(p[0]==form for p in picks): picks.append((form,acc,doc,date))
    out[t]={"cik":cik,"filings":[]}
    for form,acc,doc,date in picks:
        url=f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-','')}/{doc}"
        time.sleep(0.4)
        body,err=get(url,120)
        log.append({"host":"www.sec.gov","path":url.split("sec.gov")[1],"status":f"ok {len(body)//1000}kB" if body else f"fail {err}"})
        if not body: continue
        text=re.sub(r"<[^>]+>"," ",body); text=html.unescape(text); text=re.sub(r"\s+"," ",text)
        hits=[]
        for k in KEYS:
            for m in re.finditer(k,text,flags=re.I):
                a=max(0,m.start()-260); b=min(len(text),m.end()+260)
                snip=text[a:b]
                if re.search(r"\d{1,3}(?:\.\d)?\s?%|percent",snip,re.I): hits.append(snip)
        # dedupe
        seen=set(); uniq=[]
        for h in hits:
            key=h[100:220]
            if key in seen: continue
            seen.add(key); uniq.append(h)
        out[t]["filings"].append({"form":form,"date":date,"url":url,"n_hits":len(uniq),"hits":uniq[:40]})
        open(f"10k_{t}_{form}.txt","w").write(text)
json.dump(out,open("sec_hits.json","w"),indent=1); json.dump(log,open("sec_log.json","w"),indent=1)
for l in log: print(l)
for t,v in out.items():
    for fl in v["filings"]: print(t,fl["form"],fl["date"],"hits",fl["n_hits"])
