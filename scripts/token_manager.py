#!/usr/bin/env python3
"""
Smart Contract Tokenization Manager
Implements the tokenization flow from the sequence diagram
"""

import json
import sys
import datetime
import hashlib
import os
from typing import Dict, List, Optional


class TokenManager:
    def __init__(self, ledger_path: str = "EvaluationLabels.json"):
        self.ledger_path = ledger_path
        self.load_ledger()
    
    def load_ledger(self):
        """Load the evaluation ledger"""
        try:
            with open(self.ledger_path, 'r') as f:
                self.ledger = json.load(f)
        except FileNotFoundError:
            print(f"Error: {self.ledger_path} not found")
            sys.exit(1)
    
    def save_ledger(self):
        """Save the evaluation ledger"""
        self.ledger["metadata"]["updated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        with open(self.ledger_path, 'w') as f:
            json.dump(self.ledger, f, indent=2)
    
    def update_token_stub(self, objective_id: str, evidence_url: str, signatory: str) -> bool:
        """Update token stub with evidence delivery and signatory"""
        if objective_id not in self.ledger["objectives"]:
            print(f"Error: Objective {objective_id} not found")
            return False
        
        obj = self.ledger["objectives"][objective_id]
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Update token stub
        obj["token_stub"]["Status"] = "true"
        obj["token_stub"]["Timestamp"] = timestamp
        
        # Add signatory if not already present
        if signatory not in obj["token_stub"]["Signatories"]:
            obj["token_stub"]["Signatories"].append(signatory)
        
        # Record state transition
        self.ledger["state_transitions"].append({
            "objective_id": objective_id,
            "action": "evidence_delivered",
            "timestamp": timestamp,
            "signatory": signatory,
            "evidence_url": evidence_url,
            "anchor": obj["token_stub"]["Anchor"]
        })
        
        print(f"Token stub updated for {objective_id} by {signatory}")
        return True
    
    def professor_validate(self, objective_id: str, professor_id: str) -> bool:
        """Professor validation with epistemic lock"""
        if objective_id not in self.ledger["objectives"]:
            print(f"Error: Objective {objective_id} not found")
            return False
        
        obj = self.ledger["objectives"][objective_id]
        
        # Check if evidence was delivered
        if obj["token_stub"]["Status"] != "true":
            print(f"Error: Evidence not yet delivered for {objective_id}")
            return False
        
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Add professor signature
        if professor_id not in obj["token_stub"]["Signatories"]:
            obj["token_stub"]["Signatories"].append(professor_id)
        
        # Record state transition with epistemic lock
        self.ledger["state_transitions"].append({
            "objective_id": objective_id,
            "action": "professor_validation",
            "timestamp": timestamp,
            "signatory": professor_id,
            "epistemic_lock": True,
            "anchor": obj["token_stub"]["Anchor"]
        })
        
        print(f"Professor validation completed for {objective_id} (Epistemic Lock)")
        return True
    
    def sponsor_acknowledge(self, objective_id: str, sponsor_id: str) -> bool:
        """Sponsor acknowledgement for perception-locked consensus"""
        if objective_id not in self.ledger["objectives"]:
            print(f"Error: Objective {objective_id} not found")
            return False
        
        obj = self.ledger["objectives"][objective_id]
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Add sponsor signature
        if sponsor_id not in obj["token_stub"]["Signatories"]:
            obj["token_stub"]["Signatories"].append(sponsor_id)
        
        # Record state transition
        self.ledger["state_transitions"].append({
            "objective_id": objective_id,
            "action": "sponsor_acknowledgement",
            "timestamp": timestamp,
            "signatory": sponsor_id,
            "perception_locked": True,
            "anchor": obj["token_stub"]["Anchor"]
        })
        
        print(f"Sponsor acknowledgement completed for {objective_id}")
        return True
    
    def check_consensus(self, objective_id: str) -> bool:
        """Check if all required signatories have signed"""
        if objective_id not in self.ledger["objectives"]:
            return False
        
        obj = self.ledger["objectives"][objective_id]
        signatories = obj["token_stub"]["Signatories"]
        
        # Check for required consensus roles
        has_student = any("StudentTeam" in sig or "Student" in sig for sig in signatories)
        has_professor = any("Professor" in sig for sig in signatories)
        has_sponsor = any("Sponsor" in sig for sig in signatories)
        
        return has_student and has_professor and has_sponsor
    
    def flip_objective_flag(self, objective_id: str) -> bool:
        """Flip objective flag to true when consensus is reached"""
        if not self.check_consensus(objective_id):
            print(f"Error: Consensus not reached for {objective_id}")
            return False
        
        obj = self.ledger["objectives"][objective_id]
        obj["status"] = True
        obj["escrow_state"] = "released"
        
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Record final state transition
        self.ledger["state_transitions"].append({
            "objective_id": objective_id,
            "action": "objective_completed",
            "timestamp": timestamp,
            "consensus_achieved": True,
            "anchor": obj["token_stub"]["Anchor"]
        })
        
        print(f"Objective {objective_id} completed - consensus achieved, flag flipped to true")
        return True
    
    def revert_token(self, objective_id: str, rationale: str, signatory: str) -> bool:
        """Revert token status for dispute resolution"""
        if objective_id not in self.ledger["objectives"]:
            print(f"Error: Objective {objective_id} not found")
            return False
        
        obj = self.ledger["objectives"][objective_id]
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Revert token status
        obj["token_stub"]["Status"] = "false"
        obj["status"] = False
        obj["escrow_state"] = "disputed"
        
        # Log dispute
        dispute_entry = {
            "objective_id": objective_id,
            "timestamp": timestamp,
            "rationale": rationale,
            "initiated_by": signatory,
            "anchor": obj["token_stub"]["Anchor"]
        }
        self.ledger["dispute_log"].append(dispute_entry)
        
        # Record state transition
        self.ledger["state_transitions"].append({
            "objective_id": objective_id,
            "action": "token_reverted",
            "timestamp": timestamp,
            "signatory": signatory,
            "rationale": rationale,
            "anchor": obj["token_stub"]["Anchor"]
        })
        
        print(f"Token {objective_id} reverted due to dispute: {rationale}")
        return True
    
    def mint_stretch_token(self, base_objective: str, stretch_id: str, evidence_url: str) -> bool:
        """Mint stretch objective tokens (e.g., Stretch_Anchor_O10-XX)"""
        if base_objective != "O10":
            print("Error: Stretch objectives only supported for O10")
            return False
        
        stretch_key = f"{base_objective}-{stretch_id}"
        anchor = f"Stretch_Anchor_{stretch_key}"
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        # Create stretch token
        stretch_token = {
            "status": False,
            "token_stub": {
                "ObjectiveID": stretch_key,
                "Status": "false",
                "Timestamp": timestamp,
                "Signatories": [],
                "Anchor": anchor
            },
            "evidence_path": evidence_url,
            "escrow_state": "pending",
            "stretch_type": True,
            "base_objective": base_objective
        }
        
        self.ledger["stretch_objectives"][stretch_key] = stretch_token
        
        # Record state transition
        self.ledger["state_transitions"].append({
            "objective_id": stretch_key,
            "action": "stretch_token_minted",
            "timestamp": timestamp,
            "evidence_url": evidence_url,
            "anchor": anchor
        })
        
        print(f"Stretch token {stretch_key} minted with anchor {anchor}")
        return True
    
    def get_escrow_metadata(self, objective_id: str) -> Optional[Dict]:
        """Get token metadata for Ubiquity OS escrow"""
        objectives = {**self.ledger["objectives"], **self.ledger["stretch_objectives"]}
        
        if objective_id not in objectives:
            return None
        
        obj = objectives[objective_id]
        return {
            "ObjectiveID": obj["token_stub"]["ObjectiveID"],
            "Status": obj["token_stub"]["Status"],
            "Timestamp": obj["token_stub"]["Timestamp"],
            "Signatories": obj["token_stub"]["Signatories"],
            "Anchor": obj["token_stub"]["Anchor"],
            "EscrowState": obj["escrow_state"]
        }
    
    def display_status(self):
        """Display current ledger status"""
        print("=== Smart Contract Token Status ===")
        print(f"Updated: {self.ledger['metadata']['updated_at']}")
        print(f"Contract Anchor: {self.ledger['metadata']['contract_anchor']}")
        print()
        
        print("Core Objectives:")
        for obj_id, obj in self.ledger["objectives"].items():
            status = "✓" if obj["status"] else "○"
            sigs = len(obj["token_stub"]["Signatories"])
            escrow = obj["escrow_state"]
            print(f"  {status} {obj_id}: {escrow} ({sigs} signatures)")
        
        if self.ledger["stretch_objectives"]:
            print("\nStretch Objectives:")
            for obj_id, obj in self.ledger["stretch_objectives"].items():
                status = "✓" if obj["status"] else "○"
                sigs = len(obj["token_stub"]["Signatories"])
                escrow = obj["escrow_state"]
                print(f"  {status} {obj_id}: {escrow} ({sigs} signatures)")
        
        if self.ledger["dispute_log"]:
            print(f"\nDisputes: {len(self.ledger['dispute_log'])}")
        
        print(f"State Transitions: {len(self.ledger['state_transitions'])}")


def main():
    if len(sys.argv) < 2:
        print("Usage: token_manager.py <command> [args...]")
        print("Commands:")
        print("  deliver <objective> <evidence_url> <signatory>  - Deliver evidence")
        print("  validate <objective> <professor_id>             - Professor validation")
        print("  acknowledge <objective> <sponsor_id>            - Sponsor acknowledgement")
        print("  complete <objective>                            - Complete objective (flip flag)")
        print("  revert <objective> <rationale> <signatory>     - Revert token for dispute")
        print("  stretch <base_obj> <stretch_id> <evidence_url> - Mint stretch token")
        print("  status                                          - Display status")
        print("  escrow <objective>                              - Get escrow metadata")
        sys.exit(1)
    
    manager = TokenManager()
    command = sys.argv[1]
    
    try:
        if command == "deliver":
            objective, evidence_url, signatory = sys.argv[2:5]
            manager.update_token_stub(objective, evidence_url, signatory)
        
        elif command == "validate":
            objective, professor_id = sys.argv[2:4]
            manager.professor_validate(objective, professor_id)
        
        elif command == "acknowledge":
            objective, sponsor_id = sys.argv[2:4]
            manager.sponsor_acknowledge(objective, sponsor_id)
        
        elif command == "complete":
            objective = sys.argv[2]
            manager.flip_objective_flag(objective)
        
        elif command == "revert":
            objective, rationale, signatory = sys.argv[2:5]
            manager.revert_token(objective, rationale, signatory)
        
        elif command == "stretch":
            base_obj, stretch_id, evidence_url = sys.argv[2:5]
            manager.mint_stretch_token(base_obj, stretch_id, evidence_url)
        
        elif command == "status":
            manager.display_status()
            manager.save_ledger()
            return
        
        elif command == "escrow":
            objective = sys.argv[2]
            metadata = manager.get_escrow_metadata(objective)
            if metadata:
                print(json.dumps(metadata, indent=2))
            else:
                print(f"Objective {objective} not found")
            return
        
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
        
        manager.save_ledger()
        
    except IndexError:
        print(f"Error: Insufficient arguments for command '{command}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()