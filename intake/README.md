# intake/ — 수집 층 (원문 충실 · 판단 금지 · 덧붙이기만)

**세 층의 첫 번째다** — `intake/`(무엇이 언제 왔나) → `brain/`(그래서 어떻게 보나) → 리서치 페이퍼(왜 그렇게 보는지 설명). 2026-09-13 사용자 결정.

| 파일 | 담는 것 | 쓰는 순간 |
|---|---|---|
| `user.jsonl` | **사용자가 준 것** — 뉴스·IB 요약·방송·소셜·지시. `{id, date, channel, source, title, text(원문 또는 충실한 요약), grade_hint, used_by}` | 받는 즉시, 라우팅 **전에** |
| `collected.jsonl` | **내가 받은 것** — 공시·XBRL·시세·월지표·뉴스레터. `{id, date, kind, host, path, subject, status(ok/blocked/404), file, note, used_by}` | 받는 즉시. **실패도 적는다**(호스트 포함 — §W5가 자동으로 지켜진다) |
| `files/` | 받은 조각의 스냅샷(작은 텍스트·JSON). `collected.jsonl`의 `file`이 가리킨다 | 재현이 필요할 값이면 남긴다 — XBRL 조각·공시 절·뉴스레터 본문 |

## 규칙
1. **판단을 쓰지 않는다.** 등급도 `grade_hint`(출처 수준의 힌트)까지만. 주장 단위 등급·라우팅은 `brain/routing.jsonl`이 한다.
2. **id 로 이어진다.** `brain/routing.jsonl`의 `intake`, `brain/facts.json`의 `companies.*.intake`가 여기를 가리킨다. 훅이 포인터가 실재하는지 검사한다.
3. **재등장 대조는 여기서 grep** — 출처·날짜·핵심 문장. 같은 정보가 다시 오면 첫 id 를 `routing`에서 찾아 그때 무엇을 적었는지 본다(§R2의 「이미 판정」).
4. **버리지 않는다.** 배치처가 없어 브레인에 안 올라간 항목도 여기엔 남는다 — 세 번째 등장에서 앞의 두 번을 찾을 수 있게.
5. **자동 수집** — `collect.py`가 매일 워크플로에서 일일 브리핑(soonsal)과 TSMC 월매출 페이지, **그리고 v2(09-15)부터 매크로 스냅샷**(FRED 금리·유가·HH·VIX + 네이버 코스피·투자자별·세계지수 + 추적 종목 breadth → `files/macro/{날짜}.json`)을 받아 `collected.jsonl`에 한 줄과 `files/`에 스냅샷을 남긴다. 판단은 하지 않는다. 라우팅은 다음 세션이 `status:ok · routed:false` 항목을 읽어서 한다.

6. **시세 정의를 적는다** — 네이버 국내 `closePrice`는 2026-09-14부터 **20:00 애프터마켓가**다. 09-15부터 `update_prices.py`가 **분봉 15:30 바로 정규 종가**를 받아 `prices`에, 애프터마켓가는 `after`에 둔다(`priceDefinition` 필드). 소스 지도는 `collect_sources.py`(스카우트 2026-09-15 · `docs/datasource_scout_2026-09-15.md`).
7. **내가 직접 받은 것도 여기다** — 웹 검색·API 값·계산 결과는 `collected.jsonl` 한 줄 + `files/`에 조각(URL 포함). 대화에만 있는 값은 없는 값이다(09-14 실측: files/ 0개였다).

## 시드(2026-09-13)
사용자 항목 5건 · 수집 항목 8건(광통신 3편의 데이터 출처 + 오늘의 프록시 403 실패 기록). **원문 조각은 없다** — 시드 시점에 보관하지 않았던 것을 소급해 만들지 않는다. 다음 수집부터 `files/`에 남긴다.


## 편입 규칙 v1 (2026-09-16 · 사용자 결정 r-20260916-23)
리포트·방송·뉴스에서 **매수/관심 콜로 등장한 종목은 `update_prices.py` WATCH(KR)/WATCH_US 에 편입**한다(코드는 naver `front-api/search/autoComplete`). 편입 = 시세·재무·스크린 **추적**이지 판단이 아니다 — 판단은 스크린 G/P/Q/E 와 브레인 테제만 한다. 라우팅할 때 종목 콜이 나오면 같은 커밋에서 편입한다.


## routed 값 (2026-09-17)
`routed:false` = 주장이라 라우팅이 필요한 것(세션 시작 시 처리). `routed:"data"` = XBRL·매크로·월지표 스냅샷처럼 **주장이 아니라 원료**인 것 — facts/regime 이 직접 읽으므로 라우팅하지 않는다. 봇이 kind 로 자동 분류한다(수집 실패 기록만 false).


**2026-09-26 추가 — `routed:"skip:<이유>"`** = 라우팅 대상이 아니라고 <분류>된 것(`intake/triage.py` · 판단 아님). 이유는 `link`(링크만) · `short`(본문 40자 미만) · `media`(미디어만) · `no-claim`(이름 색인 매치도 주장 신호도 없음) · `no-thesis`(Lead가 배치처 없음으로 닫음) · `digest`(요약만 남김 · `summary` 필드). 줄과 `files/` 조각은 남는다(규칙 4). 주장이 있으면 `routed:false` + **`candidates[]`**(name_index 매치 → 걸리는 `page#T` 후보). 큐를 셀 때는 `routed is False` 만 센다.
`user.jsonl` 은 `routed` 필드 없이 `used_by` 만 있는 줄이 113건 있다(09-25 실측) — 새 줄은 `routed` 를 반드시 쓴다.

## Telegram 공개채널 수집 (2026-09-23)
`collect_telegram.py` + `.github/workflows/collect-telegram.yml` — Bot API 없이 `t.me/s/{handle}` 미리보기 HTML에서 최근 글을 받는다. 화이트리스트는 `requests/telegram_channels.txt`(handle | notes). 원문 스니펫은 `files/telegram/{handle}/{YYYY-MM-DD}/`, 한 줄은 `collected.jsonl`(kind:`telegram` · url 로 중복 제거). **09-26부터 쓰기 전에 `triage.py` 로 분류** — 주장이 있으면 `routed:false`+`candidates`, 없으면 `routed:"skip:*"`. 09-25 소급 적용: 447건 → 큐 260(후보 115) · skip 187. 스케줄 6시간마다 + 수동 `workflow_dispatch` + 화이트리스트 push. 판단은 하지 않는다.
