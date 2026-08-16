#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_a01_acceptance_current_authority as checker


class A01AcceptanceAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="a01-acceptance-authority-"))
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

    def test_01_historical_a01_acceptance_passes_after_progression(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "a01_historical_checkpoint_valid")
        self.assertTrue(report["a01_complete"])
        self.assertTrue(report["a02_ready_at_a01_exit"])
        self.assertTrue(report["later_programme_progression_allowed"])
        self.assertFalse(report["node_runtime_proven_at_a01_exit"])

    def test_02_candidate_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a01", "candidate_exact_head"), "0" * 40)
        self.invalid(root)

    def test_03_merge_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a01", "merge_commit"), "0" * 40)
        self.invalid(root)

    def test_04_workflow_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a01", "workflow_run"), 0)
        self.invalid(root)

    def test_05_artifact_digest_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a01", "final_proof_artifact_digest"), "sha256:" + "0" * 64)
        self.invalid(root)

    def test_06_a01_not_complete_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "A01"), "active")
        self.invalid(root)

    def test_07_historical_a02_exit_not_ready_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "A02"), "blocked")
        self.invalid(root)

    def test_08_a01_checkpoint_node_runtime_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "node_runtime_proven"), True)
        self.invalid(root)

    def test_09_prime_qualification_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "prime_deployment_qualified"), True)
        self.invalid(root)

    def test_10_current_ai_recovery_may_advance_beyond_a02_ready(self) -> None:
        root = self.copy_state()
        text = (root / "AI_START_HERE.md").read_text(encoding="utf-8")
        self.assertIn("A03 status: **READY**", text)
        report = checker.validate(root)
        self.assertTrue(report["later_programme_progression_allowed"])

    def test_11_current_ai_recovery_cannot_drop_a01_completion(self) -> None:
        root = self.copy_state()
        self.replace(
            root,
            "AI_START_HERE.md",
            "A01 — Repository, contracts and reproducible scaffold: **FROZEN / PROVEN / COMPLETE**",
            "A01 — Repository, contracts and reproducible scaffold: **UNKNOWN**",
        )
        self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
