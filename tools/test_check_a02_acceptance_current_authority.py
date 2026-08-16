#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_a02_acceptance_current_authority as checker


class A02AcceptanceInvariantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="a02-acceptance-invariant-"))
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

    def invalid(self, root: Path) -> None:
        with self.assertRaises(checker.ValidationError):
            checker.validate(root)

    def test_01_a02_invariant_passes_after_a03_progress(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "a02_accepted_complete")
        self.assertTrue(report["a02_complete"])
        self.assertTrue(report["node_runtime_proven"])

    def test_02_candidate_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a02", "candidate_exact_head"), "0" * 40)
        self.invalid(root)

    def test_03_merge_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a02", "merge_commit"), "0" * 40)
        self.invalid(root)

    def test_04_artifact_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a02", "proof_artifact_id"), 0)
        self.invalid(root)

    def test_05_node_proof_loss_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "node_runtime_proven"), False)
        self.invalid(root)

    def test_06_a02_completion_loss_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "A02"), "ready")
        self.invalid(root)

    def test_07_p01p_boundary_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("p01p", "status"), "complete")
        self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
