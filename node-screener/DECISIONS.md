# 설계 결정 로그

| # | 결정 | 근거 |
|---|------|------|
| D-001 | Pydantic v2 사용 | alias(`from`/`to` 예약어 처리), 유효성 검증, JSON 직렬화 내장 |
| D-002 | Pass 2는 LLM 아닌 문자열 대조 | 스펙 "문자열 대조" 준수, 결정론적 재현, API 비용 0 |
| D-003 | Sonnet 4 사용 (Pass 1) | 구조화 추출에 충분, 13회 호출에 Opus 불필요 (5x 비용 절감) |
| D-004 | 파일별 개별 처리 | 추적성·디버깅 용이, 컨텍스트 윈도우 압박 없음 |
| D-005 | 동기 API 호출 | 13파일 순차 처리 ~2분, 비동기 복잡도 불필요 |
| D-006 | 홈페이지 배포 (GitHub Pages) | 기존 리서치 리포트와 동일 방식. Phase 3에서 정적 HTML + Cytoscape.js |
| D-007 | difflib.SequenceMatcher (threshold 0.8) | Pass 2 퍼지 매칭에 표준 라이브러리 사용, 외부 의존성 없음 |
| D-008 | ID 정규화: lowercase + underscore | 대소문자·공백 변형 자동 통합 (co_SK_Hynix → co_sk_hynix) |
