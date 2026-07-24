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
SPEC = importlib.util.spec_from_file_location("complete_validator", HERE / "check_archive_campaign_complete.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

class CampaignCompleteTests(unittest.TestCase):
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

    def edit_json(self, relative: str, fn) -> None:
        path = self.root / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        fn(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def edit_text(self, relative: str, old: str, new: str) -> None:
        path = self.root / relative
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text)
        path.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_00_valid_complete_campaign(self):
        report = self.validate()
        self.assertEqual(report["status"], "campaign_001_complete_bound_non_authorizing")
        self.assertEqual(report["formation_count"], 10)
        self.assertEqual(report["obligation_count"], 98)
        self.assertEqual(report["accepted_archive_record_count"], 91)
        self.assertEqual(report["blocked_completed_outcome_count"], 7)
        self.assertEqual(report["remaining_evidence_count"], 0)

    def test_01_missing_operative_state_fails(self):
        self.fail_after(lambda: (self.root / "archive/campaign-001/OPERATIVE-STATE.json").unlink())

    def test_02_missing_binding_fails(self):
        self.fail_after(lambda: (self.root / "archive/campaign-001/OPERATIVE-BINDING.md").unlink())

    def test_03_candidate_head_drift_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/OPERATIVE-STATE.json", lambda d: d.__setitem__("candidate_exact_head", "0" * 40)))

    def test_04_accepted_head_drift_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/OPERATIVE-STATE.json", lambda d: d.__setitem__("accepted_state_exact_head", "0" * 40)))

    def test_05_acceptance_merge_drift_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/OPERATIVE-STATE.json", lambda d: d.__setitem__("operative_acceptance_merge", "0" * 40)))

    def test_06_campaign_totals_drift_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/OPERATIVE-STATE.json", lambda d: d.__setitem__("accepted_archive_record_count", 92)))

    def test_07_blocked_identity_drift_fails(self):
        def mutate(d): d["blocked_record_ids"][0] = "D000"
        self.fail_after(lambda: self.edit_json("archive/campaign-001/OPERATIVE-STATE.json", mutate))

    def test_08_manifest_formation_status_fails(self):
        self.fail_after(lambda: self.edit_text("archive/CAMPAIGN-001-FORMATION-MANIFEST.md", "## AF04\n\n- status: ACCEPTED COMPLETE", "## AF04\n\n- status: READY / NOT STARTED"))

    def test_09_manifest_total_fails(self):
        self.fail_after(lambda: self.edit_text("archive/CAMPAIGN-001-FORMATION-MANIFEST.md", "- completed formations: 10", "- completed formations: 9"))

    def test_10_result_not_accepted_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/af08/RESULT.json", lambda d: d.__setitem__("status", "candidate_evidence_complete_non_authorizing")))

    def test_11_remaining_evidence_fails(self):
        self.fail_after(lambda: self.edit_json("archive/campaign-001/af10/RESULT.json", lambda d: d.__setitem__("remaining_evidence_count", 1)))

    def test_12_record_identity_collision_fails(self):
        def mutate(d): d["records"][1]["id"] = d["records"][0]["id"]
        self.fail_after(lambda: self.edit_json("archive/campaign-001/af06/RESULT.json", mutate))

    def test_13_worker_independence_fails(self):
        def mutate(d): d["records"][0]["verifier"] = d["records"][0]["primary"]
        self.fail_after(lambda: self.edit_json("archive/campaign-001/af09/RESULT.json", mutate))

    def test_14_bound_acceptance_proof_fails(self):
        self.fail_after(lambda: self.edit_text("archive/campaign-001/af04/ACCEPTANCE.md", MODULE.ACCEPTED["accepted_state_artifact_digest"], "missing-digest"))

    def test_15_block_safe_action_fails(self):
        self.fail_after(lambda: self.edit_text("archive/campaign-001/af10/records/I018-QUALCOMM-DIAG.md", "Safe next action", "No next action"))

    def test_16_runtime_authorization_fails(self):
        self.fail_after(lambda: self.edit_text("CURRENT_STATE.md", "**Runtime implementation:** NOT AUTHORIZED", "**Runtime implementation:** AUTHORIZED"))

    def test_17_adr_acceptance_fails(self):
        self.fail_after(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
            "- ADR-0033: ACCEPTED `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        ))

    def test_18_p01_removal_fails(self):
        self.fail_after(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "**Active work unit:** 0C-04 / P01 — physical pinned-host proof",
            "**Active work unit:** campaign complete",
        ))

    def test_19_af11_fails(self):
        def mutate():
            path = self.root / "archive/campaign-001/af11"
            path.mkdir(parents=True)
            (path / "RESULT.json").write_text("{}\n", encoding="utf-8")
        self.fail_after(mutate)

    def test_20_binding_non_authorization_fails(self):
        self.fail_after(lambda: self.edit_text("archive/campaign-001/OPERATIVE-BINDING.md", "Runtime implementation remains `NOT AUTHORIZED`", "Runtime implementation is authorized"))

if __name__ == "__main__":
    unittest.main()
