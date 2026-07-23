#!/usr/bin/env python3
"""Run AF03 acceptance with anchored test transformations."""
from __future__ import annotations

from pathlib import Path

import apply_af03_acceptance as base

ROOT = Path(__file__).resolve().parents[1]


def sync_af03_tests() -> None:
    path = ROOT / "tools/test_check_archive_af03.py"
    base.replace_once(
        path,
        "from check_archive_af03 import (\n    ADR0033,\n",
        "from check_archive_af03 import (\n    ACCEPTANCE,\n    ADR0033,\n",
        "AF03 test acceptance import",
    )
    base.replace_once(
        path,
        "    RESULT_MD,\n    SERGEANT_REVIEW,\n    MANIFEST,",
        "    RESULT_MD,\n    SERGEANT_REVIEW,\n    ACCEPTANCE,\n    MANIFEST,",
        "AF03 test acceptance fixture",
    )
    base.replace_once(path, 'self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")', 'self.assertEqual(result["status"], "accepted_complete_valid_non_authorizing")', "AF03 valid status test")
    base.replace_once(path, 'self.assertEqual(result["candidate_archive_outcome_count"], 10)', 'self.assertEqual(result["accepted_archive_record_count"], 10)', "AF03 accepted count test")
    base.replace_once(path, 'self.assertFalse(result["af03_accepted"])', 'self.assertTrue(result["af03_accepted"])', "AF03 accepted assertion")
    old = '''    def test_result_status_cannot_be_accepted(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "accepted_complete")
        self.assert_invalid(root)
'''
    new = '''    def test_result_status_cannot_revert_to_candidate(self) -> None:
        root = self.make_repo()
        self.mutate_result(root, "status", "candidate_complete_pending_exact_head_review")
        self.assert_invalid(root)
'''
    base.replace_once(path, old, new, "AF03 status regression")
    old = '''    def test_acceptance_record_cannot_appear(self) -> None:
        root = self.make_repo()
        path = root / "archive/campaign-001/af03/ACCEPTANCE.md"
        path.write_text("# premature acceptance\\n", encoding="utf-8")
        self.assert_invalid(root)
'''
    new = '''    def test_acceptance_record_cannot_disappear(self) -> None:
        root = self.make_repo()
        (root / ACCEPTANCE).unlink()
        self.assert_invalid(root)
'''
    base.replace_once(path, old, new, "AF03 acceptance regression")
    base.replace_once(path, 'self.mutate_index(root, "accepted_archive_record_count", 29)', 'self.mutate_index(root, "accepted_archive_record_count", 19)', "AF03 operative total regression")


def main() -> int:
    base.sync_af03_tests = sync_af03_tests
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
