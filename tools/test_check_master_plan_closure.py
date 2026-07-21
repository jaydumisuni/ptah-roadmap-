#!/usr/bin/env python3
"""Adversarial tests for the Phase 0C-16 Master Plan closure validator."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_master_plan_closure import ClosureError, validate

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "README.md",
    "AI_HANDOFF.md",
    "CURRENT_STATE.md",
    "MASTER_PLAN.md",
    "IMPLEMENTATION_ROADMAP.md",
    "MASTER_ROADMAP.md",
    "PROGRESS.md",
    "DECISIONS.md",
    "MEMORY_PROTOCOL.md",
    "DONOR_RECOVERY.md",
    "master-plan-index.json",
    "planning/REQUIREMENTS-AND-DECISIONS-RECOVERY.md",
    "planning/MASTER-PLAN-RECONCILIATION.md",
    "planning/PHYSICAL-HOST-TO-AUTHORIZATION-CLOSURE.md",
    "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md",
    "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md",
    "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",
]


class MasterPlanClosureTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = Path(tempfile.mkdtemp(prefix="ptah-master-plan-test-"))
        self.addCleanup(shutil.rmtree, temp, ignore_errors=True)
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            target = temp / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        return temp

    @staticmethod
    def replace(path: Path, old: str, new: str) -> None:
        text = path.read_text(encoding="utf-8")
        if old not in text:
            raise AssertionError(f"test mutation source missing: {old}")
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ClosureError):
            validate(root)

    def test_valid_candidate_passes(self) -> None:
        report = validate(self.make_repo())
        self.assertEqual(report["status"], "candidate_valid_non_authorizing")
        self.assertFalse(report["runtime_implementation_authorized"])
        self.assertEqual(report["programme_a_package_count"], 15)

    def test_machine_index_cannot_authorize_runtime(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["runtime_implementation_authorized"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_current_state_rejects_flattened_proof_command(self) -> None:
        root = self.make_repo()
        path = root / "CURRENT_STATE.md"
        self.replace(
            path,
            "python3 tools/run_pinned_host_proof.py \\\n  --repo-root . \\\n  --output evidence/phase0c/pinned-host-candidate",
            "python3 tools/run_pinned_host_proof.py --repo-root . --output evidence/phase0c/pinned-host-candidate",
        )
        self.assert_invalid(root)

    def test_roadmap_requires_complete_programme_a(self) -> None:
        root = self.make_repo()
        path = root / "IMPLEMENTATION_ROADMAP.md"
        self.replace(path, "## A15 — Exact-head Online Ptah Alpha acceptance", "## AX15 — removed acceptance")
        self.assert_invalid(root)

    def test_reconciliation_requires_wp14(self) -> None:
        root = self.make_repo()
        path = root / "planning/MASTER-PLAN-RECONCILIATION.md"
        path.write_text(path.read_text(encoding="utf-8").replace("WP14", "WPXIV"), encoding="utf-8")
        self.assert_invalid(root)

    def test_adr0033_must_remain_proposed(self) -> None:
        root = self.make_repo()
        path = root / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"
        self.replace(path, "Status: proposed", "Status: accepted")
        self.assert_invalid(root)

    def test_memory_protocol_requires_unique_numbered_headings(self) -> None:
        root = self.make_repo()
        path = root / "MEMORY_PROTOCOL.md"
        self.replace(path, "# 6. Completion language", "# 11. Completion language")
        self.assert_invalid(root)

    def test_exact_kernel_target_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["physical_host_target"]["kernel"] = "6.8.0-999-generic"
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_master_plan_requires_owner_and_agent_roles(self) -> None:
        root = self.make_repo()
        path = root / "MASTER_PLAN.md"
        self.replace(path, "### 5.5 Hunter", "### 5.5 Coordinator")
        self.assert_invalid(root)

    def test_handoff_cannot_claim_authorization(self) -> None:
        root = self.make_repo()
        path = root / "AI_HANDOFF.md"
        self.replace(path, "Runtime implementation: NOT AUTHORIZED", "Runtime implementation: AUTHORIZED")
        self.assert_invalid(root)

    def test_adr0034_requires_save_as_you_go_authority(self) -> None:
        root = self.make_repo()
        path = root / "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md"
        self.replace(path, "## Save-as-you-go rule", "## Temporary notes")
        self.assert_invalid(root)

    def test_missing_required_file_fails(self) -> None:
        root = self.make_repo()
        (root / "MASTER_PLAN.md").unlink()
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
