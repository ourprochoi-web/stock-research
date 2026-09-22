# X A티어 후속 — 리드 요약 (2026-09-22 KST)

대상: Kenneth · parent 전달용  
범위: `intake/files/x/2026-09-22/` 스테이징만 (`brain/*.json` 비파괴 · push 없음 · 주문 없음)

---

## 한 줄

A티어 keep 10건을 `user_append_draft.jsonl`에 올렸고, GS 하이닉스·유가·COHR·수급·드러켄밀러 후속을 **실측/원문까지** 닫거나 막힌 지점을 표시했다. 드러켄밀러 원익IPS는 **한경 당일 대면 보도**로 루머→문서화 관측(**grade ② 유지**, ① 아님).

---

## 검증 결과

| # | 항목 | 결과 | 등급 | 산출물 |
|---|---|---|---|---|
| 1 | keep → user 스테이징 | x01–x10 + **x11**(드러켄 승격) | — | `user_append_draft.jsonl` |
| 2 | GS SKH 버추얼 | Liberty 스레드 요약 확보 · 라우팅 초안 | ③ | `routing_draft_r-20260922-x.md` |
| 3 | 호르무즈 7일 재개방 | **Kyodo English 원문 확인** + Reuters 병행. 조건부 제안(실행≠) | 클레임① / 실행 미발생 | `regime_oil_note_draft.md` |
| 4 | COHR Stifel $420 | pull JSON URL → **KIS PDF fetch 성공** (~613KB) | ③ | `cohr_note_draft.md` + `cohr_kis_stifel_260922.pdf` |
| 5 | SKH 「전부 매도」 | **실측 확인** 09-22 개인·외인·기관 모두 순매도 | ① 집계 | `skh_flow_check.md` |
| 6 | 드러켄×원익IPS | 한경 단독(성남 원익빌딩 대면) + KED | **② 관측** (① 아님) | `druckenmiller_wonik_note.md` · x11 |

### SKH 수급 (2026-09-22, Naver `.../api/stock/000660/trend`)

- 외국인 **−217,556**주 · 기관 **−159,679** · 개인 **−217,329**
- 종가 **1,841,000** (−27,000) · 거래량 ~3.22M
- Daum 외인/기관 동일 부호(외인 −217,357) — **blocked 아님**

### COHR PDF

```
https://kbox.kis-static.finance/mts-home/research-content/pdf/[2642166]260922COHR_20260922154030.pdf
```

Stifel → KIS 국문 재작성 · **매수 / TP $420** · PhotonLink.  
⚠ 기존 Citi COHR TP $420(`u-20260922-18`)과 **하우스 다름** — 혼동 금지.

### 드러켄밀러

한경 단독: 09-22 오전 **성남 원익빌딩에서 기자 대면** · 「한국 투자처 물색」·원익IPS(ALD) 초점 · 두산·삼성 전언.  
KED Global 헤드라인도 Wonik IPS 방문 명시.  
→ **① 아님**(회사/Duquesne 공식 없음). x10 보존 + **x11 관측 승격** · grade_hint **②**.

### 유가 / 헤지

Kyodo EN: https://english.kyodonews.net/articles/-/85911  
연결: open `oil-judgment` · regime `n-hormuz` breaks_if · portfolio `hormuz_open` / 파이프라인·회담 precommit(VG 추가 중단 등).  
**제안 ≠ 통행 재개** — hedge k 축소는 실측 통행·괴리 확인 전 금지.

### GS → 테제 키 (`brain/theses.json`)

- `hbm-packaging/hbm_pkg_company_sk_hynix.html` #T1 #T4  
- `hbm-packaging/hbm_pkg_theme_memory_cycle.html` #T1 #T2  
Verdict 초안: **ⓐ 관측(③)** — JPM 2027 HBM ASP +64%와 동방향 · 문턱 이동 금지.

---

## 아직 열린 것

1. 호르무즈 — 미 측 반응 · 통행량(mb/d) · Dated–선물 괴리  
2. 드러켄 — ①(IR/공시/Duquesne) · 지분 공시  
3. GS 하이닉스 — GS 원문/엄브렐라 원본(현재 X 요약 ③)  
4. COHR — Stifel 영문 원본(선택) · Citi 노트와 병치만  
5. keep 중 기타(매크로·크레딧 등)는 스테이징만(별도 딥다이브 미착수)

---

## 권고 커밋 순서 (로컬 · push 금지)

1. `user_append_draft.jsonl` → `intake/user.jsonl` append (`u-20260922-x01`..`x11`; 기존 `u-20260922-01`..`18`과 충돌 없음)  
2. `routing_draft_r-20260922-x.md` 안 JSON → `brain/routing.jsonl` 한 줄 (`theses.json` 본문 X)  
3. (선택) oil 관측 한 줄을 regime/open **메모 필드만** — 파괴적 rewrite 금지  
4. PDF·노트 md는 이미 `intake/files/x/2026-09-22/` — 경로만 커밋  
5. **brain/theses.json 본문 수정 · push · 주문 — 하지 말 것**

---

## 이번 세션이 쓴/갱신한 파일

```
intake/files/x/2026-09-22/user_append_draft.jsonl
intake/files/x/2026-09-22/routing_draft_r-20260922-x.md
intake/files/x/2026-09-22/regime_oil_note_draft.md
intake/files/x/2026-09-22/cohr_note_draft.md
intake/files/x/2026-09-22/cohr_kis_stifel_260922.pdf
intake/files/x/2026-09-22/skh_flow_check.md
intake/files/x/2026-09-22/druckenmiller_wonik_note.md
intake/files/x/2026-09-22/LEAD_SUMMARY_KO.md
```

선행(미수정): `lead_intake_drafts.jsonl` · `triage-first.json`
