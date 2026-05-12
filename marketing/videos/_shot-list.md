<!--
LOOM SHOT LIST TEMPLATE — 5–6 minute kit walkthrough
Reusable across all 5 weekly kits. Copy this file per kit as marketing/videos/{{skill-name}}.md
Fill in each shot with skill-specific narration. Keep it one take, no editing.
Forbidden: long preambles, "hey everyone I'm Phil and today we're going to talk about...", fake urgency, comment-bait.
-->

# Video Shot List Template (6 shots, ~5–6 minutes)

## Setup

- **Tool:** Loom (free or paid tier — both work)
- **Layout:** screen + camera both on. Webcam small in bottom-right corner.
- **Screen split:**
  - **Left half:** the skill markdown open in the editor (raw, not rendered, so viewers see frontmatter and structure)
  - **Right half:** Claude Code OR a rendered example output (one of the 5 deliverables, pre-opened)
- **Audio:** wired mic preferred. AirPods acceptable. Built-in MacBook mic only as last resort.
- **Recording mode:** single take, no post-editing. Founder-talking-head energy is the point. If you flub badly, redo the affected shot only — never assemble a Frankenvideo.
- **Run-time target:** 5:00–6:00. Hard cap at 6:30.

## 6 Shots

### Shot 1 — HOOK (≈ 30 seconds)

Name the buyer problem this skill solves. Do not start with "Hi, I'm Phil." Start with the failure pattern.

> **Narration shape:** "Your {{thing}} has probably been broken for {{N}} months. Here is how you can tell: {{1–2 measurable signals}}. This kit is the diagnostic that catches it."

### Shot 2 — SKILL STRUCTURE (≈ 45 seconds)

Show the skill markdown on the left side. Scroll through:
- Frontmatter (name, version, when-to-use, when-NOT-to-use)
- The "When NOT to use" block specifically — read it aloud. This is the section that earns trust.
- The 9 facilitation segments. Quick scroll, naming each one.

### Shot 3 — DEMO (≈ 90 seconds)

Switch focus to the right side. Run the skill against the worked example.
- Paste the example input into Claude Code.
- Let Claude respond live. Do not cut.
- Narrate what Claude is doing as the response streams. Point to specific segments as they are produced.
- If Claude takes too long, narrate why the structure forces deeper thinking — do not apologize for the delay.

### Shot 4 — DELIVERABLE WALKTHROUGH (≈ 60 seconds)

Open one of the 5 sample deliverables (the one most representative of the kit's output).
- Point to specific lines that prove the diagnostic produced real value.
- Highlight one number, one phrase, one recommendation.
- Call out anonymization where it shows up. ("This is a real engagement — masked per our rules.")

### Shot 5 — SCORECARD WALKTHROUGH (≈ 45 seconds)

Open the scorecard from `scoring-rubrics/{{skill-name}}/`.
- Show the score on the worked example.
- Read the top 3 actions out loud.
- Explain in one sentence why the scorecard is the artifact that survives the meeting — the kit's job is to produce a thing the operator can hand to someone else on Tuesday.

### Shot 6 — DOWNLOAD + NEXT KIT TEASER (≈ 30 seconds)

- "The kit is at {{repo path}}. Loom URL is in the README. Quiz URL is in the description below this video."
- Tease the next week's kit in one sentence. Name the framework, not the marketing title.
- Sign off: "I'm Phil at Petrichor. New kit every Monday for the next {{N}} weeks."

## Total: ~5 min 0 sec

## Quality bar

- One-take. No post-editing.
- Accept founder-talking-head energy. Polish is for the essay, not the video.
- If you flub a shot, redo the affected shot only, then reassemble in Loom's trim view if absolutely necessary. Default is just re-record the whole thing.
- Voice: direct, no preamble, no platitudes. If you catch yourself saying "in today's fast-paced world," stop and re-record.
- No comment-bait. No fake urgency. No "smash that subscribe button" — this is not YouTube.

## Per-kit customization

- Per-kit shot list filename: `marketing/videos/{{skill-name}}.md`
- Each kit copies this template and fills the 6 shots with skill-specific narration.
- The per-kit file should include: the worked example input pasted in full, the specific deliverable to open in Shot 4, and the exact next-kit name for Shot 6.

## Distribution

- Upload to Loom. Set to public, no password.
- Paste the Loom URL into:
  - The kit's README (`skills/{{track}}/{{skill-name}}/README.md`)
  - The launch copy file (`marketing/launch-templates/{{skill-name}}.md`)
  - The essay (as a footer link)
  - The Tally form's confirmation page
- Do not embed on the blog post — link only. Loom embeds slow page load.
