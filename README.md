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
5. **Trigger objectives** using the enhanced smart contract tokenization system:
   - `scripts/trigger_objective.sh O3 "evidence-url" StudentTeam "message"`
   - `scripts/professor_validate.sh O3 Professor`  
   - `scripts/sponsor_acknowledge.sh O3 Sponsor`
   - `python3 scripts/token_manager.py complete O3`
6. A GitHub Action writes enhanced **receipts** to `receipts/` with full tokenization metadata.
7. Sponsors review receipts & artifacts; faculty can see everything and comment anytime.

> NDA or private material is referenced as **"where applicable"** and handled outside this public repo.

---

## Roles
- **Students (you):** build, document, and trigger objectives. Keep logs and evidence links in your team folder.
- **Sponsors (Prompted Forge):** review objective receipts + artifacts; approve or request changes via signature consensus.
- **Faculty:** observe progress, provide academic validation via epistemic lock, and final grading per course policy.

---

## Smart Contract Tokenization System

The enhanced tokenization system implements perception-locked evaluation with consensus signatures:

### Token Flow
1. **Evidence Delivery:** Students deliver evidence and update token stub
2. **Professor Validation:** Epistemic lock applied with professor signature
3. **Sponsor Acknowledgement:** Perception-locked consensus with sponsor signature
4. **Ledger Update:** Objective flag flipped to true when consensus achieved
5. **Escrow:** Token metadata escrowed in Ubiquity OS substrate simulation

### Key Scripts
- `scripts/trigger_objective.sh` - Deliver evidence and start tokenization flow
- `scripts/professor_validate.sh` - Professor validation with epistemic lock
- `scripts/sponsor_acknowledge.sh` - Sponsor acknowledgement for consensus
- `scripts/token_manager.py` - Core token management system
- `scripts/stretch_objective.sh` - Mint stretch tokens (O10-XX)
- `scripts/dispute_token.sh` - Dispute resolution and token reversion

### Token Structure
Each objective has a token stub with:
- **ObjectiveID:** O1-O10 (or O10-XX for stretch)
- **Status:** true/false
- **Timestamp:** ISO 8601 timestamp
- **Signatories:** Array of consensus signatures
- **Anchor:** Unique anchor (e.g., Crosswalk_Anchor_O1)

### Consensus Model
- **StudentTeam:** Must sign for evidence delivery
- **Professor:** Provides epistemic lock validation
- **Sponsor:** Adds perception-locked consensus

Tokens remain in escrow until all three consensus roles have signed.

---

## Quick Links
- Welcome: `docs/00_WELCOME.md`
- Students: `docs/students/START_HERE.md`
- Deliverables list: `docs/students/DELIVERABLES.md`
- Faculty landing: `docs/faculty/00_FACULTY_START.md`
- Token manager: `scripts/token_manager.py status`
- Group contract: `docs/students/Group_Contract.md`