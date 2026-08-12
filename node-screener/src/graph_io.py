"""그래프 스냅샷 저장/로드 + CSV 임포트."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .models import (
    CompanyFunction,
    CompanyNode,
    Edge,
    FunctionNode,
    Graph,
    GraphMeta,
)

GRAPH_DIR = Path(__file__).resolve().parent.parent / "graph"


def save_graph(graph: Graph, chain: str, year_month: str) -> Path:
    """그래프를 JSON 파일로 저장. 반환: 저장 경로."""
    dest = GRAPH_DIR / chain / f"{year_month}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = graph.model_dump(by_alias=True)
    dest.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return dest


def load_graph(chain: str, year_month: str) -> Graph:
    """JSON 파일에서 그래프 로드."""
    path = GRAPH_DIR / chain / f"{year_month}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    return Graph(**data)


def import_companies_csv(graph: Graph, csv_path: str | Path) -> Graph:
    """CSV에서 기업 노드를 임포트해 기존 그래프에 추가.

    CSV 컬럼: id, name, ticker, fn, share, evidence, confidence
    같은 id의 기업이 여러 행이면 functions 리스트로 병합.
    """
    df = pd.read_csv(csv_path)
    existing = {c.id: c for c in graph.companies}

    for company_id, rows in df.groupby("id"):
        row0 = rows.iloc[0]
        if company_id not in existing:
            company = CompanyNode(
                id=str(company_id),
                name=str(row0["name"]),
                ticker=str(row0["ticker"]) if pd.notna(row0.get("ticker")) else None,
            )
            existing[company_id] = company
            graph.companies.append(company)

        company = existing[company_id]
        for _, row in rows.iterrows():
            if pd.notna(row.get("fn")):
                evidence = (
                    [s.strip() for s in str(row["evidence"]).split("|")]
                    if pd.notna(row.get("evidence"))
                    else []
                )
                cf = CompanyFunction(
                    fn=str(row["fn"]),
                    share=float(row["share"]) if pd.notna(row.get("share")) else None,
                    evidence=evidence,
                    confidence=float(row["confidence"])
                    if pd.notna(row.get("confidence"))
                    else 0.5,
                )
                company.functions.append(cf)

    return graph


def import_edges_csv(graph: Graph, csv_path: str | Path) -> Graph:
    """CSV에서 엣지를 임포트해 기존 그래프에 추가.

    CSV 컬럼: from, to, type, share, evidence, confidence, asof, substitutable, note
    """
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        evidence = (
            [s.strip() for s in str(row["evidence"]).split("|")]
            if pd.notna(row.get("evidence"))
            else ["manual"]
        )
        edge = Edge(
            **{
                "from": str(row["from"]),
                "to": str(row["to"]),
            },
            type=str(row["type"]),
            share=float(row["share"]) if pd.notna(row.get("share")) else None,
            evidence=evidence,
            confidence=float(row["confidence"])
            if pd.notna(row.get("confidence"))
            else 0.5,
            asof=str(row["asof"]) if pd.notna(row.get("asof")) else None,
            substitutable=bool(row.get("substitutable", False)),
            note=str(row["note"]) if pd.notna(row.get("note")) else None,
        )
        graph.edges.append(edge)

    return graph
