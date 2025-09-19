#!/usr/bin/env bash
set -euo pipefail

# Sponsor Acknowledgement Script for Perception-Locked Consensus
OBJ="${1:?usage: sponsor_acknowledge.sh O# [sponsor_id]}"
SPONSOR_ID="${2:-Sponsor}"

echo "=== Sponsor Acknowledgement (Perception-Locked Consensus) ==="
echo "Objective: $OBJ"
echo "Sponsor: $SPONSOR_ID"
echo

# Add sponsor signature for perception-locked consensus
echo "Adding sponsor signature for perception-locked consensus..."
python3 scripts/token_manager.py acknowledge "$OBJ" "$SPONSOR_ID"

if [ $? -ne 0 ]; then
    echo "Error: Acknowledgement failed"
    exit 1
fi

# Record state transition
git add EvaluationLabels.json
git commit -m "Sponsor acknowledgement: $OBJ | perception_locked: true | signatory: $SPONSOR_ID"

echo
echo "✓ Sponsor signature recorded"
echo "✓ Perception-locked consensus achieved"
echo "✓ State transition logged"

# Check if consensus is complete
echo
echo "Checking consensus status..."
python3 scripts/token_manager.py status

# Show next steps
echo
echo "=== Next Steps ==="
echo "Complete objective: python3 scripts/token_manager.py complete $OBJ"