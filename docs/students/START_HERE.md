# Student Start Here

1. Create your team folder: `docs/students/teams/<team-name>`
2. Keep meeting notes, decisions, and links to artifacts there.
3. Use the templates in `docs/deliverables/`.
4. When a deliverable hits the acceptance criteria, **trigger the matching objective**.

## Triggering an Objective
- Edit `EvaluationLabels.json` and set e.g. `"O3": true`, add your evidence URL to the commit message.
- Or run `scripts/trigger_objective.sh O3 "https://link-to-evidence"`

This will create a **receipt** under `receipts/` via GitHub Actions.
