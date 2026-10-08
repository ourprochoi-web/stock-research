# ledger/ — 판단의 채점

판단의 정본은 `brain/` 아홉 파일이다. 여긴 그 판단이 나중에 맞았는지를 적는 측정 층이다. 설계는 `docs/judgment_ledger.md`. `AGENTS.md` §9 는 제안이고, `check_routing.py` 는 이 디렉터리를 보지 않는다.

| 파일 | 내용 |
|---|---|
| `judgment_ledger.jsonl` | 티커당 한 행. 스탠스 · 완료된 기준가 · breaks_if · 독립 출처. `scores` 만 채점기가 갱신 |
| `schema.json` | 행 스키마 |
| `score_summary.json` | 스탠스 · lead · 페이지별 집계 |
| `scorecard.json` | 테제별 확인/반박 수, 연속 ⓐ, priced_in 경고, breaks_if 상태 |

```
python3 scripts/backfill_ledger_sample.py   # 2026-10-08 표본을 다시 받는다
python3 scripts/check_ledger.py
python3 scripts/score_ledger.py
python3 scripts/test_ledger.py
```

저장소 루트에서 실행한다. 수량 · 비중 · 스톱은 이 파일에 없다.
