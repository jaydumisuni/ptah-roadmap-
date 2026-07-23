#!/usr/bin/env python3
"""Run Phase 0C-18 acceptance with anchored validator transformations."""
from __future__ import annotations

from pathlib import Path

import apply_phase0c18_diagnostic_worker_acceptance as base

ROOT = Path(__file__).resolve().parents[1]


def fixed_accept_validator_and_tests() -> None:
    validator = ROOT / "tools/check_platform_diagnostic_advisory.py"
    base.replace_once(
        validator,
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")',
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")\n'
        f'CANDIDATE_HEAD = "{base.CANDIDATE_HEAD}"\n'
        f'CANDIDATE_RUN = "{base.CANDIDATE_RUN}"\n'
        f'CANDIDATE_ARTIFACT = "{base.CANDIDATE_ARTIFACT}"\n'
        f'CANDIDATE_ARTIFACT_DIGEST = "{base.CANDIDATE_ARTIFACT_DIGEST}"\n'
        f'CANDIDATE_REPORT_SHA256 = "{base.CANDIDATE_REPORT_SHA256}"\n'
        f'CANDIDATE_MERGE = "{base.CANDIDATE_MERGE}"\n'
        f'ACCEPTANCE_RECORD = "{base.ACCEPTANCE_RECORD}"',
        "validator evidence constants",
    )
    replacements = (
        ('require(protocol, "Status: candidate product clarification", "protocol candidate state")',
         'require(protocol, "Status: accepted product clarification", "protocol accepted state")'),
        ('require(adr, "Status: proposed", "ADR-0036 proposed state")',
         'require(adr, "Status: accepted", "ADR-0036 accepted state")'),
        ('require(work_package, "Status: candidate under review", "Phase 0C-18 candidate state")',
         'require(work_package, "Status: accepted and complete", "Phase 0C-18 accepted state")'),
        ('require(decisions, "### ADR-0036 — Platform diagnostic advisory and efficient worker execution boundary", "decision index")\n    require(decisions, "**PROPOSED.**", "decision proposed state")',
         'require(decisions, "### D-052 — Ptah may diagnose its platform and efficiently execute caller-given worker formations", "accepted decision index")\n    require(decisions, "**ACCEPTED.**", "decision accepted state")'),
        ('require(current, "## Phase 0C-18 diagnostic and efficient-worker candidate", "current-state candidate section")',
         'require(current, "## Accepted Phase 0C-18 diagnostic and efficient-worker boundary", "current-state accepted section")'),
        ('require(progress, "## Diagnostic advisory and efficient worker candidate", "progress candidate section")',
         'require(progress, "## Diagnostic advisory and efficient worker boundary — accepted", "progress accepted section")'),
        ('require(handoff, "## Diagnostic advisory and efficient worker candidate", "handoff candidate section")',
         'require(handoff, "## Accepted diagnostic advisory and efficient worker boundary", "handoff accepted section")'),
        ('"status": "candidate_under_review",', '"status": "accepted_operational_clarification",'),
        ('"status": "candidate_valid_non_authorizing",', '"status": "accepted_valid_non_authorizing",'),
    )
    for old, new in replacements:
        base.replace_once(validator, old, new, f"validator accepted state {old[:36]}")

    expected_tail = '''        "af03_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }'''
    expected_replacement = f'''        "af03_started": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "protocol_version": "1.0.0",
        "adr_0036_accepted": True,
        "phase0c_18_complete": True,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": ACCEPTANCE_RECORD,
    }}'''
    base.replace_once(validator, expected_tail, expected_replacement, "validator accepted machine index")

    report_tail = '''        "af03_started": False,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }'''
    report_replacement = f'''        "af03_started": False,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "protocol_version": "1.0.0",
        "adr_0036_accepted": True,
        "phase0c_18_complete": True,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": ACCEPTANCE_RECORD,
    }}'''
    base.replace_once(validator, report_tail, report_replacement, "validator accepted report")

    tests = ROOT / "tools/test_check_platform_diagnostic_advisory.py"
    base.replace_once(
        tests,
        'self.assertEqual(result["status"], "candidate_valid_non_authorizing")',
        'self.assertEqual(result["status"], "accepted_valid_non_authorizing")',
        "test accepted status",
    )
    insertion = '''    def test_accepted_protocol_cannot_revert(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("planning/PTAH-PLATFORM-DIAGNOSTIC-ADVISORY.md"),
            "Status: accepted product clarification",
            "Status: candidate product clarification",
        )
        self.assert_invalid(root)

    def test_accepted_adr0036_cannot_revert(self) -> None:
        root = self.make_repo()
        self.replace(
            root,
            Path("decisions/ADR-0036-PLATFORM-DIAGNOSTIC-ADVISORY-BOUNDARY.md"),
            "Status: accepted",
            "Status: proposed",
        )
        self.assert_invalid(root)

'''
    base.replace_once(
        tests,
        '\n\nif __name__ == "__main__":',
        "\n\n" + insertion + 'if __name__ == "__main__":',
        "accepted-state regressions",
    )


base.accept_validator_and_tests = fixed_accept_validator_and_tests

if __name__ == "__main__":
    raise SystemExit(base.main())
