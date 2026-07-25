#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_phase0c19_operational_binding as checker


class OperativeBindingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="phase0c19-binding-"))
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        for rel in checker.REQUIRED_FILES:
            src = self.source / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return root

    def replace(self, root: Path, rel: str, old: str, new: str) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def mutate_record(self, root: Path, key: str, value: object) -> None:
        path = root / "master-plan-index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"][key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_valid_binding(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "operative_binding_valid_non_authorizing")
        self.assertTrue(report["p01_active"])
        self.assertFalse(report["runtime_implementation_authorized"])

    def test_02_acceptance_status_pending_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md", "accepted-state proof and operative merge bound", "accepted-state proof and operative merge pending"); self.invalid(root)

    def test_03_binding_status_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, "Status: OPERATIVE ACCEPTANCE BOUND", "Status: PENDING"); self.invalid(root)

    def test_04_accepted_head_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.ACCEPTED_HEAD, "0" * 40); self.invalid(root)

    def test_05_accepted_run_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.ACCEPTED_RUN, "0"); self.invalid(root)

    def test_06_artifact_digest_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.ACCEPTED_ARTIFACT_DIGEST, "sha256:" + "0" * 64); self.invalid(root)

    def test_07_validation_digest_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.ACCEPTED_VALIDATION_SHA, "0" * 64); self.invalid(root)

    def test_08_regression_digest_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.ACCEPTED_REGRESSION_SHA, "0" * 64); self.invalid(root)

    def test_09_operative_merge_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING_PATH, checker.OPERATIVE_MERGE, "0" * 40); self.invalid(root)

    def test_10_handoff_binding_missing_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.ACCEPTED_HEAD, "removed"); self.invalid(root)

    def test_11_machine_pending_flag_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "accepted_state_proof_pending", True); self.invalid(root)

    def test_12_machine_merge_pending_flag_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "operative_acceptance_merge_pending", True); self.invalid(root)

    def test_13_machine_proof_commit_drift_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "confirmed_proof_commit", "0" * 40); self.invalid(root)

    def test_14_machine_physical_collection_start_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "physical_host_collection_started", True); self.invalid(root)

    def test_15_machine_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "adr_0033_accepted", True); self.invalid(root)

    def test_16_machine_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.mutate_record(root, "runtime_implementation_authorized", True); self.invalid(root)

    def test_17_current_physical_collection_start_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "physical-host collection: NOT STARTED", "physical-host collection: STARTED"); self.invalid(root)

    def test_18_current_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "ADR-0033: PROPOSED", "ADR-0033: ACCEPTED"); self.invalid(root)

    def test_19_current_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED"); self.invalid(root)

    def test_20_recovery_order_binding_missing_fails(self) -> None:
        path_root = self.copy_state(); path = path_root / "master-plan-index.json"; data = json.loads(path.read_text()); data["recovery_order"].remove(checker.BINDING_PATH); path.write_text(json.dumps(data, indent=2) + "\n"); self.invalid(path_root)

    def test_21_master_plan_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "MASTER_PLAN.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_22_roadmap_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "IMPLEMENTATION_ROADMAP.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_23_adr0037_proposed_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md", "Status: accepted", "Status: proposed"); self.invalid(root)

    def test_24_p01_unconfirmed_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md", "Status: CONFIRMED, non-authorizing", "Status: provisional"); self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
