#!/usr/bin/env python3
"""Adversarial regressions for Campaign 001 AF01 archive closure."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_archive_af01 import (
    ACCEPTANCE,
    ADR0033,
    CHECKPOINT_05,
    CHECKPOINT_10,
    CURRENT_STATE,
    DONOR_REGISTER,
    EXPECTED,
    MANIFEST,
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
    ACCEPTANCE,
    MANIFEST,
    DONOR_REGISTER,
    CURRENT_STATE,
    ADR0033,
    *(Path(record["path"]) for record in EXPECTED.values()),
)


class AF01ValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-af01-"))
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

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_accepted_closure(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "accepted_complete_valid_non_authorizing")
        self.assertEqual(result["record_count"], 10)
        self.assertEqual(result["accepted_archive_record_count"], 9)
        self.assertEqual(result["blocked_record_count"], 1)
        self.assertTrue(result["af02_ready"])
        self.assertFalse(result["af02_started"])
        self.assertFalse(result["af02_authorized"])

    def test_record_file_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / EXPECTED["D001"]["path"]).unlink()
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
        self.mutate_result(root, lambda value: value["records"][3].__setitem__("branch", "main"))
        self.assert_invalid(root)

    def test_primary_worker_cannot_reuse(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][1].__setitem__("primary", "AF01-P01"))
        self.assert_invalid(root)

    def test_verifier_worker_cannot_reuse(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][1].__setitem__("verifier", "AF01-V01"))
        self.assert_invalid(root)

    def test_primary_and_verifier_cannot_overlap(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][0].__setitem__("verifier", "AF01-P01"))
        self.assert_invalid(root)

    def test_accepted_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("accepted_archive_record_count", 10))
        self.assert_invalid(root)

    def test_blocked_count_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("blocked_record_count", 0))
        self.assert_invalid(root)

    def test_minirouter_cannot_be_silently_accepted(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value["records"][7].__setitem__("outcome", "accepted_for_archive"))
        self.assert_invalid(root)

    def test_minirouter_licence_block_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D047"]["path"])
        self.replace(root, path, "root `LICENSE`: not present", "root licence assumed")
        self.assert_invalid(root)

    def test_stf_security_warning_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D020"]["path"])
        self.replace(root, path, "little to no security/encryption", "strong security between all services")
        self.assert_invalid(root)

    def test_strix_target_authorization_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D058"]["path"])
        self.replace(root, path, "only owned or explicitly authorized targets", "any discovered target")
        self.assert_invalid(root)

    def test_sparkdistill_proof_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D051"]["path"])
        self.replace(root, path, "attestation proves bounded measured claims", "attestation proves universal truth")
        self.assert_invalid(root)

    def test_checkpoint_05_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / CHECKPOINT_05).unlink()
        self.assert_invalid(root)

    def test_checkpoint_10_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / CHECKPOINT_10).unlink()
        self.assert_invalid(root)

    def test_af02_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("af02_authorized", True))
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

    def test_remaining_evidence_cannot_reappear(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("remaining_evidence_count", 1))
        self.assert_invalid(root)

    def test_accepted_status_cannot_revert_to_candidate(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("status", "candidate_complete_pending_exact_head_review"))
        self.assert_invalid(root)

    def test_acceptance_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / ACCEPTANCE).unlink()
        self.assert_invalid(root)

    def test_af02_ready_cannot_be_removed(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("af02_ready", False))
        self.assert_invalid(root)

    def test_af02_cannot_start_during_af01_acceptance(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, lambda value: value.__setitem__("af02_started", True))
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
