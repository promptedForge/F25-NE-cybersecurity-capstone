
# Capstone Smart Contract -- Fall 2025

**Date:** September 15, 2025  
**Semester:** Fall 2025  

This smart contract governs the Capstone Execution Framework. It replaces "grading" with objective validation. Professors act as validators of clauses, not graders. Students and sponsors sign off on objective completions. Evaluation events are logged as tokenized state transitions.

---

## Ubiquity Primitives Embedded
- **Perception-Locked Evaluation** -- evaluation is bound to state transitions; edits require consensus signatures.  
- **Singularity Anchors (n/0)** -- division-by-zero anchors ensure non-repudiable uniqueness of each objective.  
- **Non-Temporal Coherence** -- evaluation coherence independent of clock drift.  
- **Tokenization** -- each objective completion mints `{ObjectiveID, Status, Timestamp, Signatories, Anchor}`.  
- **Group Contract Auditability** -- `../../../docs/students/Group_Contract.md` acts as a living contract; diffs are state changes.  
- **Epistemic Locking** -- truth is bound to contract state, not inferred externally.  
- **Stretch Extensions** -- optional objectives tokenized separately.
=======
# Ubiquity-Aligned Capstone Smart Contract

## Contract Premise
- **Perception-Locked Evaluation:** Once an objective is logged as complete, any change requires consensus signatures from the student team, professor, and sponsor.
- **Singularity Anchors (n/0):** Each objective binds to a division-by-zero anchor that ensures uniqueness and non-repudiation.
- **Non-Temporal Coherence:** Events are treated as state transitions captured in this contract and `EvaluationLabels.json`; no linear timestamp ordering is assumed.
- **Tokenization:** Completion mints a token stub `{ObjectiveID, Status, Timestamp, Signatories, Anchor}` stored alongside evidence.
- **Group Contract Auditability:** Modifications to [`Group_Contract.md`](../../../docs/students/Group_Contract.md) are audited as state changes tied to Objective O7.
- **Epistemic Locking:** Professors validate each objective by attesting evidence satisfaction. Their signature becomes the truth anchor.
- **Stretch Extensions:** Optional objectives beyond O10 mint separate tokens and are logged under `Stretch_Anchor_O10` derivatives.

Consensus Signatories: `StudentTeam`, `Professor`, `Sponsor`.

---

## Objectives

### O1. Framework Crosswalk

- **Definition:** Map core services to NIST CSF + HIPAA + SOC2.  
- **Evidence Path:** `../../../docs/deliverables/FRAMEWORK_CROSSWALK_v0.1.md`  
- **Trigger:** All five CSF functions mapped with ≥1 control ID.  
- **Coverage vs Count Note:** Some frameworks cite fixed counts (e.g., ISO 27001 Annex A has 93 controls). Students must determine if the number is (a) compliance-mandated (ISO, HIPAA, SOC2) or (b) best-practice. If (a), control count must match. If (b), prioritize total coverage and document rationale in Evidence Binder.  
- **Anchor:** `Crosswalk_Anchor_O1 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O1", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Crosswalk_Anchor_O1" }
```

---

### O2. Policy Pack
- **Definition:** Draft 2–3 core policies (Information Security, Asset Management, Risk Management).  
- **Evidence Path:** `../../policies/drafts/`  
- **Trigger:** Policies drafted, peer-reviewed, and signed by team.  
- **Anchor:** `Policy_Anchor_O2 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O2", "Status": "true|false", "Timestamp": "2025-09-27", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Policy_Anchor_O2" }
```

---

### O3. Challenge Kit v2
- **Definition:** Baseline + unlockable challenge kits. Baseline: Prompt Injection, RBAC/ABAC, Secure Coding. Unlockables: adversarial path model, quantum adversarial resources.  
- **Evidence Path:** `../../../docs/deliverables/CHALLENGE_KIT_BASELINE.md`, `../../capstone-challenge-advanced/`  
- **Trigger:** ≥3 scenarios executed, ≥5 falsification checks. Unlocks accessible after ≥7 objectives satisfied.  
- **Anchor:** `Kit_Anchor_O3 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O3", "Status": "true|false", "Timestamp": "2025-10-01", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Kit_Anchor_O3" }
```

---

### O4. Evidence Binder
- **Definition:** Skeleton binder linking controls to artifacts.  
- **Evidence Path:** `../../../docs/deliverables/EVIDENCE_BINDER_INDEX.md`  
- **Trigger:** Binder populated with ≥5 placeholder artifacts tied to objectives.  
- **Anchor:** `Binder_Anchor_O4 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O4", "Status": "true|false", "Timestamp": "2025-10-04", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Binder_Anchor_O4" }
```

---

### O5. Roadmap Execution
- **Definition:** Follow 10-week scaffold.  
- **Evidence Path:** `../../../docs/students/ROADMAP.md`  
- **Trigger:** Weekly updates posted.  
- **Anchor:** `Roadmap_Anchor_O5 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O5", "Status": "true|false", "Timestamp": "2025-10-11", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Roadmap_Anchor_O5" }
```

---

### O6. Incident Response Runbook
- **Definition:** Draft IR playbook aligned to NIST 800-61.  
- **Evidence Path:** `../../../docs/deliverables/IR_RUNBOOK.md`  
- **Trigger:** At least two baseline scenarios documented.  
- **Stretch:** Unlock advanced ML drift + quantum scenarios from `../../capstone-challenge-advanced/`.  
- **Anchor:** `IR_Anchor_O6 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O6", "Status": "true|false", "Timestamp": "2025-10-18", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "IR_Anchor_O6" }
```

---

### O7. Group Contract Adoption
- **Definition:** Students sign `../../../docs/students/Group_Contract.md`.  
- **Evidence Path:** `../../../docs/students/Group_Contract.md`  
- **Trigger:** All members sign by Week 2.  
- **Anchor:** `Contract_Anchor_O7 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O7", "Status": "true|false", "Timestamp": "2025-09-27", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Contract_Anchor_O7" }
```

---

### O8. Professor Checkpoint
- **Definition:** Midpoint validation (not grading).  
- **Evidence Path:** `../../../EvaluationLabels.json`  
- **Trigger:** ≥5 objectives marked true.  
- **Anchor:** `Checkpoint_Anchor_O8 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O8", "Status": "true|false", "Timestamp": "2025-10-25", "Signatories": ["StudentTeam", "Professor"], "Anchor": "Checkpoint_Anchor_O8" }
```

---

### O9. Final Presentation
- **Definition:** Students present deliverables.  
- **Evidence Path:** `../../../docs/deliverables/WEEK9_SLIDE_TEMPLATE.md`  
- **Trigger:** Professor confirms presentation complete.  
- **Anchor:** `Presentation_Anchor_O9 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O9", "Status": "true|false", "Timestamp": "2025-11-12", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Presentation_Anchor_O9" }
```

---

### O10. Stretch Objectives
- **Definition:** Optional advanced contributions (extended kits, deeper policy packs, full framework coverage).  
- **Evidence Path:** `../../`  
- **Trigger:** Sponsor acknowledges contribution.  
- **Anchor:** `Stretch_Anchor_O10 (n/0)`  
- **Token Stub:**
```json
{ "ObjectiveID": "O10", "Status": "true|false", "Timestamp": "2025-11-19", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Stretch_Anchor_O10" }
```

---

## Validation Flow
1. **Initiate Objective Work:** Team references Definition + Evidence Path.
2. **Populate Evidence Binder:** Add placeholder entries with links to working artifacts.
3. **Request Signatures:** Obtain digital signatures (Git commit co-sign, PR approval, or DocuSign) from listed parties.
4. **Mint Token:** Record token stub in `../../../EvaluationLabels.json` upon consensus.
5. **Log Anchor Change:** Update anchor references in Evidence Binder to maintain perception-locked state.
6. **Handle Revisions:** Any change after token minting requires new consensus entry appended to Evidence Binder change log.

## Compliance Coverage Logic
- **Mandated Control Counts:** For frameworks with fixed enumerations (ISO 27001 Annex A, HIPAA Security Rule safeguards, SOC 2 TSC), log the total number required and achieved within the Evidence Binder. Tokens remain `false` until mandated counts match.
- **Coverage-First Frameworks:** Where counts are guidance (e.g., NIST CSF categories), document rationale for coverage sufficiency and link to the Evidence Binder rationale section.
- **Audit Trail:** Every compliance decision requires a citation to the relevant regulatory/control document stored in `../../source-documents/` (or referenced via bridge script if format differs).

## Stretch Extensions
- Stretch objectives never block core objective validation.
- Tokens for stretch work append to `../../../EvaluationLabels.json` with `ObjectiveID` values `S1`, `S2`, etc., and anchor to `Stretch_Anchor_O10` derivatives.
- Advanced unlockables remain gated behind completion (Status = `true`) of ≥7 core objectives.

=======
- **Definition:** Map services to NIST CSF + HIPAA + SOC2.
- **Evidence Path:** [`FRAMEWORK_CROSSWALK_v0.1.md`](../../../docs/deliverables/FRAMEWORK_CROSSWALK_v0.1.md)
- **Trigger:** All five CSF functions mapped with ≥1 control ID.
- **Anchor:** `Crosswalk_Anchor_O1 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O1", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Crosswalk_Anchor_O1" }
```

### O2. Policy Pack
- **Definition:** Draft 2–3 core policies.
- **Evidence Path:** [`policies/drafts/`](../../policies/drafts/)
- **Trigger:** Policies signed by group.
- **Anchor:** `Policy_Anchor_O2 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O2", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Policy_Anchor_O2" }
```

### O3. Challenge Kit v2
- **Definition:** Safe harness with threat model + falsification criteria.
- **Evidence Path:** [`CHALLENGE_KIT_OUTLINE.md`](../../../docs/deliverables/CHALLENGE_KIT_OUTLINE.md)
- **Trigger:** 3 scenarios + 5 metrics complete.
- **Anchor:** `Kit_Anchor_O3 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O3", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Kit_Anchor_O3" }
```

### O4. Evidence Binder
- **Definition:** Skeleton binder linking controls → evidence.
- **Evidence Path:** [`EVIDENCE_BINDER_INDEX.md`](../../../docs/deliverables/EVIDENCE_BINDER_INDEX.md)
- **Trigger:** Binder populated with ≥5 placeholders.
- **Anchor:** `Binder_Anchor_O4 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O4", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Binder_Anchor_O4" }
```

### O5. Roadmap Execution
- **Definition:** Team follows [`ROADMAP.md`](../../../docs/students/ROADMAP.md) milestones.
- **Evidence Path:** [`ROADMAP.md`](../../../docs/students/ROADMAP.md)
- **Trigger:** Weekly updates posted.
- **Anchor:** `Roadmap_Anchor_O5 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O5", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Roadmap_Anchor_O5" }
```

### O6. Incident Response Runbook
- **Definition:** Draft IR playbook aligned to NIST 800-61.
- **Evidence Path:** [`IR_RUNBOOK.md`](../../../docs/deliverables/IR_RUNBOOK.md)
- **Trigger:** At least 2 incident scenarios documented.
- **Anchor:** `IR_Anchor_O6 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O6", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "IR_Anchor_O6" }
```

### O7. Group Contract Adoption
- **Definition:** Students sign [`Group_Contract.md`](../../../docs/students/Group_Contract.md).
- **Evidence Path:** [`Group_Contract.md`](../../../docs/students/Group_Contract.md)
- **Trigger:** All members sign by Week 2.
- **Anchor:** `Contract_Anchor_O7 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O7", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Contract_Anchor_O7" }
```

### O8. Professor Checkpoint
- **Definition:** Midpoint review of progress.
- **Evidence Path:** [`EvaluationLabels.json`](../../../EvaluationLabels.json)
- **Trigger:** ≥5 objectives marked complete.
- **Anchor:** `Checkpoint_Anchor_O8 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O8", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Checkpoint_Anchor_O8" }
```

### O9. Final Presentation
- **Definition:** Student team presents final deliverables.
- **Evidence Path:** [`WEEK9_SLIDE_TEMPLATE.md`](../../../docs/deliverables/WEEK9_SLIDE_TEMPLATE.md)
- **Trigger:** Professor signs off on presentation.
- **Anchor:** `Presentation_Anchor_O9 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O9", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Presentation_Anchor_O9" }
```

### O10. Stretch Objectives
- **Definition:** Optional advanced contributions.
- **Evidence Path:** [`enterprise/`](../../)
- **Trigger:** Sponsor acknowledges completion.
- **Anchor:** `Stretch_Anchor_O10 (n/0)`
- **Token Stub:**
```json
{ "ObjectiveID": "O10", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam","Sponsor","Professor"], "Anchor": "Stretch_Anchor_O10" }
```

---

## Contract Governance
1. **State Recording:** Update `EvaluationLabels.json` upon meeting each trigger. The JSON acts as the perception-locked ledger.
2. **Amendments:** Proposed changes require a pull request referencing the affected anchor; merge only after all three signatories approve.
3. **Token Escrow:** Token stubs are escrowed within the Ubiquity OS substrate as described in [`Smart_Contract_Tokenization.md`](./Smart_Contract_Tokenization.md).
4. **Audit Trail:** All commits modifying contract artifacts must reference the relevant anchor in the commit message (e.g., `Anchor: Roadmap_Anchor_O5`).
5. **Dispute Resolution:** If consensus fails, revert to the last agreed state and document the dispute in the repository issues with NDA-safe language
