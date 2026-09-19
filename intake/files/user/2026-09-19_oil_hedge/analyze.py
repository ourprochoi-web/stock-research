import json, math, csv
S=json.load(open("series.json"))
def tomap(rows): return {d:c for d,c in rows}
def logret(rows):
    rows=sorted(rows); out={}
    for i in range(1,len(rows)):
        if rows[i][1]>0 and rows[i-1][1]>0: out[rows[i][0]]=math.log(rows[i][1]/rows[i-1][1])
    return out
def stats(x,y):
    n=len(x); 
    if n<20: return None
    mx=sum(x)/n; my=sum(y)/n
    sxx=sum((a-mx)**2 for a in x); syy=sum((b-my)**2 for b in y); sxy=sum((a-mx)*(b-my) for a,b in zip(x,y))
    beta=sxy/sxx; r=sxy/math.sqrt(sxx*syy); return {"beta":round(beta,3),"r":round(r,3),"r2":round(r*r,3),"n":n}
R={k:logret(v) for k,v in S.items()}
# align on dates
def pair(a,b,start="20250901",end="20261231",lag_b=0):
    """returns list (ra, rb) on common dates; lag_b=1 means b's return on next trading date of b after a's date"""
    ra=R[a]; rb=R[b]; bd=sorted(rb)
    x=[];y=[]
    for d in sorted(ra):
        if d<start or d>end: continue
        if lag_b==0:
            if d in rb: x.append(ra[d]); y.append(rb[d])
        else:
            nxt=[q for q in bd if q>d]
            if nxt: x.append(ra[d]); y.append(rb[nxt[0]])
    return x,y
cands=["XLE","XOP","USO","BNO","LNG","WMB","KMI","ET","TRGP","EPD","FANG","EOG","COP","EQT","CVX","XOM","VG","S-Oil","SKInnovation","SPY"]
windows={"250d":("20250915","20260919"),"2026war":("20260301","20260919")}
res={}
for c in cands:
    row={"symbol":c}
    for wn,(s,e) in windows.items():
        x,y=pair("DCOILBRENTEU",c,s,e); st=stats(x,y); row[f"brent_{wn}"]=st
        x,y=pair("DCOILWTICO",c,s,e); st=stats(x,y); row[f"wti_{wn}"]=st
        # oil lag: US equity same day vs brent; Korean names react next day -> lag
        if c in ("S-Oil","SKInnovation"):
            x,y=pair("DCOILBRENTEU",c,s,e,lag_b=1); row[f"brent_{wn}_krlag1"]=stats(x,y)
        # KOSPI corr: same date and KR next day
        x,y=pair(c,"KOSPI",s,e); row[f"kospi_{wn}"]=stats(x,y)
        x,y=pair(c,"KOSPI",s,e,lag_b=1); row[f"kospi_{wn}_lag1"]=stats(x,y)
        x,y=pair(c,"SKH",s,e); row[f"skh_{wn}"]=stats(x,y)
        x,y=pair(c,"SKH",s,e,lag_b=1); row[f"skh_{wn}_lag1"]=stats(x,y)
        x,y=pair(c,"SPY",s,e); row[f"spy_{wn}"]=stats(x,y)
    res[c]=row
# ---- spike windows: 2 largest 10-trading-day Brent up-moves in 2026 (non-overlapping)
br=sorted([r for r in S["DCOILBRENTEU"] if r[0]>="20260101"])
moves=[]
for i in range(10,len(br)):
    moves.append((br[i][1]/br[i-10][1]-1, br[i-10][0], br[i][0], br[i-10][1], br[i][1]))
moves.sort(reverse=True)
chosen=[]
for m in moves:
    if all(m[2]<c[1] or m[1]>c[2] for c in chosen): chosen.append(m)
    if len(chosen)==2: break
# also top down-moves (hedge symmetry: what happens on ceasefire-type relief)
downs=[]
for m in sorted(moves):
    if all(m[2]<c[1] or m[1]>c[2] for c in downs): downs.append(m)
    if len(downs)==2: break
def ret_between(sym,d0,d1,lag=0):
    rows=sorted(S[sym]); 
    p0=[c for d,c in rows if d<=d0]; p1=[c for d,c in rows if d<=d1]
    if lag:  # Korean: shift one trading day forward
        p0=[c for d,c in rows if d<=d0]; nx=[c for d,c in rows if d>d1]
        p1 = p1 if not nx else p1+[nx[0]]
    if not p0 or not p1: return None
    return round(p1[-1]/p0[-1]-1,4)
spike={}
for tag,m in [("up1",chosen[0]),("up2",chosen[1]),("down1",downs[0]),("down2",downs[1])]:
    w={"brent_move":round(m[0],4),"from":m[1],"to":m[2],"brent_from":m[3],"brent_to":m[4],"returns":{}}
    for c in cands+["KOSPI","SKH"]:
        w["returns"][c]=ret_between(c,m[1],m[2],lag=1 if c in ("KOSPI","SKH","S-Oil","SKInnovation") else 0)
    spike[tag]=w
json.dump({"stats":res,"spike":spike},open("results.json","w"),indent=1)
# print compact
print("SPIKE WINDOWS"); 
for k,w in spike.items(): print(k,w["from"],w["to"],w["brent_from"],w["brent_to"],w["brent_move"])
print()
hdr=["sym","bB250","r2","bB26","r2","bW26","cKOSPI250","cKOSPI250lag","cKOSPI26","cKOSPI26lag","cSKH250","cSKH26lag","cSPY26","up1","up2","dn1","dn2"]
print("\t".join(hdr))
for c in cands+["KOSPI","SKH"]:
    r=res.get(c,{})
    g=lambda k,f="beta": (r.get(k) or {}).get(f)
    print("\t".join(str(v) for v in [c,g("brent_250d"),g("brent_250d","r2"),g("brent_2026war"),g("brent_2026war","r2"),g("wti_2026war"),
        g("kospi_250d","r"),g("kospi_250d_lag1","r"),g("kospi_2026war","r"),g("kospi_2026war_lag1","r"),g("skh_250d","r"),g("skh_2026war_lag1","r"),g("spy_2026war","r"),
        spike["up1"]["returns"][c],spike["up2"]["returns"][c],spike["down1"]["returns"][c],spike["down2"]["returns"][c]]))
print("KR refiner brent lag1 (2026war):",res["S-Oil"].get("brent_2026war_krlag1"),res["SKInnovation"].get("brent_2026war_krlag1"))
print("KR refiner brent lag1 (250d):",res["S-Oil"].get("brent_250d_krlag1"),res["SKInnovation"].get("brent_250d_krlag1"))
# brent path 2026 monthly
print("BRENT 2026 month-ends:", [(d,c) for d,c in br if d[6:]>="27"][::1][-12:])
print("last brent", br[-3:])
