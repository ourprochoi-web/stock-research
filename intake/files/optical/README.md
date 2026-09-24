# Optical FACT archive / 광통신 팩트 아카이브

Easy-update path for optical (CPO/NPO/UHP/CW/connectivity) claim units.
Follows `docs/rules_archive_2026-09-13.md` — claim-unit routing, ⓐ확인 / ⓑ도전 / ⓒ신규 / 이미판정.

## Layers / 계층

1. **`facts_ledger.jsonl`** — append-only claim-unit ledger (fast intake).
   Fields: `id`, `date`, `tickers`, `claim`, `grade` (①②③), `verdict` (`grounded`|`partial`|…), `source_url`, `primary_urls[]`, `routes_to` (`dossier`|`paper`), `lead_route` (ⓐ확인|ⓑ도전|ⓒ신규|이미판정), `note`.
2. **`dossiers/`** — living fact MD sheets. **Merge new facts here first.**
   Seeded by copying `2026-09-23/` dossiers; that dated folder remains the historical snapshot.
3. **Dated memos `YYYY-MM-DD/*.md`** — source digests / factmaps (what came in today).
4. **HTML research papers** (`ai-infra/optical_*.html`) — **ONLY** touch when Lead marks **ⓑ challenge** or Kenneth explicitly asks. Do **not** rewrite full HTML on routine ledger/dossier updates.
5. **Collector (x-intake)** only drops factcheck JSON under `/workspace/x-intake/checks/`. **Lead owns disposition + archive** into this tree.

## Chat UX (Kenneth → Lead)

| Phrase | Meaning |
|--------|---------|
| `광통신 팩트: …` | New claim / fact to grade + ledger |
| `광통신 원장` | Show / summarize `facts_ledger.jsonl` + `CURRENT.md` |
| `광통신 도셰 갱신 <ticker>` | Merge ledger deltas into living dossier for ticker |

## Workflow (short)

```
x-intake factcheck JSON
  → Lead grades claim units + lead_route
  → append facts_ledger.jsonl
  → merge grounded/partial into dossiers/*.md (Ledger deltas)
  → dated memo YYYY-MM-DD/*.md
  → optional CURRENT.md one-line pointer
  → HTML paper ONLY on ⓑ or explicit ask
```

## Seed note

`dossiers/*.md` started as copies of `2026-09-23/dossier_*.md` and `mxl_sec_web_sources.md` on 2026-09-24. The `2026-09-23/` folder stays as the frozen snapshot.
