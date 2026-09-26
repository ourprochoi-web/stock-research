# SpaceX (SPCX) primary-source fact pack (as of 2026-09-26)

Grades: ① = EDGAR/company · [derived] = my arithmetic on ① numbers · [추론] = inference.
EDGAR CIK **0001181412** (SPACE EXPLORATION TECHNOLOGIES CORP, FYE 12/31). Originals are saved in this folder.

Documents used
| Short name | Form · filed | URL |
|---|---|---|
| ER-Q2 | 8-K Ex.99.1 · 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm |
| 10Q-Q2 | 10-Q (period 2026-06-30) · 2026-08-04 | https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm |
| 8K-0814 | 8-K Items 2.01/3.02 (Cursor close) · 2026-08-14 | https://www.sec.gov/Archives/edgar/data/1181412/000162828026056945/spcx-20260814.htm |
| 424B4 | IPO prospectus · 2026-06-12 | https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm |
| SX-F14 | spacex.com CMS API (company source) · fetched 2026-09-26 | https://content.spacex.com/api/spacex-website/missions/starship-flight-14 |

**8-Ks since 2026-08-29: none.** The latest 8-K is 8K-0814. Checked in `data.sec.gov/submissions/CIK0001181412.json` (saved as `submissions.json`).

## Q2 2026 (quarter ended 2026-06-30). Source: ER-Q2 "Second Quarter Financial Highlights" and statements, with 10Q-Q2 notes

| Item | Verdict | Original |
|---|---|---|
| Revenue | ① | **$7,814M** (+92% YoY from $4,071M). Q1'26 $4,694M |
| Space segment | ① | $962M. Launch services $648M + launch & development $314M. Op loss −$542M |
| Connectivity (Starlink) | ① | **$4,291M**: consumer $2,485M + enterprise & government $1,806M. Op income $1,656M. 12.0M subscribers. ARPU $66 (Q2'25: $85) |
| AI segment | ① | **$2,561M**: advertising $367M + AI solutions & infra $2,194M. Op loss −$1,257M. Segment adj. EBITDA +$1,146M. 1.4 GW nameplate compute |
| AI = 32.77% of revenue | ✅ | $2,561M / $7,814M = 32.77% [derived] |
| Capex ~2x revenue | ⚠ | Capex **$18,369M / revenue $7,814M = 2.35x** (H1: $28,476M / $12,508M = 2.28x). The AI segment alone spent $15,828M, which is 6.2x AI revenue |
| AI revenue 59.5% from a single customer | ✅ (derived) | The 10-Q says **Customer B = 19.5% of consolidated Q2 revenue**, "relates to the AI segment". 19.5% × $7,814M / $2,561M = **59.5%** [derived; not stated directly]. **Customer A = 18.3%** (all three segments) |
| 90-day termination | ✅ | "cloud services agreements … after an initial period inclusive of capacity ramp … **may be terminated by either party upon 90 days' notice**" (10Q-Q2 Risk Factors, p.51) |
| Net loss | ① | −$541M. Adj. EBITDA $3,538M. D&A $2,848M. SBC $831M |
| OCF | ① / [derived] | H1 $3,466M. Q1 $1,047M (424B4 "Summary of Cash flows") → **Q2 ≈ $2,419M** |
| FCF (OCF − capex) | [derived] | **Q2 ≈ −$15.95B**. H1 −$25.0B |
| Cash | ① | Cash $93,522M + marketable securities $6,487M = **$100.0B**. Undrawn $5.0B credit facility |
| Debt | ① | **$38,433M principal**. Carrying debt + finance leases $2,525M current + $36,839M non-current. **Related-party debt $13.3B** ($2,039M current + $11,290M non-current). $25B IG notes (5.35–6.65%, WAC 5.855%, 2031–2056) |
| Backlog | ① | $47,461M. ~56% within 1 year. Deferred revenue $14,286M |
| Shares | ① | 10-Q cover (2026-07-28): Class A **7,696,293,669** + Class B **5,485,486,276** = 13.18B. **Cursor close on 8/14 added 389,289,254 + 1,752,426 Class A** (plus 29.1M RSUs and 44.4M options assumed) → ≈13.57B [derived] |
| Guidance | ❓ | No numeric guidance in ER-Q2 or 10-Q. Tried the sec.gov Ex.99.1 above and `ir.spacex.com` (HTTP 403 to curl) |

Market cap [derived]: Yahoo `query1.finance.yahoo.com/v8/finance/chart/SPCX` close 2026-09-25 = **$148.68** (IPO $135.00).
- 13.18B shares → $1.96T.
- Including the Cursor shares (≈13.57B) → **≈$2.02T**.

## Lock-up schedule (424B4 "Shares Eligible for Future Sale", p.259–260)
| Archive claim | Verdict | Prospectus text |
|---|---|---|
| 2026-09-24: 328.4M | ✅ | "September 24, 2026 (105th day) — Up to 328.4 million … 7%" |
| **2026-10-09: ~1.3B** | ⚠ | **Oct 9 (120th day) = up to 328.4M.** The **1.3B (28%)** tranche is "the second full trading day … following the public release of our quarterly financial results for the quarter ended **September 30, 2026**". That date is not fixed |
| 2026-12-08: ~798M | ✅ (conditional) | "Up to (i) 328.4M if the Additional Release Shares were released … or (ii) **up to 797.6M** if not". The Additional Release needed a close ≥ 130% × $135 = **$175.50** on 5 of the 10 trading days ending on the first earnings date (2026-08-04). Yahoo closes 7/22–8/4 were $108–125, so the release was **not triggered** and **797.6M applies** [derived] |
| Omitted from the claim | ① | Before Q3 earnings: Oct 24 +328.4M. Earlier releases: Aug 6 (2nd trading day after Q2 ER) 911.5M · Aug 20 319.0M · Sep 9 319.0M · Sep 10 59.1M (affiliates). Then extended lock-up tranches from Q4'26 ER to Q2'27 ER (351.9M / 176.0M steps). **Musk ≈6.4B shares on 2027-06-12** |

## Starship Flight 14
| Claim | Verdict | Original |
|---|---|---|
| 2026-09-28 | ✅ | "The 14th flight of Starship is preparing to launch **as soon as Monday, September 28, pending regulatory approval**. The 75-minute launch window will open at 7:15 a.m. CT." It is the first **orbital** attempt: 26 Starlink V3 satellites, ~275 km, ~6 orbits. Source SX-F14, saved as `spacex_api_flight14.json`. The upcoming-tiles API (`spacex_api_upcoming.json`) still has `launchDate: null` |
| Flight 13 | ① | Flown in July. Per ER-Q2 it met all objectives. Per SX-F14 the booster made a hard splashdown (8 of 13 landing-burn engines relit) |
