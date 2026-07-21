#!/usr/bin/env python3
"""Adversarial regressions for Campaign 001 AF02 candidate closure."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_archive_af02 import (
    ADR0033,
    CHECKPOINT_05,
    CHECKPOINT_10,
    CURRENT_STATE,
    DONOR_REGISTER,
    EXPECTED,
    MANIFEST,
    MASTER_INDEX,
    MISSION,
    RESULT_JSON,
    RESULT_MD,
    ValidationError,
    validate_repo,
)

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    MISSION,
    CHECKPOINT_05,
    CHECKPOINT_10,
    RESULT_JSON,
    RESULT_MD,
    MANIFEST,
    DONOR_REGISTER,
    CURRENT_STATE,
    MASTER_INDEX,
    ADR0033,
    *(Path(record["path"]) for record in EXPECTED.values()),
)


class AF02ValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-af02-"))
        self.addCleanup(lambda: shutil.rmtree(temporary, ignore_errors=True))
        for relative in REQUIRED:
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

    def mutate_result(self, root: Path, mutator) -> None:
        path = root / RESULT_JSON
        value = json.loads(path.read_text(encoding="utf-8"))
        mutator(value)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def mutate_index(self, root: Path, mutator) -> None:
        path = root / MASTER_INDEX
        value = json.loads(path.read_text(encoding="utf-8"))
        archive = value["operational_protocols"]["tenfold_archive_formation"]
        mutator(archive)
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_candidate_closure(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")
        self.assertEqual(result["record_count"], 10)
        self.assertEqual(result["accepted_archive_record_count"], 10)
        self.assertEqual(result["blocked_record_count"], 0)
        self.assertEqual(result["remaining_evidence_count"], 0)
        self.assertFalse(result["af03_authorized"])

    def test_record_file_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / EXPECTED["D062"]["path"]).unlink()
        self.assert_invalid(root)

    def test_record_id_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"].pop())
        self.assert_invalid(root)

    def test_record_id_cannot_duplicate(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"].__setitem__(1, dict(value["records"][0])))
        self.assert_invalid(root)

    def test_exact_source_commit_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][0].__setitem__("commit", "0" * 40))
        self.assert_invalid(root)

    def test_default_branch_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][5].__setitem__("branch", "main"))
        self.assert_invalid(root)

    def test_outcome_cannot_be_broadened(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][2].__setitem__("outcome", "accepted_for_archive"))
        self.assert_invalid(root)

    def test_primary_worker_cannot_reuse(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][1].__setitem__("primary", "AF02-P01"))
        self.assert_invalid(root)

    def test_verifier_worker_cannot_reuse(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][1].__setitem__("verifier", "AF02-V01"))
        self.assert_invalid(root)

    def test_primary_and_verifier_cannot_overlap(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][0].__setitem__("verifier", "AF02-P01"))
        self.assert_invalid(root)

    def test_accepted_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("accepted_archive_record_count", 9))
        self.assert_invalid(root)

    def test_blocked_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("blocked_record_count", 1))
        self.assert_invalid(root)

    def test_remaining_evidence_cannot_reappear(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("remaining_evidence_count", 1))
        self.assert_invalid(root)

    def test_checkpoint_05_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / CHECKPOINT_05).unlink()
        self.assert_invalid(root)

    def test_checkpoint_10_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / CHECKPOINT_10).unlink()
        self.assert_invalid(root)

    def test_candidate_state_cannot_revert_to_active(self) -> None:
        root = self.make_repo()
        self.replace(root, MISSION, "Status: CANDIDATE COMPLETE", "Status: ACTIVE")
        self.assert_invalid(root)

    def test_daytona_discontinuation_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D002"]["path"])
        self.replace(root, path, "public core development stopped in June 2026", "public core development continues")
        self.assert_invalid(root)

    def test_daytona_snapshot_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D002"]["path"])
        self.replace(root, path, "v0.190.0", "latest hosted release")
        self.assert_invalid(root)

    def test_daytona_copyleft_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D002"]["path"])
        self.replace(root, path, "AGPL-3.0", "permissive licence")
        self.assert_invalid(root)

    def test_adbkit_server_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D021"]["path"])
        self.replace(root, path, "not an ADB server", "complete ADB server")
        self.assert_invalid(root)

    def test_adbkit_authorization_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D021"]["path"])
        self.replace(root, path, "explicit device/customer authorization", "implicit device access")
        self.assert_invalid(root)

    def test_moby_library_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D036"]["path"])
        self.replace(root, path, "not intended as an imported Go library", "stable imported Go library")
        self.assert_invalid(root)

    def test_llama_integration_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D043"]["path"])
        self.replace(root, path, "more than 300 separately packaged integrations", "one uniform trusted integration")
        self.assert_invalid(root)

    def test_llama_truth_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D043"]["path"])
        self.replace(root, path, "cannot automatically become canonical Ptah Object/Knowledge truth", "becomes canonical Ptah truth")
        self.assert_invalid(root)

    def test_ray_scheduler_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D048"]["path"])
        self.replace(root, path, "must not become Ptah's global scheduler", "becomes Ptah's global scheduler")
        self.assert_invalid(root)

    def test_catalogue_linked_rights_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D062"]["path"])
        self.replace(root, path, "CC0 applies to the catalogue work", "CC0 applies to every linked work")
        self.assert_invalid(root)

    def test_control_book_cannot_preaccept_af02(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, lambda archive: archive.__setitem__("af02_accepted_archive_record_count", 10))
        self.assert_invalid(root)

    def test_af03_cannot_start(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, lambda archive: archive.__setitem__("af03_started", True))
        self.assert_invalid(root)

    def test_af03_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("af03_authorized", True))
        self.assert_invalid(root)

    def test_phase_0a_cannot_reopen(self) -> None:
        root = self.make_repo()
        self.replace(root, DONOR_REGISTER, "**Status:** COMPLETE AND FROZEN", "**Status:** REOPENED")
        self.assert_invalid(root)

    def test_adr0033_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.replace(root, ADR0033, "Status: proposed", "Status: accepted")
        self.assert_invalid(root)

    def test_runtime_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            CURRENT_STATE,
            "**Runtime implementation:** NOT AUTHORIZED",
            "**Runtime implementation:** AUTHORIZED",
        )
        self.assert_invalid(root)

    def test_manifest_pair_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, MANIFEST, "`AF02-P01` | `AF02-V01`", "`AF02-P01` | `AF02-V99`")
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
