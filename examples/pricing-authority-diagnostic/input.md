# Worked Example: Pricing Authority Diagnostic

**Synthetic Co**: Helix — vertical SaaS for healthcare scheduling. $28M ARR, 9 quarters post-PMF.

## Context

- Founded 2019. PMF achieved 2022. $28M ARR by Q1 2026.
- 64 FTEs.
- Currently mid-cycle, roughly 2 years from next raise. The board has asked the CFO to prepare a pricing review for next quarter. Internal team has not shipped a price change in 30 months — confidence in the value metric has gone soft.

## Symptom (Discount Climb + NRR Decline + Expansion Gap)

- Average discount on closed-won deals climbed from 8% in Q1 2025 to 21% in Q1 2026 — nearly tripled in 4 quarters.
- Net Revenue Retention dropped from 108% in Q4 2024 to 96% in Q1 2026 — first sub-100% quarter since PMF.
- Only 8% of customers expanded in 2025 (internal target: 25%).
- Win-rate flat at 33% across the same period — the bleed is in price realization, not in deals lost at top of funnel.
- 4 of last 5 lost deals cited price; sales attributed all 4 to "competition."
- No price increase shipped since Q3 2023 (30 months).

## Trigger Event

Board has asked CFO to prepare a pricing review by next quarter. CFO does not want to walk into the review with rep-coded discount reasons as the only evidence. Helix commissioned this diagnostic to audit price-value gap, value-metric integrity, and price-increase readiness before the board meeting.

## Current Helix Pricing Structure

| Tier | List price | Value metric | Buyer |
|------|-----------|--------------|-------|
| Starter | $12K / year | per-provider per-month | Solo practice / 1-10 providers |
| Pro | $45K / year | per-provider per-month | Group practice / 11-100 providers |
| Enterprise | $120K / year | per-provider per-month | Health system / 100+ providers |

- Last price change: Q3 2023 (30 months ago).
- Discount approval: manager-level up to 25%, VP Sales above 25%.
- Annual commitment is standard; multi-year is positioned as a discount lever.

## Discount Data (4 quarters of closed-won deals)

| Quarter | Avg discount % | Discounts >20% | Discounts >30% |
|---------|----------------|-----------------|-----------------|
| Q1 2025 | 8% | 6% of deals | 0% |
| Q2 2025 | 11% | 11% of deals | 2% |
| Q3 2025 | 15% | 19% of deals | 4% |
| Q4 2025 | 18% | 28% of deals | 9% |
| Q1 2026 | 21% | 37% of deals | 14% |

Quarter-end clustering: 62% of discounts >20% are signed in the last 10 business days of the quarter. Same pattern in all 4 quarters.

## Rep-Coded Discount Reasons (4 quarters, all closed-won)

| Reason (rep-claimed) | Share |
|----------------------|-------|
| Competitive deal (LegacyVendor named) | 41% |
| Buyer story (budget, timing) | 22% |
| Annual commitment (multi-year discount) | 18% |
| Champion ask (named customer wanted special treatment) | 12% |
| Other | 7% |

CFO's hypothesis going in: rep-coded reasons are masking the real drivers. CFO has not yet recoded them.

## Recoded Root Causes (CFO + Head of Sales spot-check on 30 deals, surfaced in Phase 2)

| Root cause | Share | What the rep had coded it as |
|------------|-------|------------------------------|
| Quarter-end manager-approved (rep pressure to close, not buyer pressure) | 38% | Mostly "buyer story" or "champion ask" |
| Structural value-metric failure at >100 providers (per-provider math breaks; buyer pushes back on linear pricing for non-linear value) | 31% | Mostly "competitive deal" or "annual commitment" |
| Genuine competitive (LegacyVendor named, side-by-side eval, buyer chose Helix on discount) | 19% | "Competitive deal" |
| Other (true champion economics, one-off concession) | 12% | Mixed |

## Lost Deal Interviews (5 deals, Q1 2026)

| # | Buyer | Size | Lost reason (verbatim) |
|---|-------|------|------------------------|
| 1 | Health system A | 240 providers | "Your per-provider math doesn't make sense at our scale. We'd pay you $432K for the same software a 100-provider group pays $120K for. We can't defend that internally." |
| 2 | Group practice B | 85 providers | "LegacyVendor came in 22% under your discounted price. We needed a reason to pay you more and your team said 'we're better' — that's not a reason." |
| 3 | Health system C | 180 providers | "Pricing was opaque. Your rep gave us three different numbers in two weeks. We went with the vendor that had a published price list." |
| 4 | Group practice D | 55 providers | "We asked what we get if we go from Pro to Enterprise. The answer was 'a few more features and a CSM.' That's not a $75K upgrade." |
| 5 | Health system E | 320 providers | "Your tier structure breaks above 100 providers. We don't want to be on a tier that wasn't designed for us. We chose a vendor with usage-based pricing for enterprise." |

3 of 5 lost deals name the structural value-metric failure. 1 names LegacyVendor. 0 cite list price as the problem — they cite the structure of the price.

## Competitor Pricing Pages (3 competitors, public-site teardown)

| Competitor | Tier 1 | Tier 2 | Tier 3 | Value metric |
|------------|--------|--------|--------|--------------|
| LegacyVendor | $9K | $36K | "Contact sales" | Per-provider, declining-rate above 100 providers |
| NewEntrant (AI-native, launched 2024) | Published list with usage component: $99/provider/mo base + $0.40/scheduled-appointment | Same model, volume discount at 5K+ appointments/mo | Usage-based only above 250 providers | Per-appointment usage |
| RegionalCo | $15K | $52K | "Contact sales" | Per-provider per-month flat |

- LegacyVendor's declining-rate model defuses the linear-pricing pushback Helix gets at >100 providers.
- NewEntrant's usage-based metric (per-appointment) is transparently buyer-verifiable — buyer can count scheduled appointments themselves. Per-provider can also be counted, but per-provider value is non-linear in actual product usage.
- Two of three competitors publish list prices. Helix does not.

## NRR Cohort Breakdown (by initial tier, last 4 quarters)

| Initial tier | NRR (Q4 2024) | NRR (Q1 2026) | Notes |
|--------------|----------------|----------------|-------|
| Starter | 112% | 104% | Best-performing cohort; natural upgrade to Pro provides expansion |
| Pro | 106% | 94% | Sub-100%; churn at the >100-provider boundary, no upgrade path to Enterprise that buyers value |
| Enterprise | 109% | 92% | Largest drop; no expansion path within Enterprise once the customer is at 100+ providers paying per-provider; no usage-based upsell motion |

The NRR decline is concentrated in Pro and Enterprise — exactly the cohorts where the per-provider value metric breaks. Starter is fine.

## Evidence Inventory (available before workshop)

- 4 quarters of closed-won deal data with list price, sold price, discount %, rep-coded discount reason, deal-close date (enables quarter-end pattern analysis), manager approval timestamp
- 30-deal spot-recoding done by CFO + Head of Sales (surfaces root-cause distribution above)
- 5 lost-deal interviews from Q1 2026 with verbatim buyer price-objection language
- Competitor pricing teardown for 3 named competitors (LegacyVendor, NewEntrant, RegionalCo)
- NRR cohort data sliced by initial tier (Starter / Pro / Enterprise) for last 6 quarters
- Internal "value-metric defensibility memo" drafted by Head of Product but never circulated
- Win/loss notes for 4 of 5 lost deals (Customer E's notes were not captured)

## In the Room

CEO, CFO, Head of Sales, Head of Product. (Head of Customer Success recommended for Phase 6 Expansion Revenue Gap Calculator — confirmed for second half of session.)
