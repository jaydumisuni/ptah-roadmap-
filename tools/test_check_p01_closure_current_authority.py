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
        root = Path(tempfile.mkdtemp(prefix="p01d-closure-authority-"))
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

    def mutate_index(self, root: Path, path: tuple[str, ...], value: object) -> None:
        target = root / "master-plan-index-amendment-2026-08-15.json"
        data = json.loads(target.read_text(encoding="utf-8"))
        cursor = data
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_current_closure_passes(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "current_authority_valid_p01d_accepted_a01_authorized")
        self.assertTrue(report["p01d_accepted"])
        self.assertTrue(report["runtime_implementation_authorized"])
        self.assertTrue(report["a01_ready"])
        self.assertTrue(report["p01p_open"])
        self.assertFalse(report["prime_native_integration_qualified"])

    def test_02_wrong_final_proof_commit_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[0], checker.PROOF_COMMIT, "0" * 40)
        self.invalid(root)

    def test_03_wrong_report_digest_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01d", "public_report_sha256"), "0" * 64)
        self.invalid(root)

    def test_04_missing_negative_evidence_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01d", "negative_evidence_retained"), False)
        self.invalid(root)

    def test_05_oracle_receipt_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01d", "oracle_live_receipt_blob_sha"), "0" * 40)
        self.invalid(root)

    def test_06_runtime_deauthorization_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("runtime_implementation_authorized",), False)
        self.invalid(root)

    def test_07_a01_not_ready_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("active_work_unit",), "P01D")
        self.invalid(root)

    def test_08_p01p_false_acceptance_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01p", "prime_native_integration_qualified"), True)
        self.invalid(root)

    def test_09_historical_ubuntu_false_pass_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("adr_0033", "historical_exact_ubuntu_proof_passed"), True)
        self.invalid(root)

    def test_10_production_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "production_authorized"), True)
        self.invalid(root)

    def test_11_ai_start_state_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "AI_START_HERE.md", "Runtime implementation: **AUTHORIZED**", "Runtime implementation: **NOT AUTHORIZED**")
        self.invalid(root)

    def test_12_adr0039_authorization_removal_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, checker.REQUIRED_FILES[4], "Accept P01D and explicitly authorize A01 runtime implementation.", "P01D remains open.")
        self.invalid(root)

    def test_13_git_fallback_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01d", "github_interactive_path_used"), True)
        self.invalid(root)

    def test_14_required_actions_reintroduced_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01d", "independent_review_required_actions"), ["review again"])
        self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
