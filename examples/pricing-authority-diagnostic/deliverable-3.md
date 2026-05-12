# Deliverable 3 — Willingness-to-Pay Reality Check

**Company**: Helix
**Audit date**: 2026-05-12
**Data**: 4 quarters of closed-won (n=187 deals), 5 lost-deal interviews, manager-approval timestamps, post-close CS check-in transcripts.

---

## 1. Actual Paid vs List Price by Segment

Effective discount % by segment, Q1 2026, weighted by ACV.

| Segment dimension | Slice | List ACV | Sold ACV | Effective discount |
|-------------------|-------|----------|----------|--------------------|
| **Revenue size** | <$5M clinic revenue | $11,800 | $11,300 | 4% |
| | $5M-$25M | $43,000 | $34,800 | 19% |
| | $25M-$100M | $108,000 | $86,400 | 20% |
| | >$100M | $138,000 | $98,000 | **29%** |
| **Vertical** | General practice | $42,000 | $33,200 | 21% |
| | Specialty (ortho, derm, etc.) | $51,000 | $39,800 | 22% |
| | Multi-specialty system | $114,000 | $86,600 | **24%** |
| **Region** | West | $46,000 | $37,700 | 18% |
| | Midwest | $44,000 | $35,200 | 20% |
| | Northeast | $49,000 | $36,800 | **25%** |
| | South | $43,000 | $36,100 | 16% |

**Pattern**: discount intensifies with deal size and complexity. The >$100M clinic segment carries a 29% effective discount — the exact zone where the per-provider value metric breaks. The Northeast outlier (25%) is a rep-distribution artifact: two of the three highest-discount reps are assigned to that region.

## 2. Discount Root-Cause Recoding (Q1 2026)

The Discount Autopsy (Segment 2) recoded the top 10 deals one by one against deal timelines, manager-approval timestamps, and CRM artifacts. Distribution was then applied across the full Q1 2026 discount pool.

| Root cause | Share of discount $ | Rep-claimed reason this masqueraded as |
|------------|---------------------|----------------------------------------|
| **Quarter-end manager-approved** (rep pressure, not buyer pressure; approval timestamps cluster after 4pm on last 5 business days) | **38%** | Reps coded most of this as "competitive" or "buyer story" |
| **Structural** (value metric breaks at >100 providers; buyer rejected per-provider math; rep capitulated) | **31%** | Coded as "competitive" (because buyer mentioned other vendors during pushback) or "champion ask" |
| **Genuine competitive** (verified LegacyVendor or ScrubsScheduler quote in CRM, dated within 14 days of close) | **19%** | "Competitive" |
| **Other** (legitimate annual commitment swap, multi-year prepay, partner-influenced) | **12%** | Mixed |

**Compare to rep-claimed pre-analysis distribution**:

| Rep-claimed reason | Share |
|--------------------|-------|
| Competitive | 41% |
| Buyer story | 22% |
| Annual commitment | 18% |
| Champion ask | 12% |
| Other | 7% |

**The 41%-to-19% gap on "competitive"** is the headline finding. More than half of what reps called "competitive pressure" was either rep-driven quarter-end pressure or buyer rejection of the broken value metric. The board narrative ("discounts climbing due to competitive pressure") is mechanically wrong.

## 3. Five Lost-Deal Verbatim Buyer Reasons, Classified

Lost-deal interviews conducted by CFO's office (not sales) within 30 days of loss. Verbatim quotes plus root-cause classification.

1. **VerdantHealth Group** (~$95K, 110-provider account, lost to LegacyVendor).
   Buyer: *"Your per-provider price doesn't make sense above our size. LegacyVendor uses tiered bands. We knew what we'd pay at scale. With you we didn't."*
   **Classification: Structural.** Lost on value metric, not price level.

2. **AlpineClinic Network** (~$58K, lost — went with status quo / no purchase).
   Buyer: *"We liked Helix. The Pro tier didn't include the multi-location dashboard, so we'd have to jump to Enterprise. The jump was too steep."*
   **Classification: Architecture gap.** Lost on tier discontinuity, not list price.

3. **PrairieCare Partners** (~$44K, lost to BookCal).
   Buyer: *"You were 40% more. BookCal does enough for our size."*
   **Classification: Genuine competitive.** Helix's Starter is correctly priced; BookCal undercut on a deal where the buyer did not need the premium capability.

4. **Sunrise Clinical** (~$72K, lost to ScrubsScheduler).
   Buyer: *"Both products were fine. Your rep offered 25% off in week three. Their rep said 'this is the price.' I trusted theirs more."*
   **Classification: Discount-discipline failure.** Discount practice signaled weakness. Authority loss directly cost the deal.

5. **HighPlainsHealth** (~$118K, lost — extended evaluation, no decision).
   Buyer: *"Pricing was the answer we got when we asked about value. We never got past pricing."*
   **Classification: Narrative failure.** Sales-led with price; buyer never reached a value frame.

## 4. "Price Was The Reason" vs "We Told Them Price Was The Reason"

When reps lose a deal, the loss-reason field gets filled by the rep. Helix's Q1 2026 loss-reason distribution had price as the #1 cited reason at 47%. The lost-deal interviews above suggest a different picture.

| Rep-coded loss reason | Buyer-verified loss reason | Gap |
|------------------------|----------------------------|-----|
| Price too high | Genuine competitive price gap | ~14 percentage points (of 47% rep-coded, ~14% verified) |
| Price too high | Structural value metric failure | ~12 percentage points (buyer rejected the math, not the magnitude) |
| Price too high | Tier architecture gap (jump too steep) | ~9 percentage points |
| Price too high | Discount discipline failure (rep gave it away, buyer lost trust) | ~7 percentage points |
| Price too high | Narrative failure (never reached value frame) | ~5 percentage points |

**The pattern**: reps code "price" because that is what they hear in the final call. But "price" is the language buyers use to end conversations they have already decided to end for other reasons. The Sunrise Clinical quote (#4) is the clearest evidence — the buyer's stated reason was a 25% discount destroying authority, but the loss code was "price too high."

Helix's pricing is not the primary problem in lost deals. **Pricing architecture, discount discipline, and value narrative are.** Each gets fixed in Deliverable 4.

---

*Produced by Resilience Stack v1.5 · pricing-authority-diagnostic · CC BY 4.0 · petrichorgrowth.com*
