# Marketing — Resilience Stack Launch Operations

This directory holds the reusable templates that power the 5-week kit launch cadence (v1.5) and any subsequent launches. It is operational, not promotional: every file here is a tool that gets filled, executed, and archived. No marketing copy lives here directly — only the templates that generate it.

## Why this exists

Resilience Stack ships in weekly "kits." Each kit is one polished skill plus its full audience-facing payload: launch copy across four channels, a diagnostic quiz, a Loom walkthrough, and a founder essay. Without templates, every Monday becomes a blank-page exercise and quality drifts. The templates below force consistency on structure while leaving voice and substance to the author.

The launch rhythm is fixed: **Week 0 soft release on LinkedIn → Weeks 1–5 one kit per Monday → Week 5 ends with the Show HN post.**

## Structure

```
marketing/
├── README.md                       ← you are here
├── launch-templates/
│   ├── _template.md                ← per-kit launch copy (X, LinkedIn, Substack, email)
│   └── _base-soft-release.md       ← Week 0 LinkedIn announcement
├── quizzes/
│   └── _template.md                ← per-kit Tally quiz spec
├── videos/
│   └── _shot-list.md               ← 6-shot Loom walkthrough template
└── essays/
    └── _template.md                ← founder long-form essay (1500–2500 words)
```

Files prefixed with `_` are templates. Per-kit instances drop the underscore and use the skill slug, e.g. `marketing/essays/relevancy-audit.md`.

## Brand voice — non-negotiable constraints

Resilience Stack content is published under Petrichor Projects' voice. Contributors who have not written for Petrichor before must read `docs/manifesto.md` (specifically "Why Frameworks Decay") before drafting anything. The voice rules below are extracted from internal boundaries documentation and apply to every file produced from these templates.

**Do:**
- Be direct, evidence-driven, specific. Name failure modes by their measurable signal.
- Cite real (anonymized) cases. Specificity beats abstraction.
- Take a position. Petrichor publishes claims, not "thought leadership."
- Use em-dashes in essays and long-form posts. They are part of the voice.

**Do not:**
- Use comment-bait CTAs on LinkedIn. "Comment X and I'll DM you" is a forbidden mechanic regardless of how well it converts. Use a newsletter subscribe or a direct quiz/kit link instead.
- Use fake urgency. No "only 24 hours," "last chance," "closing tonight" unless it is verifiably true.
- Hedge with platitudes ("In today's fast-paced world…"). Cut them at the editing pass.
- Write the words "leverage," "unlock," "synergy," or "game-changer" except as quoted critique.
- Use em-dashes in any document that may be re-used as legal copy (contracts, terms, audit reports). Hyphens only.

**Author attribution:** All long-form pieces are bylined Philipp Rimmler, Petrichor Projects. Sign-off is `*— Phil, Petrichor Projects*`.

## Anonymization rules for case study references

Every case study referenced in launch copy, essays, or quizzes must follow these rules:

1. **No real client names.** Refer to companies by stage and category: "a Series B B2B SaaS company in vertical workflow software," not "Acme Corp."
2. **No identifying revenue figures.** Use bands: "$10–25M ARR," not "$18.7M."
3. **Mask geography to region.** "A West Coast fintech," not "San Francisco fintech."
4. **Time-shift events by ≥ 3 months.** If a case happened in March, write it as "earlier this year" or "Q1 of last year."
5. **Composite when needed.** If a single case is too identifying, build a composite from 2–3 similar engagements and note `(composite, not a single client)` once in the piece.
6. **Internal review before publish.** Any case study reference is QA-checked against the engagement file. If you cannot verify anonymization, pull the example.

## How to use these templates

The standard weekly workflow:

1. **Monday week N-1, end of day.** Copy each `_template.md` to a per-kit instance: `marketing/launch-templates/{{skill}}.md`, `marketing/quizzes/{{skill}}.md`, `marketing/essays/{{skill}}.md`, `marketing/videos/{{skill}}.md`.
2. **Tuesday–Thursday.** Draft the essay first. The essay forces the thinking. The launch copy is derived from it.
3. **Thursday.** Record the Loom against the per-kit shot list. One take. Upload. Add the URL to every other file.
4. **Friday.** Build the Tally quiz from the per-kit quiz spec. Test it on three reviewers. Wire it to Beehiiv.
5. **Friday end of day.** QA pass: anonymization check, link check, voice check against `docs/manifesto.md`, comment-bait check, urgency check.
6. **Monday week N, 11:00 AM ET.** Publish in order: blog post (canonical) → LinkedIn → Substack → X thread → email blast. All cross-link to the kit in the repo and the quiz.
7. **Monday end of day.** Archive the filled templates in `marketing/_archive/{{week-number}}/` (create on first use). Capture metrics in the kit's `case-studies/` entry.

Templates evolve. If a Monday launch teaches you something — a section that always gets cut, a CTA that always converts — open a PR against the template, not just the per-kit file. The whole point is to compound.
