#!/usr/bin/env python3
"""Adversarial regressions for the Phase 0C-18 diagnostic advisory validator."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_platform_diagnostic_advisory import REQUIRED_FILES, ValidationError, validate_repo

ROOT = Path(__file__).resolve().parents[1]


class DiagnosticAdvisoryValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-diagnostic-advisory-"))
        self.addCleanup(lambda: shutil.rmtree(temporary, ignore_errors=True))
        for relative in REQUIRED_FILES:
            source = ROOT / relative
            destination = temporary / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        return temporary

    def replace(self, root: Path, relative: Path, old: str, new: str) -> None:
        path = root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_candidate(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "candidate_valid_non_authorizing")
        self.assertTrue(result["may_request_upgrade"])
        self.assertFalse(result["may_choose_caller_work"])
        self.assertFalse(result["may_install_upgrade_autonomously"])
        self.assertFalse(result["af03_started"])

    def test_protocol_cannot_become_consciousness_claim(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "platform self-observation, not product consciousness",
            "product self-awareness and consciousness",
        )
        self.assert_invalid(root)

    def test_caller_work_choice_cannot_move_to_ptah(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "Caller chooses the work",
            "Ptah chooses the work",
        )
        self.assert_invalid(root)

    def test_sergeant_review_authority_cannot_be_borrowed(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "Ptah does not borrow Sergeant's review authority",
            "Ptah borrows Sergeant's review authority",
        )
        self.assert_invalid(root)

    def test_new_core_entity_cannot_be_required(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "No new Core entity is required",
            "A new autonomous Core entity is required",
        )
        self.assert_invalid(root)

    def test_facts_and_suggestions_cannot_be_conflated(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "observed facts from suggestions",
            "observed facts and suggestions as one decision",
        )
        self.assert_invalid(root)

    def test_self_approval_prohibition_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "approve its own advisory",
            "automatically approve its own advisory",
        )
        self.assert_invalid(root)

    def test_autonomous_install_prohibition_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "install, upgrade, remove or replace software without configured authority",
            "install and replace software without asking",
        )
        self.assert_invalid(root)

    def test_unrelated_work_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "block unrelated work merely because an upgrade is available",
            "block all work whenever an upgrade is available",
        )
        self.assert_invalid(root)

    def test_acknowledgement_cannot_equal_resolution(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "acknowledgement does not equal successful upgrade",
            "acknowledgement equals successful upgrade",
        )
        self.assert_invalid(root)

    def test_master_plan_principle_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("MASTER_PLAN.md"),
            "Ptah may diagnose its own platform condition without choosing the caller's work",
            "Ptah may choose the caller's work",
        )
        self.assert_invalid(root)

    def test_master_plan_autonomous_upgrade_cannot_appear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("MASTER_PLAN.md"),
            "may not approve, purchase, install or activate it",
            "may approve, purchase, install and activate it",
        )
        self.assert_invalid(root)

    def test_roadmap_a02_cannot_lose_gap_advisory(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("IMPLEMENTATION_ROADMAP.md"),
            "bounded missing-capability and degradation advisory generation",
            "generic status message",
        )
        self.assert_invalid(root)

    def test_roadmap_a15_cannot_allow_autonomous_install(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("IMPLEMENTATION_ROADMAP.md"),
            "Ptah cannot choose caller work or autonomously install an upgrade",
            "Ptah can choose caller work and autonomously install an upgrade",
        )
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_work_choice(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["product_clarifications"]["platform_diagnostic_advisory"]["may_choose_caller_work"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_upgrade_approval(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["product_clarifications"]["platform_diagnostic_advisory"]["may_approve_upgrade"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_machine_index_cannot_grant_autonomous_install(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["product_clarifications"]["platform_diagnostic_advisory"]["may_install_upgrade_autonomously"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_machine_index_cannot_block_unrelated_work(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["product_clarifications"]["platform_diagnostic_advisory"]["may_block_unrelated_capable_work"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_af03_cannot_start(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "- status: READY / NOT STARTED",
            "- status: ACTIVE",
        )
        self.assert_invalid(root)

    def test_adr0033_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"),
            "Status: proposed",
            "Status: accepted",
        )
        self.assert_invalid(root)

    def test_runtime_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("CURRENT_STATE.md"),
            "**Runtime implementation:** NOT AUTHORIZED",
            "**Runtime implementation:** AUTHORIZED",
        )
        self.assert_invalid(root)

    def test_phase0a_cannot_reopen(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("DONOR_RECOVERY.md"),
            "**Status:** COMPLETE AND FROZEN",
            "**Status:** REOPENED",
        )
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
