#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_phase0c19_deep_workspace_reconciliation as checker


class Phase0C19ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_root = Path(__file__).resolve().parents[1]

    def copy_candidate(self) -> Path:
        temp = Path(tempfile.mkdtemp(prefix="phase0c19-test-"))
        self.addCleanup(lambda: shutil.rmtree(temp, ignore_errors=True))
        for rel in checker.REQUIRED_FILES:
            src = self.source_root / rel
            dst = temp / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return temp

    def mutate(self, root: Path, rel: str, old: str, new: str) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"missing mutation anchor: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_valid_candidate(self) -> None:
        report = checker.validate(self.copy_candidate())
        self.assertEqual(report["status"], "candidate_valid_non_authorizing")
        self.assertFalse(report["runtime_implementation_authorized"])

    def test_02_runtime_authorization_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED")
        self.assert_invalid(root)

    def test_03_adr0037_acceptance_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md", "Status: proposed", "Status: accepted")
        self.assert_invalid(root)

    def test_04_adr0033_acceptance_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "CURRENT_STATE.md", "ADR-0033: PROPOSED", "ADR-0033: ACCEPTED")
        self.assert_invalid(root)

    def test_05_p01_unpause_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "CURRENT_STATE.md", "P01: PAUSED", "P01: ACTIVE")
        self.assert_invalid(root)

    def test_06_physical_collection_start_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "CURRENT_STATE.md", "physical-host collection: NOT STARTED", "physical-host collection: STARTED")
        self.assert_invalid(root)

    def test_07_provisional_commit_removed_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/P01-ADR-0033-PROOF-CANDIDATE-SELECTION.md", "provisional", "final")
        self.assert_invalid(root)

    def test_08_new_core_entity_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"]["new_core_entity_required"] = True
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_09_contract_reopen_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"]["frozen_contract_reopen_required"] = True
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_10_capability_count_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"]["mechanical_capability_count"] = 21
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_11_mapping_count_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"]["mapping_count"] = 27
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_12_fixture_count_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"]["fixture_count"] = 19
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_13_source_merge_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "23dc4b19a0189ba55e08dfa124761efa806bd68b", "0" * 40)
        self.assert_invalid(root)

    def test_14_effect_class_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "external_side_effect", "external_effect_removed")
        self.assert_invalid(root)

    def test_15_availability_state_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "mounted_read_only", "mounted_unknown")
        self.assert_invalid(root)

    def test_16_result_state_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "partially_completed", "partial_removed")
        self.assert_invalid(root)

    def test_17_schedule_kind_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "condition_watch", "condition_removed")
        self.assert_invalid(root)

    def test_18_timing_mode_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "flexible_window", "window_removed")
        self.assert_invalid(root)

    def test_19_master_plan_profile_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "MASTER_PLAN.md", "### 6.6 Deep Workspace operations profile", "### removed profile")
        self.assert_invalid(root)

    def test_20_operational_truth_principle_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "MASTER_PLAN.md", "Operational truth must be explicit", "Operational truth may be implicit")
        self.assert_invalid(root)

    def test_21_roadmap_package_mapping_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "IMPLEMENTATION_ROADMAP.md", "## A14 amendment", "## removed amendment")
        self.assert_invalid(root)

    def test_22_cross_track_mapping_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "IMPLEMENTATION_ROADMAP.md", "**X5:**", "**removed-track:**")
        self.assert_invalid(root)

    def test_23_universal_gate_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "IMPLEMENTATION_ROADMAP.md", "operation effect class, exact precondition", "generic operation metadata")
        self.assert_invalid(root)

    def test_24_permission_grant_approval_collapse_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md", "Provider access, Ptah Grant and human/application approval remain separate", "All approval layers are one state")
        self.assert_invalid(root)

    def test_25_retry_history_removed_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "planning/DEEP-WORKSPACE-DONOR-ROADMAP-RECONCILIATION.md", "Retry creates a new Attempt", "Retry overwrites the Attempt")
        self.assert_invalid(root)

    def test_26_view_authority_boundary_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "IMPLEMENTATION_ROADMAP.md", "View style never creates authority", "View style creates authority")
        self.assert_invalid(root)

    def test_27_ptah_authority_drift_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "decisions/ADR-0037-DEEP-WORKSPACE-OPERATIONS-ROADMAP-RECONCILIATION.md", "choose the caller's job", "choose and prioritize the caller's job")
        self.assert_invalid(root)

    def test_28_active_work_unit_fails(self) -> None:
        root = self.copy_candidate()
        data = json.loads((root / "master-plan-index.json").read_text(encoding="utf-8"))
        data["active_work_unit"] = "P01-physical-host"
        (root / "master-plan-index.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_29_handoff_pause_removed_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "AI_HANDOFF.md", "P01: PAUSED", "P01: ACTIVE")
        self.assert_invalid(root)

    def test_30_candidate_marker_removed_fails(self) -> None:
        root = self.copy_candidate()
        self.mutate(root, "CURRENT_STATE.md", checker.MARKER, "REMOVED-MARKER")
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
