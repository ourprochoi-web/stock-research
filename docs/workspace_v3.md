# 워크스페이스 v3 — 「인간과 자본의 흐름을 이해하고 조언하는」 구조 (2026-09-15 밤 설계·시범 구축)

**한 줄**: v2(수집→판단→페이지)는 <u>회사·테마 판단</u>을 다루는 데는 작동했지만, **시장 자체**(레짐·수급·내러티브·인과·포트폴리오)에는 자리가 없었다. 그래서 오늘 「시장 방향」 질문에 매번 0에서 다시 쌓았고, 내 리서치의 절반이 대화에만 남았다. v3는 그 자리를 만든다 — 파일 3개, 렌더 2개, 리듬 1개.

## 0. 오늘(09-14) 실측한 실패 — 설계의 근거

| 실패 | 어디서 드러났나 | v3의 답 |
|---|---|---|
| 매크로 값이 갈 곳이 없었다 | 브렌트·HH·TTF·10Y·코스피 낙폭이 대화에만. 「유가 판단 0편」 | `facts.macro`(09-14 신설) + `regime.json` |
| 시장 상태를 매번 0에서 재구성 | 「지금 시장 방향?」에 KOSPI 60일·수급·프리마켓을 그 자리에서 다 받음 | `regime.json` — 상태의 정본 · 「바뀌면 무엇이 바뀌나」 |
| 인과 사슬을 머리로만 돌렸다 | 유가→금리→AI 배수 · HH↔스프레드 · DC 가스 수요→HH↑ 를 손으로 연결 | `mechanisms.json` — 엣지 그래프. 새 값이 오면 그래프를 걸어 걸리는 테제를 찾는다(grep 대신) |
| 헤지·시나리오·사이징이 대화에만 | 두 갈래표 · 허용손실→수량 표 · 뒤집기 조건이 채팅에 | `portfolio.json` — 노출·시나리오·헤지·사이징·사전약속의 정본 → tracker 카드 렌더 |
| 「누가 왜 사고 파는가」가 없다 | 외국인 −3.3조를 크기만 적음. 연준·하이퍼스케일러·사우디·개인 레버리지의 동기가 어디에도 | `entities.actors` — 행위자 카드(원하는 것·제약·다음 행동·근거) |
| 내 판단이 채점되지 않는다 | r-29 「9월 캘린더·유가만 아님」이 맞았는지 아무도 안 잰다 | `routing kind:prediction` + `resolve_by` + `outcome` → 캘리브레이션 명령 |
| 내 리서치 조각이 안 남았다 | `intake/files/` 0개(09-14까지) | 수집 스크립트 v2가 매일 매크로·수급·breadth 스냅샷을 남긴다 |
| 시세 정의가 바뀌었는데 몰랐다 | 네이버 종가 = 20:00 애프터마켓가 | 수집에 **정의 필드**(session) 강제 · 정규 종가 경로 스카우트(별도 보고) |

## 1. 층은 그대로 셋, 브레인이 6→9 파일

```
intake/   무엇이 언제 왔나 (원문 충실 · 판단 금지)         + collect.py v2: 매일 매크로·수급·breadth
brain/    그래서 어떻게 보나 (정본)
   theses.json      회사·테마 판단                (v2 그대로)
   facts.json       확정 수치 · companies + macro  (09-14 macro 신설)
   routing.jsonl    라우팅·판정·결정·<예측>·교훈    (kind 확장)
   entities.json    회사 카드 + <행위자 카드>        (actors 신설)
   events.json      판정 이벤트 + <사전약속>         (precommit 필드)
   open.json        열린 질문                      (그대로)
   regime.json      🆕 시장 상태 — 매크로·시장구조·수급·내러티브·회전 · 「바뀌면」
   mechanisms.json  🆕 인과 그래프 — 엣지(from→to, 부호, 시차, 등급, 근거, 걸린 테제)
   portfolio.json   🆕 포트폴리오 테제 — 노출·시나리오·헤지·사이징·회차·사전약속·사용자 결정·스톱
페이지   왜 그렇게 보는지 (뷰)  + 시장 카드(index) · 포트 카드(tracker) — 브레인에서 렌더
```

**§H1(새 저장소 금지)과의 관계** — 셋은 층 밖의 저장소가 아니라 브레인 안의 정본이다. 기준은 §H1 그대로 「실측 실패율」이며 위 표가 그 실측이다. 그래도 파일 수는 상한을 둔다: **브레인 9 파일 이상 만들지 않는다.** 다음 구멍은 기존 파일의 필드로 푼다.

## 2. 스키마

### 2.1 regime.json — 시장 상태의 정본 (바뀔 때만 쓴다 · 주 1회 「같은가」를 명시적으로 답한다)
```
{asof, one(한 줄 레짐), 
 macro:{rates:{state,us10y,us30y,direction,since,next:FOMC}, oil:{state,brent,premium_est,driver}, gas:{hh,ttf,jkm,spread,state}, fx:{usdkrw,state}, inflation:{cpi,core_mom,bei10}},
 market:{kr:{kospi,peak,drawdown,phase,days_le_3pct,breadth,pe_proxy}, us:{sp500,phase,fwd_pe,vix}},
 flows:{kr_foreign:{window,net,pct_note}, kr_institution, kr_individual, leverage:{...}, us_positioning:{...}},
 narratives:[{id,text,since,evidence[],breaks_if,status}],
 rotation:{asof,leaders,laggards,read},
 changes_if:[…]  ← 이 레짐 판단이 틀렸음을 보여줄 것,
 history:[{asof,one}]}
```
규칙: 값은 `facts.macro`·`prices.json`에서 오고 여기는 <u>해석</u>이다. 내러티브는 3~5개 상한, 시작일과 「깨지는 조건」 없이는 넣지 않는다.

### 2.2 mechanisms.json — 인과 그래프
```
{nodes:{key:{label,kind(macro|flow|sector|company|policy|narrative), fact?:"macro.brent"}},
 edges:[{id:m-NN, from, to, sign(+|−|?), lag(일|주|분기), strength(강|중|약), grade(①~④), evidence[routing id], theses[page#T], note, last_tested}]}
```
용법: 값이 바뀌면 `from` 노드에서 출발해 2홉까지 걸어 `theses`를 모은다 — 라우팅 후보. 관측으로 부호가 반박되면 엣지의 `sign`을 `?`로 내리고 routing에 lesson을 남긴다. **엣지는 테제가 아니다** — 세계의 작동 방식에 대한 가설이며 등급을 갖는다.

### 2.3 portfolio.json — 포트폴리오 테제 (tracker 카드의 원본)
```
{asof, base:{total_assets, cash, equity, holdings_ref},
 exposures:{factor:{share, direction, names[], mechanism[]}},   ← AI캐펙스·금리·유가·가스스프레드·환·중국
 scenarios:{name:{prob_hint?, book, hedge, trigger}},           ← 두 갈래표
 hedge_map:{hedges[], not_hedges[], why},
 sizing:{formula, variable:"allowed_loss_pct", drawdown_at_falsifier:{sym:pct}, table[]},
 tranches:[{n, window(이벤트 경계), names[], condition}],
 precommits:[{if, then, ref}],                                   ← 뉴스가 났을 때 생각하지 않게
 decisions:[{date, what, ref}],                                  ← 사용자 결정(승격)
 stops:[{name, level, kind}],
 next:[…]}
```
§J3은 그대로다 — 이 파일은 산술과 구조이고 수량·비중·집행은 사용자가 정한다. 「허용 손실 %」가 사용자 변수다.

### 2.4 routing.jsonl 확장 — 판단이 채점되게
`kind`: `route`(기본) · `verdict`(판정) · `decision`(사용자 결정) · **`prediction`**(내 예측: `claim`, `resolve_by`, `confidence`, 나중에 `outcome`(hit/miss/partial), `lesson`) · **`lesson`**(사후 검토 — 무엇을 잘못 봤나).
캘리브레이션 = `resolve_by` 지난 prediction 중 outcome 비율. 월 감사 때 센다(backlog 명령).

### 2.5 entities.actors — 행위자
```
actors:{key:{name, type(중앙은행|정부|기업군|투자자군|산유국|무장세력), wants, constraints, next_move, watch(무엇을 보면 아나), evidence[], grade}}
```

### 2.6 events.json — `precommit` 필드
`{when, what, judges, grade, precommit:{if_a:"…", if_b:"…"}}` — 도래 전에 「어느 쪽이면 무엇을 한다」를 적어 둔다. 판정 후 routing verdict에 실제 행동을 적고 지운다.

## 3. 리듬 — 매일 해야 하는 건 여전히 사람은 없다

| 주기 | 누가 | 무엇 |
|---|---|---|
| 매일 16:30·(드리프트) | 봇 | `update_prices.py` + `collect.py v2`: 시세·수급 + 매크로(FRED)·KOSPI 지수·투자자·breadth 스냅샷 → `intake/files/macro/`·`collected.jsonl` |
| 세션 시작 | 나 | `regime.json`(레짐 한 줄·changes_if) → `events`(7일) → `open` → `portfolio.precommits` → `routed:false` |
| 정보 유입 | 나 | intake → **mechanisms 걸기** → routing → theses/regime/portfolio 갱신 · 페이지는 테제 상태 변경 시 |
| 주 1회(월요일) | 나 | 레짐 리뷰 — 「같은 레짐인가」를 한 줄로 답하고 `history`에 남긴다. 내러티브 정리(깨진 것 status:broken) |
| 월 1회 | 감사 에이전트 | 기존 감사 + **캘리브레이션**(prediction 채점) + mechanisms 부호 검산 |

## 4. 답의 형식(§J2)에 두 줄 추가
① 기준일 **⓪ 레짐 한 줄**(regime.one) ② 가격이 전제하는 것 ③ 오늘 정보의 방향 ④ 대가 ⑤ 등급 **⑥ 포트 영향**(portfolio.exposures에서 — 어느 노출이 얼마나). 나머지는 v2와 같다.

## 5. 렌더·훅
- `render_cards.py`에 `--market`(regime→index.html `<!-- brain:market:start/end -->`) · `--portfolio`(portfolio→tracker `<!-- brain:portfolio:start/end -->`) 추가. 훅은 `regime.json`·`portfolio.json`이 스테이징되면 렌더한다.
- 훅 검사 추가: 세 파일 JSON 유효성 · `mechanisms.edges[].theses` 실재 · `portfolio.decisions[].ref`·`prediction.resolve_by` 형식.

## 6. 측정 명령(backlog.md에 추가)
- 캘리브레이션: `resolve_by ≤ 오늘` 인 prediction 중 `outcome` 없는 수 / hit·miss·partial 비율
- 레짐 신선도: `regime.asof`가 7일 초과면 🟠
- 그래프 커버리지: 카드 페이지(card:true) 테제 중 mechanisms에 안 걸린 수
- 내러티브 수명: `since`부터 일수 · `breaks_if` 없는 항목 수(0이어야)

## 7. 이행 — 일괄 아니고 시범
- 09-15 밤: 세 파일을 **오늘 실제 내용으로 시드**(레짐 09-14 · 엣지 18개 · 포트 시나리오·사이징) · 행위자 11 · prediction 4건 등록 · 렌더 2개 · 훅 검사 · collect v2 · backlog 명령.
- 다음 정보부터 mechanisms 걸기를 실제로 한다. 2주 실측 뒤(09-29) 「그래프 걸기가 grep보다 라우팅을 더 잘 찾았나」를 routing으로 센다 — 못 찾았으면 mechanisms는 폐기한다(§H1 실측 기준).
- CLAUDE.md는 표 3행 + §J2 두 줄 + §H1 「브레인 9 파일 상한」만 고친다. 규칙 본문은 v2 그대로.

## 8. 하지 않는 것
- 예측 모델·백테스트·자동 매매 신호. 이 워크스페이스의 산출물은 판단이지 신호가 아니다.
- 내러티브를 감정으로 적는 것 — 내러티브는 「시작일 + 근거 + 깨지는 조건」이 있는 명제다.
- 파일을 더 만드는 것 — 다음 구멍은 필드로.

## 9. 밤새 실제로 한 것 (09-15 00:30~02:30) — 설계와 실측이 갈린 자리

| 계획 | 실제 | 갈린 것 |
|---|---|---|
| 세 파일 시드 | regime(내러티브 5·changes_if 4) · mechanisms(엣지 27) · portfolio(시나리오 5·사전약속 5·사이징 7종목) | — |
| 행위자·예측·교훈 | actors 11 · prediction 6 · lesson 6 | 교훈이 예측과 같은 수 — 오늘 하루 틀린 것이 그만큼 |
| 렌더 2 | index 「지금 시장」 · tracker 「포트폴리오 테제」 — 브라우저로 확인 | 🔴 스키마를 바꾸자(premium_est 삭제) 렌더가 죽었다 → `.get`으로 전면 교체. **렌더는 스키마에 종속되면 안 된다**(교훈 r-20260915-02 옆) |
| 수집 v2 | files/macro/2026-09-14.json 첫 스냅샷(FRED 9·네이버 지수·투자자·session 필드) | breadth는 봇 워크플로에서만 값이 나온다(수동 재실행 시 prices.json 이 이미 커밋돼 있어 0) — 다음 봇 실행이 첫 실측 |
| 그래프 걸기 테스트 | 손 라우팅 8 중 4 적중 · 3 추가 발견 · 2 데이터 오류 · 2 노드 부재 | 🔴 유가·수급 경로에 걸린 테제 0 — **아카이브에 이란 전쟁(2026-03~) 편이 0편**이다. 6개월째 최대 매크로 변수가 페이지 없이 update_log·tracker 블록에만 흩어져 있었다 → open `war-coverage` |
| 유가 판단 채우기 | 세계은행·IEA 계열 값(②)으로 「프리미엄 $15~20」을 「전쟁 공급 손실 · 휴전 시 −20~35%」로 정정 | 내가 어제 낸 헤지 낙폭(FANG −25%)이 과소였다 → −35%. **매크로 충격은 가격 차이가 아니라 물리량 차이로 먼저 잰다**(regime.macro.*.physical) |
| 데이터 스카우트(에이전트) | KRX 정규 종가 · KOSPI 투자자 이력 · TTF/JKM · breadth 소스 탐색 | 결과는 `intake/README` 갱신과 collect v2 확장으로 반영(별도 커밋) |

**판정 유지**: 09-29에 「그래프 걸기가 grep보다 라우팅을 더 잘 찾았나」 · 첫 예측 채점은 10-14(n-rotation) · 10-31(메모리 ASP).

