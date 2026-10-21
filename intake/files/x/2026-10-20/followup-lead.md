# 2026-10-20 A티어 Lead 보강 수집 (follow-up)

- 작성: 2026-10-21 (수) 약 09:31 KST, x-intake Bot
- 범위: Lead 요청 4건만. 수집만 했고 투자 판단, keep/drop, J2, brain/git은 하지 않았음.
- 원자료: `/workspace/x-intake/raw/2026-10-20-followup/` (X 응답 13개, 디일렉 HTML, 이미지 3장)
- X 호출: **13회** (get_posts_by_ids 2 · get_posts_counts_recent 2 · search_posts_all 7 · get_users_posts 2). 429 없음, 로그인벽 없음. 마지막 확인 시 남은 한도: 일 924/1000.
- 웹: WebSearch 6 · WebFetch 3 · curl 3 (t.co 리다이렉트, 디일렉 HTML, biztoc)

---

## (1) 삼성전기–마이크론 기판 LTA 실명 출처 — **확인됨(단, 원문 기사에 '마이크론'은 없음)**

### 리다이렉트 체인
- `https://t.co/78giizlzWy` → HTTP 301 → **`https://www.thelec.kr/news/articleView.html?idxno=63936`** (GET 200, HEAD는 404)
- X API의 unwound_url도 같은 URL이고, title은 "삼성전기, 첫 패키지 기판 LTA…3600억원 규모 공급계약 체결 - 디일렉(THE ELEC)"

### 실명 출처
- **매체:** 디일렉(THE ELEC)
- **제목:** 삼성전기, 첫 패키지 기판 LTA…3600억원 규모 공급계약 체결 (부제: 글로벌 대형기업과 1년 계약)
- **기자:** 문슬예 기자
- **입력:** 2026-10-19 19:03 KST (`article:published_time` 2026-10-19T19:03:26+09:00)
- **URL:** https://www.thelec.kr/news/articleView.html?idxno=63936
- **해당 문장(원문 그대로):**
  > 삼성전기가 글로벌 대형기업과 3605억원 규모의 메모리 반도체용 패키지기판 공급계약을 체결했다고 19일 공시했다. 계약 기간은 2027년 1월 1일부터 12월 31일까지다. 계약금액은 지난해 연결 매출의 3.2%다.
  > 패키지기판 장기공급계약(LTA) 공시는 이번이 처음이다. 이번 계약으로 올해 공시한 LTA가 7건으로 늘었다.

### 중요한 차이
- 받은 HTML에서 찾아보니 **'마이크론'·'Micron'·'SSD'·'ABF'·'엔터프라이즈'·'기업용'은 0회**였음. 기사는 계약 상대를 **"글로벌 대형기업"**으로만 썼음.
- 그래서 **"마이크론", "엔터프라이즈 SSD용", "BT·ABF 기판"은 @jukan05가 덧붙인 내용**이고, 링크된 원문으로는 확인되지 않음. 다른 실명 출처도 못 찾았음.
- 다른 매체의 설명:
  - 삼성전기 보도자료(2026-10-19): "글로벌 대형기업과 3,605억 원 규모의 '메모리 반도체용 패키지기판' 장기공급계약(LTA)" — https://www.samsungsem.com/kr/newsroom/news/view.do?id=10601 (영문 id=10602)
  - 서울경제 영문(2026-10-19 17:45 KST): "The counterparty was not disclosed under a confidentiality agreement." 금액은 $251M로 환산 — https://en.sedaily.com/finance/2026/10/19/samsung-electro-mechanics-wins-251-million-chip-substrate
  - 컨슈머타임스: "회사는 계약 상대를 '글로벌 대형기업'으로만 밝혔다… 글로벌 메모리 업체 가운데 한 곳으로 추정된다." — https://www.cstimes.com/news/articleView.html?idxno=724513
  - 키움증권 권민규(10/20 보고서, 이데일리 인용): "글로벌 메모리 업체 대상 메모리 BGA(BT기판) 기판 위주 공시" — 즉 **BT 중심이고, ABF(FC-BGA)와는 구분**해서 봤음 — https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02574806645614888
  - Bluesky @fintwitter.bsky.social에 jukan05와 같은 문장이 올라와 있음(출처 없음, 미러로 보임) — https://bsky.app/profile/fintwitter.bsky.social/post/3mybc5cb3jy2r
- 금액: 3604억8776만원(컨슈머타임스). 서울경제는 $251M로 환산했고, psinvestor의 "~$260M"과는 환율 차이로 보임.

### 관련 X 글
- @jukan05 2112327685540380724 — **2026-10-20 08:39 KST** — https://x.com/jukan05/status/2112327685540380724
  > South Korea’s Samsung Electro-Mechanics has signed a long-term agreement (LTA) with U.S.-based Micron to supply BT substrates and ABF substrates for enterprise SSDs. https://t.co/78giizlzWy
- @psinvestor 2112329173050245264 — 2026-10-20 08:44 KST (위 글 인용, 첨부 이미지는 기판 사진 1장으로 수치는 없음) — https://x.com/psinvestor/status/2112329173050245264

**상태:** 출처(디일렉)는 확인됨. 금액·기간·"첫 패키지기판 LTA"는 원문과 맞음. **상대방 "마이크론"과 "엔터프라이즈 SSD·ABF"는 원문으로 확인 안 됨.** 공식 발표는 상대를 밝히지 않았고, 서울경제는 비밀유지 계약 때문이라고 썼음.

---

## (2) BofA CRWV 노트(YE28 4.8GW · $43.3B · 백로그 대비 ~$12B) — **노트 원문(PDF)은 못 찾았음. 노트 표 캡처와 실명 보도는 확보**

### 인용 체인 (X)
1. @datacenter365 2112171215297114184 — 2026-10-19 22:17 KST: "BofA projections have $CRWV generating ~$43.3B for FY2028" — https://x.com/datacenter365/status/2112171215297114184
2. @SmallCapSnipa 2112320198959104205 — **2026-10-20 08:09 KST** — https://x.com/SmallCapSnipa/status/2112320198959104205
   > BofA sees $CRWV becoming a 4.8 GW business generating $43.3B of revenue by YE28 👀 … “Under our assumptions, initial Vera Rubin contracts that were likely signed early in 2026 generate approximately $12/watt annually, with pricing gradually increasing to $14/watt annually by the end of 2028.”
   - 첨부 이미지(https://pbs.twimg.com/media/HVB4Bs_WUAA_4CF.jpg)는 **BofA 노트 표 캡처**: "Exhibit 1: We expect revenue to grow 105% in FY27 and 63% in FY28 — Active power, $/watt, and revenue estimates, FY26-FY28", Source: BofA Global Research estimates, company report. 주요 숫자: Active Power FY26E 1,900 / FY27E 3,300 / **FY28E 4,800MW**, Total Revenue FY26E $12,934M / FY27E $26,550M / **FY28E $43,347M**, Annualized $/Watt 1Q26 $9.20 → 4Q28 $14.00.
3. @psinvestor 2112325425523216520 — 2026-10-20 08:30 KST (2를 인용) — https://x.com/psinvestor/status/2112325425523216520
   - 첨부 인포그래픽(https://pbs.twimg.com/media/HVB6y_0bsAAXNWE.jpg)에 출처가 "BofA, CoreWeave 10-Q"로 적혀 있고, 패널에 **"My math, BofA estimates vs 10-Q backlog"**라고 되어 있음: BofA 매출 추정(3Q26~2Q28) $54.3B vs 24개월 안에 들어올 백로그 $42.7B(10-Q 기준 $104.2B의 41%) → **"~$11.6B"**.
4. @psinvestor 2112325999136493656 — 2026-10-20 08:32 KST (@SmallCapSnipa 답글, 3 인용): "BofA is ~$12B ahead of the backlog. New deals have to come in soon." — https://x.com/psinvestor/status/2112325999136493656

→ **"백로그 대비 ~$12B 앞섬"은 BofA 숫자가 아니라 psinvestor가 직접 계산한 값임**(본인 이미지에 "My math"라고 표기). BofA 숫자는 4.8GW, $43.3B, $/watt임.

### 웹 실명 출처 (BofA 노트 보도)
- Yahoo Finance, Brian Sozzi, "Why CoreWeave stock may still rise over 100% despite financing fears, analyst says", **2026-10-15 08:51 EDT (=10/15 21:51 KST)** — https://finance.yahoo.com/markets/stocks/article/why-coreweave-stock-may-still-rise-over-100-despite-financing-fears-analyst-says-125123226.html
  > "We are increasing our revenue growth estimates for CoreWeave from 102% and 58% in 2027 and 2028 to 105% and 63%, respectively, driven by our assumptions for active power and prices. We expect the company to add 1.4-1.5GW of power annually in FY27 and FY28, and assume higher revenue per megawatt (MW), increasing from ~$10 currently to $14 by year end 2028, on the back of Vera Rubin deployments," BofA analyst Tal Liani said in a note on Thursday.
  - 목표가 $140, Buy. 노트 날짜는 **2026-10-15(목, 미국 기준)**.
- Yahoo Finance(TheStreet 계열), "Bank of America Has Blunt Message on CoreWeave Stock After Selloff": "$26.5 billion in 2027 and $43.3 billion in 2028, up from previous estimates of $26 billion and $41 billion" — https://finance.yahoo.com/markets/stocks/articles/bank-america-blunt-message-coreweave-183050594.html (검색 스니펫으로만 확인, 날짜 미확인)
- Finimize: "reach 4.8 gigawatts of active power by end-2028" — https://finimize.com/content/bank-of-america-thinks-coreweaves-power-plans-improve-the-ai-math
- Seeking Alpha, "CoreWeave remains Buy at BofA after stock drop" — https://seekingalpha.com/news/4653524-bofa-keeps-buy-on-coreweave-after-stock-drop-sees-higher-revenue (페이월, 스니펫만 확인)
- 참고: 기사들은 "revenue per MW ~$10 → $14"라고 썼지만, BofA 표 단위는 **$/watt(연환산)**임. 기사 쪽 표기가 단위를 잘못 옮긴 것으로 보임.

**상태:** BofA 노트 원문(PDF)이나 원문 링크는 **찾지 못함**(BofA Global Research는 비공개). 노트 표 캡처(SmallCapSnipa 이미지)와 Tal Liani의 직접 인용(Yahoo)은 확보함. ~$12B는 psinvestor 계산값으로 확정.

---

## (3) Lumentum CEO Michael Hurlston, 2026-10-09 Bloomberg 인터뷰 — **확보(bloomberg.com 원문 URL은 못 찾았음. 블룸버그 로 발행본과 신디케이션으로 대체)**

- **제목:** "Nvidia-Backed Lumentum Sold Out of AI Server Parts Till 2029"
- **작성:** Takashi Mochizuki, Shery Ahn, Mari Kiyohara (Bloomberg). 인터뷰 장소는 도쿄, 날짜는 금요일(2026-10-09)
- **발행:** Bloomberg Law 게시 2026-10-09 01:53 UTC (=**10/09 10:53 KST**), 업데이트판 "(1)", "(2)" 있음
- **URL:**
  - Bloomberg Law(블룸버그 계열, 리드 문단만 공개): https://news.bloomberglaw.com/health-law-and-business/nvidia-backed-lumentum-sold-out-of-ai-server-parts-till-2029-1 · https://news.bloomberglaw.com/mergers-and-acquisitions/nvidia-backed-lumentum-sold-out-of-ai-server-parts-till-2029-1
  - **신디케이션(전문에 가까움):** Moneyweb (2026-10-09 14:00 SAST=21:00 KST) https://www.moneyweb.co.za/news-fast-news/nvidia-backed-lumentum-sold-out-of-ai-server-parts-till-2029/ · The Japan Times (2026-10-09, 앞부분만 공개) https://www.japantimes.co.jp/business/2026/10/09/companies/lumentum-ai-server-sold-out/
  - 방송: Bloomberg TV "The Asia Trade"(Shery Ahn) 영상 "Lumentum CEO: Opto-Parts Capacity Sold Out to 2029", Yahoo 게시 2026-10-09 01:36 UTC(=10:36 KST) https://finance.yahoo.com/video/lumentum-ceo-opto-parts-capacity-013640075.html
  - 2차 요약: Quartz https://qz.com/lumentum-ai-data-center-optical-parts-sold-out-2029-100926
- **핵심 인용(Moneyweb/Japan Times 신디케이션 원문 그대로):**
  > Lumentum Holdings’ optical components are “completely sold out” through early 2029 on demand from tech companies clamoring for faster artificial intelligence data centers, according to its chief executive officer.
  > Lumentum is unable to meet about 70% of demand for some products through next year, and won’t be able to address 30% of demand for some other products through 2028, Michael Hurlston said in an interview in Tokyo on Friday. Just six months ago, Hurlston said Lumentum was on track to sell out its capacity by 2028.
  > “We are really trying to catch up, add capacity as fast as we can, but we are very, very far behind what customers want,” Hurlston told Bloomberg News. “We are completely sold out, so there’s no end in sight.”
  > “I think probably in the next year, we’d like to add additional capability to what we currently have,” (인수 관련)
  > “These hyperscalers are willing to put money behind it.”
  - Bloomberg Law 업데이트판에 추가된 문장: "Customers are already starting to lock in orders for 2030, he added."
  - 그 밖의 내용: 도쿄권 공장 생산능력을 2년 동안 12배로 늘림, 그 공장과 인근 시설에 최소 $3.5억 투자, 영국 Caswell 공장 증설, 새 생산능력을 만드는 데 3~5년 걸림
- **상태:** bloomberg.com 원문은 페이월이라 URL을 찾지 못함(biztoc 미러에서도 링크를 못 뽑음). **제목, 작성자, 시간, 인용문은 Bloomberg Law 리드와 신디케이션(Moneyweb, Japan Times) 원문으로 확인함.** psinvestor가 쓴 "광부품 용량 2029년까지 매진"(10-19 22:43 KST)은 원문의 "completely sold out through early 2029"와 맞음.

---

## (4) 미수집 3건 재시도 — **회수 불가로 확정** (추정 원인: 구독자 전용 게시물)

### 정확한 위치 (counts_recent, 분 단위)
- from:blazingbees 10/19 23Z: 5건 = 23:15×2, 23:19, **23:50, 23:59**. 23:15×2와 23:19 3건은 이미 수집됨(2112321768656687516, 2112321781390569678, 2112322713054519332).
  → 미수집: **10/20 08:50 KST 1건, 08:59 KST 1건**
- from:Liberty0918 10/19 23Z: 2건 = **23:12**, 23:17. 23:17은 이미 수집됨(2112322271461441549).
  → 미수집: **10/20 08:12 KST 1건**

### 시도한 방법 (모두 해당 글이 안 나옴)
1. search_posts_all `from:blazingbees` 23:45–00:01Z(+next_token 페이지): 이미 수집한 00:00:05Z와 00:00:10Z 2건만 나오고, 다음 페이지는 0건
2. get_users_posts(blazingbees) 23:40–00:01Z: 같은 2건만 나옴
3. search_posts_all `from:Liberty0918` 23:05–23:20Z: 이미 수집한 23:17 1건만 나옴
4. get_users_posts(Liberty0918) 23:05–23:20Z: 같은 1건만 나옴
5. 대화 스레드 `conversation_id:2112322713054519332`(blazingbees 08:19 KST 글): 23:19Z 이후 답글 25건 중 숨은 부모 글 없음
6. `to:blazingbees` 23:45–00:30Z와 23:45–02:00Z, `to:Liberty0918` 23:05–03:00Z: 남들이 단 답글이 가리키는 부모 글 ID가 전부 이미 수집한 글이거나 창 밖의 글이었음. 미수집 글에 달린 공개 답글은 없음.

### 원인 정황 (작성자 본인 글, 추정)
- blazingbees 2112332993377530197 — 10/20 09:00 KST — https://x.com/blazingbees/status/2112332993377530197
  > @crossroad_dui 말씀하시는 동안 구독 코멘트 하나 더 올라갔습니다 ㅎㅎㅎ
  - 바로 앞 글인 @crossroad_dui 2112331918507483344(08:55 KST)는 "@blazingbees 오늘도 구독코멘트 감사합니다 ㅎㅎ 오늘 장 준비 완료~"
- Liberty0918 2112322271461441549 — 10/20 08:17 KST — https://x.com/Liberty0918/status/2112322271461441549
  > …지금 막 구독자 콘텐츠로 반도체 장비 대장주 한 종목 분석해서 올렸음.
- 미수집 시점(08:50, 08:59, 08:12 KST)이 위의 "구독 코멘트/구독자 콘텐츠 올렸다"는 말과 맞음. 그래서 **X 구독자 전용 게시물이라 API로 보이지 않는 것으로 추정**함. 확정된 원인은 아님. 삭제됐거나 보호계정에 단 답글일 수도 있음.

**상태:** 전문, 링크, ID는 회수 불가로 확정. 시간(KST)만 counts로 확인했음(분 단위: 08:12, 08:50, 08:59). 나머지 미수집 6건(blazingbees 02Z, 03Z, 13Z, 14Z, Liberty0918 11Z, NURadu_ 19Z)은 지시대로 시도하지 않았음.
