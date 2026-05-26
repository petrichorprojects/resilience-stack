# n8n Workflow Handoff — Resilience Stack Router

**Workflow URL:** https://petrichorprojects.app.n8n.cloud/workflow/irAN9HGG7Hs3uKMF
**Workflow ID:** `irAN9HGG7Hs3uKMF`
**Status:** Built + validated. NOT active yet. 4 manual steps before activation.

---

## What this replaces

The entire Phase 2 of `LAUNCH-EXECUTION-PACKET.md` (Zapier setup). One n8n workflow handles all 5 quizzes via single webhook + Tally formId routing. Zero Zapier cost.

---

## Architecture

```
[Tally form 1-5]
       ↓ POST webhook
[Webhook · Tally inbound]   /webhook/resilience-stack
       ↓
[Config]                     holds BEEHIIV_PUB_ID + SLACK_WEBHOOK_URL
       ↓
[Score + tier]               parses Tally payload, sums option indices, maps to tier
       ↓
[Beehiiv · Create subscription]   POST /v2/publications/{pubId}/subscriptions
       ↓
[Merge sub id + tier data]
       ↓
[Beehiiv · Apply tags]       POST /v2/publications/{pubId}/subscriptions/{subId}/tags
       ↓
[Is Tier 3?]
       ├─ yes → [Slack · Tier 3 alert]
       └─ no ──┐
[Respond to Tally]  200 OK
```

Webhook URL once active (production): `https://petrichorprojects.app.n8n.cloud/webhook/resilience-stack`

---

## 4 manual steps before activation

### Step 1: Create Beehiiv API credential in n8n

1. Open https://petrichorprojects.app.n8n.cloud/home/credentials
2. **New credential** → search "Header Auth" → select
3. Name: `Beehiiv API`
4. Header Name: `Authorization`
5. Header Value: `Bearer <YOUR_BEEHIIV_API_KEY>`
6. Save

Beehiiv key location: beehiiv.com → Settings → Integrations → API → Create new API key.

### Step 2: Attach credential to both Beehiiv HTTP nodes

1. Open the workflow: https://petrichorprojects.app.n8n.cloud/workflow/irAN9HGG7Hs3uKMF
2. Click `Beehiiv · Create subscription` node
3. Under **Credential to connect with** → select `Beehiiv API`
4. Repeat for `Beehiiv · Apply tags` node
5. Save workflow

### Step 3: Fill Config node placeholders

1. Click `Config` node
2. Edit `BEEHIIV_PUB_ID` → replace `REPLACE_WITH_BEEHIIV_PUB_ID` with your publication ID (format: `pub_xxxxxxxx`)
3. Edit `SLACK_WEBHOOK_URL` → either a real Slack incoming webhook URL OR leave the placeholder (Slack node has `neverError` + `onError: continueRegularOutput` so the workflow still completes)
4. Save

Pub ID location: beehiiv.com → Settings → Publications → URL bar shows `/publications/pub_xxxxxxxx`.

Slack webhook setup (optional): api.slack.com/apps → your app → Incoming Webhooks → Add New Webhook → pick channel → copy URL.

### Step 4: Activate workflow

1. Top right of workflow editor → toggle **Inactive → Active**
2. Webhook URL becomes live: `https://petrichorprojects.app.n8n.cloud/webhook/resilience-stack`

---

## Wire up Tally (5 forms, ~3 min each)

For each of the 5 Tally forms, add a webhook integration:

1. Open Tally form (links below)
2. **Integrations** tab → **Webhooks** → **Connect**
3. Endpoint URL: `https://petrichorprojects.app.n8n.cloud/webhook/resilience-stack`
4. Method: POST
5. Signing secret: leave blank (workflow doesn't verify yet — add later if needed)
6. Connect

**Tally form URLs:**
| Quiz | Tally URL |
|---|---|
| Relevancy Audit | https://tally.so/forms/aQe6A9/edit |
| Revenue Story Audit | https://tally.so/forms/aQAkJE/edit |
| Competitive Narrative Stress Test | https://tally.so/forms/jaJg86/edit |
| Pricing Authority Diagnostic | https://tally.so/forms/1ANOQL/edit |
| Investor Story Forensics | https://tally.so/forms/ob5gjM/edit |

---

## Critical Tally requirement: option order

The Score + tier Code node scores **by option index** (position in the options list), not by parsing answer text.

**Requirement:** every multiple-choice question must have options ordered **0pts first → 3pts last**.

Quiz spec confirms all 25 questions use this order (the points are visible in `marketing/quizzes/<slug>.md`). If you ever edit a Tally form, keep options in the same order or scoring breaks silently.

**Verification:** open each Tally form, click each question, confirm option list reads top-down as the spec's 0pt/1pt/2pt/3pt order.

---

## Smoke test (do this before sharing the URL with Jana)

1. Open Relevancy Audit form: https://tally.so/r/aQe6A9
2. Fill with deliberate Tier 0 answers (always pick the first option = 0pts each, total = 0)
3. Submit
4. Check n8n executions: https://petrichorprojects.app.n8n.cloud/workflow/irAN9HGG7Hs3uKMF/executions
5. Expect green run, `tier: tier-0`, `quiz_slug: relevancy-audit`
6. Check Beehiiv subscriber list → confirm new subscriber w/ tags: `series-resilience-stack`, `quiz-relevancy-audit`, `tier-0`, `taken-relevancy-audit-tier-0`
7. Repeat with all-last-option (= 15pts) → expect `tier-3` + Slack notification (if Slack URL filled)
8. Repeat for one boundary: score 7 should land tier-1, score 8 should land tier-2

---

## Failure mode reference

| Symptom | Cause | Fix |
|---|---|---|
| Workflow runs but Beehiiv create returns 401 | Beehiiv credential wrong or not attached | Step 1+2 above |
| Workflow runs but Beehiiv create returns 404 | Pub ID wrong | Step 3 above |
| Code node throws `Unknown formId` | Tally form ID not in FORM_TO_QUIZ map | Edit Score+tier node, add formId to map |
| Code node throws `No email field found` | Tally form missing email INPUT_EMAIL field | Audit Tally form, ensure email field present |
| All scores come back wrong | Tally option order doesn't match spec | Audit each form's option order, fix order |
| Tier 3 fires but no Slack message | SLACK_WEBHOOK_URL is placeholder | Step 3 — fill real URL |
| Tally webhook fails with 500 | Workflow inactive | Step 4 — activate |

---

## What I cannot do for you

- Generate Beehiiv API key (Beehiiv requires you to be logged in)
- Find Beehiiv pub ID (only visible in your Beehiiv account)
- Create Slack incoming webhook (requires your Slack workspace admin)
- Attach credential to nodes (n8n API does not expose credential UUID — must be done in UI)
- Activate Tally webhooks (Tally API does not currently support webhook config via API)

Everything else: built.

---

## Reference: workflow JSON

Stored in n8n. Export via:
```bash
# n8n UI: workflow → ⋮ menu → Download
# Or via API:
curl https://petrichorprojects.app.n8n.cloud/api/v1/workflows/irAN9HGG7Hs3uKMF \
  -H "X-N8N-API-KEY: <your-key>" > workflow.json
```

---

*Resilience Stack · Category Gravity Series 01 · n8n handoff · Petrichor Projects*
