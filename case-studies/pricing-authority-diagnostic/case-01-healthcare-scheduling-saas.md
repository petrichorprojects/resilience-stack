# Pricing Authority Diagnostic — Healthcare Scheduling SaaS Pre-Board-Review (Case 01)

**Skill**: `pricing-authority-diagnostic`
**Engagement date**: Q1 2026 (anonymized)
**Duration**: 2.5 hours

## Context

Vertical SaaS for healthcare scheduling, $28M ARR, 9 quarters post-PMF. Founded 2019, PMF 2022. 64 FTEs. Roughly 2 years from the next raise. The board had asked the CFO to prepare a pricing review for next quarter. No price change had shipped in 30 months — confidence in the value metric had gone soft, discount % had climbed quarter over quarter, and the working hypothesis was "tougher market." The diagnostic was commissioned to audit price-value gap, value-metric integrity, and price-increase readiness.

## Symptom

- Average discount climbed from 8% (Q1 2025) to 21% (Q1 2026) — nearly tripled in 4 quarters.
- Share of deals discounted >20% climbed 6% → 37%; >30% discounts 0% → 14%.
- NRR dropped from 108% (Q4 2024) to 96% (Q1 2026) — first sub-100% quarter since PMF.
- Only 8% of customers expanded in 2025 vs a 25% internal target.
- Win-rate held flat at 33% — the bleed was in price realization, not top of funnel.
- 4 of last 5 lost deals cited price; sales attributed all 4 to "competition."
- No price increase shipped in 30 months.

## Skill Run

In the room: CEO, CFO, Head of Sales, Head of Product (Head of CS confirmed for Phase 6). Pre-work pulled: 4 quarters of closed-won deal data w/ discount %, rep-coded reason, close date, manager-approval timestamp; 30-deal CFO + Head-of-Sales spot-recoding of discount root causes; 5 lost-deal interviews with verbatim price-objection language; competitor pricing teardown for LegacyVendor, NewEntrant, RegionalCo; NRR cohort data by initial tier; Head-of-Product "value-metric defensibility memo" that had sat undistributed for six months.

Phase 1 Discount Graveyard: 62% of discounts >20% had been signed in the last 10 business days of each quarter, every quarter, for four quarters. Head of Sales' framing — "buyer fiscal-year alignment" — was tested against the actual buyer fiscal-year distribution (clustered July 52%, January 24%, not at calendar quarter-ends). The alignment claim collapsed.

Phase 2 Discount Autopsy on the top 10 discounts last quarter: 7 of 10 reclassified from "buyer story" or "champion ask" to "quarter-end manager-approved." Across the 30-deal spot-check, the root-cause distribution: quarter-end manager-approved 38%, structural value-metric failure at >100 providers 31%, genuine competitive 19%, other 12%. Phase 3 Value Metric Stress Test using lost-deal verbatims — 3 of 5 lost deals named the structural failure. Value Metric scored 2/5. Phase 7 Price Increase Readiness Test: 30-month gap, rising discount %, undistributed defensibility memo, no published list. Increase Readiness scored 2/5. Composite Pricing Authority Score: 13/25.

## Top 3 Insights

1. **The "competitive deal" code was hiding rep behavior, not buyer behavior.** Reps coded 41% of discounts as "competitive deal," but manager-approval timestamps clustered in the last 10 business days of every quarter — not when competitor activity peaked, not when buyer fiscal years closed. Recoded genuine-competitive share was 19%; 38% reclassified to "quarter-end manager-approved" — rep-and-manager behavior dressed up as buyer pressure. Without timestamps, the recoding would not have been defensible.
2. **The per-provider value metric structurally fails above 100 providers, and customers know it.** "We'd pay you $432K for the same software a 100-provider group pays $120K for." (Lost Deal 1, 240 providers.) 3 of 5 lost-deal verbatims named the same structural failure. Pro NRR dropped to 94% and Enterprise to 92% while Starter held at 104% — the bleed was concentrated exactly where the metric broke. LegacyVendor had already shipped a declining-rate model above 100 providers; NewEntrant a per-appointment usage metric. Helix's per-provider linear model was no longer competitive at the upper tier, regardless of list price.
3. **The defensibility memo had been written six months ago and never circulated.** Head of Product had documented why the per-provider metric was no longer defensible at scale and proposed alternatives. It never reached the CRO or CFO. The board's pricing review could have been preempted six months earlier. Authority is the right to raise prices without losing customers — Helix had given up the right and forgotten it had a memo explaining why.

## 30 / 60 / 90 Day Outcome

| Window | Action | Measurable result |
|--------|--------|--------------------|
| Day 30 | Discount governance changed: manager-approval threshold tightened 25% → 15%; quarter-end approval window restricted to last 5 business days w/ VP Sales sign-off for >20% discounts; defensibility memo circulated to exec team and board | Discount % on new deals dropped 21% → 16%; share of >20% discounts cut 37% → 22% |
| Day 60 | Pricing architecture v2 designed: per-provider preserved at Starter/Pro; declining-rate above 100 providers; usage-based Enterprise option (per scheduled appointment) launched to net-new prospects only; existing customers grandfathered 12 months | 3 of 4 Enterprise prospects accepted the usage-based option without discount; 2 stalled Pro→Enterprise expansions reopened |
| Day 90 | Price increase shipped to Starter and Pro (Starter $12K → $13.5K, Pro $45K → $52K) with methodology memo as proof; CFO presented Pricing Authority Score, recoded discount distribution, and architecture v2 to board | Discount % dropped to 12% (from 21%); NRR rebuilt to 102% (from 96%); first 4 Enterprise customers on usage-based pricing expanded within 60 days; <2% churn from price increase |

## What We Would Do Differently

- Pull discount data **by rep** before the session, not just aggregate. The aggregate showed the climb; the by-rep cut would have shown which reps were quarter-end-driven, and would have made the rep-vs-buyer-pressure distinction defensible in the first 20 minutes instead of mid-Phase-2.
- Include manager-approval timestamps in the pre-work spreadsheet by default. The quarter-end clustering story is central to this engagement type, and without timestamps it can only be argued in the abstract.
- Pre-work should explicitly ask for any uncirculated internal pricing or value-metric memos — they tend to exist and they tend to predict exactly what the diagnostic surfaces.

---

*Anonymized case study — Resilience Stack v1.5 — CC BY 4.0 — Petrichor Projects*
