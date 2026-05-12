# Evals — Resilience Stack

Every skill has a test case. Test cases verify: skill triggers correctly, refuses correctly, and produces required deliverables.

## Structure

```
evals/
├── <skill-name>/
│   ├── case-01-baseline.yaml         # standard positive case
│   ├── case-02-when-not-to-use.yaml  # confirms negative gates fire
│   ├── case-03-adversarial.yaml      # break-the-skill attempt
│   └── golden/                        # expected deliverable shapes
│       ├── deliverable-1.schema.json
│       └── ...
└── README.md
```

## Eval Case Schema

```yaml
case_id: relevancy-audit-baseline-01
skill: relevancy-audit
description: Healthy growth-stage SaaS with measurable positioning drift.
input:
  company_name: Acme
  stage: growth ($30M ARR)
  symptom: win rate dropped 12% in 2 quarters
  evidence:
    - 4 quarters of win/loss data
    - 15 customer surveys with verbatim
    - 3 competitor positioning statements
expected_behavior:
  triggers: true
  refuses: false
  produces:
    - positioning-decay-map
    - signal-refresh-roadmap
    - stage-classification
    - competitive-position-snapshot
    - relevancy-scorecard
  duration_estimate_hours: 2.5
adversarial_checks:
  - skill must not accept "we are customer-obsessed" without specifics
  - skill must score stage classification (Drift / Disconnect / Displacement)
  - skill must produce written deliverables, not just verbal output
```

## Running Evals

v1 — manual review against schema files.
v1.5 — Python harness (`python3 evals/run.py <skill> <case>`) that loads case YAML, invokes skill via Claude API, compares output against `golden/`.

## Contribution

PRs that add eval cases for an existing skill auto-merge if validator passes. PRs that add new skills must include at least 2 eval cases.
