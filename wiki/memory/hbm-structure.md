# HBM 구조·수요 산식
related: memory 테제 · hbm-packaging

## 수요 산식 이력
| 날짜 | 출처 | 등급 | 내용 |
|---|---|---|---|
| 2026-10-13 | X @Liberty0918, /workspace/x-intake/packets/2026-10-14-a-tier-lead.txt | C(미검증) | MS 2027년부터 자체 칩 Maia 300 수 GW 확대 계획, 100만 개 배치 시 HBM4 약 800만 스택 필요(칩당 ~8스택 산식) |
| 2026-10-08 | X, /workspace/x-intake/packets/2026-10-08-a-tier-lead.txt | C | AMD MI455X HBM4 주요 공급 협력에 삼성 공식화(게시자 주장) |
| 2026-10-13 | /workspace/telegram-intake/pull_20261013_093820_new.md | B | CoWoS 등 첨단 패키징·HBM4·CPO 도입으로 칩 통합 난이도와 테스트 시간 동시 증가 |
| 2026-10-18 | 서울경제 단독 https://www.sedaily.com/article/20102940 · 영문 en.sedaily.com 2026/10/18 · 로이터 인용(boursorama) · intake/collected.jsonl c-20261018-t52 (PR #141) | B | NVHBM(2026-08 공개, HBM4E 기반 커스텀): 엔비디아가 공급 3사(삼성·SK하이닉스·마이크론)에 베이스다이 TSMC 3나노·코어다이 1c D램 통일 요구, 삼성 DS 수용 — HBM 제조 단계에서 삼성–TSMC 첫 협업. 표준 HBM4·HBM4E와 AMD 등 다른 커스텀은 삼성 4나노 베이스다이 턴키 유지, NVHBM도 자사 파운드리(2나노) 생산 검증 중 |
| 2026-10-18 | 서울경제 영문판(同) | B | NVHBM 구조: GPU에 있던 메모리 컨트롤러를 베이스다이로 옮기고 PHY를 표준 대비 60% 줄임 → 표준 HBM4E 대비 대역폭 최대 +30%·전력 −15%(기사 서술). 업계 추정 수율 TSMC 3나노 90%+ 대 삼성 SF2 약 60%. 삼성 4나노 베이스다이 라인은 화성 17라인·평택 P3 일부뿐 |
| 2026-10-18 | UBS via 서울경제 영문판 | B | 2027 HBM 수요 약 615억Gb(+91% YoY) 대 메모리 3사 신규 출하 약 546억Gb → 수요 대비 약 10% 부족 |
| 2026-10-18 | 로이터 via Business Standard(서울경제 인용) · intake/files/web/2026-10-19/nvhbm_sedaily_reuters.md | B | NVHBM 베이스다이: 엔비디아가 공급 3사에 TSMC 3nm 베이스다이·1c 코어다이 통일 요구, 삼성 수용 보도. 표준 HBM·다른 고객 커스텀은 자체 생산 유지, TSMC 캐파 초과 시 자사 파운드리 생산 평가(익명 소식통). 회사 확인 없음 |
| 2026-08-28 | 서울경제 20084484 · 同 | B | NVHBM은 HBM4E 8단 기반, 속도 사양 17~18Gbps(삼성 초기 HBM4E 샘플 14.4Gbps), 루빈 울트라부터 적용 가능성(기사 서술) |
| 2026-10-19 | JP모건 APAC via aether · intake/files/telegram/2026-10-19/pull_133857/aether_25924.txt | C | NVHBM 생산은 TSMC N3 캐파 여유가 생기는 FY28에 대부분(하우스). 엔비디아 주장 스택당 대역폭 +30%, 로직 베이스다이 조달은 사실상 엔비디아 통제 |
