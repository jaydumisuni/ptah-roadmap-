#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_phase0c19_acceptance as checker


class Phase0C19AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="phase0c19-acceptance-"))
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        for rel in checker.REQUIRED_FILES:
            src = self.source / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return root

    def replace(self, root: Path, rel: str, old: str, new: str) -> None:
        path = root / rel
        content = path.read_text(encoding="utf-8")
        self.assertIn(old, content)
        path.write_text(content.replace(old, new, 1), encoding="utf-8")

    def mutate_index(self, root: Path, key: str, value: object) -> None:
        path = root / "master-plan-index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"][key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_valid_accepted_state(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "accepted_state_valid_non_authorizing")
        self.assertTrue(report["adr_0037_accepted"])
        self.assertTrue(report["p01_active"])
        self.assertFalse(report["runtime_implementation_authorized"])

    def test_02_master_plan_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "MASTER_PLAN.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_03_roadmap_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "IMPLEMENTATION_ROADMAP.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_04_adr0037_proposed_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md", "Status: accepted", "Status: proposed"); self.invalid(root)

    def test_05_phase0c19_incomplete_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "work-packages/PHASE-0C-19-DEEP-WORKSPACE-ROADMAP-RECONCILIATION.md", "Status: COMPLETE / ACCEPTED", "Status: CANDIDATE"); self.invalid(root)

    def test_06_p01_pause_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "P01: ACTIVE / BLOCKED ON EXACT PHYSICAL HOST", "P01: PAUSED"); self.invalid(root)

    def test_07_physical_collection_started_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "physical-host collection: NOT STARTED", "physical-host collection: STARTED"); self.invalid(root)

    def test_08_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "ADR-0033: PROPOSED", "ADR-0033: ACCEPTED"); self.invalid(root)

    def test_09_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED"); self.invalid(root)

    def test_10_wrong_proof_commit_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "confirmed_proof_commit", "0" * 40); self.invalid(root)

    def test_11_unconfirmed_proof_commit_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "proof_commit_confirmed", False); self.invalid(root)

    def test_12_candidate_merge_drift_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "candidate_merge", "0" * 40); self.invalid(root)

    def test_13_p01_machine_pause_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "p01_paused", True); self.invalid(root)

    def test_14_machine_physical_start_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "physical_host_collection_started", True); self.invalid(root)

    def test_15_machine_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "adr_0033_accepted", True); self.invalid(root)

    def test_16_machine_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.mutate_index(root, "runtime_implementation_authorized", True); self.invalid(root)

    def test_17_acceptance_candidate_digest_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", checker.CANDIDATE_ARTIFACT_DIGEST, "sha256:" + "0" * 64); self.invalid(root)

    def test_18_acceptance_validation_digest_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", checker.CANDIDATE_VALIDATION_SHA, "0" * 64); self.invalid(root)

    def test_19_package_mapping_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "IMPLEMENTATION_ROADMAP.md", "## A14 amendment", "## removed A14"); self.invalid(root)

    def test_20_cross_track_mapping_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "IMPLEMENTATION_ROADMAP.md", "- **X5:**", "- **removed:**"); self.invalid(root)

    def test_21_core_boundary_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", "no Core family is added", "a Core family is added"); self.invalid(root)

    def test_22_contract_boundary_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", "no frozen contract is reopened", "frozen contracts are reopened"); self.invalid(root)

    def test_23_neutral_ptah_boundary_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", "Ptah does not choose work", "Ptah chooses work"); self.invalid(root)

    def test_24_handoff_next_action_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "The next action is to run the proof kit", "The next action is runtime implementation"); self.invalid(root)

    def test_25_p01_selection_not_confirmed_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md", "Status: CONFIRMED, non-authorizing", "Status: provisional"); self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
