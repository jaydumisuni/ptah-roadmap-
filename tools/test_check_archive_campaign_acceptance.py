#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SPEC = importlib.util.spec_from_file_location("acceptance_validator", HERE / "check_archive_campaign_acceptance.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

class CampaignAcceptanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "conformance"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def validate(self):
        return MODULE.validate(self.root)

    def fail_after(self, mutation):
        mutation()
        with self.assertRaises(MODULE.ValidationError):
            self.validate()

    def edit_json(self, formation: str, fn) -> None:
        path = self.root / "archive/campaign-001" / formation / "RESULT.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        fn(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def edit_text(self, relative: str, old: str, new: str) -> None:
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_00_valid_acceptance_candidate(self):
        report = self.validate()
        self.assertEqual(report["status"], "campaign_acceptance_candidate_valid_non_authorizing")
        self.assertEqual(report["campaign_accepted_archive_record_count"], 91)
        self.assertEqual(report["campaign_blocked_record_count"], 7)
        self.assertFalse(report["global_control_state_bound"])

    def test_01_missing_campaign_acceptance_fails(self):
        self.fail_after(lambda: (self.root / "archive/campaign-001/ACCEPTANCE.md").unlink())

    def test_02_formation_not_promoted_fails(self):
        self.fail_after(lambda: self.edit_json("af04", lambda d: d.__setitem__("status", "candidate_evidence_complete_non_authorizing")))

    def test_03_acceptance_record_missing_fails(self):
        self.fail_after(lambda: (self.root / "archive/campaign-001/af05/ACCEPTANCE.md").unlink())

    def test_04_candidate_head_drift_fails(self):
        self.fail_after(lambda: self.edit_json("af06", lambda d: d.__setitem__("candidate_exact_head", "0" * 40)))

    def test_05_candidate_merge_drift_fails(self):
        self.fail_after(lambda: self.edit_json("af07", lambda d: d.__setitem__("candidate_merge", "0" * 40)))

    def test_06_formation_acceptance_flag_fails(self):
        self.fail_after(lambda: self.edit_json("af08", lambda d: d.__setitem__("formation_accepted", False)))

    def test_07_binding_state_fails(self):
        self.fail_after(lambda: self.edit_json("af09", lambda d: d.__setitem__("campaign_complete_pending_binding", False)))

    def test_08_blocked_count_drift_fails(self):
        self.fail_after(lambda: self.edit_json("af10", lambda d: d.__setitem__("blocked_record_count", 4)))

    def test_09_remaining_evidence_fails(self):
        self.fail_after(lambda: self.edit_json("af05", lambda d: d.__setitem__("remaining_evidence_count", 1)))

    def test_10_sergeant_result_drift_fails(self):
        self.fail_after(lambda: self.edit_json("af04", lambda d: d.__setitem__("sergeant_review_result", "pass")))

    def test_11_duplicate_record_fails(self):
        def mutate(d): d["records"][1]["id"] = d["records"][0]["id"]
        self.fail_after(lambda: self.edit_json("af06", mutate))

    def test_12_worker_independence_fails(self):
        def mutate(d): d["records"][0]["verifier"] = d["records"][0]["primary"]
        self.fail_after(lambda: self.edit_json("af07", mutate))

    def test_13_acceptance_candidate_proof_missing_fails(self):
        self.fail_after(lambda: self.edit_text("archive/campaign-001/af08/ACCEPTANCE.md", MODULE.CANDIDATE_DIGEST, "digest-missing"))

    def test_14_block_safety_fails(self):
        self.fail_after(lambda: self.edit_text("archive/campaign-001/af10/records/I018-QUALCOMM-DIAG.md", "Safe next action", "No next action"))

    def test_15_runtime_authorization_fails(self):
        self.fail_after(lambda: self.edit_text("CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED"))

    def test_16_adr_acceptance_fails(self):
        self.fail_after(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
            "- ADR-0033: ACCEPTED `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        ))

    def test_17_p01_removal_fails(self):
        self.fail_after(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "**Active work unit:** 0C-04 / P01 — physical pinned-host proof",
            "**Active work unit:** archive complete",
        ))

    def test_18_premature_global_binding_fails(self):
        self.fail_after(lambda: self.edit_text(
            "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
            "- completed formations: 3",
            "- completed formations: 10",
        ))

    def test_19_af11_fails(self):
        def mutate():
            path = self.root / "archive/campaign-001/af11"
            path.mkdir(parents=True)
            (path / "RESULT.json").write_text("{}\n", encoding="utf-8")
        self.fail_after(mutate)

    def test_20_af01_baseline_drift_fails(self):
        self.fail_after(lambda: self.edit_json("af01", lambda d: d.__setitem__("accepted_archive_record_count", 10)))

if __name__ == "__main__":
    unittest.main()
