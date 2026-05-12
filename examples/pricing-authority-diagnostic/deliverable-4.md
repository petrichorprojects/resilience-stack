# Deliverable 4 — Pricing Architecture Recommendations

**Company**: Helix
**Audit date**: 2026-05-12
**Sequencing principle**: structure before list price. Helix cannot raise prices on a broken architecture; the architecture rebuild is the precondition for every list-price move.

---

## Recommendation 1 — Replace per-provider metric above 100 providers with tiered provider-band pricing

**Rationale**. The per-provider per-month metric is defensible up to ~100 providers and breaks above. 31% of Q1 2026 discount dollars come from buyer rejection of the broken math, concentrated in 12 Enterprise accounts ($4.2M ARR). The metric was flagged internally by product 18 months ago; not escalated.

**Structure**. Keep per-provider pricing through 100 providers. Above 100, switch to tiered provider bands: 101-200 providers at a flat ACV, 201-400 at another flat ACV, 400+ enterprise-negotiated. Buyer can predict cost at scale; rep does not need to defend per-provider math past the breakpoint.

**NRR impact estimate**. Recovers ~9-11 NRR points within 12 months by eliminating the structural discount class and enabling clean upsell paths within bands. Expansion in the >100-provider cohort becomes mechanical rather than negotiated.

**Rollout sequence**. Pilot on top-30 customers in the >100-provider zone (60 days). Measure renewal price and expansion response. Lock for all new deals at day 90; migrate existing on renewal.

**Risk**. 2-3 of the 12 broken-zone accounts may negotiate harder on renewal once they see new structure. Mitigation: grandfather effective per-provider rates for current term; apply bands at next renewal.

## Recommendation 2 — Add usage-based component (appointments processed)

**Rationale**. Helix has no usage-based revenue lever. Expansion can only come from adding providers — which is the metric that breaks. Appointments processed is a clean, buyer-verifiable usage metric. Buyers can count appointments themselves (passes Petrichor's value-metric defensibility test).

**Structure**. Each tier includes an annual appointment volume cap (e.g., Starter: 25K, Pro: 100K, Enterprise: 400K). Overages billed at $0.18-$0.22 per appointment, billed quarterly with annual true-up.

**NRR impact estimate**. Recovers ~4-6 NRR points within 12 months from usage overage in existing accounts. Critical secondary benefit: gives sales a non-discount expansion conversation ("you've grown past your appointment band; here's the path").

**Rollout sequence**. Soft-launch as opt-in on new Enterprise deals (30 days). Make standard for all new deals at 60 days. Roll into existing accounts at renewal starting day 90.

**Risk**. Overage billing perceived as "gotcha" pricing if poorly communicated. Mitigation: dashboard showing real-time appointment count vs cap; 90-day forward notice before any overage charge.

## Recommendation 3 — Convert ad-hoc discounts into structured commitment discounts

**Rationale**. 38% of Q1 2026 discount dollars are quarter-end manager-approved with no buyer-side trigger. The discount practice is destroying authority (see Sunrise Clinical lost-deal verbatim in Deliverable 3). Replacing ad-hoc discounts with **structured, published commitment discounts** converts the leak into a commitment lever and removes the rep's quarter-end escape hatch.

**Structure**.
- Annual prepay: -8%
- 24-month commitment: -12%
- 36-month commitment: -15%
- No other deal-close discounts permitted without CFO sign-off above 10%.

**NRR impact estimate**. Recovers ~3-5 NRR points within 12 months. Larger second-order effect: kills the 38% quarter-end discount class, recovering an estimated $1.1M-$1.4M of leaked Q1 2026 ACV at run-rate. Buyer perception of authority recovers (cited as a contributor to win rate, hard to attribute precisely).

**Rollout sequence**. CFO approval gate live at day 30 (named in Deliverable 5 as Action 1). Commitment discount structure published on pricing page and in sales playbook at day 60.

**Risk**. Sales team friction in the first quarter. Mitigation: comp plan adjustment to reward multi-year deals, not gross discount-driven close volume.

## Recommendation 4 — Introduce a $240K Enterprise+ tier as anchor

**Rationale**. Pricing Psychology Exposure Test (Segment 4) found Enterprise functions as the ceiling, not as an anchor. Pro carries the buying weight (71% of new deals) but has no tier above it that visibly pushes against. Adding a fourth tier above Enterprise anchors the full pricing page and reframes Enterprise as the rational mid-premium choice rather than the top.

**Structure**. Enterprise+ at $240K list. Bundled with: dedicated CSM, SLA upgrade, multi-region admin console, custom SSO/SCIM, white-glove onboarding. Real product, not a phantom tier — needs to be sellable to the top 5% of accounts. Estimated 4-8 deals/year at this tier in the first 18 months.

**NRR impact estimate**. Direct revenue contribution modest (~$1-2M ACV in year 1). Indirect anchoring effect on Enterprise close rates and effective discount % is the primary value — estimated 2-3 percentage point improvement in Enterprise effective discount within 6 months of launch.

**Rollout sequence**. Build the Enterprise+ bundle definition (Product + CS, 45 days). Soft-launch to top-20 prospect list at day 60. Public pricing page update at day 90.

**Risk**. Tier introduced without real differentiation gets read as a fake anchor and destroys credibility. Mitigation: ship two of the Enterprise+ features (multi-region admin, dedicated CSM tier) as real, sellable capabilities before launch.

## Recommendation 5 — Add expansion-revenue pathway with in-tier upgrades

**Rationale**. The 2025 expansion ratio was 8% against a 25% target. The architecture has no in-tier upgrade mechanic; growth happens only at tier boundaries (Starter→Pro→Enterprise), which are too steep (see AlpineClinic lost-deal verbatim). In-tier modules — multi-location dashboard, advanced reporting, integrations bundle, compliance pack — give CS a $4K-$12K expansion conversation that does not require a tier jump.

**Structure**. Four add-on modules, each priced $4K-$12K/yr, attachable to any tier. Each maps to a real CS use case so the upsell is value-led, not packaging-led.

**NRR impact estimate**. Recovers ~5-7 NRR points within 12 months by activating the missing expansion path. Combined with Recommendation 1 (clean bands above 100 providers) and Recommendation 2 (usage overages), the architecture can produce the 25% expansion target.

**Rollout sequence**. Define the four modules (Product, 30 days). Pilot two of the four with the top-30 CS-managed accounts (60 days). Roll out remaining two and open to all accounts at day 90.

**Risk**. Modules cannibalize Enterprise tier deals if positioned as substitutes rather than complements. Mitigation: CS owns module sales motion in existing accounts; Sales sells full tiers in new business. Clear lane separation in the comp plan.

## Combined NRR Recovery Trajectory

Stacking the five recommendations, with realistic execution risk discounted:

- Current NRR: **96%** (Q1 2026)
- 6-month target: **104%** (architecture changes live, ad-hoc discount class eliminated)
- 12-month target: **112%** (usage-based component and modules contributing; Enterprise+ anchor effect compounding)
- 18-month target: **118%+** (back inside the band Helix told the board it was already in)

The 22 NRR points of recovery (96% → 118%) is the difference between Helix walking into the next raise as a structurally-broken account base and walking in as a vertical-native premium with a working expansion engine.

---

*Produced by Resilience Stack v1.5 · pricing-authority-diagnostic · CC BY 4.0 · petrichorgrowth.com*
