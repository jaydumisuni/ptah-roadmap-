#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_a03_acceptance_current_authority as checker


class A03AcceptanceInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="a03-acceptance-invariant-"))
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        for rel in checker.REQUIRED_FILES:
            src = self.source / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return root

    def mutate_index(self, root: Path, path: tuple[str, ...], value: object) -> None:
        target = root / "master-plan-index-amendment-2026-08-15.json"
        data = json.loads(target.read_text(encoding="utf-8"))
        cursor = data
        for key in path[:-1]:
            cursor = cursor[key]
        cursor[path[-1]] = value
        target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def replace(self, root: Path, rel: str, old: str, new: str) -> None:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_current_a03_acceptance_invariant_passes(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "a03_acceptance_invariant_valid")
        self.assertTrue(report["a03_complete"])
        self.assertTrue(report["ledger_runtime_proven"])

    def test_02_candidate_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "candidate_exact_head"), "0" * 40)
        self.invalid(root)

    def test_03_merge_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "merge_commit"), "0" * 40)
        self.invalid(root)

    def test_04_receipt_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "physical_proof_receipt"), "wrong")
        self.invalid(root)

    def test_05_proof_digest_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "physical_proof_manifest_sha256"), "0" * 64)
        self.invalid(root)

    def test_06_test_count_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "crash_recovery_tests_passed"), 3)
        self.invalid(root)

    def test_07_sergeant_finding_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "sergeant_admitted_findings"), 1)
        self.invalid(root)

    def test_08_ledger_proof_loss_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "ledger_runtime_proven"), False)
        self.invalid(root)

    def test_09_prime_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "prime_deployment_qualified"), True)
        self.invalid(root)

    def test_10_p01p_false_completion_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "P01P"), "accepted_complete")
        self.invalid(root)

    def test_11_historical_a04_nonclaim_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a03", "a04_activity_execution_implemented"), True)
        self.invalid(root)

    def test_12_runtime_proof_route_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(
            root,
            "planning/A03-LEDGER-SCHEMA-MIGRATIONS-ACCEPTANCE.md",
            "A03-specific GitHub Actions runtime-proof workflows were removed before freeze",
            "A03-specific GitHub Actions runtime-proof workflows were used for proof",
        )
        self.invalid(root)

    def test_13_later_a04_completion_does_not_falsify_a03(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "A04"), "accepted_complete")
        self.mutate_index(root, ("claim_boundaries", "activity_runtime_proven"), True)
        report = checker.validate(root)
        self.assertEqual(report["status"], "a03_acceptance_invariant_valid")


if __name__ == "__main__":
    unittest.main(verbosity=2)
