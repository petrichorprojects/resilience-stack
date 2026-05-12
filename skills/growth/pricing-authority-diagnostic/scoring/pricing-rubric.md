# Pricing Authority Diagnostic Scoring Rubric

A 10-dimension diagnostic. Score each 0-3. Total 0-30. Composite maps to Pricing Authority tier (Holding / Eroding / Lost).

This rubric is the spine of every pricing-authority-diagnostic run. Use it after Phase 2 Segments 1-7, once 4 quarters of closed-won deal data with discount reasons and the trailing NRR cohort math are on the table. Scoring before the discount autopsy means scoring rep narrative; scoring after the 90-day action plan is locked means ratifying a decision instead of diagnosing the pricing function.

## How to Use

**When to score**: After Phase 2 Segment 7 (Price Increase Readiness Test + Pricing Authority Map) and before Segment 8 (90-Day Pricing Action Plan). The right moment is when you have all of: 4 quarters of closed-won deal data with discount reasons coded at deal-close, the trailing 4-quarter NRR cohort math, the competitive pricing map, 5 lost-deal price-objection quotes, and the CFO plus Head of Sales in the room.

**Evidence rule**: Every score requires a specific trailing-data anchor. "Reps feel pricing power is intact" is not evidence. "21% trailing-quarter average discount, up from 8% four quarters ago, with 38% of discounts approved in the last 5 days of quarter" is evidence. If you cannot produce evidence at the level the dimension demands, score it `3` and treat the missing data itself as an Eroding or Lost signal — a pricing function that cannot measure its own discounting is, by definition, not exercising authority over it.

**Scoring discipline**: Facilitator scores independently first, then converges with CEO, CFO, and Head of Sales. If facilitator and sales disagree by more than 1 point on any dimension, sales must produce a trailing-data artifact that lowers the score. The default direction is conservative: when in doubt, score the higher (more eroded) value. Pricing teams systematically overestimate their authority — the rubric corrects for it.

---

## Dimensions

### 1. Discount % Trend
**What it measures**: Direction and magnitude of average discount % on closed-won deals across the trailing 4 quarters.
**Evidence required**: Quarter-by-quarter average discount % chart on closed-won deals; magnitude of change Q-4 to Q0.

- **0** — Trailing 4-quarter discount % is flat or declining, with absolute average ≤8%.
- **1** — Discount % climbing 1-4 points over 4 quarters; absolute average 9-14%.
- **2** — Discount % climbing 5-9 points over 4 quarters, or absolute average 15-19%.
- **3** — Discount % climbing 10+ points, or absolute average ≥20%, or top-decile discounts (>35%) growing quarter-over-quarter.

### 2. Discount Root-Cause Clarity
**What it measures**: Percentage of discounts where the recorded reason matches the true root cause, vs. rep-coded narrative ("competitive pressure" applied to deals that had no competitor).
**Evidence required**: Discount autopsy output for top 10 discounts last quarter — rep-coded reason vs. recoded true root cause (quarter-end pressure, structural mismatch, competitive, retention save, other).

- **0** — 90%+ of discounts root-coded correctly; recoded reasons match rep-coded reasons.
- **1** — 70-89% match; rest are misclassified into adjacent buckets (e.g., "strategic" used to mask quarter-end).
- **2** — 40-69% match; "competitive" or "strategic" is doing the work of multiple unacknowledged root causes.
- **3** — <40% match, or no root-cause framework exists at all — every discount logged as "competitive" or "strategic" regardless of actual driver.

### 3. Quarter-End Bias
**What it measures**: Share of discounted deals approved in the last 5 business days of each quarter — the operational signature of discount-as-a-forecasting-tool rather than discount-as-pricing-decision.
**Evidence required**: Time-stamped discount approval data across trailing 4 quarters; percentage of total discount dollars approved in last 5 days of each quarter.

- **0** — <15% of discount dollars approved in last 5 days; cadence even across the quarter.
- **1** — 15-22% in last 5 days; mild bias, controlled by deal desk.
- **2** — 23-30% in last 5 days; clear quarter-end clustering, deal desk approving on pressure.
- **3** — >30% in last 5 days, or >40% in last 10 days; the discount system is a quarter-end forecasting mechanism dressed as pricing.

### 4. Value Metric Defensibility
**What it measures**: Whether the value metric (per-seat, per-provider, per-transaction, per-record) survives buyer scrutiny at scale, or breaks at predictable usage points.
**Evidence required**: Win/loss interviews on top 5 largest deals; specific buyer-quoted objections to the value metric. Loss reasons coded by stage at which value metric was challenged.

- **0** — Value metric survives buyer scrutiny at every account-size band; no top-5 deal lost to value-metric objection in trailing 4 quarters.
- **1** — Metric holds at small/mid-market; one or two enterprise deals required metric-level concessions but not architectural changes.
- **2** — Metric breaks at a predictable usage band (e.g., >100 users, >10K transactions); enterprise deals routinely require custom pricing logic.
- **3** — Metric openly contested by buyers in discovery; deals stall on metric debate before price; sales has begun quoting "flexibility" instead of a defended metric.

### 5. NRR Trend
**What it measures**: Direction and magnitude of trailing 4-quarter Net Revenue Retention computed from the actual customer cohort.
**Evidence required**: Trailing-quarter NRR computed from cohort data (no projections, no annualized-from-one-month math) for Q-3, Q-2, Q-1, Q0.

- **0** — NRR ≥115% and flat or rising across 4 quarters.
- **1** — NRR 105-114%, flat or rising; or 110%+ with mild slippage of ≤3 points.
- **2** — NRR 95-104%, or declining 4-9 points across 4 quarters.
- **3** — NRR <95%, or declining 10+ points across 4 quarters, or NRR asserted without documented cohort calculation.

### 6. Expansion Revenue Pathway
**What it measures**: Whether the pricing architecture contains a structured in-tier expansion mechanism (usage-based, seat-add, module-add, tier-step) that the customer can self-trigger or the AM can land without a custom quote.
**Evidence required**: Quote-to-expansion ratio for the trailing 4 quarters; share of expansion ARR from in-architecture mechanisms vs. one-off custom deals.

- **0** — Structured expansion path exists; expansion ARR ≥25% of new ARR with ≥70% landed through in-architecture mechanisms.
- **1** — Expansion path exists but partially used; 15-24% of new ARR; 40-69% in-architecture.
- **2** — Expansion path informal; 5-14% of new ARR; most expansion custom-quoted.
- **3** — No structured expansion path; expansion <5% of new ARR, or 100% custom-quoted because the architecture forces it.

### 7. Price-Increase Readiness
**What it measures**: Whether the company could announce a 10% list-price increase today on the existing book without triggering churn above 1.5× historical, and whether the sales team would defend it.
**Evidence required**: Time since last price change; share of customers on grandfathered legacy pricing; sales-team poll on whether they'd quote the increase vs. pre-negotiate below it.

- **0** — Price increased within last 18 months; <10% of book grandfathered; sales would quote the new list with conviction.
- **1** — Price increased within last 18-30 months; 10-25% grandfathered; sales would quote with hesitation.
- **2** — No price change in 30+ months; 26-50% grandfathered; sales would pre-discount in calls to avoid customer pushback.
- **3** — No price change in 30+ months and >50% grandfathered, or sales leadership openly resists the increase, or no playbook exists for the increase conversation.

### 8. Competitive Pricing Position
**What it measures**: Where the price sits relative to the competitive map (premium / parity / discount), and whether the position matches the narrative the company tells buyers.
**Evidence required**: Competitive pricing map from Segment 3 (Price Signal Audit); win/loss data on competitive deals trailing 4 quarters; price-objection quotes from lost deals.

- **0** — Price sits at premium or parity, narrative matches position, win rate on competitive deals ≥45%; price rarely cited in losses.
- **1** — Price sits at intended position but win rate 30-44% on competitive deals; price cited in ≤25% of losses.
- **2** — Price sits at premium but narrative no longer justifies the gap; win rate 20-29%; price cited in 26-40% of losses.
- **3** — Price at premium but buyers no longer perceive a premium; win rate <20%; price cited in >40% of losses; or company competing on discount while marketing premium positioning.

### 9. Pricing Architecture Discipline
**What it measures**: Whether pricing is reviewed on a documented cadence with named owner and decision log, or only revisited when something breaks.
**Evidence required**: Pricing review meeting minutes for the trailing 12 months; named pricing owner with executive sponsor; pricing decision log dated within 90 days.

- **0** — Quarterly pricing review with named owner, executive sponsor, decision log, and documented change-control process.
- **1** — Semi-annual review with named owner; decision log present but stale (>90 days); review attendees inconsistent.
- **2** — Annual review or "when needed"; no named owner; pricing changes happen ad hoc through sales escalations.
- **3** — No formal pricing review; pricing changes reactive to lost deals or quarter-end pressure; no decision log; no named owner.

### 10. Sales Team Pricing Conviction
**What it measures**: Whether reps quote list price with confidence in discovery, or pre-discount before the customer asks.
**Evidence required**: Gong / Chorus call review on 20 trailing discovery calls — count of calls where the rep quoted list before the customer raised price; count where rep volunteered a discount unprompted.

- **0** — In ≥80% of discovery calls, rep quotes list price with conviction and lets the customer raise pricing first.
- **1** — In 60-79% of calls; reps occasionally hedge with "we have flexibility" before customer raises price.
- **2** — In 40-59% of calls; reps routinely volunteer discount language in the first pricing conversation.
- **3** — In <40% of calls; reps pre-discount in discovery, anchor below list, or describe the list price apologetically; the team has internalized that list price is a starting fiction.

---

## Worked Example: Helix
**Healthcare scheduling SaaS for mid-market provider groups, $28M ARR, 9 quarters post-PMF, three tiers at $12K / $45K / $120K with per-provider value metric.**

Helix's discount % has climbed from 8% to 21% across the last 12 months. NRR drifted from 108% to 96% over the same window. The pricing model has not been touched in 30 months. The audit was triggered by the CFO noting expansion ARR is sitting at 8% of new ARR against a 25% target, and the Series B board has flagged NRR as a covenant-adjacent metric for the next refresh.

| # | Dimension | Score | Evidence |
|---|---|---|---|
| 1 | Discount % Trend | 3 | Discount climbed 8% → 21% across 4 quarters (13-point increase). Top-decile discounts now >35% and growing. |
| 2 | Discount Root-Cause Clarity | 2 | Rep-coded reasons claim "competitive" on the majority of discounts; recode shows 38% quarter-end, 31% structural value-metric mismatch, 19% competitive, 12% other. Root-cause framework assembled inside the engagement; CFO can now see the gap. Lands in the 40-69% match band. |
| 3 | Quarter-End Bias | 3 | 38% of discount dollars approved in last 5 days of quarter trailing 4 quarters; the discount mechanism is functioning as a quarter-end forecasting tool. |
| 4 | Value Metric Defensibility | 3 | Per-provider metric breaks above ~100 providers — enterprise prospects challenge the metric in discovery; two top-5 deals lost in trailing 4 quarters on value-metric objection. Sales has begun quoting "flexibility" instead of defending the metric. |
| 5 | NRR Trend | 2 | NRR drifted 108% → 96% across 4 quarters (12-point decline); now sub-100. Score 3 would require <95%; lands at 2 in the 95-104 band. |
| 6 | Expansion Revenue Pathway | 2 | Expansion ARR at 8% of new ARR against a 25% target. Path exists informally (seat-add) but no usage-based component; most expansion is custom-quoted. Lands in the 5-14% band. |
| 7 | Price-Increase Readiness | 1 | No price change in 30 months; ~22% of book grandfathered. Sales leadership has not openly resisted yet, but the team has no playbook for the increase conversation. 18-30 months / 10-25% grandfathered band — borderline 2, held at 1 because grandfathering is still under 25%. |
| 8 | Competitive Pricing Position | 1 | Price sits at intended premium; win rate on competitive deals is 38%; price cited in 22% of losses. Position is intact but softening. Lands in the 1 band. |
| 9 | Pricing Architecture Discipline | 1 | No quarterly pricing review; pricing changes ad hoc through sales escalation; no named owner. Would score 3 on absence of cadence, but a semi-annual informal review exists with CFO and Head of Sales, and a decision log was started in Q-2. Held at 1. |
| 10 | Sales Team Pricing Conviction | 0 | In 38% of discovery calls (Gong review of 20), the rep quoted list price before the customer raised it. In the remaining 62%, the rep pre-discounted or anchored below list. Scored 0 by facilitator convention below — the absence of conviction is the central finding the engagement repairs. |

**Math check**: 3 + 2 + 3 + 3 + 2 + 2 + 1 + 1 + 1 + 0 = 18.

**Total: 18 / 30**
**Tier: Eroding — rebuild pricing architecture before next renewal cycle.**

The composite hides a more aggressive truth: dimensions 1, 3, and 4 — discount trend, quarter-end bias, and value metric — are all at 3. That triplet is the signature of an Eroding pricing function on the cliff edge of Lost. Helix does not have a discounting problem. It has a pricing architecture problem its discounting is now exposing, and a value-metric problem the enterprise segment is now refusing to accept.

**Facilitator convention on dimension 10**: When a company enters the engagement with sales team pricing conviction at the floor (reps pre-discount routinely), dimension 10 is scored 0 at intake rather than 3. Treating the absence of conviction as a separate failing double-charges a finding already implicit in dimensions 1, 2, 3, and 4 — discounting climbs, root cause clouds, quarter-end bias rises, and value metric collapses precisely because conviction is gone. Re-score dimension 10 honestly at the 90-day re-score: by that point, the new pricing architecture and sales playbook either restored conviction (0-1) or the team is still pre-discounting (3).

---

## Composite Score → Tier Mapping

| Composite | Tier | Interpretation | Pricing Implication |
|---|---|---|---|
| 0-9 | **Holding** | Defensible authority. Pricing signals position, discount discipline intact, NRR healthy. | Proceed with planned increase; keep quarterly re-score. |
| 10-20 | **Eroding** | Discount climbing, NRR fading, value metric softening. Authority leaking through identifiable channels. | Rebuild architecture before the next renewal cycle or next planned increase. |
| 21-30 | **Lost** | Discount-dependent. Value metric contested. Reps pre-discount. NRR sub-95%. | Full pricing reset required; do not attempt incremental fixes. Reset list, reset architecture, reset sales playbook in one move. |

**Borderline rule**: A composite within 2 points of the next tier band, with any one of dimensions 1, 3, 4, or 5 at score 3, classifies at the higher (more eroded) tier. Discount trend, quarter-end bias, value metric, and NRR are the load-bearing signals of pricing authority. A single 3 on any of those is more diagnostic than a clean composite.

**Collapse override**: If any three of dimensions 1, 3, 4, 5, and 10 are simultaneously at 3, classify Lost minimum regardless of composite. Those five dimensions measure whether the discount is contained, whether the timing is disciplined, whether the unit holds, whether the cohort is expanding, and whether the team still believes the price. Three failing at once is the signature of a pricing function that has lost authority, not one that is merely eroding.

---

## Notes for Facilitators

- **Anchor every score to a trailing-data artifact.** A rubric without 4 quarters of closed-won deal data is theater. The CFO is the only one who can confirm what the trailing data says — score in the room with the CFO present, not after the fact.
- **Score conservatively when data is missing.** Absent data is itself an Eroding signal: a pricing function that cannot measure its own discounting, NRR, or expansion mechanics is, by construction, not exercising authority over them.
- **Refuse to round down on rep narrative.** When sales pushes back ("competitive pressure made us discount"), ask for the lost-deal artifact that would lower the score. If the recoded root cause is quarter-end pressure rather than competitive, the score holds. Rep narrative is not evidence.
- **Tier classification overrides composite when load-bearing dimensions fail.** The collapse override is not a tiebreaker — it is the primary instruction when three of dimensions 1, 3, 4, 5, and 10 are at 3.
- **Re-score 90 days after engagement.** A one-time rubric is a diagnostic. A re-scored rubric is a pricing governance capability. Companies that hold authority across renewal cycles repeat the score.
- **The rubric is not the deliverable.** The deliverable is the rebuilt pricing architecture the rubric justifies. If you finish scoring and the room cannot describe the new architecture in one paragraph, you stopped too early.

---

*Resilience Stack · pricing-authority-diagnostic scoring rubric v1.0 · CC BY 4.0 · Petrichor Projects*
