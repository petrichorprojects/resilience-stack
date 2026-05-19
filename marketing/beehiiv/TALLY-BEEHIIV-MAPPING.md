# Tally → Beehiiv Plumbing Spec

End-to-end data flow for the 5 v1.5 quizzes. Tally captures responses; **Category Gravity** (single Beehiiv publication) scores them, tags them, and routes to the right tier drip inside the **Resilience Stack** series.

---

## 1. Architecture

```
[Tally form × 5] --webhook--> [Zapier zap × 5] --API--> [Beehiiv: Category Gravity (single pub)]
                                                                    |
                                                          [Tags applied:
                                                            series-resilience-stack
                                                            quiz-<slug>
                                                            tier-<0|1|2|3>]
                                                                    |
                                                                    v
                                                          [One automation, 20 branches
                                                            (5 quizzes × 4 tiers)]
                                                                    |
                                                                    v
                                                          [Subscriber inbox]
```

**Key shift from v1 spec:** one Beehiiv publication (`Category Gravity`), not 5. Cross-pollination across quizzes — a relevancy-audit lead who later takes pricing-authority is already a sub, gets both drip arcs in parallel (both fire, tagged separately).

---

## 2. Beehiiv setup (Category Gravity pub)

### 2a. Publication

Already created by Phil. Confirm config:

- Name: `Category Gravity`
- Sender name: `Phil Rimmler`
- Sender email: `phil@petrichorgrowth.com`
- Reply-to: `phil@petrichorgrowth.com`
- Series 01 = Resilience Stack (this rollout). Future series = 02, 03, …

### 2b. Custom fields

Add once on the Category Gravity pub. All 5 zaps write to the same schema.

| Field name | Type | Source | Notes |
|---|---|---|---|
| `first_name` | Text | Tally `First name` | |
| `q1`..`q5` | Text | Tally Q1..Q5 answer labels | Per-quiz semantics differ; tag tracks which quiz |
| `score` | Number | Computed in Zap | Sum of per-Q point values |
| `tier` | Text | Computed in Zap | `tier-0` / `tier-1` / `tier-2` / `tier-3` |
| `quiz_slug` | Text | Hardcoded per Zap | `relevancy-audit`, etc. |
| `series` | Text | Hardcoded | `resilience-stack` |
| `last_quiz_taken_at` | Date | Zap sets to `now()` on submission | Updated on every new quiz; powers re-engagement logic |

### 2c. Tags

Apply on every submission. Multi-tag, additive (never replace).

| Tag pattern | When set |
|---|---|
| `series-resilience-stack` | On any of the 5 quiz submissions |
| `quiz-<slug>` | One of: `quiz-relevancy-audit`, `quiz-revenue-story-audit`, `quiz-competitive-narrative-stress-test`, `quiz-pricing-authority-diagnostic`, `quiz-investor-story-forensics` |
| `tier-<n>` | `tier-0` / `tier-1` / `tier-2` / `tier-3` (most recent quiz's tier) |
| `taken-<quiz>-tier-<n>` | Stamped tier per quiz. Example: `taken-relevancy-audit-tier-2`. **Never reset.** Lets the automation know which (quiz, tier) drip arcs the lead has already entered. |

### 2d. Cross-quiz logic

- Subscriber takes quiz #1 → tagged `series-resilience-stack`, `quiz-relevancy-audit`, `tier-2`, `taken-relevancy-audit-tier-2`
- Same subscriber later takes quiz #4 → tags become `series-resilience-stack` (already), `quiz-pricing-authority-diagnostic` (added), `tier-3` (replaces `tier-2`), `taken-pricing-authority-diagnostic-tier-3` (added; the `taken-relevancy-audit-tier-2` from before stays).
- Both drip arcs fire in parallel. The `taken-*` tag prevents the same arc from re-firing if the lead retakes the same quiz at the same tier.

The "most recent tier" tag (`tier-<n>`) drives general re-engagement campaigns (newsletter sends, Petrichor offers). The `taken-*` tags drive drip gating.

---

## 3. Zapier zap (per quiz × 5)

Identical structure to v1 spec, but Step 5 + 6 target Category Gravity instead of per-quiz pubs.

### Step 1 — Trigger: Tally → "New submission"

Form IDs:
- relevancy-audit: `aQe6A9`
- revenue-story-audit: `aQAkJE`
- competitive-narrative-stress-test: `jaJg86`
- pricing-authority-diagnostic: `1ANOQL`
- investor-story-forensics: `ob5gjM`

### Step 2 — Formatter (Numbers → Run Lookup Table) × 5

One per question. Source of truth: `marketing/quizzes/<slug>.md` "5 Diagnostic Questions" section.

Option order: A = 0, B = 1, C = 2, D = 3 (verified across all 5 quizzes). Default `0` on unmatched label.

### Step 3 — Formatter (Numbers → Perform Math)

`score = q1 + q2 + q3 + q4 + q5`

### Step 4 — Code by Zapier (JavaScript)

```javascript
const score = Number(inputData.score);
return { tier:
  score <= 5  ? 'tier-0' :
  score <= 10 ? 'tier-1' :
  score <= 15 ? 'tier-2' :
                'tier-3'
};
```

**Note on tier 3 reachability:** with current spec (5 Qs × 4 options × 0–3 pts) max score = 15, so tier-3 is unreachable. **Decision pending — see §6.** Until rebucket lands, the `score <= 15` branch catches all tier-2+ submissions.

### Step 5 — Beehiiv → "Create or update subscriber"

- Publication: **Category Gravity**
- Email: Tally `Email`
- Custom fields:
  - `first_name` ← Tally `First name`
  - `q1`..`q5` ← Tally answers
  - `score` ← Step 3
  - `tier` ← Step 4
  - `quiz_slug` ← hardcoded per Zap
  - `series` ← `resilience-stack`
  - `last_quiz_taken_at` ← Zap `Format → Date/Time → now`
- Subscribe: yes
- Default publication welcome: **off** (tier welcome lives in automation)

### Step 6 — Beehiiv → "Add tags to subscriber"

Add 4 tags in one call:
1. `series-resilience-stack`
2. `quiz-<slug>` (hardcoded per Zap)
3. `tier-<n>` from Step 4
4. `taken-<slug>-tier-<n>` (concatenate)

⚠️ **Remove `tier-*` first** before adding the new one. Beehiiv's "Add tag" is additive, so a re-take would leave both `tier-2` and `tier-3` on the sub. Use a `Remove tag` step first, looping over `tier-0`/`tier-1`/`tier-2`/`tier-3`, then add the new one. The `taken-*` tag from prior takes stays.

---

## 4. Beehiiv automation (single, inside Category Gravity)

One automation. Trigger: subscriber tagged with any `taken-*-tier-*` tag.

### Branch structure

20 branches = 5 quizzes × 4 tiers. Each branch:

1. If/Else gate on `taken-<slug>-tier-<n>` tag
2. Send tier welcome email (immediate) — body from `marketing/beehiiv/<slug>/welcome.md` matching tier section
3. Wait → drip 1 (Day 2)
4. Wait → drip 2 (Day 4)
5. Wait → drip 3 (Day 7)
6. Wait → drip 4 (Day 10)
7. Wait → drip 5 (Day 14)

### Drip schedule (universal)

| Day after submission | Email |
|---|---|
| 0 (within 60s) | Welcome (tier-conditional) |
| Day 2 | Drip 1 |
| Day 4 | Drip 2 |
| Day 7 | Drip 3 |
| Day 10 | Drip 4 |
| Day 14 | Drip 5 |

Tier 3 deviation: Phil sends a personal Loom + email manually within 48h. Drip still fires in parallel.

### Drip copy

Pending Phase A. Topics outlined in `marketing/quizzes/<slug>.md` per tier.

---

## 5. Welcome email branding (Category Gravity wrap)

All 5 welcome files in `marketing/beehiiv/<slug>/welcome.md` keep their tier-conditional body. Add this universal wrap inside Beehiiv send templates:

**Header (above the personalized body):**

```
[Category Gravity]
Series 01 — Resilience Stack
```

**Footer (below the personalized body, above the sign-off):**

```
You are reading Category Gravity, Petrichor Projects' newsletter on
positioning, pricing, and narrative discipline. This email is part of
Series 01 — Resilience Stack. Reply to this email to talk to me directly.

— Phil
```

**Unsubscribe + sender block:** Beehiiv default footer, no edits.

---

## 6. ⚠️ Tier 3 unreachable — decision pending

Max attainable score with current scoring (5 Qs × 4 options × 0–3 pts) = 15. Tier 3 (16–20) is unreachable.

**Options:**

- **A) Rebucket tiers** (recommended): Tier 0: 0–3 / Tier 1: 4–7 / Tier 2: 8–11 / Tier 3: 12–15
- B) Re-weight Q3 + Q4 to 0/1/3/5 → max = 22, original ranges preserved
- C) Keep current, treat Tier 2 max as effective Tier 3

Until decision: 5 quiz specs, 5 welcome emails, and the Step 4 lookup all reflect the old 0–5/6–10/11–15/16–20 ranges. Going live before fixing this means real submissions never trigger Tier 3 drips.

Recommend Option A. I will execute the 10-file edit in a separate PR after Phil confirms.

---

## 7. Test plan (per quiz, before going live)

For each quiz, fire 4 synthetic submissions, one per tier under the rebucketed thresholds (assumes Option A):

| Test | Answer pattern | Score | Expected tier |
|---|---|---|---|
| Tier 0 boundary | All option A | 0 | `tier-0` |
| Tier 1 boundary | 3× option A + 2× option B | 2 | `tier-0` (sanity) |
| Tier 1 mid | 4× option B + 1× option C | 6 | `tier-1` |
| Tier 2 mid | 5× option B + 0 (3B + 2C) | 7 → 8 | check `tier-2` start at 8 |
| Tier 3 boundary | All option D | 15 | `tier-3` |

Boundary verification: scores 3, 4, 7, 8, 11, 12 — confirm correct tier per the lookup.

---

## 8. Failure modes & guardrails

| Failure | Detection | Mitigation |
|---|---|---|
| Tally answer label drifts | Zap Step 2 returns blank | Lookup default `0`; weekly reconciliation Zap |
| Zap throttle / error | Tally submission has no matching Beehiiv sub | Zapier 3× retry; weekly diff script |
| Cross-quiz tier collision | Sub has multiple `tier-*` tags | Step 6 removes all `tier-*` before add (per §3 Step 6) |
| Default Beehiiv welcome fires | Sub gets generic + tier welcome | Disable default welcome on Category Gravity pub |
| Repeat submission re-fires drip | Same `taken-*` tag re-added | Beehiiv tag-add is idempotent; automation gates on `taken-*` not `tier-*` |
| Tier 3 unreachable | All submissions cap at tier-2 | §6 — rebucket before launch |

---

## 9. Cost & limits

- Tally: free tier, unlimited submissions across 5 forms
- Zapier: 5 zaps × ~8 tasks per submission. **Recommend Zapier Starter ($29/mo, 750 tasks)** for first 3 months.
- Beehiiv: Category Gravity on free tier covers 2,500 subscribers. Single pub means cross-quiz subs don't double-count. Upgrade trigger: 2,000 subs (80% of free tier).
- **Total v1.5 marketing automation cost: $29/mo** until Beehiiv free tier breaches.

---

## 10. Phil's checklist

Order matters.

- [ ] Confirm tier rebucket decision (§6) — recommend Option A
- [ ] If Option A: apply rebucket PR across `marketing/quizzes/*.md` + `marketing/beehiiv/*/welcome.md`
- [ ] Confirm Category Gravity pub config (§2a)
- [ ] Add 9 custom fields + 4 tag patterns to Category Gravity (§2b, §2c)
- [ ] Build 1 Zap (relevancy-audit) end-to-end; verify tag application + tier assignment
- [ ] Duplicate Zap × 4 for remaining quizzes; swap form ID + `quiz_slug`
- [ ] Build Beehiiv automation w/ 20 branches; load welcome bodies from `marketing/beehiiv/<slug>/welcome.md` w/ Category Gravity header/footer wrap (§5)
- [ ] Capture Calendly URL + 5 Loom URLs; replace placeholders in welcome bodies
- [ ] Run §7 test plan per quiz (4 submissions each = 20 total)
- [ ] Soft launch relevancy-audit; observe 1 week before enabling quizzes 2–5
- [ ] Set Beehiiv upgrade alert at 2,000 subs

---

*Resilience Stack v1.5 · Category Gravity Series 01 · Petrichor Projects · CC BY 4.0*
