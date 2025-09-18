#!/usr/bin/env bash
set -euo pipefail
OBJ="${1:?usage: trigger_objective.sh O# <evidence-url> [message]}"
EVID="${2:-}"
MSG="${3:-trigger $OBJ}"
python3 - <<PY
import json,sys,datetime
path="EvaluationLabels.json"
data=json.load(open(path))
obj=sys.argv[1]
if obj not in data: data[obj]=False
data[obj]=True
data["updated_at"]=datetime.datetime.utcnow().isoformat()+"Z"
json.dump(data, open(path,"w"), indent=2)
print("Updated", obj)
PY "$OBJ"
git add EvaluationLabels.json
if [ -n "$EVID" ]; then MSG="$MSG | evidence: $EVID"; fi
git commit -m "$MSG"
echo "Commit created. Push your branch to open a PR."
