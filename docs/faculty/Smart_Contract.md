
# Capstone Smart Contract -- Fall 2025

**Date:** September 15, 2025  
**Semester:** Fall 2025  

This smart contract governs the Capstone Execution Framework. It replaces "grading" with objective validation. Professors act as validators of clauses, not graders. Students and sponsors sign off on objective completions. Evaluation events are logged as tokenized state transitions.

---

## Contract Principles

- **Consensus-Based Validation:** Once an objective is logged as complete, any change requires unanimous approval from the student team, professor, and sponsor.
- **Immutable Anchors:** Each objective uses a unique anchor identifier that ensures non-repudiation and prevents duplicate submissions.
- **State-Based Evaluation:** Progress is tracked through discrete state transitions recorded in this contract and `EvaluationLabels.json`, independent of timing.
- **Digital Tokenization:** Completion generates a token record `{ObjectiveID, Status, Timestamp, Signatories, Anchor}` stored with evidence.
- **Living Contract Audit:** All modifications to the Group Contract are tracked as versioned state changes tied to Objective O7.
- **Evidence-Based Validation:** Professors validate objectives by verifying evidence meets stated criteria before digital signature.
- **Optional Extensions:** Stretch objectives beyond the core requirements are tokenized separately and do not block core validation.

**Required Signatories:** `StudentTeam`, `Professor`, `Sponsor`

---

## Objectives

### O1. Framework Crosswalk

- **Definition:** Map core services to NIST CSF + HIPAA + SOC2.  
- **Evidence Path:** `../../../docs/deliverables/FRAMEWORK_CROSSWALK_v0.1.md`  
- **Trigger:** All five CSF functions mapped with ≥1 control ID.  
- **Compliance Requirements:** Map organizational services to specific controls from each framework. For frameworks with mandatory control counts (ISO 27001, HIPAA Security Rule, SOC 2), document the total number required and achieved. For guidance-based frameworks (NIST CSF), prioritize comprehensive coverage and document rationale for scope decisions.
- **Anchor:** `Crosswalk_Anchor_O1`  
- **Token Stub:**
```json
{ "ObjectiveID": "O1", "Status": "true|false", "Timestamp": "2025-09-20", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Crosswalk_Anchor_O1" }
```

---

### O2. Policy Pack
- **Definition:** Draft 2–3 core policies (Information Security, Asset Management, Risk Management).  
- **Evidence Path:** `../../policies/drafts/`  
- **Trigger:** Policies drafted, peer-reviewed, and signed by team.  
- **Anchor:** `Policy_Anchor_O2`  
- **Token Stub:**
```json
{ "ObjectiveID": "O2", "Status": "true|false", "Timestamp": "2025-09-27", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Policy_Anchor_O2" }
```

---

### O3. Challenge Kit v2
- **Definition:** Develop baseline security challenge scenarios with advanced unlockable content. Baseline includes: Prompt Injection, RBAC/ABAC, and Secure Coding challenges. Advanced scenarios (adversarial modeling, quantum-resistant security) unlock after completing ≥7 core objectives.
- **Evidence Path:** `../../../docs/deliverables/CHALLENGE_KIT_BASELINE.md`, `../../capstone-challenge-advanced/`  
- **Trigger:** ≥3 baseline scenarios executed with ≥5 validation metrics documented.
- **Anchor:** `Kit_Anchor_O3`  
- **Token Stub:**
```json
{ "ObjectiveID": "O3", "Status": "true|false", "Timestamp": "2025-10-01", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Kit_Anchor_O3" }
```

---

### O4. Evidence Binder
- **Definition:** Create comprehensive documentation linking security controls to implementation evidence.
- **Evidence Path:** `../../../docs/deliverables/EVIDENCE_BINDER_INDEX.md`  
- **Trigger:** Index populated with ≥5 placeholder artifacts, each linked to specific control objectives.
- **Anchor:** `Binder_Anchor_O4`  
- **Token Stub:**
```json
{ "ObjectiveID": "O4", "Status": "true|false", "Timestamp": "2025-10-04", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Binder_Anchor_O4" }
```

---

### O5. Roadmap Execution
- **Definition:** Maintain consistent progress tracking through structured 10-week execution timeline.
- **Evidence Path:** `../../../docs/students/ROADMAP.md`  
- **Trigger:** Weekly status updates documented with milestone completion notes.
- **Anchor:** `Roadmap_Anchor_O5`  
- **Token Stub:**
```json
{ "ObjectiveID": "O5", "Status": "true|false", "Timestamp": "2025-10-11", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Roadmap_Anchor_O5" }
```

---

### O6. Incident Response Runbook
- **Definition:** Develop incident response procedures aligned with NIST 800-61 framework.
- **Evidence Path:** `../../../docs/deliverables/IR_RUNBOOK.md`  
- **Trigger:** At least two complete incident scenarios documented with prepare/detect/respond/recover phases.
- **Advanced Option:** Extended scenarios covering ML model drift and quantum-resistant incident response available after core completion.
- **Anchor:** `IR_Anchor_O6`  
- **Token Stub:**
```json
{ "ObjectiveID": "O6", "Status": "true|false", "Timestamp": "2025-10-18", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "IR_Anchor_O6" }
```

---

### O7. Group Contract Adoption
- **Definition:** Team members formalize collaboration agreement by signing the Group Contract.
- **Evidence Path:** `../../../docs/students/Group_Contract.md`  
- **Trigger:** All team members provide digital signatures by Week 2.
- **Anchor:** `Contract_Anchor_O7`  
- **Token Stub:**
```json
{ "ObjectiveID": "O7", "Status": "true|false", "Timestamp": "2025-09-27", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Contract_Anchor_O7" }
```

---

### O8. Professor Checkpoint
- **Definition:** Mid-semester progress review and validation checkpoint.
- **Evidence Path:** `../../../EvaluationLabels.json`  
- **Trigger:** Minimum of 5 core objectives completed and validated.
- **Anchor:** `Checkpoint_Anchor_O8`  
- **Token Stub:**
```json
{ "ObjectiveID": "O8", "Status": "true|false", "Timestamp": "2025-10-25", "Signatories": ["StudentTeam", "Professor"], "Anchor": "Checkpoint_Anchor_O8" }
```

---

### O9. Final Presentation
- **Definition:** Comprehensive presentation of all capstone deliverables and outcomes.
- **Evidence Path:** `../../../docs/deliverables/WEEK9_SLIDE_TEMPLATE.md`  
- **Trigger:** Completed presentation delivered and approved by professor.
- **Anchor:** `Presentation_Anchor_O9`  
- **Token Stub:**
```json
{ "ObjectiveID": "O9", "Status": "true|false", "Timestamp": "2025-11-12", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Presentation_Anchor_O9" }
```

---

### O10. Stretch Objectives
- **Definition:** Optional advanced work including extended challenge kits, comprehensive policy frameworks, or full regulatory compliance coverage.
- **Evidence Path:** `../../`  
- **Trigger:** Sponsor acknowledgment of meaningful advanced contribution beyond core requirements.
- **Anchor:** `Stretch_Anchor_O10`  
- **Token Stub:**
```json
{ "ObjectiveID": "O10", "Status": "true|false", "Timestamp": "2025-11-19", "Signatories": ["StudentTeam", "Sponsor", "Professor"], "Anchor": "Stretch_Anchor_O10" }
```

---

## Validation Process
1. **Initiate Objective Work:** Team reviews objective definition and identifies required evidence deliverables.
2. **Create Evidence Placeholders:** Add structured entries in the Evidence Binder linking to work-in-progress artifacts.
3. **Request Digital Signatures:** Obtain consensus approvals via Git commit co-signatures, PR approvals, or DocuSign from required parties.
4. **Generate Token Record:** Upon consensus, record completion token in `../../../EvaluationLabels.json`.
5. **Update Anchor References:** Maintain immutable state by updating anchor references in Evidence Binder.
6. **Handle Modifications:** Any post-completion changes require new consensus approval documented in change log.

## Framework Compliance Guidance
- **Fixed-Count Frameworks:** For standards with mandatory control counts (ISO 27001 Annex A has 93 controls, HIPAA Security Rule has specific safeguards), document total required vs. achieved in Evidence Binder. Objective remains incomplete until counts are satisfied.
- **Coverage-Based Frameworks:** For guidance frameworks (NIST CSF functions, SOC 2 trust principles), prioritize comprehensive coverage and document scope rationale in Evidence Binder.
- **Documentation Requirements:** All compliance decisions must cite authoritative source documents stored in `../../source-documents/` or provide clear references to external standards.

## Advanced Objectives
- Advanced objectives do not block completion of core requirements.
- Stretch work uses separate token identifiers (`S1`, `S2`, etc.) linked to `Stretch_Anchor_O10` derivatives.
- Advanced challenge scenarios unlock only after completing minimum 7 core objectives.

---

## Contract Governance

### State Management
1. **Ledger Updates:** Record objective completions in `EvaluationLabels.json` upon achieving consensus validation.
2. **Amendment Process:** Proposed contract changes require pull request with affected anchor reference; approval requires all signatory consensus.
3. **Token Escrow:** Completion tokens remain in pending state until all required signatures are obtained, as detailed in [`Smart_Contract_Tokenization.md`](./Smart_Contract_Tokenization.md).
4. **Audit Requirements:** All commits modifying contract artifacts must reference relevant anchor in commit message (format: `Anchor: <AnchorName>`).
5. **Dispute Resolution:** Upon consensus failure, revert to last agreed state and document dispute in repository issues using NDA-appropriate language.

### Validation Authority
- **Professor Role:** Academic validation of evidence quality and technical completeness
- **Sponsor Role:** Industry validation of practical applicability and business value  
- **Student Role:** Delivery responsibility and evidence compilation

### Quality Assurance
- All deliverables must meet professional documentation standards
- Evidence must be directly linked to stated objectives
- Timestamps reflect actual completion, not retroactive dating
- Digital signatures confirm informed approval, not administrative processing
