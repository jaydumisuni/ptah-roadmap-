#!/usr/bin/env python3
"""Apply the neutral substrate correction with copy-safe generated tests."""
from __future__ import annotations

from pathlib import Path

import apply_neutral_substrate_plan_correction as base

ROOT = Path(__file__).resolve().parents[1]


def correct_tests_copy_safe() -> None:
    path = ROOT / "tools/test_check_master_plan_closure.py"
    base.replace_once(
        path,
        '    "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n',
        '    "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",\n    "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md",\n    "planning/PTAH-NEUTRAL-SUBSTRATE-PLAN-CORRECTION.md",\n',
        "test required files",
    )
    base.replace_once(
        path,
        '        self.assertEqual(report["programme_a_package_count"], 15)\n',
        '        self.assertEqual(report["programme_a_package_count"], 15)\n        self.assertTrue(report["neutral_substrate_boundary_restored"])\n        self.assertFalse(report["ptah_decision_authority"])\n        self.assertFalse(report["ptah_review_authority"])\n        self.assertFalse(report["af03_started"])\n',
        "test valid correction assertions",
    )
    insertion = r'''
    def test_master_plan_cannot_restore_ptah_context_compiler(self) -> None:
        root = self.make_repo()
        path = root / "MASTER_PLAN.md"
        self.replace(
            path,
            "Before an agent participates, Hunter, Sergeant, a human-facing application or another caller may request exact Workspace records and construct its own bounded packet.",
            "Before an agent participates, Ptah compiles a bounded packet.",
        )
        self.assert_invalid(root)

    def test_roadmap_cannot_restore_source_authority_service(self) -> None:
        root = self.make_repo()
        path = root / "IMPLEMENTATION_ROADMAP.md"
        self.replace(
            path,
            "- exact Workspace, Session, Activity, Object and Artifact retrieval APIs;",
            "- source-authority service;",
        )
        self.assert_invalid(root)

    def test_machine_index_cannot_give_ptah_review_authority(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["ptah_neutral_substrate_boundary"]["ptah_review_authority"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_af03_cannot_start_during_boundary_correction(self) -> None:
        root = self.make_repo()
        path = root / "master-plan-index.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["ptah_neutral_substrate_boundary"]["af03_started"] = True
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        self.assert_invalid(root)

    def test_stale_af02_active_sentence_is_rejected(self) -> None:
        root = self.make_repo()
        path = root / "CURRENT_STATE.md"
        path.write_text(
            path.read_text(encoding="utf-8")
            + "\nAF02 evidence collection is active under its accepted twenty-private mission.\n",
            encoding="utf-8",
        )
        self.assert_invalid(root)
'''
    base.replace_once(
        path,
        '\n\nif __name__ == "__main__":',
        insertion + '\n\nif __name__ == "__main__":',
        "neutral tests",
    )


base.correct_tests = correct_tests_copy_safe

if __name__ == "__main__":
    raise SystemExit(base.main())
