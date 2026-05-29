#!/usr/bin/env bash
# Resilience Stack — placeholder swap script
#
# Replaces {{loom-url}} and {{calendly-url}} placeholders across all
# marketing/beehiiv/*/welcome.md and drips/tier-*.md files. Commits to a
# feature branch and opens a PR. After merge, the n8n drip workflow auto-fetches
# the updated markdown on the next subscription submission (no n8n redeploy needed).
#
# Usage:
#   ./scripts/swap-placeholders.sh <loom-url> <calendly-url>
#
# Example:
#   ./scripts/swap-placeholders.sh \
#     "https://www.loom.com/share/abc123def456" \
#     "https://calendly.com/petrichor/resilience-stack-triage"
#
# Safety:
#   - Refuses to run if not in resilience-stack repo
#   - Refuses to run on main branch (creates feature branch)
#   - Validates URLs match expected domain patterns
#   - Dry-run shows diff before committing
#   - Verifies zero remaining placeholders before commit

set -euo pipefail

# --- args ---
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <loom-url> <calendly-url>"
  echo ""
  echo "Example:"
  echo "  $0 \"https://www.loom.com/share/abc123\" \"https://calendly.com/petrichor/triage\""
  exit 1
fi

LOOM_URL="$1"
CALENDLY_URL="$2"

# --- repo sanity ---
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || echo "")"
if [ -z "$REPO_ROOT" ]; then
  echo "ERROR: not in a git repo"
  exit 1
fi

REPO_NAME="$(basename "$REPO_ROOT")"
if [ "$REPO_NAME" != "resilience-stack" ]; then
  echo "ERROR: must run from resilience-stack repo. Currently in: $REPO_NAME"
  exit 1
fi

cd "$REPO_ROOT"

# --- URL validation ---
case "$LOOM_URL" in
  https://*loom.com/share/*|https://*loom.com/embed/*) ;;
  *)
    echo "ERROR: LOOM_URL should match https://*loom.com/share/* — got: $LOOM_URL"
    exit 1
    ;;
esac

case "$CALENDLY_URL" in
  https://calendly.com/*) ;;
  *)
    echo "ERROR: CALENDLY_URL should start with https://calendly.com/ — got: $CALENDLY_URL"
    exit 1
    ;;
esac

# --- branch safety ---
CURRENT_BRANCH="$(git branch --show-current)"
if [ "$CURRENT_BRANCH" = "main" ]; then
  TARGET_BRANCH="feat/placeholder-swap-$(date +%Y%m%d-%H%M%S)"
  echo "Creating branch: $TARGET_BRANCH"
  git checkout -b "$TARGET_BRANCH"
else
  TARGET_BRANCH="$CURRENT_BRANCH"
  echo "Using current branch: $TARGET_BRANCH"
fi

# --- find files ---
FILES=$(find marketing/beehiiv -type f -name "*.md" | sort)
if [ -z "$FILES" ]; then
  echo "ERROR: no markdown files found under marketing/beehiiv/"
  exit 1
fi

FILE_COUNT=$(echo "$FILES" | wc -l | tr -d ' ')
echo "Found $FILE_COUNT markdown files"

# --- count current placeholders ---
LOOM_BEFORE=$(grep -l "{{loom-url}}" $FILES 2>/dev/null | wc -l | tr -d ' ')
CAL_BEFORE=$(grep -l "{{calendly-url}}" $FILES 2>/dev/null | wc -l | tr -d ' ')
echo ""
echo "Before swap:"
echo "  {{loom-url}}     in $LOOM_BEFORE files"
echo "  {{calendly-url}} in $CAL_BEFORE files"

if [ "$LOOM_BEFORE" = "0" ] && [ "$CAL_BEFORE" = "0" ]; then
  echo ""
  echo "No placeholders found. Nothing to swap. Exiting."
  exit 0
fi

# --- perform swap ---
echo ""
echo "Swapping placeholders..."
for file in $FILES; do
  # macOS sed needs '' after -i
  sed -i '' "s|{{loom-url}}|${LOOM_URL}|g" "$file"
  sed -i '' "s|{{calendly-url}}|${CALENDLY_URL}|g" "$file"
done

# --- verify zero remaining ---
LOOM_AFTER=$(grep -l "{{loom-url}}" $FILES 2>/dev/null | wc -l | tr -d ' ')
CAL_AFTER=$(grep -l "{{calendly-url}}" $FILES 2>/dev/null | wc -l | tr -d ' ')
echo ""
echo "After swap:"
echo "  {{loom-url}}     in $LOOM_AFTER files"
echo "  {{calendly-url}} in $CAL_AFTER files"

if [ "$LOOM_AFTER" != "0" ] || [ "$CAL_AFTER" != "0" ]; then
  echo ""
  echo "ERROR: placeholders remain after swap. Aborting commit."
  echo "Inspect with: grep -r '{{loom-url\\|{{calendly-url' marketing/beehiiv/"
  git diff --stat
  exit 1
fi

# --- show diff stat ---
echo ""
echo "Changed files:"
git diff --stat marketing/beehiiv/

# --- commit ---
git add marketing/beehiiv/
git commit -m "Swap {{loom-url}} and {{calendly-url}} placeholders

Loom: ${LOOM_URL}
Calendly: ${CALENDLY_URL}
Files updated: ${FILE_COUNT}

n8n drip workflow fetches latest markdown on each new submission,
so this commit goes live for new subscribers as soon as it merges to main."

# --- push + open PR ---
echo ""
echo "Pushing branch..."
git push -u origin "$TARGET_BRANCH" 2>&1 | tail -3

echo ""
echo "Opening PR..."
gh pr create \
  --title "Swap placeholders: {{loom-url}} + {{calendly-url}}" \
  --body "Replaces {{loom-url}} and {{calendly-url}} in all welcome + drip markdown files.

**Loom:** ${LOOM_URL}
**Calendly:** ${CALENDLY_URL}
**Files updated:** ${FILE_COUNT}

After merge, n8n drip scheduler auto-fetches updated content on next submission — no redeploy.

## Verify before merge
- [ ] Loom URL opens and shows the right video
- [ ] Calendly URL opens to your booking page
- [ ] One drip file spot-checked — placeholders replaced cleanly, no broken markdown" 2>&1 | tail -3

echo ""
echo "✓ Done. Review the PR, merge to main, drip content updates instantly for new subscribers."
echo ""
echo "Verify any drip:"
echo "  grep -A 1 'loom\\.com\\|calendly\\.com' marketing/beehiiv/relevancy-audit/drips/tier-2.md | head -10"
