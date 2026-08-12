"""통계 리포트 생성 — L1/L2/L3 루프 지표 산출."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, TYPE_CHECKING

import yaml

from .models import Graph

if TYPE_CHECKING:
    from .ingest import IngestResult


# ── L1: 추출 품질 리포트 ────────────────────────────────────

def pass_rate_report(results: List["IngestResult"]) -> str:
    """L1 루프용: 파일별·전체 Pass 2 통과율 + 폐기 원인 분류."""
    lines = ["## L1 추출 품질 리포트\n"]

    total_raw = 0
    total_passed = 0
    category_counts: Dict[str, int] = {}

    lines.append("| 파일 | 체인 | 원본 | 통과 | 통과율 | 폐기 |")
    lines.append("|------|------|------|------|--------|------|")

    for r in results:
        if r.error:
            lines.append(f"| {r.filename} | {r.chain} | ERROR | — | — | {r.error} |")
            continue

        total_raw += r.total_raw
        total_passed += r.total_passed
        rate = f"{r.pass_rate * 100:.0f}%"
        discarded_count = len(r.discarded)
        lines.append(
            f"| {r.filename} | {r.chain} | {r.total_raw} | "
            f"{r.total_passed} | {rate} | {discarded_count} |"
        )

        for d in r.discarded:
            cat = d.get("category", "기타")
            category_counts[cat] = category_counts.get(cat, 0) + 1

    overall_rate = (total_passed / total_raw * 100) if total_raw > 0 else 0
    lines.append(f"\n**전체 통과율: {overall_rate:.1f}%** ({total_passed}/{total_raw})")

    if category_counts:
        lines.append("\n### 폐기 원인 분포\n")
        lines.append("| 원인 | 건수 |")
        lines.append("|------|------|")
        for cat, cnt in sorted(category_counts.items(), key=lambda x: -x[1]):
            lines.append(f"| {cat} | {cnt} |")

    # L1 종료 조건 판정
    all_file_rates = [r.pass_rate for r in results if not r.error]
    min_file_rate = min(all_file_rates) if all_file_rates else 0
    gate_pass = overall_rate >= 85 and min_file_rate >= 0.70
    lines.append(f"\n### L1 Gate 판정: {'PASS' if gate_pass else 'FAIL'}")
    lines.append(f"- 전체 ≥ 85%: {'OK' if overall_rate >= 85 else 'FAIL'} ({overall_rate:.1f}%)")
    lines.append(f"- 최저 파일 ≥ 70%: {'OK' if min_file_rate >= 0.70 else 'FAIL'} ({min_file_rate * 100:.0f}%)")

    return "\n".join(lines)


# ── 그래프 통계 리포트 ──────────────────────────────────────

def graph_stats(graph: Graph) -> str:
    """체인별 그래프 통계 요약."""
    lines = [f"## 그래프 통계: {graph.meta.chain}\n"]

    lines.append(f"- Function 노드: {len(graph.functions)}")
    lines.append(f"- Company 노드: {len(graph.companies)}")
    lines.append(f"- Edge 수: {len(graph.edges)}")
    lines.append(f"- 소스 파일: {len(graph.meta.source_files)}")

    # confidence 분포
    if graph.edges:
        confidences = [e.confidence for e in graph.edges]
        high = sum(1 for c in confidences if c >= 0.8)
        medium = sum(1 for c in confidences if 0.5 <= c < 0.8)
        low = sum(1 for c in confidences if c < 0.5)
        lines.append(f"\n### Confidence 분포 (Edge)")
        lines.append(f"- High (≥0.8): {high} ({high/len(confidences)*100:.0f}%)")
        lines.append(f"- Medium (0.5~0.8): {medium} ({medium/len(confidences)*100:.0f}%)")
        lines.append(f"- Low (<0.5): {low} ({low/len(confidences)*100:.0f}%)")

    # evidence 커버리지
    if graph.edges:
        with_evidence = sum(1 for e in graph.edges if e.evidence)
        lines.append(
            f"\n### Evidence 커버리지"
            f"\n- evidence 있는 엣지: {with_evidence}/{len(graph.edges)}"
            f" ({with_evidence/len(graph.edges)*100:.0f}%)"
        )

    # company 기능 매핑 현황
    no_fn = [c for c in graph.companies if not c.functions]
    if no_fn:
        lines.append(f"\n### 기능 미매핑 기업 ({len(no_fn)}개)")
        for c in no_fn:
            lines.append(f"- {c.id} ({c.name})")

    return "\n".join(lines)


# ── L2: 커버리지 갭 리포트 ──────────────────────────────────

def coverage_report(
    chain_graphs: Dict[str, Graph],
    ground_truth_path: Optional[str] = None,
) -> str:
    """L2 루프용: ground_truth 노드의 그래프 포함 여부 확인."""
    if ground_truth_path is None:
        ground_truth_path = str(
            Path(__file__).resolve().parent.parent.parent
            / "data"
            / "ground_truth.yaml"
        )

    gt_path = Path(ground_truth_path)
    if not gt_path.exists():
        return "ground_truth.yaml 파일을 찾을 수 없습니다."

    gt_data = yaml.safe_load(gt_path.read_text(encoding="utf-8"))
    if not gt_data:
        return "ground_truth.yaml가 비어 있습니다."

    lines = ["## L2 커버리지 갭 리포트\n"]
    lines.append("| # | ID | 이름 | 체인 | 그래프 포함 | 비고 |")
    lines.append("|---|-----|------|------|------------|------|")

    # 그래프의 모든 노드 ID 수집 (function + company)
    all_fn_ids: set = set()
    all_co_ids: set = set()
    all_fn_names: Dict[str, str] = {}
    all_co_names: Dict[str, str] = {}

    for g in chain_graphs.values():
        for fn in g.functions:
            nid = fn.id.lower().replace("-", "_")
            all_fn_ids.add(nid)
            all_fn_names[nid] = fn.name
        for co in g.companies:
            nid = co.id.lower().replace("-", "_")
            all_co_ids.add(nid)
            all_co_names[nid] = co.name

    covered = 0
    total = len(gt_data)

    for i, node in enumerate(gt_data, 1):
        gt_id = node["id"].lower().replace("-", "_")
        gt_name = node["name"]
        gt_chain = node["chain"]
        is_fn = gt_id.startswith("fn_")

        # ID 매칭
        found = gt_id in (all_fn_ids if is_fn else all_co_ids)

        # 이름 유사도 매칭 (ID 실패 시)
        note = ""
        if not found:
            search_names = all_fn_names if is_fn else all_co_names
            for nid, name in search_names.items():
                if gt_name in name or name in gt_name:
                    found = True
                    note = f"이름 매칭: {nid}"
                    break

        if found:
            covered += 1
            status = "O"
        else:
            status = "X"
            note = "누락"

        lines.append(f"| {i} | {gt_id} | {gt_name} | {gt_chain} | {status} | {note} |")

    lines.append(f"\n**커버리지: {covered}/{total}**")

    gate_pass = covered >= 8
    lines.append(f"\n### L2 Gate 판정: {'PASS' if gate_pass else 'FAIL'}")
    lines.append(f"- 8/10 이상: {'OK' if gate_pass else 'FAIL'} ({covered}/{total})")

    return "\n".join(lines)


# ── 스코어 리포트 ──────────────────────────────────────────

def score_report(fn_scores: List[Dict], co_scores: List[Dict]) -> str:
    """스코어보드 테이블 (function + company 랭킹)."""
    lines = ["## Function 병목 스코어보드\n"]
    lines.append("| # | Function | Stage | S1 | S2 | S3 | S4 | S5 | Total | RaRR |")
    lines.append("|---|----------|-------|----|----|----|----|-----|-------|------|")

    for r in fn_scores[:20]:
        rarr = r.get("rarr", {})
        rarr_str = (
            f"{rarr['rarr_ratio']:.0%}"
            if rarr.get("total_downstream", 0) > 0 else "—"
        )
        name = r["name"][:22]
        stage = r["stage"][:12]
        lines.append(
            f"| {r['rank']} | {name} | {stage} | "
            f"{r['s1']:.1f} | {r['s2']:.1f} | {r['s3']:.1f} | "
            f"{r['s4']:.1f} | {r['s5']:.1f} | **{r['total']:.1f}** | {rarr_str} |"
        )

    lines.append(f"\n_총 {len(fn_scores)}개 function 중 상위 20개 표시_\n")

    lines.append("\n## Company 스코어보드\n")
    lines.append("| # | Company | Ticker | Score | 기여 Functions |")
    lines.append("|---|---------|--------|-------|---------------|")

    for r in co_scores[:15]:
        fns = ", ".join(
            f["fn"].replace("fn_", "")
            for f in r["contributing_fns"][:3]
        )
        ticker = r["ticker"] or "—"
        lines.append(
            f"| {r['rank']} | {r['name']} | {ticker} | "
            f"**{r['score']:.1f}** | {fns} |"
        )

    lines.append(f"\n_총 {len(co_scores)}개 company 중 상위 15개 표시_")

    return "\n".join(lines)


def calibration_report(result: Dict) -> str:
    """L4 캘리브레이션 결과 리포트."""
    lines = ["## L4 캘리브레이션 결과\n"]

    status = (
        "CONVERGED" if result["converged"]
        else f"NOT CONVERGED ({result.get('reason', 'unknown')})"
    )
    lines.append(f"**상태**: {status}")
    lines.append(f"**사이클**: {result['cycles_run']}")
    lines.append(f"**Recall@20%**: {result['recall']:.1%}")
    lines.append(f"**평균 랭크 백분위**: {result['mean_rank_pct']:.1%}")

    # 사이클별 추이
    lines.append("\n### 사이클별 추이\n")
    lines.append("| Cycle | Recall@20% | Mean Rank% | LOO Pass |")
    lines.append("|-------|-----------|------------|----------|")
    for h in result.get("history", []):
        lines.append(
            f"| {h['cycle']} | {h['recall']:.1%} | "
            f"{h['mean_rank_pct']:.1%} | {h['loo_pass_rate']:.0%} |"
        )

    # LOO 매트릭스
    lines.append("\n### LOO 교차 검증\n")
    lines.append("| GT Node | Resolved | Rank | Rank% | Pass |")
    lines.append("|---------|----------|------|-------|------|")
    for lo in result.get("loo_results", []):
        resolved = lo.get("resolved") or "—"
        rank = str(lo["rank"]) if lo["rank"] is not None else "—"
        pct = f"{lo['rank_pct']:.0%}"
        p = "O" if lo["pass"] else "X"
        note = lo.get("note", "")
        extra = f" {note}" if note else ""
        lines.append(f"| {lo['left_out']} | {resolved} | {rank} | {pct} | {p} |{extra}")

    # Gate 판정
    gate = result["recall"] >= 0.8 and all(
        lo["pass"] for lo in result.get("loo_results", [])
    )
    lines.append(f"\n### L4 Gate 판정: {'PASS' if gate else 'FAIL'}")
    lines.append(
        f"- Recall@20% >= 0.8: "
        f"{'OK' if result['recall'] >= 0.8 else 'FAIL'} ({result['recall']:.1%})"
    )
    loo_all = all(lo["pass"] for lo in result.get("loo_results", []))
    lines.append(f"- LOO 전원 상위 30%: {'OK' if loo_all else 'FAIL'}")

    # 최종 가중치
    lines.append("\n### 최종 가중치\n```yaml")
    for k, v in result.get("final_weights", {}).items():
        lines.append(f"  {k}: {v}")
    lines.append("```")

    return "\n".join(lines)


# ── L3: 그래프 무결성 리포트 ─────────────────────────────────

def integrity_report(graph: Graph) -> str:
    """L3 루프용: 그래프 구조 무결성 검사."""
    lines = [f"## L3 무결성 리포트: {graph.meta.chain}\n"]

    issues = []

    # 1. 고립 기업 노드 (엣지 0개)
    edge_nodes = set()
    for e in graph.edges:
        edge_nodes.add(e.source)
        edge_nodes.add(e.target)

    orphan_companies = [
        c for c in graph.companies if c.id not in edge_nodes
    ]
    if orphan_companies:
        issues.append(f"고립 기업 {len(orphan_companies)}개")
        lines.append(f"### 1. 고립 기업 노드 ({len(orphan_companies)}개)")
        for c in orphan_companies:
            lines.append(f"- {c.id} ({c.name})")
    else:
        lines.append("### 1. 고립 기업 노드: 없음")

    # 2. 기능 미매핑 기업
    no_fn = [c for c in graph.companies if not c.functions]
    if no_fn:
        issues.append(f"기능 미매핑 {len(no_fn)}개")
        lines.append(f"\n### 2. 기능 미매핑 기업 ({len(no_fn)}개)")
        for c in no_fn:
            lines.append(f"- {c.id} ({c.name})")
    else:
        lines.append("\n### 2. 기능 미매핑 기업: 없음")

    # 3. 댕글링 참조 (엣지가 존재하지 않는 노드 참조)
    all_node_ids = {c.id for c in graph.companies} | {f.id for f in graph.functions}
    dangling = []
    for e in graph.edges:
        if e.source not in all_node_ids:
            dangling.append(f"edge.from={e.source}")
        if e.target not in all_node_ids:
            dangling.append(f"edge.to={e.target}")

    if dangling:
        issues.append(f"댕글링 참조 {len(dangling)}개")
        lines.append(f"\n### 3. 댕글링 참조 ({len(dangling)}개)")
        for d in dangling:
            lines.append(f"- {d}")
    else:
        lines.append("\n### 3. 댕글링 참조: 없음")

    # 4. 중복 매핑
    dup_count = 0
    for co in graph.companies:
        fn_ids = [cf.fn for cf in co.functions]
        dups = len(fn_ids) - len(set(fn_ids))
        if dups > 0:
            dup_count += dups
            lines.append(f"\n- 중복 매핑: {co.id} — {[f for f in fn_ids if fn_ids.count(f) > 1]}")

    if dup_count:
        issues.append(f"중복 매핑 {dup_count}개")

    # Gate 판정
    critical_issues = len(orphan_companies) + len(dangling)
    gate_pass = critical_issues == 0
    lines.append(f"\n### L3 Gate 판정: {'PASS' if gate_pass else 'FAIL'}")
    if issues:
        lines.append(f"- 이슈: {', '.join(issues)}")
    else:
        lines.append("- 이슈 없음")

    return "\n".join(lines)
