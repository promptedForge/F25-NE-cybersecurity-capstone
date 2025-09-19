#!/usr/bin/env bash
set -euo pipefail

# Enhanced Smart Contract Tokenization Trigger
OBJ="${1:?usage: trigger_objective.sh O# <evidence-url> [role] [message]}"
EVID="${2:?evidence URL required}"
ROLE="${3:-StudentTeam}"
MSG="${4:-trigger $OBJ}"

echo "=== Smart Contract Tokenization Flow ==="
echo "Objective: $OBJ"
echo "Evidence: $EVID" 
echo "Role: $ROLE"
echo

# Step 1: Deliver evidence and update token stub
echo "Step 1: Delivering evidence and updating token stub..."
python3 scripts/token_manager.py deliver "$OBJ" "$EVID" "$ROLE"

if [ $? -ne 0 ]; then
    echo "Error: Failed to deliver evidence"
    exit 1
fi

# Step 2: Check if this completes the consensus requirements
echo
echo "Step 2: Checking consensus status..."
python3 scripts/token_manager.py status

# Commit the changes
git add EvaluationLabels.json
COMMIT_MSG="$MSG | evidence: $EVID | role: $ROLE | anchor: $(python3 -c "
import json
with open('EvaluationLabels.json') as f:
    data = json.load(f)
    if '$OBJ' in data['objectives']:
        print(data['objectives']['$OBJ']['token_stub']['Anchor'])
    else:
        print('unknown')
")"

git commit -m "$COMMIT_MSG"

echo
echo "=== Next Steps ==="
echo "1. Professor validation: python3 scripts/token_manager.py validate $OBJ Professor"
echo "2. Sponsor acknowledgement: python3 scripts/token_manager.py acknowledge $OBJ Sponsor"  
echo "3. Complete objective: python3 scripts/token_manager.py complete $OBJ"
echo
echo "Commit created. Push your branch to open a PR."
