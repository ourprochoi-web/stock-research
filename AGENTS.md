# AGENTS.md — Lead 에이전트 작업 계약 (v1 · 2026-09-26)

**누구를 위한 파일인가** — 이 저장소에 **git으로 쓰는 모든 LLM 에이전트**(Grok Bot Lead · Claude 세션 · 그 외). 모델을 가리지 않는다.
사람용 규칙 전문은 `CLAUDE.md`(§J·§R·§W·§E·§H)이고, 이 파일은 그중 **에이전트가 매 실행에 지켜야 하는 것만** 기계가 검사할 수 있는 형태로 적은 것이다. 둘이 어긋나면 `CLAUDE.md`가 정본이고 이 파일을 고친다.
**어긴 커밋은 CI(`brain-check.yml`)와 로컬 훅(`check_routing.py`)이 거절한다.** 쓰여 있는 규칙이 아니라 검사되는 규칙이 이 파일의 전부다.

---

## 0. 역할 한 줄

Lead는 **해석자**다 — 들어온 주장을 테제에 착지시키고(ⓐ 확인 · ⓑ 도전 · ⓒ 신규), 테제의 `last_tested`·`log`·`status`를 움직인다.
요약해서 파일에 넣는 것은 해석이 아니라 보관이다. 보관은 수집기가 이미 한다. **테제를 건드리지 않은 routing 줄은 해석이 아니며 거절된다.**

## 1. 실행 루프 (매 실행 · 이 순서 · 건너뛰면 그렇다고 적는다)

```
0. git pull --rebase origin main
1. python3 portfolio/data/watch.py            ← 지난 이벤트 · 스톱 거리 · 반증 후보 · 레짐 신선도 · 큐 크기
2. 큐 읽기: intake/*.jsonl 중 routed:false 이고 status:ok — candidates 가 붙은 것부터
3. 항목마다:
   a. grep intake·routing 으로 재등장 대조 (같은 URL·같은 제목·같은 수치)
   b. 걸리는 테제 찾기 — candidates → docs/name_index.json → brain/theses.json 의 page 키
      (통째로 읽지 않는다 · python3 portfolio/data/packet.py <이름> 으로 꺼낸다)
   c. 주장 단위로 쪼개 각각 등급(①공시 ②미확인 ③전문가 ④수사) — 통째 인용 금지
   d. routing.jsonl 한 줄 (§3 스키마) + theses.json 갱신 (§4 권한) + 수치면 facts.json
   e. intake 줄의 routed 를 true 로, routing 필드에 r-id
4. python3 .githooks/check_routing.py         ← 0 이 아니면 커밋하지 않는다. 고친다
5. git add -A brain intake && git commit && git push (실패 시 pull --rebase 후 재시도 5회)
```

배치처가 없는 항목은 **`routed:"skip:no-thesis"`**로 닫고 routing 줄을 만들지 않는다(intake 규칙 4 — 줄과 원문은 남는다).
한 실행에서 처리할 수 있는 양보다 큐가 크면 **보유 종목 · card:true 페이지 · events.json 7일 내 이벤트에 걸리는 것부터** 하고, 남은 수를 커밋 메시지에 적는다.

## 2. 쓰기 권한 표

| 파일 | Lead가 할 수 있는 것 | Lead가 하지 않는 것 |
|---|---|---|
| `intake/*.jsonl` | 줄 append · `routed` 값 변경 · `routing` r-id 부착 · `summary` 필드 추가 | 기존 `text`·`subject` 수정 · 줄 삭제 |
| `brain/routing.jsonl` | 줄 append (§3) | 기존 줄 수정 (정정은 새 줄 `kind:correction` + `corrects: r-id`) |
| `brain/theses.json` | `log[]` append · `last_tested` · `evidence[]` append · `status` 유지→도전/관측 · `basis` (도전 시) | `status` → 정정·철회 (사람 확정) · `card` 토글 · 테제 삭제 · `claim` 수정 |
| `brain/facts.json` | metrics 추가·갱신 (`value·unit·num·den·asof·grade·source·intake` 전부) | 분자·분모 없는 값 |
| `brain/events.json` | 이벤트 추가 (`due` 필수) · 도래한 이벤트 판정 후 삭제 + routing `kind:verdict` | `precommit` 내용 변경 (사람) |
| `brain/open.json` | 항목 추가·`updates[]` append · 해소 시 삭제 | — |
| `brain/regime.json` | `history[]` append · `narratives[].status` · 수치 필드 | `one` 변경 (사람과 합의 후) |
| `brain/mechanisms.json` | `edges[].last_tested` · `evidence[]` append · `sign` → `?` (반박 시) | 엣지 추가 (09-29 판정 전까지) |
| `brain/portfolio.json` | `exposures`·`scenarios` 서술 · `_changelog` | **`holdings`·`cash`·`stops`·`decisions`·`precommits`** — 전부 사용자 |
| `brain/entities.json` | 회사·행위자 카드 추가·갱신 | — |
| HTML 페이지 | 열지 않는다 | 본문 수정 (테제 상태가 바뀐 페이지는 open.json 에 `page-debt:` 로 남긴다) |

## 3. routing.jsonl 한 줄 — 필수 필드 (2026-09-26 이후 줄에 강제)

```
{id:"r-YYYYMMDD-NN", date:"YYYY-MM-DD", kind, intake:[…], grade, claim, routed:[…] | parked,
 verdict, action, priced_in, variant, breaks_if [, resolve_by, confidence, source, corrects, found_by]}
```

| 필드 | 규칙 |
|---|---|
| `id` | `r-YYYYMMDD-NN` (NN 두 자리 순번). 파일을 읽고 다음 번호를 쓴다. 글자 접미(`x`·`tg`) 금지 |
| `kind` | `route` · `observation` · `judgment` · `verdict` · `prediction` · `decision` · `lesson` · `correction` · `measurement` 중 하나 |
| `intake[]` | `route`·`observation`·`judgment` 는 1개 이상 · 전부 intake 파일에 실재 |
| `claim` | **한국어 포함**(재등장 대조가 grep 이라 언어가 갈리면 못 찾는다). 영어 원문은 intake `text` 에 |
| `grade` | ①~④ 중 하나 이상 포함 |
| `routed[]` | 원소는 **실재하는 `page.html#Tn`** 또는 실재 페이지 경로만. intake 파일 경로·`"관측"`·`"#T5"` 같은 문자열 금지 |
| `parked` | `routed[]` 가 비면 필수 — `"open"`·`"regime"`·`"portfolio"`·`"events"` (파이프 구분) |
| `priced_in`·`variant`·`breaks_if` | `observation`·`judgment` 는 셋 다 비면 안 된다 |
| `action` | `priced_in ≈ variant` 면 `no-edge`. **`digest-only` 는 routing 줄이 아니다** — intake 줄에 `summary` 를 붙이고 `routed:"skip:digest"` 로 닫는다 |
| **테제 접촉** | `routed[]` 에 `page#T` 가 있으면 그 테제의 `log[]` 에 `rid == id` 인 항목이 있거나 `last_tested >= date` 여야 한다. **이게 없으면 해석이 아니다** |
| `resolve_by` | `prediction` 필수 · `judgment` 중 `verdict` 가 ⓑ 면 필수 (「언제 틀렸는지 아나」) |
| `kind:verdict` | `event` 필드(판정한 events.json 항목 what 앞 40자) + 그 이벤트는 events.json 에서 삭제 |

알 수 없는 최상위 필드(`disposition`·`keep`·`investment_keep` 등)는 경고 → 다음 버전에서 거절. 쓰고 싶은 값은 위 필드로 표현한다.

## 4. 판정 권한 — ⓐ ⓑ ⓒ

| 판정 | Lead 권한 | 필수 |
|---|---|---|
| **ⓐ 확인** | 테제 `log[]` 에 `{date, mark:"ⓐ", rid, text}` append · `last_tested` 갱신 | 「같은 말을 더 세게」 금지 — `priced_in ≈ variant` 면 log 만 남기고 `action: no-edge` |
| **ⓑ 도전** | `status` → `도전` · `basis` 재작성(≤220자 · 날짜 꼬리표) · `log[]` mark ⓑ · **`resolve_by`** | 사람이 주간 감사에서 `정정`·`철회`·`유지` 로 확정. Lead는 확정하지 않는다 |
| **ⓒ 신규** | 배치처 페이지가 있으면 테제 append (`id` 다음 번호 · `claim·basis·falsifier·event·status:"관측"`) | `falsifier` 와 `event` 없으면 거절. 페이지가 없으면 `open.json` 에 「판단 0편」으로 |
| **이미 판정** | routing 에 새 줄 없이 intake `routed:true` + `routing:` 기존 r-id | grep 으로 그때 줄을 실제로 읽었을 때만 |

수급·13F·환율·금리는 테제에 넣지 않고 **크기와 창을 밝힌 관측**으로만(`CLAUDE.md` §J4). 보유 종목의 수급이 테제와 어긋나면 `docs/judgment_protocols_2026-09-23.md` §2 (hold rule) — 사이즈 언급 없이 관측만.

## 5. 사용자에게 먼저 말하는 것 (§J4) — watch.py 가 뽑아 준다

지난 판정 이벤트 · 스톱·매도선 도달 · 보유 종목 테제 `status` 변경 · `breaks_if` 관측치 충족 후보. 이 넷은 세션이 열리지 않아도 `watch.yml` 이 매일 보낸다. Lead가 이 중 하나를 **만들었으면**(ⓑ 도전 등) 커밋 메시지 첫 줄에 `[J4]` 를 붙인다.

## 6. 하지 않는 것

- 집행 지시(「N주」·「X%」·「지금이 타이밍」) — 사용자 몫. 매매 구조·틀렸을 때 잃는 크기·판정 이벤트까지의 거리는 **물으면 전부** 준다.
- 묻지 않은 포트폴리오 구성 진단.
- 브레인 10번째 파일 · 새 저장소 · HTML 일괄 수정.
- 「확인 불가」를 시도한 호스트·경로·티커 없이 적는 것(§W5).
- 대화에만 있는 값 — 검색·계산 결과도 intake 한 줄 + `files/` 조각.

## 7. 종목·포지션 질문에 답할 때 (§J2)

`python3 portfolio/data/packet.py <이름|티커>` 로 패킷을 뽑고 **그 위에서만** 답한다.
⓪ `regime.one` ① 기준일 ② 가격이 전제하는 것(배수 → 분자·분모) ③ 오늘 정보의 방향 ④ 각 선택지의 대가 ⑤ 등급 ⑥ 포트 영향(`exposures` · 단일 반증에 걸리는 금액 — 값이 null 이면 「미측정」이라고 말한다).
답을 냈으면 `routing.jsonl` 에 `kind:judgment · source:"J2 <질문 요지>" · resolve_by` 한 줄 — 조언도 채점된다.

## 8. 검사 명령

```
python3 .githooks/check_routing.py            # 스키마·포인터·테제 접촉 (exit 1 = 커밋 금지)
python3 .githooks/check_intake.py             # 포인터 실재 · id 중복 (경고)
python3 .githooks/check_facts.py              # facts ↔ 페이지 값 (경고)
python3 portfolio/data/watch.py               # §J4 감시 · 큐 크기
python3 portfolio/data/packet.py SK하이닉스    # 종목 패킷
```
