# Security Policy — Resilience Stack

## Reporting a Vulnerability

If you discover a security vulnerability — in the skills, the installer, the npm package, the GitHub Action, or any tooling shipped from this repository — please report it privately so we can address it before public disclosure.

**Preferred channel**: email `phil@petrichorgrowth.com` with subject `SECURITY: <short description>`.

We aim to respond within 72 hours.

## Scope

Things in scope for a security report:

- Code execution via the npm installer (`bin/resilience-stack.js`)
- Code execution via `install.sh`
- Supply chain risk in `package.json` dependencies
- Skill files that attempt to exfiltrate data, escape sandboxes, or trick the Claude runtime
- GitHub Action workflow vulnerabilities (`.github/workflows/`)
- Any credential, secret, or PII accidentally committed to the repository

Out of scope:

- Strategic disagreement with a framework — that is content, not a vulnerability
- Stylistic preferences in skill markdown
- Anything that requires the attacker to already have write access

## What Resilience Stack Does Not Do

Skills in this repository are **markdown facilitation protocols**. They:

- Run inside the user's own Claude Code or Claude Agent SDK session
- Use the user's own API key
- Write deliverables to the user's own local filesystem (`./<skill-name>-output/`)
- Do not phone home to any Petrichor-controlled endpoint
- Do not collect telemetry (an opt-in trajectory-logging specification exists in `docs/trajectory-logging-spec.md` but is not implemented in v1.5)

If you discover any of these guarantees being violated, that is a security report.

## Supported Versions

Only the latest tagged release on the `main` branch is supported for security fixes.

| Version | Supported |
|---------|-----------|
| latest tagged | yes |
| older tags | no |
| forks / derivative repos | no |

## Disclosure Coordination

If you report a vulnerability, we will:

1. Acknowledge within 72 hours
2. Confirm or refute the report within 7 days
3. Coordinate a fix and a disclosure date
4. Credit you in the release notes (unless you prefer to remain anonymous)

Thank you for helping keep Resilience Stack and its users safe.

---

*Petrichor Projects · CC BY 4.0 · https://petrichorgrowth.com*
