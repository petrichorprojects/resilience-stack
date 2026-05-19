# Changelog — Resilience Stack

All notable changes documented per [Keep a Changelog](https://keepachangelog.com) and [Semantic Versioning](https://semver.org).

---

## Unreleased

### Added
- `meta-skills/interface-hardening/interface-hardening.md` — targeted resilience hardening for UI surfaces, forms, workflows, dashboards, and API-bound interfaces.
- `evals/interface-hardening/` — baseline form hardening, when-not-to-use redirect, and adversarial dashboard rubber-stamp cases.

---

## [1.5.0] — 2026-06-16 (Week 5 — HN Launch Week)

### Added — Kit 5: investor-story-forensics (full depth) + HN launch
- `evals/investor-story-forensics/`: 3 cases (Aperture baseline, refuse <14d to term sheet, adversarial sanitized)
- `examples/investor-story-forensics/`: input + trajectory + 5 deliverables + post-engagement + board-brief sample
- `case-studies/investor-story-forensics/case-01-industrial-qa-saas.md` (998w)
- `skills/investor/investor-story-forensics/scoring/investor-rubric.md` — Aperture 14/30 Vulnerable
- `skills/investor/investor-story-forensics/formatters/board-brief.md`
- `marketing/essays/investor-story-forensics.md` (2319w)
- `marketing/quizzes/investor-story-forensics.md` — 5-Q, 4 tiers
- `marketing/videos/investor-story-forensics.md`
- `marketing/launch-templates/investor-story-forensics.md`
- `marketing/launch-templates/_v1.5-launch-week-5-hn.md` — Show HN post + cumulative recap thread + babysit plan

### v1.5 Final Cumulative
- 5 priority kits shipped (relevancy-audit, revenue-story-audit, competitive-narrative-stress-test, pricing-authority-diagnostic, investor-story-forensics)
- 50+ artifacts: 15 eval cases + 35 worked example files + 5 case studies + 5 scoring rubrics + 5 board-brief formatters + 5 board-brief samples + 5 essays + 5 quiz specs + 5 video shot lists + 5 launch templates
- 1 manifesto, 1 trajectory-logging spec, 1 skill-creator meta-skill, 1 marketing scaffold, 1 glossary
- Schedule: Soft release Week 0 → 5 weekly kit drops → HN Show HN Week 5 Tuesday 9am ET

### Pending Phil for full launch
- 5 Tally quiz URLs + Beehiiv list config
- 5 Loom video recordings
- Outside-Petrichor review (2 strategists per essay)
- GitHub org `petrichorprojects` setup + npm `resilience-stack` publish
- Weekly Monday posts (LinkedIn, X, Substack) Weeks 1-5
- HN submission Tuesday 9am ET Week 5

---

## [1.5.0-kit-4] — 2026-06-09 (Week 4)

### Added — Kit 4: pricing-authority-diagnostic (full depth)
- `evals/pricing-authority-diagnostic/`: 3 cases (Helix baseline, refuse pre-PMF, adversarial sales sanitization)
- `examples/pricing-authority-diagnostic/`: input + trajectory + 5 deliverables + post-engagement + board-brief sample
- `case-studies/pricing-authority-diagnostic/case-01-healthcare-scheduling-saas.md` (999w)
- `skills/growth/pricing-authority-diagnostic/scoring/pricing-rubric.md` — Helix 18/30 Eroding
- `skills/growth/pricing-authority-diagnostic/formatters/board-brief.md`
- `marketing/essays/pricing-authority-diagnostic.md` (2486w)
- `marketing/quizzes/pricing-authority-diagnostic.md` — 5-Q, 4 tiers
- `marketing/videos/pricing-authority-diagnostic.md`
- `marketing/launch-templates/pricing-authority-diagnostic.md`

Synthetic: Helix (healthcare scheduling SaaS, $28M ARR). Discount climb 8→21%, NRR 108→96%, 30mo no price change. Root cause 38/31/19/12.

### Pending Phil
- Tally + Loom URLs
- Outside review
- Monday 2026-06-09 launch

---

## [1.5.0-kit-3] — 2026-06-02 (Week 3)

### Added — Kit 3: competitive-narrative-stress-test (full depth)
- `evals/competitive-narrative-stress-test/`: 3 cases (Tessera baseline, blue-ocean refuse, sanitized adversarial)
- `examples/competitive-narrative-stress-test/`: input + trajectory + 5 deliverables + post-engagement + board-brief sample
- `case-studies/competitive-narrative-stress-test/case-01-retail-analytics-decay.md` (991w)
- `skills/positioning/competitive-narrative-stress-test/scoring/narrative-rubric.md` — 10-dim rubric, Tessera 17/30 Fragile
- `skills/positioning/competitive-narrative-stress-test/formatters/board-brief.md`
- `marketing/essays/competitive-narrative-stress-test.md` (2205w)
- `marketing/quizzes/competitive-narrative-stress-test.md` — 5-Q diagnostic, 4 tiers
- `marketing/videos/competitive-narrative-stress-test.md` — 6-shot Loom shot list
- `marketing/launch-templates/competitive-narrative-stress-test.md`

Synthetic: Tessera (retail analytics SaaS, $14M ARR, 6-8mo from Series B). Attack Surface Durability 13/25 → 19/25 post-rebuild.

### Pending Phil
- Tally URL + Loom URL
- Outside review (2 strategists)
- Monday 2026-06-02 launch posts

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
