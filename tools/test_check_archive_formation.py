#!/usr/bin/env python3
"""Adversarial regressions for the Ptah tenfold archive formation validator."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_archive_formation import REQUIRED_FILES, ValidationError, validate_repo

ROOT = Path(__file__).resolve().parents[1]


class ArchiveFormationValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-archive-formation-"))
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

    def remove_line_containing(self, root: Path, relative: Path, token: str) -> None:
        path = root / relative
        lines = path.read_text(encoding="utf-8").splitlines()
        self.assertTrue(any(token in line for line in lines))
        path.write_text("\n".join(line for line in lines if token not in line) + "\n", encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_accepted_campaign_progress(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "accepted_valid_non_authorizing")
        self.assertEqual(result["assigned_record_count"], 98)
        self.assertEqual(result["allocated_private_count"], 200)
        self.assertTrue(result["authority_sync_complete"])
        self.assertEqual(result["accepted_archive_record_count"], 9)
        self.assertEqual(result["blocked_archive_record_count"], 1)
        self.assertEqual(result["completed_formation_count"], 1)
        self.assertEqual(result["af01_status"], "accepted_complete")
        self.assertEqual(result["af02_status"], "ready_not_started")
        self.assertFalse(result["af02_started"])
        self.assertFalse(result["af02_authorized"])
        self.assertFalse(result["runtime_implementation_authorized"])

    def test_sergeant_pin_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md"),
            "44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd",
            "0000000000000000000000000000000000000000",
        )
        self.assert_invalid(root)

    def test_force_multiplier_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md"),
            "human-equivalent workers × 10",
            "human-equivalent workers × 9",
        )
        self.assert_invalid(root)

    def test_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.remove_line_containing(root, Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"), "`D001`")
        self.assert_invalid(root)

    def test_record_cannot_be_duplicated(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "| `D002` | DAYTONA",
            "| `D001` | DAYTONA",
        )
        self.assert_invalid(root)

    def test_primary_worker_cannot_be_reused(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "`AF02-P03`",
            "`AF01-P01`",
        )
        self.assert_invalid(root)

    def test_verifier_worker_cannot_be_reused(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "`AF02-V03`",
            "`AF01-V01`",
        )
        self.assert_invalid(root)

    def test_reserve_pair_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = root / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
        text = path.read_text(encoding="utf-8")
        reserve = "| reserve | overflow/complexity escalation | reserve | `AF10-P09` | `AF10-V09` |\n"
        self.assertIn(reserve, text)
        path.write_text(text.replace(reserve, "", 1), encoding="utf-8")
        self.assert_invalid(root)

    def test_formation_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"), "## AF06", "## ARCHIVE-SIX")
        self.assert_invalid(root)

    def test_private_verdict_authority_cannot_appear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "private verdict authority: none",
            "private verdict authority: allowed",
        )
        self.assert_invalid(root)

    def test_phase_0a_cannot_reopen(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("DONOR_RECOVERY.md"),
            "**Status:** COMPLETE AND FROZEN",
            "**Status:** REOPENED",
        )
        self.assert_invalid(root)

    def test_adr0033_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        path = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")
        text = (root / path).read_text(encoding="utf-8")
        self.assertIn("Status: proposed", text)
        (root / path).write_text(text.replace("Status: proposed", "Status: accepted", 1), encoding="utf-8")
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

    def test_save_after_five_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md"),
            "after every five reconciled records",
            "after an unspecified amount of work",
        )
        self.assert_invalid(root)

    def test_allocated_private_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md"),
            "allocated privates: 200",
            "allocated privates: 20",
        )
        self.assert_invalid(root)

    def test_memory_protocol_rule_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("MEMORY_PROTOCOL.md"),
            "## 5.1 Tenfold archive formation rule",
            "## 5.1 Ordinary sequential archive rule",
        )
        self.assert_invalid(root)

    def test_handoff_cannot_replace_p01(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("AI_HANDOFF.md"),
            "P01 physical-host closure remains the exact next authorization action",
            "archive formation replaces P01 as the authorization action",
        )
        self.assert_invalid(root)

    def test_decision_index_entry_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("DECISIONS.md"),
            "### D-051 — Tenfold archive formation separates parallel evidence from promotion authority",
            "### Archive idea without decision authority",
        )
        self.assert_invalid(root)

    def test_machine_index_active_work_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["active_work_unit"] = "archive-formation-replaces-physical-host"
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_machine_index_private_count_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["operational_protocols"]["tenfold_archive_formation"]["allocated_private_count"] = 20
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_donor_register_archive_rule_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("DONOR_RECOVERY.md"),
            "## 2A. Tenfold archival-completeness rule",
            "## 2A. Untracked archive notes",
        )
        self.assert_invalid(root)


    def test_accepted_adr0035_cannot_revert(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md"),
            "Status: accepted",
            "Status: proposed",
        )
        self.assert_invalid(root)

    def test_af01_accepted_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("master-plan-index.json"),
            '"accepted_archive_record_count": 9',
            '"accepted_archive_record_count": 10',
        )
        self.assert_invalid(root)

    def test_af01_acceptance_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / "archive/campaign-001/af01/ACCEPTANCE.md").unlink()
        self.assert_invalid(root)

    def test_af02_cannot_start_implicitly(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["operational_protocols"]["tenfold_archive_formation"]["af02_started"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

if __name__ == "__main__":
    unittest.main()
