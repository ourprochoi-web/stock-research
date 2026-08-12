# 진행 상황 기록

## Phase 0 — 스키마·저장

### Gate 0: L0 스키마 스트레스 루프 (2026-07-25)

**결과: PASS (12/12 tests)**

| 테스트 | 결과 |
|--------|------|
| 왕복 테스트 (저장 → 로드 → model_dump 일치) | PASS |
| 한글 보존 (ensure_ascii=False) | PASS |
| Edge alias 직렬화 (from/to) | PASS |
| Edge evidence 필수 (min_length=1) | PASS |
| 디렉토리 자동 생성 | PASS |
| ID 정규화 (co_SK_Hynix → co_skhynix) | PASS |
| 알려진 변형 매핑 (co_sk_hainix → co_skhynix) | PASS |
| Function 중복 제거 | PASS |
| Company 병합 (higher confidence 우선) | PASS |
| Edge evidence 병합 + max confidence | PASS |
| 다른 type은 별개 엣지 | PASS |
| 소스 파일 목록 병합 | PASS |

**구현 파일:**
- `src/models.py` — Pydantic v2 스키마 (Python 3.9 호환: Optional[] 사용)
- `src/graph_io.py` — JSON 저장/로드 + CSV 임포트
- `src/merge.py` — 그래프 병합 + ID 정규화
- `tests/test_graph_io.py` — 5 tests
- `tests/test_merge.py` — 7 tests
- `config/weights.yaml` — 스코어링 가중치 스켈레톤

**설계 결정:**
- D-009: Python 3.9 호환 (시스템 Python). `float | None` → `Optional[float]`

---

## Phase 1 — 시드 인제스트

### 구현 상태

| 파일 | 상태 | 비고 |
|------|------|------|
| src/ingest.py | 구현 완료 | LLM 2-pass 파이프라인 |
| src/report.py | 구현 완료 | 통계 리포트 생성 |
| cli.py | 구현 완료 | CLI 진입점 |

### L1 추출 품질 루프

> API 호출 필요. `ANTHROPIC_API_KEY` 설정 후 실행:
> ```bash
> cd node-screener && python3 cli.py ingest
> ```

| 사이클 | 전체 통과율 | 최저 파일 | 프롬프트 변경 | 비고 |
|--------|------------|----------|--------------|------|
| 1 | — | — | 초기 프롬프트 | 미실행 |

### L2 커버리지 갭 루프

> L1 완료 후 실행:
> ```bash
> python3 cli.py coverage-check
> ```

### L3 그래프 무결성 루프

> L2 완료 후 실행:
> ```bash
> python3 cli.py integrity-check hbm 2026-07
> python3 cli.py integrity-check ai_power 2026-07
> ```


---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 12 | 38% | 20 |
| research_ai_power_companies_kr.md | ai_power | 26 | 13 | 50% | 13 |
| research_ai_power_part12_overview.md | ai_power | 51 | 44 | 86% | 7 |
| research_ai_power_part3_investment.md | ai_power | 34 | 21 | 62% | 13 |
| research_ai_power_themes_AB.md | ai_power | 38 | 12 | 32% | 26 |
| research_ai_power_themes_CD.md | ai_power | 42 | 20 | 48% | 22 |
| research_ai_power_themes_extra.md | ai_power | 48 | 25 | 52% | 23 |
| research_gas_turbine_ai_power.md | ai_power | 48 | 48 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 57 | 36 | 63% | 21 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 27 | 60% | 18 |
| research_hbm_pkg_part12_overview.md | hbm | 66 | 54 | 82% | 12 |
| research_hbm_pkg_themes.md | hbm | 57 | 34 | 60% | 23 |
| research_smr_nuclear_ai_power.md | ai_power | 47 | 47 | 100% | 0 |

**전체 통과율: 66.5%** (393/591)

### 폐기 원인 분포

| 원인 | 건수 |
|------|------|
| 오인용 | 198 |

### L1 Gate 판정: FAIL
- 전체 ≥ 85%: FAIL (66.5%)
- 최저 파일 ≥ 70%: FAIL (32%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 59
- Edge 수: 34
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 22 (65%)
- Medium (0.5~0.8): 9 (26%)
- Low (<0.5): 3 (9%)

### Evidence 커버리지
- evidence 있는 엣지: 34/34 (100%)

## 그래프 통계: hbm

- Function 노드: 51
- Company 노드: 23
- Edge 수: 38
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 32 (84%)
- Medium (0.5~0.8): 4 (11%)
- Low (<0.5): 2 (5%)

### Evidence 커버리지
- evidence 있는 엣지: 38/38 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | X | 누락 |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | X | 누락 |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | X | 누락 |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | X | 누락 |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 6/10**

### L2 Gate 판정: FAIL
- 8/10 이상: FAIL (6/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 38 | 38 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 42 | 42 | 100% | 0 |
| research_ai_power_themes_extra.md | ai_power | 48 | 48 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 48 | 48 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 57 | 57 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 66 | 66 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 57 | 57 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 47 | 47 | 100% | 0 |

**전체 통과율: 100.0%** (591/591)

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (100.0%)
- 최저 파일 ≥ 70%: OK (100%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 79
- Edge 수: 57
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 34 (60%)
- Medium (0.5~0.8): 17 (30%)
- Low (<0.5): 6 (11%)

### Evidence 커버리지
- evidence 있는 엣지: 57/57 (100%)

## 그래프 통계: hbm

- Function 노드: 51
- Company 노드: 33
- Edge 수: 50
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 42 (84%)
- Medium (0.5~0.8): 5 (10%)
- Low (<0.5): 3 (6%)

### Evidence 커버리지
- evidence 있는 엣지: 50/50 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | X | 누락 |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | X | 누락 |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | X | 누락 |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | X | 누락 |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 6/10**

### L2 Gate 판정: FAIL
- 8/10 이상: FAIL (6/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 38 | 38 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 42 | 42 | 100% | 0 |
| research_ai_power_themes_extra.md | ai_power | 48 | 48 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 48 | 48 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 57 | 57 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 66 | 66 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 57 | 57 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 47 | 47 | 100% | 0 |

**전체 통과율: 100.0%** (591/591)

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (100.0%)
- 최저 파일 ≥ 70%: OK (100%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 79
- Edge 수: 57
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 34 (60%)
- Medium (0.5~0.8): 17 (30%)
- Low (<0.5): 6 (11%)

### Evidence 커버리지
- evidence 있는 엣지: 57/57 (100%)

## 그래프 통계: hbm

- Function 노드: 49
- Company 노드: 33
- Edge 수: 50
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 42 (84%)
- Medium (0.5~0.8): 5 (10%)
- Low (<0.5): 3 (6%)

### Evidence 커버리지
- evidence 있는 엣지: 50/50 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | O |  |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | O |  |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | O |  |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | O |  |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 10/10**

### L2 Gate 판정: PASS
- 8/10 이상: OK (10/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 38 | 38 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 42 | 42 | 100% | 0 |
| research_ai_power_themes_extra.md | ai_power | 48 | 48 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 48 | 48 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 57 | 57 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 66 | 66 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 57 | 57 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 47 | 47 | 100% | 0 |

**전체 통과율: 100.0%** (591/591)

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (100.0%)
- 최저 파일 ≥ 70%: OK (100%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 79
- Edge 수: 57
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 34 (60%)
- Medium (0.5~0.8): 17 (30%)
- Low (<0.5): 6 (11%)

### Evidence 커버리지
- evidence 있는 엣지: 57/57 (100%)

## 그래프 통계: hbm

- Function 노드: 49
- Company 노드: 33
- Edge 수: 50
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 42 (84%)
- Medium (0.5~0.8): 5 (10%)
- Low (<0.5): 3 (6%)

### Evidence 커버리지
- evidence 있는 엣지: 50/50 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | O |  |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | O |  |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | O |  |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | O |  |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 10/10**

### L2 Gate 판정: PASS
- 8/10 이상: OK (10/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 39 | 39 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 48 | 47 | 98% | 1 |
| research_ai_power_themes_extra.md | ai_power | 58 | 58 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 56 | 56 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 62 | 62 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 70 | 70 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 61 | 61 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 48 | 48 | 100% | 0 |

**전체 통과율: 99.8%** (629/630)

### 폐기 원인 분포

| 원인 | 건수 |
|------|------|
| 오인용 | 1 |

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (99.8%)
- 최저 파일 ≥ 70%: OK (98%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 78
- Edge 수: 82
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 45 (55%)
- Medium (0.5~0.8): 31 (38%)
- Low (<0.5): 6 (7%)

### Evidence 커버리지
- evidence 있는 엣지: 82/82 (100%)

## 그래프 통계: hbm

- Function 노드: 49
- Company 노드: 33
- Edge 수: 55
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 47 (85%)
- Medium (0.5~0.8): 5 (9%)
- Low (<0.5): 3 (5%)

### Evidence 커버리지
- evidence 있는 엣지: 55/55 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | O |  |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | O |  |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | O |  |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | O |  |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 10/10**

### L2 Gate 판정: PASS
- 8/10 이상: OK (10/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 39 | 39 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 48 | 47 | 98% | 1 |
| research_ai_power_themes_extra.md | ai_power | 58 | 58 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 56 | 56 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 62 | 62 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 70 | 70 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 61 | 61 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 48 | 48 | 100% | 0 |

**전체 통과율: 99.8%** (629/630)

### 폐기 원인 분포

| 원인 | 건수 |
|------|------|
| 오인용 | 1 |

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (99.8%)
- 최저 파일 ≥ 70%: OK (98%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 78
- Edge 수: 82
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 45 (55%)
- Medium (0.5~0.8): 31 (38%)
- Low (<0.5): 6 (7%)

### Evidence 커버리지
- evidence 있는 엣지: 82/82 (100%)

## 그래프 통계: hbm

- Function 노드: 49
- Company 노드: 33
- Edge 수: 55
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 47 (85%)
- Medium (0.5~0.8): 5 (9%)
- Low (<0.5): 3 (5%)

### Evidence 커버리지
- evidence 있는 엣지: 55/55 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | O |  |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | O |  |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | O |  |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | O |  |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 10/10**

### L2 Gate 판정: PASS
- 8/10 이상: OK (10/10)

---

### L1 인제스트 결과 (자동 기록)

## L1 추출 품질 리포트

| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |
|------|------|------|------|--------|------|
| research_ai_power_companies_global.md | ai_power | 32 | 32 | 100% | 0 |
| research_ai_power_companies_kr.md | ai_power | 26 | 26 | 100% | 0 |
| research_ai_power_part12_overview.md | ai_power | 51 | 51 | 100% | 0 |
| research_ai_power_part3_investment.md | ai_power | 34 | 34 | 100% | 0 |
| research_ai_power_themes_AB.md | ai_power | 39 | 39 | 100% | 0 |
| research_ai_power_themes_CD.md | ai_power | 47 | 47 | 100% | 0 |
| research_ai_power_themes_extra.md | ai_power | 57 | 57 | 100% | 0 |
| research_gas_turbine_ai_power.md | ai_power | 56 | 56 | 100% | 0 |
| research_hbm_pkg_companies_global.md | hbm | 62 | 62 | 100% | 0 |
| research_hbm_pkg_companies_kr.md | hbm | 45 | 45 | 100% | 0 |
| research_hbm_pkg_part12_overview.md | hbm | 67 | 67 | 100% | 0 |
| research_hbm_pkg_themes.md | hbm | 61 | 61 | 100% | 0 |
| research_smr_nuclear_ai_power.md | ai_power | 48 | 48 | 100% | 0 |

**전체 통과율: 100.0%** (625/625)

### L1 Gate 판정: PASS
- 전체 ≥ 85%: OK (100.0%)
- 최저 파일 ≥ 70%: OK (100%)

## 그래프 통계: ai_power

- Function 노드: 62
- Company 노드: 76
- Edge 수: 83
- 소스 파일: 9

### Confidence 분포 (Edge)
- High (≥0.8): 46 (55%)
- Medium (0.5~0.8): 31 (37%)
- Low (<0.5): 6 (7%)

### Evidence 커버리지
- evidence 있는 엣지: 83/83 (100%)

## 그래프 통계: hbm

- Function 노드: 49
- Company 노드: 30
- Edge 수: 55
- 소스 파일: 4

### Confidence 분포 (Edge)
- High (≥0.8): 47 (85%)
- Medium (0.5~0.8): 5 (9%)
- Low (<0.5): 3 (5%)

### Evidence 커버리지
- evidence 있는 엣지: 55/55 (100%)

## L2 커버리지 갭 리포트

| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |
|---|-----|------|------|------------|------|
| 1 | fn_cowos_packaging | CoWoS 첨단 패키징 | hbm | O |  |
| 2 | fn_tc_bonding | TC 본딩 (열압착 본딩) | hbm | O |  |
| 3 | fn_hydrogen_annealing | 고압수소어닐링 | hbm | O |  |
| 4 | fn_abf_substrate_film | ABF 필름 (기판 소재) | hbm | O |  |
| 5 | fn_ate_test | ATE (자동테스트장비) | hbm | O | 이름 매칭: fn_test_ate |
| 6 | fn_dicing_grinding | 웨이퍼 다이싱/그라인딩 | hbm | O |  |
| 7 | fn_pogo_pin_socket | 포고핀 테스트 소켓 | hbm | O |  |
| 8 | fn_power_transformer | 초고압 변압기 | ai_power | O | 이름 매칭: fn_ehv_transformer |
| 9 | fn_gas_turbine | 대형 가스터빈 (CCGT) | ai_power | O |  |
| 10 | fn_grid_interconnection | 계통연계 (Grid Interconnection) | ai_power | O |  |

**커버리지: 10/10**

### L2 Gate 판정: PASS
- 8/10 이상: OK (10/10)

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 14.3%
**평균 랭크 백분위**: 54.2%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 14.3% | 54.2% | 14% |
| 2 | 14.3% | 54.2% | 14% |
| 3 | 14.3% | 54.2% | 14% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 1 | 2% | O |
| fn_tc_bonding | fn_tc_bonding | 45 | 92% | X |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 25 | 51% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 44 | 90% | X |
| fn_ate_test | fn_test_ate | 26 | 53% | X |
| fn_dicing_grinding | fn_dicing_grinding | 30 | 61% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 15 | 31% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (14.3%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 24.2
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 28.6%
**평균 랭크 백분위**: 39.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 28.6% | 39.1% | 29% |
| 2 | 28.6% | 39.1% | 29% |
| 3 | 28.6% | 39.1% | 29% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 19 | 39% | X |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 26 | 53% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 6 | 12% | O |
| fn_ate_test | fn_test_ate | 22 | 45% | X |
| fn_dicing_grinding | fn_dicing_grinding | 25 | 51% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 34 | 69% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (28.6%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 24.2
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 30.0%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 30.0% | 43% |
| 2 | 42.9% | 30.0% | 43% |
| 3 | 42.9% | 30.0% | 43% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 1 | 2% | O |
| fn_tc_bonding | fn_tc_bonding | 9 | 18% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 17 | 35% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 5 | 10% | O |
| fn_ate_test | fn_test_ate | 18 | 37% | X |
| fn_dicing_grinding | fn_dicing_grinding | 21 | 43% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 32 | 65% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 24.2
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 27.4%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 27.4% | 57% |
| 2 | 42.9% | 27.4% | 57% |
| 3 | 42.9% | 27.4% | 57% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 8 | 16% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 22 | 45% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 14 | 29% | O |
| fn_dicing_grinding | fn_dicing_grinding | 20 | 41% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 27 | 55% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 24.2
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 25.9%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 25.9% | 57% |
| 2 | 42.9% | 25.9% | 57% |
| 3 | 42.9% | 25.9% | 57% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 8 | 16% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 24 | 49% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 14 | 29% | O |
| fn_dicing_grinding | fn_dicing_grinding | 23 | 47% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 17 | 35% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 24.2
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 23.9%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 23.9% | 71% |
| 2 | 42.9% | 23.9% | 71% |
| 3 | 42.9% | 23.9% | 71% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 9 | 18% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 24 | 49% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 10 | 20% | O |
| fn_dicing_grinding | fn_dicing_grinding | 23 | 47% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 13 | 26% | O |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 20
  s4_demand: 18.2
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 19.0%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 19.0% | 71% |
| 2 | 42.9% | 19.0% | 71% |
| 3 | 42.9% | 19.0% | 71% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 18 | 37% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 10 | 20% | O |
| fn_dicing_grinding | fn_dicing_grinding | 12 | 24% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 15 | 31% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 3
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 16.9%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 16.9% | 86% |
| 2 | 42.9% | 16.9% | 86% |
| 3 | 42.9% | 16.9% | 86% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 18 | 37% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 10 | 20% | O |
| fn_dicing_grinding | fn_dicing_grinding | 10 | 20% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 10 | 20% | O |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (max_cycles)
**사이클**: 10
**Recall@20%**: 28.6%
**평균 랭크 백분위**: 27.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 16.9% | 86% |
| 2 | 42.9% | 18.4% | 86% |
| 3 | 42.9% | 21.9% | 86% |
| 4 | 28.6% | 23.3% | 86% |
| 5 | 28.6% | 26.5% | 43% |
| 6 | 28.6% | 26.5% | 43% |
| 7 | 28.6% | 23.0% | 86% |
| 8 | 28.6% | 23.9% | 43% |
| 9 | 28.6% | 23.9% | 43% |
| 10 | 28.6% | 23.6% | 86% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 1 | 2% | O |
| fn_tc_bonding | fn_tc_bonding | 12 | 24% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 24 | 49% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 5 | 10% | O |
| fn_ate_test | fn_test_ate | 17 | 35% | X |
| fn_dicing_grinding | fn_dicing_grinding | 17 | 35% | X |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 17 | 35% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (28.6%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 59.6
  s2_barrier: 30.0
  s3_economics: 10.2
  s4_demand: 6.8
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 1
**Recall@20%**: 42.9%
**평균 랭크 백분위**: 16.9%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 42.9% | 16.9% | 86% |
| 2 | 42.9% | 18.4% | 86% |
| 3 | 42.9% | 21.9% | 86% |
| 4 | 28.6% | 23.3% | 86% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 18 | 37% | X |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 10 | 20% | O |
| fn_dicing_grinding | fn_dicing_grinding | 10 | 20% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 10 | 20% | O |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (42.9%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 1
**Recall@20%**: 57.1%
**평균 랭크 백분위**: 14.9%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 57.1% | 14.9% | 100% |
| 2 | 57.1% | 14.9% | 100% |
| 3 | 57.1% | 14.9% | 100% |
| 4 | 57.1% | 14.9% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 11 | 22% | O |
| fn_dicing_grinding | fn_dicing_grinding | 11 | 22% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 11 | 22% | O |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (57.1%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 25
  s2_barrier: 25
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 2
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 13.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 57.1% | 14.9% | 100% |
| 2 | 100.0% | 13.1% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 9 | 18% | O |
| fn_dicing_grinding | fn_dicing_grinding | 9 | 18% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 9 | 18% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (ai_power, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 1
**Recall@20%**: 66.7%
**평균 랭크 백분위**: 25.3%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 66.7% | 25.3% | 67% |
| 2 | 33.3% | 23.7% | 67% |
| 3 | 33.3% | 25.3% | 67% |
| 4 | 33.3% | 23.1% | 67% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_power_transformer | fn_ehv_transformer | 10 | 16% | O |
| fn_gas_turbine | fn_gas_turbine | 12 | 19% | O |
| fn_grid_interconnection | fn_grid_interconnection | 25 | 40% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (66.7%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 13.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 13.1% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 9 | 18% | O |
| fn_dicing_grinding | fn_dicing_grinding | 9 | 18% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 9 | 18% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (ai_power, 자동 기록)

## L4 캘리브레이션 결과

**상태**: NOT CONVERGED (stagnation)
**사이클**: 1
**Recall@20%**: 66.7%
**평균 랭크 백분위**: 25.3%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 66.7% | 25.3% | 67% |
| 2 | 33.3% | 23.7% | 67% |
| 3 | 33.3% | 25.3% | 67% |
| 4 | 33.3% | 23.1% | 67% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_power_transformer | fn_ehv_transformer | 10 | 16% | O |
| fn_gas_turbine | fn_gas_turbine | 12 | 19% | O |
| fn_grid_interconnection | fn_grid_interconnection | 25 | 40% | X |

### L4 Gate 판정: FAIL
- Recall@20% >= 0.8: FAIL (66.7%)
- LOO 전원 상위 30%: FAIL

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (ai_power, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 14.0%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 14.0% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_power_transformer | fn_ehv_transformer | 10 | 16% | O |
| fn_gas_turbine | fn_gas_turbine | 12 | 19% | O |
| fn_grid_interconnection | fn_grid_interconnection | 4 | 6% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 13.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 13.1% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 9 | 18% | O |
| fn_dicing_grinding | fn_dicing_grinding | 9 | 18% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 9 | 18% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (ai_power, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 14.0%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 14.0% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_power_transformer | fn_ehv_transformer | 10 | 16% | O |
| fn_gas_turbine | fn_gas_turbine | 12 | 19% | O |
| fn_grid_interconnection | fn_grid_interconnection | 4 | 6% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 13.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 13.1% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 9 | 18% | O |
| fn_dicing_grinding | fn_dicing_grinding | 9 | 18% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 9 | 18% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```

---

### L4 캘리브레이션 결과 (hbm, 자동 기록)

## L4 캘리브레이션 결과

**상태**: CONVERGED
**사이클**: 1
**Recall@20%**: 100.0%
**평균 랭크 백분위**: 13.1%

### 사이클별 추이

| Cycle | Recall@20% | Mean Rank% | LOO Pass |
|-------|-----------|------------|----------|
| 1 | 100.0% | 13.1% | 100% |

### LOO 교차 검증

| GT Node | Resolved | Rank | Rank% | Pass |
|---------|----------|------|-------|------|
| fn_cowos_packaging | fn_cowos_packaging | 2 | 4% | O |
| fn_tc_bonding | fn_tc_bonding | 7 | 14% | O |
| fn_hydrogen_annealing | fn_hydrogen_annealing | 8 | 16% | O |
| fn_abf_substrate_film | fn_abf_substrate_film | 1 | 2% | O |
| fn_ate_test | fn_test_ate | 9 | 18% | O |
| fn_dicing_grinding | fn_dicing_grinding | 9 | 18% | O |
| fn_pogo_pin_socket | fn_pogo_pin_socket | 9 | 18% | O |

### L4 Gate 판정: PASS
- Recall@20% >= 0.8: OK (100.0%)
- LOO 전원 상위 30%: OK

### 최종 가중치
```yaml
  s1_structure: 20.0
  s2_barrier: 30.0
  s3_economics: 20
  s4_demand: 15
  s5_penalty: -25
```