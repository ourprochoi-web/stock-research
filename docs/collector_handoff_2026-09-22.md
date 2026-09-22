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

### `user.jsonl` shape (Lead write)
- Must include **`text`**: raw excerpt or faithful paraphrase of the claim body. Title/subject alone is not enough.
- Typical keys: `{id, date, channel, source, title, text, grade_hint?, used_by?}` — see `intake/README.md`.
- **Never put KEEP / DROP / A / B in `subject` (or title).** Disposition lives in Lead routing (`verdict` / `action`), not in intake subject lines. Collectors must not invent those tags either.

## Lead disposition checklist (before / with routing)
For each kept observation or judgment, Lead fills the edge three-liner (see `brain/README.md` routing schema · `docs/judgment_protocols_2026-09-23.md`):

| field | ask |
|---|---|
| `priced_in` | What does consensus already price? |
| `variant` | Where is our causality / time-axis read different? |
| `breaks_if` | What observation kills this variant / edge? |

If `priced_in` ≈ our view → `action: no-edge` (or digest-only). Soft targets use `parked: "open|regime|portfolio|events"`, not those strings inside `routed[]`.

## Cadence
- X A-tier each pull; `USAnt_IDEA` weekly only.
- Telegram: whitelist in `intake/requests/telegram_channels.txt` via `t.me/s/{handle}`.
- X login target: x-intake box; interim relay via lead box `@KenChoiSwift`.

## Git
- Lead may commit/push with repo write PAT when Kenneth has granted it.
- Actions: existing auto-collect commits continue.
- **This ops-lock doc stream does not invent portfolio weights or push by itself.**

## Collectors
- `x-intake Bot` — X whitelist
- `youtube-wiki Bot` — YouTube
- `telegram-intake Bot` — public Telegram `t.me/s/`
