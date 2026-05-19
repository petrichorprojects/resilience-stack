# Quiz Spec — competitive-narrative-stress-test

## Tool: Tally.so (free tier)
## URL: https://tally.so/r/jaJg86
## Title: "Can your competitive narrative survive a competitor's best day?"

## v1 Implementation Status (2026-05-18)

- Live form captures: email, first name, 5 multi-choice answers (Q1-Q5)
- **Deferred to v1.1**: per-Q calc rules + 4 conditional thank-you tier sections (Holding / Fragile / Outflanked / Collapsed)
- **v1 routing**: Tally captures raw responses → Beehiiv automation scores + tier-routes drips

## Why this quiz exists

This quiz diagnoses how exposed a respondent's competitive narrative is to attack from a sharper-positioned competitor. Five questions map to the five attack surfaces of the Narrative Attack Surface framework: win-rate trend, competitor-verbatim discipline, future-claim survivability, outcome-methodology evidence, and oral delivery under pressure. The composite score routes the respondent into one of four durability tiers, and the tier determines what happens next: a manifesto read, the kit plus a five-day drip, the kit plus a private Loom, or Phil personally reaching out inside 48 hours.

The quiz is a triage tool, not a content asset. Its only job is to put operators heading into a Series B raise, an analyst briefing, or a board confrontation about a category reframe into the right tier — fast enough that we stop wasting their time and ours.

## 5 Diagnostic Questions

1. **Win Rate Trend — "How has your competitive win rate (head-to-head deals) trended over the last two quarters?"**
   - Stable or up — 0 pts (narrative is holding)
   - Down 5–15% — 1 pt (early erosion, attributable to noise)
   - Down 16–30% — 2 pts (pattern is forming, attributable to a competitor)
   - Down 30% or more — 3 pts (narrative has been outflanked; the room knows it)

2. **Competitor Verbatim — "When was the last time someone on your team read a competitor's full pitch deck — word-for-word, not summarized?"**
   - In the last 30 days — 0 pts (live competitive surveillance)
   - 30–90 days ago — 1 pt (stale but recent)
   - 90+ days ago — 2 pts (you are arguing against a competitor you no longer know)
   - Never — 3 pts (the narrative is built against an imagined opponent)

3. **Future Claim Survivability — "Pick the line: a buyer asks 'okay, but how' after your strongest future-state claim. What happens next?"**
   - Specific 12-month roadmap with proof points — 0 pts (claim is anchored)
   - Generic answer about innovation or AI — 1 pt (claim drifts under follow-up)
   - Buyer changes the subject — 2 pts (silent disqualification has begun)
   - Sales rep doesn't know — 3 pts (claim has no internal owner)

4. **Outcome Methodology — "Is the methodology behind your strongest customer-outcome claim (e.g., '$12M saved,' '40% lift') publicly published?"**
   - Yes, with at least two case studies showing the math — 0 pts (claim is defensible)
   - Partially — public claim, no public methodology — 1 pt (claim survives until pressed)
   - Methodology exists internally only — 2 pts (claim collapses under analyst scrutiny)
   - No documented methodology, public or internal — 3 pts (the claim is folklore)

5. **60-Second Delivery — "Could your CEO deliver your competitive narrative cold, in 60 seconds, under hostile questioning from an analyst or board member?"**
   - Yes, confidently — 0 pts (narrative is operational, not aspirational)
   - Probably, with a beat of preparation — 1 pt (narrative is fragile under cold delivery)
   - Unsure — 2 pts (narrative has not been rehearsed under pressure)
   - No — 3 pts (the narrative exists only on the slide)

## Scoring Rubric

### Tier 0 — Holding (0–3 points)

**Result page copy:**

Your competitive narrative is doing the work it is supposed to do. Win rate is stable. Someone on the team is reading competitor decks in something close to real time. Your strongest future-state claim has a real twelve-month roadmap behind it. Outcome claims are anchored to public methodology. Your CEO can deliver the narrative cold without breaking a sweat.

You do not have a competitive-narrative problem right now. What you have is a maintenance problem. The Narrative Attack Surface is not a one-time audit — it is a quarterly discipline. Narratives drift from buyer language and analyst language inside a single quarter if nobody is watching. The companies that hold the line do it because someone runs the Blank Check Test every quarter, not because they got it right once.

Two actions:

1. Read the Resilience Stack manifesto. It explains why competitive narratives decay even when the business is healthy, and why the gap is invisible until a competitor surfaces it for you. Twenty minutes. No pitch at the end.
2. Bookmark the competitive-narrative-stress-test kit in the repo. Run the Attack Surface Mapping and 60-Second Delivery Test as a 45-minute internal exercise every quarter. If two of the five signals in this quiz slip, that is your trigger to run the full audit.

You do not need a call. You need a calendar reminder.

**Beehiiv list:** `narrative-stress-test-leads`
**Email sequence trigger:** tier-0-holding
**5-email drip topic:**
1. Why competitive narratives decay even when win rate looks fine
2. The 5 attack-surface layers and how to monitor each one
3. The 45-minute quarterly self-check (Attack Surface + 60-Second Delivery)
4. Case: how a Series B SaaS caught Tier 0 drift before the next analyst briefing
5. When to escalate from quarterly self-check to the full stress test

---

### Tier 1 — Fragile (4–7 points)

**Result page copy:**

One or two of your attack surfaces have started cracking. The pattern is not yet visible in the boardroom — the deck still reads fine, win rate has slipped but no single deal explains it, the team has not raised a flag. But underneath, the narrative and the competitive reality are no longer telling the same story. A future-state claim has started drifting under follow-up. Your sales team has stopped reading competitor decks in full. The outcome number on slide twelve has lost its methodology trail.

This is what a Fragile competitive narrative looks like before it becomes a Series B problem or a Gartner-downgrade problem. The window to close it cheaply is short. Companies that catch it here usually need a focused 2.5-hour stress test and a reconstructed narrative with proof anchors — not a category re-launch, not a rebrand, not a new agency.

Two actions:

1. Download the competitive-narrative-stress-test kit. Run the full diagnostic against your current narrative, your top 3 competitors' verbatim decks, and your last 5 lost-deal post-mortems. Block 2.5 hours. Bring your CEO, your head of sales, and your head of product — the stress test does not work without all three in the room.
2. Re-test the same five questions 30 days after you ship the reconstructed narrative. If two scores improved, you caught it in time. If not, escalate.

You probably do not need a Petrichor engagement. You need a focused internal session with the right artifact at the end.

**Beehiiv list:** `narrative-stress-test-leads`
**Email sequence trigger:** tier-1-fragile
**5-email drip topic:**
1. Kit delivery + the 9 stress-test segments, in order
2. How to run the Blank Check Test in 30 minutes
3. The 60-Second Delivery Test — what hostile questioning sounds like
4. Case: how Tessera (anonymized) caught Tier 1 fragility 90 days before a Series B raise
5. How to tell whether your reconstructed narrative actually improved durability

---

### Tier 2 — Cracking (8–11 points)

**Result page copy:**

Three or more of your attack surfaces are flashing. Win rate has dropped meaningfully against a single competitor over two quarters. Your team has not read that competitor's deck in 90+ days. Your strongest future-state claim collapses under a single "okay, but how." Your outcome claim has no published methodology. This is the stage where the narrative still feels true to the people who wrote it and has stopped being defensible to anyone reading it cold — including, increasingly, your own board.

At Tier 2, a kit alone is rarely enough. The stress test will name the cracks precisely — that is what it is built for. But the reconstruction usually requires uncomfortable conversations across leadership about what is true versus what is rehearsed, and a self-serve kit cannot run those for you. The Reconstructed Narrative plus the CEO Briefing Document is what makes the gap movable. Building it well requires a third party in the room.

Two actions:

1. Download the kit and run the diagnostic before any call. The Attack Surface Assessment tells you which of the five layers are most exposed and what the composite Durability Score is. Bring this to the conversation.
2. I am sending you a private Loom inside the welcome email. Six minutes. It walks through the Tessera worked example — Tier 2, win rate 52% → 31%, narrative reframed from "retail operating system" to "retail data layer agents need." Watch it before you do anything else with this score.

The Loom is not a sales pitch. It is the same diagnostic vocabulary we will use if and when you book a call. If after watching it you think the kit alone is enough, run it yourself — that is the deal.

**Beehiiv list:** `narrative-stress-test-leads`
**Email sequence trigger:** tier-2-cracking
**5-email drip topic:**
1. Kit + Attack Surface Assessment + private Loom link, sent within 60 seconds
2. The Competitor's Best Day Simulation — how to run it without flinching
3. Case: Tessera's Tier 2 scorecard and the three 30-day reconstruction actions
4. What a Petrichor competitive-narrative engagement looks like end-to-end
5. What to bring to the triage call if you book one

---

### Tier 3 — Collapsed (12–15 points)

**Result page copy:**

This is not fragility and it is not cracking. The narrative has collapsed. Win rate has fallen off a cliff against a specific competitor. Nobody on the team has read that competitor's full pitch in months. Your future-state claim cannot be defended past one follow-up question. Your outcome claim has no published methodology and no internal owner. Your CEO cannot deliver the narrative cold under pressure. If you are anywhere near a Series B raise, an analyst briefing, or a board conversation about why the category is moving without you in the next two quarters, the competitive narrative you are about to tell will not survive the room it is told in.

This is also the stage where the cost of waiting compounds the fastest. A Gartner reframe that catches you flat-footed costs a category. Three board members independently asking "why aren't we agentic?" costs a CEO. The path out of Tier 3 is not a quiz, a kit, or a drip — it is a structured engagement that produces a reconstructed narrative with proof anchors before the next external conversation.

One action:

1. I will respond personally within 48 hours of your submission. The Loom in your welcome email is mine — six minutes, the Tessera case, the cracks and the reconstruction. Watch it before we talk. If Petrichor is not the right team for your situation, the call ends with two names that are. That is the deal.

You do not need to download the kit before we talk. You can — it is the same diagnostic vocabulary I will use — but the kit is not the path out of Tier 3. The path out is the engagement, and the only question worth answering on the call is whether we are the right team to run it.

**Beehiiv list:** `narrative-stress-test-leads`
**Email sequence trigger:** tier-3-collapsed
**5-email drip topic:**
1. Calendar link + private Loom + 48-hour Phil response confirmed
2. What a Tier 3 reconstruction engagement looks like (scope, timeline, deliverables)
3. Case: a retail-analytics SaaS that took the Tier 3 call 90 days before Series B and what changed
4. The three signals that confirm Tier 3 vs severe Tier 2
5. Who else to call if Petrichor is not the right fit

## Email capture

- **Beehiiv list:** `narrative-stress-test-leads`
- **Fields:** first name, email. Nothing else.
- **Welcome email:** triggers a personalised summary of the tier result + direct kit link (Tiers 0–2) or calendar link plus private Loom (Tiers 2–3). Sent within 60 seconds of submission.

## Lead routing

- **Tier 0 (Holding, 0–3):** Add to Beehiiv list. Trigger tier-0-holding drip. No human follow-up.
- **Tier 1 (Fragile, 4–7):** Add to Beehiiv list. Trigger tier-1-fragile drip. Email-only follow-up. No human outreach.
- **Tier 2 (Cracking, 8–11):** Add to Beehiiv list. Trigger tier-2-cracking drip. Private Loom in the welcome email. No proactive outbound from Phil unless the respondent books.
- **Tier 3 (Collapsed, 12–15):** Add to Beehiiv list. Trigger tier-3-collapsed drip. Phil personal email + Loom outreach within 48 hours of submission. Calendar link in the welcome email.

## QA checklist (before going live)

- [ ] Tested end-to-end by 3 non-team reviewers across all 4 score tiers
- [ ] Score thresholds verified — no respondent path lands on the wrong tier (boundary tests at 5/6, 10/11, 15/16)
- [ ] Beehiiv integration confirmed and tier-specific drips load against the correct list segment
- [ ] No PII collected beyond email + first name; no comment-bait or fake-urgency copy anywhere in the form, result pages, or drip sequences
- [ ] Tier 3 routing confirmed against Phil's inbox — 48-hour SLA is real, not aspirational

---

*Resilience Stack quiz · CC BY 4.0 · Petrichor Projects*
