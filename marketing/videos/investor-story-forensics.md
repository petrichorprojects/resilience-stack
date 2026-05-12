# Video Shot List — investor-story-forensics

## Setup

- **Tool:** Loom (free or paid tier — both work)
- **Layout:** screen + camera both on. Webcam small in bottom-right corner.
- **Screen split:**
  - **Left half:** `skills/investor/investor-story-forensics/investor-story-forensics.md` open in the editor (raw, not rendered)
  - **Right half:** Claude Code, with `examples/investor-story-forensics/input.md`, `examples/investor-story-forensics/deliverable-2.md` (Claim-Evidence Matrix), `examples/investor-story-forensics/deliverable-5-scorecard.md`, and `examples/investor-story-forensics/investor-narrative-brief.md` already opened in tabs and ready to surface
- **Audio:** wired mic preferred. AirPods acceptable.
- **Recording mode:** single take, no post-editing.
- **Run-time target:** 5:00. Hard cap at 6:00.
- **Loom URL:** {{loom-url-to-be-added-by-phil}}
- **Loom caption/title:** "Investor Story Forensics walkthrough — Resilience Stack v1.5 Kit 5 (Final)"

## 6 Shots

### Shot 1 — HOOK (30 seconds)

**Camera:** webcam full-frame for this shot. Screen visible behind but not the focus.
**Visual cues:** founder talking head. No slide. No title card. Just face on camera.

**Narration (verbatim):**

"Your deck says one hundred thirty percent NRR. Your trailing-four-quarter NRR is one hundred seventeen. Both numbers can be true on paper. Only one survives diligence. The other ends the round. The investor-story-forensics kit is the diagnostic that catches the gap between the story you are pitching and the story your data room actually tells, ten months before the partner meetings start. Five minutes. Let me show you what it does."

---

### Shot 2 — SKILL STRUCTURE (45 seconds)

**Camera:** screen-focused. Webcam shrinks to corner. Left half (skill markdown) is the focus.
**Visual cues:** scroll through `skills/investor/investor-story-forensics/investor-story-forensics.md`. Pause on the frontmatter. Pause on the "When NOT to use" block. Pause on the 9 facilitation segments.

**Narration (verbatim):**

"The skill file is one markdown document. Top of the file is the frontmatter — name, version, track, when-to-use. Below that, the persona — forensic auditor. The facilitator plays the diligence partner, the QoE provider, the reference-call interviewer. The skill speaks in the partner's voice when cross-examining, not the founder's. That choice matters. Now scroll to the 'When NOT to use' block. Read it aloud. Already inside fourteen days of term sheet, the audit is too late, use deck-coaching instead. Pre-product companies raising on team only, no narrative-data gap to audit yet. Insider rounds where the existing investors already know the warts, the forensic vocabulary creates noise without signal. Companies in the middle of restating their financials, fix the data first. That block exists because the most expensive mistake operators make with this framework is running it on the wrong stage or the wrong round. The skill says no for you, so you do not have to. Below that, nine forensic segments — Narrative Surface Mapping, Claim-Evidence Audit, Cross-Examination Protocol, Split-Room Test, Reference Customer Stress Audit, Bear Case Construction, Investor Archetype Calibrator, QoE Pre-Mortem, Investor Narrative Brief. The order matters. Run in sequence."

---

### Shot 3 — DEMO (90 seconds)

**Camera:** screen-focused. Right half (Claude Code) becomes the focus.
**Visual cues:** open `examples/investor-story-forensics/input.md`. Copy the full contents. Paste into Claude Code with the investor-story-forensics skill loaded. Hit enter. Let the response stream live. Point to the screen as each layer of the Cross-Examination Protocol surfaces and then as the Split-Room divergence is named.

**Narration (verbatim):**

"This is the worked example. Aperture. Industrial QA SaaS. Forty-two million ARR. Series B closed twenty months ago, ten to twelve months from Series C. The deck claims net revenue retention of one hundred thirty percent. The trailing-four-quarter NRR is one hundred seventeen. The deck claims fourteen of twenty-five named OEM accounts. Active production deployments — eleven of twenty-five. The deck claims plus ninety-five percent growth. Trailing growth is plus sixty-eight. Non-automotive vertical has thirty-eight percent pilot churn. Two of five named reference customers have had champion changes in the last six months that nobody has tracked. I am pasting their full intake into Claude Code right now. The skill is loaded. Watch what happens. Claude does not jump to a rewrite. The first thing it does is run the Claim-Evidence Audit. NRR 130% claim — scored zero of three, the trailing data contradicts the snapshot. The 14-of-25 OEM claim — scored one of three, anecdotal. The +95% growth claim — scored zero of three, the trailing shape is materially different from the claimed shape. Then the Cross-Examination Protocol — Claude asks the partner-voice question: how do you reconcile +130 NRR claimed with +117 trailing? Then it runs the Split-Room Test. Sales tells the story one way — plus ninety-five percent growth is realistic, the pipeline supports it. Finance tells it another — plus ninety-five percent is a stretch case, the base case is plus sixty-eight. Divergence on the most important number in the deck. Composite Narrative Integrity — fourteen of thirty. Vulnerable. This is what the skill does. It produces a sequence of findings, each one defensible, each one referenced to the verbatim evidence in the intake."

---

### Shot 4 — DELIVERABLE WALKTHROUGH (60 seconds)

**Camera:** screen-focused. Right half shows `examples/investor-story-forensics/deliverable-2.md` (Claim-Evidence Matrix).
**Visual cues:** open the file. Scroll to the NRR row. Scroll to the +95% growth row. Hold the cursor on the 0/3 verdicts for two beats each. Let the audience sit with the discomfort.

**Narration (verbatim):**

"This is deliverable two. The Claim-Evidence Matrix. It is the artifact that scores every load-bearing claim in the deck against the auditable evidence in the data room. Look at the rows. NRR 130% claimed — evidence column is empty for trailing-four-quarter. Verdict — zero of three. Below it — the +95% growth row. Same shape. The trailing number is sixty-eight percent. The deck has been pitching a J-curve. The actual shape is linear. Verdict — zero of three. Now look at the 14/25 OEMs row. Trailing-active deployments — eleven of twenty-five. Three of the fourteen are paused pilots logged as active accounts. Verdict — one of three, anecdotal. This is what the matrix does. It does not argue. It scores. The score is what the founder hands the CFO and the head of sales on Wednesday morning and says — these are the three claims we cannot defend. Fix the underlying business or stop pitching the claim. The deliverable is uncomfortable on purpose. The partner reading the data room is going to be more uncomfortable. Better the discomfort lives here, in a room you control, than in a partner meeting you don't."

---

### Shot 5 — SCORECARD WALKTHROUGH (45 seconds)

**Camera:** screen-focused. Right half shows `examples/investor-story-forensics/deliverable-5-scorecard.md`.
**Visual cues:** open the scorecard. Show the composite Narrative Integrity lift — 14/30 Vulnerable to 21/30 Defensible post-rebuild. Scroll to the top 3 actions. Pause on the leading indicator.

**Narration (verbatim):**

"This is the scorecard. Pre-rebuild Narrative Integrity — fourteen of thirty. Vulnerable. Post-rebuild — twenty-one of thirty. Defensible. Seven-point lift, which exceeds the thirty-percent rebuild threshold the skill enforces. If the lift was under thirty percent, the skill rejects the rebuild and forces a redo. Three actions for the next thirty days. Publish the trailing-four-quarter NRR alongside the claimed NRR in the data room, every claim labeled by window — owner CFO, deadline fourteen days. Run the reference-customer stress audit against all five named references, replace the two with champion changes — owner CEO and head of customer success, deadline twenty-one days. Reframe the growth-rate slide from +95 percent to '+95 percent run-rate, +68 percent trailing, J-curve forward thesis with named pipeline anchors' — owner CEO, deadline thirty days. Leading indicator at the bottom — when the data room can be opened to a friendly partner on a one-hour QoE pre-mortem without the founder needing to translate the deck, the reconstruction is holding. Two and a half hours of forensic audit produced the matrix, the brief, and the scorecard. That is the entire point of the kit."

---

### Shot 6 — CTA (30 seconds)

**Camera:** webcam full-frame. Screen visible behind but not the focus.
**Visual cues:** founder talking head. End on a clean stop. No outro animation.

**Narration (verbatim):**

"Take the quiz. The link is in the description below this video. Five questions, two minutes, scored against the same five fault lines I just walked you through. The quiz tells you which integrity tier your investor narrative is in and what to do about it. Download the kit. Repo link is in the description and in the README. Free, CC BY 4.0, runs in any modern AI assistant. This is Kit 5 of the Resilience Stack v1.5 release. That is the full v1.5 release live on GitHub. Resilience Stack on GitHub. I am Phil at Petrichor."

---

## Total: ~5 min 0 sec

## Quality bar

- One-take. No post-editing.
- Founder-talking-head energy. No production polish.
- 6 minutes maximum. If a shot runs long, redo the affected shot only.
- No comment-bait. No fake urgency. No "smash that subscribe" — this is not YouTube.
- Voice: direct, diagnostic, blunt. If you catch yourself coaching, stop and re-record.

## Per-kit customisation notes

- Loom URL: {{loom-url-to-be-added-by-phil}}
- Loom caption/title: "Investor Story Forensics walkthrough — Resilience Stack v1.5 Kit 5 (Final)"
- Worked example input: `examples/investor-story-forensics/input.md` (Aperture, $42M ARR industrial QA SaaS, Series C prep, 130% NRR claimed / 117% trailing)
- Shot 4 deliverable to open: `examples/investor-story-forensics/deliverable-2.md` (Claim-Evidence Matrix)
- Shot 5 scorecard to open: `examples/investor-story-forensics/deliverable-5-scorecard.md`
- This is the final kit of v1.5. Shot 6 names "Resilience Stack v1.5 release live on GitHub" instead of a next-kit teaser.

## Distribution

- Upload to Loom. Set to public, no password.
- Paste the Loom URL into:
  - `skills/investor/investor-story-forensics/README.md`
  - `marketing/launch-templates/investor-story-forensics.md`
  - `marketing/essays/investor-story-forensics.md` (footer link)
  - The Tally quiz confirmation page and result-tier pages
  - The private Loom delivery for Tier 2 and Tier 3 result pages
- Do not embed on the blog post — link only.

---

*Resilience Stack video · CC BY 4.0 · Petrichor Projects*
