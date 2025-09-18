# Professor Validation Guide -- Capstone Objectives (Fall 2025)

**Date:** September 16, 2025  \\
**Semester:** Fall 2025

---

## What this is

This guide is the "smart contract" translated for faculty. It lists each objective, the evidence path inside the repository, and the trigger you confirm. You are not grading line-by-line; you simply validate that the stated trigger is satisfied.

- **Low-friction:** You only review marked evidence, then confirm completion.
- **Flexible:** Objectives can map to your local rubric or checkpoint structure.
- **Traceable:** Once you comment "complete" on a pull request or issue, the student steward updates `../../../EvaluationLabels.json` and the ledger stays in sync.

---

## How to use this

1. Review the objective definition below.  
2. Open the evidence path (links are relative to this file).  
3. When the trigger is satisfied, note "complete" in a PR/issue comment or checklist.  
4. The student steward toggles the ledger entry; no additional paperwork is required.

**Fixed milestones**
- **Midpoint Checkpoint:** At least five objectives validated.  
- **Final Presentation:** Team presents their deliverables; you confirm completion.

All other cadence choices are yours as long as student progress remains visible on the shared GitHub Project board.

---

## Objective summary (at a glance)

| ID | Objective | Evidence Path(s) | Trigger (mark complete when…) |
|----|-----------|------------------|--------------------------------|
| **O1** | Framework Crosswalk | `../../../docs/deliverables/FRAMEWORK_CROSSWALK_v0.1.md` | All five NIST CSF functions mapped with ≥1 control ID (with SOC 2 + HIPAA notes) |
| **O2** | Policy Pack | `../../policies/drafts/` | 2–3 priority policies drafted, peer-reviewed, and team-signed |
| **O3** | Challenge Kit v2 | `../../../docs/deliverables/CHALLENGE_KIT_BASELINE.md`, `../../capstone-challenge-advanced/` | ≥3 scenarios executed and ≥5 falsification checks captured |
| **O4** | Evidence Binder | `../../../docs/deliverables/EVIDENCE_BINDER_INDEX.md` | ≥5 entries populated (placeholders acceptable early) |
| **O5** | Roadmap Execution | `../../../docs/students/ROADMAP.md` | Weekly updates visible in repo / project board |
| **O6** | Incident Response Runbook | `../../../docs/deliverables/IR_RUNBOOK.md` | ≥2 baseline scenarios documented |
| **O7** | Group Contract | `../../../docs/students/Group_Contract.md` | All team members sign by Week 2 |
| **O8** | Midpoint Checkpoint | `../../../EvaluationLabels.json` | ≥5 objectives marked `true` |
| **O9** | Final Presentation | `../../../docs/deliverables/WEEK9_SLIDE_TEMPLATE.md` | Presentation delivered and confirmed |
| **O10** | Stretch Work (optional) | [`enterprise/`](../..) | Sponsor acknowledges completion |

---

## Notes for O1 (Framework Crosswalk)

Frameworks such as HIPAA, ISO, or SOC 2 sometimes require a fixed number of controls. When the count is mandated, ensure the deliverable demonstrates all controls are accounted for. Otherwise, validate on coverage: every relevant category should have a mapped control with rationale captured in the evidence binder.

---

## Why this approach

- **Transparency:** Every validation maps to an artifact and anchor.  
- **Auditability:** The binder plus pull-request history provide a self-contained trail.  
- **Flexibility:** Aside from the midpoint and final checkpoints, you may adapt the cadence to your course norms.  
- **Shared accountability:** Students own progress updates; you simply attest when triggers are satisfied.

---

## In practice

- If the work meets the definition and trigger, comment "complete" (or similar).  
- If anything is missing, leave a short note (e.g., "Need stronger mapping for CSF Protect" or "Show peer-review notes on Policy Pack").  
- Students revise and re-request validation.

Bottom line: this should be low-friction for you, rigorous for them, and compatible with your local assessment model.
