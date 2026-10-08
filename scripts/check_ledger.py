#!/usr/bin/env python3
"""Validate ledger/judgment_ledger.jsonl. Exit 1 on contract breaks.

Does not change check_routing.py. routing.jsonl is read, not written.
"""
from __future__ import annotations

import sys

from ledger_common import LEDGER_PATH, load_routing_index, load_thesis_index, read_jsonl, validate_row


def main(argv=None):
    path = LEDGER_PATH
    if argv and argv[0] != "--":
        # optional path
        if not argv[0].startswith("-"):
            path = argv[0]
    rows = read_jsonl(path)
    routing_ids = set(load_routing_index())
    theses = load_thesis_index()
    errors = []
    seen = set()
    for row in rows:
        if row.get("id") in seen:
            errors.append(f"{row.get('id')}: id 중복")
        seen.add(row.get("id"))
        errors.extend(validate_row(row, routing_ids, theses))
    if errors:
        print(f"[ledger] 거절 {len(errors)}건")
        for err in errors:
            print("   · " + err)
        return 1
    print(f"[ledger] ✓ {len(rows)}행 · routing 포인터와 금지 필드 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
