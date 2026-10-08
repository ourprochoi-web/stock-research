#!/usr/bin/env python3
"""Show independent-origin counts for one routing id or a ledger file.

  python3 scripts/source_cluster.py r-20261008-10
  python3 scripts/source_cluster.py --ledger ledger/judgment_ledger.jsonl
"""
from __future__ import annotations

import argparse
import json

from ledger_common import LEDGER_PATH, cluster_records, cross_claim_duplicates, load_intake_index, load_routing_index, read_jsonl


def main(argv=None):
    ap = argparse.ArgumentParser(description="Count independent origins behind a claim")
    ap.add_argument("routing_id", nargs="?")
    ap.add_argument("--ledger", default=None)
    args = ap.parse_args(argv)
    if args.ledger:
        rows = read_jsonl(args.ledger or LEDGER_PATH)
        for row in rows:
            ev = row.get("evidence") or {}
            print(f"{row['id']} {row['routing_id']} {row['ticker']} {ev.get('independent_n')}/{ev.get('intake_n')}")
        dups = cross_claim_duplicates(rows)
        if dups:
            print("cross-claim URL/filing duplicates:")
            print(json.dumps(dups, ensure_ascii=False, indent=1))
        return 0
    if not args.routing_id:
        ap.error("routing id or --ledger")
    route = load_routing_index().get(args.routing_id)
    if not route:
        print(f"no routing {args.routing_id}")
        return 1
    intake = load_intake_index()
    records = [intake[i] for i in route.get("intake") or [] if i in intake]
    result = cluster_records(records)
    print(json.dumps(result, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
