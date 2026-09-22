# routing draft — r-20260922-x (미커밋 · brain/routing.jsonl 에 붙이기 전 초안)

```json
{"id": "r-20260922-x", "date": "2026-09-22", "intake": ["u-20260922-x05"], "source": "X @Liberty0918 GS 버추얼미팅 요약(엄브렐라/Jay씨 경유) · https://x.com/Liberty0918/status/2102388706871296325", "grade": "③", "claim": "GS SK하이닉스 버추얼(09-22): 2026 잔여 QoQ 가격↑(속도 둔화 가능) · HBM4 비중↑로 하반기 ASP·마진↑ · 2027 HBM ASP↑ · M15X 신규캐파 주로 HBM · 용인 2027-02 오픈·양산은 2027말 · 서버메모리(HBM포함)≈DRAM매출 60% → LTA ≥50% 가능 · 환노출(매출$100%/비용외화<50%) · 추가 환원은 3Q 실적 때", "routed": ["hbm-packaging/hbm_pkg_company_sk_hynix.html#T1", "hbm-packaging/hbm_pkg_company_sk_hynix.html#T4", "hbm-packaging/hbm_pkg_theme_memory_cycle.html#T1", "hbm-packaging/hbm_pkg_theme_memory_cycle.html#T2"], "verdict": "ⓐ 관측(③ IB 채널체크) — JPM(09-22) 「2027 HBM 혼합 ASP YoY +64%·협상 마무리」와 같은 방향. 회사 공시 아님", "action": "lead: SKH T1/T4·memory_cycle T1/T2 basis에 ③ 한 줄 후보로만 붙일지 판단. 테제 문장·반증선 변경 금지. 판정 창은 3Q26 실적·10월말 컨콜 유지. intake u-20260922-x05 → user.jsonl 병합 후 routing.jsonl에 본 라인 append"}
```

## 라우팅 키 (brain/theses.json · docs/thesis_index.md)

| page key | 관련 테제 |
|---|---|
| `hbm-packaging/hbm_pkg_company_sk_hynix.html` | T1(주가·실적/자본배분) · T4(Scale-Out·ASP 희석) |
| `hbm-packaging/hbm_pkg_theme_memory_cycle.html` | T1(LTA·상방 포기) · T2(공급부족 정점 연도) |

## claim 요약 (원 스레드)

1. 2026 잔여 QoQ 가격 상승 지속·속도 둔화 가능(타이트·HBM 믹스·2Q 기저)
2. 연말 HBM4 비중↑ → 하반기 ASP·마진↑
3. 2027 컨벤셔널+HBM 타이트·프리미엄 비중↑ → HBM ASP↑
4. 클린룸 제약 → 기술 마이그레이션·M15X는 HBM 중심 · 용인 오픈 2027-02 / 양산 2027말
5. LTA 긍정·서버메모리≈60% → ≥50% 커버 가능
6. 환율: 매출 거의 100% USD
7. 추가 환원은 3Q26 실적 발표 때

## lead 액션

- [ ] `user_append_draft.jsonl` → `intake/user.jsonl` 병합(id 충돌 없음: u-20260922-x05)
- [ ] 위 JSON 한 줄을 `brain/routing.jsonl`에 append (테제 본문 비파괴)
- [ ] JPM +64% 기준선과 나란히 두되 문턱 이동 금지
