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
SPEC = importlib.util.spec_from_file_location("campaign_validator", HERE / "check_archive_campaign_af04_af10.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

class CampaignClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "conformance"))

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def validate(self):
        return MODULE.validate(self.root)

    def expect_fail(self, mutation):
        mutation()
        with self.assertRaises(MODULE.ValidationError):
            self.validate()

    def edit_json(self, formation, fn):
        path = self.root / "archive" / "campaign-001" / formation / "RESULT.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        fn(data)
        path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    def edit_text(self, path, old, new):
        target = self.root / path
        text = target.read_text(encoding="utf-8")
        self.assertIn(old, text)
        target.write_text(text.replace(old, new, 1), encoding="utf-8")

    def test_00_valid_candidate(self):
        report = self.validate()
        self.assertEqual(report["status"], "af04_af10_candidate_complete_valid_non_authorizing")
        self.assertEqual(report["new_record_count"], 68)
        self.assertEqual(report["campaign_accepted_archive_record_count_if_promoted"], 91)
        self.assertEqual(report["campaign_blocked_record_count_if_promoted"], 7)

    def test_01_missing_result_fails(self):
        self.expect_fail(lambda: (self.root / "archive/campaign-001/af04/RESULT.json").unlink())

    def test_02_status_promotion_fails(self):
        self.expect_fail(lambda: self.edit_json("af04", lambda d: d.__setitem__("status", "accepted_complete")))

    def test_03_assigned_count_drift_fails(self):
        self.expect_fail(lambda: self.edit_json("af05", lambda d: d.__setitem__("assigned_record_count", 9)))

    def test_04_accepted_count_drift_fails(self):
        self.expect_fail(lambda: self.edit_json("af10", lambda d: d.__setitem__("accepted_archive_record_count", 4)))

    def test_05_remaining_evidence_fails(self):
        self.expect_fail(lambda: self.edit_json("af06", lambda d: d.__setitem__("remaining_evidence_count", 1)))

    def test_06_duplicate_record_identity_fails(self):
        def mutate(d): d["records"][1]["id"] = d["records"][0]["id"]
        self.expect_fail(lambda: self.edit_json("af07", mutate))

    def test_07_duplicate_primary_fails(self):
        def mutate(d): d["records"][1]["primary"] = d["records"][0]["primary"]
        self.expect_fail(lambda: self.edit_json("af08", mutate))

    def test_08_primary_verifier_collapse_fails(self):
        def mutate(d): d["records"][0]["verifier"] = d["records"][0]["primary"]
        self.expect_fail(lambda: self.edit_json("af09", mutate))

    def test_09_missing_record_file_fails(self):
        self.expect_fail(lambda: (self.root / "archive/campaign-001/af04/records/D044-DIFY.md").unlink())

    def test_10_primary_packet_binding_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af05/records/D033-YOUKI.md", "Primary Archivist: `AF05-P01`", "Primary Archivist: `AF05-X01`"))

    def test_11_verifier_packet_binding_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af06/records/D034-CRUN.md", "Independent Verifier: `AF06-V01`", "Independent Verifier: `AF06-P01`"))

    def test_12_bounded_outcome_heading_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af07/records/D041-DENO.md", "## Bounded outcome", "## Recommendation"))

    def test_13_result_record_outcome_mismatch_fails(self):
        def mutate(d): d["records"][0]["outcome"] = "accepted_for_archive_weakened"
        self.expect_fail(lambda: self.edit_json("af08", mutate))

    def test_14_non_authorizing_statement_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af09/records/I004-TECHGUY-IMEI.md", "This outcome does not authorize implementation.", "Implementation may begin."))

    def test_15_block_safe_action_missing_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af10/records/I018-QUALCOMM-DIAG.md", "Safe next action", "Future idea"))

    def test_16_block_prohibition_missing_fails(self):
        self.expect_fail(lambda: self.edit_text("archive/campaign-001/af05/records/D065-AMERTOGLU16-GITHUB-IO.md", "copying or adapting source remains prohibited", "source reuse may proceed"))

    def test_17_sergeant_result_fails(self):
        self.expect_fail(lambda: self.edit_json("af04", lambda d: d.__setitem__("sergeant_review_result", "pass")))

    def test_18_sergeant_frozen_head_fails(self):
        self.expect_fail(lambda: self.edit_json("af10", lambda d: d.__setitem__("sergeant_review_target_head", "0" * 40)))

    def test_19_runtime_authorization_fails(self):
        self.expect_fail(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "**Runtime implementation:** NOT AUTHORIZED",
            "**Runtime implementation:** AUTHORIZED",
        ))

    def test_20_adr_acceptance_fails(self):
        self.expect_fail(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
            "- ADR-0033: ACCEPTED `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        ))

    def test_21_p01_removal_fails(self):
        self.expect_fail(lambda: self.edit_text(
            "CURRENT_STATE.md",
            "**Active work unit:** 0C-04 / P01 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure",
            "**Active work unit:** 0C-04 / PX1 — physical pinned-host proof, package review, durable evidence and ADR-0033 closure",
        ))

    def test_22_af11_creation_fails(self):
        def mutate():
            path = self.root / "archive/campaign-001/af11"
            path.mkdir(parents=True)
            (path / "MISSION.md").write_text("unexpected\n", encoding="utf-8")
        self.expect_fail(mutate)

    def test_23_premature_manifest_promotion_fails(self):
        self.expect_fail(lambda: self.edit_text(
            "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
            "## AF04\n\n- status: READY / NOT STARTED",
            "## AF04\n\n- status: ACCEPTED COMPLETE",
        ))

    def test_24_af10_reserve_consumption_fails(self):
        self.expect_fail(lambda: self.edit_json("af10", lambda d: d.__setitem__("reserve_pairs_used", 1)))

    def test_25_baseline_af01_drift_fails(self):
        self.expect_fail(lambda: self.edit_json("af01", lambda d: d.__setitem__("accepted_archive_record_count", 10)))

if __name__ == "__main__":
    unittest.main()
