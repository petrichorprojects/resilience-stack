# Quiz Spec — investor-story-forensics

## Tool: Tally.so (free tier)
## URL: https://tally.so/r/ob5gjM
## Title: "Does your investor narrative survive forensic examination?"

## v1 Implementation Status (2026-05-18)

- Live form captures: email, first name, 5 multi-choice answers (Q1-Q5)
- **Deferred to v1.1**: per-Q calc rules + 4 conditional thank-you tier sections (Defensible / Fragile / Vulnerable / Indefensible)
- **v1 routing**: Tally captures raw responses → Beehiiv automation scores + tier-routes drips

## Why this quiz exists

This quiz diagnoses whether a Series-stage operator's investor narrative will survive forensic diligence — the version of diligence sophisticated partners run when a round is real, the QoE provider has been engaged, and the reference calls are actually placed. Five questions map to the five fault lines that produce term-sheet drops, valuation cuts, and pulled rounds: trailing-data truth, reference-customer readiness, bear-case honesty, split-room consistency, and trajectory-shape match. The composite score routes the respondent into one of four integrity tiers, and the tier determines what happens next: a manifesto read, the kit plus a five-day drip, the kit plus a private Loom, or Phil personally reaching out inside 48 hours.

The quiz is a triage tool, not a content asset. Its only job is to put operators 8-14 months out from a Series B or Series C raise — the window where the gap between the pitched story and the auditable story is still movable — into the right tier fast enough that we stop wasting their time and ours.

## 5 Diagnostic Questions

1. **Trailing-Data Truth — "Are the metrics in your investor deck (NRR, growth rate, retention) from trailing four quarters or best-quarter snapshots?"**
   - Trailing four-quarter only, no snapshots — 0 pts (the deck and the data room agree)
   - Mostly trailing, one or two best-quarter highlights — 1 pt (defensible but fragile under QoE)
   - Mix of trailing and best-quarter, no labels — 2 pts (the reconciliation conversation will be ugly)
   - Best-quarter snapshots framed as steady-state — 3 pts (the deck and the trailing data tell different stories)

2. **Reference Customer Readiness — "If a partner called all five of your deck-named reference customers tomorrow, what would they say?"**
   - All five would confirm the story exactly as the deck tells it — 0 pts (references rehearsed and current)
   - Most would confirm; one or two have minor drift — 1 pt (manageable, briefable)
   - Some would confirm, but champion changes or paused contracts we haven't tracked — 2 pts (the call will surface what the deck does not)
   - Don't know — we have not contacted them in 90+ days — 3 pts (the references are a question mark, not an asset)

3. **Bear Case Honesty — "Has someone on your team written the most credible short thesis a sophisticated investor would write against you?"**
   - Yes, painfully honest, every weakness on the page — 0 pts (you can defend what you have already named)
   - Yes, but sanitized for executive comfort — 1 pt (it will not survive partner cross-examination)
   - Started but parked — nobody owns finishing it — 2 pts (the gap is real and someone will write it for you)
   - No, never written — 3 pts (the investor's bear case will be the first version your team sees)

4. **Split-Room Test — "If we split your leadership team in half and each half told the company story independently for thirty minutes, would they tell the same story?"**
   - Yes, confidently — same numbers, same arc, same emphasis — 0 pts (operational alignment)
   - Mostly — minor divergence on emphasis, not facts — 1 pt (rehearsable)
   - Probably not — sales would tell a different story than finance — 2 pts (the partners will hear the divergence)
   - Definitely not — the founder's story and the executives' story are different stories — 3 pts (the diligence call will end early)

5. **Trajectory Shape — "Does your claimed trajectory shape (linear, J-curve, step-function) match the actual shape of your trailing-data growth?"**
   - Match exactly — claimed shape and actual shape are the same — 0 pts (the story is the data)
   - Close — claimed slightly more aggressive than actual — 1 pt (defensible with a forward narrative)
   - Off by one shape — claiming J-curve, trailing is linear — 2 pts (partners will model the trailing shape)
   - Don't know — nobody has plotted the actual shape — 3 pts (the QoE will plot it for you, badly)

## Scoring Rubric

### Tier 0 — Defensible (0–3 points)

**Result page copy:**

Your investor narrative would survive forensic diligence today. Your deck metrics are trailing-four-quarter, not cherry-picked from a peak window. Your reference customers would confirm the story if a partner called tomorrow. Someone on your team has written the painfully-honest bear case, and you have an answer for every line in it. Your leadership team would tell the same story in a split-room test. Your claimed trajectory shape matches the shape your trailing data actually traces.

You do not have an investor-story-forensics problem. What you have is a maintenance problem. Narrative integrity is not a fundraise-prep checkbox — it is a quarterly discipline. The companies that walk into Series C with a forensically clean story are the companies that ran the Narrative Due Diligence Protocol on a 90-day cadence between rounds, not the companies that pulled an all-nighter the week before partner meetings. Between fundraises, reference customers move on. Champions leave. The peak quarter recedes into the trailing data. The bear case ages. The split-room divergence widens silently.

Two actions:

1. Read the Resilience Stack manifesto. It explains why narratives that were honest at the time of the last round drift into "technically true, not defensible" by the time of the next one, and why the gap is invisible from the inside. Twenty minutes. No pitch at the end.
2. Bookmark the investor-story-forensics kit in the repo. Run the Cross-Examination Protocol and the Split-Room Test as a 90-minute internal exercise every quarter. If two of the five signals in this quiz slip, that is your trigger to run the full forensic audit before you open the next data room.

You do not need a call. You need a quarterly calendar reminder.

**Beehiiv list:** `investor-story-forensics-leads`
**Email sequence trigger:** tier-0-defensible
**5-email drip topic:**
1. Why investor narratives decay between rounds even when the numbers are healthy
2. The 5 fault lines of forensic diligence and how to monitor each one
3. The 90-minute quarterly self-check (Cross-Examination + Split-Room)
4. Case: how a Series B SaaS caught Tier 0 drift before Series C kickoff
5. When to escalate from quarterly self-check to a full forensic audit

---

### Tier 1 — Vulnerable (4–7 points)

**Result page copy:**

One or two of your forensic fault lines have started moving. The pattern is not yet visible in partner meetings — the deck still reads clean, the team still believes the story, the data room has not been opened to a serious diligence team yet. But underneath, the pitched narrative and the auditable narrative are no longer the same narrative. A trailing-data line has slipped behind the snapshot version. A reference customer has had a champion change you have not yet tracked. The bear case was started and parked. The split-room test would now produce visible divergence on at least one major claim.

This is what a Vulnerable investor narrative looks like 8-14 months before the round it would otherwise blow up. The window to close the gap cheaply is open right now and closes the day the partner meetings start. Companies that catch it here usually need a focused forensic audit and a reconstructed Investor Narrative Brief with claim-evidence anchors — not a fundraise consultant, not a new deck designer, not a banker.

Two actions:

1. Download the investor-story-forensics kit. Run the full diagnostic against your current deck, your top five named reference customers, and your trailing four quarters of operating data. Block 3 hours. Bring your CEO, CFO, and head of customer success — the audit does not work without all three in the room.
2. Re-test the same five questions 30 days after you ship the reconstructed Investor Narrative Brief. If two scores improved, you caught it in time. If not, escalate.

You probably do not need a Petrichor engagement. You need a focused internal session with the right artifact at the end.

**Beehiiv list:** `investor-story-forensics-leads`
**Email sequence trigger:** tier-1-vulnerable
**5-email drip topic:**
1. Kit delivery + the 9 forensic segments, in order
2. How to run the Cross-Examination Protocol in 45 minutes
3. The Split-Room Test — facilitation script and what to watch for
4. Case: how Aperture (anonymized) caught Tier 1 vulnerability 10 months before Series C
5. How to tell whether your reconstructed Investor Narrative Brief actually improved integrity

---

### Tier 2 — Cracking (8–11 points)

**Result page copy:**

Three or more of your forensic fault lines are flashing. Trailing-quarter data is materially behind the snapshot you have been pitching. At least two of your five named reference customers have had champion changes, paused contracts, or pilot churn you have not tracked. The bear case is unwritten or sanitized to the point of uselessness. The split-room test would produce a story divergence your CFO and head of sales can already feel in finance meetings. Your claimed trajectory shape and your trailing trajectory shape are no longer the same shape. This is the stage where the story still feels true to the people who pitched it and has stopped being defensible to anyone reading the data room cold — including the partner who will ask why NRR-claimed is 130% and NRR-trailing is 117%.

At Tier 2, a kit alone is rarely enough. The forensic audit will name the cracks precisely — that is what it is built for. But the reconstruction usually requires uncomfortable conversations across leadership about which claims are still true, which were true once, and which were never true on a trailing basis. The Investor Narrative Brief plus the Claim-Evidence Matrix is what makes the gap movable. Building it well requires a third party in the room.

Two actions:

1. Download the kit and run the diagnostic before any call. The Claim-Evidence Matrix tells you which of your top fifteen narrative claims are 0/3 (no evidence), 1/3 (anecdotal), 2/3 (one verifiable source), or 3/3 (multi-source, trailing, defensible). Bring this to the conversation.
2. I am sending you a private Loom inside the welcome email. Six minutes. It walks through the Aperture worked example — industrial QA SaaS, $42M ARR, 14/30 Vulnerable scorecard, the +95% growth claim that was actually +68% on trailing, the reference customers nobody had called in 90 days. Watch it before you do anything else with this score.

The Loom is not a sales pitch. It is the same diagnostic vocabulary we will use if and when you book a call. If after watching it you think the kit alone is enough, run it yourself — that is the deal.

**Beehiiv list:** `investor-story-forensics-leads`
**Email sequence trigger:** tier-2-cracking
**5-email drip topic:**
1. Kit + Claim-Evidence Matrix + private Loom link, sent within 60 seconds
2. The Investor Archetype Calibrator — what the platform partner asks vs the growth lead vs the conviction partner
3. Case: Aperture's Tier 2 scorecard and the three 30-day reconstruction actions
4. What a Petrichor investor-story-forensics engagement looks like end-to-end
5. What to bring to the triage call if you book one

---

### Tier 3 — Collapsed (12–15 points)

**Result page copy:**

This is not vulnerability and it is not cracking. The narrative has collapsed. Best-quarter snapshots are framed in the deck as steady-state. You have not contacted your named reference customers in over 90 days. The bear case has never been written. The split-room test would produce two visibly different companies. Your claimed trajectory shape has not been plotted against your actual trailing-data shape. If you are anywhere near opening a Series B or Series C data room in the next two quarters, the diligence call you are about to take will not survive the partner reading the trailing numbers next to the deck.

This is also the stage where the cost of waiting compounds the fastest. A partner walking out citing "narrative inconsistency" — code for "we could not reconcile what the deck claimed with what the QoE produced" — costs a valuation turn. Two partners walking out costs the round. A reference call that surfaces a paused contract the founder did not flag in advance costs the relationship and the round and the reputation. The path out of Tier 3 is not a quiz, a kit, or a drip — it is a structured forensic engagement that produces a reconstructed Investor Narrative Brief with claim-evidence anchors before the next partner meeting, not after.

One action:

1. I will respond personally within 48 hours of your submission. The Loom in your welcome email is mine — six minutes, the Aperture case, the cracks and the reconstruction from 14/30 Vulnerable to 21/30 Defensible. Watch it before we talk. If Petrichor is not the right team for your situation, the call ends with two names that are. That is the deal.

You do not need to download the kit before we talk. You can — it is the same diagnostic vocabulary I will use — but the kit is not the path out of Tier 3. The path out is the engagement, and the only question worth answering on the call is whether we are the right team to run it.

**Beehiiv list:** `investor-story-forensics-leads`
**Email sequence trigger:** tier-3-collapsed
**5-email drip topic:**
1. Calendar link + private Loom + 48-hour Phil response confirmed
2. What a Tier 3 forensic reconstruction engagement looks like (scope, timeline, deliverables)
3. Case: a Series-B SaaS that took the Tier 3 call 10 months before Series C and what changed
4. The three signals that confirm Tier 3 vs severe Tier 2
5. Who else to call if Petrichor is not the right fit

## Email capture

- **Beehiiv list:** `investor-story-forensics-leads`
- **Fields:** first name, email. Nothing else.
- **Welcome email:** triggers a personalised summary of the tier result + direct kit link (Tiers 0-2) or calendar link plus private Loom (Tiers 2-3). Sent within 60 seconds of submission.

## Lead routing

- **Tier 0 (Defensible, 0-5):** Add to Beehiiv list. Trigger tier-0-defensible drip. No human follow-up.
- **Tier 1 (Vulnerable, 6-10):** Add to Beehiiv list. Trigger tier-1-vulnerable drip. Email-only follow-up. No human outreach.
- **Tier 2 (Cracking, 11-15):** Add to Beehiiv list. Trigger tier-2-cracking drip. Private Loom in the welcome email. No proactive outbound from Phil unless the respondent books.
- **Tier 3 (Collapsed, 16-20):** Add to Beehiiv list. Trigger tier-3-collapsed drip. Phil personal email + Loom outreach within 48 hours of submission. Calendar link in the welcome email.

## QA checklist (before going live)

- [ ] Tested end-to-end by 3 non-team reviewers across all 4 score tiers
- [ ] Score thresholds verified — no respondent path lands on the wrong tier (boundary tests at 5/6, 10/11, 15/16)
- [ ] Beehiiv integration confirmed and tier-specific drips load against the correct list segment
- [ ] No PII collected beyond email + first name; no comment-bait or fake-urgency copy anywhere in the form, result pages, or drip sequences
- [ ] Tier 3 routing confirmed against Phil's inbox — 48-hour SLA is real, not aspirational

---

*Resilience Stack quiz · CC BY 4.0 · Petrichor Projects*
