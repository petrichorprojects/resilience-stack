<!--
QUIZ SPEC TEMPLATE — Resilience Stack kit diagnostic
Copy this file once per kit. Filename: marketing/quizzes/{{skill-name}}.md
Build the corresponding Tally form, paste the URL back into this file and into the launch copy.
Tone: clinical, not playful. The buyer is a strategy operator. No emoji. No "What kind of pizza are you?"
Forbidden: comment-bait, fake urgency, PII beyond email + first name.
-->

# Quiz Spec — {{skill-name}}

## Tool: Tally.so (free tier)
## URL: {{tally-url-after-build}}
## Title: "{{question-headline}}"

<!-- The title is a diagnostic question, not a marketing line.
Example shapes:
- "How decayed is your positioning?"
- "Where is your pricing actually leaking?"
- "Is your ICP definition still describing the market you sell into?"
Avoid: "Discover your X type!" / "Find out your Y score!" -->

## Why this quiz exists

[1–2 sentences. Operational, not promotional. Example: "This quiz routes strategy operators into one of three tiers based on how far their {{framework}} has decayed. Tier output determines the follow-up sequence: kit, kit + Loom invite, or direct outreach."]

## 5 Diagnostic Questions

<!-- Each question must:
- Test a single observable signal of the framework's health
- Offer 3–4 mutually exclusive multiple-choice options
- Have a clear point weighting (0/1/2/3) — higher = more decay
- Avoid leading language. The respondent should not be able to guess the "good" answer. -->

1. **[Q1 — measures signal #1, e.g. "When did your team last revisit the assumptions behind this framework?"]**
   - [Option A — 0 pts — healthy baseline]
   - [Option B — 1 pt — mild drift]
   - [Option C — 2 pts — clear disconnect]
   - [Option D — 3 pts — full displacement]

2. **[Q2 — measures signal #2]**
   - [Option A — 0 pts]
   - [Option B — 1 pt]
   - [Option C — 2 pts]
   - [Option D — 3 pts]

3. **[Q3 — measures signal #3]**
   - [Option A — 0 pts]
   - [Option B — 1 pt]
   - [Option C — 2 pts]
   - [Option D — 3 pts]

4. **[Q4 — measures signal #4]**
   - [Option A — 0 pts]
   - [Option B — 1 pt]
   - [Option C — 2 pts]
   - [Option D — 3 pts]

5. **[Q5 — measures signal #5]**
   - [Option A — 0 pts]
   - [Option B — 1 pt]
   - [Option C — 2 pts]
   - [Option D — 3 pts]

## Scoring Rubric

- **0–5 points: Stage 1 — Drift.** Action: read the manifesto + bookmark the repo. The framework is still working. Maintenance, not replacement.
- **6–10 points: Stage 2 — Disconnect.** Action: download the kit and run the diagnostic on your own business. Likely 2–4 hour exercise.
- **11–15 points: Stage 3 — Displacement.** Action: book a Petrichor call. The framework has stopped describing your market. A self-serve kit is unlikely to be enough.

## Email capture

- **Beehiiv list:** {{list-id}}
- **Fields:** first name, email. Nothing else.
- **Welcome email:** triggers a personalized summary of the tier result + direct kit link. Sent within 60 seconds of submission.

## Lead routing

- **Tier 1 (Drift, 0–5):** Add to Beehiiv list. 5-day educational email sequence. No human follow-up.
- **Tier 2 (Disconnect, 6–10):** Add to Beehiiv list. Send kit link + Phil Loom invite. Tag in CRM for week-3 check-in.
- **Tier 3 (Displacement, 11–15):** Add to Beehiiv list. Phil personal outreach within 48 hours. Calendar link in the welcome email.

## QA checklist (before going live)

- [ ] Tested end-to-end by 3 non-team reviewers
- [ ] Score thresholds verified — no respondent path lands on the wrong tier
- [ ] Beehiiv integration confirmed (test submission appears in the list)
- [ ] Welcome email triggers and renders correctly on iOS Mail + Gmail web
- [ ] 5-day email sequence is loaded and scheduled
- [ ] No PII collected beyond email + first name
- [ ] Privacy line at the bottom of the form: "We use your email to send you the kit and follow-up resources. You can unsubscribe at any time. We never share your email."
- [ ] Tally URL is the production URL, not a draft preview
- [ ] No comment-bait or fake urgency anywhere in the form copy or the welcome email
- [ ] Loads in < 2 seconds on mobile
