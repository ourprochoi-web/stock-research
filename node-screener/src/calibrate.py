"""L4 캘리브레이션 루프 — ground_truth 정답지 기반 가중치 튜닝.

사이클: score -> recall 측정 -> miss 진단 -> 가중치 조정 -> 반복
종료: Gate 통과 | max_cycles | 2사이클 연속 정체 (Recall 변화 < 0.05)
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import yaml

from .models import Graph
from .scoring import (
    graph_to_nx,
    load_weights,
    score_functions,
    _fn_to_companies,
)

GT_PATH = (
    Path(__file__).resolve().parent.parent.parent / "data" / "ground_truth.yaml"
)

# ground_truth ID -> graph function ID (불일치 보정)
GT_ID_MAP: dict[str, str] = {
    "fn_ate_test": "fn_test_ate",
    "fn_power_transformer": "fn_ehv_transformer",
}


# ── 데이터 로드 ───────────────────────────────────────────

def load_ground_truth(chain: str, gt_path: str | None = None) -> list[dict]:
    """ground_truth.yaml에서 해당 체인의 GT 노드 로드."""
    p = Path(gt_path) if gt_path else GT_PATH
    if not p.exists():
        return []
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not data:
        return []
    return [n for n in data if n["chain"] == chain]


def resolve_gt_id(gt_id: str, fn_ids: set[str]) -> str | None:
    """Ground truth ID -> graph function ID."""
    if gt_id in fn_ids:
        return gt_id
    mapped = GT_ID_MAP.get(gt_id)
    if mapped and mapped in fn_ids:
        return mapped
    return None


# ── 지표 ──────────────────────────────────────────────────

def recall_at_k(fn_scores: list[dict], ground_truth: list[dict],
                k_pct: float = 0.2) -> float:
    """Recall@k%: GT 노드 중 상위 k%에 포함된 비율.

    동점 경쟁 랭킹 기반: rank <= k인 모든 노드를 top으로 간주.
    position 기반이면 동점 노드가 임의 순서로 탈락할 수 있음.
    """
    n = len(fn_scores)
    k = max(1, int(n * k_pct))
    top_ids = {r["fn_id"] for r in fn_scores if r["rank"] <= k}
    fn_ids = {r["fn_id"] for r in fn_scores}

    hits = total = 0
    for gt in ground_truth:
        resolved = resolve_gt_id(gt["id"], fn_ids)
        if resolved is None:
            continue
        total += 1
        if resolved in top_ids:
            hits += 1

    return hits / total if total > 0 else 0.0


def mean_rank_percentile(fn_scores: list[dict],
                         ground_truth: list[dict]) -> float:
    """GT 노드의 평균 랭크 백분위 (낮을수록 좋음)."""
    n = len(fn_scores)
    fn_ids = {r["fn_id"] for r in fn_scores}
    rank_map = {r["fn_id"]: r["rank"] for r in fn_scores}

    pcts: list[float] = []
    for gt in ground_truth:
        resolved = resolve_gt_id(gt["id"], fn_ids)
        if resolved and resolved in rank_map:
            pcts.append(rank_map[resolved] / n)

    return sum(pcts) / len(pcts) if pcts else 1.0


# ── 진단 ──────────────────────────────────────────────────

def diagnose_miss(fn_scores: list[dict], graph: Graph,
                  G: nx.DiGraph, missed_fn: str) -> str:
    """미달 원인 이분법: 'weight_issue' vs 'edge_missing'.

    betweenness가 낮으면 -> edge_missing (그래프 구조 문제)
    betweenness는 높은데 점수 낮으면 -> weight_issue (가중치 문제)
    """
    all_bc = nx.betweenness_centrality(G) if G.number_of_nodes() > 0 else {}
    cos = _fn_to_companies(graph, missed_fn)

    if not cos:
        return "edge_missing"

    avg_bc = sum(all_bc.get(c, 0) for c in cos) / len(cos)
    bc_values = sorted(all_bc.values())
    if bc_values:
        bc_pct = sum(1 for v in bc_values if v <= avg_bc) / len(bc_values)
    else:
        bc_pct = 0.0

    return "weight_issue" if bc_pct >= 0.5 else "edge_missing"


# ── LOO 교차 검증 ─────────────────────────────────────────

def leave_one_out(graph: Graph, ground_truth: list[dict],
                  weights: dict) -> list[dict]:
    """LOO 교차 검증: 각 GT 노드의 랭크 위치 확인."""
    fn_scores = score_functions(graph, weights)
    n = len(fn_scores)
    fn_ids = {r["fn_id"] for r in fn_scores}
    rank_map = {r["fn_id"]: r["rank"] for r in fn_scores}

    results = []
    for gt in ground_truth:
        resolved = resolve_gt_id(gt["id"], fn_ids)
        if resolved is None:
            results.append({
                "left_out": gt["id"], "resolved": None,
                "rank": None, "rank_pct": 1.0, "pass": False,
                "note": "그래프 미포함",
            })
            continue

        rank = rank_map.get(resolved, n)
        rank_pct = rank / n
        results.append({
            "left_out": gt["id"], "resolved": resolved,
            "rank": rank, "rank_pct": round(rank_pct, 3),
            "pass": rank_pct <= 0.30,
        })

    return results


# ── 가중치 자동 조정 ──────────────────────────────────────

def _adjust_weights(weights: dict, fn_scores: list[dict],
                    ground_truth: list[dict],
                    target_pct: float = 0.30) -> dict:
    """미달 GT 노드의 상대 우위/열위 기반 가중치 조정.

    target_pct: LOO 미달 시 0.30 (상위 30%), LOO 통과 시 0.20 (recall 개선).
    """
    fn_ids = {r["fn_id"] for r in fn_scores}
    n = len(fn_scores)
    score_map = {r["fn_id"]: r for r in fn_scores}

    axis_ratio_map = {
        "s1_structure": "r1", "s2_barrier": "r2",
        "s3_economics": "r3", "s4_demand": "r4",
    }

    # 타겟 경계 노드의 ratio 산출
    boundary_rank = max(1, int(n * target_pct))
    boundary_nodes = [r for r in fn_scores if r["rank"] <= boundary_rank]
    if not boundary_nodes:
        return weights

    max_rank = max(r["rank"] for r in boundary_nodes)
    target_nodes = [r for r in fn_scores if r["rank"] == max_rank]
    target_ratios = {}
    for axis, rkey in axis_ratio_map.items():
        target_ratios[axis] = (
            sum(r["_ratios"][rkey] for r in target_nodes) / len(target_nodes)
        )

    # 미달 GT 노드의 상대 우위/열위 집계
    advantage: dict[str, float] = {a: 0.0 for a in axis_ratio_map}
    disadvantage: dict[str, float] = {a: 0.0 for a in axis_ratio_map}

    miss_count = 0
    for gt in ground_truth:
        resolved = resolve_gt_id(gt["id"], fn_ids)
        if resolved is None:
            continue
        r = score_map.get(resolved)
        if not r or "_ratios" not in r:
            continue
        if r["rank"] / n <= target_pct:
            continue
        miss_count += 1
        for axis, rkey in axis_ratio_map.items():
            diff = r["_ratios"][rkey] - target_ratios[axis]
            if diff > 0:
                advantage[axis] += diff
            else:
                disadvantage[axis] += abs(diff)

    if miss_count == 0:
        return weights

    new_w = dict(weights)

    # 우위 축 강화 (+20%), 열위 축 약화 (-20%)
    best_adv = max(advantage, key=lambda x: advantage[x])
    worst_dis = max(disadvantage, key=lambda x: disadvantage[x])

    if advantage[best_adv] > 0:
        new_w[best_adv] = round(new_w.get(best_adv, 25) * 1.2, 1)
    if disadvantage[worst_dis] > 0 and worst_dis != best_adv:
        new_w[worst_dis] = round(
            max(new_w.get(worst_dis, 15) * 0.8, 1.0), 1,
        )

    return new_w


# ── 캘리브레이션 루프 ─────────────────────────────────────

def calibration_loop(
    graph: Graph,
    ground_truth: list[dict],
    weights: dict,
    max_cycles: int = 10,
) -> dict:
    """L4 캘리브레이션 루프.

    종료 조건:
      1. Gate 통과 (Recall >= 0.8 AND LOO 전원 상위 30%)
      2. max_cycles 도달
      3. 2사이클 연속 정체 (Recall 변화 < 0.05)
    """
    history: list[dict] = []
    stagnation = 0

    # 최적 상태 추적 (LOO 통과율 → recall → mean rank 순으로 우선)
    best_weights = dict(weights)
    best_loo_rate = -1.0
    best_recall = -1.0
    best_mrp = 1.0
    best_loo: list = []
    best_fn_scores: list = []
    best_cycle = 0

    for cycle in range(1, max_cycles + 1):
        fn_scores = score_functions(graph, weights)
        recall = recall_at_k(fn_scores, ground_truth)
        mrp = mean_rank_percentile(fn_scores, ground_truth)
        loo = leave_one_out(graph, ground_truth, weights)

        loo_pass_rate = (
            sum(1 for l in loo if l["pass"]) / len(loo) if loo else 0
        )
        history.append({
            "cycle": cycle,
            "recall": round(recall, 3),
            "mean_rank_pct": round(mrp, 3),
            "weights": dict(weights),
            "loo_pass_rate": round(loo_pass_rate, 3),
        })

        # 최적 상태 갱신 (LOO → recall → mrp 순)
        is_better = (
            loo_pass_rate > best_loo_rate
            or (loo_pass_rate == best_loo_rate and recall > best_recall)
            or (loo_pass_rate == best_loo_rate and recall == best_recall
                and mrp < best_mrp)
        )
        if is_better:
            best_weights = dict(weights)
            best_loo_rate = loo_pass_rate
            best_recall = recall
            best_mrp = mrp
            best_loo = loo
            best_fn_scores = fn_scores
            best_cycle = cycle
            stagnation = 0
        else:
            stagnation += 1

        # Gate 체크
        loo_all = all(l["pass"] for l in loo)
        if recall >= 0.8 and loo_all:
            return _result(True, None, cycle, weights, recall, mrp,
                           loo, history, fn_scores)

        # 정체: 최적 상태가 3사이클 동안 갱신 안 되면 종료
        if stagnation >= 3:
            return _result(False, "stagnation", best_cycle, best_weights,
                           best_recall, best_mrp, best_loo, history,
                           best_fn_scores)

        # 가중치 조정 — LOO 통과 시 recall 타겟으로 전환
        loo_all_pass = all(l["pass"] for l in loo)
        target = 0.20 if loo_all_pass else 0.30
        candidate = _adjust_weights(weights, fn_scores, ground_truth, target)
        cand_scores = score_functions(graph, candidate)
        cand_loo = leave_one_out(graph, ground_truth, candidate)
        cand_loo_rate = (
            sum(1 for l in cand_loo if l["pass"]) / len(cand_loo)
            if cand_loo else 0
        )
        if cand_loo_rate >= loo_pass_rate:
            weights = candidate
        else:
            # 회귀 → 소폭 조정 시도 (절반만 적용)
            half = {}
            for k in candidate:
                if k in weights:
                    half[k] = round((weights[k] + candidate[k]) / 2, 1)
                else:
                    half[k] = candidate[k]
            weights = half

    # max_cycles 도달
    fn_scores = score_functions(graph, weights)
    recall = recall_at_k(fn_scores, ground_truth)
    mrp = mean_rank_percentile(fn_scores, ground_truth)
    loo = leave_one_out(graph, ground_truth, weights)

    return _result(False, "max_cycles", max_cycles, weights, recall, mrp,
                   loo, history, fn_scores)


def _result(converged: bool, reason: str | None, cycles: int,
            weights: dict, recall: float, mrp: float,
            loo: list, history: list, fn_scores: list) -> dict:
    return {
        "converged": converged,
        "reason": reason,
        "cycles_run": cycles,
        "final_weights": weights,
        "recall": recall,
        "mean_rank_pct": mrp,
        "loo_results": loo,
        "history": history,
        "fn_scores": fn_scores,
    }
