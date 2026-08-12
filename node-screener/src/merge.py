"""그래프 병합 — 엔티티 중복 제거 + ID 정규화."""

from __future__ import annotations

import re

from .models import CompanyNode, Edge, FunctionNode, Graph

# 알려진 ID 변형 매핑 (정규화 후 기준)
KNOWN_VARIANTS: dict[str, str] = {
    # Company 정규화
    "co_sk_hynix": "co_skhynix",
    "co_sk_hainix": "co_skhynix",
    "co_skhainix": "co_skhynix",
    "co_hd_hyundai_electric": "co_hd_hyundai",
    "co_hd_현대일렉트릭": "co_hd_hyundai",
    "co_ge_vernova_inc": "co_ge_vernova",
    "co_siemens_energy_ag": "co_siemens_energy",
    "co_schneider_electric": "co_schneider",
    # Function 정규화 — ground_truth.yaml ID 기준
    "fn_cowos": "fn_cowos_packaging",
    "fn_abf_film": "fn_abf_substrate_film",
    "fn_abf_substrate": "fn_abf_substrate_film",
    "fn_stealth_dicing": "fn_dicing_grinding",
    "fn_taiko_grinding": "fn_dicing_grinding",
    "fn_test_socket": "fn_pogo_pin_socket",
}


def normalize_id(raw_id: str) -> str:
    """ID 정규화: lowercase, 공백→언더스코어, 연속 언더스코어 제거."""
    nid = raw_id.strip().lower().replace(" ", "_").replace("-", "_")
    nid = re.sub(r"_+", "_", nid).strip("_")
    return KNOWN_VARIANTS.get(nid, nid)


def merge_graphs(base: Graph, incoming: Graph) -> Graph:
    """incoming 그래프를 base에 병합. base를 in-place 수정 후 반환."""
    _merge_functions(base, incoming.functions)
    _merge_companies(base, incoming.companies)
    _merge_edges(base, incoming.edges)

    # 소스 파일 목록 병합
    existing_sources = set(base.meta.source_files)
    for sf in incoming.meta.source_files:
        if sf not in existing_sources:
            base.meta.source_files.append(sf)
            existing_sources.add(sf)

    return base


def _merge_functions(base: Graph, incoming: list[FunctionNode]) -> None:
    existing = {normalize_id(f.id): f for f in base.functions}
    for fn in incoming:
        nid = normalize_id(fn.id)
        if nid not in existing:
            fn.id = nid
            base.functions.append(fn)
            existing[nid] = fn


def _merge_companies(base: Graph, incoming: list[CompanyNode]) -> None:
    existing = {normalize_id(c.id): c for c in base.companies}
    for co in incoming:
        nid = normalize_id(co.id)
        if nid not in existing:
            co.id = nid
            base.companies.append(co)
            existing[nid] = co
        else:
            # functions 리스트 병합 (높은 confidence 우선)
            base_co = existing[nid]
            existing_fns = {cf.fn: cf for cf in base_co.functions}
            for cf in co.functions:
                if cf.fn not in existing_fns:
                    base_co.functions.append(cf)
                    existing_fns[cf.fn] = cf
                elif cf.confidence > existing_fns[cf.fn].confidence:
                    # 기존보다 confidence가 높으면 교체
                    idx = base_co.functions.index(existing_fns[cf.fn])
                    base_co.functions[idx] = cf
                    existing_fns[cf.fn] = cf


def _merge_edges(base: Graph, incoming: list[Edge]) -> None:
    def edge_key(e: Edge) -> tuple[str, str, str]:
        return (normalize_id(e.source), normalize_id(e.target), e.type)

    existing: dict[tuple[str, str, str], Edge] = {}
    for e in base.edges:
        existing[edge_key(e)] = e

    for e in incoming:
        key = edge_key(e)
        if key not in existing:
            e.source = normalize_id(e.source)
            e.target = normalize_id(e.target)
            base.edges.append(e)
            existing[key] = e
        else:
            base_edge = existing[key]
            # evidence 병합 (중복 제거)
            ev_set = set(base_edge.evidence)
            for ev in e.evidence:
                if ev not in ev_set:
                    base_edge.evidence.append(ev)
                    ev_set.add(ev)
            # max confidence 채택
            if e.confidence > base_edge.confidence:
                base_edge.confidence = e.confidence
