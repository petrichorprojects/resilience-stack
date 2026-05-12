# Worked Example: Investor Story Forensics

**Synthetic Co**: Aperture — vertical SaaS for industrial QA / manufacturing inspection. $42M ARR, Series B-funded, 10-12 months from Series C kickoff.

## Context

- Founded 2018. PMF achieved 2021. $42M ARR by Q1 2026.
- 92 FTEs.
- Series B closed 2023. Series C kickoff planned 10-12 months out. CEO wants to rebuild the investor narrative now so it survives diligence — not 30 days before a partner meeting.

## Symptom (Narrative-Reality Gap Across 5 Claim Classes)

The current deck makes 5 narrative claims. A forensic pull of the underlying data shows widening gaps between what the deck claims and what the trailing data actually says. The gaps are not yet visible to LPs — but they are visible to anyone who pulls financials and calls references.

- Why-Us claim: "$42M ARR, 130% NRR, 14 of 25 top global automotive OEMs as customers." Trailing NRR is 117% (130% was a single best-quarter cited as if trailing). 11 of 25 OEMs are active today (the 14 figure is verbatim from a Q2 2025 customer list — 3 have churned or paused since).
- Why-This-Trajectory claim: "+95% Y/Y growth, expanding to non-automotive verticals (aerospace, pharma, semiconductor)." Trailing growth is +68%. Non-automotive is 6% of revenue, mostly pilots, with 38% pilot churn.
- Reference customer arc: 5 customers named in the deck. 2 have leadership changes (champion left). 1 is in renewal negotiation. 1 paused (auto OEM strategy shift). 1 remains a clean reference.

## Trigger Event

Series C kickoff in 10-12 months. CEO has seen two competitors get cratered in diligence after partners pulled cohort retention and called references that contradicted the deck. CEO wants the same forensic pull done on Aperture now, with enough runway to rebuild the narrative around defensible claims before the first partner meeting.

## Current 5 Narrative Claims (Verbatim from Current Deck)

1. **Why-We-Win**: "We're the only platform built by manufacturing operators, for manufacturing operators."
2. **Why-Now**: "AI-native inspection is the inevitable next layer of factory operations."
3. **Why-Us**: "Founder-led, $42M ARR, 130% NRR, 14 of 25 top global automotive OEMs as customers."
4. **Why-This-Trajectory**: "+95% Y/Y growth, expanding to non-automotive verticals (aerospace, pharma, semiconductor)."
5. **Why-This-Price**: "Series C at $400M post (10x ARR multiple), w/ growth-stage exit story → $1.5B in 36 months."

## Reality Per Claim (Gap Analysis Done Pre-Workshop)

| Claim | Status | Gap |
|-------|--------|-----|
| Why-We-Win | Defensible | 4 of 5 founders are ex-manufacturing operators (Toyota, GE, Caterpillar). Reference-confirmable. |
| Why-Now | Defensible, with framing risk | "AI-native" framing was adopted Q4 2025. Pre-2025 deck said "data-driven inspection." Diligence will pull old decks and ask why the framing changed. |
| Why-Us | **Partially false** | NRR is 117% trailing (130% was Q3 2025 single best-quarter, cited as if it were the trailing number). Customer count is 11 of 25 today (14 was a Q2 2025 snapshot; 3 churned or paused since). |
| Why-This-Trajectory | **Vulnerable** | Non-automotive vertical expansion is 6% of revenue, mostly pilot contracts, with 38% pilot churn. Trailing growth is +68%, not +95%. |
| Why-This-Price | **Fragile** | 10x ARR multiple is defensible at 130% NRR + 95% growth. At 117% + 68% the comparable-set multiple drops to 6-7x, implying $250-290M post. The price claim depends on the Why-Us and Why-This-Trajectory claims being true. |

## 5 Reference Customer Relationship Statuses (Q1 2026)

| # | Customer (anonymized) | Status | Risk |
|---|------------------------|--------|------|
| 1 | Global auto OEM A (top-5 global) | Champion left Q4 2025 (VP Quality, new VP brought in from Tier-1 supplier w/ competing internal tool); active relationship, no renewal yet | Champion-change risk; new VP has not endorsed Aperture publicly |
| 2 | Global auto OEM B (top-10 global) | In renewal negotiation; pushing for 18% price reduction or moving to per-station usage pricing | Renewal-pricing risk; reference call would surface pricing pressure |
| 3 | Global auto OEM C (top-15 global) | Paused Q1 2026 — auto OEM strategy shift away from in-house inspection software; pilot for re-engagement in 9 months | Paused-not-churned, but reference call would not confirm an active relationship |
| 4 | Tier-1 supplier D | Clean reference; expanded twice in 2025; CFO and VP Quality both willing to take calls | Clean — only one of the 5 |
| 5 | Global auto OEM E (top-25 global) | Champion change Q1 2026 (Head of Inspection retired); successor has not yet been briefed on Aperture relationship | Champion-change risk; reference call may go cold |

3 of 5 reference customers are not ready to take a reference call cold today. The deck names all 5 as proof points.

## Internal Forecast vs Trailing Actuals (Y/Y growth)

| Period | Internal forecast (set in deck) | Trailing actual |
|--------|----------------------------------|------------------|
| Q1 2025 → Q1 2026 | +95% | +68% |
| Q3 2025 → Q3 2026 (projected) | +110% | (pacing +60-65%) |

The +95% claim is the projection set at the beginning of 2025. Trailing came in at +68%. The deck has not been updated to the actual trailing number; +95% is still the headline. A partner pulling the cohort retention and back-calculating Y/Y will surface the gap inside 30 minutes.

## NRR Trailing vs Best-Quarter

| Metric | Deck claim | Reality |
|--------|------------|---------|
| NRR | 130% | 130% was the Q3 2025 single best-quarter. Trailing 12-month NRR is 117%. |
| NRR by cohort (auto OEM) | (not broken out) | 124% — strong, holding |
| NRR by cohort (non-auto pilot) | (not broken out) | 78% — 38% pilot churn, low expansion |

## Pilot Churn (Non-Automotive Expansion)

Non-automotive verticals (aerospace, pharma, semiconductor) are 6% of revenue. Most are pilot contracts (3-6 month paid pilots converting to annual). Pilot-to-annual conversion: 62%. **Of the 38% that do not convert, the reasons are structural** — verticals require workflow adaptations Aperture has not built (aerospace certification chain, pharma 21 CFR Part 11 audit trail, semiconductor sub-micron tolerance). Vertical expansion is real but ahead of the product.

## Evidence Inventory (Available Before Workshop)

- Current investor deck (10-12 month draft for Series C)
- Last 4 board decks (Q2 2025 → Q1 2026), including the deck where 130% NRR was the headline metric for the quarter
- Last 4 quarters of financials with cohort retention sliced by initial vertical (auto OEM / Tier-1 supplier / non-automotive pilot)
- Customer list w/ status (active / paused / churned), updated Q1 2026
- 5 reference customer relationship status one-pagers (champion still here? renewal due? exec change?)
- Q3 2025 internal forecast vs actuals + Q1 2026 forecast vs actuals
- Pilot conversion data for non-automotive (aerospace, pharma, semiconductor) over 6 quarters
- Comparable-set valuation pull (10 vertical SaaS Series C rounds 2024-2025) — multiples ranged 5-12x ARR depending on NRR + growth pair

## In the Room

CEO, CFO, Head of Sales, Head of Customer Success, Head of Product. (Head of Marketing optional for the Investor Memory Anchor Design phase — confirmed for second half.)
