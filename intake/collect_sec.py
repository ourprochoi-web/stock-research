#!/usr/bin/env python3
"""SEC XBRL companyfacts 를 티커 목록으로 받아 intake/files/sec/{TICKER}.json 에 <슬림> 스냅샷으로 남긴다.

수집 층의 주문형 수집기. 이 샌드박스는 data.sec.gov 가 막혀 있어 GitHub Actions(collect-sec.yml)에서 돈다.
판단은 하지 않는다 — 태그별 분기·연간 원값만 남기고, 분기 재구성·TTM·비율은 브레인 단계에서 한다.
용법: collect_sec.py XOM CVX ... [--out intake/files/sec]
"""
import io
import json
import os
import sys
import time
import urllib.request
from datetime import date

UA = "ourprochoi Research kenchoi@keywestaim.com"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG = os.path.join(ROOT, "intake", "collected.jsonl")
TAGS = [  # 손익 · 현금흐름 · 재무상태 · 상류 특유 · 주식수
    "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "RevenueFromContractWithCustomerIncludingAssessedTax",
    "OperatingIncomeLoss", "NetIncomeLoss", "DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
    "CostOfRevenue", "CostsAndExpenses", "InterestExpense", "IncomeTaxExpenseBenefit",
    "NetCashProvidedByUsedInOperatingActivities", "PaymentsToAcquirePropertyPlantAndEquipment",
    "PaymentsToAcquireOilAndGasPropertyAndEquipment", "PaymentsToAcquireProductiveAssets", "PaymentsToExploreAndDevelopOilAndGasProperties",
    "PaymentsOfDividends", "PaymentsOfDividendsCommonStock", "PaymentsForRepurchaseOfCommonStock",
    "LongTermDebt", "LongTermDebtNoncurrent", "LongTermDebtCurrent", "LongTermDebtAndCapitalLeaseObligations", "DebtCurrent",
    "CashAndCashEquivalentsAtCarryingValue", "StockholdersEquity", "Assets",
    "ImpairmentOfOilAndGasProperties", "ResultsOfOperationsImpairmentOfOilAndGasProperties",
    "DerivativeGainLossOnDerivativeNet", "GainLossOnDerivativeInstrumentsNetPretax", "UnrealizedGainLossOnDerivatives",
    "CommonStockSharesOutstanding", "EntityCommonStockSharesOutstanding",
    # 2026-09-13 2차 — 메이저(XOM·CVX·COP·OXY)는 OperatingIncomeLoss 를 안 쓴다. 세전이익·기타 매출·감액 태그
    "RevenuesExcludingInterestAndDividends", "RevenuesNetOfInterestExpense", "SalesRevenueNet",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
    "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesForeign",
    "AssetImpairmentCharges", "ImpairmentOfLongLivedAssetsHeldForUse", "ImpairmentOfLongLivedAssetsToBeDisposedOf", "ImpairmentOfOilAndGasPropertiesAndOtherAssets",
    "ExplorationExpense", "ExplorationAbandonmentAndImpairmentExpense", "ProductionTaxExpense",
    "NetCashProvidedByUsedInInvestingActivities", "PaymentsToAcquireBusinessesNetOfCashAcquired", "ProceedsFromSaleOfPropertyPlantAndEquipment",
    "IncomeLossFromEquityMethodInvestments", "NoncontrollingInterestInNetIncomeLoss", "NetIncomeLossAttributableToNoncontrollingInterest",
]


def get(url, retries=3):
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
            with urllib.request.urlopen(req, timeout=40) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    data = gzip.decompress(data)
                return r.status, data
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    return 0, str(last).encode()


def main(argv):
    out = os.path.join(ROOT, "intake", "files", "sec")
    if "--out" in argv:
        out = argv[argv.index("--out") + 1]
        argv = [a for a in argv if a not in ("--out", out)]
    tickers = [t.upper() for t in argv[1:] if not t.startswith("--")]
    if not tickers:
        print("usage: collect_sec.py TICKER [TICKER ...]")
        return 2
    os.makedirs(out, exist_ok=True)
    st, body = get("https://www.sec.gov/files/company_tickers.json")
    if st != 200:
        print(f"[sec] ⚠ company_tickers.json 실패 HTTP {st}: {body[:120]!r}")
        return 1
    tk2cik = {v["ticker"].upper(): int(v["cik_str"]) for v in json.loads(body).values()}
    today = date.today().isoformat()
    ids = set()
    if os.path.exists(LOG):
        for ln in io.open(LOG, encoding="utf-8"):
            if ln.strip():
                ids.add(json.loads(ln)["id"])
    n = 1
    for tk in tickers:
        cik = tk2cik.get(tk)
        rec = {"date": today, "kind": "XBRL", "host": "data.sec.gov", "subject": f"{tk} companyfacts 슬림 스냅샷", "auto": True, "routed": False}
        while f"c-{today.replace('-', '')}-{n:02d}" in ids:
            n += 1
        rec["id"] = f"c-{today.replace('-', '')}-{n:02d}"
        ids.add(rec["id"])
        if not cik:
            rec.update(status="404", note="company_tickers.json 에 티커 없음", path="—")
        else:
            url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
            rec["path"] = url.split("data.sec.gov", 1)[1]
            st, body = get(url)
            if st != 200:
                rec.update(status="blocked" if st in (0, 403) else str(st), note=body[:160].decode(errors="ignore"))
            else:
                facts = json.loads(body)
                slim = {"cik": cik, "entityName": facts.get("entityName"), "fetched": today, "source": url, "facts": {}}
                for ns in ("us-gaap", "dei"):
                    for tag, obj in facts.get("facts", {}).get(ns, {}).items():
                        if tag in TAGS:
                            units = {}
                            for unit, rows in obj.get("units", {}).items():
                                units[unit] = [{k: r.get(k) for k in ("start", "end", "val", "fy", "fp", "form", "filed", "frame")} for r in rows]
                            slim["facts"][f"{ns}:{tag}"] = {"label": obj.get("label"), "units": units}
                path = os.path.join(out, f"{tk}.json")
                io.open(path, "w", encoding="utf-8").write(json.dumps(slim, ensure_ascii=False))
                rec.update(status="ok", file=os.path.relpath(path, ROOT), bytes=os.path.getsize(path), tags=len(slim["facts"]))
            time.sleep(0.15)  # SEC fair-use
        io.open(LOG, "a", encoding="utf-8").write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[sec] {tk}: {rec['status']}" + (f" · {rec.get('tags')} tags · {rec.get('bytes')}B" if rec.get("status") == "ok" else f" · {rec.get('note')}"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
