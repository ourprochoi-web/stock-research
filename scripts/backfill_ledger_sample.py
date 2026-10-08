#!/usr/bin/env python3
"""Write the 2026-10-08 judgment-ledger sample (≤15 rows).

Stance labels are backfill inferences from routing text, not what Lead stored
on the day. Prices come from the Naver chart. A null price stays null.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone

from ledger_common import (
    LEDGER_PATH,
    cluster_records,
    endpoint_for,
    http_json,
    iso_date,
    last_completed_close,
    load_intake_index,
    load_routing_index,
    naver_daily,
    NAVER_UA,
    yyyymmdd,
)

# Explicit sample. One row per (routing_id, ticker). No sizing.
SAMPLE = [
    {
        "id": "j-20261008-01",
        "routing_id": "r-20261008-10",
        "ticker": "005930",
        "name": "삼성전자",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "005930",
        "currency": "KRW",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [
            "hbm-packaging/hbm_pkg_company_samsung.html#T1",
            "hbm-packaging/hbm_pkg_company_samsung.html#T2",
        ],
        "claim_ko": "삼성 3Q26 잠정은 매출이 예상을 밑돌았지만 메모리 이익은 추정을 상회했다는 읽기다.",
        "stance_note": "백필 추론. variant 가 메모리 축 강화이고, 헤드라인 비트 폭은 priced_in.",
        "breaks_if": [
            {
                "text": "10/29 콜에서 HBM4 QoQ 3배 가이던스가 미달이면 합산 비트의 메모리 해석이 깨진다.",
                "metric": "hbm4_qoq_guide",
                "op": "lt",
                "threshold": 3,
                "unit": "x",
                "deadline": "2026-10-29",
                "check": "manual",
            },
            {
                "text": "10/29 콜에서 메모리 영업이익 둔화가 확인되면 같은 해석이 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2026-10-29",
                "check": "manual",
            },
        ],
    },
    {
        "id": "j-20261008-02",
        "routing_id": "r-20261008-11",
        "ticker": "005930",
        "name": "삼성전자",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "005930",
        "currency": "KRW",
        "stance": "중립",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "HBM4E 12단 퀄 헤드라인은 이미 돌았고 물량·양산은 미확정이며 회사는 확인을 거부했다.",
        "stance_note": "백필 추론. 새 사양은 있으나 방향 스탠스로 읽지 않았다.",
        "breaks_if": [
            {
                "text": "회사가 퀄 미통과를 공시하거나 10/29 콜에서 HBM4E 양산이 2027년 이후로 밀리면 공급 선점 해석이 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2026-10-29",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-03",
        "routing_id": "r-20261008-12",
        "ticker": "000660",
        "name": "SK하이닉스",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "000660",
        "currency": "KRW",
        "stance": "중립",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "솔리다임 IPO 주관·약 100억달러·2027년은 확정 공시가 아니라 하이닉스 주가 방향이 아니다.",
        "stance_note": "백필 추론. 기업 이벤트 소문이라 긍정/부정을 붙이지 않았다.",
        "breaks_if": [
            {
                "text": "주관 계약이 깨지거나 2027년에도 신고서가 없으면 규모 서사는 무산이다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2027-12-31",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-04",
        "routing_id": "r-20261008-14",
        "ticker": "AVGO.O",
        "name": "브로드컴",
        "market": "US",
        "naver_kind": "foreign/item",
        "naver_code": "AVGO.O",
        "currency": "USD",
        "stance": "부정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "오픈AI 커스텀칩 생산 금융이 고객 신용위험을 브로드컴 대차대조표로 옮긴다는 읽기다.",
        "stance_note": "백필 추론. 신용이전은 주식에 부정으로 적었다. 규모 추정은 하지 않는다.",
        "breaks_if": [
            {
                "text": "조달이 무산되거나 고객 신용이 공급사 채무로 연결되지 않으면 신용이전 해석이 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": None,
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-05",
        "routing_id": "r-20261008-14",
        "ticker": "ORCL.K",
        "name": "오라클",
        "market": "US",
        "naver_kind": "foreign/item",
        "naver_code": "ORCL.K",
        "currency": "USD",
        "stance": "부정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "오라클이 AI 칩 구매 자금으로 별도 금융을 논의한다는 것은 같은 신용이전 읽기다.",
        "stance_note": "백필 추론. r-20261008-14 를 티커별로 나눴다.",
        "breaks_if": [
            {
                "text": "조달이 무산되거나 고객 신용이 공급사 채무로 연결되지 않으면 신용이전 해석이 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": None,
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-06",
        "routing_id": "r-20261008-15",
        "ticker": "SPCX.O",
        "name": "스페이스X",
        "market": "US",
        "naver_kind": "foreign/item",
        "naver_code": "SPCX.O",
        "currency": "USD",
        "stance": "부정",
        "score_mode": "manual",
        "instrument": "cds_5y",
        "pages": [],
        "claim_ko": "스페이스X 5년 CDS가 약 150bp에서 약 190bp로 넓어졌다는 신용 읽기다. 주식 초과수익으로 채점하지 않는다.",
        "stance_note": "백필 추론. 네이버에 SPCX.O 시세는 있으나 주장은 CDS다.",
        "breaks_if": [
            {
                "text": "5년 CDS가 150bp 아래로 되돌아오거나 부채 조달이 철회되면 신용위험 확대 해석이 깨진다.",
                "metric": "cds_5y_bp",
                "op": "lt",
                "threshold": 150,
                "unit": "bp",
                "deadline": None,
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-07",
        "routing_id": "r-20261008-16",
        "ticker": "APLD.O",
        "name": "어플라이드 디지털",
        "market": "US",
        "naver_kind": "foreign/item",
        "naver_code": "APLD.O",
        "currency": "USD",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "APLD는 재계약 가격 상승과 조달금리 하락이 마진 레버리지라는 읽기다.",
        "stance_note": "백필 추론. variant 가 마진 레버리지이고 레버리지는 breaks_if 로 남겼다.",
        "breaks_if": [
            {
                "text": "12개월 600MW 가동이 지연되거나 총부채 약 64억달러가 현금흐름 전환을 막으면 레버리지 해석이 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": None,
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-08",
        "routing_id": "r-20261008-20",
        "ticker": "353200",
        "name": "대덕전자",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "353200",
        "currency": "KRW",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [
            "hbm-packaging/hbm_pkg_theme_substrate.html#T2",
            "hbm-packaging/hbm_pkg_theme_substrate.html#T4",
        ],
        "claim_ko": "메모리 패키지 기판의 추가 판가·LTA가 대덕전자 BT capa 에 이익 레버리지로 닿는다는 읽기다.",
        "stance_note": "백필 추론. 라우팅이 이름을 용량과 함께 적었다. 테마 전체를 한 종목 스탠스로 단정하지 않는다.",
        "breaks_if": [
            {
                "text": "메모리 IDM 증설 지연·감산 또는 중국 BT 기판 증설로 수급이 완화되면 판가·LTA 레버리지가 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2027-06-30",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-09",
        "routing_id": "r-20261008-20",
        "ticker": "222800",
        "name": "심텍",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "222800",
        "currency": "KRW",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [
            "hbm-packaging/hbm_pkg_theme_substrate.html#T2",
            "hbm-packaging/hbm_pkg_theme_substrate.html#T4",
        ],
        "claim_ko": "같은 판가·LTA 읽기가 심텍 MSAP capa 와 Micron LTA 전례에 걸려 있다.",
        "stance_note": "백필 추론. r-20261008-20 을 티커별로 나눴다.",
        "breaks_if": [
            {
                "text": "메모리 IDM 증설 지연·감산 또는 중국 BT 기판 증설로 수급이 완화되면 판가·LTA 레버리지가 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2027-06-30",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-10",
        "routing_id": "r-20261008-20",
        "ticker": "195870",
        "name": "해성디에스",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "195870",
        "currency": "KRW",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [
            "hbm-packaging/hbm_pkg_theme_substrate.html#T2",
            "hbm-packaging/hbm_pkg_theme_substrate.html#T4",
        ],
        "claim_ko": "같은 판가·LTA 읽기가 해성디에스 패널 capa 숫자와 함께 적혀 있다.",
        "stance_note": "백필 추론. 이름은 라우팅 본문에 있다. 코드 195870 은 update_prices.WATCH 와 name_index 에 있다.",
        "breaks_if": [
            {
                "text": "메모리 IDM 증설 지연·감산 또는 중국 BT 기판 증설로 수급이 완화되면 판가·LTA 레버리지가 깨진다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2027-06-30",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-11",
        "routing_id": "r-20261008-40",
        "ticker": "005930",
        "name": "삼성전자",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "005930",
        "currency": "KRW",
        "stance": "긍정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [
            "hbm-packaging/hbm_pkg_company_samsung.html#T1",
            "hbm-packaging/hbm_pkg_company_samsung.html#T2",
        ],
        "claim_ko": "JPM 은 삼성이 내년 NVDA향 8Hi HBM4 SKU를 준비한다고 적었다. 그 SKU의 기존 주공급은 하이닉스였다.",
        "stance_note": "백필 추론. 점유 이동의 수혜 쪽으로만 이 행을 둔다.",
        "breaks_if": [
            {
                "text": "10/29 콜에서 8Hi HBM4 NVDA향이 하이닉스 독점으로 남고 삼성 진입이 없으면 점유 이동은 기각된다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2026-10-29",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-12",
        "routing_id": "r-20261008-40",
        "ticker": "000660",
        "name": "SK하이닉스",
        "market": "KR",
        "naver_kind": "domestic/item",
        "naver_code": "000660",
        "currency": "KRW",
        "stance": "부정",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": ["hbm-packaging/hbm_pkg_company_sk_hynix.html#T4"],
        "claim_ko": "같은 JPM 문장은 하이닉스가 주공급이던 NVDA향 8Hi HBM4 SKU에 삼성 진입을 적었다.",
        "stance_note": "백필 추론. 같은 라우팅의 반대 티커다. LTA 평탄화는 별도 해석이라 이 행의 조건에 넣지 않았다.",
        "breaks_if": [
            {
                "text": "10/29 콜에서 8Hi HBM4 NVDA향이 하이닉스 독점으로 남고 삼성 진입이 없으면 점유 이탈 해석은 기각된다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2026-10-29",
                "check": "manual",
            }
        ],
    },
    {
        "id": "j-20261008-13",
        "routing_id": "r-20261008-42",
        "ticker": "6762.T",
        "name": "TDK",
        "market": "JP",
        "naver_kind": "foreign/item",
        "naver_code": "6762.T",
        "currency": "JPY",
        "stance": "중립",
        "score_mode": "excess",
        "instrument": "equity",
        "pages": [],
        "claim_ko": "TDK가 HDD 헤드 매각 자금으로 타이요유덴과 자본제휴할 수 있다는 것은 미확정 질문 응답이다.",
        "stance_note": "백필 추론. 확정 계약이 아니므로 긍정으로 올리지 않았다. 코드는 name_index 의 6762.T.",
        "breaks_if": [
            {
                "text": "헤드 매각·JV나 타이요유덴 자본제휴가 공시되지 않고 토시바/STX 캐파 자금 지원으로 끝나면 제휴 추정은 기각된다.",
                "metric": None,
                "op": None,
                "threshold": None,
                "deadline": "2027-03-31",
                "check": "manual",
            }
        ],
    },
]

BENCHMARKS = {
    "KR": {
        "symbol": "KOSPI",
        "kind": "domestic/index",
        "code": "KOSPI",
        "currency": "KRW",
        "why": "국내 주식의 기본 벤치마크. 섹터 ETF는 스탠스가 그 베타일 때만 따로 적는다.",
    },
    "US": {
        "symbol": "SPY",
        "kind": "foreign/item",
        "code": "SPY",
        "currency": "USD",
        "why": "미국 상장 주식의 기본 벤치마크. update_prices 의 SMH.O 는 반도체 베타용으로 남겨 두고 이 표본에는 쓰지 않았다.",
    },
    "JP": {
        "symbol": ".N225",
        "kind": "foreign/index",
        "code": ".N225",
        "currency": "JPY",
        "why": "일본 주식의 기본 지수. api.stock.naver.com/index/.N225/basic 의 indexName 이 니케이 225 다. 종목 차트 코드 .N225 는 비어 있었고 지수 차트는 열렸다.",
    },
}


def quote_name(kind, code):
    """Display name from the same Naver host. Failure returns None and the caller keeps the archive name."""
    if kind == "domestic/item":
        url = f"https://m.stock.naver.com/api/stock/{code}/basic"
        key = "stockName"
    elif kind == "foreign/item":
        url = f"https://api.stock.naver.com/stock/{code}/basic"
        key = "stockName"
    elif kind == "domestic/index":
        # api.stock.naver.com/index/KOSPI/basic returns 409. The mobile host has stockName.
        url = f"https://m.stock.naver.com/api/index/{code}/basic"
        key = "stockName"
    elif kind == "foreign/index":
        url = f"https://api.stock.naver.com/index/{code}/basic"
        key = "indexName"
    else:
        return None, None
    try:
        body = http_json(url, NAVER_UA)
    except Exception as exc:
        return None, f"{type(exc).__name__}: {url}"
    return body.get(key), url


def fetch_ref(spec, asof_iso, now):
    kind = spec["naver_kind"]
    code = spec["naver_code"]
    start = "20260901"
    end = yyyymmdd(asof_iso)
    try:
        series = naver_daily(kind, code, start, end)
    except Exception as exc:
        return {
            "price": None,
            "currency": spec["currency"],
            "asof": None,
            "session": None,
            "naver_code": code,
            "endpoint": endpoint_for(kind, code),
            "unverified_reason": f"fetch failed {type(exc).__name__} {endpoint_for(kind, code)}",
        }, []
    chosen = last_completed_close(series, end, spec["market"], now)
    ref = {
        "price": None if not chosen else chosen[1],
        "currency": spec["currency"],
        "asof": None if not chosen else iso_date(chosen[0]),
        "session": None if not chosen else "regular-close",
        "naver_code": code,
        "endpoint": endpoint_for(kind, code),
        "fetched_at": now.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    if not chosen:
        ref["unverified_reason"] = f"no completed session on or before {asof_iso} at {ref['endpoint']}"
    # Same-calendar bar that is still an open session is recorded and not used.
    same = [pair for pair in series if pair[0] == end]
    if same and (not chosen or chosen[0] != end):
        ref["same_day_bar_ignored"] = {
            "date": iso_date(end),
            "last": same[-1][1],
            "session": "incomplete",
            "used": False,
        }
    return ref, series


def main():
    now = datetime.now(timezone.utc)
    routing = load_routing_index()
    intake = load_intake_index()
    bench_cache = {}
    rows = []
    for spec in SAMPLE:
        route = routing.get(spec["routing_id"])
        if route is None:
            sys.exit(f"missing routing {spec['routing_id']}")
        if route.get("date") != "2026-10-08":
            sys.exit(f"{spec['routing_id']} date is {route.get('date')}")
        ref, _series = fetch_ref(spec, route["date"], now)
        verified_name, name_url = quote_name(spec["naver_kind"], spec["naver_code"])
        market = spec["market"]
        if market not in bench_cache:
            bspec = {
                "naver_kind": BENCHMARKS[market]["kind"],
                "naver_code": BENCHMARKS[market]["code"],
                "currency": BENCHMARKS[market]["currency"],
                "market": market,
            }
            bref, _ = fetch_ref(bspec, route["date"], now)
            bname, burl = quote_name(BENCHMARKS[market]["kind"], BENCHMARKS[market]["code"])
            bench_cache[market] = {
                "symbol": BENCHMARKS[market]["symbol"],
                "name": bname,
                "name_endpoint": burl,
                "kind": BENCHMARKS[market]["kind"],
                "naver_code": BENCHMARKS[market]["code"],
                "currency": BENCHMARKS[market]["currency"],
                "price": bref.get("price"),
                "asof": bref.get("asof"),
                "session": bref.get("session"),
                "endpoint": bref.get("endpoint"),
                "why": BENCHMARKS[market]["why"],
                "same_day_bar_ignored": bref.get("same_day_bar_ignored"),
                "unverified_reason": bref.get("unverified_reason"),
            }
        ids = route.get("intake") or []
        records = [intake[i] for i in ids if i in intake]
        missing = [i for i in ids if i not in intake]
        evidence = cluster_records(records)
        evidence["intake"] = ids
        evidence["intake_missing"] = missing
        row = {
            "id": spec["id"],
            "routing_id": spec["routing_id"],
            "date": route["date"],
            "ticker": spec["ticker"],
            "name": spec["name"],
            "name_on_naver": verified_name,
            "name_endpoint": name_url,
            "market": market,
            "instrument": spec["instrument"],
            "stance": spec["stance"],
            "stance_source": "backfill-inferred",
            "stance_note": spec["stance_note"],
            "score_mode": spec["score_mode"],
            "lead": route.get("source") or "unknown",
            "routing_mark": route.get("verdict"),
            "routing_grade": route.get("grade"),
            "pages": spec["pages"],
            "claim_ko": spec["claim_ko"],
            "ref": ref,
            "benchmark": bench_cache[market],
            "horizons": ["30d", "90d"],
            "breaks_if": spec["breaks_if"],
            "evidence": evidence,
            "scores": None,
        }
        rows.append(row)
        px = ref.get("price")
        print(f"{row['id']} {row['ticker']} {row['stance']} px={px} asof={ref.get('asof')} origins={evidence['independent_n']}/{evidence['intake_n']}")

    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    print(f"wrote {len(rows)} {LEDGER_PATH}")


if __name__ == "__main__":
    main()
