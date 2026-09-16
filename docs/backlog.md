# 백로그 — 시작점 지표 · 측정 명령 (판정 이벤트·미착수는 brain/)

**세션을 시작할 때 이 파일을 연다.** 규칙(`CLAUDE.md`)이 아니라 <u>상태</u>다 — 무엇을 판정할 차례이고 무엇이 남았는지.
2026-09-13에 `CLAUDE.md` §I-1·§I-3·§I-4에서 <u>한 글자도 고치지 않고</u> 옮겼다(경위는 `rules_journal.md#restructure-0913`).
**판정 이벤트가 도래하면 표에서 <u>지우는 것이 판정의 일부</u>다.** 원문 경로(구 §I-2)는 `method_datasource.md`로 갔다.

---

## 1. 다음 세션 시작점

**갱신일 2026-09-12.** 이 절은 <u>서술을 담지 않는다</u> — 무엇을 판정할 차례이고 무엇이 남았는지만 담는다.
그날의 경위·사용자 지적·신설 편 목록은 `journal#prev-start`.

**지표**(2026-09-08 실측): §0 규칙5 **0편** · `[미검증]` **0건** · 판단 보유 **88/155(56.8%)** · **추적 종목 170**(국내 91·해외 79 · 09-08 +8) ·
🟠 **판단 신선도 30일 초과 4편**(전일 0편) — `ns_korea_impact_strategy` · `ns_china_ai_ecosystem` ·
`ai_power_top5_picks` · `ai_power_company_nuclear_smr`(2026-09-08 갱신 완료).
**나머지 셋은 규칙 6대로 손댈 때 적용한다.**

**🔴 판단은 있는데 시세가 없는 종목 — 2026-09-08 신설.**
**「판정 이벤트를 걸어 놓고 그 종목 시세를 안 받는」 공백이다.** 오늘 하루에 **두 번** 걸렸다 —
**① 원전 3사**(T1 반증 조건을 재려는데 4사 중 3사가 추적 밖. 남은 하나는 **가스터빈 겸업이라 대리변수가 오염**)
**② 탈모 3사**(어제 판정 이벤트를 걸고 시세는 안 넣어, 다음에 또 손으로 받게 돼 있었다).
**세는 법**: 판단 보유 페이지의 주요 종목이 `prices.json`의 `prices`·`us`에 있는가.
**2026-09-08 감사 — 주요 25종목 중 미추적 8건**(상장 5 + 비상장 3) → **상장 5건 전부 해소**.

**🔑 그리고 마지막 하나(키옥시아)가 <u>「경로가 없다」가 아니라 「코드가 틀렸다」</u>였다** —
`6600.T`·`6600.JP`·`KIOXIA` 등 **8종을 시도해 전부 409**여서 「네이버가 일본 종목을 안 준다」고 적을 뻔했는데,
**도요타(`7203.T`)로 대조하니 열렸다.** **형식은 맞고 코드가 틀렸던 것이다** —
**6600은 옛 도시바메모리 코드**이고 키옥시아 홀딩스는 **2024-12-18 도쿄 프라임 상장 시 `285A`**를 받았다.
**📌 규칙 — <u>「이 소스는 X를 지원하지 않는다」고 적기 전에 <b>같은 소스의 다른 X로 대조</b>한다</u>**(§G).
**§H0의 「차단됐다고 적기 전에 호스트 단위로 확인한다」와 같은 형태이며, 이번은 <u>티커 단위</u>다.**
**⚠ 추적 추가는 <u>새 저장소가 아니라 기존 `update_prices.py`의 목록</u>이므로 §H에 걸리지 않는다.**

**🔴 R5 건너뜀 — 누적 2건**(2026-09-07 · IB 9건 배치 · 텍사스 대미투자 배치).
**세는 법**: 배치를 처리한 세션에서 **위 「남은 미착수」 표를 읽었는가**. 안 읽었으면 +1이고 여기에 적는다.
**판정**: 누적 10건에 도달하거나 **미착수 항목이 30일 이상 방치되면** §H 예외(훅 강제) 여부를 논의한다.

**다가오는 판정 이벤트 · 남은 미착수 → `brain/events.json` · `brain/open.json`으로 이동(2026-09-13).**
이 파일에는 표를 두지 않는다 — 두 곳에 있으면 한 곳이 낡는다. 판정 이벤트는 도래하면 판정하고 `events.json`에서 지운다.

## 2. 판정 시 주의 — 숫자가 좋아진 것과 방식이 작동한 것은 다르다

기준선 4개가 모두 0으로 갔지만, 이것은 **한 번의 집중 작업으로 밀어낸 결과**다. 이 방식이
실제로 작동하는지는 **다음 정보가 들어왔을 때** 판정된다. 진짜 판정 지표는 이것이다.

- **새 사실이 들어왔을 때 본문이 고쳐지는가, 아니면 아래에 블록이 하나 더 붙는가.**
  Tier 1에서 반복해서 발견한 실패 양상이 정확히 이것이었다 — 편집자 주에 "본문 기준가가
  낡았다", "R3의 전제가 흔들렸다"라고 **적어만 두고 본문은 그대로** 두는 것. 경고를 적는
  순간이 곧 고칠 순간이다.
- **"최근 변경 3~5건" 상한이 지켜지는가.** 이 상한이 페이지 길이 상한을 만든다. 6건째를
  붙이고 싶어지면 그것은 본문에 병합할 내용이라는 뜻이다.



## 3. 측정 명령 — 지표를 손으로 세지 않는다

**`[미검증]`이 38건으로 멈춰 있는 동안 실제로는 60건이 됐다.** 지표를 수기로 적으면
**지표 자체가 낡고, 낡은 지표는 개선을 감춘다.** F4 `desc`처럼 명령을 박는다.
**새 저장소를 만들지 않는다 — 세는 명령 한 줄이다.**

```
# §0 규칙5 — <양방향>으로 검사한다 (2026-08-22 보강)
#   기존 검사는 「판단 < dateModified」만 봤는데, 반대(판단이 <미래>)도 결함이다.
#   실측: 미래 날짜 3편이 6일간 검출되지 않았다(08-16 커밋인데 판단 08.18).
python3 - <<'EOF'
import glob,io,re
for f in glob.glob('*/*.html'):
    if 'update_log' in f: continue
    s=io.open(f,encoding='utf8',errors='ignore').read()
    dm=re.search(r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})"',s)
    tj=re.search(r'현재 판단 · (\d{4})\.(\d{2})\.(\d{2})',s)
    if dm and tj:
        d2=f"{tj.group(1)}-{tj.group(2)}-{tj.group(3)}"
        if d2<dm.group(1): print('과거',f,d2,dm.group(1))
        if d2>dm.group(1): print('🔴미래',f,d2,dm.group(1))
EOF

# [미검증] — update_log 제외 (본문만)
grep -ro '\[미검증\]' --include='*.html' --exclude=update_log.html . | wc -l

# 판단 보유 페이지 / 전체
#   🔴 2026-09-12 수정 — 종전 명령은 <문자열> '현재 판단'을 세어 "현재 판단이 0편이다" 같은
#   <서술>까지 6편 과대 계상했다(93 vs 87). §G가 [미검증]에서 두 번 겪은 것과 같은 형태다.
#   날짜 패턴으로 바꾸고 분모는 index.html DATA(연구 페이지)로 고정한다.
echo "$(grep -rlE '현재 판단 · [0-9]{4}' --include='*.html' */ | grep -v update_log | wc -l) / $(node -e "
const t=require('fs').readFileSync('index.html','utf8');
eval('var D='+t.match(/var DATA = \[[\s\S]*?\n  \];/)[0].replace(/^var DATA = /,'').replace(/;$/,''));
console.log(D.length)")"

# 시도 없는 불가 판정 (읽고 §G 기준으로 걸러야 한다 — grep은 후보만 좁힌다)
#   🔴 2026-09-12 수정 — 후보의 <61%>가 「「확인할 수 없다」가 아니라…」 같은 <규칙 자기인용>이었다.
#   페이지가 §G를 인용할수록 지표가 오르는 구조였다. 자기인용을 뺀다.
grep -rn '확보하지 못\|확인할 수 없\|검증 불가\|산출 불가\|역산 불가' --include='*.html' . \
  | grep -v update_log | grep -v '가 아니라\|은 다르\|는 다르\|§G' | wc -l

# 🔴 본문 인라인 날짜 마커 — §0 규칙4가 「최근 변경」만 세는 사이 여기로 샌다 (2026-09-12 신설)
#   실측: 선언값 「최근 변경 N건」 초과는 0편인데 인라인 마커는 551개이고 <상위 2편이 220개(40%)>다.
#   memory_cycle 72K→472K(6.5배) · value_chain_guide_v2 133K→511K(3.8배), 35일간 약 11KB/일.
for f in */*.html; do case $f in *update_log*) continue;; esac
  n=$(grep -o '\[2026\.[0-9][0-9]\.[0-9][0-9]' "$f" | wc -l | tr -d ' ')
  [ "$n" -gt 20 ] && echo "$n $f"; done | sort -rn
```

**⚠ 셋 다 grep이므로 §C1이 적용된다 — 후보를 좁힐 뿐 판정하지 않는다.**
실제로 2026-08-18에 불가 판정 **grep 10건 중 §G 기준에 해당한 것은 3건**이었고,
나머지는 **세계에 대한 서술·판정 조건이 걸린 것·이미 해소된 것을 서술한 문장**이었다.
**§G가 이미 겪은 실패(23건 → 실제 4건)와 같은 형태이며, 세는 명령이 있어도 읽는 단계는 사라지지 않는다.**

측정 명령:
```
node -e "const t=require('fs').readFileSync('index.html','utf8');eval('var D='+t.match(/var DATA = \[[\s\S]*?\n  \];/)[0].replace(/^var DATA = /,'').replace(/;$/,''));console.log(D.filter(d=>d.desc.length>120).length+'/'+D.length)"
```

## 4. v3 측정 명령 (2026-09-15 신설) — 레짐 신선도 · 캘리브레이션 · 그래프 커버리지 · 내러티브 수명

```
PYTHONIOENCODING=utf-8 python3 - <<'EOF'
# -*- coding: utf-8 -*-
import json,io
from datetime import date
T=json.load(io.open('brain/theses.json',encoding='utf8'))['pages']; R=json.load(io.open('brain/regime.json',encoding='utf8'))
M=json.load(io.open('brain/mechanisms.json',encoding='utf8')); L=[json.loads(l) for l in io.open('brain/routing.jsonl',encoding='utf8') if l.strip()]
td=date.today()
print("레짐 신선도 %d일 (asof %s) %s"%((td-date.fromisoformat(R['asof'])).days,R['asof'],"🟠" if (td-date.fromisoformat(R['asof'])).days>7 else "✓"))
P=[r for r in L if r.get('kind')=='prediction']; due=[r for r in P if r.get('resolve_by') and r['resolve_by']<=td.isoformat()]
sc=[r for r in due if r.get('outcome')]; print("예측 %d건 · 기한 도래 %d · 채점 %d · 미채점 %d"%(len(P),len(due),len(sc),len(due)-len(sc)))
if sc: print("  hit %d · partial %d · miss %d"%(sum(1 for r in sc if r['outcome']=='hit'),sum(1 for r in sc if r['outcome']=='partial'),sum(1 for r in sc if r['outcome']=='miss')))
linked={t for e in M['edges'] for t in e['theses']}
card=[(p,t['id']) for p,pg in T.items() if pg.get('card') for t in pg['theses']]
print("그래프 커버리지 — 카드 테제 %d 중 mechanisms에 걸린 %d"%(len(card),sum(1 for p,i in card if f"{p}#{i}" in linked)))
print("내러티브:",[(n['id'],(td-date.fromisoformat(n['since'])).days,n.get('status')) for n in R['narratives']],"| breaks_if 없음:",sum(1 for n in R['narratives'] if not n.get('breaks_if')))
print("엣지 부호 ?:",[e['id'] for e in M['edges'] if e['sign']=='?'])
EOF
```

```
# mechanisms 걸기 — 값이 바뀐 노드에서 2홉. 라우팅 <후보>다(§C1 grep과 같은 지위 · 판정은 읽어서).
PYTHONIOENCODING=utf-8 python3 - brent <<'EOF'
# -*- coding: utf-8 -*-
import json,io,sys
M=json.load(io.open('brain/mechanisms.json',encoding='utf8')); start=sys.argv[1] if len(sys.argv)>1 else 'brent'
seen={start}; frontier=[start]
for h in (1,2):
    nxt=[]
    for n in frontier:
        for e in M['edges']:
            if e['from']==n:
                print(h,e['id'],e['from'],'→',e['to'],e['sign'],e['grade'],e['theses'] or '(테제 없음)')
                if e['to'] not in seen: seen.add(e['to']); nxt.append(e['to'])
    frontier=nxt
EOF
```

```
# 세션 시작 브리핑(v3) — 레짐 한 줄 · 7일 내 판정 이벤트(+사전약속) · 열린 질문 · 포트 사전약속 · 미라우팅 intake
PYTHONIOENCODING=utf-8 python3 - <<'EOF'
# -*- coding: utf-8 -*-
import json,io
from datetime import date,timedelta
R=json.load(io.open('brain/regime.json',encoding='utf8')); E=json.load(io.open('brain/events.json',encoding='utf8'))['events']
O=json.load(io.open('brain/open.json',encoding='utf8'))['open']; P=json.load(io.open('brain/portfolio.json',encoding='utf8'))
td=date.today(); print("▎레짐(%s · %d일)"%(R['asof'],(td-date.fromisoformat(R['asof'])).days)); print("  ",R['one'])
print("▎7일 내 판정 이벤트")
for e in E:
    w=e['when'][:10].replace('/','-')
    try:
        d=date.fromisoformat(w[:10])
        if td<=d<=td+timedelta(days=7): print("  ",e['when'],"|",e['what'][:90],"| 사전약속:",bool(e.get('precommit')))
    except ValueError: pass
print("▎열린 질문 %d건 · 🔴 %d"%(len(O),sum(1 for o in O if '🔴' in o['what'])))
print("▎포트 사전약속"); [print("   if",x['if'],"→",x['then'][:60]) for x in P['precommits']]
n=0
for f in ('intake/user.jsonl','intake/collected.jsonl'):
    for ln in io.open(f,encoding='utf8'):
        if ln.strip() and json.loads(ln).get('routed') is False and json.loads(ln).get('status','ok')=='ok': n+=1
print("▎미라우팅 intake(routed:false·ok): %d"%n)
EOF
```

```
# 주도주 스크린 — 이벤트 트리거(판정 이벤트 처리 뒤 · 지수 ±3% 일 · 보유/후보 실적 다음 날 · 월 1회 하한). 후보를 좁힐 뿐 판단하지 않는다.
#   --diff 로 직전 파일과 격자 이동을 뽑아 routing 에 남긴다 · --html 로 페이지 재생성
PYTHONIOENCODING=utf-8 python3 portfolio/data/leader_screen.py --top 15 --html --diff intake/files/leader_screen_<직전날짜>.json
```

```
# 스크린 팩터 재검증(분기 1회 · 일봉 캐시 갱신 --fetch) — IC 표가 페이지 방법 섹션에 들어간다
PYTHONIOENCODING=utf-8 python3 portfolio/data/screen_backtest.py --fetch --months 36
```

```
# 수급·VCP 재검증(분기 1회) — Daum investor/days 3년 · KR
PYTHONIOENCODING=utf-8 python3 portfolio/data/screen_backtest_flows.py
```


## ⓐ 누적 · 페이지 낡음 측정 (W1 넷째 조건 · 2026-09-16)
```
python3 - <<'EOF'
import json,re,io,collections
T=json.load(open('brain/theses.json'))['pages']; R=[json.loads(l) for l in open('brain/routing.jsonl',encoding='utf8') if l.strip()]; rd={r['id']:r['date'] for r in R}
def dm(p):
    m=re.search(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})',io.open(p,encoding='utf8').read()); return m.group(1) if m else None
for p,v in T.items():
    d=dm(p); n=sum(1 for t in v.get('theses',[]) for e in t.get('evidence',[]) if d and rd.get(e,'0')>d)
    if n>=5: print(n,d,p)
EOF
```
함께 보는 것: 테제 상태 도전/정정/철회인데 `last_tested` > 페이지 갱신일 · `needs_manual` · 테제 0편 · 훅의 facts 불일치·끊긴 포인터 수.
