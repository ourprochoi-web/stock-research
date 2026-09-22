# Judgment protocols (2026-09-23)

Structure / ops lock for Lead judgment. Complements `CLAUDE.md` §J · `brain/README.md` routing schema · `docs/collector_handoff_2026-09-22.md`.
Does **not** invent market numbers or portfolio weights.

---

## 1. Edge three-liner (`priced_in` / `variant` / `breaks_if`)

Every **new** `routing.jsonl` row with `kind` in `{observation, judgment}` (and any route that asserts an edge) must carry:

| field | content |
|---|---|
| `priced_in` | What market consensus already prices (multiple → implied earnings/growth, narrative already in the tape). |
| `variant` | Our different causality and/or time-axis read — the wedge vs consensus. |
| `breaks_if` | The observation that kills this variant / edge (concrete, checkable). |

**Disposition rule:** if `priced_in` ≈ our view (variant collapses into consensus), set `action` to **`no-edge`** or digest-only. Do not escalate size, thesis status, or “stronger same-story” language.

Id / soft-target conventions: prefer `r-YYYYMMDD-NN`; letter suffixes (`x`, `tg`) are legacy 09-22 only; soft targets use `parked: "open|regime|portfolio|events"` — never those bare strings inside `routed[]`. Detail: `brain/README.md`.

---

## 2. Flow vs thesis conflict — hold rule (template)

When **flow / positioning** (foreign/institution net, 13F, short interest, breadth) conflicts with the **open thesis** on a held name:

1. **Log the flow as observation** in `routing.jsonl` (grade typically ③ or datasource grade; claim states window + size). Attach intake id.
2. **Do not change size** (no trim / add / hedge instruction) solely on that flow print.
3. **Hold size until** one of:
   - an **N-day** re-check window you name in `action` / `breaks_if` (e.g. “N=3 trading days of same-direction flow”), or
   - a **pre-committed gate event** already in `events.json` / portfolio precommits (earnings, Micron G1, etc.).
4. Thesis `status` / `basis` stay unless the conflict itself falsifies a thesis sentence (then ⓑ challenge with its own three-liner).

**Example (logging without size change):** `r-20260922-x2` — SKH 09-22 agent-flow print (foreign/institution/retail net sells) recorded as ⓐ confirmation of *supply observation* only; action = no position impact; juxtaposed with 10/1 Micron gate. Thesis wording unchanged. Use this shape whenever flow fights the earnings/thesis anchor.

Template action line:

```
action: "hold size · log flow only · recheck after {N}d or gate {event_id/date}"
```

---

## 3. Contra book

For **top exposures** (portfolio core / largest factor sleeves in `portfolio.exposures`), Lead must keep **one live `contra_claim`** either:

- as an item in `brain/open.json` (`what` starts with or includes `contra_claim:` + the opposing sentence + what would make it win), **or**
- as a dated note in the relevant thesis `log[]` / routing judgment that names `contra_claim`.

Purpose: top risk is not unopposed narrative. Refresh when exposure rank changes or the contra is resolved (then delete/retire — do not leave stale contras).

---

## 4. J2 must include regime ⓪ + portfolio ⑥

On ticker / position / timing questions, answer shape is (`CLAUDE.md` §J2):

- **⓪** regime one-liner from `regime.one` (+ `changes_if` if relevant)
- ① as-of date · ② what price already assumes · ③ today’s info same/opposite · ④ cost of each choice · ⑤ grade
- **⑥** portfolio impact from `portfolio.exposures` (which sleeve, concentration, single-falsifier dollars if already measured — **do not invent new weights**)

Missing ⓪ or ⑥ = incomplete J2. Judgment events remain falsifiers, not entry calendars.

---

## 5. Prediction resolve cadence

`kind:"prediction"` rows in `routing.jsonl` carry `resolve_by` (and usually `confidence`). Cadence:

| when | what |
|---|---|
| **Session start / daily skim** | List predictions with `resolve_by` ≤ today and missing `outcome` / `judged_by`; resolve or explicitly slip `resolve_by` with reason in a follow-on routing line. |
| **Weekly regime review** | Sweep near-due predictions; attach lessons that affect `regime` narratives. |
| **Monthly audit** | Score hit rate only (맞음/틀림/부분). No “improvement ideas” — measurement only (`docs/backlog.md` 「예측 채점」). |

Resolve fields: set `outcome` (or `verdict_result`) + `judged_by` (resolving routing id) + optional `lesson`. Unresolved past-due predictions are open risk, not decoration.
