# Prompted Forge — F25 NE Cybersecurity Capstone

Welcome. This repo is the **student + faculty** workspace for the Prompted Forge–sponsored capstone.
It is public by design and excludes enterprise-only methods. The workflow is **student-triggered** — your
execution flips objective receipts; faculty can observe and comment; sponsors review asynchronously.

---
## Visualize the capstone mgmt:

```mermaid
```mermaid
sequenceDiagram
    participant Student
    participant Group_Contract
    participant Professor
    participant Sponsor
    participant Ledger
    participant Ubiquity_OS

    Student->>Group_Contract: Deliver evidence (O1–O10), update artifact
    Student->>Group_Contract: Update Token Stub (Status=true, timestamp, signatories)
    Professor->>Group_Contract: Validate evidence (Epistemic Lock), append signature
    Professor->>Ledger: Record state transition
    Sponsor->>Group_Contract: Add signature (perception-locked consensus)
    Group_Contract->>Ledger: Flip objective flag to true (mirror token state)
    Ledger->>Ubiquity_OS: Escrow Token Metadata ({ObjectiveID, Status, Timestamp, Signatories, Anchor})

    Note over Group_Contract,Ledger: 
      Tokens remain in escrow until all roles have signed.
    alt Dispute arises
        Group_Contract->>Ledger: Revert Token (Status=false), record rationale
    end
    alt Stretch objectives
        Group_Contract->>Ledger: Mint Stretch_Anchor_O10-XX tokens
    end

    Note over Group_Contract: 
      Each contract change generates diffs/state capsules, references Contract_Anchor_O7 for auditability.
    Note over Ubiquity_OS: 
      State transitions are non-temporal; anchors enable deterministic replay.
```

``` 


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
