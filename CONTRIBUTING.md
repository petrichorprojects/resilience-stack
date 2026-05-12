# Contributing to Resilience Stack

PRs welcome. Bar is high. Read this fully before opening one.

---

## What We Accept

A strategy skill that meets all of:

1. **Proprietary framework** — named, opinionated, distinct. Not a rebrand of Porter's Five Forces or a generic SWOT.
2. **Adversarial facilitation** — the skill must apply pressure, demand evidence, push back on platitudes.
3. **Evidence-required pre-work** — must specify the data the participant gathers before running.
4. **5 named deliverables** — concrete artifacts written to disk.
5. **Segmented session flow** — 8-10 numbered segments with time boxes.
6. **Facilitation rules** — at least 3 adversarial rules at the end.

If your skill is "a Claude prompt that gives advice on X," it will be rejected.

---

## What We Reject

- Generic frameworks rebadged with new names
- Skills that produce only "insights" with no written deliverable
- Skills with no pre-work / data requirements
- Skills that flatter the participant
- Skills under 1,000 words (no depth)
- Skills over 5,000 words (no discipline)
- Marketing-copy skills (LinkedIn post generators, etc.)
- Skills that depend on external API keys (the user's Claude key is the only allowed credential)

---

## Skill Spec Template

Copy this into `skills/<track>/<skill-name>/<skill-name>.md`:

```markdown
---
name: skill-name-kebab-case
description: One-line description starting with "Run a [Workshop Name] —" and ending with "Based on [Framework Name]."
framework: The Named Framework
tier: 1 | 2 | 3
track: Positioning | Diagnostic | Brand Infrastructure | Growth Architecture | Market Definition | Market Intelligence | Investor & Stakeholder
author: Your Name (https://your-link.com)
---

# Skill Name — Interactive Strategy Diagnostic

You are a senior strategy facilitator running [Workshop Name] using [Framework Name].

**Persona**: [2-3 sentences — adversarial stance]

**Core question**: "[The question this skill answers]"

**Framework — [Framework Name]**: [3-5 sentences describing the framework and its components]

---

## FACILITATION PROTOCOL

Run sequentially. Write outputs to `./<skill-name>-output/`.

### PHASE 1 — Pre-Work
[Required data, surveys, transcripts, decks]

### PHASE 2 — [Workshop Name] (8-10 Segments)

1. **Opening & Framing** — [purpose]
2. **[Segment Name]** — [purpose]
... (8-10 total)
N. **Commitments & Close** — [owner per output, deadlines]

### PHASE 3 — Deliverables

1. **[Deliverable 1 Name]** — [one-line description]
2. **[Deliverable 2 Name]** — [one-line description]
3. **[Deliverable 3 Name]** — [one-line description]
4. **[Deliverable 4 Name]** — [one-line description]
5. **[Deliverable 5 Name]** — [one-line description]

---

## Facilitation Rules

- [Rule 1 — adversarial, evidence-demanding]
- [Rule 2]
- [Rule 3]
- [Rule 4+ as needed]
```

---

## PR Process

1. **Fork → branch → PR.** Branch name: `skill/<skill-name>`.
2. **One skill per PR.** Bundled PRs auto-close.
3. **Self-review the template** — every field present, every section non-empty.
4. **GitHub Action runs** — checks frontmatter fields, word count, required sections. Failures auto-comment.
5. **Petrichor reviews within 14 days.** Verdict: merge / request changes / reject with reason.
6. **Merged PRs**: contributor credited in `author` frontmatter, listed in `CONTRIBUTORS.md`.

---

## License Agreement

By opening a PR you agree:

- Your contribution is licensed under CC BY 4.0
- You authored the content or have the right to contribute it
- Petrichor Projects may use it, modify it, sublicense it under the same terms
- You retain authorship credit via the `author` field

No CLA signing required — your PR commit is your sign-off.

---

## Code of Conduct

Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Adversarial in frameworks, professional with humans. Harassment, ad hominem, or bad-faith reviews close issues immediately.

---

## Out-of-Scope Contributions

Things we do not accept as skills, even if well-built:

- LinkedIn post / tweet / blog content generators
- Email writers
- SDR / outbound tools
- SEO content tools
- Generic "consultant chatbot" personas

These belong in other repos. This stack is **strategy diagnostic frameworks** only.

---

## Questions

Open a GitHub Discussion. Do not DM the maintainers.
