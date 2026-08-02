#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_p01_closure_current_authority as checker


class P01ClosureCurrentAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="p01-closure-authority-"))
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

    def test_01_current_state_passes(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "current_authority_valid_non_authorizing")
        self.assertTrue(report["p01_active"])
        self.assertFalse(report["runtime_implementation_authorized"])

    def test_02_stale_phase0c19_review_wording_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "Phase 0C-19 complete and ADR-0037 accepted", "Phase 0C-19 / ADR-0037 planning-load reconciliation in review")
        self.invalid(root)

    def test_03_stale_preparation_commit_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], checker.PROOF_COMMIT, checker.STALE_PREPARATION_COMMIT)
        self.invalid(root)

    def test_04_master_plan_version_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "Master Plan version `1.1.0` accepted and operative", "Master Plan version `1.0.0` accepted and operative")
        self.invalid(root)

    def test_05_roadmap_version_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "implementation roadmap version `1.1.0` accepted and operative", "implementation roadmap version `1.0.0` accepted and operative")
        self.invalid(root)

    def test_06_accepted_plan_listed_open_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "- execution on the exact physical Ubuntu host;", "- Master Plan closure accepted and merged;\n- execution on the exact physical Ubuntu host;")
        self.invalid(root)

    def test_07_incomplete_phase_review_range_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "Phase 0C-01 through Phase 0C-19", "Phase 0C-01 through Phase 0C-16")
        self.invalid(root)

    def test_08_wrong_host_kernel_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "6.8.0-136-generic", "6.8.0-135-generic")
        self.invalid(root)

    def test_09_missing_proof_eligible_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], "proof_eligible: true", "proof complete")
        self.invalid(root)

    def test_10_runtime_authorization_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED")
        self.invalid(root)

    def test_11_physical_collection_started_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "CURRENT_STATE.md", "physical-host collection: NOT STARTED", "physical-host collection: STARTED")
        self.invalid(root)

    def test_12_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "CURRENT_STATE.md", "ADR-0033: PROPOSED", "ADR-0033: ACCEPTED")
        self.invalid(root)

    def test_13_machine_proof_commit_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, "confirmed_proof_commit", "0" * 40)
        self.invalid(root)

    def test_14_machine_collection_start_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, "physical_host_collection_started", True)
        self.invalid(root)

    def test_15_machine_runtime_authorization_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, "runtime_implementation_authorized", True)
        self.invalid(root)

    def test_16_missing_binding_merge_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], checker.PLANNING_BINDING_MERGE, "0" * 40)
        self.invalid(root)

    def test_17_missing_handoff_correction_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], checker.HANDOFF_CORRECTION_MERGE, "0" * 40)
        self.invalid(root)

    def test_18_unconfirmed_selection_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md", "Status: CONFIRMED, non-authorizing", "Status: provisional, non-authorizing")
        self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
