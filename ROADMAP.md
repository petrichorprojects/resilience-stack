# Roadmap — Resilience Stack

## Shipped — v1.5 (May-June 2026)

✅ **18 skills** at v1.2 structured-frontmatter baseline + "When NOT to use" blocks
✅ **5 priority kits at full depth** (10 artifacts each):
  - relevancy-audit (Week 1)
  - revenue-story-audit (Week 2)
  - competitive-narrative-stress-test (Week 3)
  - pricing-authority-diagnostic (Week 4)
  - investor-story-forensics (Week 5)
✅ **Foundational artifacts**: manifesto, glossary, trajectory-logging spec, skill-creator meta-skill, skill-compass meta-skill
✅ **Marketing scaffold**: 5 weekly launch templates + 5 quiz specs + 5 Loom shot lists + 5 founder essays + 5 cross-platform copy bundles
✅ **HN Show HN launch** Week 5 Tuesday 9am ET
✅ **CC BY 4.0** license, open contributions w/ tight `CONTRIBUTING.md`

## Now (v1.6 — post-launch signal-dependent)

### Quality fill (high-leverage)
- Long-tail 13 skills: scoring rubric + worked example + case study per skill
- 3 eval cases per long-tail skill (target: 18/18 with 3 cases each)
- Per-skill industry variants (SaaS / DTC / B2B services) for top 3 inbound-driving skills

### Tooling (Phil's choice based on launch signal)
- Python eval runner: `python evals/run.py <skill> <case>` (Claude API, golden-output comparison)
- CLI: `resilience-stack run <skill> --context "..."` (local-only, user's own API key)
- VS Code extension for skill authoring (frontmatter validator + section linter)

### Distribution expansions
- MyClaude marketplace mirror (Petrichor authority signal)
- LangChain tool wrapper (skills as LangChain tools)
- MCP server wrapping the stack

## Next (v2.0 — 120 days post-launch)

## Later (v2.0 — 120 days POST-LAUNCH-SIGNAL)

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
