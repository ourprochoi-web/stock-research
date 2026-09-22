# Optical / copper connectivity chips dossier — SMTC · CRDO · MXL · ALAB · MTSI

- **As-of / staging date:** 2026-09-23 (KST)
- **Scope:** Semtech (SMTC), Credo (CRDO), MaxLinear (MXL), Astera Labs (ALAB), MACOM (MTSI)
- **Primary sources:** archive `brain/facts.json` · `brain/entities.json` · `ai-infra/optical_interconnect_layer.html` · `ai-infra/optical_valuechain_9.html` · `intake/files/financials/` · `intake/files/prices_daily/` · `data/13f/2026Q2/`
- **MXL fill:** was **archive-empty** — built 2026-09-23 from SEC companyfacts + 10-Q/8-K; optical guide labeled **WEB/②**. See `mxl_sec_web_sources.md`.
- **Rules:** no buy/sell share counts · no stops · edge cards only · **WEB vs SEC labeled**.

---

## Executive comparison (parent)

| Axis | SMTC | CRDO | MXL | ALAB | MTSI |
|------|------|------|-----|------|------|
| **AI optical vs copper AEC purity** | Mixed SI: FiberEdge/Tri-Edge **optical drivers/TIA** + CopperEdge **AEC** in one SI seg (LPO alone **not** disclosed) | Dual: **AEC/Zero-Flap copper** today + **optical DSP/PIC** growth axis (co. FY27 optical $600M+ guide ②) | **Rising optical purity inside Infra**: Keystone **PAM4 DSP 800G** ramp; Infra 50% of Q2 rev (**SEC**). Still broadband/connectivity ballast | **Copper-scale purity** (PCIe/CXL retimer, AEC/CopperEdge) — **not** optical DSP/laser layer | **Optical PHY analog** (drivers/TIA) + broad RF/industrial — optical is real but **not** majority of TTM |
| **Margin quality** | Consol GPM **53.8%** hides SI GPM **65.3%** (①). Consol OPM thin **5.5%** (reported 2.1% w/ impairment) | GPM **67.1%** / OPM **31.7%** best OPM in set (①) — quality high but SBC-diluted | GAAP GPM **~57.5% TTM** solid; GAAP OPM **still negative TTM**; **Non-GAAP OPM 22.3%** Q2 (SEC 8-K) — quality = non-GAAP dependent | GPM **75.1%** best; OPM **22.8%**; R&D/rev **34.6%** eats GPM→OPM bridge | GPM **56.5%** / OPM **18.1%** (①) — stable mid; less explosive |
| **SBC / inventory red flags** | SBC/rev Q **9.1%** OK; inv +**20%** < sales growth | **SBC 18.4%** of rev (T2); inv +**168%** vs sales +115% (T5); OCF/EBIT **0.75×**; top cust **43%** | SBC/rev Q **16.3%** elevated; inv +**23%** < sales +55% (cleaner than CRDO); AR **−52% YoY** (watch mix) | SBC **15.9%**; inv +**94%**; **AR +691%** (largest BS flag in set) | SBC/rev ~**6.2%** (Q end Jul-03) low; inv +**~31%** moderate |
| **Residual edge rank (this sleeve)** | **#2** | **#3** | **#1** | **#5** | **#4** |
| **Why rank** | SI understated by consol; P/S 13× cheaper than ALAB/CRDO; but mixed AEC/optical | Franchise + growth/valuation (P/S÷g **16.8**) already known; SBC/inv open | Archive gap + optical DSP inflection not fully in peer set; P/S ~14× on +55% with Infra +145%; GAAP loss still discounts | Highest purity **copper** not optical; P/S **42×**; Whale Rock 6% book; AR flag | “Can’t-delete” driver/TIA physics but RF conglomerate dilution; Whale Rock holds but trimmed sh |

**Purity continuum (optical AI DSP/analog):** MXL (PAM4 DSP) ≳ MTSI (driver/TIA) ≳ SMTC (driver/TIA+AEC mix) > CRDO (AEC+optical DSP dual) ≫ ALAB (copper retimer).  
**Purity continuum (copper AEC/retimer):** ALAB ≈ CRDO > SMTC > MXL ≈ MTSI.

Snapshot valuation (prices Yahoo chart ~2026-09-22; shares SEC latest; archive TTM facts asof **2026-09-11** except MXL **2026-09-23**):

| | SMTC | CRDO | MXL | ALAB | MTSI |
|--|-----:|-----:|----:|-----:|-----:|
| Price (WEB) | $173.64 | $191.23 | $85.73 | $365.86 | $278.03 |
| Mcap ~ | $16.2B | $35.9B | $7.8B | $63.5B | $21.2B |
| Rev TTM $M | 1,174 | 1,591 | 569 | 1,202 | 1,164 |
| P/S | ~13.8 | ~22.6 | ~13.7 | ~52.8 | ~18.2 |
| YoY (facts/Q) | +32.7% | +114.7% | +55.2% | +104.5% | +35.8% |
| P/S÷g (approx) | ~42 | ~20 | ~25 | ~51 | ~51 |
| 6m price (chart prev→now, WEB) | 73.6→174 (~+136%) | 103→191 (~+85%) | 17→86 (~+5×) | 116→366 (~+3×) | 219→278 (~+27%) |

---

# 1. SMTC — Semtech

## 1. Business
- **Products:** Signal Integrity — FiberEdge/Tri-Edge **optical drivers & TIA**, CopperEdge **AEC**; plus IoT/LoRa (non-AI ballast). (`entities` ②; optical_interconnect T3)
- **AI role:** LPO/linear optical adjacent **analog front-end** + in-rack copper AEC. Archive warns: **SI ≠ LPO alone** — AEC+optical lumped; LPO revenue **not** broken out.
- **Customers:** Top customer **15%** of rev (10-Q ① asof 2026-07-26) — better diversification than CRDO.
- **Moat:** Analog SI IP in module BOM that DSP-removal (LPO) still needs; CopperEdge if copper reach extends.
- **Competitors:** CRDO (AEC+DSP), MTSI (drivers/TIA), Broadcom/Marvell DSP, ALAB (retimer/AEC).

## 2. Financials (source · date)
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM | **$1,174M** | BRAIN facts ① SEC XBRL · **2026-09-11** |
| GPM TTM / SI seg | **53.8%** / SI **65.3%** | facts ①; SI 10-Q seg **2026-07-26** |
| OPM TTM | **5.5%** (reported **2.1%** w/ $42M impairment) | facts ① |
| Rev growth YoY | **+32.7%**; SI seg **+64.4%**, SI share **36.9%** | facts ① |
| Latest Q rev | **$341.9M** (Q ended ~2026-07-26) | facts / financials intake |
| SBC / rev Q | **9.1%** | facts ① |
| Inventory YoY / AR YoY | **+20.2%** / **+5.5%** | facts ① |
| OCF / EBIT Q | **1.4×** | facts ① |

## 3. Valuation + price move
| | |
|--|--|
| Archive mcap / P/S | **$15.6B** / **13.3×** (asof **2026-09-11**) |
| WEB refresh | Px **$173.64**, mcap ~**$16.2B**, P/S ~**13.8×** (09-22) |
| Archive daily | 2026-09-15 close **$150.57**; 09-02 **$133.85** |
| Move | 6m WEB ~**+136%** from ~$74; still **cheapest P/S** in connectivity chip subset vs ALAB/CRDO |
| P/S÷g | Archive **40.6** (chip-layer peer table) — not “cheap on growth” vs CRDO’s 16.8 |

## 4. Flow-positioning
- Tracked_price **false** in entities (less screen focus than CRDO/ALAB).
- Manager-7 overlap: portfolio.next notes SMTC as **same** vs manager list (r-31).
- 13F sample set (`data/13f/2026Q2` watchfunds): **no SMTC** in Whale Rock / Coatue top files scanned — positioning **not** crowded in that sleeve.
- Short-interest archive (`flows_daily/us_si`) is large-cap-only — **SMTC not in file** (thin).

## 5. Edge card
| | |
|--|--|
| **priced_in** | AI SI/LPO narrative + CopperEdge; consol print looks mediocre so segment story partially known after optical_interconnect T3. |
| **variant** | Consol GPM/OPM still **mask** SI 65% GPM / +64% growth; if SI mix → 40%+ of sales without GPM giveback, re-rate toward pure-play SI multiples without needing CRDO growth. |
| **breaks_if** | SI GPM **<62%** or SI share stalls **~37%**; CopperEdge loses to CRDO/ALAB; LoRa drag worsens OPM. |
| **residual** | **#2** — valuation + segment opacity leave wedge; purity mixed. |

## 6. Open questions
- LPO-only vs AEC split inside SI (never disclosed).
- Next-Q SI growth deceleration?
- Why institutions in our 13F sleeve underweight vs CRDO/ALAB.

---

# 2. CRDO — Credo

## 1. Business
- **Products:** SerDes IP, **AEC (Zero-Flap)**, optical **DSP**, SiPh **PIC** (Dust Photonics deal ②). (`entities`)
- **AI role:** Dominant **copper AEC** narrative + company-guided **optical DSP** as growth pillar — archive T1: “DSP goes away → Credo wins” **conflicts** with co. FY27 optical **$600M+** = Zero-Flap · PIC · optical DSP each **$100M+** (② IR).
- **Customers:** Top customer **43%** (10-Q ①) — concentration risk.
- **Moat:** SerDes + system-level AEC reliability (Zero-Flap); optical DSP attach.
- **Competitors:** Broadcom/Marvell DSP, ALAB retimers, SMTC CopperEdge, Ciena/Nubis entering AEC (valuechain T5).

## 2. Financials (source · date)
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM | **$1,591M** | facts ① **2026-09-11** |
| GPM / OPM TTM | **67.1%** / **31.7%** | facts ① |
| Rev growth YoY | **+114.7%** | facts ① |
| Latest Q | Rev **$479M**, GPM **64.5%**, OPM **25.2%** (asof **2026-08-01**) | facts ① |
| SBC / rev Q | **18.4%** (+148% YoY in cost story) — T2 | facts / interconnect ① |
| Inventory YoY | **+168.3%** (1.47× sales growth) — T5 | facts ① |
| AR YoY | **+59.4%** | facts ① |
| OCF / EBIT Q | **0.75×** | facts ① |
| Max daily drop | **−20.04%** on **2026-09-02** | facts ① |

## 3. Valuation + price move
| | |
|--|--|
| Archive mcap / P/S / P/S÷g | **$30.6B** / **19.3×** / **16.8** (best growth-adjusted in chip layer) · **2026-09-11** |
| WEB refresh | Px **$191.23**, mcap ~**$35.9B**, P/S ~**22.6×** |
| Move | 09-02 crash −20%; archive 09-15 **$150.99** → WEB ~$191 rebound; 6m ~**+85%** |
| Screen note | portfolio.next: Credo **B-dropout candidate** pending SBC-ex OPM check |

## 4. Flow-positioning
- entities `tracked_price: true`.
- Mizuho (③ **2026-09-21**): TP **$290→$245**, still “buy the dip” — demand-channel checks only (T5 log).
- 13F watchfunds: **no CRDO** line in Whale Rock Q2 file (thin on this sleeve).
- High retail/momentum sensitivity implied by −20% single day.

## 5. Edge card
| | |
|--|--|
| **priced_in** | Hypergrowth AEC + optical optionality; P/S÷g already **best** in layer; post-crash “SBC understood” partially. |
| **variant** | True open issue is **inventory/OCF** (T5) not margin; if inv growth < sales next Q **and** SBC/rev <18%, quality catch-up without needing new narrative. |
| **breaks_if** | Optical DSP share of optical revenue **falls** (T1 falsifier); inv stays >1.3× sales growth another Q; top customer loses design. |
| **residual** | **#3** — franchise strong, edge **compressed** by flags + ownership of story. |

## 6. Open questions
- AEC vs optical DSP revenue mix **this** year (guide is FY27).
- Contract liability almost nil — how to read channel inventory.
- SBC-ex OPM path into Nov FY27 Q2 print.

---

# 3. MXL — MaxLinear (**archive was empty**)

## 1. Business
- **Products:** **Keystone** 5nm PAM4 DSP (100G/lane) for **400G/800G** optical modules; roadmap **Rushmore** 1.6T (200G/lane), Washington TIA, Annapurna retimer; plus Broadband / Connectivity / Industrial SoCs. (**SEC** 10-Q business description; **WEB** call for product names)
- **AI role:** Optical **DSP** for pluggable AI optics — same “eraseable” layer as Marvell/Broadcom DSP, not “can’t-delete” laser. Infra market was **50%** of Q2 rev (**SEC**).
- **Customers:** Hyperscale via module OEMs (US/Asia) — **WEB** call. SEC revenue concentration: Customer A **16%** of Q2'26 net rev (Customer B <10% that Q) (**SEC** 10-Q).
- **Moat claim:** ~**40% lower power** vs competition on Keystone (**WEB** call — treat as company claim ②).
- **Competitors:** Broadcom, Marvell, Credo optical DSP; LPO path is a **threat** to DSP content.

## 2. Financials (source · date) — **SEC-built**
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM | **$568.9M** | SEC companyfacts frames Q3'25–Q2'26 · **2026-09-23** ① |
| GPM TTM | **~57.5%** | companyfacts ① |
| OPM TTM (GAAP) | **~−13.6%** | companyfacts ① |
| Q2'26 rev | **$168.8M** (+23% QoQ, **+55% YoY**) | 8-K EX-99.1 **2026-07-23** ① |
| Q2 GAAP GM / OM | **57.8%** / **−2.5%** | 8-K ① |
| Q2 Non-GAAP GM / OM | **59.5%** / **22.3%** | 8-K ① |
| Infrastructure | **$85.0M** (**50%**), **+145% YoY** (from $34.7M) | 10-Q Note · 8-K ① |
| Broadband / Connectivity / Industrial | $44.9M (27%) / $24.0M (14%) / $15.0M (9%) | 10-Q ① |
| SBC / rev Q2 | **16.3%** ($27.5M / $168.8M) | companyfacts ① |
| Inventory YoY | **+22.6%** ($105.5M) | companyfacts ① |
| AR YoY | **−51.8%** | companyfacts ① |
| Cash / LT debt | **$64.8M** / **$123.9M** (2026-06-30) | companyfacts ① |
| Q3'26 guide rev | **$210–220M** | 8-K ① |
| Optical DC FY26 guide | **$210–230M** | **WEB** earnings call / press summaries ② |

## 3. Valuation + price move
| | |
|--|--|
| Mcap / P/S | ~**$7.8B** / ~**13.7×** TTM (shares 90.69M × $85.73) · **2026-09-22** WEB+SEC |
| P/S÷g | ~**25** on +55% YoY — between CRDO and SMTC |
| Move | 6m WEB ~**$17→$86** (~**5×**) — largest % move in set; still **smallest mcap** |
| Interpretation | Re-rating on optical Infra already violent; residual = **whether PAM4 share & GAAP profitability sustain** after the move |

## 4. Flow-positioning
- **Not** in Whale Rock / scanned mega-fund 13F names (Q2'26) — still **under-owned** vs ALAB/MTSI in that sleeve.
- Schedule 13G activity Jul–Aug 2026 on filings index (names not expanded here) — watch institutionalization.
- us_si universe **excludes** MXL (thin).

## 5. Edge card
| | |
|--|--|
| **priced_in** | Keystone 800G ramp + Infra +145% + multi-bagger tape; Non-GAAP profitability. |
| **variant** | Street still anchors on **legacy broadband** MaxLinear; if Infra stays ≥50% and optical DC guide **$210–230M** converts while GAAP OPM → positive by FY27, multiple can migrate toward optical-DSP peers **without** needing ALAB-like P/S. Archive empty → process edge for this desk. |
| **breaks_if** | Q3 rev **<****$210M** or Infra growth collapses; optical DC guide cut; LPO adoption hits Keystone content; SBC stays >15% as GAAP losses persist. |
| **residual** | **#1** for this five-name sleeve — highest combo of optical DSP exposure **inflection** + still-mixed perception + smaller abs mcap; **execution/LPO risk elevated**. |

## 6. Open questions
- Exact **optical DSP $** inside Infrastructure $85M (SEC only gives market buckets).
- Rushmore 1.6T timing credibility (WEB: 2H27 revenue).
- Gross margin trajectory if 800G ASP falls.
- Debt vs thin cash ($65M cash / $124M LT debt).

---

# 4. ALAB — Astera Labs

## 1. Business
- **Products:** PCIe/CXL **retimers**, AEC / fabric switches — **server-in / scale-up copper** connectivity. (`entities`)
- **AI role:** GPU-cluster **electrical** reach extension — complements optics; **loses** if optics moves into the rack aggressively / CPO shortens copper.
- **Moat:** Protocol (PCIe/CXL) + rack-level software/hardware stack; design wins with hyperscalers (names thin in archive).
- **Competitors:** Broadcom retimers, CRDO AEC, SMTC CopperEdge, Cisco/Ciena vertical moves.

## 2. Financials (source · date)
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM | **$1,202M** | facts ① **2026-09-11** |
| GPM / OPM TTM | **75.1%** / **22.8%** | facts ① |
| Rev growth YoY | **+104.5%** | facts ① |
| Latest Q | Rev **$392.4M**, GPM **73.3%**, OPM **22.7%** (Q ended **2026-06-30**) | facts ① |
| R&D / rev Q | **34.6%** | facts ① |
| SBC / rev Q | **15.9%** | facts ① |
| Inventory YoY | **+94.2%** | facts ① |
| AR YoY | **+691.5%** ⚠ | facts ① |
| OCF / EBIT Q | **1.21×** | facts ① |

## 3. Valuation + price move
| | |
|--|--|
| Archive mcap / P/S / P/S÷g | **$50.5B** / **42.0×** / **40.2** · **2026-09-11** |
| WEB refresh | Px **$365.86**, mcap ~**$63.5B**, P/S ~**53×** |
| Move | 6m ~**+3×**; archive 09-15 **$258.55** → WEB ~$366 |
| Read | **Most expensive** growth chip in set; copper purity already consensus |

## 4. Flow-positioning
- Whale Rock Q2'26: **Astera Labs $757M**, **6.08%** of that book (① 13F) — **crowded quality** sleeve.
- entities `tracked_price: true`.
- Layer-boundary risk: Ciena/Nubis AEC entry (valuechain T5).

## 5. Edge card
| | |
|--|--|
| **priced_in** | PCIe/CXL AI rack copper monopoly narrative; 75% GPM; Whale Rock-sized ownership; P/S >40×. |
| **variant** | Only if AR +691% proves **timing/billings** not demand pull-forward **and** optics fails to eat retimer sockets through 2027 — i.e. copper duration longer than optical bulls price. |
| **breaks_if** | AR/rev normalizes via **restatement-like** growth air-pocket; PCIe gen transition share loss; rack optics (NPO/CPO) cuts retimer TAM. |
| **residual** | **#5** for *optical* sleeve — wrong primary instrument; residual is copper-duration vs optical, already priced. |

## 6. Open questions
- AR explosion explanation (contract terms / new logos / channel).
- AEC vs retimer mix.
- 13F follow-through beyond Whale Rock (full universe not in archive).

---

# 5. MTSI — MACOM

## 1. Business
- **Products:** RF/analog · **optical drivers & TIA** · some lasers — broad catalog. (`entities`)
- **AI role:** “Can’t-delete” **analog** in optical modules (valuechain T2 physics) but **diluted** by RF/industrial end markets.
- **Moat:** Compound semi / RF process + optical analog sockets.
- **Competitors:** SMTC SI, Broadcom, Laser Components vendors; less direct vs ALAB/CRDO digital.

## 2. Financials (source · date)
| Metric | Value | Source · as-of |
|--------|-------|----------------|
| Revenue TTM | **$1,164M** | facts ① **2026-09-11** |
| GPM / OPM TTM | **56.5%** / **18.1%** | facts ① |
| Rev growth YoY | **+35.8%** | facts ① |
| Latest Q (fiscal Q3 ended **2026-07-03**) | Rev **$342.2M**, GP **$199.6M** (~**58.3%**), OI **$77.1M** (~**22.5%**) | SEC companyfacts ① |
| SBC that Q | **$21.1M** (~**6.2%** of rev) | companyfacts ① |
| Inventory | **$281.5M** vs **$215.4M** YoY (~**+31%**) | companyfacts ① |
| facts depth | Fewer quality flags stored than CRDO/SMTC (no SBC/inv in brain until this pull) | archive gap partial |

## 3. Valuation + price move
| | |
|--|--|
| Archive mcap / P/S / P/S÷g | **$21.0B** / **18.0×** / **50.4** · **2026-09-11** |
| WEB refresh | Px **$278**, mcap ~**$21.2B**, P/S ~**18×** |
| Move | 6m ~**+27%** — **laggard** vs SMTC/MXL/ALAB; archive 09-15 **$240** |
| Read | Modest re-rate; growth-adjusted valuation **rich** vs CRDO |

## 4. Flow-positioning
- Whale Rock Q2'26: MACOM **$376M**, **3.02%** of book; shares **988,785** vs Q1 **1,174,991** — **trimmed shares**, value up with price.
- entities `tracked_price: false`; theses list empty on entity card.

## 5. Edge card
| | |
|--|--|
| **priced_in** | Optical analog AI BOM + RF recovery; ~18× sales. |
| **variant** | If optical driver/TIA content per 1.6T module rises faster than RF mix and MACOM takes share from SMTC, OPM can sustain **>20%** with less SBC drama than CRDO/ALAB — quiet compounder. |
| **breaks_if** | RF downturn offsets optical; optical share loss to integrated DSP vendors; inv grows without sales. |
| **residual** | **#4** — correct physics layer, wrong purity/ownership for a concentrated optical bet. |

## 6. Open questions
- Optical vs RF **% of sales** (not in facts).
- Laser vs driver mix.
- Why Whale Rock trimmed shares.

---

## Cross-check vs archive theses (do not contradict without new ①)

| Thesis | Implication for this five |
|--------|---------------------------|
| interconnect **T1** | CRDO benefits from DSP *survival*, not DSP death |
| interconnect **T2/T5** | CRDO SBC + inventory still open falsifiers |
| interconnect **T3** | SMTC SI strength real but ≠ pure LPO |
| valuechain **T2** | Prefer can’t-delete laser/driver/TIA over eraseable DSP long-term — **tension with MXL #1 residual** (MXL is DSP). Rank #1 is **trading/process residual**, not “physics forever.” |
| valuechain **T5** | Chip-layer P/S÷g: CRDO still cheapest growth-adjusted; Ciena/Nubis presses CRDO/ALAB copper |

**Physics vs residual:** Long-horizon bottleneck sleeve still favors **SMTC/MTSI analog** and lasers (sibling dossiers). **MXL #1** here = *near-term variant* (PAM4 share + archive gap + size) that **breaks if LPO wins**.

---

## Source legend
- **①** SEC XBRL / 10-Q / 8-K / companyfacts / 13F XML in archive  
- **②** Company IR / earnings call (WEB)  
- **③** Broker / trade press  
- **WEB** market prices (Yahoo chart)

*No execution orders. Sizing reserved for Kenneth.*
