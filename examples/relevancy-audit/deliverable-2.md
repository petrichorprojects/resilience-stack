# Deliverable 2 — Signal Refresh Roadmap (90 Days)

**Company**: Synthetic Co
**Window**: Days 1-90 from 2026-05-12
**Owners**: VP Marketing (Devan), Head of Sales (Rasheed), Founder/CEO (Maya), Head of Product (Jen)

---

## Action 1 — Positioning Rewrite Using Buyer Language

**Owner**: VP Marketing (Devan)
**Deadline**: 30 days (2026-06-11)
**Tier**: First 30 days — high decay impact, high response speed, high cost of delay

### Rationale
The current positioning ("The leading legal operations platform for modern firms") contains 0 of the top 12 terms buyers use. This is the Stage 3 leading indicator. Until the positioning is rewritten in buyer language, every downstream asset — homepage, decks, paid ads, sales enablement — is mis-tuned. Marketing spend doubled over the last 18 months with flat share-of-voice; the issue is not budget, it is language.

### Steps
1. **Day 1-5**: Lock the top 12 buyer terms (already surfaced). VP Marketing owns the canonical list.
2. **Day 6-10**: Draft 3 candidate positioning statements. Each must contain 6+ of the top 12 terms verbatim.
3. **Day 11-15**: Test candidates with 5 current customers + 5 lapsed prospects (1-question test: "Which of these sounds like what you bought / would buy?").
4. **Day 16-20**: Select winning statement. Founder + VP Marketing sign off.
5. **Day 21-30**: Cascade to homepage hero, sales one-pager, top-of-funnel paid ads, analyst-brief language.

### Success metric
Final positioning statement contains 6 or more of the top 12 buyer terms. Homepage hero updated. Sales one-pager updated. Analyst brief updated.

### Dependencies
- Customer survey verbatim corpus (have it)
- Lapsed prospect contact list (need it — flagged in Phase 1 as a Phase 7 dependency)
- Founder availability for sign-off

### Risk register
- **Risk**: Statement reads as a feature list, not a position. **Mitigation**: every candidate must answer "vs. what alternative" — at least one of LegacyVendor / NewEntrant / InHouse.
- **Risk**: Sales team rejects the rewrite. **Mitigation**: Rasheed is in the room for the Day 16-20 sign-off, not surprised at Day 30.

---

## Action 2 — Competitive Intel Feed on NewEntrant

**Owner**: Head of Sales (Rasheed) + VP Marketing as Product Marketing proxy (Devan)
**Deadline**: 14 days (2026-05-26)
**Tier**: First 14 days — highest cost of delay, structural gap

### Rationale
Three deals lost to NewEntrant in one quarter; NewEntrant did not appear in any win/loss field; sales had no playbook. This is not a sales-execution problem — it is a structural intelligence gap. The fastest way to stop the bleed is to install the feed and recode the loss data.

### Steps
1. **Day 1-3**: Add NewEntrant as a tracked competitor in CRM. Recode the last 4 quarters of win/loss for NewEntrant mentions in verbatim notes (not just the structured field).
2. **Day 4-7**: Build the intel sources — their site, their LinkedIn, their funding announcements, 2 paralegal-community subreddits, G2 reviews. Devan owns weekly digest format.
3. **Day 8-11**: Reps interview the 3 lost-deal contacts (Texas, Florida, NY) for verbatim "why them" — recorded, not paraphrased.
4. **Day 12-14**: First weekly intel digest ships internally. Sales playbook v0.1 ships — minimum: their claim, our counter, 3 questions to ask a prospect who mentions them.

### Success metric
Weekly intel digest live. Win/loss recoded for last 12 months. Sales playbook v0.1 shipped and used in at least 3 live deals by Day 30.

### Dependencies
- CRM admin access
- 3 lost-deal contact warmth (Rasheed owns the asks)
- 60 minutes/week of Devan's time on an ongoing basis

### Risk register
- **Risk**: Intel digest becomes noise — too much, not actionable. **Mitigation**: digest format is constrained to 1 page, "What changed / What we'll do / What to watch."
- **Risk**: Sales team treats playbook v0.1 as final. **Mitigation**: explicit "v0.1 — expect v0.2 by Day 45" framing.

---

## Action 3 — Validate or Kill the "AI-Native" Claim

**Owner**: Founder/CEO (Maya) + Head of Product (Jen)
**Deadline**: 60 days (2026-07-11)
**Tier**: Days 31-60 — high decay impact, moderate response speed

### Rationale
NewEntrant's positioning is "AI-native legal ops." Three lost deals cite "AI workflow" as the reason. Synthetic Co does not know whether AI workflow is (a) a real buyer priority — in which case Product roadmap must respond, or (b) a marketing claim by NewEntrant that hasn't been validated against actual buying behavior — in which case Marketing/Sales must neutralize the narrative without a Product investment. Spending product cycles on the wrong answer is the most expensive mistake of the next 6 months.

### Steps
1. **Day 31-40**: Run the `customer-truth-extraction` skill. Interview 12 buyers — mix of current customers (6), recent losses (3), active prospects (3). Structured: "Walk me through your last evaluation. Where, if at all, did AI come up?"
2. **Day 41-50**: Code transcripts. Two outcomes: AI workflow is a top-3 buyer priority OR it is a vendor-led narrative not yet matched by buyer demand.
3. **Day 51-55**: Synthesis brief. Founder + Head of Product co-author the verdict. One of two paths:
   - **Validate**: AI workflow goes on the Q3 product roadmap. Marketing tells a real story.
   - **Kill**: Marketing builds the "AI-native is theater" counter-narrative. Sales playbook updates. No product spend.
4. **Day 56-60**: Brief the analyst (Q4 quadrant cycle starts) with the verdict + evidence.

### Success metric
Documented verdict (validate or kill) with 12 buyer transcripts as evidence. Roadmap decision made. Analyst briefed.

### Dependencies
- `customer-truth-extraction` skill (in the Resilience Stack)
- 12 buyer interview slots — Rasheed owns recruitment
- Founder + Head of Product availability for Day 51-55 synthesis

### Risk register
- **Risk**: Interview sample is biased toward current happy customers — no AI gap surfaces. **Mitigation**: enforced mix (6 current / 3 lost / 3 active prospect).
- **Risk**: Verdict is ambiguous (some buyers, not most). **Mitigation**: pre-commit to a decision rule — "AI workflow is a priority if 5+ of 12 buyers cite it unprompted in the top 3 evaluation factors." Decision rule chosen Day 31, not Day 55.

---

## Cross-Action Dependency Map

- Action 1 (positioning rewrite) depends on Action 2 (competitive intel) Days 1-14 to ensure the new statement is positioned against the right alternatives.
- Action 3 (AI-native verdict) potentially triggers a second positioning revision around Day 60-75. Action 1 must produce a v1 statement that is robust to the AI verdict — i.e. does not bet the brand on "AI" before Action 3 lands.
- Maya owns the September board narrative — all three actions feed into it.

## Monthly Decay Check Commitment

First check: 2026-06-12. Recurring monthly. 15 minutes, 5 signals per attendee, one decision per check.

---

*Produced by Resilience Stack v1.2 · relevancy-audit · CC BY 4.0 · petrichorgrowth.com*
