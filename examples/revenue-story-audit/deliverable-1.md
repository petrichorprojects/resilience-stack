# Deliverable 1 — Revenue Narrative Gap Report

**Company**: NorthStack
**Sector**: B2B fintech — operations layer for mid-market neobanks
**ARR**: $20M (Q1 2026)
**Stage**: Series B-funded, Series C kickoff 90 days
**Audit date**: 2026-05-12

---

## 1. Current Revenue Narrative (verbatim, Q4 2025 board deck)

> *"NorthStack is executing against a multi-channel growth motion, with diversified revenue across customer segments and a sales-led GTM driving 60% of new ARR. The team is bullish on a +120% Y/Y trajectory, supported by 115% net revenue retention and durable expansion in the existing book."*

This narrative was assembled by the CFO from the Q3 2025 board pre-read and carried forward into the Q4 deck without re-derivation. None of the five quantitative claims was re-validated against system data before the deck was finalized.

## 2. Claim-by-Claim Audit

Each claim from the narrative classified as **verified** (traceable to mechanics), **extrapolated** (derived from a real data point but extended without evidence), **hopeful** (assumed without underlying data), or **wrong** (contradicted by mechanics).

| # | Claim | Classification | Mechanics reality | Gap severity |
|---|-------|----------------|-------------------|--------------|
| 1 | "Diversified revenue across customer segments" | **Wrong** | Top 1 customer = 22% of revenue. Top 10 = 64%. Top geo (US East) = 71%. Top product (core ledger) = 64%. Concentration on every axis. | **High** |
| 2 | "Sales-led GTM driving 60% of new ARR" | **Wrong** | System-attributed channel mix: outbound 40%, inbound 38%, partner referrals 22%. Rep coding over-credited outbound by ~20 points. | **High** |
| 3 | "Bullish on +120% Y/Y trajectory" | **Hopeful** | Trailing 4Q growth = +47%. Forecast extrapolated from a single Q2 2025 expansion spike. No bottoms-up build. Partner referral channel (38% of Q1 new logos) silent since Feb 2026 — not yet modeled into the forecast. | **High** |
| 4 | "Supported by 115% net revenue retention" | **Wrong** | Last full-quarter measured NRR = 96%. The 115% figure was an annualization of a peak-cohort run-rate, not a measured trailing NRR. 3 of top 10 customers showing active churn signals (usage decline, contract renegotiation, exec turnover). | **High** |
| 5 | "Durable expansion in the existing book" | **Extrapolated** | Expansion ARR exists ($1.5M last 4Q) but is concentrated in 5 customers. 2 of those 5 are now in churn-signal status. Customer #1 renegotiated -8% effective price in Q1 2026 — net expansion on that account is negative quarter-over-quarter. | **Medium** |

## 3. Underlying Evidence Integrity Findings

Two structural problems contributed to the gap, beyond the claims themselves.

**Rep-coded channel attribution.** Channel was a self-reported CRM field at deal close, not a system measurement. The $1 Trace Exercise (Segment 2) found 3 of 6 traced dollars had channel codes that contradicted the actual first-touch and conversion path. Recommendation: replace rep-coded attribution with system-attributed multi-touch starting next quarter.

**Modeled NRR carried as measured.** The 115% NRR figure was created in a financial model two quarters ago and propagated into every subsequent deck without being re-derived from the live customer ledger. The model assumed: (a) no contraction in the bottom decile, (b) Q2 2025 expansion run-rate continues, (c) no renegotiations. All three assumptions failed by Q4 2025. Recommendation: NRR is a measured number, not a modeled one. Lock the methodology with the finance team before next reporting cycle.

## 4. Top 3 Highest-Severity Gaps

These are the three claims that would not survive a Series C diligence cycle and that materially mis-price the round if uncorrected.

1. **Concentration disclosure gap (Claim 1).** Top 1 customer at 22%, with a -8% renegotiation already in flight, is a single-point-of-failure that a buyer will discover in the customer-call portion of diligence. The deck describes the inverse — diversification. The Externally-Defensible version must lead with concentration acknowledgement plus the mitigation plan, not bury it.
2. **NRR gap (Claim 4).** 96% vs 115% is a 19-point swing. Diligence will pull the live ledger; the discrepancy is not survivable. The reconciled narrative must show measured NRR (96%) and the explicit path to 105%+ within 4 quarters, not the modeled 115%.
3. **Forecast gap (Claim 3).** +120% claimed vs +47% trailing is a 73-point delta. Without a bottoms-up build that survives sensitivity analysis, the forecast is hopeful. The reconciled forecast (+60-75%) is defensible because the underlying assumptions are named, sourced, and have a sensitivity band. Going into diligence with +120% on the cover page risks the entire round.

## 5. Narrative-Mechanics Gap Score

Composite of severity-weighted claim accuracy:

- Verified claims: 0 / 5
- Extrapolated: 1 / 5
- Hopeful: 1 / 5
- Wrong: 3 / 5

**Pre-rebuild gap: 62%.** Target post-rebuild: **<15%.** The path to <15% requires rewriting Claims 1, 2, 4 around measured mechanics and rebuilding Claim 3 with a bottoms-up forecast. Claim 5 survives with a tightened scope (expansion is durable in the Top 11+ cohort, not the Top 10).

---

*Produced by Resilience Stack v1.5 · revenue-story-audit · CC BY 4.0 · petrichorgrowth.com*
