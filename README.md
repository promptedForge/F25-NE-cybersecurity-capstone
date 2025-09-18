# Prompted Forge — F25 NE Cybersecurity Capstone

Welcome. This repo is the **student + faculty** workspace for the Prompted Forge–sponsored capstone.
It is public by design and excludes enterprise-only methods. The workflow is **student-triggered** — your
execution flips objective receipts; faculty can observe and comment; sponsors review asynchronously.

---

## TL;DR — How to Use This Repo
1. **Start here:** `docs/00_WELCOME.md` (5‑minute overview).
2. **Read student guide:** `docs/students/START_HERE.md`.
3. **Clone the repo** and create your team folder under `docs/students/teams/<team-name>`.
4. **Deliverables** are listed in `docs/students/DELIVERABLES.md` with templates under `docs/deliverables/`.
5. **Trigger objectives** by updating `EvaluationLabels.json` (or run `scripts/trigger_objective.sh O3 "evidence link"`).
6. A GitHub Action writes a **receipt** to `receipts/` — think of it as a public hash of your state change.
7. Sponsors review receipts & artifacts; faculty can see everything and comment anytime.

> NDA or private material is referenced as **“where applicable”** and handled outside this public repo.

---

## Roles
- **Students (you):** build, document, and trigger objectives. Keep logs and evidence links in your team folder.
- **Sponsors (Prompted Forge):** review objective receipts + artifacts; approve or request changes.
- **Faculty:** observe progress, provide academic validation, and final grading per course policy.

---

## Smart‑Contract (Public Simulation)
The real contract mechanics live in the sponsor’s enterprise systems. Here, when you trigger an objective:
- A GitHub Action creates a **signed receipt file** with a timestamp + content hash in `receipts/`.
- The receipt links to your PR/commit and the evidence URLs you provided.
- This gives a tamper‑evident audit trail the faculty can inspect in real time.

Details: `.github/workflows/contract-receipt.yml`

---

## Quick Links
- Welcome: `docs/00_WELCOME.md`
- Students: `docs/students/START_HERE.md`
- Deliverables list: `docs/students/DELIVERABLES.md`
- Faculty landing: `docs/faculty/00_FACULTY_START.md`
- Trigger objective helper: `scripts/trigger_objective.sh`
