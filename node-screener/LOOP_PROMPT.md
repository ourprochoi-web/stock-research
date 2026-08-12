# Node Screener — L4 캘리브레이션 반복 개선 프롬프트

> 이 프롬프트를 Claude Code에 붙여넣으면 자동으로 모든 체인의 L4 Gate를 통과시킬 때까지 반복합니다.

---

## 프롬프트

```
node-screener 프로젝트의 L4 캘리브레이션을 모든 체인이 Gate를 통과할 때까지 반복 개선해줘.

## 프로젝트 위치
/Users/kenchoi/Desktop/research_homepage/node-screener

## 현재 상태
- HBM 체인: CONVERGED (Recall 100%, LOO 7/7)
- AI Power 체인: NOT CONVERGED (Recall 66.7%, LOO 2/3, fn_grid_interconnection 실패)

## Gate 통과 조건
1. Recall@20% >= 0.8 (ground_truth 노드의 80%+ 가 상위 20% 랭크)
2. LOO 교차 검증: 모든 GT 노드가 상위 30% 이내

## 반복 사이클 (체인별 독립 실행)

### Step 1: 현황 파악
```bash
cd /Users/kenchoi/Desktop/research_homepage/node-screener
python3 cli.py calibrate <chain> 2026-07
```
출력에서 확인:
- converged 여부
- Recall@20% 값
- LOO 결과 (어떤 GT 노드가 FAIL인지)

이미 CONVERGED인 체인은 건너뛰기.

### Step 2: 실패 GT 노드 진단
LOO FAIL인 GT 노드마다:

(a) 그래프 파일 읽기: `graph/<chain>/2026-07.json`
(b) GT 노드에 매핑된 company 식별 (ground_truth.yaml의 dominant_player 참고)
(c) 해당 company의 edge 상황 분석:
   - out-edge (고객) 수: 1개뿐이면 S5 감점이 과도
   - in-edge (공급자) 수: 0이면 S1/S3가 과소 평가
   - betweenness centrality 대비 스코어: BC는 높은데 점수 낮으면 가중치 문제
(d) 진단 분류:
   - **edge_missing**: 실제로 알려진 거래 관계가 그래프에 빠져 있음 → Step 3a
   - **weight_issue**: 엣지는 충분하나 스코어링 수식이 구조적으로 불리 → Step 3b

### Step 3a: 데이터 보강 (edge_missing인 경우)
research 소스 파일(`data/seed/`)과 ground_truth.yaml의 evidence를 참고하여:

1. 누락된 edge 추가 (graph/<chain>/2026-07.json 직접 편집)
   - source/target: 기존 company ID 사용 (co_ 프리픽스)
   - 새 company가 필요하면 companies 배열에도 추가
   - evidence: 근거 문자열 리스트 (반드시 1개 이상)
   - confidence: 근거 강도에 따라 0.3~1.0
   - substitutable: 대체 가능 여부
   - type: "supply" | "customer" | "compete" | "partner"

2. 추가할 edge 예시 패턴:
   - 유틸리티/규제기관 노드가 고객 1개뿐 → 발전사, 수요처 추가
   - 장비사가 고객 1개뿐 → 알려진 고객사 추가
   - 독점 공급사의 in-edge 0개 → upstream 소재/부품 공급사 추가

3. edge 추가 후 L3 무결성 검사:
   ```bash
   python3 cli.py integrity-check <chain> 2026-07
   ```

### Step 3b: 스코어링 수식 검토 (weight_issue인 경우)
`src/scoring.py` 내 S1~S5 함수를 분석하여:

1. 해당 GT 노드의 5축 ratio (r1~r5) 확인
2. 상위 20% 경계 노드 대비 어느 축이 열위인지 파악
3. 수식 개선 옵션:
   - 특정 축의 정규화 방식 변경
   - 새로운 그래프 특성 반영 (예: 2-hop 이웃 정보)
   - 감점 로직 완화/강화

주의: 수식 변경 시 기존 CONVERGED 체인이 깨지지 않는지 반드시 확인
```bash
python3 cli.py calibrate hbm 2026-07   # 기존 체인 회귀 테스트
```

### Step 4: 캘리브레이션 재실행
```bash
python3 cli.py calibrate <chain> 2026-07
```

결과 확인:
- CONVERGED면 다음 체인으로
- NOT CONVERGED면 Step 2로 돌아가서 남은 FAIL 노드 진단

### Step 5: 전체 Gate 확인
모든 체인이 CONVERGED인지 확인:
```bash
python3 cli.py calibrate hbm 2026-07
python3 cli.py calibrate ai_power 2026-07
```

두 체인 모두 Gate PASS면 종료.

## 핵심 참조 파일
| 파일 | 용도 |
|------|------|
| `data/ground_truth.yaml` | GT 정답지 (10 노드: HBM 7 + AI Power 3) |
| `graph/hbm/2026-07.json` | HBM 그래프 (49 fn, 30 co, 58 edges) |
| `graph/ai_power/2026-07.json` | AI Power 그래프 (62 fn, 76 co, 83 edges) |
| `src/scoring.py` | 5축 스코어링 엔진 |
| `src/calibrate.py` | L4 캘리브레이션 루프 |
| `config/weights.yaml` | 현재 가중치 + 캘리브레이션 상태 |
| `data/seed/` | 원본 리서치 소스 (edge 근거용) |

## GT ID 매핑 (ground_truth → graph)
- fn_ate_test → fn_test_ate
- fn_power_transformer → fn_ehv_transformer
- 나머지는 동일 ID

## 현재 알려진 이슈
### AI Power: fn_grid_interconnection (계통연계)
- dominant_player: 유틸리티/규제기관 → graph에서 co_kepco
- KEPCO가 out-edge 1개뿐 → S5 감점 -15점 (0.6 * -25)
- S3/S4도 낮음 (고객/공급자 연결 부족)
- 해결 방향: KEPCO의 실제 고객 (발전소, 데이터센터, 산업시설) edge 추가

## 종료 조건
- 모든 체인 L4 Gate PASS (Recall >= 0.8 AND LOO 전원 상위 30%)
- 또는 3회 연속 개선 불가 시: 잔여 이슈 요약 보고 후 종료

## 주의사항
- 수식 변경 시 반드시 모든 체인 회귀 테스트
- edge 추가 시 evidence 필수 (빈 리스트 불가, pydantic ValidationError)
- edge의 evidence는 list[str] 타입 (문자열 아님)
- 가중치 변경 후 weights.yaml이 자동 갱신됨
- PROGRESS.md에 결과가 자동 append됨 (수동 편집 불필요)
```
