"""LLM 2-pass 추출 파이프라인.

Pass 1: 파일별 LLM 호출 → 트리플 JSON 추출
Pass 2: 인용구 문자열 대조 (difflib, LLM 호출 없음)
"""

from __future__ import annotations

import difflib
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from dotenv import load_dotenv

from .merge import merge_graphs, normalize_id
from .models import (
    CompanyFunction,
    CompanyNode,
    Edge,
    FunctionNode,
    Graph,
    GraphMeta,
)

load_dotenv()

# ── 체인 매핑 ──────────────────────────────────────────────

CHAIN_MAP: Dict[str, str] = {
    "research_hbm_pkg": "hbm",
    "research_ai_power": "ai_power",
    "research_gas_turbine": "ai_power",
    "research_smr_nuclear": "ai_power",
}


def detect_chain(filename: str) -> str:
    """파일명에서 체인 추론."""
    for prefix, chain in CHAIN_MAP.items():
        if filename.startswith(prefix):
            return chain
    return "unknown"


# ── Pass 2: 인용구 검증 ───────────────────────────────────

FUZZY_THRESHOLD = 0.8


@dataclass
class VerifyResult:
    """인용구 검증 결과."""

    passed: int = 0
    failed: int = 0
    discarded: List[Dict[str, Any]] = field(default_factory=list)


def _normalize_ws(text: str) -> str:
    """공백·줄바꿈 정규화 (비교용)."""
    return re.sub(r"\s+", " ", text).strip()


def verify_evidence(quote: str, source_text: str) -> bool:
    """인용구가 원문에 존재하는지 확인.

    1차: 정확 부분 문자열 매칭 (공백 정규화 후)
    2차: 퍼지 매칭 (SequenceMatcher, threshold 0.8)
    """
    norm_quote = _normalize_ws(quote)
    norm_source = _normalize_ws(source_text)

    # 너무 짧은 인용은 의미 없음 — 통과 처리
    if len(norm_quote) < 5:
        return True

    # 1차: 정확 부분 문자열
    if norm_quote in norm_source:
        return True

    # 2차: 퍼지 매칭 — 인용구 길이 기준 윈도우 슬라이딩
    quote_len = len(norm_quote)
    best_ratio = 0.0

    # 소스가 너무 길면 청크 단위로 비교
    step = max(1, quote_len // 2)
    for i in range(0, len(norm_source) - quote_len + 1, step):
        window = norm_source[i : i + quote_len + 20]  # 약간 여유
        ratio = difflib.SequenceMatcher(None, norm_quote, window).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
        if best_ratio >= FUZZY_THRESHOLD:
            return True

    return best_ratio >= FUZZY_THRESHOLD


def verify_triple(
    triple_type: str,
    triple: Dict[str, Any],
    source_text: str,
) -> Tuple[bool, Optional[str]]:
    """트리플(function/company/edge)의 evidence 전체 검증.

    Returns: (통과 여부, 실패 사유)
    """
    evidence_list: List[str] = []

    if triple_type == "function":
        return True, None  # function은 evidence 없을 수 있음

    if triple_type == "company":
        for fn_map in triple.get("functions", []):
            evidence_list.extend(fn_map.get("evidence", []))
    elif triple_type == "edge":
        evidence_list = triple.get("evidence", [])

    if not evidence_list:
        return False, "evidence 비어 있음"

    for ev in evidence_list:
        if not verify_evidence(ev, source_text):
            return False, f"인용구 불일치: '{ev[:50]}...'"

    return True, None


# ── Pass 1: LLM 추출 ──────────────────────────────────────

EXTRACTION_PROMPT = """당신은 밸류체인 분석 전문가입니다. 아래 문서에서 밸류체인 그래프 데이터를 추출해주세요.

## 규칙 (엄격히 준수)
1. **문서에 명시적으로 기술된 정보만** 추출. 추론·해석·외부 지식 사용 금지.
2. 모든 company의 functions 매핑과 모든 edge에 **원문 인용구(10~80자)**를 evidence로 포함. 인용구는 문서에서 그대로 복사.
3. confidence 자기평가: 0.0~1.0 (1.0=문서에 명확히 기술, 0.5=간접 언급, 0.3=약한 암시)
4. edge type은 반드시 "supply", "tech_dependency", "qualification" 중 하나.
5. id 형식: function은 fn_소문자영어 (예: fn_tc_bonding), company는 co_소문자영어 (예: co_skhynix)
6. 한 문서에서 추출 가능한 모든 노드와 관계를 빠짐없이 추출.
7. 시장 점유율(M/S, share)이 언급되면 반드시 share 필드에 소수점으로 기록 (예: 71.2% → 0.712)

## 출력 형식 (JSON만 출력, 다른 텍스트 없이)
```json
{
  "functions": [
    {"id": "fn_xxx", "name": "기능명", "chain": "hbm 또는 ai_power", "stage": "단계명"}
  ],
  "companies": [
    {
      "id": "co_xxx", "name": "기업명", "ticker": "종목코드 또는 null",
      "functions": [
        {"fn": "fn_xxx", "share": 0.7, "evidence": ["원문 인용구"], "confidence": 0.9}
      ]
    }
  ],
  "edges": [
    {
      "from": "co_xxx", "to": "co_yyy", "type": "supply",
      "share": 0.35, "evidence": ["원문 인용구"], "confidence": 0.8,
      "asof": "2026-06", "substitutable": false, "note": "비고"
    }
  ]
}
```

## 문서 내용:
"""


def extract_from_file(
    filepath: Path,
    model: str = "claude-sonnet-4-6",
) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    """단일 파일에서 LLM 추출 (Pass 1).

    Returns: (추출 결과 dict, 에러 메시지)
    """
    try:
        import anthropic
    except ImportError:
        return None, "anthropic 패키지 미설치. pip3 install anthropic"

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None, "ANTHROPIC_API_KEY 환경변수 미설정"

    source_text = filepath.read_text(encoding="utf-8")
    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model=model,
            max_tokens=8192,
            messages=[
                {
                    "role": "user",
                    "content": EXTRACTION_PROMPT + source_text,
                }
            ],
        )
    except Exception as e:
        return None, f"API 호출 실패: {e}"

    response_text = message.content[0].text

    # JSON 블록 추출
    json_match = re.search(r"```json\s*(.*?)\s*```", response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
    else:
        # JSON 블록 마커 없이 바로 JSON인 경우
        json_str = response_text.strip()

    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        return None, f"JSON 파싱 실패: {e}\n응답: {response_text[:200]}"

    return data, None


# ── 파이프라인 ─────────────────────────────────────────────

@dataclass
class IngestResult:
    """인제스트 결과 (파일 단위)."""

    filename: str
    chain: str
    raw_functions: int = 0
    raw_companies: int = 0
    raw_edges: int = 0
    passed_functions: int = 0
    passed_companies: int = 0
    passed_edges: int = 0
    discarded: List[Dict[str, Any]] = field(default_factory=list)
    error: Optional[str] = None

    @property
    def total_raw(self) -> int:
        return self.raw_functions + self.raw_companies + self.raw_edges

    @property
    def total_passed(self) -> int:
        return self.passed_functions + self.passed_companies + self.passed_edges

    @property
    def pass_rate(self) -> float:
        if self.total_raw == 0:
            return 0.0
        return self.total_passed / self.total_raw


def _build_graph_from_verified(
    data: Dict[str, Any],
    source_text: str,
    filename: str,
    chain: str,
) -> Tuple[Graph, IngestResult]:
    """Pass 2: 추출 데이터를 검증하고 Graph 객체로 변환."""
    result = IngestResult(filename=filename, chain=chain)

    functions: List[FunctionNode] = []
    companies: List[CompanyNode] = []
    edges: List[Edge] = []

    # Functions
    for fn_data in data.get("functions", []):
        result.raw_functions += 1
        try:
            fn = FunctionNode(
                id=normalize_id(fn_data["id"]),
                name=fn_data["name"],
                chain=fn_data.get("chain", chain),
                stage=fn_data.get("stage", ""),
            )
            functions.append(fn)
            result.passed_functions += 1
        except Exception as e:
            result.discarded.append({
                "type": "function",
                "data": fn_data,
                "reason": f"모델 유효성 오류: {e}",
                "category": "형식오류",
            })

    # Companies
    for co_data in data.get("companies", []):
        result.raw_companies += 1
        passed, reason = verify_triple("company", co_data, source_text)
        if passed:
            try:
                fn_list = []
                fn_seen: Dict[str, int] = {}  # fn_id → index (중복 제거)
                for fn_map in co_data.get("functions", []):
                    nfn = normalize_id(fn_map["fn"])
                    cf = CompanyFunction(
                        fn=nfn,
                        share=fn_map.get("share"),
                        evidence=fn_map.get("evidence", []),
                        confidence=fn_map.get("confidence", 0.5),
                    )
                    if nfn in fn_seen:
                        # 높은 confidence 우선
                        if cf.confidence > fn_list[fn_seen[nfn]].confidence:
                            fn_list[fn_seen[nfn]] = cf
                    else:
                        fn_seen[nfn] = len(fn_list)
                        fn_list.append(cf)
                co = CompanyNode(
                    id=normalize_id(co_data["id"]),
                    name=co_data["name"],
                    ticker=co_data.get("ticker"),
                    functions=fn_list,
                )
                companies.append(co)
                result.passed_companies += 1
            except Exception as e:
                result.discarded.append({
                    "type": "company",
                    "data": co_data,
                    "reason": f"모델 유효성 오류: {e}",
                    "category": "형식오류",
                })
        else:
            result.discarded.append({
                "type": "company",
                "data": co_data,
                "reason": reason,
                "category": "오인용" if "인용구" in (reason or "") else "환각",
            })

    # Edges
    for edge_data in data.get("edges", []):
        result.raw_edges += 1
        passed, reason = verify_triple("edge", edge_data, source_text)
        if passed:
            try:
                edge = Edge(
                    source=normalize_id(edge_data["from"]),
                    target=normalize_id(edge_data["to"]),
                    type=edge_data["type"],
                    share=edge_data.get("share"),
                    evidence=edge_data.get("evidence", ["manual"]),
                    confidence=edge_data.get("confidence", 0.5),
                    asof=edge_data.get("asof"),
                    substitutable=edge_data.get("substitutable", False),
                    note=edge_data.get("note"),
                )
                edges.append(edge)
                result.passed_edges += 1
            except Exception as e:
                result.discarded.append({
                    "type": "edge",
                    "data": edge_data,
                    "reason": f"모델 유효성 오류: {e}",
                    "category": "형식오류",
                })
        else:
            result.discarded.append({
                "type": "edge",
                "data": edge_data,
                "reason": reason,
                "category": "오인용" if "인용구" in (reason or "") else "환각",
            })

    graph = Graph(
        meta=GraphMeta(
            chain=chain,
            year_month="2026-07",
            source_files=[filename],
        ),
        functions=functions,
        companies=companies,
        edges=edges,
    )

    return graph, result


def ingest_seed(
    seed_dir: Optional[str] = None,
    model: str = "claude-sonnet-4-6",
    year_month: str = "2026-07",
    offline_dir: Optional[str] = None,
) -> Tuple[Dict[str, Graph], List[IngestResult]]:
    """시드 디렉토리의 모든 MD 파일을 인제스트.

    Args:
        offline_dir: 오프라인 추출 JSON 디렉토리. 주어지면 LLM 호출 대신
                     {offline_dir}/{stem}.json 파일을 로드한다.

    Returns: (체인별 그래프 dict, 파일별 결과 리스트)
    """
    if seed_dir is None:
        seed_dir = str(
            Path(__file__).resolve().parent.parent.parent
            / "data"
            / "seed"
            / "recent"
        )

    seed_path = Path(seed_dir)
    md_files = sorted(seed_path.glob("*.md"))

    if not md_files:
        print(f"[ERROR] {seed_path}에 MD 파일 없음")
        return {}, []

    offline_path = Path(offline_dir) if offline_dir else None
    mode_label = "오프라인" if offline_path else "LLM"

    print(f"[INFO] 시드 디렉토리: {seed_path}")
    print(f"[INFO] 파일 수: {len(md_files)}")
    if offline_path:
        print(f"[INFO] 오프라인 모드: {offline_path}")
    print()

    # 체인별 베이스 그래프
    chain_graphs: Dict[str, Graph] = {}
    all_results: List[IngestResult] = []

    for i, md_file in enumerate(md_files, 1):
        filename = md_file.name
        chain = detect_chain(filename)
        source_text = md_file.read_text(encoding="utf-8")

        print(f"[{i}/{len(md_files)}] {filename} → {chain}")

        # Pass 1: 추출 (오프라인 또는 LLM)
        if offline_path:
            json_file = offline_path / f"{md_file.stem}.json"
            print(f"  Pass 1: 오프라인 로드 ({json_file.name})...", end="", flush=True)
            if not json_file.exists():
                error = f"오프라인 JSON 없음: {json_file}"
                print(f" 실패: {error}")
                result = IngestResult(filename=filename, chain=chain, error=error)
                all_results.append(result)
                continue
            try:
                data = json.loads(json_file.read_text(encoding="utf-8"))
                error = None
            except json.JSONDecodeError as e:
                data, error = None, f"JSON 파싱 실패: {e}"
        else:
            print(f"  Pass 1: LLM 추출 중...", end="", flush=True)
            data, error = extract_from_file(md_file, model=model)

        if error:
            print(f" 실패: {error}")
            result = IngestResult(filename=filename, chain=chain, error=error)
            all_results.append(result)
            continue

        print(" 완료")

        # Pass 2: 인용구 검증
        print(f"  Pass 2: 인용구 검증 중...", end="", flush=True)
        file_graph, result = _build_graph_from_verified(
            data, source_text, filename, chain
        )
        all_results.append(result)

        pass_rate_pct = result.pass_rate * 100
        print(
            f" 완료 (통과율 {pass_rate_pct:.0f}%: "
            f"fn {result.passed_functions}/{result.raw_functions}, "
            f"co {result.passed_companies}/{result.raw_companies}, "
            f"edge {result.passed_edges}/{result.raw_edges})"
        )

        if result.discarded:
            for d in result.discarded:
                print(
                    f"    [폐기] {d['type']} — {d['category']}: {d['reason']}"
                )

        # 체인별 병합
        if chain not in chain_graphs:
            chain_graphs[chain] = Graph(
                meta=GraphMeta(
                    chain=chain,
                    year_month=year_month,
                ),
            )

        merge_graphs(chain_graphs[chain], file_graph)
        print()

    return chain_graphs, all_results
