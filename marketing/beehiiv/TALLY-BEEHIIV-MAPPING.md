# Tally → Beehiiv Plumbing Spec

End-to-end data flow for the 5 v1.5 quizzes. Tally captures responses; Beehiiv scores them and routes to the right tier drip.

---

## 1. Architecture (one diagram)

```
[Tally form] --webhook--> [Zapier zap] --API--> [Beehiiv list + custom fields]
                                                       |
                                                  [Automation: score + tier tag]
                                                       |
                                                       v
                                             [4 tier-specific drip emails]
                                                       |
                                                       v
                                                [Subscriber inbox]
```

One zap per quiz, one Beehiiv publication (or one publication + one tag per quiz — both work). Recommend separate publications because tier-routing automations are simpler against a single list.

---

## 2. Beehiiv setup (per quiz)

### 2a. Create publication

- Name: `Resilience Stack — <quiz-slug>`
- Sender name: `Phil Rimmler`
- Sender email: `phil@petrichorgrowth.com`
- Reply-to: `phil@petrichorgrowth.com`
- Default audience: this publication

### 2b. Custom fields (Settings → Audience → Custom fields)

Add these on every publication. Names must match exactly so the same Zap template works across quizzes.

| Field name | Type | Source |
|---|---|---|
| `first_name` | Text | Tally `First name` |
| `q1` | Text | Tally Q1 answer label |
| `q2` | Text | Tally Q2 answer label |
| `q3` | Text | Tally Q3 answer label |
| `q4` | Text | Tally Q4 answer label |
| `q5` | Text | Tally Q5 answer label |
| `score` | Number | Computed in Zap (sum of per-Q point values) |
| `tier` | Text | Computed in Zap (`tier-0` / `tier-1` / `tier-2` / `tier-3`) |
| `quiz_slug` | Text | Hardcoded per quiz |

### 2c. Per-quiz scoring tables

Each option maps to a numeric value. Zap computes `score = q1_val + q2_val + q3_val + q4_val + q5_val`, then maps to tier.

#### Tier thresholds (universal across all 5 quizzes)

| Score range | Tier |
|---|---|
| 0–5 | `tier-0` |
| 6–10 | `tier-1` |
| 11–15 | `tier-2` |
| 16–20 | `tier-3` |

#### Per-option point values

Authoritative source: `marketing/quizzes/<quiz-slug>.md` — "5 Diagnostic Questions" section. Order across all quizzes is: option A = 0 pts, B = 1, C = 2, D = 3 (verified against every quiz spec). The Zap maps by exact-string match on the answer label.

---

## 3. Zapier zap (per quiz)

One zap per quiz. Identical structure; only the Tally form ID, Beehiiv publication ID, and `quiz_slug` change.

### Step 1 — Trigger: Tally → "New submission"

- Connect Tally account
- Form: pick by Tally form ID
  - relevancy-audit: `aQe6A9`
  - revenue-story-audit: `aQAkJE`
  - competitive-narrative-stress-test: `jaJg86`
  - pricing-authority-diagnostic: `1ANOQL`
  - investor-story-forensics: `ob5gjM`

### Step 2 — Formatter (Numbers → Run Lookup Table) × 5

One formatter step per question. Map answer label → point value.

Example for relevancy-audit Q1:

| Lookup key | Lookup value |
|---|---|
| `Improving` | `0` |
| `Flat` | `1` |
| `Down 3–15%` | `2` |
| `Down 16% or more` | `3` |

Repeat for Q2–Q5 using the values in `marketing/quizzes/<quiz-slug>.md`. If a label does not match, the formatter returns blank — wire a default of `0` to avoid breaking the sum.

### Step 3 — Formatter (Numbers → Perform Math)

Operation: Add
Inputs: Q1 value, Q2 value, Q3 value, Q4 value, Q5 value
Output: `score`

### Step 4 — Formatter (Utilities → Lookup Table)

Map `score` → `tier`. One lookup with 4 entries:

| Min | Max | Tier |
|---|---|---|
| 0 | 5 | `tier-0` |
| 6 | 10 | `tier-1` |
| 11 | 15 | `tier-2` |
| 16 | 20 | `tier-3` |

Zapier's Lookup Table is exact-match. Easier alternative: use a Code step (JavaScript) — one line:

```javascript
const score = inputData.score;
return { tier:
  score <= 5  ? 'tier-0' :
  score <= 10 ? 'tier-1' :
  score <= 15 ? 'tier-2' :
                'tier-3'
};
```

### Step 5 — Beehiiv → "Create or update subscriber"

- Publication: <pick per quiz>
- Email: Tally `Email`
- Custom fields (map from prior steps):
  - `first_name` ← Tally `First name`
  - `q1`..`q5` ← Tally answer labels
  - `score` ← Step 3 output
  - `tier` ← Step 4 output
  - `quiz_slug` ← hardcoded (`relevancy-audit`, etc.)
- Subscribe to publication: yes
- Welcome email: **off** (the tier-conditional welcome lives in Beehiiv automation, not the default publication welcome)

### Step 6 — Beehiiv → "Add tag to subscriber"

- Tag: value of `tier` from Step 4

Beehiiv automations are tag-triggered (see §4).

---

## 4. Beehiiv automation (per publication)

One automation per publication, 4 branches by `tier` tag.

### Trigger

Subscriber receives tag `tier-0` OR `tier-1` OR `tier-2` OR `tier-3`.

### Branches

Each branch is one If/Else gate on `tier` tag, then:

1. Send tier welcome email (immediate) — body from `marketing/beehiiv/<quiz-slug>/welcome.md` § matching tier
2. Wait — see schedule below
3. Send drip email 1
4. Wait
5. Send drip email 2
6. ... (5 drips total)

### Drip schedule (universal across all 4 tiers)

| Day after submission | Email |
|---|---|
| 0 (within 60s) | Welcome (tier-conditional) |
| Day 2 | Drip 1 |
| Day 4 | Drip 2 |
| Day 7 | Drip 3 |
| Day 10 | Drip 4 |
| Day 14 | Drip 5 |

Tier 3 deviates: Phil sends a personal Loom + email manually within 48h. The drip still fires.

### Drip copy

Pending — Phase A of this rollout. Topic outlines already speced in `marketing/quizzes/<quiz-slug>.md` under each tier.

---

## 5. Test plan (before going live)

For each quiz, fire one synthetic submission per tier (4 boundary tests):

| Test | Answers | Expected score | Expected tier |
|---|---|---|---|
| Boundary 0/1 | All option A | 0 | `tier-0` |
| Boundary 1/2 | 2× option C + 3× option B | 7 | `tier-1` |
| Boundary 2/3 | All option C | 10 | `tier-1` |
| Mid Tier 2 | 1× A + 4× C | 8 ... wait that's tier-1 |
| Mid Tier 2 | 5× option C | 10 → tier-1 |
| Mid Tier 2 | 3× C + 2× D | 12 | `tier-2` |
| Mid Tier 3 | 5× option D | 15 | `tier-2` |
| Max | 5× D + override? | 15 (max possible w/ 4-option / 0–3) |

*Note: max attainable score = 5 questions × 3 max points = 15. **Tier 3 (16–20) is unreachable with the current scoring table.** This is a spec bug — fix one of:*

- *Option A: re-weight Q3 + Q4 (the most diagnostic) to 0/1/3/5 → max = 22, Tier 3 reachable*
- *Option B: re-bucket tiers to 0–3 / 4–7 / 8–11 / 12–15 → Tier 3 starts at 12*

*Recommend Option B (cleaner, no per-question re-weighting, preserves the 5-question / 4-option structure). Update the spec in `marketing/quizzes/<quiz-slug>.md` and the Zap lookup tables before going live.*

Confirm with Phil before final wiring.

---

## 6. Failure modes & guardrails

| Failure | Detection | Mitigation |
|---|---|---|
| Tally answer label changes (typo fix, etc.) | Zap fails Step 2 lookup | Lookup default `0`; Zap email alert on blank score |
| Zapier throttles / errors | Submission in Tally but not in Beehiiv | Zapier retries 3×; failed runs in Zap history; weekly reconciliation script: `tally_submissions - beehiiv_subscribers WHERE quiz_slug=X` |
| Beehiiv custom field schema drift | Subscriber created but score/tier missing | Lock schema; only edit via PR; document changes here |
| Two tier tags assigned to same subscriber (re-submission with different answers) | Subscriber in multiple drip branches | Beehiiv automation: clear all `tier-*` tags before adding the new one |
| Beehiiv welcome email fires by default | Subscriber gets generic welcome + tier welcome | Disable default welcome on every publication |
| Tier 3 not reachable (current scoring) | All real submissions cap at score 15 | Fix per §5 before launch |

---

## 7. Phil's checklist

Order matters. Skip any step and the pipeline silently fails.

- [ ] Decide tier scoring fix (§5) — re-bucket or re-weight
- [ ] Update tier thresholds in all 5 `marketing/quizzes/*.md` files and all 5 `marketing/beehiiv/*/welcome.md` files
- [ ] Create 5 Beehiiv publications (one per quiz)
- [ ] Add 9 custom fields to each publication (§2b)
- [ ] Build 5 Zapier zaps (§3) — start with relevancy-audit, duplicate + edit for others
- [ ] Build 5 Beehiiv automations (§4) with the welcome bodies from `marketing/beehiiv/<quiz>/welcome.md`
- [ ] Capture Calendly URL and Loom URLs; replace `{{calendly-url}}` and `{{loom-url}}` in the welcome emails
- [ ] Run 4 boundary tests per quiz (§5)
- [ ] Verify Tier 3 personal-response SLA against Phil's actual inbox capacity
- [ ] Soft launch with relevancy-audit first; observe one full week before enabling quizzes 2–5

---

## 8. Cost & limits

- Tally: free tier covers all 5 forms, unlimited submissions
- Zapier: 5 zaps × 100 free tasks/month is tight. Each submission = ~7 tasks (1 trigger + 5 formatters + 1 Beehiiv create + 1 tag = 8). 100 tasks / 8 = ~12 submissions/month free. **Recommend Zapier Starter ($29/mo, 750 tasks)** for the first 3 months, evaluate volume, then decide.
- Beehiiv: free tier covers 2,500 subscribers per publication. 5 publications × 2,500 = 12,500 free leads before paid tier kicks in. Comfortable for v1.5 launch.
- Total v1.5 marketing automation cost: **$29/mo** until Beehiiv free tier breaches.

---

*Resilience Stack v1.5 · CC BY 4.0 · Petrichor Projects*
