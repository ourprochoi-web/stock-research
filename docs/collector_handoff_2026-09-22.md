# Collector → Lead handoff (2026-09-22; ops lock 2026-09-23)

## Roles
- **Collectors** (`x-intake`, `youtube-wiki`, `telegram-intake`): **collection only**. No investment keep/drop, no A/B grades, no thesis links, no J2, no brain edits, no git.
- **Lead** (`Grok Bot`): disposition, priced-in vs variant read, risk/return synthesis, intake ids, routing, brain updates, Kenneth-facing judgment.
- **Kenneth**: execution sizing; market study via rich collector digests.

## Dual report (Kenneth 2026-09-23)
1. **Kenneth chat** — **maximum-detail factual summary** (study use): who / what / when / numbers / links / claim gist. No thin headlines. No buy/sell judgment.
2. **Lead** — `SendToAgent` priority with **full packet** (raw text or close paraphrase, URL, timestamp, handle/channel). Lead alone decides archive keep/drop.

## Required fields (to lead)
`date | source (handle or channel+URL) | full claim / excerpt | tickers if named | media links`

## Archive rule
Chat-only ≠ archived. Lead writes kept items to `intake/user.jsonl` or `collected.jsonl` (+ `files/`) before routing.

## Cadence
- X A-tier each pull; `USAnt_IDEA` weekly only.
- Telegram: whitelist in `intake/requests/telegram_channels.txt` via `t.me/s/{handle}`.
- X login target: x-intake box; interim relay via lead box `@KenChoiSwift`.

## Git
- Lead may commit/push with repo write PAT when Kenneth has granted it.
- Actions: existing auto-collect commits continue.

## Collectors
- `x-intake Bot` — X whitelist
- `youtube-wiki Bot` — YouTube
- `telegram-intake Bot` — public Telegram `t.me/s/`
