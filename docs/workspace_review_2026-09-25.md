# 구조 진단 · 개선 제안 (2026-09-25 · 실측 기준)

**한 줄**: 수집은 자동화가 끝났고 **판단은 손으로 남아 있다.** 09-23 텔레그램 봇이 붙은 뒤 사흘간 수집 501건 / 라우팅 43줄이고, 그 43줄 중 **테제를 실제로 건드린 것은 0건**이다(테제 `last_tested` 최신값이 09-22에 멈춰 있다). v3가 만든 자리(regime·mechanisms·portfolio)는 살아 있지만, 그 자리에 **판단을 넣는 처리량**이 병목이다. 아래는 재측정 명령을 붙인 실측과, 그 실측이 가리키는 제안 다섯이다.

**이 문서의 지위** — `workspace_v3.md`와 같다. 규칙이 아니라 **진단과 제안**이고, 채택된 것만 `CLAUDE.md`·`brain/README.md`로 올라간다. §H1(브레인 9파일 상한 · 새 저장소 금지)과 §J3(집행 지시 금지)은 제안 전부가 지킨다.

---

## 0. 측정 (2026-09-25 · 명령은 §6)

| 층 | 값 | 판정 |
|---|---|---|
| intake | 총 884건(collected 652 · user 232) · `routed:false` **461건**(450이 텔레그램) | 🔴 큐 폭발 |
| intake → routing | 라우팅이 참조한 intake id **336/884 = 38.0%** · 끊긴 포인터 0 | 🟠 |
| routing | 273줄 · 09월 전부 · kind 16종 | — |
| routing → theses | `routed[]` 대상 643개 중 **실재 테제로 해석되는 것 150개(23%)** · 소프트 타깃 248(=`parked` 로 가야 할 것) · 자유문자열·오타 **245개** | 🔴 링크 붕괴 |
| theses | 92페이지 475테제 · `유지` **443(93.3%)** · 도전 6 · 정정 10 · 철회 **1** | 🔴 반증이 안 일어난다 |
| theses 신선도 | `last_tested` 370/475가 **09-17 일괄 마이그레이션 날짜**에 고정 · 09-23 이후 갱신 **0** | 🔴 |
| 카드 | `card:true` **14/92 페이지** · 아카이브 HTML 168편 중 theses 등재 92편 | 🟠 J1이 대부분 페이지에서 미작동 |
| 페이지 부채 | W1 넷째 조건(갱신일 이후 log 5건) 충족 **30편** · 상태가 도전/정정/철회로 바뀌었는데 페이지 미수정 **9테제**(최장 `ai_chip_company_marvell` T1 철회 — 페이지 갱신일 08-28) | 🔴 |
| prediction | 6건 / 273줄(2.2%) · `resolve_by` 도래 0 · 채점 0 | 🟠 채점 루프가 아직 한 번도 안 돌았다 |
| mechanisms | 엣지 43 · `theses` 붙은 엣지 22/43 · **`last_tested` 전부 null** · 카드 테제 70 중 그래프에 걸린 것 **7(10%)** | 🔴 09-29 폐기 판정의 근거를 지금 못 만든다 |
| events | 113건 · **기한 지났는데 안 지워진 것 9건** · `precommit` 13/113 | 🟠 |
| open | open 17 · **parked 79**(4.6배) · `contra_claim` **0건** (09-23 프로토콜 §3은 최대 노출마다 1건을 요구) | 🔴 |
| facts | 693값 · 등급 ① 626(90%) · **기준일 2026-06 이 251값(36%)** | 🟠 3Q 시즌 전 점검 필요 |
| regime / portfolio | asof 09-22 / 09-23 · 내러티브 6(breaks_if 누락 0) · 노출 7 · 사전약속 8 · 스톱 9 | ✅ 여기는 살아 있다 |

### 수집과 판단의 처리량 (일자별 · 수집 / 라우팅)

```
09-19     9 /  9      09-22    56 / 32
09-20   112 / 35      09-23   268 /  8   ← 텔레그램 봇 투입
09-21    12 /  3      09-24   133 / 23
                      09-25   100 / 12
```

**09-22까지 수집:라우팅은 약 1.5:1이었고, 09-23부터 15~30:1이다.** 큐는 사흘 만에 454건이 됐고 매일 100건 이상 늘어난다. 이 속도에서 §R3의 「세션 시작에 `routed:false`를 읽는다」는 **지킬 수 없는 규칙**이다 — 규칙이 아니라 구조를 고쳐야 한다.

---

## 1. 잘 작동하는 것 (먼저 적는다 — 고치지 말 것)

- **세 층 분리**(intake / brain / 페이지)는 옳다. 끊긴 intake 포인터가 **0건**이라는 것이 증거다 — 「대화에만 있는 값은 없는 값이다」가 실제로 지켜지고 있다.
- **v3의 세 파일**(regime·mechanisms·portfolio)은 죽지 않았다. regime 신선도 3일, 내러티브 전부 `breaks_if` 보유, portfolio에 노출·시나리오·스톱·사전약속이 실제 값으로 들어 있다.
- **09-23 엣지 3종 세트**(`priced_in`/`variant`/`breaks_if`)는 **신규 줄 기준 100% 준수**다(09-23 이후 obs/judgment 42줄 중 누락 0 · 그 이전 누적은 72줄 누락). 새 규칙이 실제로 정착한 드문 사례다.
- **자동 수집**(시세·XBRL·PTR·SEC·텔레그램·매크로)은 사람 손이 안 들어간다.
- **`docs/name_index.json`**(318개 이름 → 테제·facts 역색인, 192개가 테제와 연결)이 이미 있다. 아래 제안 A의 재료가 이미 만들어져 있다.

---

## 2. 구멍 — 무엇이 어디서 새는가

### ① 수집 ≫ 판단 (가장 큰 것)
`collected.jsonl`의 텔레그램 447건은 **파일 용량의 53%**이고 전부 `routed:false`다(user.jsonl 3건을 더해 큐 기준 450건). 채널별로는 insidertracking 191 · YeouidoStory2 83 · aetherjapanresearch 71 · Samsung_Global_AI_SW 39 · pikachu_aje 29 · milperc 21 · meritz_research 13. 이 중 **URL만 있는 줄 43건 · 60자 미만 91건** — 134건(30%)은 애초에 주장이 아니다.

### ② routing → theses 링크가 사실상 끊겼다
`routed[]`에 들어온 값의 실제 분포:
```
실재 테제(page#Tn)   150 (23%)
소프트 타깃          248 (39%)  open:…, events:FOMC, brain/regime.json:rates …
자유문자열·오타      245 (38%)  "관측", "memory_cycle", "#T5", "samsung", "" …
```
09-23에 `parked` 필드를 도입했지만 **39줄만 쓴다.** 훅의 포인터 검사는 전부 **「경고만」**이라 10일 만에 77%가 깨졌다. 브레인이 「DB다」(brain/README)라고 선언한 것과 실제 상태가 다르다 — **지금은 grep 가능한 로그이지 조회 가능한 DB가 아니다.**

### ③ 테제가 거의 반증되지 않는다
475테제 중 `철회`는 **1건**, `도전`은 6건이다. falsifier는 100% 채워져 있는데 **다시 재는 일이 없다.** `last_tested`의 78%가 09-17 마이그레이션 날짜다. 이 상태의 위험은 명확하다 — 확증만 쌓이는 아카이브는 시간이 갈수록 **틀린 확신을 더 크게 만든다.** 판정 이벤트를 「틀렸을 때 빨리 아는 장치」로 정의(§J2)해 놓고, 장치가 돌지 않고 있다.

### ④ 뷰(페이지)가 판단보다 낡았다
상태가 `철회`/`정정`으로 바뀌었는데 페이지가 그대로인 테제 9건. W1 넷째 조건을 넘긴 페이지 30편. 카드는 14편뿐이라 **나머지 78편은 상단이 낡아도 보이지 않는다** — brain/README가 적은 「브레인이 죽지 않는 이유(카드가 여기서 나온다)」가 15%에서만 작동한다.

### ⑤ 조언이 채점되지 않는다
prediction 6건, 기한 도래 0, 채점 0. mechanisms는 `last_tested`가 전부 null이라 **09-29로 예정된 「그래프가 grep보다 나았나」 판정을 지금 데이터로는 할 수 없다.** 라우팅 줄에 「무엇으로 찾았나」가 안 적혀 있기 때문이다.

### ⑥ 반대 주장이 없다
`contra_claim` 0건. 노출 7개(ai_capex_beta · rates_up · oil_up · gas_spread · krw_weak · china_memory_selfsufficiency · non_ai_kr) 전부 반대편이 비어 있다. 93% 유지와 같은 뿌리다.

---

## 3. 제안 — 다섯 (우선순위 순 · 각각 폐기 판정 조건을 붙인다)

### A. 수집에 분류기를 붙인다 — 큐를 사람이 볼 크기로 자른다 🔴 최우선
**무엇** — `collect.py`가 뉴스레터에만 적용하는 **후보 테제 태깅**(`name_index.json` 매칭 → `rec["candidates"]`)을 텔레그램·PTR·SEC·fetch 전부에 적용하고, 결과로 `routed` 값을 셋으로 가른다.

| 값 | 무엇 | 누가 본다 |
|---|---|---|
| `false` | 후보 테제가 붙었거나 보유 종목·최대 노출을 건드리는 것 | **사람(세션 시작)** |
| `"archive"` | 후보 없음 · 본문 60자 미만 · URL 전용 | 안 본다(grep 대상으로만 남는다) |
| `"data"` | 기존과 같음(XBRL·매크로 스냅샷) | facts/regime이 직접 읽는다 |

**왜** — 447건에 이 매칭을 돌려 보면 **후보가 붙는 것은 112건(25%)**, 나머지 335건은 어느 테제에도 안 걸린다. 큐가 454 → **약 112**로 줄고, 남은 112건은 **「어느 테제를 재라」가 이미 적힌 채로** 온다. intake 규칙 4(버리지 않는다)는 그대로다 — 줄도 `files/` 스냅샷도 남고, 큐에서만 빠진다.

**어디** — `intake/collect.py`의 후보 태깅 블록을 함수로 빼서 `collect_telegram.py`·`collect_fetch.py`·`collect_sec.py`·`collect_congress.py`가 부른다. 새 파일·새 저장소 없음(§H1 통과).

**곁들여** — 큐에 수명을 준다. `routed:false`가 **7일** 지나면 `routed:"lapsed"` + 사유 한 줄. 지금은 무한 누적이라 규칙이 먼저 무너진다.

**판정** — 도입 7일 뒤 `routed:false` 큐가 **50건 이하**로 유지되지 않으면 채널 화이트리스트를 줄인다(insidertracking 191건이 최대 발신원이다). 10월 말까지 큐가 다시 300을 넘으면 텔레그램 수집 자체를 폐기한다.

---

### B. 훅의 경고 셋을 차단으로 올린다 — 브레인을 조회 가능한 DB로 되돌린다 🔴
**무엇** — `.githooks/pre-commit`의 「경고만」 항목 중 셋을 **커밋 차단**으로 승격한다.
1. `routed[]`의 대상이 `theses.json`에 실재하는 `page` 또는 `page#Tn` 인가
2. 소프트 타깃(`open:`·`events`·`regime`·`portfolio`·`brain/*`)이 `routed[]`가 아니라 `parked`에 있는가
3. `routing`·`facts`의 intake id가 실재하는가 (지금 0건 위반 — 차단으로 올려도 비용 0)

**왜** — §H1이 정한 예외 기준은 편의가 아니라 **실측 실패율**이다. 경고로 둔 채 10일 만에 **77%(493/643)**가 깨졌다. 반대로 차단이 걸려 있는 항목(카드 렌더·dateModified)은 깨진 게 없다. 기준을 이미 충족한다.

**어디** — 기존 `routed[]` 643개의 소급 정리 1회(자유문자열 245건을 `parked` 또는 실재 테제로 판정 · 소프트 타깃 248건을 `parked`로 이동 — 라우팅 로그를 읽어야 하므로 grep으로 끝나지 않는다) → 그 다음 커밋부터 차단.

**판정** — 차단 도입 후 **우회 커밋(`--no-verify`)이 2주에 3회를 넘으면** 규칙이 아니라 스키마가 틀린 것이므로 `routed[]` 형식을 다시 설계한다.

---

### C. 라우팅이 테제를 건드리게 만든다 — 「유지 93%」의 정면
**무엇** 셋:
1. **착지 강제** — `kind`가 `route`/`judgment`인 줄은 `routed[]`(실재 테제) 또는 `parked` 중 하나가 반드시 있어야 한다. 그리고 `routed[]`가 있으면 **같은 커밋에서** 그 테제의 `last_tested`·`log[]`가 갱신됐는지 훅이 검사한다(경고 → 2주 뒤 차단). 지금 09-23 이후 라우팅 43줄이 테제를 하나도 못 건드린 것이 이 검사로 바로 드러난다.
2. **테제 나이를 카드에 노출** — `last_tested`가 30일을 넘으면 렌더된 카드에 🟠. 브레인이 죽지 않는 이유가 「카드가 여기서 나온다」라면, **낡음도 카드에서 보여야 한다.**
3. **분기 1회 반증 스윕** — 카드 테제(70개)의 `falsifier`를 `facts`·`regime` 현재값과 기계적으로 대조해 **후보만** 뽑는다(§C1 지위 — 판정은 읽어서). 지금은 반증을 「정보가 올 때」만 재는데, 그러면 **조용히 틀리는 테제**는 영원히 안 걸린다.

**왜** — 철회 1/475는 아카이브가 틀린 적이 거의 없다는 뜻이 아니라 **틀렸는지 재지 않는다**는 뜻이다. 09-15 실측에서 「교훈이 예측과 같은 수(6/6)」였던 것과 대비하면, 하루치 손 라우팅에서는 절반이 틀렸는데 누적 테제에서는 0.2%만 철회됐다.

**판정** — 도입 4주 뒤 `도전+정정+철회` 비중이 **475테제의 10%(≈48건)**에 못 미치면, 스윕이 후보를 못 뽑는 것이므로 falsifier 문장 형식을 「기계 대조 가능한 값+임계」로 다시 쓴다.

---

### D. 조언을 채점한다 — prediction을 판단의 필수 출력으로
**무엇**:
1. `kind:"judgment"` 줄에는 **`resolve_by`를 가진 prediction을 하나** 달거나, 못 달면 `no_prediction` 사유 한 줄을 남긴다. 지금 6/273(2.2%)이다.
2. 라우팅 줄에 **`found_by`**(`graph`|`grep`|`user`|`bot`) 한 필드를 붙인다 — **09-29 mechanisms 판정의 유일한 근거**다. 지금 붙이지 않으면 09-29에 「모르겠다」로 폐기하거나 근거 없이 존치하게 된다(엣지 43개 중 `last_tested` 0건 · 카드 테제 그래프 커버리지 10%).
3. 노출 7개마다 `open.json`에 **`contra_claim` 1건**(09-23 프로토콜 §3 이행 · 현재 0/7).

**왜** — 사용자와의 계약(§J)은 「불확실할 때 방향을 말하라, 대신 등급과 잃는 크기를 붙여라」다. 방향을 말하는 시스템은 **채점 없이는 개선되지 않는다.** v3가 채점 자리를 만들었는데 10일간 6건만 들어왔다.

**판정** — 10월 말 기준 채점된 prediction이 **10건 미만**이면 「judgment마다 예측」 규칙을 폐기하고, 대신 **판정 이벤트(events)의 `precommit` 결과만** 채점한다(현재 13/113 → 이쪽을 키운다).

---

### E. 뷰 부채를 보유 종목 기준으로 갚는다
**무엇** — 전면 마이그레이션 금지(W1)는 유지하되, **카드 전환 순서를 정한다**: ① 보유 9종목이 걸린 페이지 → ② `portfolio.exposures` 상위 3개 노출에 걸린 페이지 → ③ W1 넷째 조건 충족 30편 중 나머지. 상태가 바뀌었는데 안 고쳐진 9테제는 **부채 목록으로 `open.json`에 올린다**(지금은 어디에도 없다).

**왜** — 카드 14/92는 §J1(브레인 먼저)이 85% 페이지에서 작동하지 않는다는 뜻이고, 그 페이지들이 바로 검색으로 되돌아가는 자리다. 168편 중 92편만 theses에 등재된 것도 같은 부채다(나머지 76편은 판단이 아예 없다 — 대부분 board/market/node-screener 등 도구 페이지지만 확인이 필요하다).

**판정** — 4주 뒤 카드 페이지가 **25편**에 못 미치면, 카드 렌더 대상을 페이지가 아니라 **종목**으로 바꾼다(entities.json 기준 회사 카드 렌더).

---

## 4. 제안하지 않는 것 (그리고 그 이유)

- **새 파일·새 저장소** — 제안 A~E 전부 기존 `intake/collect*.py` · `.githooks/` · 브레인 9파일 안에서 끝난다. §H1 상한을 건드리지 않는다.
- **LLM 자동 라우팅**(수집 → 테제 판정 자동화) — 판단을 자동화하면 이 아카이브의 산출물(판단)의 등급 체계가 무너진다. A는 **분류(후보 붙이기)까지만** 하고 판정은 사람이 한다. §R1의 「주장 단위 등급」은 자동화 대상이 아니다.
- **예측 모델·매매 신호** — workspace_v3 §8 그대로.
- **규칙 문서 통합** — 규칙이 6곳(CLAUDE.md · brain/README · intake/README · judgment_protocols · workspace_v3 · rules_journal)에 흩어져 있는 것은 사실이고 세션 시작 비용을 올리지만, **지금 손대면 위 다섯이 밀린다.** 다만 `judgment_protocols_2026-09-23.md`는 **새 규칙을 만들고 있어**(3종 세트 필수화·contra book) 성격상 CLAUDE.md §R·§J로 올라가야 한다 — 다음 규칙 개정 때.

---

## 5. 순서

1. **A**(분류기 + 큐 수명) — 큐가 안 줄면 나머지가 전부 안 돌아간다.
2. **B**(훅 차단) — A로 들어온 것이 다시 안 새게.
3. **C**(테제 착지 + 나이 + 스윕) — 여기서부터 판단이 실제로 바뀐다.
4. **D**(채점 · `found_by`) — **09-29 mechanisms 판정 전에** `found_by`만 먼저.
5. **E**(뷰 부채) — 상시.

---

## 6. 재측정 명령 (채택되면 `docs/backlog.md` §4로 옮긴다)

```bash
# 이 문서의 표를 통째로 다시 잰다
PYTHONIOENCODING=utf-8 python3 - <<'EOF'
# -*- coding: utf-8 -*-
import json,io,re,glob,collections
from datetime import date
ROUT=[json.loads(l) for l in io.open('brain/routing.jsonl',encoding='utf8') if l.strip()]
T=json.load(io.open('brain/theses.json',encoding='utf8'))['pages']
COL=[json.loads(l) for l in io.open('intake/collected.jsonl',encoding='utf8') if l.strip()]
USR=[json.loads(l) for l in io.open('intake/user.jsonl',encoding='utf8') if l.strip()]
td=date.today()

# ① 큐
q=[r for r in COL+USR if r.get('routed') is False]
print("intake 큐(routed:false) %d | 그중 telegram %d"%(len(q),sum(1 for r in q if r.get('kind')=='telegram')))

# ② routed[] 무결성
pages=set(T); ok=soft=bogus=0
for r in ROUT:
    for t in r.get('routed',[]) or []:
        p=str(t).split('#')[0]
        if p in pages: ok+=1
        elif p.startswith(('open','events','regime','portfolio','brain/','docs/')) or ':' in p: soft+=1
        else: bogus+=1
print("routed[] 실재 %d · 소프트(→parked) %d · 깨짐 %d | parked 쓰는 줄 %d"%(ok,soft,bogus,sum(1 for r in ROUT if r.get('parked'))))

# ③ 테제 상태·신선도
th=[t for v in T.values() for t in v.get('theses',[])]
st=collections.Counter(t.get('status') for t in th)
lt=collections.Counter(str(t.get('last_tested'))[:10] for t in th)
print("테제 %d | 유지 %.1f%% | 도전·정정·철회 %d | last_tested 최신 %s"%(
    len(th),100*st.get('유지',0)/len(th),
    sum(v for k,v in st.items() if str(k).startswith(('도전','정정','철회'))), max(lt)))

# ④ 카드·페이지 부채
print("카드 페이지 %d/%d | 아카이브 HTML %d"%(sum(1 for v in T.values() if v.get('card')),len(T),
    len([f for f in glob.glob('*/*.html') if 'update_log' not in f])))

# ⑤ 채점·그래프
P=[r for r in ROUT if r.get('kind')=='prediction']
print("prediction %d | 기한도래 %d | 채점 %d | found_by 붙은 줄 %d"%(
    len(P),sum(1 for r in P if r.get('resolve_by') and r['resolve_by']<=td.isoformat()),
    sum(1 for r in P if r.get('outcome') or r.get('judged_by')), sum(1 for r in ROUT if r.get('found_by'))))

# ⑥ 반대 주장
O=json.load(io.open('brain/open.json',encoding='utf8'))['open']
PF=json.load(io.open('brain/portfolio.json',encoding='utf8'))
print("contra_claim %d / 노출 %d"%(sum(1 for o in O if 'contra_claim' in json.dumps(o,ensure_ascii=False)),len(PF['exposures'])))
EOF
```

```bash
# A 도입 전후 비교 — name_index 후보가 붙는 intake 비율
PYTHONIOENCODING=utf-8 python3 - <<'EOF'
# -*- coding: utf-8 -*-
import json,io
N=json.load(io.open('docs/name_index.json',encoding='utf8'))['names']
K=[(n,[n]+v.get('aliases',[])) for n,v in N.items() if v.get('auto_candidate') and v.get('theses')]
R=[json.loads(l) for l in io.open('intake/collected.jsonl',encoding='utf8') if l.strip()]
R=[r for r in R if r.get('routed') is False]
hit=sum(1 for r in R if any(k in (r.get('text') or '') for _,ks in K for k in ks))
print("큐 %d | 후보 붙는 것 %d (%.0f%%) → 사람이 볼 큐"%(len(R),hit,100*hit/max(len(R),1)))
EOF
```

```bash
# 페이지 부채 — 상태가 바뀌었는데 페이지가 안 고쳐진 테제
PYTHONIOENCODING=utf-8 python3 - <<'EOF'
# -*- coding: utf-8 -*-
import json,io,re
T=json.load(io.open('brain/theses.json',encoding='utf8'))['pages']
def dm(p):
    try: s=io.open(p,encoding='utf8',errors='ignore').read()
    except OSError: return None
    m=re.search(r'"dateModified"\s*:\s*"(\d{4}-\d{2}-\d{2})',s); return m.group(1) if m else None
for p,v in T.items():
    d=dm(p)
    for t in v.get('theses',[]):
        if d and str(t.get('status','')).startswith(('도전','정정','철회')) and str(t.get('last_tested',''))[:10]>d:
            print(t['status'],t['id'],'| 판단',t.get('last_tested'),'> 페이지',d,'|',p)
EOF
```
