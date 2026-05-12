# Resilience Stack v1.5 — Design Spec

**Date**: 2026-05-12
**Owner**: Petrichor Projects
**Status**: Approved, ready for implementation planning

---

## 1. Context

Resilience Stack v1.2 shipped 2026-05-12. State:

- 18 strategy facilitator skills across 7 tracks
- Structured frontmatter (name, description, version, tier, track, duration_hours, prerequisites, composable_with, outputs, license, author)
- `## When NOT to use` block on every skill
- Meta-skill `skill-compass` for entry-point selection
- Scaffolded directories: `evals/`, `examples/`, `case-studies/`, `docs/glossary.md`, `CHANGELOG.md`, `ROADMAP.md`
- Coverage thin: 1/18 skills have evals, 1/18 have worked examples, 1/18 have case studies
- Public CC BY 4.0, open contributions, GitHub Action validator on PRs

This spec defines v1.5 — a 6-week vertical polish sprint on the top 5 skills, paired with the supporting brand assets that turn a curated list into a world-class library.

---

## 2. Goal

Ship a credible launch of Resilience Stack by week 5, with:

- 5 skill kits at full depth (each with eval cases, worked example, case study, scoring rubric, deliverable formatter, video walkthrough, quiz lead magnet, founder essay)
- A foundational manifesto that anchors the brand
- A skill-creator meta-skill that unlocks community contributions
- An opt-in trajectory logging spec that sets up v2 Curator data without committing to implementation

The remaining 13 skills stay at v1.2 (skill markdown only) until inbound demand or contributor PRs lift them.

---

## 3. Non-Goals

- Hosted runner / managed infrastructure (defer to v2)
- API endpoint per skill (defer)
- Slack or Discord community (defer to v1.6, after launch signal)
- Bounty / affiliate program (defer)
- Annual benchmark report (defer to v2)
- Resilience Summit / live event (defer to v2)
- Industry-specific skill variants (defer to v1.6)

---

## 4. Approach Selected

**Skill-by-skill vertical, top 5 first.** Each priority skill ships as a complete kit (10 artifact types) before the next is started. This produces 5 world-class kits at the cost of leaving 13 thin — preferred over 18 mediocre kits.

**Top 5 priority skills:**

1. `relevancy-audit` — entry skill, already partially polished
2. `revenue-story-audit` — fundraise trigger, VC-backed buyers
3. `competitive-narrative-stress-test` — sales pain, easy demo
4. `pricing-authority-diagnostic` — operator buyers, immediate ROI story
5. `investor-story-forensics` — high-ticket Tier-3, biggest signal

**Release cadence:**

| Week | Event | Public artifacts shipped |
|------|-------|--------------------------|
| 0 | Soft base release | v1.2 repo public on GitHub + npm. One low-key LinkedIn post. No HN. |
| 1 | Kit 1 launch | `relevancy-audit` full kit + video + quiz + essay + X/LinkedIn |
| 2 | Kit 2 launch | `revenue-story-audit` full kit |
| 3 | Kit 3 launch | `competitive-narrative-stress-test` full kit |
| 4 | Kit 4 launch | `pricing-authority-diagnostic` full kit |
| 5 | Kit 5 launch + HN | `investor-story-forensics` full kit + Show HN + Product Hunt + cumulative recap |

---

## 5. Kit Definition (10 Artifacts)

Each of the 5 priority skills ships with:

1. **Skill markdown** (already exists in v1.2)
2. **3 eval cases** (`evals/<skill>/case-01-baseline.yaml`, `case-02-when-not-to-use.yaml`, `case-03-adversarial.yaml`)
3. **Worked example** (`examples/<skill>/input.md` + 5 deliverable files + `trajectory.md` + `post-engagement-notes.md`)
4. **Anonymized case study** (`case-studies/<skill>/case-01-<slug>.md`)
5. **Scoring rubric** (`skills/<track>/<skill>/scoring/<skill>-rubric.md`)
6. **Deliverable formatter** (a sub-skill that converts skill output into board-deck-ready markdown — lives at `skills/<track>/<skill>/formatters/board-brief.md`)
7. **Video walkthrough** (5-min Loom showing the skill running on the worked example — link stored in skill README)
8. **Quiz lead magnet** (5-question Typeform/Tally diagnostic → email capture → routes user to the kit — link stored in kit README)
9. **Founder long-form essay** (1500-2500 words by Philipp, published to petrichorgrowth.com/blog and cross-posted)
10. **Launch copy templates** (X thread + LinkedIn carousel + Substack post — drafts stored at `marketing/launch-templates/<skill>.md`)

---

## 6. One-Time Foundational Artifacts (before Week 0)

1. **`docs/manifesto.md`** — single foundational essay titled "Why Frameworks Decay (And What To Do About It)" by Philipp. ~3000 words. Cited by every kit launch.
2. **`meta-skills/skill-creator/skill-creator.md`** — meta-skill that walks contributors through building a Resilience Stack skill end-to-end. Pre-built before HN launch so external PRs become viable.
3. **`docs/trajectory-logging-spec.md`** — opt-in telemetry specification (no implementation). Defines what gets logged, what doesn't, how users opt in, what the data is used for (training future Curator agent). Implementation deferred to v2.

---

## 7. Repo Structure (post-v1.5)

```
resilience-stack/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTORS.md
├── CHANGELOG.md
├── ROADMAP.md
├── package.json
├── install.sh
├── .github/
├── bin/
├── skills/
│   ├── positioning/
│   │   ├── relevancy-audit/
│   │   │   ├── relevancy-audit.md
│   │   │   ├── scoring/relevancy-rubric.md            # NEW v1.5
│   │   │   └── formatters/board-brief.md              # NEW v1.5
│   │   ├── positioning-under-pressure/
│   │   └── competitive-narrative-stress-test/
│   │       ├── competitive-narrative-stress-test.md
│   │       ├── scoring/narrative-rubric.md            # NEW v1.5
│   │       └── formatters/board-brief.md              # NEW v1.5
│   ├── growth/
│   │   ├── revenue-story-audit/
│   │   │   ├── revenue-story-audit.md
│   │   │   ├── scoring/revenue-rubric.md              # NEW v1.5
│   │   │   └── formatters/board-brief.md              # NEW v1.5
│   │   └── pricing-authority-diagnostic/
│   │       ├── pricing-authority-diagnostic.md
│   │       ├── scoring/pricing-rubric.md              # NEW v1.5
│   │       └── formatters/board-brief.md              # NEW v1.5
│   ├── investor/
│   │   └── investor-story-forensics/
│   │       ├── investor-story-forensics.md
│   │       ├── scoring/investor-rubric.md             # NEW v1.5
│   │       └── formatters/board-brief.md              # NEW v1.5
│   └── ... (other 13 skills unchanged from v1.2)
├── meta-skills/
│   ├── skill-compass/
│   └── skill-creator/                                  # NEW v1.5
├── evals/
│   ├── relevancy-audit/                                # 3 cases (1 exists, +2)
│   ├── revenue-story-audit/                            # NEW 3 cases
│   ├── competitive-narrative-stress-test/              # NEW 3 cases
│   ├── pricing-authority-diagnostic/                   # NEW 3 cases
│   └── investor-story-forensics/                       # NEW 3 cases
├── examples/
│   ├── relevancy-audit/                                # 1 doc exists, +rest
│   ├── revenue-story-audit/                            # NEW
│   ├── competitive-narrative-stress-test/              # NEW
│   ├── pricing-authority-diagnostic/                   # NEW
│   └── investor-story-forensics/                       # NEW
├── case-studies/
│   ├── relevancy-audit/                                # 1 exists
│   ├── revenue-story-audit/                            # NEW
│   ├── competitive-narrative-stress-test/              # NEW
│   ├── pricing-authority-diagnostic/                   # NEW
│   └── investor-story-forensics/                       # NEW
├── marketing/                                           # NEW v1.5
│   ├── launch-templates/
│   │   ├── relevancy-audit.md
│   │   ├── revenue-story-audit.md
│   │   ├── competitive-narrative-stress-test.md
│   │   ├── pricing-authority-diagnostic.md
│   │   └── investor-story-forensics.md
│   ├── quizzes/
│   │   └── <5 quiz specs + Typeform/Tally URLs>
│   └── videos/
│       └── <5 Loom URLs and shot lists>
├── docs/
│   ├── glossary.md
│   ├── manifesto.md                                    # NEW v1.5
│   ├── trajectory-logging-spec.md                      # NEW v1.5
│   └── superpowers/
│       └── specs/
│           └── 2026-05-12-resilience-stack-v1.5-design.md  # this file
```

---

## 8. Per-Kit Workstream (per priority skill)

Roughly 1 week of effort per kit, structured as:

| Day | Workstream |
|-----|------------|
| Mon | Eval cases authored (3 cases) |
| Tue | Worked example built (input + run trajectory + 5 deliverables) |
| Wed | Case study drafted from a real or representative engagement |
| Thu | Scoring rubric + board-brief formatter |
| Fri AM | Video walkthrough recorded (Loom) + quiz built (Tally) |
| Fri PM | Founder essay written + launch copy drafted |
| Mon (next) | Kit published, launch copy posted |

Reality: many slots will compress. Some artifacts (essay, video) may be parallelized with prior-week work.

---

## 9. Quality Gates Per Kit

Before a kit launches publicly:

- [ ] All 3 eval cases pass manual review against skill markdown
- [ ] Worked example produces all 5 deliverables in `examples/<skill>/`
- [ ] Case study anonymization rules applied (no real company names)
- [ ] Scoring rubric scores at least 1 historical engagement
- [ ] Video walkthrough under 6 minutes, no production polish required, but clear
- [ ] Quiz tested by 3 non-team reviewers
- [ ] Founder essay reviewed by 2 strategists outside Petrichor (informal)
- [ ] Launch copy reviewed against `boundaries.md` (no comment-bait, no auto-DM mechanics)

---

## 10. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Kit 1 lands soft, momentum dies | Medium | High | Pre-launch DM 10 friendlies for amplification. Reserve right to pause + diagnose before Kit 2. |
| Founder essay quality varies | Medium | Medium | Use a single voice template. Reviewer outside Petrichor before each post. |
| Quiz tools (Tally) require subscription | Low | Low | Tally free tier is generous. Worst case, build inline HTML quiz. |
| Loom videos look amateurish | Low | Medium | Define a 6-shot template that works for every skill. Accept "founder talking head" as the standard. |
| HN launch (Week 5) requires hosted demo | Low | Medium | Skip live demo. README + worked example + video = sufficient. |
| 13 unaddressed skills become a credibility liability | Low | Medium | README explicitly labels v1 vs polished kit. Polished kits get gold badges in repo index. |
| External contributor PR opens before skill-creator meta-skill ships | Medium | Low | Skill-creator is week-0 foundational work. Won't accept new-skill PRs until it exists. |

---

## 11. Success Metrics (90 days)

| Metric | Target | Stretch |
|--------|--------|---------|
| GitHub stars | 500 | 2000 |
| npm weekly downloads | 100 | 500 |
| Email captures via quizzes | 200 | 1000 |
| Inbound engagement leads | 5 | 15 |
| Closed engagements attributable to stack | 1 | 5 |
| External contributor PRs | 3 | 10 |
| Podcast bookings driven by launches | 2 | 8 |

---

## 12. Out of Scope for v1.5

- v2 Curator agent (logged in ROADMAP)
- Hosted runner / SaaS layer
- Industry variants (SaaS / DTC / B2B services)
- Annual benchmark report
- Certified Facilitator program
- Resilience Summit event
- Skill marketplace inside the stack

These are tracked in `ROADMAP.md`. Decisions on which to pursue in v1.6 happen post-launch based on signal.

---

## 13. Open Decisions

- Domain: `resilience-stack.com` standalone vs `petrichorgrowth.com/stack` subpath. **Default**: subpath unless launch traction justifies standalone.
- GitHub org: `petrichorprojects` vs Phil's personal. **Default**: `petrichorprojects` org for repo, single-owner for now.
- Trademark filing: defer until brand traction. ~$350 USPTO investment becomes worthwhile after Kit 3 lands.

---

## 14. Definition of Done (v1.5)

v1.5 is shipped when:

- 5 priority kits are publicly available in the repo, with all 10 artifacts per kit
- Manifesto, skill-creator meta-skill, and trajectory-logging spec are published
- `CHANGELOG.md` and `ROADMAP.md` are updated
- 5 weekly launch posts have shipped on X and LinkedIn
- HN Show HN post has been published (Week 5)
- At least 1 inbound conversation has been booked

---

## 15. Next Step

After this spec is approved, invoke the `superpowers:writing-plans` skill to create the implementation plan.

The implementation plan will sequence:

1. Week-0 foundational artifacts (manifesto, skill-creator, trajectory spec, base release)
2. Kits 1-5 in order, with the 10-artifact checklist applied to each
3. Launch sequence (LinkedIn → X → blog → HN at week 5)

---

*Spec v1.0 — 2026-05-12 — Petrichor Projects — CC BY 4.0*
