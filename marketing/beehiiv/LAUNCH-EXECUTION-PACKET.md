# Resilience Stack — Launch Execution Packet

**Status:** Ready to execute. All upstream artifacts shipped (5 quizzes live on Tally, 100 drip emails written, 5 welcome emails written, landing page deployed at petrichorgrowth.com/resilience-stack).

**Owner:** Phil
**Estimated total time:** 4–5 hours across one focused afternoon
**Outcome at end:** End-to-end pipeline live. Quiz submission → score → tier → tagged in Beehiiv → tier-specific drip fires. Ready for soft-launch.

---

## Pre-flight checklist

Confirm before starting:

- [ ] Beehiiv account exists (Category Gravity is the pub). Pub ID accessible from Settings → API.
- [ ] Beehiiv API key generated. Settings → Integrations → API → Generate Key. Store in 1Password.
- [ ] Zapier account on paid tier (Code step requires Starter or higher).
- [ ] All 5 Tally forms live and capturing submissions (already confirmed — see TALLY-BEEHIIV-MAPPING.md §1).
- [ ] Calendly link finalized for {{calendly-url}} placeholder. Pick one: existing Petrichor Calendly OR new Resilience Stack-specific link.
- [ ] Loom account access (you will record a 6-min Tier 2/3 walkthrough in Phase 3).

---

## Phase 1: Beehiiv Setup (45 min)

### 1.1 Confirm pub config

- [ ] Category Gravity pub exists and is in pre-launch state. Welcome email default OFF (we use automation, not pub-level welcome).
- [ ] Default sender: `phil@petrichorgrowth.com`
- [ ] Default reply-to: `phil@petrichorgrowth.com`
- [ ] Footer includes: "Petrichor Projects · petrichorgrowth.com"

### 1.2 Add 9 custom fields

Navigate: Settings → Subscriber Fields → Add Field

| Field name | Type | Notes |
|---|---|---|
| `first_name` | Text | Used in all drip subject lines + greetings |
| `q1` | Text | Raw Q1 answer (debugging) |
| `q2` | Text | Raw Q2 answer |
| `q3` | Text | Raw Q3 answer |
| `q4` | Text | Raw Q4 answer |
| `q5` | Text | Raw Q5 answer |
| `score` | Number | 0–15 composite |
| `tier` | Text | `tier-0` / `tier-1` / `tier-2` / `tier-3` |
| `quiz_slug` | Text | `relevancy-audit` / `revenue-story-audit` / `competitive-narrative-stress-test` / `pricing-authority-diagnostic` / `investor-story-forensics` |
| `series` | Text | Always `resilience-stack` (forward-compat for Series 02) |
| `last_quiz_taken_at` | Date | ISO timestamp |

### 1.3 Create tag taxonomy

Navigate: Settings → Tags → Create Tags

Create these 31 tags (will be applied by Zapier):

**Series tag (1):**
- `series-resilience-stack`

**Quiz tags (5):**
- `quiz-relevancy-audit`
- `quiz-revenue-story-audit`
- `quiz-competitive-narrative-stress-test`
- `quiz-pricing-authority-diagnostic`
- `quiz-investor-story-forensics`

**Tier tags (4):**
- `tier-0`
- `tier-1`
- `tier-2`
- `tier-3`

**Taken tags (20) — these are the drip triggers:**
- `taken-relevancy-audit-tier-0` / `-tier-1` / `-tier-2` / `-tier-3`
- `taken-revenue-story-audit-tier-0` / `-tier-1` / `-tier-2` / `-tier-3`
- `taken-competitive-narrative-stress-test-tier-0` / `-tier-1` / `-tier-2` / `-tier-3`
- `taken-pricing-authority-diagnostic-tier-0` / `-tier-1` / `-tier-2` / `-tier-3`
- `taken-investor-story-forensics-tier-0` / `-tier-1` / `-tier-2` / `-tier-3`

### 1.4 Build 20 drip automations

Navigate: Automations → Create New Automation

For each of the 20 `taken-*` tags, create one automation:

**Trigger:** Tag added → `taken-<slug>-tier-<n>`

**Steps:**
1. Send welcome email (tier-conditional section from `marketing/beehiiv/<slug>/welcome.md`) — immediate
2. Wait 2 days
3. Send Email 1 from `marketing/beehiiv/<slug>/drips/tier-<n>.md` (Email 1 — Day 2 block)
4. Wait 2 days
5. Send Email 2 (Day 4 block)
6. Wait 3 days
7. Send Email 3 (Day 7 block)
8. Wait 3 days
9. Send Email 4 (Day 10 block)
10. Wait 4 days
11. Send Email 5 (Day 14 block)

Naming convention: `RS-<slug>-tier-<n>` (e.g. `RS-relevancy-audit-tier-2`).

**Time-saver:** Build one automation end-to-end, duplicate 19 times, swap content + trigger tag. Each duplicate takes ~3 min once template exists.

---

## Phase 2: Zapier Setup (60 min)

### 2.1 Connect accounts

- [ ] Tally → Zapier (OAuth, one-time)
- [ ] Beehiiv → Zapier (API key — paste the key from Phase 1.1 pre-flight)

### 2.2 Build the master Zap (one Zap, replicate 4 times)

**Zap name:** `RS — Relevancy Audit → Beehiiv`

**Step 1 — Trigger:** Tally → New Submission
- Form: Relevancy Audit (https://tally.so/r/aQe6A9)
- Test: submit once to populate fields

**Step 2 — Formatter (Numbers):** Convert each Q answer to point value
- Use Formatter → Utilities → Lookup Table
- Build one lookup per Q (Q1 has 4 possible answers each mapping to 0/1/2/3 pts)
- See per-quiz scoring rubric in `marketing/quizzes/<slug>.md` §"Scoring Rubric"

**Step 3 — Formatter (Math):** Sum the 5 point values
- Operation: Add
- Inputs: Q1pts + Q2pts + Q3pts + Q4pts + Q5pts
- Output stored as `score`

**Step 4 — Code (JavaScript):** Map score → tier

```javascript
const score = Number(inputData.score);
let tier;
if (score <= 3) {
  tier = 'tier-0';
} else if (score <= 7) {
  tier = 'tier-1';
} else if (score <= 11) {
  tier = 'tier-2';
} else {
  tier = 'tier-3';
}
return {
  tier: tier,
  score: score,
  quiz_slug: 'relevancy-audit',
  series: 'resilience-stack',
  taken_tag: `taken-relevancy-audit-${tier}`,
  last_quiz_taken_at: new Date().toISOString()
};
```

Input data mapping: `score` = output from Step 3 Math.

**Step 5 — Beehiiv: Create Subscription**
- Email: from Tally Step 1
- First name: from Tally Step 1
- Custom fields: map all 9 (q1-q5 from Step 1, score/tier/quiz_slug/series/last_quiz_taken_at from Step 4)
- Tags to apply (comma-separated):
  - `series-resilience-stack`
  - `quiz-relevancy-audit`
  - `{{Step 4: tier}}` (resolves to `tier-0`/1/2/3)
  - `{{Step 4: taken_tag}}` (resolves to `taken-relevancy-audit-tier-X`)
- Reactivate if unsubscribed: NO
- Send welcome email: NO (handled by automation in Phase 1.4)

**Step 6 (optional) — Slack notify on Tier 3:**
- Filter: only continue if `tier` = `tier-3`
- Slack DM to Phil: "Tier 3 submission on Relevancy Audit — {{first_name}} {{email}}. 48h SLA started."

### 2.3 Replicate for other 4 quizzes

Duplicate the Zap 4 times. For each duplicate:
- [ ] Change Step 1 trigger form
- [ ] Update Step 2 lookup tables (different answer wording per quiz)
- [ ] Update Step 4 code: change `quiz_slug` string + `taken_tag` template
- [ ] Update Step 5 tags: change `quiz-<slug>` tag

**Tally URLs reference:**
| Quiz | Tally URL |
|---|---|
| relevancy-audit | https://tally.so/r/aQe6A9 |
| revenue-story-audit | https://tally.so/r/aQAkJE |
| competitive-narrative-stress-test | https://tally.so/r/jaJg86 |
| pricing-authority-diagnostic | https://tally.so/r/1ANOQL |
| investor-story-forensics | https://tally.so/r/ob5gjM |

### 2.4 Turn on all 5 Zaps

- [ ] Each Zap toggled ON
- [ ] Each Zap shows "0 errors" on Zap History dashboard

---

## Phase 3: Loom + Calendly placeholder replacement (45 min)

### 3.1 Record Loom (15 min record + 5 min trim)

**Script outline (6 min target):**

- **0:00–0:30** — Open. "If you came back Tier 2 or Tier 3 on the [quiz name], this is the walkthrough I promised."
- **0:30–1:30** — The diagnostic vocabulary. Walk one Helix-class case from the kit (use whichever is most universal — pricing-authority Helix is the cleanest because the numbers are most visceral).
- **1:30–3:00** — The layered diagnostic. Discipline / value-metric / rev-rec layers (or the equivalent for whichever kit you walk). Why the leading layer is rarely what the team thinks it is.
- **3:00–4:30** — The reconstruction. Internal-Effective vs External-List. Options A/B/C. What the leadership conversations actually feel like.
- **4:30–5:30** — The artifact. Show the actual deliverable shape — price map, reconciliation plan, discipline document. Three pages each.
- **5:30–6:00** — Close. "If after this you think the kit alone is enough, run it yourself — that's the deal. If you want the engagement, calendar's in the email."

**Recording setup:**
- Loom standalone app, camera bubble in lower-right
- Screen share: one tab open to the kit on GitHub + one tab to a sample scorecard
- Mic: external if available, MacBook mic if not (test playback first)
- One take. Do not over-rehearse.

**Output:**
- Upload to Loom workspace
- Get share URL (format: `loom.com/share/<hash>`)
- Set visibility: "Anyone with link can view"

### 3.2 Replace placeholders across drips + welcome emails

Run this from repo root after Loom URL + Calendly URL are confirmed:

```bash
cd ~/Downloads/Projects/resilience-stack

# Replace Loom placeholder
LOOM_URL="https://loom.com/share/REPLACE_ME"
find marketing/beehiiv -name "*.md" -exec sed -i '' "s|{{loom-url}}|${LOOM_URL}|g" {} +

# Replace Calendly placeholder
CALENDLY_URL="https://calendly.com/petrichor/resilience-stack-triage"
find marketing/beehiiv -name "*.md" -exec sed -i '' "s|{{calendly-url}}|${CALENDLY_URL}|g" {} +

# Verify zero remaining placeholders
grep -r "{{loom-url\|{{calendly-url" marketing/beehiiv/ && echo "FAIL: placeholders remain" || echo "OK: all replaced"
```

### 3.3 Copy drip content into Beehiiv automation emails

For each of the 20 automation emails:
- [ ] Copy email body from `marketing/beehiiv/<slug>/drips/tier-<n>.md` (the matching Email N block)
- [ ] Paste into Beehiiv automation step editor
- [ ] Set subject line (from the `**Subject:**` line in the markdown)
- [ ] Set preview text (from the `**Preview:**` line in the markdown)
- [ ] Send test to your own inbox — verify rendering on desktop + iOS Mail

**Time-saver:** Beehiiv supports markdown paste. Most formatting will preserve. Manual cleanup on bold/italic/links only.

---

## Phase 4: Test Plan (45 min)

### 4.1 End-to-end smoke test per quiz

For each of the 5 quizzes:

- [ ] Submit form with deliberately Tier 0 answers (all 0pts) — verify lands at tier-0
- [ ] Submit form with deliberately Tier 3 answers (all 3pts = 15) — verify lands at tier-3
- [ ] Submit one boundary case (score 7 → tier-1, score 8 → tier-2) — verify boundary math

**Per submission verify:**
- Zap History shows green success
- Beehiiv subscriber created with all custom fields populated
- All expected tags applied (series + quiz + tier + taken)
- Welcome email arrives within 60 seconds
- Day-2 email scheduled (visible on subscriber's automation timeline)

### 4.2 Tier 3 SLA confirmation

- [ ] Submit Tier 3 on one quiz with your own email
- [ ] Confirm Slack notification fires (if Step 6 enabled)
- [ ] Manually reply within 48h to validate the SLA pipeline (this is the live commitment in every Tier 3 drip)

### 4.3 Cross-quiz cross-pollination test

- [ ] Take quiz A → land at tier-1
- [ ] Same email takes quiz B → land at tier-2
- [ ] Verify Beehiiv subscriber now has BOTH drip arcs firing (tags are additive — `taken-A-tier-1` AND `taken-B-tier-2`)
- [ ] Verify subscriber receives both arcs on their respective Day-2/4/7/10/14 cadences

### 4.4 Re-take protection

- [ ] Same email re-takes quiz A → land at same tier-1
- [ ] Verify `taken-A-tier-1` tag does NOT re-fire the drip (Beehiiv automations are tag-add-triggered and only fire once per subscriber per tag by default — confirm in automation settings)

---

## Phase 5: Soft-launch (30 min)

### 5.1 Internal share

- [ ] Send `outputs/resilience-stack-jana-email.md` to Jana
- [ ] Forward to one operator you trust who fits one of the diagnostics (Tier 1 or 2 ideal — they get real signal AND see the drip in action)
- [ ] Do NOT post to LinkedIn, X, or paid promo yet

### 5.2 Watch first 10 organic submissions

For each:
- [ ] Tier assignment correct? (Spot-check 3 of 10 against the raw answers)
- [ ] Drip arrived on schedule?
- [ ] Any Tier 3 submissions get 48h response?
- [ ] Any complaint, confusion, or unsubscribe in the first 14 days?

### 5.3 Adjust if needed

Common failure modes to watch for:
- Boundary misroutes (score 7 vs 8) — check Zap Step 4 logic
- Tally answer wording change → Step 2 lookup breaks — re-run Zap
- Beehiiv tag typo → drip never fires — audit tag spelling exactly
- Drip subject line lands in promotions tab → adjust sender warm-up cadence

### 5.4 Green-light for paid promo

Once all 4.x tests pass + first 10 organic submissions look clean:

- [ ] LinkedIn post (Phil personal) linking to /resilience-stack
- [ ] Category Gravity launch email to existing subscribers
- [ ] X thread
- [ ] Paid amplification (if budget): LinkedIn Ads to founder ICP, $500 test budget

---

## Reference: file map

| Artifact | Path |
|---|---|
| This packet | `marketing/beehiiv/LAUNCH-EXECUTION-PACKET.md` |
| Tally → Beehiiv mapping spec | `marketing/beehiiv/TALLY-BEEHIIV-MAPPING.md` |
| Welcome emails (5) | `marketing/beehiiv/<slug>/welcome.md` |
| Drip emails (100, 20 per quiz) | `marketing/beehiiv/<slug>/drips/tier-{0,1,2,3}.md` |
| Quiz specs (5) | `marketing/quizzes/<slug>.md` |
| Landing page | Petrichor repo: `client/src/pages/ResilienceStack.tsx` |
| Jana email | Petrichor repo: `outputs/resilience-stack-jana-email.md` |

---

## Reference: scoring math sanity check

Each quiz: 5 questions × 0–3 points = 0–15 score range.

| Score | Tier |
|---|---|
| 0–3 | Tier 0 — Holding / Defensible |
| 4–7 | Tier 1 — Eroding / Vulnerable |
| 8–11 | Tier 2 — Compromised / Cracking |
| 12–15 | Tier 3 — Collapsed |

The Step 4 JS implements exactly this. Boundary tests in Phase 4.1 verify.

---

*Resilience Stack · Category Gravity Series 01 · Launch packet · Petrichor Projects*
