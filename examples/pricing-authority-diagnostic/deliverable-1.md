# Deliverable 1 — Price-Value Gap Assessment

**Company**: Helix
**Sector**: Healthcare scheduling — vertical SaaS for multi-location clinics
**ARR**: $28M (Q1 2026)
**Stage**: 9 quarters post-PMF, ~24 months from next raise
**Audit date**: 2026-05-12

---

## 1. Per-Tier Price/Value Gap

Each tier evaluated on three dimensions: list price vs delivered value, list price vs sold price, and tier-internal coherence (does the buyer in this tier get a meaningfully different product than the tier above/below?).

| Tier | List ($/yr) | Avg sold ($/yr) | Effective discount | Value gap | Verdict |
|------|-------------|-----------------|--------------------|-----------|---------|
| Starter | $12,000 | $11,400 | 5% | **Underpriced ~15%.** Feature parity with LegacyVendor at half their list price. Renewal rate 91%, no price-sensitivity churn last 4 quarters. | Hold list. Modest increase defensible (+8-10%). |
| Pro | $45,000 | $36,000 | 20% | **Priced correctly on paper, eroded by discount practice.** Discount % climbed from 9% (Q1 2025) to 22% (Q1 2026). The list price is sound. The sold price is not. | Hold list. Fix discount discipline before any increase. |
| Enterprise | $120,000 | $94,800 | 21% | **Structurally underpriced above 100 providers.** Per-provider math breaks: buyers above 100 providers refuse to pay 2x for 2x providers and negotiate down. 12 accounts ($4.2M ARR) sit in the broken zone. | Replace value metric before pricing. |

## 2. Value Metric Stress Test Result

The per-provider per-month metric is **defensible up to ~100 providers** and **breaks above**.

**Why it works below 100**: small/mid clinics think of staff count linearly. Adding the 12th provider to a 50-provider clinic feels like 1/50 more cost. Buyer can verify the metric themselves by counting providers in the system. The metric passes Petrichor's defensibility test ("can the buyer verify it themselves?").

**Why it breaks above 100**: large clinic groups think in cohorts and locations, not individual providers. A 200-provider system does not perceive 2x the value of a 100-provider system because the marginal provider contributes less in the buyer's mental model (shared schedulers, shared admin overhead). When the rep quotes $24K/mo for 200 providers, the buyer pushes back. Reps capitulate. The 31% of Q1 2026 discount dollars classified as "structural" sit entirely in this zone.

Product flagged this internally **18 months ago**. No escalation reached pricing or finance. The structural failure was carried as a sales-execution problem until this session.

## 3. Customer Segment Willingness-to-Pay vs Current Price

Segment defined by clinic size (provider count), vertical (specialty vs general), and region.

| Segment | Current avg ACV | Modeled WTP (top quartile) | Gap | Notes |
|---------|-----------------|----------------------------|-----|-------|
| Small general (<25 providers) | $11,400 | $13,500 | **+$2,100 (18%)** | Insensitive to price; renewals driven by switching cost. |
| Mid general (25-100 providers) | $36,000 | $42,000 | **+$6,000 (17%)** | The Pro tier sweet spot. Discounts here are 80% quarter-end, not buyer-driven. |
| Large general (>100 providers) | $94,800 | $112,000-$135,000 | **+$17,000 to +$40,000** | WTP exists. Pricing architecture cannot capture it. |
| Specialty (any size) | $52,000 | $58,000 | **+$6,000 (12%)** | Underserved by tier structure — specialty workflows justify premium that current tiers do not signal. |
| Multi-region (any size) | $88,000 | $104,000 | **+$16,000 (18%)** | Annual + multi-region commitment unpriced. |

## 4. Top 5 Deals Where Buyer Would Have Paid 20%+ More If Asked (Lost Upside)

Five closed-won deals last quarter where post-close customer interviews (conducted by CS for renewal forecasting) revealed the buyer had budget headroom and price was never the binding constraint.

1. **MidwestCare Group** ($82K closed, 18% discount). Buyer comment to CS at 90-day check-in: *"We had $110K budgeted. We told you $80K because that's what you offered first."* Anchor missed. Lost upside: ~$28K.
2. **CoastalSpecialty Partners** ($64K closed, 23% discount). Quarter-end approved. Buyer had not asked for a discount — rep offered 23% on the last day of Q4 to close. Lost upside: ~$19K.
3. **NorthernHealth Network** ($138K closed, 27% discount, 180-provider account). Structural — per-provider math triggered pushback. Buyer would have paid $165K on a tiered band structure. Lost upside: ~$27K.
4. **PineRidge Clinics** ($41K closed, 25% discount). Rep-coded "competitive" — no competing quote in CRM. Lost upside: ~$10K.
5. **MountainStateHealth** ($104K closed, 18% discount, 140-provider account). Same structural pattern as #3 on a smaller scale. Lost upside: ~$18K.

**Aggregate Q1 2026 lost upside on these five deals alone: ~$102K.** Extrapolated across the discount root-cause distribution (Section 3 of Deliverable 3), Helix is leaving an estimated **$1.4M-$1.8M of annual ACV** on the table from discount practice and architecture failure combined.

---

*Produced by Resilience Stack v1.5 · pricing-authority-diagnostic · CC BY 4.0 · petrichorgrowth.com*
