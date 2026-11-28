# 타이거일렉(219130) 후보 카드 개설 — 들어온 것 (판단은 routing)

- 승인: Kenneth, 2026-11-28 09:14 KST. 타이거일렉(코스닥 219130) 후보 카드를 연다. 보유·현금·스톱·regime.one·다른 테제 status는 건드리지 않는다.
- 하우스 원문(이미 intake에 있음. 이 파일은 다시 베끼지 않음):
  - 2026-11-10 메리츠 양승수 연간전망 기업분석 줄 — Buy(신규), 120,000원. `c-20261110-t83` (routing에 삼성전기로 이미 착지. PDF 본문은 이 세션에서 안 열음).
  - 2026-11-16 게시, 수집일 2026-11-17. 3Q 리뷰 Buy 유지, 적정주가 130,000원. `c-20261117-t32`. 파일 `intake/files/telegram/meritz_research/2026-11-16/45184.txt`.
  - 2026-11-27 NDR. `c-20261127-t68`. 파일 `intake/files/telegram/meritz_research/2026-11-27/45242.txt`.
- 10/26 프리뷰(매출 348억·OP 86억)는 `r-20261026-30`이 `parked:open`에 두었고 카드는 없었다. 그 줄은 수정하지 않음.

## 네이버 시세 (2026-11-28 조회, 11/27 정규장 완료)

- 일봉: `https://api.stock.naver.com/chart/domestic/item/219130/day` — 20261127 closePrice 81700, open 76900, high 82700, low 73500, volume 48850.
- 통합: `https://m.stock.naver.com/api/stock/219130/integration` — 전일 76,900, 대금 38.8억, 시총 5,159억, 52주 최고 120,000, 52주 최저 19,500, PER 33.02배·EPS 2,474원(2026.09), PBR 7.19배·BPS 11,367원(2026.09), 추정PER N/A. 목표가 평균 119,000원(consensusInfo createDate 2026-11-26).
- 이름: `https://m.stock.naver.com/api/stock/219130/basic` — stockName 타이거일렉, closePrice 81,700, localTradedAt 2026-11-27T20:20:20+09:00, KOSDAQ.
- 코스닥: `https://api.stock.naver.com/chart/domestic/index/KOSDAQ/day` — 20261127 closePrice 708.99.

산술(이 파일의 계산, 공시 아님): (120,000−81,700)/120,000 = 31.9%. 81,700/11,367 = 7.19. 2027E 영업이익 476억 × (1−0.22) = 371.28억. 시총 5,159억 / 371.28억 = 13.9배. 22%는 세무 공시가 아니다.
