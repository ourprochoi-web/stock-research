"""병합 로직 테스트."""

from __future__ import annotations

from src.merge import merge_graphs, normalize_id
from src.models import (
    CompanyFunction,
    CompanyNode,
    Edge,
    FunctionNode,
    Graph,
    GraphMeta,
)


def _empty_graph(chain: str = "hbm") -> Graph:
    return Graph(
        meta=GraphMeta(chain=chain, year_month="2026-07"),
    )


def test_normalize_id_basic():
    assert normalize_id("co_SK_Hynix") == "co_skhynix"
    assert normalize_id("co_sk_hynix") == "co_skhynix"
    assert normalize_id("FN_TC_BOND") == "fn_tc_bond"
    assert normalize_id("  co_TSMC  ") == "co_tsmc"
    assert normalize_id("co-some-company") == "co_some_company"


def test_normalize_id_known_variants():
    assert normalize_id("co_sk_hainix") == "co_skhynix"
    assert normalize_id("co_hd_hyundai_electric") == "co_hd_hyundai"


def test_merge_functions_dedup():
    base = _empty_graph()
    base.functions.append(
        FunctionNode(id="fn_tc_bond", name="TC 본딩", chain="hbm", stage="후공정")
    )

    incoming = _empty_graph()
    incoming.functions.append(
        FunctionNode(id="fn_tc_bond", name="TC 본딩(중복)", chain="hbm", stage="후공정")
    )
    incoming.functions.append(
        FunctionNode(id="fn_cowos", name="CoWoS", chain="hbm", stage="패키징")
    )

    merge_graphs(base, incoming)
    assert len(base.functions) == 2
    ids = {f.id for f in base.functions}
    assert "fn_tc_bond" in ids
    assert "fn_cowos" in ids


def test_merge_companies_higher_confidence():
    base = _empty_graph()
    base.companies.append(
        CompanyNode(
            id="co_hanmi",
            name="한미반도체",
            functions=[
                CompanyFunction(fn="fn_tc_bond", share=0.7, evidence=["old"], confidence=0.6)
            ],
        )
    )

    incoming = _empty_graph()
    incoming.companies.append(
        CompanyNode(
            id="co_hanmi",
            name="한미반도체",
            functions=[
                CompanyFunction(fn="fn_tc_bond", share=0.71, evidence=["new"], confidence=0.9),
                CompanyFunction(fn="fn_new", share=0.5, evidence=["new2"], confidence=0.8),
            ],
        )
    )

    merge_graphs(base, incoming)
    assert len(base.companies) == 1
    fns = base.companies[0].functions
    assert len(fns) == 2
    tc_bond = next(f for f in fns if f.fn == "fn_tc_bond")
    assert tc_bond.confidence == 0.9  # 높은 confidence로 교체


def test_merge_edges_evidence_merge():
    base = _empty_graph()
    base.edges.append(
        Edge(
            **{"from": "co_a", "to": "co_b"},
            type="supply",
            evidence=["ev1"],
            confidence=0.7,
        )
    )

    incoming = _empty_graph()
    incoming.edges.append(
        Edge(
            **{"from": "co_a", "to": "co_b"},
            type="supply",
            evidence=["ev1", "ev2"],
            confidence=0.9,
        )
    )

    merge_graphs(base, incoming)
    assert len(base.edges) == 1
    assert set(base.edges[0].evidence) == {"ev1", "ev2"}
    assert base.edges[0].confidence == 0.9


def test_merge_edges_different_type():
    """같은 from/to라도 type이 다르면 별개 엣지."""
    base = _empty_graph()
    base.edges.append(
        Edge(
            **{"from": "co_a", "to": "co_b"},
            type="supply",
            evidence=["ev1"],
            confidence=0.7,
        )
    )

    incoming = _empty_graph()
    incoming.edges.append(
        Edge(
            **{"from": "co_a", "to": "co_b"},
            type="tech_dependency",
            evidence=["ev2"],
            confidence=0.8,
        )
    )

    merge_graphs(base, incoming)
    assert len(base.edges) == 2


def test_merge_source_files():
    base = _empty_graph()
    base.meta.source_files = ["a.md"]

    incoming = _empty_graph()
    incoming.meta.source_files = ["a.md", "b.md"]

    merge_graphs(base, incoming)
    assert base.meta.source_files == ["a.md", "b.md"]
