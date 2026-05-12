# Skill Stack Launch Checklist

Reusable pre-launch checklist for any curated skill / framework / template stack (awesome-list pattern, Claude skill pack, GPT pack, MCP server collection, etc).

Work top-to-bottom. Don't scaffold the repo until §1-§5 are answered.

---

## §1 — Strategy

- [ ] **Problem statement**: One sentence on what this stack solves that no existing curated list covers.
  > _Answer:_
- [ ] **ICP (buyer/user)**: Specific role + company stage. Not "everyone."
  > _Answer:_
- [ ] **Outcome promise**: Concrete deliverable the user walks away with (revenue, decisions, artifacts, status, learning).
  > _Answer:_
- [ ] **One-sentence "why this exists"** that survives a 10-second skim.
  > _Answer:_

---

## §2 — Packaging Vector

- [ ] **Monetization model** (pick one or stack):
  - [ ] Free + reputation play
  - [ ] Free OSS + paid Pro (rubrics, templates, slides, runner)
  - [ ] Paid per skill (Gumroad / marketplace)
  - [ ] Productized service ($k+)
  - [ ] Hybrid (describe split):
        > _Notes:_
- [ ] **Free/paid gate location** — if hybrid, where is the line?
  > _Answer:_
- [ ] **Funnel use** — does the free stack drive a paid service?
  - [ ] Yes (describe upsell path):
  - [ ] No

---

## §3 — Branding

- [ ] **Brand stance**:
  - [ ] Forward (logo + name dominant)
  - [ ] Subtle (footer + author credit only)
  - [ ] Stealth (no brand)
- [ ] **Name candidates** (list 3-5):
  > _Candidates:_
- [ ] **Naming style chosen**:
  - [ ] Descriptive (SEO-friendly, generic)
  - [ ] Abstract / rare word (ownable, needs explanation)
  - [ ] Metaphor (memorable, brand-native)
- [ ] **Tone**:
  - [ ] Positive / aspirational
  - [ ] Problem-framed / urgent
- [ ] **Tagline** — one sentence, read aloud, must survive an elevator pitch.
  > _Tagline:_
- [ ] **Name availability check**:
  - [ ] GitHub org/repo free
  - [ ] npm / PyPI / package registry free
  - [ ] Domain free (optional)
  - [ ] Trademark conflict check (USPTO TESS, EUIPO)

---

## §4 — License

- [ ] **Commercial use allowed?**
  - [ ] Yes
  - [ ] No (warning: kills consultant/agency adoption)
- [ ] **Attribution mandatory?**
  - [ ] Yes
  - [ ] No
- [ ] **Mixed code + content?**
  - [ ] Yes — dual license (code: MIT or Apache-2.0 / content: CC BY 4.0)
  - [ ] No — single license
- [ ] **License selected**:
  - [ ] MIT
  - [ ] Apache 2.0
  - [ ] CC BY 4.0
  - [ ] CC BY-SA 4.0
  - [ ] CC BY-NC 4.0 (only if blocking commercial use)
  - [ ] Other:
- [ ] **Trademark filing** (optional, ~$350 USPTO, ~12 months):
  - [ ] Filing
  - [ ] Skipping
- [ ] **LICENSE file written + linked from README**

---

## §5 — Contributions

- [ ] **Contribution model**:
  - [ ] Open (anyone PRs)
  - [ ] Curated (maintainer-only)
  - [ ] Hybrid (open w/ validator + maintainer veto) ← recommended
- [ ] **Rejection bar written down** (paste into CONTRIBUTING.md):
  - [ ] Required frontmatter fields
  - [ ] Required sections
  - [ ] Min / max length
  - [ ] Required output / deliverable type
  - [ ] Required stance / quality marker (e.g., "adversarial," "evidence-required")
- [ ] **Sign-off mechanism**:
  - [ ] CLA (formal, friction)
  - [ ] DCO (commit sign-off)
  - [ ] Implicit (PR = agreement via license text)
- [ ] **Review SLA**:
  > _Answer:_ ___ days
- [ ] **Out-of-scope contributions listed explicitly** in CONTRIBUTING.md

---

## §6 — Hosting + Security

- [ ] **Source-of-truth host**:
  - [ ] GitHub
  - [ ] GitLab
  - [ ] Codeberg
  - [ ] Other:
- [ ] **Distribution channels** (pick all):
  - [ ] GitHub releases / clone
  - [ ] npm
  - [ ] PyPI
  - [ ] Homebrew tap
  - [ ] Marketplace mirror (MyClaude, OpenAI GPT store, etc.)
  - [ ] curl bash one-liner installer
- [ ] **Hosted runner?**
  - [ ] No → users run locally w/ own keys ← zero key risk
  - [ ] Yes → flag for API-key risk, rate limiting, abuse handling, billing
- [ ] **Runtime credentials needed?**
  - [ ] No
  - [ ] Yes — document required env vars, never commit secrets
- [ ] **Security hygiene**:
  - [ ] `.gitignore` blocks `.env*`, `*.key`, `credentials*`, `secrets*`
  - [ ] GitHub Secret Scanning enabled
  - [ ] No secrets in commit history (run `git log -p | grep -iE "key|secret|token"` once)
  - [ ] Dependencies pinned (if any code shipped)
  - [ ] npm package signed w/ provenance (if publishing to npm)

---

## §7 — Scope + Robustness

- [ ] **Launch entry count** (honest):
  > _Answer:_ ___ entries
- [ ] **Positioning matches count**?
  - [ ] "Curated" → 10-25 ← works
  - [ ] "Awesome" → needs 50-100+
  - [ ] "Comprehensive" → needs 200+
- [ ] **v1.5 expansion roadmap written**:
  > _Answer:_
- [ ] **v1 scope locked** — what ships now vs deferred:
  > _v1:_
  > _v1.5+:_

---

## §8 — Tech / Format

- [ ] **Skill / entry format**:
  - [ ] Markdown
  - [ ] JSON
  - [ ] YAML
  - [ ] TypeScript / JS
  - [ ] Python
  - [ ] Mixed
- [ ] **Required frontmatter fields** listed (name, description, version, author, license, tags, etc.):
  > _Fields:_
- [ ] **Required sections** listed (Persona, Protocol, Deliverables, Rules, etc.):
  > _Sections:_
- [ ] **Installer pattern selected**:
  - [ ] `git clone`
  - [ ] `npx <package>`
  - [ ] `curl ... | bash`
  - [ ] Package manager (`brew install`, etc.)
  - [ ] Marketplace-only
- [ ] **Validation tooling**:
  - [ ] GitHub Action validates PRs
  - [ ] Lint rules documented
  - [ ] Test runner (if entries are executable)

---

## §9 — Repo Scaffold (build checklist)

- [ ] `README.md` — branded intro, install, full index, license, contribution hook, "why this exists"
- [ ] `LICENSE` — full license text
- [ ] `CONTRIBUTING.md` — spec template, rejection bar, PR process, license agreement, out-of-scope
- [ ] `CODE_OF_CONDUCT.md` — Contributor Covenant (or equivalent)
- [ ] `CONTRIBUTORS.md` — credit ledger
- [ ] `.gitignore` — secrets + build artifacts blocked
- [ ] `.github/PULL_REQUEST_TEMPLATE.md` — self-checklist for PR authors
- [ ] `.github/workflows/validate-*.yml` — auto-validate PRs
- [ ] `bin/<cli>.js` or installer script (if shipping installer)
- [ ] `install.sh` — curl one-liner installer (if applicable)
- [ ] `package.json` / `pyproject.toml` / etc. — package metadata
- [ ] `docs/` — methodology, roadmap, FAQ
- [ ] Entries organized into folders by track / category

---

## §10 — Launch

- [ ] **Launch channels selected** (rank top 3):
  - [ ] Hacker News (Show HN)
  - [ ] X / Twitter
  - [ ] LinkedIn
  - [ ] Reddit (which subs?)
  - [ ] Product Hunt
  - [ ] Newsletter
  - [ ] Direct outreach
  - [ ] Cross-post to relevant Discord / Slack communities
- [ ] **Launch order + timing** mapped (which first, 24h follow-up plan):
  > _Sequence:_
- [ ] **Pre-launch ask list** — friendlies tagged for amplification:
  > _Names:_
- [ ] **Launch copy drafted**:
  - [ ] Show HN title + body
  - [ ] X thread (1 entry per post or 1 megapost)
  - [ ] LinkedIn carousel or long-form
  - [ ] Newsletter blast (if applicable)
- [ ] **Success metric for 30 days**:
  > _Metric:_ ___ stars / installs / signups / leads
- [ ] **Failure threshold + pivot plan** (when to re-position vs walk away):
  > _Trigger:_
- [ ] **Repo discoverability set up**:
  - [ ] Repo description filled
  - [ ] Topics added (5-10 tags)
  - [ ] Social preview image uploaded
  - [ ] Pinned to GitHub profile / org
  - [ ] Badges in README (license, stars, version)

---

## §11 — Governance + Long-Term

- [ ] **Maintainer count**:
  > _Answer:_
- [ ] **Bus factor mitigation** — co-maintainer or backup named:
  > _Answer:_
- [ ] **Versioning approach**:
  - [ ] Semver
  - [ ] Calendar versioning
  - [ ] "main is stable"
- [ ] **Breaking-change policy** documented:
  > _Answer:_
- [ ] **Sunset / transfer plan** (when to archive, transfer ownership, fork):
  > _Answer:_

---

## §12 — Quick-Fill 10 (for rapid scaffolding)

If short on time, answer these 10 only — they unlock the scaffold:

1. **Buyer**:
2. **Outcome**:
3. **Monetization**:
4. **Brand stance**:
5. **Name + tagline**:
6. **License**:
7. **Contributions** (open / curated / hybrid):
8. **Host + runner?** (local-only / hosted):
9. **Launch count + v1.5 plan**:
10. **Launch channel order**:

---

## Sign-Off

- [ ] §1-§5 answered → ready to scaffold
- [ ] §6-§9 complete → ready to commit + push
- [ ] §10 complete → ready to launch
- [ ] §11 complete → ready to sustain

**Date completed**: ______
**Stack name**: ______
**Owner**: ______

---

*Template version: 1.0 — based on Resilience Stack launch (Petrichor Projects, 2026). CC BY 4.0.*
