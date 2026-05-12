#!/usr/bin/env python3
"""
Patch all 18 Resilience Stack skills with:
1. Tightened description for BM25 retrieval (one-sentence what+when+why)
2. Inserted `## When NOT to use` block after Framework section

Based on SkillOS / Anthropic skills schema best practices.
"""
import os
import re
from pathlib import Path

ROOT = Path("/Users/philipprimmler/Downloads/Projects/resilience-stack/skills")

# {skill_name: (track, tightened_description, when_not_to_use_block)}
PATCHES = {
    "relevancy-audit": (
        "positioning",
        "Diagnose positioning decay across 3 stages (Drift → Disconnect → Displacement) and produce a 90-day signal-refresh roadmap. Use when win rates are declining, sales cycles are extending, or share of voice has flattened.",
        [
            "Pre-product-market-fit — no positioning to decay yet.",
            "Total category collapse — the question is exit strategy, not positioning refresh.",
            "Operational fires (hiring, runway, ops) consuming all leadership bandwidth — schedule after stabilization.",
            "Recently completed positioning work (<6 months) — skill expects measurable signal drift.",
        ],
    ),
    "positioning-under-pressure": (
        "positioning",
        "Apply competitive, market, and narrative pressure to current positioning, surface fault lines across 4 attack vectors, and produce a Positioning Durability Score with defense architecture. Use when entering a new competitive cycle, planning a raise, or anticipating a market shift.",
        [
            "Positioning has never been formalized — run `relevancy-audit` first.",
            "Pre-revenue companies with no real competitive engagements to stress test.",
            "Team lacks emotional resilience to be attacked live — facilitator must read the room.",
            "Leadership team incomplete — defense architecture requires the full set of owners present.",
        ],
    ),
    "competitive-narrative-stress-test": (
        "positioning",
        "Reverse-engineer competitor narratives, map your story's attack surface across 5 layers, force you to face the competitor's best pitch, and prove the rebuild under 60-second oral delivery. Use when lost-deal post-mortems blame the narrative, or when entering a head-to-head category fight.",
        [
            "No named competitors yet (true blue-ocean) — `category-creation-pressure-test` is the right tool.",
            "Cannot collect verbatim competitor language — skill is evidence-required.",
            "Sales leader unwilling to provide candid lost-deal reasons.",
            "Recent positioning rewrite (<30 days) — give the new narrative time to gather signal.",
        ],
    ),
    "reality-audit": (
        "diagnostic",
        "Surface the gap between what the team believes is true and what the evidence shows across product, revenue, customer, and team layers. Use as a kickoff diagnostic before any major strategic decision or investor process.",
        [
            "Team in active crisis mode (layoffs, board fight) — defer until operational stability returns.",
            "Founder-only company (<3 people) — peer pressure dynamics that surface gaps don't exist yet.",
            "Recently completed honest external audit (<90 days) — diminishing return on re-diagnosis.",
            "Cannot pull objective data (no analytics, no CRM, no financial records) — skill is evidence-required.",
        ],
    ),
    "false-familiarity": (
        "brand",
        "Expose the trap of buyers recognizing your brand without recalling what it does, mapping 4 trap layers plus Trust Migration. Use when brand awareness metrics look healthy but pipeline, consideration, or recall scores have stagnated.",
        [
            "Early-stage brand (<24 months) — no familiarity built yet to be false.",
            "Niche B2B with <5K total addressable buyers — sample sizes won't support the survey methodology.",
            "Brand awareness has never been measured — establish baseline first via simple survey.",
            "Currently mid-rebrand — rerun 90 days after launch.",
        ],
    ),
    "brand-as-memory-system": (
        "brand",
        "Map how your brand actually lives in buyer minds via Category Entry Points, Distinctiveness Assets, association networks, and retrieval contexts. Use when CMOs report declining unaided recall, when launching a new category entry, or when refreshing brand investment allocation.",
        [
            "Cannot run external surveys (15-25 customers + 15-25 prospects + 10 lapsed) — skill is external-data-required.",
            "Pre-PMF — no consistent brand impression yet to memorize.",
            "Recent major rebrand (<6 months) — memory hasn't formed against new identity yet.",
            "Single-buyer or single-account business — memory architecture is a mass-market construct.",
        ],
    ),
    "legacy-brand-relevance-reset": (
        "brand",
        "Diagnose when heritage becomes a constraint and design evolution that does not erase credibility. Use when older buyer cohorts dominate revenue, when innovation launches keep underperforming, or when stakeholders block change citing tradition.",
        [
            "Brand younger than 10 years — not yet legacy enough to require reset.",
            "Recent heritage rebrand (<18 months) — give the market time to absorb.",
            "Cannot interview long-tenure customers OR founder/long-tenure employees — both perspectives required.",
            "Company in pure crisis (cash <6 months) — heritage debate is the wrong fight.",
        ],
    ),
    "brand-permission-boundaries": (
        "brand",
        "Surface what the market will and will not let your brand become, mapping Permission Floor + Ceiling + Stretch Zone with Equity Draw-Down cost per extension. Use before launching adjacent products, new categories, or premium tiers — never after.",
        [
            "First-product company — no permission earned yet to test boundaries of.",
            "Already launched the extension — too late for permission diagnostic; use `false-familiarity` to measure damage.",
            "Cannot survey 15-25 customers on the extension hypothesis — skill is evidence-required.",
            "Crisis pivot driven by survival — permission analysis is academic when revenue requires the move.",
        ],
    ),
    "revenue-story-audit": (
        "growth",
        "Forensic audit comparing the revenue story you tell vs the mechanics of how revenue actually works, producing a reconciled two-version narrative (internal-honest + externally-defensible). Use 6-12 months before a raise, before a board reset, or after a deal where the buyer narrative didn't survive diligence.",
        [
            "Pre-revenue companies — no story-vs-mechanics gap to audit yet.",
            "Cannot access 4 quarters of segmented revenue data — skill is evidence-required.",
            "Public companies bound by Reg FD — narrative reconciliation may create disclosure obligations.",
            "Audit team incomplete — CEO, CFO, and Head of Sales must all be present and candid.",
        ],
    ),
    "pricing-authority-diagnostic": (
        "growth",
        "Audit whether prices signal authority or just fit a spreadsheet, mapping discount patterns, value-metric integrity, and willingness-to-pay reality. Use when NRR is below 110%, when discount % is climbing quarter-over-quarter, or before any pricing increase.",
        [
            "Pre-product-market-fit — pricing experimentation is the right move, not pricing audit.",
            "Cannot pull 4 quarters of closed-won deal data with discount reasons coded — evidence-required.",
            "Currently implementing a price increase — wait 90 days post-rollout for accurate signal.",
            "Single-tier flat pricing with <12 months of data — insufficient variance for pattern analysis.",
        ],
    ),
    "category-creation-pressure-test": (
        "market-definition",
        "Diagnose whether you are creating a real category or claiming one that doesn't exist, testing buyer mental models, analyst readiness, category economics, and narrative capacity. Use before raising on a category-creation thesis, before naming a category publicly, or after analyst pushback.",
        [
            "Selling into a well-defined existing category — `relevancy-audit` or `positioning-under-pressure` are right.",
            "Cannot survey 10-15 buyers about category language — skill is buyer-evidence-required.",
            "<$5M ARR — usually too early to justify category creation costs.",
            "Already named the category publicly and shipped it — `competitive-blind-spot-mapping` to defend it instead.",
        ],
    ),
    "tam-lie-detector": (
        "market-definition",
        "Stress test TAM/SAM/SOM claims for inflation, double-counting, and adoption-curve hand-waves, producing a defensible market size with explicit assumptions. Use before any raise, before a board-level strategy reset, or before signing a partnership predicated on market projections.",
        [
            "Pre-product TAM exercises with no comparable buyer data — `category-creation-pressure-test` is the better tool.",
            "Regulatory-defined market (e.g., a specific FDA-approved indication) — TAM is exogenous, not negotiable.",
            "Board has already accepted the TAM — re-litigating without a triggering event burns trust.",
            "Cannot access bottom-up customer data to validate top-down claims.",
        ],
    ),
    "competitive-blind-spot-mapping": (
        "intelligence",
        "Surface what competitors see about you that you don't see about them, via War Room simulation, Asymmetry Audit, Win/Loss Archaeology, and Perception Gap survey. Use after losing 3+ consecutive deals to the same competitor, before a major pricing move, or quarterly as a competitive hygiene check.",
        [
            "First-mover with no real competitors — `category-creation-pressure-test` instead.",
            "Cannot conduct 20 win/loss interviews — skill is evidence-required.",
            "Just completed a competitive teardown (<60 days) — diminishing return.",
            "Sales leadership unwilling to provide candid loss reasons — skill will produce a flattering fiction.",
        ],
    ),
    "signal-vs-noise-audit": (
        "intelligence",
        "Diagnose which market signals deserve a strategic response and which are distractions, using the NATO Admiralty Grid (A-F × 1-6) plus Decision Velocity audit. Use when leadership team feels reactive, when 3+ pivots have happened in 12 months, or when a major market event triggered an over-response.",
        [
            "Cannot list 20+ recent signals leadership responded to — skill requires trajectory data.",
            "Pre-revenue companies — signal/noise discrimination requires market exposure.",
            "Single-decision-maker company (no committee) — bias map is internal, not structural.",
            "Currently mid-pivot — let the pivot land before auditing the signal that triggered it.",
        ],
    ),
    "customer-truth-extraction": (
        "intelligence",
        "Surface what customers actually believe vs what you think they believe, mapping 4 belief layers (Stated, Revealed, Implicit, Counter-belief). Use when NPS and renewal data diverge, when churn surprises leadership, or before redesigning the value proposition.",
        [
            "Pre-PMF companies with <10 customers — sample size too small for belief patterns.",
            "Cannot run 5+ Enemy Customer interviews (no permission-to-be-honest customers reachable).",
            "Just ran a major customer research project (<90 days) — leverage that first.",
            "Customer base is single-buyer enterprise (1-3 accounts) — direct conversation beats this protocol.",
        ],
    ),
    "investor-story-forensics": (
        "investor",
        "Forensic cross-examination of the investor narrative across 5 claim classes (Why-We-Win, Why-Now, Why-Us, Why-This-Trajectory, Why-This-Price). Use 90+ days before a fundraise, after a failed raise, or before any partner meeting where diligence is expected.",
        [
            "Already in due diligence (<14 days to term sheet) — too late; preserve narrative consistency, don't rebuild.",
            "Cannot list 5 reference customers who will pick up a diligence call.",
            "Pre-product company raising on team alone — `bear case pre-mortem` framing doesn't yet apply.",
            "Insider round with existing investors who already know the story — diminishing return.",
        ],
    ),
    "board-narrative-alignment": (
        "investor",
        "Audit whether the board hears the same story the market hears across 5 axes, plus expectation-ratchet mapping. Use 30 days before any difficult board conversation, after a board surprise, or when board cadence has degraded.",
        [
            "First board meeting — no narrative history to audit yet.",
            "Pre-board company (advisors only) — informal expectation management is more efficient.",
            "Board has unanimous confidence — defer to the next forcing function.",
            "Cannot pull last 4 board decks verbatim — skill requires the full longitudinal record.",
        ],
    ),
    "exit-narrative-architecture": (
        "investor",
        "Test whether the company story survives acquirer scrutiny via 6 acquirer-facing dimensions, including Quality of Earnings pre-mortem and Management Presentation Crucible. Use 6-12 months before formal exit process, after an unsolicited inbound, or before hiring a banker.",
        [
            "Less than $5M ARR — exit narrative is premature; revenue mechanics still being built.",
            "No identified acquirer types yet — `tam-lie-detector` + `category-creation-pressure-test` first.",
            "Already in LOI / exclusivity — too late to rebuild; preserve continuity instead.",
            "Strategic-only buyer scenario with one logical acquirer — single-buyer dynamic invalidates archetype mapping.",
        ],
    ),
}


def patch_skill(skill_name, track, new_description, when_not_to_use):
    """Read skill file, replace description, insert When NOT to use block."""
    path = ROOT / track / skill_name / f"{skill_name}.md"
    if not path.exists():
        return False, f"NOT FOUND: {path}"

    txt = path.read_text()

    # 1. Replace description line in frontmatter
    new_desc_line = f"description: {new_description}"
    txt2 = re.sub(
        r"^description:.*$",
        new_desc_line,
        txt,
        count=1,
        flags=re.MULTILINE,
    )
    if txt2 == txt:
        return False, "description not replaced"

    # 2. Insert When NOT to use block. Place AFTER the Framework block and BEFORE the
    # "## FACILITATION PROTOCOL" line. Pattern: line "---" followed by "## FACILITATION".
    when_not_block_lines = ["", "## When NOT to use", ""]
    for item in when_not_to_use:
        when_not_block_lines.append(f"- {item}")
    when_not_block_lines.append("")
    when_not_block_lines.append("---")
    when_not_block = "\n".join(when_not_block_lines)

    # Match the separator + FACILITATION heading
    pattern = re.compile(
        r"^---\s*\n+## FACILITATION PROTOCOL",
        flags=re.MULTILINE,
    )
    if not pattern.search(txt2):
        return False, "FACILITATION marker not found"

    txt3 = pattern.sub(
        when_not_block + "\n\n## FACILITATION PROTOCOL",
        txt2,
        count=1,
    )

    path.write_text(txt3)
    return True, "OK"


def main():
    results = []
    for skill, (track, desc, when_not) in PATCHES.items():
        ok, msg = patch_skill(skill, track, desc, when_not)
        results.append((skill, ok, msg))

    for s, ok, msg in results:
        prefix = "✓" if ok else "✗"
        print(f"{prefix} {s}: {msg}")
    ok_count = sum(1 for _, ok, _ in results if ok)
    print(f"\n{ok_count}/{len(results)} skills patched")


if __name__ == "__main__":
    main()
