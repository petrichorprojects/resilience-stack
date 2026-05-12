#!/usr/bin/env python3
"""
v1.2 upgrades — bring Resilience Stack to world-class spec.

For each skill, inject into frontmatter:
- version: 1.0.0 (semver)
- prerequisites: [<skill_name>, ...] (composability)
- composable_with: [<skill_name>, ...] (lateral pairing)
- outputs: [<deliverable_name>, ...] (structured outputs)
- estimated_duration_hours
- tier: 1|2|3
- track: positioning | brand | growth | ...
"""
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "skills"

# {skill_name: {field: value}}
META = {
    "relevancy-audit": {
        "track": "positioning",
        "tier": 1,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["positioning-under-pressure", "competitive-narrative-stress-test", "false-familiarity"],
        "outputs": ["positioning-decay-map", "signal-refresh-roadmap", "stage-classification", "competitive-position-snapshot", "relevancy-scorecard"],
    },
    "positioning-under-pressure": {
        "track": "positioning",
        "tier": 1,
        "duration_hours": 2.5,
        "prerequisites": ["relevancy-audit"],
        "composable_with": ["competitive-narrative-stress-test", "competitive-blind-spot-mapping"],
        "outputs": ["positioning-stress-test-results", "competitive-pressure-map", "position-defense-playbook", "positioning-fault-line-analysis", "positioning-scorecard"],
    },
    "competitive-narrative-stress-test": {
        "track": "positioning",
        "tier": 1,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["positioning-under-pressure", "competitive-blind-spot-mapping", "investor-story-forensics"],
        "outputs": ["competitive-narrative-map", "attack-surface-assessment", "reconstructed-narrative", "competitive-narrative-cards", "ceo-briefing-document"],
    },
    "reality-audit": {
        "track": "diagnostic",
        "tier": 1,
        "duration_hours": 3.0,
        "prerequisites": [],
        "composable_with": ["relevancy-audit", "revenue-story-audit", "customer-truth-extraction"],
        "outputs": ["reality-map", "belief-evidence-gap-report", "decision-readiness-score", "team-alignment-assessment", "reality-scorecard"],
    },
    "false-familiarity": {
        "track": "brand",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["brand-as-memory-system", "customer-truth-extraction"],
        "outputs": ["familiarity-trap-diagnostic", "recognition-vs-recall-gap-report", "trust-migration-map", "category-placement-audit", "familiarity-scorecard"],
    },
    "brand-as-memory-system": {
        "track": "brand",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["false-familiarity", "brand-permission-boundaries", "legacy-brand-relevance-reset"],
        "outputs": ["brand-memory-map", "association-inventory", "memory-trigger-assessment", "competitive-memory-analysis", "brand-memory-scorecard"],
    },
    "legacy-brand-relevance-reset": {
        "track": "brand",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["brand-as-memory-system", "brand-permission-boundaries", "relevancy-audit"],
        "outputs": ["heritage-asset-inventory", "constraint-assessment", "evolution-strategy", "stakeholder-communication-plan", "legacy-reset-scorecard"],
    },
    "brand-permission-boundaries": {
        "track": "brand",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["brand-as-memory-system", "category-creation-pressure-test"],
        "outputs": ["permission-boundary-map", "brand-stretch-assessment", "market-acceptance-zones", "expansion-risk-matrix", "permission-scorecard"],
    },
    "revenue-story-audit": {
        "track": "growth",
        "tier": 1,
        "duration_hours": 2.5,
        "prerequisites": ["reality-audit"],
        "composable_with": ["pricing-authority-diagnostic", "investor-story-forensics", "board-narrative-alignment"],
        "outputs": ["revenue-narrative-gap-report", "growth-mechanics-map", "channel-truth-assessment", "revenue-story-reconciliation", "revenue-scorecard"],
    },
    "pricing-authority-diagnostic": {
        "track": "growth",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["revenue-story-audit", "competitive-blind-spot-mapping", "customer-truth-extraction"],
        "outputs": ["price-value-gap-assessment", "competitive-pricing-map", "willingness-to-pay-reality-check", "pricing-architecture-recommendations", "pricing-scorecard"],
    },
    "category-creation-pressure-test": {
        "track": "market-definition",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["tam-lie-detector", "brand-permission-boundaries", "competitive-narrative-stress-test"],
        "outputs": ["category-viability-assessment", "market-readiness-analysis", "category-narrative-architecture", "buyer-category-mental-model-map", "category-scorecard"],
    },
    "tam-lie-detector": {
        "track": "market-definition",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["category-creation-pressure-test", "revenue-story-audit", "investor-story-forensics"],
        "outputs": ["tam-decomposition", "assumption-stress-test-results", "comparable-set-validation", "defensible-tam-statement", "tam-scorecard"],
    },
    "competitive-blind-spot-mapping": {
        "track": "intelligence",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["positioning-under-pressure", "signal-vs-noise-audit", "competitive-narrative-stress-test"],
        "outputs": ["blind-spot-map", "competitive-intelligence-gap-assessment", "win-loss-root-cause-analysis", "competitor-strategy-inference", "competitive-scorecard"],
    },
    "signal-vs-noise-audit": {
        "track": "intelligence",
        "tier": 3,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["competitive-blind-spot-mapping", "board-narrative-alignment"],
        "outputs": ["signal-integrity-report", "noise-reduction-protocol", "strategic-signal-dashboard", "decision-velocity-assessment", "signal-scorecard"],
    },
    "customer-truth-extraction": {
        "track": "intelligence",
        "tier": 2,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["false-familiarity", "pricing-authority-diagnostic", "reality-audit"],
        "outputs": ["customer-belief-map", "perception-reality-gap-analysis", "churn-risk-assessment", "customer-voice-synthesis", "customer-truth-scorecard"],
    },
    "investor-story-forensics": {
        "track": "investor",
        "tier": 3,
        "duration_hours": 2.5,
        "prerequisites": ["revenue-story-audit"],
        "composable_with": ["competitive-narrative-stress-test", "tam-lie-detector", "board-narrative-alignment"],
        "outputs": ["narrative-due-diligence-report", "claim-evidence-matrix", "vulnerability-assessment", "investor-faq-preparation", "investor-story-scorecard"],
    },
    "board-narrative-alignment": {
        "track": "investor",
        "tier": 3,
        "duration_hours": 2.5,
        "prerequisites": [],
        "composable_with": ["investor-story-forensics", "revenue-story-audit", "signal-vs-noise-audit"],
        "outputs": ["board-market-coherence-report", "narrative-divergence-map", "board-communication-strategy", "expectation-management-framework", "board-alignment-scorecard"],
    },
    "exit-narrative-architecture": {
        "track": "investor",
        "tier": 3,
        "duration_hours": 3.0,
        "prerequisites": ["investor-story-forensics", "tam-lie-detector"],
        "composable_with": ["board-narrative-alignment", "competitive-narrative-stress-test"],
        "outputs": ["exit-narrative-blueprint", "acquirer-perception-assessment", "value-driver-documentation", "risk-narrative-management-plan", "exit-readiness-scorecard"],
    },
}


def patch(skill_name, fields):
    """Find skill file across tracks; rewrite frontmatter with new fields."""
    track = fields["track"]
    path = ROOT / track / skill_name / f"{skill_name}.md"
    if not path.exists():
        return False, f"NOT FOUND: {path}"

    txt = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.DOTALL)
    if not m:
        return False, "no frontmatter"

    existing = yaml.safe_load(m.group(1)) or {}
    # merge: keep name/description, set new structured fields
    existing.setdefault("version", "1.0.0")
    existing["track"] = fields["track"]
    existing["tier"] = fields["tier"]
    existing["duration_hours"] = fields["duration_hours"]
    existing["prerequisites"] = fields["prerequisites"]
    existing["composable_with"] = fields["composable_with"]
    existing["outputs"] = fields["outputs"]
    existing["license"] = "CC-BY-4.0"
    existing["author"] = "Petrichor Projects"
    existing["source_url"] = "https://petrichorgrowth.com"

    new_frontmatter = yaml.safe_dump(
        existing,
        sort_keys=False,
        default_flow_style=False,
        allow_unicode=True,
        width=1000,
    ).strip()

    rebuilt = f"---\n{new_frontmatter}\n---\n" + txt[m.end():]
    path.write_text(rebuilt)
    return True, "OK"


def main():
    ok_count = 0
    for skill, fields in META.items():
        ok, msg = patch(skill, fields)
        prefix = "✓" if ok else "✗"
        print(f"{prefix} {skill}: {msg}")
        if ok:
            ok_count += 1
    print(f"\n{ok_count}/{len(META)} patched")


if __name__ == "__main__":
    main()
