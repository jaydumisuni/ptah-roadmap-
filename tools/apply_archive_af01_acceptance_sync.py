#!/usr/bin/env python3
"""Promote AF01 candidate evidence to accepted campaign closure."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "f60e340cb856d50e88b4279147a933d838fce759"
CANDIDATE_RUN = "29862087745"
CANDIDATE_ARTIFACT = "8507695005"
CANDIDATE_ARTIFACT_DIGEST = "sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267"
CANDIDATE_REPORT_DIGEST = "4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691"
CANDIDATE_MERGE = "0a35a8a904bdf235fa4989ea05b684443d5a879a"
ACCEPTANCE_RECORD = "archive/campaign-001/af01/ACCEPTANCE.md"


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sync_manifest() -> None:
    path = ROOT / "archive/CAMPAIGN-001-FORMATION-MANIFEST.md"
    common = "- private count: 20\n- assigned records: 10\n- reserve pairs: 0"
    replace_once(
        path,
        common,
        "- status: ACCEPTED COMPLETE\n- private count: 20\n- assigned records: 10\n- accepted archive records: 9\n- blocked completed outcomes: 1\n- remaining evidence: 0\n- result: `archive/campaign-001/af01/RESULT.json`\n- acceptance: `archive/campaign-001/af01/ACCEPTANCE.md`\n- reserve pairs: 0",
        "AF01 manifest status",
    )
    replace_once(
        path,
        common,
        "- status: READY / NOT STARTED\n- private count: 20\n- assigned records: 10\n- reserve pairs: 0",
        "AF02 manifest status",
    )
    replace_once(
        path,
        "- private verdict authority: none",
        "- private verdict authority: none\n- completed formations: 1\n- accepted archive records: 9\n- blocked completed outcomes: 1\n- next formation: AF02 READY / NOT STARTED",
        "campaign totals",
    )


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    old = "AF01 is READY but not started. This cross-cutting recovery protocol does not replace P01 as the active authorization work, reopen Phase 0A, mark records archived, accept ADR-0033 or authorize runtime implementation."
    new = f"""Campaign 001 progress:

- AF01: ACCEPTED COMPLETE;
- accepted archive records: 9;
- blocked completed outcomes: 1 (`D047` MiniRouter source reuse);
- AF02: READY / NOT STARTED;
- AF01 candidate exact head: `{CANDIDATE_HEAD}`;
- AF01 workflow run/artifact: `{CANDIDATE_RUN}` / `{CANDIDATE_ARTIFACT}`;
- AF01 candidate merge: `{CANDIDATE_MERGE}`;
- AF01 acceptance record: `{ACCEPTANCE_RECORD}`.

AF02 readiness does not start evidence collection or authorize source reuse. The archive campaign does not replace P01 as the active implementation-authorization work, reopen Phase 0A, accept ADR-0033 or authorize runtime implementation."""
    replace_once(path, old, new, "current AF01 acceptance")


def sync_progress() -> None:
    path = ROOT / "PROGRESS.md"
    old = "- [ ] AF01 is READY but not started; no source record is pre-ticked as archived."
    new = f"""- [x] AF01 completed ten paired source reviews with nine accepted archive records and one completed MiniRouter source-reuse block;
- [x] AF01 candidate exact head `{CANDIDATE_HEAD}` passed 24 regression cases in run `{CANDIDATE_RUN}`;
- [x] AF01 retained artifact `{CANDIDATE_ARTIFACT}` with digest `{CANDIDATE_ARTIFACT_DIGEST}`;
- [x] AF01 candidate merged as `{CANDIDATE_MERGE}` and accepted closure recorded;
- [ ] AF02 is READY / NOT STARTED; no AF02 source record is pre-ticked as archived."""
    replace_once(path, old, new, "progress AF01 acceptance")


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "AF01: READY / NOT STARTED",
        "AF01: ACCEPTED COMPLETE\nAF02: READY / NOT STARTED",
        "handoff formation states",
    )
    old = "Campaign 001 covers 98 source obligations with ten twenty-private formations and one primary/verifier pair per obligation. It is an accepted queue and operating protocol, not proof that records are archived or that a 200-agent runtime exists."
    new = f"""Campaign 001 covers 98 source obligations with ten twenty-private formations and one primary/verifier pair per obligation. AF01 is accepted complete with nine accepted archive records and one completed MiniRouter source-reuse block. Evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, candidate merge `{CANDIDATE_MERGE}`, acceptance record `{ACCEPTANCE_RECORD}`. AF02 is ready but not started.

The campaign is an archive/recovery workflow, not proof that a 200-agent runtime exists and not runtime implementation authority."""
    replace_once(path, old, new, "handoff AF01 evidence")


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise SyncError("active P01 work drifted")
    if data.get("runtime_implementation_authorized") is not False:
        raise SyncError("runtime unexpectedly authorized")
    archive = data["operational_protocols"]["tenfold_archive_formation"]
    archive.update(
        {
            "status": "accepted_operational_protocol_af01_complete_af02_ready",
            "af01_status": "accepted_complete",
            "af01_candidate_exact_head": CANDIDATE_HEAD,
            "af01_candidate_workflow_run": CANDIDATE_RUN,
            "af01_candidate_artifact_id": CANDIDATE_ARTIFACT,
            "af01_candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
            "af01_candidate_validation_report_sha256": CANDIDATE_REPORT_DIGEST,
            "af01_candidate_merge": CANDIDATE_MERGE,
            "af01_acceptance_record": ACCEPTANCE_RECORD,
            "accepted_archive_record_count": 9,
            "blocked_archive_record_count": 1,
            "completed_formation_count": 1,
            "af02_status": "ready_not_started",
            "af02_started": False,
            "af02_authorized": False,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_validator() -> None:
    path = ROOT / "tools/check_archive_af01.py"
    replacements = (
        (
            'RESULT_MD = Path("archive/campaign-001/af01/RESULT.md")',
            'RESULT_MD = Path("archive/campaign-001/af01/RESULT.md")\nACCEPTANCE = Path("archive/campaign-001/af01/ACCEPTANCE.md")',
        ),
        (
            '    result_md = read(root, RESULT_MD)\n    result = json.loads(read(root, RESULT_JSON))',
            '    result_md = read(root, RESULT_MD)\n    acceptance = read(root, ACCEPTANCE)\n    result = json.loads(read(root, RESULT_JSON))',
        ),
        (
            'require(mission, "Status: CANDIDATE COMPLETE", "mission candidate state")',
            'require(mission, "Status: ACCEPTED COMPLETE", "mission accepted state")',
        ),
        (
            'require(mission, "AF02 is not authorized", "AF02 boundary")',
            'require(mission, "AF02 is READY / NOT STARTED", "AF02 ready boundary")',
        ),
        (
            'require(result_md, "CANDIDATE COMPLETE", "result candidate state")',
            'require(result_md, "Status: ACCEPTED COMPLETE", "result accepted state")\n    require(acceptance, "Status: ACCEPTED EVIDENCE RECORD", "acceptance record state")\n    require(acceptance, CANDIDATE_MERGE, "AF01 candidate merge evidence")\n    require(acceptance, "AF02: READY / NOT STARTED", "AF02 next state")',
        ),
        (
            '        "status": "candidate_complete_pending_exact_head_review",',
            '        "status": "accepted_complete_non_authorizing",\n        "candidate_exact_head": CANDIDATE_HEAD,\n        "candidate_workflow_run": CANDIDATE_RUN,\n        "candidate_artifact_id": CANDIDATE_ARTIFACT,\n        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,\n        "candidate_validation_report_sha256": CANDIDATE_REPORT_DIGEST,\n        "candidate_merge": CANDIDATE_MERGE,\n        "acceptance_record": str(ACCEPTANCE),',
        ),
        (
            '        "af02_authorized": False,',
            '        "af02_ready": True,\n        "af02_started": False,\n        "af02_authorized": False,',
        ),
        (
            '    require(donor_register, "**Status:** COMPLETE AND FROZEN", "frozen Phase 0A")',
            '    require(manifest, "- status: ACCEPTED COMPLETE", "manifest AF01 accepted state")\n    require(manifest, "- status: READY / NOT STARTED", "manifest AF02 ready state")\n    require(current_state, "AF01: ACCEPTED COMPLETE", "current AF01 accepted state")\n    require(current_state, "AF02: READY / NOT STARTED", "current AF02 ready state")\n    require(donor_register, "**Status:** COMPLETE AND FROZEN", "frozen Phase 0A")',
        ),
        (
            '        "status": "candidate_complete_valid_non_authorizing",',
            '        "status": "accepted_complete_valid_non_authorizing",',
        ),
        (
            '        "runtime_implementation_authorized": False,\n        "af02_authorized": False,',
            '        "runtime_implementation_authorized": False,\n        "af02_ready": True,\n        "af02_started": False,\n        "af02_authorized": False,',
        ),
    )
    text = path.read_text(encoding="utf-8")
    prefix = (
        'CANDIDATE_HEAD = "f60e340cb856d50e88b4279147a933d838fce759"\n'
        'CANDIDATE_RUN = "29862087745"\n'
        'CANDIDATE_ARTIFACT = "8507695005"\n'
        'CANDIDATE_ARTIFACT_DIGEST = "sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267"\n'
        'CANDIDATE_REPORT_DIGEST = "4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691"\n'
        'CANDIDATE_MERGE = "0a35a8a904bdf235fa4989ea05b684443d5a879a"\n\n'
    )
    anchor = 'MISSION = Path("archive/campaign-001/af01/MISSION.md")\n'
    if anchor not in text:
        raise SyncError("validator constant anchor missing")
    text = text.replace(anchor, prefix + anchor, 1)
    path.write_text(text, encoding="utf-8")
    for old, new in replacements:
        replace_once(path, old, new, f"validator replacement {old[:36]}")


def sync_tests() -> None:
    path = ROOT / "tools/test_check_archive_af01.py"
    replacements = (
        (
            '    ADR0033,\n    CHECKPOINT_05,',
            '    ACCEPTANCE,\n    ADR0033,\n    CHECKPOINT_05,',
        ),
        (
            '    RESULT_MD,\n    ValidationError,',
            '    RESULT_MD,\n    ValidationError,',
        ),
        (
            '    RESULT_MD,\n    MANIFEST,',
            '    RESULT_MD,\n    ACCEPTANCE,\n    MANIFEST,',
        ),
        (
            '    def test_valid_candidate(self) -> None:',
            '    def test_valid_accepted_closure(self) -> None:',
        ),
        (
            'self.assertEqual(result["status"], "candidate_complete_valid_non_authorizing")',
            'self.assertEqual(result["status"], "accepted_complete_valid_non_authorizing")',
        ),
        (
            '        self.assertFalse(result["af02_authorized"])',
            '        self.assertTrue(result["af02_ready"])\n        self.assertFalse(result["af02_started"])\n        self.assertFalse(result["af02_authorized"])',
        ),
        (
            '    def test_candidate_status_cannot_claim_acceptance_early(self) -> None:\n        root = self.make_repo()\n        self.mutate_result(root, lambda value: value.__setitem__("status", "accepted_complete"))\n        self.assert_invalid(root)',
            '    def test_accepted_status_cannot_revert_to_candidate(self) -> None:\n        root = self.make_repo()\n        self.mutate_result(root, lambda value: value.__setitem__("status", "candidate_complete_pending_exact_head_review"))\n        self.assert_invalid(root)\n\n    def test_acceptance_record_cannot_disappear(self) -> None:\n        root = self.make_repo()\n        (root / ACCEPTANCE).unlink()\n        self.assert_invalid(root)\n\n    def test_af02_ready_cannot_be_removed(self) -> None:\n        root = self.make_repo()\n        self.mutate_result(root, lambda value: value.__setitem__("af02_ready", False))\n        self.assert_invalid(root)\n\n    def test_af02_cannot_start_during_af01_acceptance(self) -> None:\n        root = self.make_repo()\n        self.mutate_result(root, lambda value: value.__setitem__("af02_started", True))\n        self.assert_invalid(root)',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"test replacement {old[:36]}")


def sync_workflow() -> None:
    path = ROOT / ".github/workflows/archive-campaign-001-af01.yml"
    replacements = (
        ("Validate AF01 candidate closure", "Validate AF01 accepted closure"),
        (
            'if evidence["status"] != "candidate_complete_valid_non_authorizing":\n              raise SystemExit("AF01 candidate validation status is invalid")',
            'if evidence["status"] != "accepted_complete_valid_non_authorizing":\n              raise SystemExit("AF01 accepted validation status is invalid")',
        ),
        (
            '              "remaining_evidence_count": 0,',
            '              "remaining_evidence_count": 0,\n              "af02_ready": True,\n              "af02_started": False,',
        ),
    )
    for old, new in replacements:
        replace_once(path, old, new, f"workflow replacement {old[:36]}")


def main() -> int:
    sync_manifest()
    sync_current_state()
    sync_progress()
    sync_handoff()
    sync_index()
    sync_validator()
    sync_tests()
    sync_workflow()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime non-authorization boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A donor register is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")

    print("AF01 accepted closure synchronization complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
