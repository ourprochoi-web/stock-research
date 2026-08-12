"""5축 스코어링 엔진 — function-first 스코어 산출 + RaRR.

S1~S5 각 축은 0~1 ratio를 산출, weights.yaml의 가중치를 곱해 최종 점수.
총점 = S1*w1 + S2*w2 + S3*w3 + S4*w4 + S5*w5  (w5 < 0 → 감점)
"""

from __future__ import annotations

from pathlib import Path

import networkx as nx
import yaml

from .models import Graph

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


# ── 가중치 I/O ─────────────────────────────────────────────

def load_weights(path: str | None = None) -> dict:
    """config/weights.yaml에서 scoring 가중치 로드."""
    p = Path(path) if path else CONFIG_DIR / "weights.yaml"
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    return data.get("scoring", {})


def save_weights(weights: dict, calibration: dict | None = None,
                 path: str | None = None) -> None:
    """weights.yaml에 scoring + calibration 섹션 저장."""
    p = Path(path) if path else CONFIG_DIR / "weights.yaml"
    data = yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}
    data["scoring"] = weights
    if calibration is not None:
        data["calibration"] = calibration
    p.write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False),
        encoding="utf-8",
    )


# ── NetworkX 어댑터 ───────────────────────────────────────

def graph_to_nx(graph: Graph) -> nx.DiGraph:
    """Pydantic Graph -> NetworkX DiGraph (company 노드 + edge).

    노드 속성: name, functions (fn id 리스트)
    엣지 속성: type, confidence, share, substitutable
    동일 source-target 쌍이 복수이면 최고 confidence 유지.
    """
    G = nx.DiGraph()
    for co in graph.companies:
        G.add_node(co.id, name=co.name,
                   functions=[cf.fn for cf in co.functions])
    for e in graph.edges:
        if not (G.has_node(e.source) and G.has_node(e.target)):
            continue
        attrs = dict(type=e.type, confidence=e.confidence,
                     share=e.share, substitutable=e.substitutable)
        if G.has_edge(e.source, e.target):
            if e.confidence > G[e.source][e.target].get("confidence", 0):
                G[e.source][e.target].update(attrs)
        else:
            G.add_edge(e.source, e.target, **attrs)
    return G


# ── 유틸 ──────────────────────────────────────────────────

def _fn_to_companies(graph: Graph, fn_id: str) -> list[str]:
    """기능 ID -> 해당 기능을 수행하는 기업 ID 리스트."""
    return [
        co.id for co in graph.companies
        if any(cf.fn == fn_id for cf in co.functions)
    ]


# ── S1: 구조 (0~1) ────────────────────────────────────────

def score_s1_structure(G: nx.DiGraph, graph: Graph, fn_id: str,
                       all_pr: dict[str, float],
                       aps: set[str],
                       forward_pr: dict[str, float] | None = None) -> float:
    """S1 구조: 역방향 PageRank + 고객 중요도 블렌드 + AP 보너스.

    역방향 PageRank만으로는 말단 공급사(Disco, 한미, Leeno)가
    허브 대비 낮은 점수를 받음. 고객의 순방향 PageRank를 혼합하여
    "중요한 고객에게 공급하는 말단 독점 공급사"의 구조적 중요성을 반영.
    """
    cos = _fn_to_companies(graph, fn_id)
    if not cos:
        return 0.0

    # (1) 역방향 PageRank 백분위
    pr_vals = [all_pr.get(c, 0.0) for c in cos]
    avg_pr = sum(pr_vals) / len(pr_vals)

    all_vals = sorted(all_pr.values())
    if not all_vals:
        rev_pct = 0.5
    else:
        rank = sum(1 for v in all_vals if v <= avg_pr)
        rev_pct = rank / len(all_vals)

    # (2) 고객 중요도 백분위 (순방향 PageRank 기반)
    cust_pct = 0.0
    if forward_pr:
        cust_prs = []
        for c in cos:
            for succ in G.successors(c):
                cust_prs.append(forward_pr.get(succ, 0.0))
        if cust_prs:
            avg_cust = sum(cust_prs) / len(cust_prs)
            all_fwd = sorted(forward_pr.values())
            cust_pct = sum(1 for v in all_fwd if v <= avg_cust) / len(all_fwd)

    # 블렌드: 역방향 PR 50% + 고객 중요도 50%
    blended = rev_pct * 0.5 + cust_pct * 0.5

    base = blended * 0.8             # 0 ~ 0.8
    if any(c in aps for c in cos):
        base += 0.2                  # AP 보너스
    return min(base, 1.0)


# ── S2: 대체 장벽 (0~1) ───────────────────────────────────

def score_s2_barrier(graph: Graph, fn_id: str) -> float:
    """S2 대체 장벽: 1등 점유율 우선, 없으면 회사 수 fallback.

    핵심: 회사가 여러 개여도 1등이 70%+ 잡으면 사실상 독점.
    - share 데이터 있으면 max_share 기반 판정
    - 없으면 회사 수 bracket fallback
    """
    cos = _fn_to_companies(graph, fn_id)
    n = len(cos)
    if n == 0:
        return 0.0

    if n == 1:
        # 그래프에 1사만 → 우리 분석에선 독점
        base = 1.0
    else:
        # 1등 점유율 탐색
        max_share = 0.0
        has_share = False
        for co in graph.companies:
            for cf in co.functions:
                if cf.fn == fn_id and cf.share is not None:
                    has_share = True
                    max_share = max(max_share, cf.share)

        if has_share and max_share > 0:
            # 점유율 기반: 1등이 지배적이면 높은 장벽
            if max_share >= 0.7:
                base = 0.95
            elif max_share >= 0.5:
                base = 0.80
            elif max_share >= 0.3:
                base = 0.60
            else:
                base = 0.40
        else:
            # fallback: 회사 수 bracket
            bracket = {2: 0.8, 3: 0.6, 4: 0.4}
            base = bracket.get(n, 0.2)

    # 비대체 엣지 미세 보너스 (+최대 0.05)
    cos_set = set(cos)
    non_sub = total_e = 0
    for e in graph.edges:
        if e.source in cos_set or e.target in cos_set:
            total_e += 1
            if not e.substitutable:
                non_sub += 1
    bonus = (non_sub / total_e * 0.05) if total_e else 0.0

    return min(base + bonus, 1.0)


# ── S3: 경제성 MVP 근사 (0~1) ─────────────────────────────

def score_s3_economics(G: nx.DiGraph, graph: Graph, fn_id: str,
                       forward_pr: dict[str, float] | None = None) -> float:
    """S3 경제성: 중요도 가중 downstream reach + 고객 수(out-degree).

    이전: 단순 downstream 노드 수 → 말단 공급사가 4/29=14%로 과소평가.
    수정: downstream 노드의 순방향 PageRank 합으로 가중. SK하이닉스에
    공급하는 Disco(3개 고객)가 소규모 기업 10개 공급보다 높은 점수.
    """
    cos = _fn_to_companies(graph, fn_id)
    if not cos:
        return 0.0

    total_n = G.number_of_nodes()
    if total_n <= 1:
        return 0.5

    # downstream reach (중요도 가중)
    downstream: set[str] = set()
    for c in cos:
        if c in G:
            downstream.update(nx.descendants(G, c))

    if forward_pr and downstream:
        # 중요도 가중: downstream 노드의 PR 합 / 자기 제외 전체 PR
        ds_pr = sum(forward_pr.get(n, 0.0) for n in downstream)
        cos_pr = sum(forward_pr.get(c, 0.0) for c in cos)
        remaining_pr = 1.0 - cos_pr    # PageRank 합 = 1.0
        dr = ds_pr / remaining_pr if remaining_pr > 0 else 0.0
    else:
        dr = len(downstream) / (total_n - 1) if total_n > 1 else 0.0

    # out-degree (고객 수 기반 경제적 중요도)
    out_deg = [G.out_degree(c) for c in cos if c in G]
    avg_out = sum(out_deg) / len(out_deg) if out_deg else 0
    all_out = dict(G.out_degree())
    max_out = max(all_out.values()) if all_out else 1
    od = avg_out / max_out if max_out > 0 else 0

    return min(dr * 0.6 + od * 0.4, 1.0)


# ── S4: 수요 내구성 MVP 근사 (0~1) ────────────────────────

def score_s4_demand(graph: Graph, fn_id: str,
                    all_demands: dict[str, float]) -> float:
    """S4 수요: confidence 가중 edge 수의 백분위.

    이전: max 대비 비율 → hub 노드가 max를 독점해 말단은 항상 낮음.
    수정: 백분위 정규화 → 고르게 분포.
    """
    demand = all_demands.get(fn_id, 0.0)
    if not all_demands:
        return 0.0

    sorted_vals = sorted(all_demands.values())
    rank = sum(1 for v in sorted_vals if v <= demand)
    return rank / len(sorted_vals)


# ── S5: 감점 — 고객 집중도 (0~1, 1 = 최대 감점) ──────────

def score_s5_penalty(graph: Graph, fn_id: str) -> float:
    """S5 고객 집중도: 고객 수 기반 감점.

    edge share는 "공급 비중"이지 "매출 의존도"가 아님.
    매출 데이터 없으므로 고객(out-edge target) 수로 집중도 근사.
    - 고객 1곳 → 높은 집중 → 큰 감점
    - 고객 5곳+ → 분산 → 감점 없음
    """
    cos = _fn_to_companies(graph, fn_id)
    if not cos:
        return 0.0

    # 매핑 기업들의 고객(out-edge target) 수 집계
    customers: set[str] = set()
    for c in cos:
        for e in graph.edges:
            if e.source == c:
                customers.add(e.target)

    n = len(customers)
    if n == 0:
        return 0.0
    if n == 1:
        return 0.6
    if n == 2:
        return 0.3
    if n <= 4:
        return 0.1
    return 0.0


# ── RaRR (Revenue-at-Risk via Removal) ────────────────────

def compute_rarr(G: nx.DiGraph, company_ids: list[str]) -> dict:
    """노드 제거 -> 대체 경로 없는 downstream 노드 수."""
    if not company_ids:
        return {"disconnected": 0, "total_downstream": 0, "rarr_ratio": 0.0}

    valid = [c for c in company_ids if c in G]
    if not valid:
        return {"disconnected": 0, "total_downstream": 0, "rarr_ratio": 0.0}

    pre_ds: set[str] = set()
    for c in valid:
        pre_ds.update(nx.descendants(G, c))
    pre_ds -= set(valid)

    if not pre_ds:
        return {"disconnected": 0, "total_downstream": 0, "rarr_ratio": 0.0}

    G2 = G.copy()
    G2.remove_nodes_from(valid)

    still_reachable: set[str] = set()
    for src in set(G2.nodes()) - pre_ds:
        still_reachable.update(nx.descendants(G2, src))

    disc = pre_ds - still_reachable
    return {
        "disconnected": len(disc),
        "total_downstream": len(pre_ds),
        "rarr_ratio": len(disc) / len(pre_ds) if pre_ds else 0.0,
    }


# ── 메인 스코어 산출 ──────────────────────────────────────

def score_functions(graph: Graph, weights: dict | None = None) -> list[dict]:
    """전체 function 스코어 산출 -> 랭킹 (내림차순)."""
    if weights is None:
        weights = load_weights()

    G = graph_to_nx(graph)

    # 사전 계산: 역방향 PageRank (공급사 중요도) + 순방향 PageRank (고객 중요도)
    if G.number_of_nodes() > 0:
        G_rev = G.reverse()
        all_pr = nx.pagerank(G_rev, alpha=0.85)
        forward_pr = nx.pagerank(G, alpha=0.85)
    else:
        all_pr = {}
        forward_pr = {}
    aps = (set(nx.articulation_points(G.to_undirected()))
           if G.number_of_nodes() > 1 else set())

    # S4 백분위 정규화용 전체 demand 맵 (중요도 가중 고유 거래처)
    # 이전: confidence 합산 → 같은 고객을 가진 기능도 edge confidence 차이로 점수 차이
    # 수정: 고유 거래처의 forward PageRank 합 → "얼마나 중요한 거래처와 연결?"
    all_demands: dict[str, float] = {}
    for fn in graph.functions:
        cs = set(_fn_to_companies(graph, fn.id))
        counterparties: set[str] = set()
        for c in cs:
            for e in graph.edges:
                if e.source == c:
                    counterparties.add(e.target)
                elif e.target == c:
                    counterparties.add(e.source)
        counterparties -= cs  # 자기 회사 제외
        all_demands[fn.id] = sum(
            forward_pr.get(cp, 0.01) for cp in counterparties
        )

    w_s1 = weights.get("s1_structure", 25)
    w_s2 = weights.get("s2_barrier", 25)
    w_s3 = weights.get("s3_economics", 20)
    w_s4 = weights.get("s4_demand", 15)
    w_s5 = weights.get("s5_penalty", -25)

    results = []
    for fn in graph.functions:
        cos = _fn_to_companies(graph, fn.id)

        r1 = score_s1_structure(G, graph, fn.id, all_pr, aps, forward_pr)
        r2 = score_s2_barrier(graph, fn.id)
        r3 = score_s3_economics(G, graph, fn.id, forward_pr)
        r4 = score_s4_demand(graph, fn.id, all_demands)
        r5 = score_s5_penalty(graph, fn.id)

        s1 = r1 * w_s1
        s2 = r2 * w_s2
        s3 = r3 * w_s3
        s4 = r4 * w_s4
        s5 = r5 * w_s5          # w_s5 < 0 -> 감점

        total = s1 + s2 + s3 + s4 + s5

        results.append({
            "fn_id": fn.id,
            "name": fn.name,
            "stage": fn.stage,
            "companies": cos,
            "s1": round(s1, 2),
            "s2": round(s2, 2),
            "s3": round(s3, 2),
            "s4": round(s4, 2),
            "s5": round(s5, 2),
            "total": round(total, 2),
            "rarr": compute_rarr(G, cos),
            "_ratios": {"r1": r1, "r2": r2, "r3": r3, "r4": r4, "r5": r5},
        })

    results.sort(key=lambda x: x["total"], reverse=True)

    # 동점 경쟁 랭킹 (competition ranking): 같은 점수 → 같은 랭크
    # 예: 1,2,3,3,3,6 (동점자 모두 최소 순위 부여)
    rank = 1
    for i, r in enumerate(results):
        if i > 0 and results[i]["total"] < results[i - 1]["total"]:
            rank = i + 1
        r["rank"] = rank

    return results


def score_companies(graph: Graph, fn_scores: list[dict]) -> list[dict]:
    """Function 점수를 Company에 배분 (share 가중 평균)."""
    fn_map = {r["fn_id"]: r["total"] for r in fn_scores}

    results = []
    for co in graph.companies:
        if not co.functions:
            results.append({
                "co_id": co.id, "name": co.name, "ticker": co.ticker,
                "score": 0.0, "contributing_fns": [], "rank": 0,
            })
            continue

        wsum = wtot = 0.0
        contribs = []
        for cf in co.functions:
            fs = fn_map.get(cf.fn, 0.0)
            w = cf.share if cf.share is not None else 1.0
            wsum += fs * w
            wtot += w
            contribs.append({"fn": cf.fn, "share": cf.share, "fn_score": fs})

        results.append({
            "co_id": co.id, "name": co.name, "ticker": co.ticker,
            "score": round(wsum / wtot, 2) if wtot else 0.0,
            "contributing_fns": contribs, "rank": 0,
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    for i, r in enumerate(results, 1):
        r["rank"] = i

    return results
