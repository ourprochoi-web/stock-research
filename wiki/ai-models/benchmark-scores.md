# AI 모델 벤치마크 점수 이력
related: ai-sw/ai_sw_overview.html#T1 · entity:ANTHROPIC · entity:OPENAI · entity:META

비정본 배경 위키. 회사 발표 점수는 C(미검증), 독립 평가(AA 등)는 B. append-only. 이전 점수(AA Opus 58·Sonnet 56·Muse Wonder 52 등)는 brain watch r-20261016-556·r-20261013-206에 있다.

| 날짜 | 출처 | 등급 | 모델 | 벤치 | 점수 | 비교 |
|---|---|---|---|---|---|---|
| 2026-10-17 | 딥시크 공지 x.com/deepseek_ai/status/2111375640717033777 via intake/files/telegram/Samsung_Global_AI_SW/2026-10-17/4801.txt | C | DeepSeek-V4.1-Flash-1017(MIT 가중치·100만 토큰) | Terminal-Bench 4.0 | 31.2→42.3 | GPT-5.6 Sol 39.9 · Claude Opus 5 51.8 |
| 2026-10-17 | 同 | C | 同 | ProgramBench | 20.3→29.1 | — |
| 2026-10-17 | 同 | C | 同 | Automation-Bench / Agents' Last Exam / Apex | 54.8→60.5 / 31.8→35.4 / 64.6→72.1 | 세 지표 모두 Sol·Opus 5 상회 주장 |
| 2026-10-17 | 同 | C | 同 | HLE / Chartography | 36.8→42.6 / 78.9→83.0 | HLE: Sol 44.5 · Opus 5 56.3 |
| 2026-10-13 | intake/files/telegram/Samsung_Global_AI_SW/2026-10-13/4769.txt | B | Meta Muse Wonder / Wonder Full | AAII | 52 / 56 | Muse Spark 1.3(6주 전) 48 |
| 2026-10-16 | c-20261016-t86(채널 요약) | B | Meta Muse Spark Open(816B·활성 42B) | AAII | 39 | Mistral Large 4 38 |
| 2026-10-04 | 씨티 via c-20261004-t01 | B | Gemini 4 Argon(9/30) | AA | 53 | Fable 5.1·GPT-6 Astra와 같은 수준(씨티 서술) |
| 2026-10-19 | 손경제 김아람 7J8fmfx-9m8 · intake/files/youtube/sonkyung/2026-10-19/today_02.md | C/ASR | Gemini 4 Argon | 아레나 / Vals / 환각률 | 종합·지시이행 1위·웹개발 8위 / 1위(구글 첫 1위) / 15%(정답률 50%) | 오픈AI 환각 50%대(정답 63%) ·  AA 지수 Opus 5.5 58·Muse Wonder Full 56·Argon 53(방송). 앱 기본 미디엄 vs 발표 하이 모드. API 반값 11/30까지 |
| 2026-10-19 | minimax.io/blog/minimax-m31f via intake/files/telegram/2026-10-19/pull_214157/samsung_4813.txt | B | MiniMax M3.1 Flash(익명 Space Bunny 정식판) | DeepSWE v1.1 / OSWorld V2 / ALE / CyberGym / BankerToolBench | 73.7% / 61.7 / 29.6 / 82% / 76.2 | 가격 입력 $0.15·출력 $0.60(100만 토큰), 출력 170~200TPS, 가중치 10/23 공개, Pro 예고 |
| 2026-10-24 | t.me/Samsung_Global_AI_SW/4861(채널 요약, 미대조) (routing r-20261024-15) | B | Moonshot Kimi K3.1 Pro(2.8T·활성 104B) | AAII | 55(4위) | 오픈·클로즈드 격차 12→3점 주장, 가중치 11/4까지 공개 예정 |
