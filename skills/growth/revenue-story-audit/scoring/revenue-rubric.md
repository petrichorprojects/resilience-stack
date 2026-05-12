# Revenue Story Audit Scoring Rubric

A 10-dimension diagnostic. Score each 0-3. Total 0-30. Composite maps to Narrative Integrity tier (Reconciled / Drifting / Inflated).

This rubric is the spine of every revenue-story-audit run. Use it after Phase 2 Segments 1-7, once enough trailing-data evidence is on the table to anchor each dimension to a number rather than a feeling.

## How to Use

**When to score**: After Phase 2 Segment 7 (The Uncomfortable Metric reveal) and before Segment 8 (Reconciliation). Scoring earlier means scoring vibes. Scoring later means the reconciled two-version artifact has already been negotiated and the rubric becomes a ratification exercise instead of a diagnostic. The right moment is when you have all of: 4 quarters of segmented revenue, the last 2 board decks, attribution data on the trailing 4 quarters of pipeline, and the leadership team in a room with the Uncomfortable Metric on the wall.

**Evidence rule**: Every score requires a specific trailing-data anchor. "We feel good about pipeline" is not evidence. "Qualified pipeline coverage is 1.8× forecast against a 3.0× internal standard, trailing 2 quarters" is evidence. If you cannot produce evidence at the level the dimension demands, score it `3` and treat the missing data itself as a Drifting or Inflated signal — a revenue function that cannot measure its own mechanics is, by definition, not telling a defensible story about them.

**Scoring discipline**: Facilitator scores independently first, then converges with CEO, CFO, and Head of Sales. If facilitator and participant disagree by more than 1 point on any dimension, the participant must produce a trailing-data artifact that pulls the score down. The default direction is conservative: when in doubt, score the higher (more inflated) value. This counteracts the natural tendency of revenue teams to flatter themselves before a raise.

---

## Dimensions

### 1. Forecast Integrity
**What it measures**: Percentage of forecast assumptions backed by trailing-data evidence (vs. extrapolated, hopeful, or undocumented).
**Evidence required**: Forecast assumption ledger with per-assumption evidence rating (verified / extrapolated / hopeful / undocumented). If no ledger exists, score 3.

- **0** — 90%+ of forecast assumptions are verified against trailing data; sensitivity analysis exists for the rest.
- **1** — 70-89% of assumptions verified; remaining assumptions are extrapolated from at-least-one-quarter trailing data with documented logic.
- **2** — 40-69% of assumptions verified; rest are extrapolation or "team is bullish" without quantified backing.
- **3** — <40% verified, or forecast growth rate is 2×+ trailing growth rate with no documented assumption change to justify the step-up.

### 2. Channel Attribution Truth
**What it measures**: Accuracy of claimed channel mix vs. attributed channel mix on closed-won revenue, trailing 4 quarters.
**Evidence required**: Attribution model output (first-touch, last-touch, or multi-touch — pick one and apply consistently) compared line-by-line to the channel mix asserted in board decks and investor narrative.

- **0** — Claimed channel mix within ±5 percentage points of attributed mix across every channel.
- **1** — Claimed mix within ±10 points; no single channel is misstated by more than 15 points.
- **2** — Claimed mix differs from attributed by 11-20 points on the top channel, or a "growth channel" is overstated by 2× its actual contribution.
- **3** — Claimed mix differs from attributed by 20+ points on the top channel, or attribution is not measured at all (channel claims are operator intuition).

### 3. Customer Concentration
**What it measures**: Top-1 and top-10 customer concentration as a percentage of trailing-quarter revenue, weighted against the narrative the board has been told about diversification.
**Evidence required**: Customer revenue table for the trailing quarter, sorted descending, with cumulative percentages.

- **0** — Top 1 < 5% and top 10 < 30% of revenue, and concentration is explicitly disclosed in board materials.
- **1** — Top 1 5-10% or top 10 31-45%, disclosure is present but not foregrounded.
- **2** — Top 1 11-20% or top 10 46-60%, narrative still claims "diversified customer base."
- **3** — Top 1 >20% or top 10 >60%, and the narrative still claims diversification or omits concentration from board materials.

### 4. NRR Truth
**What it measures**: Distance between claimed NRR (Net Revenue Retention) in board / investor materials and trailing-quarter NRR computed from cohort data.
**Evidence required**: Trailing-quarter NRR computed from the actual customer cohort (no projections, no annualized-from-one-month math), compared to the NRR number in the most recent board deck.

- **0** — Claimed NRR within ±2 points of trailing NRR; both above 110%.
- **1** — Claimed within ±5 points of trailing; trailing is between 100-110%.
- **2** — Claimed overstates trailing by 6-15 points, or trailing is 90-99%.
- **3** — Claimed overstates trailing by 15+ points, or trailing is <90%, or NRR is asserted without a documented calculation methodology.

### 5. Cohort Retention Visibility
**What it measures**: Whether leadership (CEO, CFO, Head of Sales) can name retention by cohort cohort-on-cohort without pulling a dashboard, and whether the cohort math is reconciled across finance, sales, and CS.
**Evidence required**: Live ask in the room — "name the gross retention of the H2 2024 cohort at month 12." Three independent answers are collected; cohort data is then surfaced and compared.

- **0** — All three answers within ±2 points of the actual, and a single source-of-truth cohort dashboard exists.
- **1** — Two of three within ±5 points; cohort dashboard exists but is not reviewed in standing cadence.
- **2** — One of three is roughly right; cohort math diverges across finance and CS by 5+ points.
- **3** — No leader can name the cohort retention, or no cohort dashboard exists at all.

### 6. Discount / Pricing Reality
**What it measures**: Whether discounts on closed-won deals are root-coded (CRM-tracked at deal-close with reason) or rep-coded (after-the-fact, narrative).
**Evidence required**: Discount field audit on the last 50 closed-won deals — present, populated, reason-coded, finance-reconciled.

- **0** — 90%+ of deals have a root-coded discount with reason and finance reconciliation.
- **1** — 70-89% root-coded; rest rep-coded but audit-ready.
- **2** — 40-69% root-coded; remainder reconstructed from rep memory or quote artifacts.
- **3** — <40% root-coded, or discount data lives in spreadsheets the CFO cannot reconcile.

### 7. Pipeline Quality
**What it measures**: Qualified-pipeline coverage of the forecast (coverage ratio) and the trailing-quarter conversion of qualified pipeline to closed-won.
**Evidence required**: Pipeline-coverage ratio against forecast, plus trailing-quarter qualified-pipeline-to-closed-won conversion rate.

- **0** — Coverage ratio ≥3.0× and trailing conversion ≥25%; both have held for 2+ quarters.
- **1** — Coverage 2.0-3.0× or conversion 18-24%; one quarter of slippage.
- **2** — Coverage 1.5-1.9× or conversion 10-17%; pipeline padded with stage-1 deals to hit ratio.
- **3** — Coverage <1.5× or conversion <10%, or qualification criteria have been quietly loosened to make coverage look better.

### 8. Single-Points-of-Failure Inventory
**What it measures**: Whether the revenue function has identified, named, and documented its top single-points-of-failure (top customer dependency, single referral channel, single closer, single integration partner) with a mitigation plan for each.
**Evidence required**: Written SPOF inventory with named risks and mitigation plan, dated within 90 days. If no inventory exists, score 3.

- **0** — SPOF inventory exists, is reviewed quarterly, and each SPOF has an active mitigation plan with owner and deadline.
- **1** — Inventory exists but mitigation plans are partial or stale; 1-2 SPOFs lack named owners.
- **2** — Inventory exists in informal form (a conversation, a one-pager) but no mitigation plans; or one major SPOF is unacknowledged in board materials.
- **3** — No inventory exists, or a known SPOF has gone silent / degraded materially (e.g., a key channel partner stops referring) without escalation.

### 9. Narrative-Mechanics Gap
**What it measures**: Composite gap percentage across all narrative claims when each claim is rated against trailing mechanics. Computed from the Board Deck Lie Detector output (verified / extrapolated / hopeful / wrong).
**Evidence required**: Board Deck Lie Detector results — each claim coded; gap = (extrapolated×0.33) + (hopeful×0.67) + (wrong×1.0), divided by total claims.

- **0** — Gap <10%; majority of claims verified, no wrong claims.
- **1** — Gap 10-19%; mostly verified with a small extrapolated tail.
- **2** — Gap 20-34%; meaningful extrapolation and/or one wrong claim that has not been corrected.
- **3** — Gap ≥35%, or any single claim coded "wrong" on a load-bearing metric (forecast, NRR, channel mix, concentration).

### 10. Reconciliation Discipline
**What it measures**: Whether a 2-version artifact (Internal-Honest + Externally-Defensible) already exists pre-engagement, or whether the company has been telling one version everywhere.
**Evidence required**: Written 2-version artifact dated within the last 90 days, with both versions signed off by CEO + CFO. If only one version exists, score 3.

- **0** — Both versions exist, are dated within 90 days, and the deltas are explicitly catalogued and reviewed at board cadence.
- **1** — Both versions exist but the delta document is missing or stale; one of the versions was last updated >90 days ago.
- **2** — Only one version exists, but leadership can articulate verbally where the Internal-Honest version would differ.
- **3** — Only one version exists and leadership cannot name the deltas, or the same deck is shown to board, prospects, and investors without segmentation.

---

## Worked Example: NorthStack
**Fintech operations layer for mid-market neobanks, Series B, $20M ARR, prepping Series C in 90 days.**

NorthStack has a clean product story and a Series B board deck. The board has been told NRR 115%, +120% Y/Y forecast, 60% outbound channel mix, and "diversified customer base." Trailing mechanics tell a different story. The audit was triggered by a Series C investor returning early diligence questions on the partner referral channel.

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Forecast Integrity | 3 | Forecast claims +120% Y/Y; trailing growth is +47%. No documented assumption ledger justifies the 2.5× step-up. |
| 2 | Channel Attribution Truth | 3 | Outbound claimed at 60% of new ARR; last-touch attribution shows 40%. 20-point overstatement on the top channel. |
| 3 | Customer Concentration | 3 | Top 1 customer = 22% of trailing-quarter revenue; top 10 = 64%. Board narrative still claims "diversified customer base." |
| 4 | NRR Truth | 3 | NRR claimed at 115% in last board deck; trailing-quarter cohort NRR is 96%. 19-point overstatement; trailing is sub-100. |
| 5 | Cohort Retention Visibility | 2 | CEO and CFO answers diverge by 7 points on H2 2024 cohort gross retention. Dashboard exists in finance but is not reviewed in standing cadence. |
| 6 | Discount / Pricing Reality | 1 | Discount field is populated on ~78% of closed-won deals with reason codes; CFO can reconcile most. Audit-ready but not 90%+. |
| 7 | Pipeline Quality | 2 | Coverage ratio sits at 1.8× against an internal 3.0× standard; trailing qualified-pipeline conversion is 16%. Pipeline has been padded with stage-1 deals to defend ratio. |
| 8 | Single-Points-of-Failure Inventory | 3 | No written SPOF inventory. Two material SPOFs unacknowledged: (a) top-1 customer at 22%; (b) the partner referral channel has gone silent in Q1 with no escalation. |
| 9 | Narrative-Mechanics Gap | 2 | Board Deck Lie Detector: 4 verified, 6 extrapolated, 3 hopeful, 1 wrong (the +120% forecast). Gap = (6×0.33 + 3×0.67 + 1×1.0) / 14 ≈ 29%. Lands in the 20-34% band. |
| 10 | Reconciliation Discipline | 0 | No 2-version artifact exists pre-engagement. The same deck is shown to board, prospects, and Series C investors. Leadership cannot name the deltas. (Note: dimension scored 0 because absence of the artifact is the central finding the engagement repairs — see facilitator convention below.) |

**Math check**: 3 + 3 + 3 + 3 + 2 + 1 + 2 + 3 + 2 + 0 = 22.

**Total: 22 / 30**
**Tier: Inflated — rebuild required before Series C diligence.**

The composite hides a more aggressive truth: dimensions 1, 2, 3, and 4 — the four load-bearing claims in the Series C narrative (forecast, channel, concentration, NRR) — are all at 3. Per the concentration override below, this combination alone justifies Inflated tier regardless of composite. NorthStack does not have a forecasting problem. It has a narrative problem its forecasting is now catching up to, and a partner-channel SPOF the silent-quarter signal is now exposing.

**Facilitator convention on dimension 10**: When a company enters the engagement without a pre-existing 2-version artifact (which is most of them), dimension 10 is scored 0 at intake, not 3. The absence of the artifact is the trigger that the engagement itself is the repair — counting it against the company would double-charge a finding that is already implicit in the other nine dimensions. Re-score dimension 10 honestly at the 90-day re-score: at that point, the company either has the artifact (0-1) or has not done the work (3).

---

## Composite Score → Tier Mapping

| Composite | Tier | Interpretation | Series-C / Board Implication |
|---|---|---|---|
| 0-9 | **Reconciled** | Story matches mechanics. Defensible under diligence. | Proceed; keep quarterly re-score. |
| 10-20 | **Drifting** | Gap forming between story and mechanics. Individually explainable signals. | Repair before next board cycle or before raise kickoff. |
| 21-30 | **Inflated** | Story and mechanics materially disconnected. Multiple load-bearing claims fail trailing-data test. | Rebuild the narrative before diligence; assume valuation cut of 1-2 turns if status quo enters a process. |

**Borderline rule**: A composite within 2 points of the next tier band, with any one of dimensions 1, 2, 3, or 4 at score 3, classifies at the higher (more inflated) tier. Forecast, channel, concentration, and NRR are the load-bearing claims in any revenue narrative; a single 3 on any of those is more diagnostic than a clean composite.

**Concentration override**: If any three of dimensions 1, 2, 3, 4, and 9 are all 3, classify Inflated minimum regardless of composite. Those five dimensions measure whether the forecast holds, whether the channel claim holds, whether concentration is acknowledged, whether NRR is honest, and whether the board deck as a whole is defensible. Three failing simultaneously is the signature of an inflated story, not a drifting one.

---

## Notes for Facilitators

- **Anchor every score to a trailing-data artifact.** A rubric without trailing data is theater. Trailing data is the only thing diligence will accept.
- **Score conservatively when data is missing.** Absent data is itself an Inflated signal: a revenue function that cannot measure its own mechanics is, by construction, telling a story it cannot defend.
- **Refuse to round down on bullishness.** When a participant pushes back ("the team is bullish on Q4"), ask for the trailing-data artifact that would lower the score. If they cannot produce it, the score holds. Bullishness is not evidence.
- **Score in the room with CFO present.** A score without the CFO is a sales-leader narrative. The CFO is the only one who can confirm what the trailing data actually says.
- **Tier classification overrides composite when load-bearing dimensions fail.** The concentration override is not a tiebreaker — it is the primary instruction when 1, 2, 3, or 4 are at 3.
- **Re-score 90 days after engagement.** A one-time rubric is a diagnostic. A re-scored rubric is a governance capability. Companies that survive Series C diligence repeat the score.
- **The rubric is not the deliverable.** The deliverable is the reconciled 2-version artifact the rubric justifies. If you finish scoring and the room cannot describe both versions in one paragraph each, you stopped too early.

---

*Resilience Stack · revenue-story-audit scoring rubric v1.0 · CC BY 4.0 · Petrichor Projects*
