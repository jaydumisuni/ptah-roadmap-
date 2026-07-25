#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_phase0c19_handoff_authority as checker


class Phase0C19HandoffAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="phase0c19-handoff-"))
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

    def mutate_phase(self, root: Path, key: str, value: object) -> None:
        path = root / "master-plan-index.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["phase0c19_deep_workspace_reconciliation"][key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_valid_current_handoff(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "current_handoff_authority_valid_non_authorizing")
        self.assertEqual(report["master_plan_version"], "1.1.0")
        self.assertTrue(report["p01_active"])
        self.assertFalse(report["runtime_implementation_authorized"])

    def test_02_stale_date_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "Last updated: 2026-07-25", "Last updated: 2026-07-24"); self.invalid(root)

    def test_03_ambiguous_authority_heading_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "## Current accepted planning authority", "## Accepted planning authority"); self.invalid(root)

    def test_04_current_master_plan_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "Master Plan version: `1.1.0`", "Master Plan version: `1.0.0`"); self.invalid(root)

    def test_05_current_roadmap_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "implementation roadmap version: `1.1.0`", "implementation roadmap version: `1.0.0`"); self.invalid(root)

    def test_06_adr0037_proposed_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "ADR-0037 — ACCEPTED", "ADR-0037 — PROPOSED"); self.invalid(root)

    def test_07_phase0c19_incomplete_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "Phase 0C-19 — COMPLETE", "Phase 0C-19 — CANDIDATE"); self.invalid(root)

    def test_08_stale_proposed_reading_entry_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", "3. accepted ADR-0037;", "3. proposed ADR-0037;"); self.invalid(root)

    def test_09_binding_missing_from_read_order_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", f"6. `{checker.BINDING}`", "6. `missing-binding.md`"); self.invalid(root)

    def test_10_binding_after_physical_closure_fails(self) -> None:
        root = self.copy_state(); path = root / "AI_HANDOFF.md"; content = path.read_text(encoding="utf-8"); a = f"6. `{checker.BINDING}`"; b = "9. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`"; self.assertIn(a, content); self.assertIn(b, content); content = content.replace(a, "6. `planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md`", 1).replace(b, f"9. `{checker.BINDING}`", 1); path.write_text(content, encoding="utf-8"); self.invalid(root)

    def test_11_acceptance_merge_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.ACCEPTANCE_MERGE, "0" * 40); self.invalid(root)

    def test_12_binding_head_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.BINDING_HEAD, "0" * 40); self.invalid(root)

    def test_13_binding_run_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.BINDING_RUN, "0"); self.invalid(root)

    def test_14_binding_artifact_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.BINDING_ARTIFACT, "0"); self.invalid(root)

    def test_15_binding_merge_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.BINDING_MERGE, "0" * 40); self.invalid(root)

    def test_16_proof_commit_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "AI_HANDOFF.md", checker.PROOF_COMMIT, "0" * 40); self.invalid(root)

    def test_17_physical_collection_start_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "physical-host collection: NOT STARTED", "physical-host collection: STARTED"); self.invalid(root)

    def test_18_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "ADR-0033: PROPOSED", "ADR-0033: ACCEPTED"); self.invalid(root)

    def test_19_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED"); self.invalid(root)

    def test_20_machine_accepted_proof_pending_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "accepted_state_proof_pending", True); self.invalid(root)

    def test_21_machine_operative_merge_pending_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "operative_acceptance_merge_pending", True); self.invalid(root)

    def test_22_machine_acceptance_merge_drift_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "operative_acceptance_merge", "0" * 40); self.invalid(root)

    def test_23_machine_binding_path_drift_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "operative_binding", "planning/missing.md"); self.invalid(root)

    def test_24_machine_proof_commit_drift_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "confirmed_proof_commit", "0" * 40); self.invalid(root)

    def test_25_machine_physical_start_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "physical_host_collection_started", True); self.invalid(root)

    def test_26_machine_adr0033_acceptance_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "adr_0033_accepted", True); self.invalid(root)

    def test_27_machine_runtime_authorization_fails(self) -> None:
        root = self.copy_state(); self.mutate_phase(root, "runtime_implementation_authorized", True); self.invalid(root)

    def test_28_master_plan_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "MASTER_PLAN.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_29_roadmap_version_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, "IMPLEMENTATION_ROADMAP.md", "Version: 1.1.0", "Version: 1.0.0"); self.invalid(root)

    def test_30_binding_status_drift_fails(self) -> None:
        root = self.copy_state(); self.replace(root, checker.BINDING, "Status: OPERATIVE ACCEPTANCE BOUND", "Status: PENDING"); self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
