"""그래프 스키마 — Pydantic v2 모델."""

from __future__ import annotations

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


class FunctionNode(BaseModel):
    """Layer 1 — 기능 노드 (공정·기술 단계)."""

    id: str
    name: str
    chain: str
    stage: str


class CompanyFunction(BaseModel):
    """기업이 수행하는 기능 매핑."""

    fn: str
    share: Optional[float] = None
    evidence: List[str] = Field(default_factory=list)
    confidence: float = 0.5


class CompanyNode(BaseModel):
    """Layer 2 — 기업 노드."""

    id: str
    name: str
    ticker: Optional[str] = None
    functions: List[CompanyFunction] = Field(default_factory=list)


class Edge(BaseModel):
    """기업 간 관계 엣지. from/to는 Python 예약어이므로 alias 사용."""

    source: str = Field(alias="from", serialization_alias="from")
    target: str = Field(alias="to", serialization_alias="to")
    type: Literal["supply", "tech_dependency", "qualification"]
    share: Optional[float] = None
    evidence: List[str] = Field(min_length=1)
    confidence: float = 0.5
    asof: Optional[str] = None
    substitutable: bool = False
    note: Optional[str] = None

    model_config = {"populate_by_name": True}


class GraphMeta(BaseModel):
    """그래프 메타데이터."""

    chain: str
    year_month: str
    source_files: List[str] = Field(default_factory=list)
    created: Optional[str] = None


class Graph(BaseModel):
    """밸류체인 그래프 루트."""

    meta: GraphMeta
    functions: List[FunctionNode] = Field(default_factory=list)
    companies: List[CompanyNode] = Field(default_factory=list)
    edges: List[Edge] = Field(default_factory=list)
