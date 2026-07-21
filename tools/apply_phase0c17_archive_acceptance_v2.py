#!/usr/bin/env python3
"""Run Phase 0C-17 acceptance with an anchored validator transformation."""
from __future__ import annotations

from pathlib import Path

import apply_phase0c17_archive_acceptance as base

ROOT = Path(__file__).resolve().parents[1]


def fixed_accept_validator_and_tests() -> None:
    validator = ROOT / "tools/check_archive_formation.py"
    replacements = (
        (
            'require(adr, "Status: proposed", "ADR-0035 proposed state")',
            'require(adr, "Status: accepted", "ADR-0035 accepted state")',
        ),
        (
            'require(work_package, "Status: candidate under review", "Phase 0C-17 candidate state")',
            'require(work_package, "Status: accepted and complete", "Phase 0C-17 accepted state")',
        ),
        (
            'require(decisions, "### ADR-0035 — Tenfold archive formation and evidence promotion", "decision index entry")\n'
            '    require(decisions, "**PROPOSED.**", "ADR-0035 proposed index state")',
            'require(decisions, "### D-051 — Tenfold archive formation separates parallel evidence from promotion authority", "accepted decision index entry")\n'
            '    require(decisions, "**ACCEPTED.**", "ADR-0035 accepted index state")',
        ),
        (
            'require(progress, "## Tenfold archive formation candidate", "progress archive section")',
            'require(progress, "## Tenfold archive formation — accepted", "progress archive section")',
        ),
        (
            'require(progress, "200 private slots allocated", "progress force count")',
            'require(progress, "200 private slots allocated", "progress force count")\n'
            '    require(progress, "AF01 is READY but not started", "progress AF01 state")',
        ),
        (
            'require(current_state, "## Active Phase 0C-17 tenfold archive formation candidate", "current archive candidate")\n'
            '    require(current_state, "PR #26", "current archive PR")\n'
            '    require(current_state, "does not replace P01", "current P01 boundary")',
            'require(current_state, "## Accepted Phase 0C-17 tenfold archive formation", "current archive acceptance")\n'
            '    require(current_state, "ADR-0035: ACCEPTED", "current accepted ADR")\n'
            '    require(current_state, "AF01 is READY but not started", "current AF01 state")\n'
            '    require(current_state, "does not replace P01", "current P01 boundary")',
        ),
        (
            'require(handoff, "## Cross-cutting archive formation candidate", "handoff archive candidate")\n'
            '    require(handoff, "pull request: #26", "handoff archive PR")',
            'require(handoff, "## Accepted cross-cutting archive formation", "handoff archive acceptance")\n'
            '    require(handoff, "ADR-0035: ACCEPTED", "handoff accepted ADR")\n'
            '    require(handoff, "AF01: READY / NOT STARTED", "handoff AF01 state")',
        ),
        (
            '"status": "candidate_under_review",\n        "source_branch": "phase0c-tenfold-archive-formation",',
            '"status": "accepted_operational_protocol_af01_ready",\n        "source_branch": "main",',
        ),
        (
            '"assigned_record_count": 98,\n'
            '        "phase_0a_reopened": False,\n'
            '        "runtime_implementation_authorized": False,\n'
            '    }',
            '"assigned_record_count": 98,\n'
            '        "phase_0a_reopened": False,\n'
            '        "runtime_implementation_authorized": False,\n'
            '        "protocol_version": "1.0.0",\n'
            f'        "candidate_exact_head": "{base.CANDIDATE_HEAD}",\n'
            f'        "candidate_workflow_run": "{base.CANDIDATE_RUN}",\n'
            f'        "candidate_artifact_id": "{base.CANDIDATE_ARTIFACT}",\n'
            f'        "candidate_artifact_digest": "{base.CANDIDATE_ARTIFACT_DIGEST}",\n'
            f'        "validation_report_sha256": "{base.VALIDATION_REPORT_DIGEST}",\n'
            f'        "candidate_merge": "{base.CANDIDATE_MERGE}",\n'
            '        "adr_0035_accepted": True,\n'
            '        "phase0c_17_complete": True,\n'
            '        "af01_status": "ready_not_started",\n'
            '        "accepted_archive_record_count": 0,\n'
            '    }',
        ),
        (
            '"status": "candidate_valid_non_authorizing",',
            '"status": "accepted_valid_non_authorizing",',
        ),
    )
    for old, new in replacements:
        base.replace_once(validator, old, new, f"validator replacement {old[:32]}")

    tests = ROOT / "tools/test_check_archive_formation.py"
    base.replace_once(
        tests,
        'self.assertEqual(result["status"], "candidate_valid_non_authorizing")',
        'self.assertEqual(result["status"], "accepted_valid_non_authorizing")',
        "test accepted status",
    )
    insertion = """    def test_accepted_adr0035_cannot_revert(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md"),
            "Status: accepted",
            "Status: proposed",
        )
        self.assert_invalid(root)

    def test_af01_cannot_be_precompleted(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("master-plan-index.json"),
            '"accepted_archive_record_count": 0',
            '"accepted_archive_record_count": 10',
        )
        self.assert_invalid(root)

"""
    base.replace_once(
        tests,
        '\n\nif __name__ == "__main__":',
        "\n\n" + insertion + 'if __name__ == "__main__":',
        "accepted-state tests",
    )


base.accept_validator_and_tests = fixed_accept_validator_and_tests

if __name__ == "__main__":
    raise SystemExit(base.main())
