import json, urllib.request, time, sys, io, csv
UA={"User-Agent":"Mozilla/5.0"}
def get(url, headers=UA, timeout=20):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=timeout) as r:
            return r.read().decode("utf-8","replace"), None
    except Exception as e:
        return None, repr(e)
START,END="202408010000","202609200000"
cands={"XLE":["XLE","XLE.K"],"XOP":["XOP","XOP.K"],"LNG":["LNG","LNG.K"],"WMB":["WMB","WMB.K"],"KMI":["KMI","KMI.K"],
 "ET":["ET","ET.K"],"TRGP":["TRGP.K","TRGP"],"EPD":["EPD","EPD.K"],"FANG":["FANG.O"],"EOG":["EOG","EOG.K"],"COP":["COP","COP.K"],
 "EQT":["EQT","EQT.K"],"CVX":["CVX","CVX.K"],"XOM":["XOM","XOM.K"],"VG":["VG","VG.K"],"USO":["USO","USO.K"],"BNO":["BNO","BNO.K"],"SPY":["SPY","SPY.K"]}
log=[]; out={}
for k,syms in cands.items():
    for s in syms:
        url=f"https://api.stock.naver.com/chart/foreign/item/{s}/day?startDateTime={START}&endDateTime={END}"
        txt,err=get(url)
        ok=False
        if txt:
            try:
                d=json.loads(txt)
                rows=[(x["localDate"],float(x["closePrice"])) for x in d if x.get("closePrice")]
                if len(rows)>50:
                    out[k]=rows; ok=True
                    log.append({"host":"api.stock.naver.com","path":f"/chart/foreign/item/{s}/day","status":f"ok n={len(rows)} {rows[0][0]}..{rows[-1][0]}"})
                    break
                else: log.append({"host":"api.stock.naver.com","path":f"/chart/foreign/item/{s}/day","status":f"empty n={len(rows)}"})
            except Exception as e:
                log.append({"host":"api.stock.naver.com","path":f"/chart/foreign/item/{s}/day","status":f"parse-fail {txt[:80]!r}"})
        else:
            log.append({"host":"api.stock.naver.com","path":f"/chart/foreign/item/{s}/day","status":f"fail {err[:80]}"})
        time.sleep(0.3)
# Korean refiners + KOSPI
for k,s in {"S-Oil":"010950","SKInnovation":"096770","SKH":"000660"}.items():
    url=f"https://api.stock.naver.com/chart/domestic/item/{s}/day?startDateTime={START}&endDateTime={END}"
    txt,err=get(url)
    if txt:
        d=json.loads(txt); rows=[(x["localDate"],float(x["closePrice"])) for x in d if x.get("closePrice")]
        out[k]=rows; log.append({"host":"api.stock.naver.com","path":f"/chart/domestic/item/{s}/day","status":f"ok n={len(rows)} {rows[0][0]}..{rows[-1][0]}"})
    else: log.append({"host":"api.stock.naver.com","path":f"/chart/domestic/item/{s}/day","status":f"fail {err}"})
url=f"https://api.stock.naver.com/chart/domestic/index/KOSPI/day?startDateTime={START}&endDateTime={END}"
txt,err=get(url)
if txt:
    d=json.loads(txt); rows=[(x["localDate"],float(x["closePrice"])) for x in d if x.get("closePrice")]
    out["KOSPI"]=rows; log.append({"host":"api.stock.naver.com","path":"/chart/domestic/index/KOSPI/day","status":f"ok n={len(rows)} {rows[0][0]}..{rows[-1][0]}"})
else: log.append({"host":"api.stock.naver.com","path":"/chart/domestic/index/KOSPI/day","status":f"fail {err}"})
# FRED
FUA={"User-Agent":"ourprochoi Research (kenchoi@keywestaim.com)"}
for sid in ("DCOILBRENTEU","DCOILWTICO"):
    txt,err=get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}",FUA,30)
    if txt:
        rows=[]
        for r in csv.DictReader(io.StringIO(txt)):
            v=r.get(sid) or r.get('value')
            if v and v!='.':
                rows.append((r['observation_date'].replace('-',''), float(v)))
        rows=[r for r in rows if r[0]>="20240801"]
        out[sid]=rows; log.append({"host":"fred.stlouisfed.org","path":f"/graph/fredgraph.csv?id={sid}","status":f"ok n={len(rows)} {rows[0][0]}..{rows[-1][0]}"})
    else: log.append({"host":"fred.stlouisfed.org","path":f"/graph/fredgraph.csv?id={sid}","status":f"fail {err}"})
json.dump(out,open("series.json","w")); json.dump(log,open("fetch_log.json","w"),indent=1)
for l in log: print(l)
