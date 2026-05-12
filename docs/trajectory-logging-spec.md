# Trajectory Logging — Specification v1.0

A privacy-first contract for what gets recorded when a Resilience Stack skill runs, so a future curator agent can learn from runs without ever turning the library into a surveillance system.

## Status

**Specification only — no implementation in v1.5. Implementation is deferred to v2 Curator.**

This document exists so contributors, users, and security reviewers can audit the data model *before* a single byte of trajectory data is ever collected. Nothing in v1.5 reads, writes, or transmits trajectory data. The skills in `skills/` do not currently emit any of the fields described below. When v2 ships the Curator agent, this file is the contract it must obey.

> A library that watches its users without telling them what it is watching for has already failed the only test that matters.

## Default Behavior — The Privacy Floor

Five rules govern this spec. They are not negotiable in v2 implementation:

1. **Logging is OFF by default.** A user who installs Resilience Stack and runs any skill without doing anything special leaves no trace. No file is created. No telemetry is sent. The skill produces deliverables and exits.
2. **Opt-in is per-run and explicit.** A user who wants to log a trajectory must pass `--log-trajectory` (CLI), set `RESILIENCE_LOG_TRAJECTORY=1` (env), or answer "yes" to the in-run prompt defined in section 7. There is no global "always log" toggle. Every run is a fresh consent decision.
3. **Logs are stored locally.** The default path lives inside the skill's working directory. Nothing is auto-uploaded. No background process exfiltrates anything.
4. **Petrichor receives nothing unless the user explicitly shares.** The Curator agent in v2 will train on aggregated, anonymized, user-submitted trajectories — and only those. There is no "phone home" channel and there will not be one.
5. **The user owns the file.** A trajectory log is a regular file on the user's machine. They can read it, edit it, delete it, share it, or never look at it again. Resilience Stack treats it as user-owned data, not as library telemetry.

This is the privacy floor. v2 may add capabilities above it. v2 may not lower it.

## Trajectory Schema (v1)

A single skill-run trajectory is a YAML document with the following shape:

```yaml
trajectory_id: 7c2e1f3a-9b4d-4c1e-8a2f-1d3e5b7c9a01
skill: relevancy-audit
skill_version: 1.5.0
run_start: 2026-05-12T14:03:11Z
run_end: 2026-05-12T15:47:42Z
phases_completed:
  - intake
  - dimension-scoring
  - prescription-generation
  - deliverable-assembly
deliverables_produced:
  - scorecard.md
  - prescription-set.md
  - executive-summary.md
outcome_score: 8
outcome_score_reason: >
  Five dimensions scored cleanly. Dimension 3 required two clarification
  rounds because the user's category framing was ambiguous. Final
  deliverable was approved without revision.
agent_observations:
  - phase: dimension-scoring
    note: >
      Facilitator paused twice on dimension 3 because the input contained
      a vocabulary mismatch between buyer language and internal language.
      Prescription engine handled this correctly.
  - phase: prescription-generation
    note: >
      Top-3 prescription ordering matched user's stated priorities without
      re-prompting.
facilitation_rules_triggered:
  - clarify-on-ambiguity
  - no-self-approval
  - evidence-before-recommendation
user_consent_share: false
```

Field semantics:

- **`trajectory_id`** — UUID v4. Generated locally. Not a user identifier.
- **`skill`** — Skill name as it appears in `skills/<name>/`.
- **`skill_version`** — Semver of the installed skill at run time. Required so v2 can correlate trajectories with skill diffs.
- **`run_start` / `run_end`** — ISO 8601 UTC timestamps.
- **`phases_completed`** — Ordered list of phase names actually completed. Aborted runs log whatever was reached.
- **`deliverables_produced`** — Filenames only. Not contents.
- **`outcome_score`** — Integer 1–10. Self-reported by the user at run end. Required.
- **`outcome_score_reason`** — Short free-text rationale. Subject to the never-logged rules in section 5.
- **`agent_observations`** — Structured notes the facilitator wrote during the run. One entry per observation. Phase-tagged.
- **`facilitation_rules_triggered`** — Which rules in the skill's `SKILL.md` actually fired. Required for v2 to learn which rules are load-bearing.
- **`user_consent_share`** — Boolean. False by default. Set to true only by an explicit second prompt at run end (section 7).

The schema is intentionally narrow. A trajectory is a record of *what the skill did*, not *what the user said*.

## What Is NEVER Logged

The trajectory schema is allowlist, not denylist. Anything not explicitly listed in section 4 is not logged. In particular, the following are forbidden under any condition, including in `outcome_score_reason` and `agent_observations` free-text fields:

- **No customer names, company names, or organization names.** Not the user's company. Not their customers. Not their competitors.
- **No revenue numbers, ARR, MRR, valuation, runway, headcount, or any other financial figure.** Not rounded. Not bucketed. Not approximated.
- **No verbatim survey responses, interview quotes, or customer voice excerpts.** These are the most identifying artifacts in strategy work.
- **No employee names, titles, or roles.** "The VP of Marketing said X" is forbidden. "A stakeholder raised a concern" is acceptable.
- **No competitor names.** Generic shape ("a larger incumbent", "a venture-backed challenger") only.
- **No personally identifying information of any kind.** Names, emails, phone numbers, addresses, social handles, account IDs.
- **No file paths from the user's system.** Deliverable filenames are logged. Absolute paths are not.
- **No model API keys, OAuth tokens, environment variable values, or credentials of any kind.** If a credential appears in input, the facilitator must refuse to write the trajectory at all.

> The privacy floor is not a stylistic preference. It is the condition under which any trajectory data exists at all. A skill that cannot honor it must not log.

When the facilitator is uncertain whether a note crosses the line, the rule is: do not write it. A missing observation is recoverable. A leaked one is not.

## Storage Locations

Default storage:

```
./<skill-name>-output/.trajectory.yaml
```

The leading dot makes the file hidden by default and signals to users that this is metadata, not deliverable content. It sits alongside the skill's actual outputs so the user sees it the moment they open the output directory.

User-overridable when the CLI exists (v1.5+):

```
--trajectory-path=<path>
```

Constraints on storage behavior:

- Trajectory files are written only inside the user's working directory or to the explicit `--trajectory-path` location.
- Nothing is written to `~`, `/tmp`, system caches, or any directory the user did not nominate.
- No trajectory is ever transmitted over the network by the skill itself. Sharing requires the user to attach the file to a PR, email, or upload of their own choosing.
- Existing trajectory files are never silently overwritten. A second run produces a second file with a fresh UUID.

## Opt-In UX

Two prompts. Both default to no. Both explain what would be shared.

**At skill start:**

> Would you like to log an anonymized trajectory of this run? It will be stored locally only, at `./<skill-name>-output/.trajectory.yaml`. It records which phases ran, which facilitation rules fired, and your self-reported outcome score at the end. It never logs company names, financial figures, customer quotes, or any personally identifying information. (yes/no, default no)

**At skill end:**

> Want to share this trajectory with the Resilience Stack maintainers to help train future curator agents? Sharing means you will attach the trajectory file to a pull request or submission of your own choosing — nothing is uploaded automatically. Before you share, run the anonymization checklist in `case-studies/README.md` and confirm the file contains no identifying content. (yes/no, default no)

The second prompt sets `user_consent_share`. A trajectory with `user_consent_share: false` is local-only forever. A trajectory with `user_consent_share: true` is still local-only until the user takes a deliberate sharing action.

A user who answers "no" to the first prompt produces no file. A user who answers "yes" to the first and "no" to the second produces a file that stays on their machine.

## Future Use — v2 Curator

The reason this spec exists in v1.5 at all is that v2 introduces the Curator agent. The Curator reads aggregated, anonymized trajectories submitted by users and proposes operations against the SkillRepo:

- **Insert** — propose a new skill or a new phase inside an existing skill when trajectories show a recurring gap.
- **Update** — propose a refined facilitation rule, prescription, or phase ordering when trajectories show that the current shape produces predictable failures.
- **Delete** — propose retirement of a skill, phase, or rule when trajectories show it never triggers, never correlates with positive outcomes, or actively correlates with low scores.

This pattern is taken directly from Google's *SkillOS* paper, which establishes that a curator agent operating over trajectory logs can produce more durable skill libraries than human-only curation, provided the trajectory schema is narrow enough to avoid overfitting and the privacy contract is strong enough to keep contributors willing to submit. The first condition is satisfied by the schema in section 4. The second is satisfied by the privacy floor in section 5.

See `ROADMAP.md` for the v2 timeline and Curator design notes.

**To repeat: implementation is deferred to v2.** The v1.5 release ships zero trajectory infrastructure. No skill in `skills/` writes a trajectory file in v1.5. The spec is published now so the schema can be reviewed before the code exists, not after.

## Anonymization Rules — User-Side Checklist

A user who decides to share a trajectory must run the same anonymization checklist used for the worked case studies in `case-studies/README.md`. The checklist is short and load-bearing:

- **Replace company names with "Synthetic Co."** Both the user's company and any third party. If multiple companies appear, use "Synthetic Co A", "Synthetic Co B".
- **Round all monetary figures to the nearest $5M.** ARR, valuation, raise size, deal size. If rounding would still identify the company (e.g. only one company in a category raised "$25M"), round further or omit entirely.
- **Strip all named individuals.** Replace with role-free placeholders ("a stakeholder", "a contributor"). Roles like "VP of Marketing" are themselves identifying and must be removed.
- **Strip vertical and geography when the combination is identifying.** "A Series B B2B SaaS company in Boston in legal tech" is identifying. "A growth-stage B2B SaaS company" is not.
- **Re-read the file end-to-end before submission.** The user must confirm sanitization explicitly. The maintainers will reject any submission that violates the privacy floor and will not store the raw file.

> Anonymization is the user's responsibility. The library's responsibility is to make anonymization possible by never logging the hard-to-anonymize fields in the first place.

## Open Questions for v2

The following decisions are explicitly deferred. v1.5 does not pre-commit to any answer:

- **Aggregation format and transport.** PR-based submission to a public repo vs. an authenticated API endpoint vs. signed email attachments. Each has different privacy, auditability, and friction tradeoffs. v2 will pick one and justify it in writing.
- **Privacy review process.** Whether submitted trajectories go through human review before entering the Curator training set, automated pattern review, or both. Likely both, but the gating order is undecided.
- **Composite reward signal.** Whether the Curator should weight `outcome_score` alone, blend it with `facilitation_rules_triggered` counts, or incorporate downstream signals from users who re-run the same skill. The risk of overfitting to a 1–10 self-report is real and must be addressed.
- **Curator agent architecture.** Single-shot proposer, multi-agent committee, or human-in-the-loop assistant. The SkillOS paper favors the third for early-stage libraries. Resilience Stack will start there.

Each open question becomes a separate spec document before any v2 code is merged. The principle is the same as v1.5: publish the contract before writing the implementation.

---

*Petrichor Projects · CC BY 4.0 · Specification v1.0 · 2026-05-12*
