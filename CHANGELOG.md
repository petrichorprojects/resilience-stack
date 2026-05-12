# Changelog — Resilience Stack

All notable changes documented per [Keep a Changelog](https://keepachangelog.com) and [Semantic Versioning](https://semver.org).

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
