#!/usr/bin/env bash
set -euo pipefail

# Stretch Objective Token Minting Script
BASE_OBJ="${1:?usage: stretch_objective.sh <base_objective> <stretch_id> <evidence_url>}"
STRETCH_ID="${2:?stretch ID required (e.g., XX, A1, etc.)}"
EVID="${3:?evidence URL required}"

echo "=== Stretch Objective Token Minting ==="
echo "Base Objective: $BASE_OBJ"
echo "Stretch ID: $STRETCH_ID"
echo "Evidence: $EVID"
echo

# Validate base objective
if [ "$BASE_OBJ" != "O10" ]; then
    echo "Error: Stretch objectives are only supported for O10"
    exit 1
fi

# Mint stretch token
echo "Minting stretch token: ${BASE_OBJ}-${STRETCH_ID}..."
python3 scripts/token_manager.py stretch "$BASE_OBJ" "$STRETCH_ID" "$EVID"

if [ $? -ne 0 ]; then
    echo "Error: Failed to mint stretch token"
    exit 1
fi

# Commit the changes
git add EvaluationLabels.json
git commit -m "Stretch token minted: ${BASE_OBJ}-${STRETCH_ID} | evidence: $EVID | anchor: Stretch_Anchor_${BASE_OBJ}-${STRETCH_ID}"

echo
echo "✓ Stretch token ${BASE_OBJ}-${STRETCH_ID} minted successfully"
echo "✓ Anchor: Stretch_Anchor_${BASE_OBJ}-${STRETCH_ID}"
echo "✓ State transition recorded"

# Show next steps
echo
echo "=== Next Steps ==="
echo "1. Deliver evidence: ./scripts/trigger_objective.sh ${BASE_OBJ}-${STRETCH_ID} $EVID StudentTeam"
echo "2. Professor validation: ./scripts/professor_validate.sh ${BASE_OBJ}-${STRETCH_ID}"
echo "3. Sponsor acknowledgement: ./scripts/sponsor_acknowledge.sh ${BASE_OBJ}-${STRETCH_ID}"

# Display current status
echo
python3 scripts/token_manager.py status