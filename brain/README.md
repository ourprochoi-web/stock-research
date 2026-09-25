# brain/ — 제가 생각하고 판단하는 층 (정본)

**세 층의 가운데다** — `intake/`(수집 · 무엇이 왔나) → **`brain/`(판단 · 그래서 어떻게 보나)** → 리서치 페이퍼(설명 · 사용자가 읽는 뷰). 판단·수치·라우팅 기록의 정본은 여기다. 2026-09-13 사용자 결정.

| 파일 | 담는 것 | 언제 고치나 |
|---|---|---|
| `theses.json` | 페이지별 현재 판단 — 한 문장 · 테제(주장·근거·반증·판정 이벤트·상태) · 다음 검증 · 포지션 | **정보가 올 때마다.** 페이지 상단 카드는 여기서 렌더된다(`card:true`) |
| `facts.json` | 확정 지표 — 값·단위·창·기준일·분자·분모·등급·출처·산출 페이지 | 수치를 인용·정정할 때 |
| `routing.jsonl` | 라우팅 기록 — `intake` id · 주장 단위 등급 · 어느 테제에 ⓐⓑⓒ로 착지 · 행동 | **intake 에 적힌 뒤.** 「그때 무엇을 적었나」는 여기, 「무엇이 왔나」는 intake |
| `entities.json` | 회사·테마 카드 — 무슨 사업(등급 표기)·층·정본 페이지·facts 키·걸린 테제 | 회사를 새로 다룰 때 |
| `events.json` | 판정 이벤트 일정 — 도래하면 판정하고 **지운다** | 이벤트를 걸 때·판정할 때 |
| `open.json` | 열린 질문·미착수 | 배치를 열기 전에 읽고, 닫으면 지운다 |
| `regime.json` 🆕v3 | **시장 상태의 정본** — 레짐 한 줄 · 매크로(금리·유가·가스·환·인플레) · 시장 구조(낙폭·breadth·배수) · 수급 · 내러티브(since·깨지는 조건) · 회전 · 「틀렸음을 보여줄 것」 | **바뀔 때만.** 주 1회 「같은 레짐인가」를 `history`에 한 줄. index 「지금 시장」 카드가 여기서 렌더 |
| `mechanisms.json` 🆕v3 | **인과 그래프** — 엣지(from→to · 부호 · 시차 · 강도 · 등급 · 근거 · 걸린 테제). 테제가 아니라 세계의 작동 방식에 대한 등급 있는 가설 | 값이 바뀌면 from 노드에서 2홉을 걸어 라우팅 후보를 찾는다. 반박되면 sign→`?` + routing lesson |
| `portfolio.json` 🆕v3 | **포트폴리오 테제** — 노출(요인별) · 시나리오(두 갈래표) · 헤지 지도 · 사이징 산술(변수=허용 손실%) · 회차 · 사전약속 · 사용자 결정 · 스톱 | 결정·시나리오가 바뀔 때. tracker 「포트폴리오 테제」 카드가 여기서 렌더. §J3 그대로 — 수량·집행은 사용자 |

## v3 (2026-09-15) — 시장·인과·포트폴리오 층. 설계·근거는 `docs/workspace_v3.md`
**브레인은 9 파일이 상한이다.** 다음 구멍은 필드로 푼다. `routing.jsonl`의 `kind`가 늘었다 — `route`(기본) · `verdict` · `decision`(사용자 결정) · **`prediction`**(내 예측: `resolve_by`·`confidence`·나중에 `outcome`·`lesson`) · **`lesson`**. `entities.json`에 `actors`(행위자 카드), `events.json`에 `precommit`(도래 전에 「어느 쪽이면 무엇」)이 붙었다.
**답의 형식(§J2)에 두 줄** — ⓪ 레짐 한 줄(`regime.one`) · ⑥ 포트 영향(`portfolio.exposures`).
**세션 시작 읽기 순서** — `regime.one`+`changes_if` → `events`(7일·precommit) → `open` → `portfolio.precommits` → `intake` `routed:false`.

## 스키마 v2 (2026-09-14 — 첫 실전 하루 뒤 고침)

**theses.json 테제 한 개**
```
{id, claim(≤170), status(유지·도전·정정·철회·관측·방법),
 basis(≤220 · 현재 근거 <요약> · 라우팅 때 덮어쓴다 — 누적하면 페이지 인라인 비대화의 브레인판),
 evidence[ routing id … ]  (append · 「왜」의 로그는 여기서 routing 으로 간다),
 falsifier, event, last_tested,
 auto:true(파서가 뽑은 테제 · basis·event 빌 수 있음) · auto_basis:true(파서가 페이지에서 뽑은 ② 근거)}
```
**routing.jsonl 한 줄** = `{id: r-YYYYMMDD-NN, date, intake[], grade, claim, routed[page#T…], verdict, action}` · 판정 이벤트 결과는 `kind:"verdict"` 로 여기(inbox.jsonl 은 없다). **새 observation/judgment** 는 `priced_in`·`variant`·`breaks_if` 필수 · soft target 은 `parked` (아래 「routing.jsonl 스키마」).
**왜 이렇게 고쳤나** — 시드 직후 실측: 테제 43/407 누락(추출기 12K 캡 + 「반증 조건」 본문 문구 충돌 · 둘 다 수정) · **basis 빈 것 400/428(93%)** — §J1 「브레인 먼저」가 「왜」 질문에 93% 실패하는 상태였다. 파서 v2로 361개를 ②로 채웠고(auto_basis), 라우팅이 닿을 때 ①로 올린다.
**theses.json 은 문서가 아니라 DB다** — 264KB(≈90K 토큰). 통째로 읽지 않고 page 키로 꺼낸다.

## 작업 규칙

1. **정보 유입 = intake 에 한 줄 → 브레인만 고친다.** `routing` 한 줄(intake id 부착) → 걸리는 테제의 `status`·`basis`·`last_tested` → 수치면 `facts`(회사의 `intake` 갱신). 페이지는 열지 않는다.
2. **페이지는 세 경우에만 연다** — 테제 상태가 바뀌었을 때(유지→도전·정정·철회, 신설) · 사용자가 페이퍼를 요청할 때 · 판정 이벤트를 처리한 뒤. 그때 브레인을 읽고 **본문 서술**을 다시 쓴다. 카드는 손대지 않는다(훅이 렌더).
3. **카드 상한** — 테제 1~3개 기본·5개 상한, claim 120자, 근거·반증·판정 각 한 줄. 날짜 블록은 카드에 넣지 않는다 — 경위는 `routing`·`intake`와 페이지 footer 타임라인에.
4. **훅이 하는 것** — `theses.json`이나 카드 페이지가 스테이징되면 카드를 다시 렌더해 함께 커밋 · `facts` 값이 정본 페이지에 있는지 대조(경고) · `routing`·`facts`의 intake 포인터 실재 검사(경고) · `docs/thesis_index.md` 재생성.
5. **죽지 않는 이유** — 카드가 여기서 나온다. 이 파일이 낡으면 페이지 상단이 낡은 것이 바로 보인다.

## 시드 (2026-09-13)
`theses.json` 88편 428테제(09-14 파서 v2 후 · `card:true` 4편 · auto_basis 361) + 광통신 3편 수동 카드 · `facts.json` 광통신 25사 164값 · `events.json` 19건 · `open.json` 20건.
**손대는 페이지부터 카드로 전환한다. 일괄 마이그레이션은 하지 않는다.**


## 테제 스키마 — basis / log 분리 (2026-09-17 구조 개선 A)
- `basis`: 카드에 나오는 **정본 한 문단**. 상태(유지/도전/정정/철회)가 바뀔 때만 고친다.
- `log[]`: `{date, mark(ⓐⓑⓒ·🟢🔴…), text, rid?}` — 라우팅마다 한 줄씩 **뒤에 붙인다**. 페이지를 열 때(W1 넷째 조건: 페이지 갱신일 이후 log 5건) 여기서 본문으로 병합한다.
- `evidence[]`: routing id 목록(기존). log 와 1:1일 필요는 없다.
- 09-17 마이그레이션: basis 꼬리의 날짜 태그 45건을 log 로 옮겼다(40 테제). basis 가 태그로 시작하는 23 테제는 정본 문단이 없어 그대로 뒀다 — 페이지를 열 때 basis 를 다시 쓴다.


## routing.jsonl 스키마 — observation / judgment (2026-09-23)

기존 한 줄 골격은 유지한다:

```
{id, date, intake[], grade, claim, routed[page#T…], verdict, action
 [, kind, source, resolve_by, confidence, outcome, lesson, …]}
```

**새 observation / judgment 줄에는 아래 세 필드를 채운다** (optional in schema · **required for new obs/judgment**):

| field | type | meaning |
|---|---|---|
| `priced_in` | string | 시장 컨센서스가 **이미 가격에 넣은 것** (배수·함의 이익·내러티브) |
| `variant` | string | 우리 쪽 **다른 인과 / 시간축 읽기** (priced_in 과 어디서 갈리는지) |
| `breaks_if` | string | 이 variant/엣지를 **죽이는 관측** (무엇이면 접는지) |

**규칙** — `priced_in` ≈ our view(variant 가 컨센서스와 실질 동일)이면 `action` 은 **`no-edge`** 또는 digest-only(관측만 · 사이즈/테제 변경 없음). 「같은 말을 다시 세게」하지 않는다.

**id 형식**
- 선호: `r-YYYYMMDD-NN` (`NN` = 그날 순번 01, 02, …)
- 레거시(09-22 only): 글자 접미 `x`, `tg` 등 (`r-20260922-x`, `r-20260922-tg6`) — **새 줄에 쓰지 않는다**

**2026-09-26 이후 줄은 `AGENTS.md` §3 이 정본이고 `.githooks/check_routing.py` 가 <차단>한다** — id 형식 · intake 실재 · claim 한국어 · grade ①~④ · `routed[]` 는 실재 `page#T`/페이지만 · obs/judgment 3행 · `digest-only` 는 routing 아님 · **`routed` 한 테제의 `log[].rid` 또는 `evidence` 에 이 줄이 있어야 한다** · ⓑ·prediction 은 `resolve_by`. `events.json` 은 `due`(YYYY-MM-DD|null) 필드가 기계용 날짜다(09-26 · `when` 은 사람용).

**소프트 타깃 (parked)**
- `open` / `regime` / `portfolio` / `events` 처럼 **아직 페이지#T 에 안 붙는 대기**는 `routed[]` 에 문자열로 넣지 않는다.
- 대신 필드: `parked: "open|regime|portfolio|events"` (파이프 구분 · 해당되는 것만).
- `routed[]` 는 실재하는 `page` 또는 `page#T…` 만.
