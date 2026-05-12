# Changelog — Resilience Stack

All notable changes documented per [Keep a Changelog](https://keepachangelog.com) and [Semantic Versioning](https://semver.org).

---

## [1.5.0-kit-2] — 2026-05-26 (Week 2)

### Added — Kit 2: revenue-story-audit (full depth)
- `evals/revenue-story-audit/`: 3 cases (NorthStack baseline, refuse pre-revenue, adversarial vague-claims)
- `examples/revenue-story-audit/`: input + trajectory + 5 deliverables + post-engagement-notes + board-brief sample
- `case-studies/revenue-story-audit/case-01-fintech-ops-layer.md` (833w)
- `skills/growth/revenue-story-audit/scoring/revenue-rubric.md` — 10-dim rubric (0-30 → Reconciled/Drifting/Inflated)
- `skills/growth/revenue-story-audit/formatters/board-brief.md` — sub-skill compressing 5 deliverables → 1-page brief
- `marketing/essays/revenue-story-audit.md` (1962w)
- `marketing/quizzes/revenue-story-audit.md` — 5-question Tally diagnostic
- `marketing/videos/revenue-story-audit.md` — 6-shot Loom shot list
- `marketing/launch-templates/revenue-story-audit.md` — X + LinkedIn + Substack + email bundle

Synthetic company: NorthStack (fintech ops layer, Series B, $20M ARR). Composite Inflated 22/30.

### Pending Phil
- Tally URL + Loom URL
- Outside-Petrichor essay review (2 reviewers)
- Monday 2026-05-26 launch posts

---

## [1.5.0-kit-1] — 2026-05-19 (Week 1)

### Added — Kit 1: relevancy-audit (full depth)
- `docs/manifesto.md` (2657w) — foundational "Why Frameworks Decay" essay (Petrichor brand anchor)
- `docs/trajectory-logging-spec.md` — opt-in telemetry spec (no impl; v2 Curator prep)
- `meta-skills/skill-creator/` — meta-skill for contributors to author new skills
- `marketing/` scaffold — launch-templates, quizzes, videos, essays templates
- `examples/relevancy-audit/`: trajectory, deliverables 1-4, post-engagement-notes, board-brief sample
- `skills/positioning/relevancy-audit/scoring/relevancy-rubric.md` — 10-dimension rubric (0-30 → Decay Stage)
- `skills/positioning/relevancy-audit/formatters/board-brief.md` — sub-skill compressing 5 deliverables → 1-page board brief
- `marketing/essays/relevancy-audit.md` (1800w) — founder essay
- `marketing/quizzes/relevancy-audit.md` — 5-question Tally diagnostic spec
- `marketing/videos/relevancy-audit.md` — 6-shot Loom shot list w/ verbatim narration
- `marketing/launch-templates/relevancy-audit.md` — X thread + LinkedIn + Substack + email bundle

### Pending Phil
- Tally URL (build quiz, paste into spec)
- Loom URL (record video, paste into spec)
- Outside-Petrichor essay review (2 reviewers)
- GitHub org + npm publish + soft-release LinkedIn post

---

## [1.2.0] — 2026-05-12

### Added
- Structured frontmatter across all 18 skills: `version`, `tier`, `track`, `duration_hours`, `prerequisites`, `composable_with`, `outputs`, `license`, `author`, `source_url`
- `meta-skills/skill-compass/` — Tier-0 selector that routes the user to the right skill
- `evals/` — test cases per skill (baseline / when-not-to-use / adversarial)
- `examples/` — worked examples (anonymized input, trajectory, deliverables)
- `case-studies/` — anonymized real engagements per skill
- `docs/glossary.md` — shared vocabulary across the stack
- `CHANGELOG.md` (this file)

### Changed
- All 18 skill descriptions tightened to one-sentence what+when format (BM25 retrieval optimized)
- All 18 skills now include `## When NOT to use` block (Anthropic + SkillOS schema compliance)

### Rationale
- Aligns to Google SkillOS paper (composite reward, atomic skills, retrieval-optimized)
- Aligns to Anthropic Skills schema (frontmatter spec)
- Adds the world-class layer missing in v1.1: evals + examples + case studies + glossary + meta-selector

---

## [1.1.0] — 2026-05-12

### Added
- `## When NOT to use` section to each of the 18 skills
- Tightened skill descriptions for BM25 retrieval

---

## [1.0.0] — 2026-05-11

### Added
- 18 strategy facilitator skills across 7 tracks
- `README.md`, `LICENSE` (CC BY 4.0), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`
- `.github/workflows/validate-skill.yml` — auto-validate PRs
- `bin/resilience-stack.js` — npx installer
- `install.sh` — curl bash one-liner installer

### Notes
- Initial public release derived from Petrichor's $45k workshop catalog
- Branded as Petrichor-forward, subtle (logo + footer + author credit)
- Open contributions w/ tight `CONTRIBUTING.md` + auto-validator
