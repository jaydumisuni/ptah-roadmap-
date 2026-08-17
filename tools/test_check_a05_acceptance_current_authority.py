#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

import check_a05_acceptance_current_authority as checker


class A05AcceptanceAuthorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source = Path(__file__).resolve().parents[1]

    def copy_state(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="a05-acceptance-authority-"))
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

    def test_01_current_a05_acceptance_passes(self) -> None:
        report = checker.validate(self.copy_state())
        self.assertEqual(report["status"], "a05_accepted_complete_a06_ready")
        self.assertTrue(report["a05_complete"])
        self.assertTrue(report["a06_ready"])
        self.assertTrue(report["native_process_pty_runtime_proven"])
        self.assertFalse(report["workspace_runtime_proven"])
        self.assertEqual(report["tenfold_private_lanes"], 150)

    def test_02_candidate_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "candidate_exact_head"), "0" * 40)
        self.invalid(root)

    def test_03_merge_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "merge_commit"), "0" * 40)
        self.invalid(root)

    def test_04_proof_receipt_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "frozen_exact_head_proof_receipt"), "wrong")
        self.invalid(root)

    def test_05_sergeant_digest_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "sergeant_review_packet_sha256"), "0" * 64)
        self.invalid(root)

    def test_06_portable_pty_checksum_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "portable_pty_checksum"), "0" * 64)
        self.invalid(root)

    def test_07_tenfold_lane_drift_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "tenfold_private_lanes"), 20)
        self.invalid(root)

    def test_08_native_process_proof_loss_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "native_process_pty_runtime_proven"), False)
        self.invalid(root)

    def test_09_a06_not_ready_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "A06"), "blocked")
        self.invalid(root)

    def test_10_wrong_active_work_unit_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("active_work_unit",), "A05-native-process-pty-multi-terminal-provider")
        self.invalid(root)

    def test_11_p01p_false_completion_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("programmes", "P01P"), "accepted_complete")
        self.invalid(root)

    def test_12_prime_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "prime_deployment_qualified"), True)
        self.invalid(root)

    def test_13_production_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "production_authorized"), True)
        self.invalid(root)

    def test_14_ai_handoff_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(root, "AI_START_HERE.md", "A06 status: **READY**", "A06 status: **BLOCKED**")
        self.invalid(root)

    def test_15_runtime_proof_route_drift_fails(self) -> None:
        root = self.copy_state()
        self.replace(
            root,
            "planning/A05-NATIVE-PROCESS-PTY-PROVIDER-ACCEPTANCE.md",
            "GitHub Actions are **not** the A05 runtime execution or proof authority",
            "GitHub Actions are the A05 runtime execution and proof authority",
        )
        self.invalid(root)

    def test_16_a04_historical_nonclaim_rewrite_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a04", "a05_native_process_pty_implemented"), True)
        self.invalid(root)

    def test_17_a05_false_a06_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("a05", "a06_workspace_session_implemented"), True)
        self.invalid(root)

    def test_18_workspace_false_proof_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "workspace_runtime_proven"), True)
        self.invalid(root)

    def test_19_release_false_claim_fails(self) -> None:
        root = self.copy_state()
        self.mutate_index(root, ("claim_boundaries", "release_accepted"), True)
        self.invalid(root)


if __name__ == "__main__":
    unittest.main(verbosity=2)
