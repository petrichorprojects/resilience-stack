# Roadmap — Resilience Stack

## Now (v1.2 — May 2026)

- 18 skills, structured frontmatter, evals + examples + case-studies
- Meta-skill `skill-compass` for selection
- CC BY 4.0 license
- Open contributions w/ tight `CONTRIBUTING.md`

## Next (v1.5 — 60 days)

### Skill expansions (target: 18 → 46 skills)
- 18 scoring rubric skills (one per workshop)
- 5 deliverable-formatter skills (board-deck-ready outputs)
- 5 meta-skills: prep-pack, debrief, retro, follow-up planner, integration map

### Tooling
- Python eval runner: `python evals/run.py <skill> <case>` (calls Claude API, scores against golden)
- CLI: `resilience-stack run <skill> --context "..."` (local-only, user's own API key)
- VS Code extension for skill authoring (frontmatter validator + section linter)

### Quality
- 3 eval cases per skill (currently 1 has 3, 17 have 0)
- Worked example per skill (currently 1 of 18 complete)
- 1 case study per skill per quarter (currently 1 of 18 complete)

## Later (v2.0 — 120 days)

### SkillOS-style Curator (the thesis upgrade)
- `curator` agent that reads skill-run trajectories from `<skill>-output/` dirs
- LLM-as-judge scores each run on outcome quality
- Curator proposes Insert / Update / Delete on SkillRepo
- Composite reward: task outcome + format integrity + compression + redundancy
- This makes Resilience Stack **self-evolving** — the first strategy library with built-in learning

### Industry variants
- SaaS / DTC / B2B services / fintech / healthtech variants per top skill
- Triggered by `skill-compass` based on user industry

### Distribution
- MyClaude marketplace mirror
- VS Code extension publish
- Cursor extension publish
- LangChain integration (skills as LangChain tools)
- MCP server wrapping the stack

## Far (v3.0 — 12 months)

### Public Resilience Stack OS
- Hosted facilitator (Petrichor-branded webapp)
- Org-level skill repo (private skills per company w/ shared core)
- Skill marketplace inside the stack (community-contributed, curator-validated)
- Telemetry dashboard (opt-in) showing skill effectiveness across the community
- Quarterly Resilience Stack report on which frameworks moved which outcomes

---

## How To Influence This Roadmap

- Open a GitHub Discussion for feature requests
- Submit eval cases / examples / case studies to validate skills are working
- Contribute new skills via PR (see `CONTRIBUTING.md`)
- Sponsor a track (Petrichor partners may sponsor a track for branded co-development)
