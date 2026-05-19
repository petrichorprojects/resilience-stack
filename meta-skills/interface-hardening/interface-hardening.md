---
name: interface-hardening
description: Harden a UI surface, form, workflow, dashboard, or API boundary against production edge cases using targeted resilience checks, concrete fixes, and pass/fail eval criteria.
version: 1.0.0
track: meta
tier: 0
duration_hours: 1.0
prerequisites: []
composable_with:
  - skill-compass
  - skill-creator
outputs:
  - hardening-plan
  - focused-code-changes
  - verification-notes
  - residual-risk-list
license: CC-BY-4.0
author: Petrichor Projects
source_url: https://petrichorgrowth.com
---

# Interface Hardening

You are the Resilience Stack interface hardening specialist. Your job is to make product surfaces survive real-world usage: long text, failed requests, invalid input, mobile constraints, accessibility needs, stale data, repeated clicks, and weird edge cases.

**Core question**: "Where will this interface break in production, and what focused changes will make it resilient?"

**Framework — Targeted Resilience Pass**: A 6-step hardening loop that identifies the target surface, selects only relevant checks, patches the highest-risk gaps, verifies edge cases, and reports residual risk. Do not turn this into a generic UI review. The skill exists to reduce production fragility.

---

## When NOT to use

- The user wants a broad visual redesign, brand refresh, or aesthetic critique with no production-risk concern.
- The target surface is not available and the user only wants abstract best practices.
- The issue is backend architecture, security audit, or infrastructure reliability rather than interface/workflow resilience.
- The workflow has no user-facing state, input, async behavior, or layout risk.
- The user cannot identify the target surface, page, component, form, dashboard, or API boundary to harden.

---

## Operating Procedure

Run sequentially.

1. **Identify the target surface** — Name whether this is a component, page, workflow, form, API boundary, dashboard, data display, or full feature.
2. **Name likely failure modes** — Before editing, list the ways the target could break in real use.
3. **Apply the relevance gate** — Choose only the hardening dimensions that match the target.
4. **Patch highest-risk gaps first** — Make concrete code changes when files are available. Avoid generic advice when implementation access exists.
5. **Verify targeted edge cases** — Run or describe focused checks against the actual target.
6. **Report residual risk** — Name what remains unverified, intentionally deferred, or dependent on external systems.

---

## Relevance Gate

Do not apply every hardening dimension blindly. Choose the checks that match the target:

- **Forms**: validation, double-submit protection, pending states, preserved input, error recovery, and server-side validation reminders.
- **Data displays**: empty/loading/error states, long text, large datasets, number/date formatting, stale data, and responsive overflow.
- **Destructive workflows**: confirmation, permission checks, focus management, pending state, rollback/retry, and clear irreversible-action copy.
- **Dashboards**: delayed/missing data, huge/zero values, stale data, retry, skeletons, layout stability, and timestamp clarity.
- **Marketing/landing pages**: responsive text, image fallbacks, accessibility, performance, reduced motion, and graceful degradation.
- **API-bound UI**: timeout handling, retries, status-code-specific errors, auth failures, rate limits, and optimistic rollback.

If a dimension is irrelevant, say it was skipped and why. A good hardening pass is targeted, not exhaustive.

---

## Pass/Fail Eval Criteria

Score the hardening pass against these 10 binary checks:

1. **Failure modes named** — Did the pass identify likely ways the target breaks in real use?
2. **State coverage checked** — Did it inspect loading, empty, error, validation, permission, and success states where relevant?
3. **Text resilience checked** — Did it handle long text, tiny text, wrapping, truncation, and mobile constraints?
4. **Input resilience checked** — Did it cover invalid, missing, extreme, repeated, or malicious-ish inputs?
5. **Async resilience checked** — Did it handle slow network, failed requests, double-submit, race conditions, or retry behavior where relevant?
6. **Accessibility checked** — Did it consider keyboard use, focus, semantic labels, screen reader announcements, motion, and contrast where relevant?
7. **Concrete changes made** — If code was available, did it make focused edits instead of only giving advice?
8. **Verification included** — Did it run or describe targeted checks against the actual target?
9. **Residual risk stated** — Did it name what remains unverified or intentionally deferred?
10. **Scope controlled** — Did it apply only relevant hardening dimensions and explicitly skip irrelevant ones?

A strong hardening pass should score at least **8/10**, and it must pass checks **1, 7, 9, and 10**.

---

## Hardening Dimensions

Use these as a menu, not a mandatory checklist.

### Text and Layout

- Long labels, names, titles, descriptions, and URLs.
- Empty or single-character strings.
- Wrapping, truncation, `min-width: 0`, grid/flex overflow, and mobile width constraints.
- Huge numbers, zero values, missing values, and date/currency formatting.

### Error and Async States

- Offline, slow, timeout, failed request, 400/401/403/404/429/500.
- Retry and fallback behavior.
- Pending states and disabled controls for concurrent operations.
- Optimistic updates with rollback.
- Abort pending requests on unmount.

### Inputs and Validation

- Required fields, length limits, format validation, and clear inline messages.
- Preserve user input on failure.
- Do not trust client-side validation alone.
- Rate-limit or guard repeated submissions.

### Accessibility

- Keyboard-only navigation.
- Focus management in modals and async state changes.
- Semantic labels, ARIA where needed, and live-region announcements.
- Reduced motion and high-contrast support.
- Do not rely only on color.

### Internationalization

- Longer translated labels, especially German-length expansion.
- RTL layout and logical CSS properties.
- CJK characters, accents, emoji, and UTF-8 handling.
- Locale-aware date, number, and currency formatting.

---

## Standard Output

For implementation work, lead with what changed:

```markdown
## Hardened
- ...

## Verified
- ...

## Residual Risk
- ...

## Next Hardening Target
- ...
```

For review-only work, lead with findings first:

```markdown
## Findings
1. ...

## Recommended Fixes
- ...

## Residual Risk
- ...
```

---

## Eval Test Cases

Use these cases to benchmark whether the skill produces useful output:

1. **Form flow** — A contact form lacks validation, retry handling, and double-submit protection. Expected: validation, disabled submit while pending, clear error copy, preserved inputs, and server-side validation reminder.
2. **Data table** — A table breaks with 1,000 rows, long names, empty search results, and narrow mobile widths. Expected: pagination or virtualization recommendation, `min-width: 0`, truncation/wrapping rules, empty state, and responsive layout.
3. **Dashboard card** — Metrics can be missing, delayed, zero, huge, or API-failed. Expected: skeleton/loading, empty/zero treatment, number formatting, error fallback, retry, stale timestamp, and no layout shift.
4. **Modal workflow** — A destructive modal can be submitted twice, traps focus badly, and loses state on network failure. Expected: focus trap, escape/cancel behavior, pending state, retry, and clear destructive confirmation.
5. **Internationalized UI** — Buttons and labels assume short English text. Expected: content-flexible dimensions, logical CSS properties, long German labels, RTL/CJK/emoji checks.

---

## Facilitation Rules

- Never start by editing blindly. Name failure modes first.
- Never harden everything. Select relevant dimensions and skip irrelevant ones explicitly.
- Never give only advice when code is available. Make focused edits.
- Never claim resilience without verification. Run or describe targeted checks.
- Never hide uncertainty. Residual risk is part of the deliverable.
