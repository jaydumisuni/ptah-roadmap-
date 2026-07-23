#!/usr/bin/env python3
"""Adversarial regressions for the Campaign 001 AF03 validator."""
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check_archive_af03 import (
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
    SERGEANT_REVIEW,
    ValidationError,
    validate_repo,
)

ROOT = Path(__file__).resolve().parents[1]
BASE_FILES = (
    MISSION,
    CHECKPOINT_05,
    CHECKPOINT_10,
    RESULT_JSON,
    RESULT_MD,
    SERGEANT_REVIEW,
    MANIFEST,
    DONOR_REGISTER,
    CURRENT_STATE,
    MASTER_INDEX,
    ADR0033,
)


class AF03ValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temporary = Path(tempfile.mkdtemp(prefix="ptah-af03-"))
        self.addCleanup(lambda: shutil.rmtree(temporary, ignore_errors=True))
        paths = list(BASE_FILES) + [Path(value["path"]) for value in EXPECTED.values()]
        for relative in paths:
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

    def mutate_result(self, root: Path, key: str, value: object) -> None:
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data[key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def mutate_index(self, root: Path, key: str, value: object) -> None:
        path = root / MASTER_INDEX
        data = json.loads(path.read_text(encoding="utf-8"))
        data["operational_protocols"]["tenfold_archive_formation"][key] = value
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def assert_invalid(self, root: Path) -> None:
        with self.assertRaises(ValidationError):
            validate_repo(root)

    def test_valid_candidate(self) -> None:
        result = validate_repo(self.make_repo())
        self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")
        self.assertEqual(result["candidate_archive_outcome_count"], 10)
        self.assertEqual(result["sergeant_review_result"], "pass_with_mandatory_retained_restrictions")
        self.assertFalse(result["af03_accepted"])
        self.assertFalse(result["af04_started"])

    def test_missing_record_fails(self) -> None:
        root = self.make_repo()
        (root / Path(EXPECTED["D052"]["path"])).unlink()
        self.assert_invalid(root)

    def test_result_status_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "accepted_complete")
        self.assert_invalid(root)

    def test_record_count_cannot_drop(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"] = data["records"][:-1]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_record_order_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"][0], data["records"][1] = data["records"][1], data["records"][0]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_source_pin_cannot_drift(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"][4]["commit"] = "0" * 40
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_primary_worker_cannot_be_reused(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"][1]["primary"] = data["records"][0]["primary"]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_verifier_worker_cannot_be_reused(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"][1]["verifier"] = data["records"][0]["verifier"]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_primary_and_verifier_cannot_overlap(self) -> None:
        root = self.make_repo()
        path = root / RESULT_JSON
        data = json.loads(path.read_text(encoding="utf-8"))
        data["records"][0]["verifier"] = data["records"][0]["primary"]
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_sergeant_review_cannot_be_incomplete(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "sergeant_review_complete", False)
        self.assert_invalid(root)

    def test_sergeant_target_cannot_drift(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "sergeant_review_target_head", "0" * 40)
        self.assert_invalid(root)

    def test_sergeant_result_cannot_be_forged(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "sergeant_review_result", "pass")
        self.assert_invalid(root)

    def test_sergeant_blockers_cannot_be_hidden(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "sergeant_blocking_finding_count", 1)
        self.assert_invalid(root)

    def test_sergeant_independence_cannot_disappear(self) -> None:
        root = self.make_repo()
        self.replace(root, SERGEANT_REVIEW, "Sergeant did not participate in producing", "Sergeant participated in producing")
        self.assert_invalid(root)

    def test_sergeant_cannot_accept_af03(self) -> None:
        root = self.make_repo()
        self.replace(root, SERGEANT_REVIEW, "does not accept AF03", "accepts AF03")
        self.assert_invalid(root)

    def test_acceptance_record_cannot_appear(self) -> None:
        root = self.make_repo()
        path = root / "archive/campaign-001/af03/ACCEPTANCE.md"
        path.write_text("# premature acceptance\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_af04_cannot_start(self) -> None:
        root = self.make_repo()
        self.replace(root, MANIFEST, "## AF04\n\n- private count: 20", "## AF04\n\n- status: ACTIVE\n- private count: 20")
        self.assert_invalid(root)

    def test_phase0a_cannot_reopen(self) -> None:
        root = self.make_repo()
        self.replace(root, DONOR_REGISTER, "**Status:** COMPLETE AND FROZEN", "**Status:** REOPENED")
        self.assert_invalid(root)

    def test_adr0033_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.replace(root, ADR0033, "Status: proposed", "Status: accepted")
        self.assert_invalid(root)

    def test_runtime_cannot_be_authorized(self) -> None:
        root = self.make_repo()
        self.replace(root, CURRENT_STATE, "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED")
        self.assert_invalid(root)

    def test_operative_totals_cannot_be_promoted(self) -> None:
        root = self.make_repo()
        self.mutate_index(root, "accepted_archive_record_count", 29)
        self.assert_invalid(root)

    def test_d052_no_licence_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D052"]["path"])
        self.replace(root, path, "root `LICENSE`: absent", "root licence: MIT")
        self.assert_invalid(root)

    def test_d052_copy_restriction_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D052"]["path"])
        self.replace(root, path, "do not copy or adapt profile text", "copy profile text freely")
        self.assert_invalid(root)

    def test_d059_lgpl_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D059"]["path"])
        self.replace(root, path, "LGPL-2.1", "permissive")
        self.assert_invalid(root)

    def test_d059_finding_cannot_become_verdict(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D059"]["path"])
        self.replace(root, path, "do not treat findings as final vulnerability truth", "treat findings as final vulnerability truth")
        self.assert_invalid(root)

    def test_d063_upstream_proof_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D063"]["path"])
        self.replace(root, path, "exact upstream evidence", "profile statement")
        self.assert_invalid(root)

    def test_d067_build_cannot_equal_truth(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D067"]["path"])
        self.replace(root, path, "successful build as proof that documentation content is accurate or approved", "successful build proves documentation")
        self.assert_invalid(root)

    def test_d003_temporal_ids_cannot_become_canonical(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D003"]["path"])
        self.replace(root, path, "do not map Temporal Workflow or Activity IDs directly", "map Temporal IDs directly")
        self.assert_invalid(root)

    def test_d003_retry_cannot_equal_effect_proof(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D003"]["path"])
        self.replace(root, path, "do not treat retry completion", "treat retry completion")
        self.assert_invalid(root)

    def test_d014_agpl_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D014"]["path"])
        self.replace(root, path, "AGPL-3.0", "permissive")
        self.assert_invalid(root)

    def test_d018_hosted_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D018"]["path"])
        self.replace(root, path, "hosted Browser Use capabilities", "all Browser Use capabilities")
        self.assert_invalid(root)

    def test_d022_compatibility_cannot_be_overclaimed(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D022"]["path"])
        self.replace(root, path, "do not claim modern Android, emulator or universal-device compatibility", "claim universal compatibility")
        self.assert_invalid(root)

    def test_d032_kvm_boundary_cannot_disappear(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D032"]["path"])
        self.replace(root, path, "requires Linux KVM", "runs everywhere")
        self.assert_invalid(root)

    def test_d032_start_ack_cannot_equal_success(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D032"]["path"])
        self.replace(root, path, "do not treat API start acknowledgement as guest workload success", "API start proves guest success")
        self.assert_invalid(root)

    def test_d037_cli_cannot_become_engine(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D037"]["path"])
        self.replace(root, path, "not Docker Engine", "is Docker Engine")
        self.assert_invalid(root)

    def test_d037_cli_success_cannot_equal_workload_success(self) -> None:
        root = self.make_repo()
        path = Path(EXPECTED["D037"]["path"])
        self.replace(root, path, "do not treat CLI success as workload", "CLI success proves workload")
        self.assert_invalid(root)


if __name__ == "__main__":
    unittest.main()
