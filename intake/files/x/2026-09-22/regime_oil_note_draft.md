# regime / oil note draft — 호르무즈 7일 내 재개방 제안 (2026-09-22)

**status:** draft only · `brain/regime.json` / `brain/open.json` 비파괴  
**intake:** u-20260922-x03 · X @blazingbees https://x.com/blazingbees/status/2102324218440606083

## 클레임

이란이 **미 군사압박 완화·항만 봉쇄 해제 등 전제** 하에 **7일 내 호르무즈 재개방** 의지를 중재국 통해 전달했다는 보도. 유가 $90대 급락·KRX 애프터 급락 후 반등(X 서술).

## 1차 확인 (이번 세션)

| 소스 | 등급 | URL | 결과 |
|---|---|---|---|
| **Kyodo News (English)** | **① 통신 원문** | https://english.kyodonews.net/articles/-/85911 | **확인** — 고위 이란 당국자→Kyodo: US가 압박 완화 초기조치를 취하면 7일 내 재개방·협상 복귀. UNGA 중재 활용. Pezeshkian–Trump 회동은 배제. |
| Reuters | ② | https://www.reuters.com/world/middle-east/iran-ready-reopen-strait-hormuz-if-us-eases-military-pressure-lifts-blockade-2026-09-22/ | 동일 방향(고위 당국자→Reuters) |
| X blazingbees | ②→교차 | 위 status | Kyodo 인용으로 시작 → 원문 대조 완료 |

**초안 grade_hint ②(보도 미대조) → Kyodo ① 대조 후 클레임 자체는 ① 가능.**  
다만 **실행(실제 통행 재개)은 미발생** — 조건부 제안일 뿐.

## open · portfolio 연결

- **open `oil-judgment`:** 휴전/재개 시 기준선 세계은행 $86/2026·$70/2027 → **−20~35%**. Citi(③) 재개 4Q26(직선 아님). 이번 제안은 breaks_if 후보 재료.
- **regime `n-hormuz` breaks_if:** 휴전·회담 재개 · 사우디 동서 파이프라인 복구(10월 말).
- **portfolio:**
  - `scenarios.hormuz_open` — trigger: 휴전·회담 재개 또는 사우디 파이프 복구 → book: 유가↓→금리↓→AI 반등.
  - `precommits`: 「호르무즈 회담 재개 또는 TTF <$15」→ VG 추가 회차 중단 · 「사우디 동서 파이프라인 복구」→ hormuz_open과 동일(VG 추가 중단·FANG 감액 확인까지 유지).
  - `energy/oil_hedge_vehicles.html` T3: 출구 = regime breaks_if. 헤지 대가(휴전 창 USO·VG −21%대) 재확인 자리.

## lead 권고

1. Kyodo ①을 oil-judgment / n-hormuz 관측 한 줄로 붙일지 결정(테제 문장 변경 X).
2. **실제 통행량·Dated–선물 괴리**가 줄는지가 판정 — 제안만으로 hedge k 축소 금지.
3. 9/22–23 UNGA 걸프·이란 회동 결과를 다음 관측 창으로.

## still open

- [ ] US 측 공식 반응 / 봉쇄 완화 여부
- [ ] 해협 통행량(mb/d) 실측 갱신
- [ ] WTI/Brent vs Dated 괴리 추적
