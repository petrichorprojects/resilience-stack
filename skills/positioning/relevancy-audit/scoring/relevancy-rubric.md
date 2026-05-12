# Relevancy Audit — Scoring Rubric

## Overview
All scores use evidence from the participant's own responses. Never assign a score without citing the specific answer that drove it.

---

## Phase 2: Customer Amnesia Test

### Description Gap (1-10)
How far apart is how customers describe them vs. how they describe themselves?

| Score | Criteria | Evidence Pattern |
|-------|----------|-----------------|
| 1-2 | **Aligned.** Customer language matches current positioning. | Participant says customers would use the same terms the company uses. No lag between internal and external language. |
| 3-4 | **Minor drift.** Customers use slightly outdated language but capture the core value. | "They'd probably say [old tagline] but they'd also mention [current capability]." Minor vocabulary gap. |
| 5-6 | **Material drift.** Customers describe the company that existed 1-2 years ago. | Participant acknowledges customer perception is "a version behind." The company has evolved but the market's mental model hasn't. |
| 7-8 | **Disconnected.** Customer description misses current differentiation entirely. | Participant can't confidently predict what customers would say, or predicts something materially different from current positioning. |
| 9-10 | **Invisible.** Customers can barely articulate what the company does. | "They'd probably just say we're a [generic category] company." Zero differentiation in customer perception. |

### Value Decay (1-10)
How much has the original reason customers chose them been commoditized?

| Score | Criteria | Evidence Pattern |
|-------|----------|-----------------|
| 1-2 | **Original differentiation holds.** No competitor has matched the reason customers chose them. | "We won because of [X] and no one else does [X] yet." Clear, specific, defensible. |
| 3-4 | **Slight erosion.** 1-2 competitors now offer similar capability. | "A couple of competitors have started doing [X] but we're still ahead." Gap is closing. |
| 5-6 | **Partially commoditized.** The original "why us" is now common but execution quality still differs. | "Everyone claims [X] now, but we're better at it." The differentiation has shifted from "we have it" to "we do it better" — a weaker position. |
| 7-8 | **Largely commoditized.** The original differentiator is now table stakes. | "I think customers chose us because of [security/reliability/ease of use]." These are expected features, not differentiators. |
| 9-10 | **Fully commoditized.** The original reason to choose is now the minimum bar for every competitor. | Participant struggles to name what originally differentiated them, or names something every competitor now offers. |

### Consideration Risk (1-10)
How likely are customers to consider alternatives if re-evaluating today?

| Score | Criteria | Evidence Pattern |
|-------|----------|-----------------|
| 1-2 | **Loyal with conviction.** Customers would choose again without hesitation. | Participant is confident customers would say "absolutely" with no qualifiers. Can name specific reasons. |
| 3-4 | **Loyal with minor exploration.** Would choose again but would do a quick market scan. | "They'd probably still choose us but they'd look at what else is out there." |
| 5-6 | **Loyal with inertia.** Staying because switching is hard, not because conviction is strong. | "They're staying because of integrations/contracts/switching costs." Renewal ≠ conviction. |
| 7-8 | **At risk with trigger events.** One catalyst (contract renewal, new leadership, competitor outreach) could shift them. | Participant mentions competitors customers have brought up. "We've heard [Competitor X] mentioned a few times." |
| 9-10 | **Actively at risk.** Customers are already evaluating or would seriously consider alternatives immediately. | "To be honest, I think a few would look at [Competitor] seriously." Or: can't articulate why customers would stay. |

---

## Phase 3: Market Archaeology

### Detection Speed (1-5)

| Score | Criteria |
|-------|----------|
| 1 | **Blind.** Last to know about market shifts. Learns from customers or press after competitors have already repositioned. Average detection lag: 9+ months. |
| 2 | **Slow.** Detects shifts 6-9 months after first signals. No formal signal monitoring. Relies on anecdotal observation. |
| 3 | **Average.** Detects within 3-6 months. Has some monitoring but it's informal or inconsistent. |
| 4 | **Fast.** Detects within 1-3 months. Has deliberate signal monitoring (competitor tracking, customer advisory board, analyst relationships). |
| 5 | **Leading.** Detects shifts before competitors. Often identifies signals before the market consensus. Has systematic signal detection infrastructure. |

### Response Speed (1-5)

| Score | Criteria |
|-------|----------|
| 1 | **Frozen.** 12+ months to meaningful change after detection. Organizational inertia, consensus-seeking, or denial prevents action. |
| 2 | **Slow.** 6-12 months. Acknowledges shifts but decision-making is slow. Multiple approval layers or "let's watch it" culture. |
| 3 | **Moderate.** 3-6 months. Can mobilize but requires significant internal alignment before acting. |
| 4 | **Fast.** 1-3 months. Leadership can make positioning decisions quickly. Has authority concentrated enough to act. |
| 5 | **Immediate.** Under 1 month. Treats signal detection as a trigger for action, not discussion. Small team or decisive leadership. |

---

## Phase 5: Competitive Relevancy Map

### Dimension Scoring

For each of the 6 dimensions, score the gap between the company's position and where the market is heading:

| Gap Score | Meaning |
|-----------|---------|
| **Ahead** | Company is positioned closer to market direction than competitors. Relevancy advantage. |
| **Aligned** | Company is tracking with market direction. No decay on this dimension. |
| **Behind (minor)** | Market is moving and company hasn't adjusted yet, but gap is small (< 6 months of drift). |
| **Behind (major)** | Competitors are materially closer to where market is heading. Active decay zone. |
| **Displaced** | Company's position on this dimension is no longer part of the market conversation. |

Dimensions scored as "Behind (major)" or "Displaced" = **Active Decay Zones**.

---

## Phase 6: Decay Rate — Stage Classification

### Stage Determination

Use the weight of evidence across all phases:

**Stage 1: Drift**
- Description Gap: 3-5
- Value Decay: 3-5
- Detection Speed: 3+
- 0-1 Active Decay Zones
- Signals are present but individually explainable
- Revenue metrics show slight softening, nothing alarming

**Stage 2: Disconnect**
- Description Gap: 5-8
- Value Decay: 5-8
- Detection Speed: 1-3
- 2-3 Active Decay Zones
- Competitors using language the company doesn't
- Customers mention alternatives or hesitate on re-evaluation
- Revenue showing clear pattern (win rate, cycle length, pipeline quality)

**Stage 3: Displacement**
- Description Gap: 8-10
- Value Decay: 8-10
- Multiple Active Decay Zones
- Market conversation happening without them
- Consideration rates collapsing (not just losing deals — not being invited)
- Talent starting to leave for "more relevant" companies

### Decay Clock Calculation

```
If Stage 1 (Drift):
  Base = (10 - Description Gap) × 3
  Adjustment = -(Average Response Lag in months)
  Months to Disconnect = max(3, min(24, Base + Adjustment))

If Stage 2 (Disconnect):
  Base = (10 - Description Gap) × 2
  Adjustment = -(Average Response Lag in months)
  Months to Displacement = max(3, min(24, Base + Adjustment))

If Stage 3 (Displacement):
  Months remaining = "Recovery requires a fundamental repositioning, not incremental adjustment."
  Do not give a number — give the honest assessment that the positioning is already displaced.
```

---

## Signal Prioritization (Phase 7)

### Priority Scoring

For each signal classified as SIGNAL:

| Dimension | 1 | 2 | 3 | 4 | 5 |
|-----------|---|---|---|---|---|
| **Decay Impact** | Minor — affects perception at the margins | Noticeable — drives one decay dimension | Significant — drives 2+ decay dimensions | Major — central to the positioning gap | Critical — if unaddressed, accelerates to next stage |
| **Response Speed** | 12+ months to act | 6-12 months | 3-6 months | 1-3 months | Can act this month |
| **Cost of Delay** | No change if delayed 3 months | Minor — gap widens slightly | Moderate — competitor advantage grows | High — window of opportunity closing | Critical — 3-month delay = irreversible |

**Priority tiers:**
- **Tier 1 (First 30 days)**: Total score 12+ (out of 15)
- **Tier 2 (Days 31-60)**: Total score 9-11
- **Tier 3 (Days 61-90)**: Total score 6-8
- **Park**: Total score under 6
