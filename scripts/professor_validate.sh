#!/usr/bin/env bash
set -euo pipefail

# Professor Validation Script with Epistemic Lock
OBJ="${1:?usage: professor_validate.sh O# [professor_id]}"
PROF_ID="${2:-Professor}"

echo "=== Professor Validation (Epistemic Lock) ==="
echo "Objective: $OBJ"
echo "Professor: $PROF_ID"
echo

# Validate evidence and append signature
echo "Validating evidence and applying epistemic lock..."
python3 scripts/token_manager.py validate "$OBJ" "$PROF_ID"

if [ $? -ne 0 ]; then
    echo "Error: Validation failed"
    exit 1
fi

# Record state transition
git add EvaluationLabels.json
git commit -m "Professor validation: $OBJ | epistemic_lock: true | signatory: $PROF_ID"

echo
echo "✓ Epistemic lock applied"
echo "✓ Professor signature recorded"
echo "✓ State transition logged"

# Show next steps
echo
echo "=== Next Steps ==="
echo "Sponsor acknowledgement: ./scripts/sponsor_acknowledge.sh $OBJ"
echo "Complete objective: python3 scripts/token_manager.py complete $OBJ"