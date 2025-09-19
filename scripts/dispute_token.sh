#!/usr/bin/env bash
set -euo pipefail

# Token Dispute Resolution Script
OBJ="${1:?usage: dispute_token.sh <objective> <rationale> [signatory]}"
RATIONALE="${2:?rationale required}"
SIGNATORY="${3:-Professor}"

echo "=== Token Dispute Resolution ==="
echo "Objective: $OBJ"
echo "Rationale: $RATIONALE"
echo "Initiated by: $SIGNATORY"
echo

# Confirm dispute action
echo "⚠️  WARNING: This will revert the token status to false and log a dispute."
echo "Are you sure you want to proceed? (y/N)"
read -r confirm

if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
    echo "Dispute cancelled."
    exit 0
fi

# Revert token and log dispute
echo "Reverting token and logging dispute..."
python3 scripts/token_manager.py revert "$OBJ" "$RATIONALE" "$SIGNATORY"

if [ $? -ne 0 ]; then
    echo "Error: Failed to process dispute"
    exit 1
fi

# Commit the changes
git add EvaluationLabels.json
git commit -m "Token dispute: $OBJ | rationale: $RATIONALE | initiated_by: $SIGNATORY"

echo
echo "✓ Token $OBJ reverted to Status=false"
echo "✓ Dispute logged in commit history"
echo "✓ Escrow state changed to 'disputed'"

# Show dispute status
echo
echo "=== Dispute Status ==="
python3 scripts/token_manager.py status

echo
echo "=== Resolution Process ==="
echo "1. Address the dispute rationale"
echo "2. Provide new evidence if needed"
echo "3. Re-trigger objective with updated evidence"
echo "4. Obtain consensus from all signatories"