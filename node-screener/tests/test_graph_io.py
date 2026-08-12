"""Phase 0 완료 게이트: 그래프 저장 → 로드 왕복 테스트."""

from __future__ import annotations

import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from src.graph_io import load_graph, save_graph
from src.models import (
    CompanyFunction,
    CompanyNode,
    Edge,
    FunctionNode,
    Graph,
    GraphMeta,
)


def _make_sample_graph() -> Graph:
    return Graph(
        meta=GraphMeta(
            chain="hbm",
            year_month="2026-07",
            source_files=["test.md"],
            created="2026-07-25",
        ),
        functions=[
            FunctionNode(
                id="fn_tc_bond", name="TC 본딩", chain="hbm", stage="후공정"
            ),
            FunctionNode(
                id="fn_cowos", name="CoWoS 패키징", chain="hbm", stage="첨단 패키징"
            ),
        ],
        companies=[
            CompanyNode(
                id="co_hanmi",
                name="한미반도체",
                ticker="042700.KS",
                functions=[
                    CompanyFunction(
                        fn="fn_tc_bond",
                        share=0.71,
                        evidence=["IR 자료 2026"],
                        confidence=0.9,
                    )
                ],
            ),
            CompanyNode(
                id="co_tsmc",
                name="TSMC",
                ticker="TSM",
                functions=[
                    CompanyFunction(
                        fn="fn_cowos",
                        share=0.95,
                        evidence=["TrendForce 2026.06"],
                        confidence=0.85,
                    )
                ],
            ),
        ],
        edges=[
            Edge(
                **{"from": "co_hanmi", "to": "co_tsmc"},
                type="supply",
                share=0.35,
                evidence=["IR 자료", "뉴스 기사"],
                confidence=0.8,
                asof="2026-06",
                substitutable=False,
                note="TC본더 납품",
            )
        ],
    )


def test_roundtrip(tmp_path: Path):
    """저장 → 로드 왕복: model_dump() 결과가 동일해야 한다."""
    original = _make_sample_graph()

    with patch("src.graph_io.GRAPH_DIR", tmp_path):
        saved_path = save_graph(original, "hbm", "2026-07")
        assert saved_path.exists()

        loaded = load_graph("hbm", "2026-07")

    assert original.model_dump(by_alias=True) == loaded.model_dump(by_alias=True)


def test_korean_preserved(tmp_path: Path):
    """한글이 유니코드 이스케이프 없이 보존되는지 확인."""
    graph = _make_sample_graph()

    with patch("src.graph_io.GRAPH_DIR", tmp_path):
        saved_path = save_graph(graph, "hbm", "2026-07")
        content = saved_path.read_text(encoding="utf-8")

    assert "한미반도체" in content
    assert "\\u" not in content


def test_edge_alias_serialization():
    """Edge의 from/to alias가 JSON 직렬화 시 올바르게 출력되는지 확인."""
    edge = Edge(
        **{"from": "co_a", "to": "co_b"},
        type="supply",
        evidence=["test"],
    )
    dumped = edge.model_dump(by_alias=True)
    assert "from" in dumped
    assert "to" in dumped
    assert "source" not in dumped
    assert "target" not in dumped


def test_edge_requires_evidence():
    """Edge에 evidence가 비어 있으면 유효성 검증 실패."""
    with pytest.raises(Exception):
        Edge(
            **{"from": "co_a", "to": "co_b"},
            type="supply",
            evidence=[],
        )


def test_directory_creation(tmp_path: Path):
    """존재하지 않는 체인 디렉토리가 자동 생성되는지 확인."""
    graph = _make_sample_graph()

    with patch("src.graph_io.GRAPH_DIR", tmp_path):
        saved_path = save_graph(graph, "new_chain", "2026-07")

    assert saved_path.parent.name == "new_chain"
    assert saved_path.exists()
