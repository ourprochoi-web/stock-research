# RKLB + Iridium primary-source fact pack (as of 2026-09-26)

Grades: ① = EDGAR/company filing · [derived] = my arithmetic on ① numbers · [추론] = inference.
Every original is saved in this folder (`*.htm`, `submissions.json`, `companyfacts.json`, `yahoo_*.json`).
EDGAR: RKLB CIK 0001819994 · IRDM CIK 0001418819. I fetched everything with UA `Ken Choi kenchoi@keywestaim.com`. No sec.gov host was blocked.

Documents used
| Short name | Form · filed | URL |
|---|---|---|
| ER-Q2 | 8-K Ex.99.1 · 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000061/rklb-08102026ex991.htm |
| 10Q-Q2 | 10-Q (period 2026-06-30) · 2026-08-10 | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000062/rklb-20260630.htm |
| 8K-0629 | 8-K Item 1.01 + Ex.99.1 · 2026-06-29 | https://www.sec.gov/Archives/edgar/data/1819994/000175392626001085/g085783_8k.htm |
| 8K-0813 | 8-K Ex.99.1 (ATM) and Ex.99.2 (HSR/FCC) · 2026-08-13 | https://www.sec.gov/Archives/edgar/data/1819994/000175392626001463/g085846_ex99-2.htm |
| 8K-0915 | 8-K Ex.99.1 · 2026-09-15 | https://www.sec.gov/Archives/edgar/data/1819994/000175392626001769/g085951_ex99-1.htm |
| 8K-0121 | 8-K Items 7.01/8.01 · 2026-01-22 | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000004/rklb-01212026ex991.htm |
| 8K-0520 | 8-K (May ATM, $3.0B) · 2026-05-20 | https://www.sec.gov/Archives/edgar/data/1819994/000181999426000045/rklb-20260520.htm |
| IRDM-vote | IRDM 8-K Item 5.07 · 2026-09-24 | https://www.sec.gov/Archives/edgar/data/1418819/000095010326014464/dp253851_8k.htm |
| IRDM-lit | IRDM 8-K Item 8.01 · 2026-09-18 | https://www.sec.gov/Archives/edgar/data/1418819/000095010326014197/dp253526_8k.htm |
| DEFM14A | IRDM proxy/prospectus · 2026-08-26 | https://www.sec.gov/Archives/edgar/data/1418819/000175392626001637/g085903_def14am.htm |
| IRDM-0707 | IRDM 8-K (Aireon close) · 2026-07-07 | https://www.sec.gov/Archives/edgar/data/1418819/000110465926081335/tm2619278d14_8k.htm |

---

## A1. Q2 2026 (quarter ended 2026-06-30)
| Claim | Verdict | Original (① unless tagged) | Where |
|---|---|---|---|
| Revenue $234.1M, +62% YoY | ✅ | $234,066k vs $144,498k → +62.0% | ER-Q2 income statement. 10Q-Q2 MD&A |
| Space Systems $189.5M | ✅ | $189,480k (+94% YoY, "spacecraft manufacturing growth **and acquisitions**") | 10Q-Q2 Note 18 Segments (p.32). MD&A |
| Launch Services $44.6M | ✅ | $44,586k, **−4% YoY** (Q2'25 $46,646k). Reason given: HASTE revenue recognized over time | 10Q-Q2 Note 18. MD&A |
| Backlog $2.36B | ✅ | $2,355,949k. **~45% recognized within 12 months, 55% beyond** | 10Q-Q2 Note 2 "Backlog" (p.12) |
| Backlog split launch ~40% / space systems ~60% | ❓ | Not in the 10-Q or in ER-Q2. Probably from the earnings deck or call. Tried: sec.gov 8-K 0001819994-26-000061 (Ex.99.1 only, no deck), `investors.rocketlabcorp.com` (curl returned HTTP 000, no connection) | — |
| GAAP gross margin | ① | $84,576k / $234,066k = **36.1%** [derived] | ER-Q2 |
| Non-GAAP gross margin | ① | **41.5%** ($97,033k) | ER-Q2 reconciliation |
| Adjusted EBITDA | ① | **−$8.833M** (Q2'25 −$27.584M). H1 −$20.584M | ER-Q2 reconciliation |
| Net loss | ① | −$49.258M. EPS −$0.08. Basic WASO 629,681,803 | ER-Q2 |
| Operating cash flow | ① / [derived] | H1 −$134.407M. Q1 −$50.332M (XBRL) → **Q2 −$84.1M** | ER-Q2 cash-flow statement. companyfacts |
| Capex (PP&E + software) | ① / [derived] | H1 $53.112M. Q1 $27.065M → **Q2 $26.0M** | same |
| FCF (OCF − capex) | [derived] | **Q2 −$110.1M**. H1 −$187.5M | — |
| Cash & liquidity 6/30 | ① | Cash and equivalents $2,129.5M + marketable securities $258.1M (current $172.7M, non-current $85.4M) = **$2,387.6M**. Restricted cash $8.4M. Convertible notes $13.1M | ER-Q2 balance sheet. 10Q-Q2 Liquidity |
| Share count | ① | Common outstanding 598,180,438 (6/30) and **598,350,482 (8/5, 10-Q cover)**. Plus Series A preferred **40,951,250**, which is treated as common for EPS | 10Q-Q2 cover. Balance sheet |
| Customer concentration | ① | **Government customer = 42% of H1'26 revenue**. MDA = 11% of AR | 10Q-Q2 Note 2 "Concentration" (p.12–13) |
| Contingency | ① | MDA 17-bus contract is delayed, so the customer may claim **liquidated damages**. Net amount "not possible to determine" | 10Q-Q2 Note 2 |

## A2. Q3 2026 guidance (ER-Q2, "Third Quarter 2026 Guidance")
| Claim | Verdict | Original |
|---|---|---|
| Revenue $250–265M | ✅ | $250M–$265M |
| GAAP GM 29–31% | ✅ | 29%–31%. **Down from Q2 actual 36.1%** |
| Non-GAAP GM 35–37% | ✅ | 35%–37%. **Down from Q2 actual 41.5%** |
| Adj. EBITDA guide | ① | **Loss of $17M–$23M** (worse than Q2's −$8.8M) |
| Other | ① | GAAP opex $143–149M. Non-GAAP opex $121–127M. Net interest income $21M. SBC $18–20M. **Basic WASO 641M, including ~41M preferred** |

## A3. Iridium (IRDM) acquisition
| Claim | Verdict | Original | Where |
|---|---|---|---|
| $27 cash + RKLB stock with collar. Nominal $54/share | ✅ | $27.00 cash plus an Exchange Ratio: **0.4000 if RKLB VWAP ≤ $67.50**; $27/VWAP between $67.50 and $112.50; **0.2400 if ≥ $112.50**. VWAP = 10 trading days ending 2 days before close | 8K-0629 Item 1.01 "Merger Consideration" |
| EV ~$8B | ✅ | "enterprise value for Iridium of approximately $8.0 billion" | 8K-0629 Ex.99.1. 10Q-Q2 Liquidity |
| Special meeting 2026-09-24: ~99.6% of votes cast, ~81.0% of outstanding | ✅ | For 85,862,105 · Against 318,415 · Abstain 67,862 · record-date shares 105,981,552. → 99.55% of all votes incl. abstain (99.63% of for+against). **81.02% of outstanding**. Quorum 81.38% | IRDM-vote Item 5.07 |
| Target close mid-2027 | ✅ | "expected to close in mid-2027". **Outside date 2027-06-28**, extendable to 2027-09-28 and 2027-12-28 | IRDM-vote. 8K-0629 "Termination" |
| Remaining conditions | ① | FCC consent to transfer of control (possible **Team Telecom** referral). Other foreign-investment, satellite and telecom approvals. **NISPOM/DCSA**. S-4 effective (EFFECT 2026-08-26). No MAE | DEFM14A "Regulatory Approvals Required" (p.15, p.96) |
| HSR expired | ✅ | Expired 11:59 p.m. ET **2026-08-12**. FCC applications filed 2026-08-10 | 8K-0813 Ex.99.2 |
| Iridium term loan ~$1.78B, change-of-control amendment | ✅ | **$1.775B** outstanding at 6/30. Amendment signed **2026-09-15**. Rocket Lab USA gives an **unsecured guarantee** at close | 8K-0915 Ex.99.1 |
| Sept-2026 ATM ~$1.94B / 29.3M shares | ✅ | "approximately $1.944 billion gross … issuance of 29.3 million shares". Implied average ≈ **$66.35/share** [derived] | 8K-0915 Ex.99.1. Program $1,944,369,826 per 8K-0813 Ex.99.1 |
| $3.6B bridge terminated | ✅ | "terminated its $3.6 billion debt commitment" | 8K-0915 Ex.99.1 |
| Termination fee | ① | **$223.62M**, payable by Iridium in specified cases (superior proposal, recommendation change) | 8K-0629 Item 1.01 |
| Litigation | ① | **3 NY state-court stockholder suits** (Index 655039/2026, 655037/2026, 626928/2026) plus demand letters. They allege disclosure defects and seek an injunction | IRDM-lit Item 8.01 |
| Iridium extra debt | ① | Aireon buyout closed 2026-07-02 for $366.7M. Seller loan **$183.36M** (0%, 1-yr, **mandatory repayment on change of control**) plus consolidated Aireon term loans **$154.7M** | IRDM-0707 Item 1.01 |
| Iridium 2025 financials | ① | Revenue $871.7M. OEBITDA $495M (57%) | 8K-0629 Ex.99.1 |
| Premium / fairness | ① | 24% premium to IRDM close of $43.52 on 6/26. Evercore DCF for **RKLB: $46.23–$102.45/share** vs $84.54 on 6/26 | DEFM14A "Reasons" / "Opinion of Evercore" |

## A4. Neutron
| Claim | Verdict | Original | Where |
|---|---|---|---|
| 2026-01-21 stage-1 tank hydrostatic rupture | ✅ | "qualification testing of the Stage 1 tank overnight resulted in a rupture during a hydrostatic pressure trial". Next tank already in production | 8K-0121 Items 7.01/8.01, Ex.99.1 |
| Debut NET Q4 2026 or later | ✅ (wording) | "Production of the Stage 1 tank is currently aligned with the target **delivery of Neutron to the launch pad in Q4 2026**. While the **window for an end-of-year launch date is narrowing** … Exact launch timing will also depend on the outcome of **first stage qualification and other critical tests occurring later in 2026**." The filing targets pad delivery in Q4, not launch, so first flight in 2027 is consistent with the text [추론] | 10Q-Q2 MD&A "Recent Developments — Neutron Update". ER-Q2 bullet |
| Q2 call language | ❓ | No transcript on EDGAR. Tried `investors.rocketlabcorp.com` (no connection, HTTP 000). `rocketlabcorp.com/updates/` and `/launch/neutron/` load their text by JS, so the static HTML had nothing | — |
| Archimedes test count | ❓ | 10-Q says only "continued progress on Archimedes engine testing". No count in any EDGAR doc here (grep of all saved texts). Company hosts as above | 10Q-Q2 MD&A |
| LC-3 | ❓ | No "Launch Complex 3"/"LC-3" string in 10Q-Q2, ER-Q2 or the 8-Ks. ER-Q2 mentions a new **LC-4** (GHOST, Kodiak, Alaska, suborbital debut 2027) | ER-Q2 bullets |

## A5. Dilution: common shares outstanding (XBRL `CommonStockSharesOutstanding`, ①)
| Date | Common | + Series A preferred (as-converted) | Total |
|---|---|---|---|
| 2025-06-30 | 479,326,649 | 45,951,250 | 525.3M |
| 2025-09-30 | 496,224,616 | 45,951,250 | 542.2M |
| 2025-12-31 | 543,574,552 | 45,951,250 | 589.5M |
| 2026-03-31 | 575,767,500 | 45,951,250 | 621.7M |
| 2026-06-30 | 598,180,438 | 40,951,250 | 639.1M |
| 2026-08-05 (cover) | 598,350,482 | 40,951,250 | 639.3M |
| after Sept ATM [derived] | ≈627.65M (+29.3M) | 40,951,250 | **≈668.6M** |

- Total shares rose about **+27%** from 6/30/25 to after the September ATM [derived].
- 2026 ATM sales ①:
  - Q1: 6,358,097 shares, $445M net.
  - Q2: 8,152,223 shares, $1,068M net. May-program sales averaged about $135.6/share (7,783,458 shares, $1,055.6M gross).
  - Q3: 29.3M shares, $1.944B gross.
  - These all come from the $1.0B March program and the $3.0B May program (8K-0520). The August program carried over the May remainder.
- **Collared forwards: 7,451,200 more shares** sold forward under the March program. They mature **April 2028** for $474M–$642M of proceeds, and none has been received yet (10Q-Q2 Note 12).
- **Iridium stock consideration** [derived]: ratio × 105.98M IRDM shares.
  - At $73.95 the ratio is 0.3651, which means **≈38.7M new RKLB shares**.
  - At the $67.50 floor or below it is 0.40, or ≈42.4M shares.
  - At the $112.50 cap it is 0.24, or ≈25.4M shares.
  - Assumed Iridium RSUs come on top.
- Pro forma total after close is ≈707M at the current price [추론]. That is about **+35% vs 6/30/25**.

## C. Valuation (price: Yahoo `query1.finance.yahoo.com/v8/finance/chart/RKLB`, close 2026-09-25 = **$73.95**. 52-week range $37.57–$151.00. File `yahoo_RKLB.json`)
- **Market cap** ≈ $73.95 × 668.6M (627.65M common + 40.95M preferred) = **$49.4B**. Common only = $46.4B.
- **Cash** ≈ $2,387.6M (6/30) + $1,944M ATM gross = $4.33B. Commissions and Q3 burn are not netted, so this is an upper bound.
- **Debt + leases** ≈ $29.3M (convertible notes $13.1M + borrowings $1.7M + non-current finance leases $14.5M).
- **EV ≈ $49.44B − $4.33B + $0.03B = $45.1B.**
- **TTM revenue** (Q3'25 → Q2'26) = $155.08M + $179.65M (FY25 $601.80M − 9M $422.15M) + $200.35M + $234.07M = **$769.1M** (XBRL).
- **EV/Sales TTM = $45.1B / $0.769B ≈ 58.7x.** On the 6/30 balance sheet with 639.1M shares: EV $44.9B → 58.4x.
- Against the Q3 guidance midpoint annualized ($257.5M × 4 = $1.03B): ≈44x.
- This is RKLB standalone. The ATM cash is earmarked for Iridium, so a pro forma EV has to add ≈$2.9B cash paid, Iridium's $1.775B TL + Aireon debt, and ≈38.7M shares [추론].
- **IRDM price $48.75** (2026-09-25) vs $54 notional. RKLB at $73.95 is inside the collar, so the stock leg is worth $27. The spread is **+10.8%** with about 9 months to close.
- The collar floor is $67.50. RKLB traded between $62.55 and $67.82 from 2026-08-31 to 09-17. **Below $67.50 the stock leg is worth less than $27.**
