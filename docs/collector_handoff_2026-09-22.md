# Collector → Lead handoff (2026-09-22)

## Roles
- **Collectors** (`x-intake Bot`, `youtube-wiki Bot`): pull + 1st triage only. No J2, no brain edits, no git commit.
- **Lead** (`Grok Bot`): synthesize, intake ids, routing, brain updates, Kenneth-facing judgment disposition.
- **Kenneth**: execution sizing; interim git push of lead drafts until lead has repo write.

## Report path (Kenneth 2026-09-22)
Collectors dual-report:
1. **User chat** — short summary each collection/summary cycle
2. **Grok Bot** — `SendToAgent` priority with full triage fields

Lead still owns keep/drop disposition and archive intake drafts.

## Required fields (to lead)
`date | source (handle or channel+URL) | claim summary | tickers | keep/drop | grade_hint | intake draft line`

## Archive rule
Chat-only ≠ archived. Lead must write kept items to `intake/user.jsonl` or `collected.jsonl` (+ `files/`) before routing.

## Cadence (interim)
- Stabilize X/YouTube bots before Telegram automation.
- X A-tier each pull; `USAnt_IDEA` weekly only.
- X login target: x-intake box; interim relay via lead box `@KenChoiSwift`.

## Git (interim)
- Actions: existing auto-collect commits.
- Lead: draft intake/brain patches.
- Kenneth: review + push until lead write exists.

## Collectors (updated)
- `x-intake Bot` — X whitelist
- `youtube-wiki Bot` — YouTube
- `telegram-intake Bot` — public Telegram via `t.me/s/{handle}`; seed `aetherjapanresearch` in `intake/requests/telegram_channels.txt`
