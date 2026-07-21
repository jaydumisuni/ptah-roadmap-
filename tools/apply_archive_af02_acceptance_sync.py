#!/usr/bin/env python3
"""Promote AF02's merged exact-head candidate into accepted campaign state."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "b710574b99269647cdd9029db5a2b217642aa344"
CANDIDATE_RUN = "29875542752"
CANDIDATE_ARTIFACT = "8512821506"
CANDIDATE_DIGEST = "sha256:78c5b702aa6025f088e2c54002bbe84fead003c92e0bb98ec18fcd0220b1d81c"
CANDIDATE_REPORT = "e18dac8a154547deb30c4482027b10c40dd892fd8a1024cba78f7366b44c6fd9"
CANDIDATE_MERGE = "58d89dfd1d5348cc8423222e3aff256ee041dce2"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"guarded replacement count for {path}: expected 1, got {count}: {old[:80]}")
    write(path, text.replace(old, new, 1))


acceptance = f"""# Campaign 001 — AF02 Accepted Closure

Status: ACCEPTED EVIDENCE RECORD

Accepted: 2026-07-21

## Candidate evidence

- candidate exact head: `{CANDIDATE_HEAD}`;
- AF02 workflow run: `{CANDIDATE_RUN}`;
- retained artifact: `{CANDIDATE_ARTIFACT}`;
- artifact digest: `{CANDIDATE_DIGEST}`;
- validation report SHA-256: `{CANDIDATE_REPORT}`;
- regression result: 33 passed — one valid state and 32 adversarial mutations;
- exact changed-file boundary: 18 durable files;
- unresolved review threads: zero;
- candidate merge: `{CANDIDATE_MERGE}`.

## Accepted formation result

- assigned records: 10;
- reconciled records: 10;
- accepted archive records: 10;
- blocked completed outcomes: 0;
- remaining evidence collection: 0;
- Primary Archivists: 10;
- Independent Verifiers: 10;
- durable checkpoints: 2.

## Next formation state

```text
AF02: ACCEPTED COMPLETE
AF03: READY / NOT STARTED
```

AF03 readiness does not start evidence collection, authorize source reuse, alter P01, accept ADR-0033 or authorize runtime implementation.

## Preserved boundaries

- Daytona remains bounded to its discontinued public AGPL-3.0 `v0.190.0` snapshot;
- E2B Desktop and Playwright MCP remain adapters, not independent authority;
- ADBKit grants no device authority;
- Kata, Moby, LlamaIndex and Ray remain optional donors behind native Ptah contracts;
- Phase 0A remains frozen;
- WP01–WP14 remain unchanged;
- P01 physical-host closure remains active;
- ADR-0033 remains proposed;
- runtime implementation remains unauthorized;
- AF03 is not started or authorized.
"""
write("archive/campaign-001/af02/ACCEPTANCE.md", acceptance)

replace_once(
    "archive/campaign-001/af02/MISSION.md",
    "Status: CANDIDATE COMPLETE — all records reconciled; pending exact-head validation and direct review",
    "Status: ACCEPTED COMPLETE",
)
replace_once(
    "archive/campaign-001/af02/MISSION.md",
    "- formation closure: pending exact-head validation and direct review.",
    "- accepted closure: `archive/campaign-001/af02/ACCEPTANCE.md`.",
)
replace_once(
    "archive/campaign-001/af02/MISSION.md",
    "No record remains unexamined. AF03 is not authorized until AF02 closure is reviewed and merged. P01 remains the active implementation-authorization work outside this archive campaign.",
    "AF02 is accepted complete. AF03 is READY / NOT STARTED and remains unstarted and unauthorized. P01 remains the active implementation-authorization work outside this archive campaign.",
)

result_md = read("archive/campaign-001/af02/RESULT.md")
result_md = result_md.replace("# Campaign 001 — AF02 Candidate Closure Result", "# Campaign 001 — AF02 Accepted Closure Result", 1)
result_md = result_md.replace("Status: CANDIDATE COMPLETE — pending exact-head validation and direct review", "Status: ACCEPTED COMPLETE", 1)
marker = "## Acceptance gates\n"
if result_md.count(marker) != 1:
    raise SystemExit("AF02 result acceptance-gate marker mismatch")
result_md = result_md.split(marker, 1)[0] + f"""## Accepted evidence

- candidate exact head: `{CANDIDATE_HEAD}`;
- workflow run: `{CANDIDATE_RUN}`;
- retained artifact: `{CANDIDATE_ARTIFACT}`;
- artifact digest: `{CANDIDATE_DIGEST}`;
- validation report SHA-256: `{CANDIDATE_REPORT}`;
- candidate merge: `{CANDIDATE_MERGE}`;
- regression result: 33 passed;
- exact-head identity matched;
- direct review found zero unresolved threads.

## Next formation

AF03 is READY / NOT STARTED. It remains unstarted and unauthorized.
"""
write("archive/campaign-001/af02/RESULT.md", result_md)

result_path = ROOT / "archive/campaign-001/af02/RESULT.json"
result = json.loads(result_path.read_text(encoding="utf-8"))
result.update({
    "status": "accepted_complete_non_authorizing",
    "candidate_exact_head": CANDIDATE_HEAD,
    "candidate_workflow_run": CANDIDATE_RUN,
    "candidate_artifact_id": CANDIDATE_ARTIFACT,
    "candidate_artifact_digest": CANDIDATE_DIGEST,
    "candidate_validation_report_sha256": CANDIDATE_REPORT,
    "candidate_merge": CANDIDATE_MERGE,
    "acceptance_record": "archive/campaign-001/af02/ACCEPTANCE.md",
    "af03_ready": True,
    "af03_started": False,
    "af03_authorized": False,
})
result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

replace_once(
    "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
    "- completed formations: 1\n- accepted archive records: 9\n- blocked completed outcomes: 1\n- active formation: AF02\n- AF02 accepted archive records: 0\n- AF02 remaining evidence: 10",
    "- completed formations: 2\n- accepted archive records: 19\n- blocked completed outcomes: 1\n- next formation: AF03 READY / NOT STARTED",
)
replace_once(
    "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
    "- status: ACTIVE\n- private count: 20\n- assigned records: 10\n- accepted archive records: 0\n- remaining evidence: 10\n- mission: `archive/campaign-001/af02/MISSION.md`\n- reserve pairs: 0",
    "- status: ACCEPTED COMPLETE\n- private count: 20\n- assigned records: 10\n- accepted archive records: 10\n- blocked completed outcomes: 0\n- remaining evidence: 0\n- result: `archive/campaign-001/af02/RESULT.json`\n- acceptance: `archive/campaign-001/af02/ACCEPTANCE.md`\n- reserve pairs: 0",
)
replace_once(
    "archive/CAMPAIGN-001-FORMATION-MANIFEST.md",
    "## AF03\n\n- private count: 20",
    "## AF03\n\n- status: READY / NOT STARTED\n- private count: 20",
)

replace_once(
    "PROGRESS.md",
    "- [-] AF02 is ACTIVE under `archive/campaign-001/af02/MISSION.md`; ten paired reviews are in evidence collection and zero AF02 records are accepted.",
    f"- [x] AF02 completed ten paired source reviews with ten bounded archive acceptances and zero blocks;\n- [x] AF02 candidate exact head `{CANDIDATE_HEAD}` passed 33 adversarial regressions in run `{CANDIDATE_RUN}`;\n- [x] AF02 retained artifact `{CANDIDATE_ARTIFACT}` with digest `{CANDIDATE_DIGEST}`;\n- [x] AF02 candidate merged as `{CANDIDATE_MERGE}` and accepted closure recorded;\n- [ ] AF03 is READY / NOT STARTED; no AF03 source record is pre-ticked as archived.",
)

replace_once(
    "AI_HANDOFF.md",
    "AF02: ACTIVE / ZERO RECORDS ACCEPTED",
    "AF02: ACCEPTED COMPLETE\nAF03: READY / NOT STARTED",
)
replace_once(
    "AI_HANDOFF.md",
    "AF02 is active under `archive/campaign-001/af02/MISSION.md`, with ten records in evidence collection and zero accepted.",
    f"AF02 is accepted complete with ten accepted archive records and zero blocks. Evidence: exact head `{CANDIDATE_HEAD}`, run `{CANDIDATE_RUN}`, artifact `{CANDIDATE_ARTIFACT}`, candidate merge `{CANDIDATE_MERGE}`, acceptance record `archive/campaign-001/af02/ACCEPTANCE.md`. AF03 is READY / NOT STARTED.",
)

replace_once(
    "CURRENT_STATE.md",
    "AF02: ACTIVE / ZERO RECORDS ACCEPTED",
    "AF02: ACCEPTED COMPLETE\nAF03: READY / NOT STARTED",
)

replace_once(
    "archive/campaign-001/af01/ACCEPTANCE.md",
    "AF02: ACTIVE / ZERO RECORDS ACCEPTED\nAF02 mission: archive/campaign-001/af02/MISSION.md\nAF02 base: ea2424bb5bc2bdb698bfc1bf389601457abd3c89",
    f"AF02: ACCEPTED COMPLETE\nAF02 candidate merge: {CANDIDATE_MERGE}\nAF03: READY / NOT STARTED",
)
replace_once(
    "archive/campaign-001/af01/ACCEPTANCE.md",
    "AF02 activation does not grant source reuse, accept any AF02 record, alter P01 implementation authorization work or start AF03.",
    "AF02 acceptance does not grant dependency adoption, alter P01 implementation authorization work or start AF03.",
)

index_path = ROOT / "master-plan-index.json"
index = json.loads(index_path.read_text(encoding="utf-8"))
archive = index["operational_protocols"]["tenfold_archive_formation"]
archive.update({
    "status": "accepted_operational_protocol_af02_complete_af03_ready",
    "accepted_archive_record_count": 19,
    "blocked_archive_record_count": 1,
    "completed_formation_count": 2,
    "af02_status": "accepted_complete",
    "af02_started": True,
    "af02_authorized": True,
    "af02_accepted_archive_record_count": 10,
    "af02_remaining_evidence_count": 0,
    "af02_candidate_exact_head": CANDIDATE_HEAD,
    "af02_candidate_workflow_run": CANDIDATE_RUN,
    "af02_candidate_artifact_id": CANDIDATE_ARTIFACT,
    "af02_candidate_artifact_digest": CANDIDATE_DIGEST,
    "af02_candidate_validation_report_sha256": CANDIDATE_REPORT,
    "af02_candidate_merge": CANDIDATE_MERGE,
    "af02_acceptance_record": "archive/campaign-001/af02/ACCEPTANCE.md",
    "af03_status": "ready_not_started",
    "af03_started": False,
    "af03_authorized": False,
})
index_path.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")

# AF01 remains historical evidence but must acknowledge the subsequent accepted AF02 state.
replace_once(
    "tools/check_archive_af01.py",
    'require(acceptance, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "AF02 subsequent active state")',
    'require(acceptance, "AF02: ACCEPTED COMPLETE", "AF02 subsequent accepted state")\n    require(acceptance, "AF03: READY / NOT STARTED", "AF03 subsequent ready state")',
)

# Promote AF02 validator from candidate to accepted state.
replace_once("tools/check_archive_af02.py", 'RESULT_MD = Path("archive/campaign-001/af02/RESULT.md")', 'RESULT_MD = Path("archive/campaign-001/af02/RESULT.md")\nACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")')
replace_once("tools/check_archive_af02.py", 'result_md = read(root, RESULT_MD)\n    result = json.loads(read(root, RESULT_JSON))', 'result_md = read(root, RESULT_MD)\n    acceptance = read(root, ACCEPTANCE)\n    result = json.loads(read(root, RESULT_JSON))')
replace_once("tools/check_archive_af02.py", 'require(mission, "Status: CANDIDATE COMPLETE", "mission candidate state")', 'require(mission, "Status: ACCEPTED COMPLETE", "mission accepted state")')
replace_once("tools/check_archive_af02.py", 'require(mission, "AF03 is not authorized", "AF03 boundary")', 'require(mission, "AF03 is READY / NOT STARTED", "AF03 ready boundary")')
replace_once("tools/check_archive_af02.py", 'require(result_md, "CANDIDATE COMPLETE", "result candidate state")', 'require(result_md, "ACCEPTED COMPLETE", "result accepted state")\n    require(acceptance, "Status: ACCEPTED EVIDENCE RECORD", "acceptance state")\n    require(acceptance, CANDIDATE_MERGE, "candidate merge evidence")\n    require(acceptance, "AF03: READY / NOT STARTED", "AF03 next state")')
replace_once("tools/check_archive_af02.py", '"status": "candidate_complete_pending_exact_head_review",', '"status": "accepted_complete_non_authorizing",\n        "candidate_exact_head": CANDIDATE_HEAD,\n        "candidate_workflow_run": CANDIDATE_RUN,\n        "candidate_artifact_id": CANDIDATE_ARTIFACT,\n        "candidate_artifact_digest": CANDIDATE_DIGEST,\n        "candidate_validation_report_sha256": CANDIDATE_REPORT,\n        "candidate_merge": CANDIDATE_MERGE,\n        "acceptance_record": str(ACCEPTANCE),')
replace_once("tools/check_archive_af02.py", '"af03_authorized": False,', '"af03_ready": True,\n        "af03_started": False,\n        "af03_authorized": False,',)
replace_once("tools/check_archive_af02.py", 'require(current_state, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "current AF02 active state")', 'require(current_state, "AF02: ACCEPTED COMPLETE", "current AF02 accepted state")\n    require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")')
replace_once("tools/check_archive_af02.py", 'if archive.get("af02_status") != "active" or archive.get("af02_started") is not True:\n        raise ValidationError("machine index AF02 is not active")\n    if archive.get("af02_accepted_archive_record_count") != 0:\n        raise ValidationError("control book pre-accepted AF02 records before closure")\n    if archive.get("af03_started") is not False or archive.get("af03_authorized") is not False:', 'if archive.get("af02_status") != "accepted_complete" or archive.get("af02_started") is not True:\n        raise ValidationError("machine index AF02 is not accepted complete")\n    if archive.get("af02_accepted_archive_record_count") != 10 or archive.get("af02_remaining_evidence_count") != 0:\n        raise ValidationError("machine index AF02 accepted counts are invalid")\n    if archive.get("completed_formation_count") != 2 or archive.get("accepted_archive_record_count") != 19:\n        raise ValidationError("campaign accepted totals are invalid")\n    if archive.get("af03_status") != "ready_not_started" or archive.get("af03_started") is not False or archive.get("af03_authorized") is not False:')
replace_once("tools/check_archive_af02.py", '"status": "candidate_complete_valid_non_authorizing",', '"status": "accepted_complete_valid_non_authorizing",')
replace_once("tools/check_archive_af02.py", '"af03_authorized": False,\n    }', '"af03_ready": True,\n        "af03_started": False,\n        "af03_authorized": False,\n    }')
# Constants inserted near EXPECTED.
replace_once("tools/check_archive_af02.py", 'EXPECTED: dict[str, dict[str, str]] = {', f'CANDIDATE_HEAD = "{CANDIDATE_HEAD}"\nCANDIDATE_RUN = "{CANDIDATE_RUN}"\nCANDIDATE_ARTIFACT = "{CANDIDATE_ARTIFACT}"\nCANDIDATE_DIGEST = "{CANDIDATE_DIGEST}"\nCANDIDATE_REPORT = "{CANDIDATE_REPORT}"\nCANDIDATE_MERGE = "{CANDIDATE_MERGE}"\n\nEXPECTED: dict[str, dict[str, str]] = {{')

# Update AF02 tests to accepted-state expectations.
replace_once("tools/test_check_archive_af02.py", '    RESULT_JSON,\n    RESULT_MD,', '    RESULT_JSON,\n    RESULT_MD,\n    ACCEPTANCE,')
replace_once("tools/test_check_archive_af02.py", '    RESULT_MD,\n    MANIFEST,', '    RESULT_MD,\n    ACCEPTANCE,\n    MANIFEST,')
replace_once("tools/test_check_archive_af02.py", '"candidate_complete_valid_non_authorizing"', '"accepted_complete_valid_non_authorizing"')
replace_once("tools/test_check_archive_af02.py", 'self.assertFalse(result["af03_authorized"])', 'self.assertTrue(result["af03_ready"])\n        self.assertFalse(result["af03_started"])\n        self.assertFalse(result["af03_authorized"])')
replace_once("tools/test_check_archive_af02.py", 'self.replace(root, MISSION, "Status: CANDIDATE COMPLETE", "Status: ACTIVE")', 'self.replace(root, MISSION, "Status: ACCEPTED COMPLETE", "Status: CANDIDATE COMPLETE")')
replace_once("tools/test_check_archive_af02.py", 'archive.__setitem__("af02_accepted_archive_record_count", 10)', 'archive.__setitem__("af02_accepted_archive_record_count", 9)')

# Governing campaign validator recognizes AF02 acceptance and AF03 readiness.
replace_once("tools/check_archive_formation.py", 'AF01_ACCEPTANCE = Path("archive/campaign-001/af01/ACCEPTANCE.md")', 'AF01_ACCEPTANCE = Path("archive/campaign-001/af01/ACCEPTANCE.md")\nAF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")')
replace_once("tools/check_archive_formation.py", '    AF01_ACCEPTANCE,\n)', '    AF01_ACCEPTANCE,\n    AF02_ACCEPTANCE,\n)')
replace_once("tools/check_archive_formation.py", '    af01_acceptance = texts[AF01_ACCEPTANCE]', '    af01_acceptance = texts[AF01_ACCEPTANCE]\n    af02_acceptance = texts[AF02_ACCEPTANCE]')
replace_once("tools/check_archive_formation.py", 'require(current_state, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "current AF02 active state")', 'require(current_state, "AF02: ACCEPTED COMPLETE", "current AF02 accepted state")\n    require(current_state, "AF03: READY / NOT STARTED", "current AF03 ready state")')
replace_once("tools/check_archive_formation.py", 'require(handoff, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "handoff AF02 active state")', 'require(handoff, "AF02: ACCEPTED COMPLETE", "handoff AF02 accepted state")\n    require(handoff, "AF03: READY / NOT STARTED", "handoff AF03 ready state")')
replace_once("tools/check_archive_formation.py", 'require(af01_acceptance, "AF02: ACTIVE / ZERO RECORDS ACCEPTED", "AF02 subsequent state")', 'require(af01_acceptance, "AF02: ACCEPTED COMPLETE", "AF02 subsequent state")\n    require(af01_acceptance, "AF03: READY / NOT STARTED", "AF03 subsequent state")\n    require(af02_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF02 acceptance state")\n    require(af02_acceptance, "58d89dfd1d5348cc8423222e3aff256ee041dce2", "AF02 candidate merge")\n    require(af02_acceptance, "AF03: READY / NOT STARTED", "AF03 next state")')
replace_once("tools/check_archive_formation.py", '"status": "accepted_operational_protocol_af01_complete_af02_active",', '"status": "accepted_operational_protocol_af02_complete_af03_ready",')
replace_once("tools/check_archive_formation.py", '"accepted_archive_record_count": 9,', '"accepted_archive_record_count": 19,')
replace_once("tools/check_archive_formation.py", '"completed_formation_count": 1,\n        "af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_mission": "archive/campaign-001/af02/MISSION.md",\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",', f'"completed_formation_count": 2,\n        "af02_status": "accepted_complete",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_mission": "archive/campaign-001/af02/MISSION.md",\n        "af02_accepted_archive_record_count": 10,\n        "af02_remaining_evidence_count": 0,\n        "af02_candidate_exact_head": "{CANDIDATE_HEAD}",\n        "af02_candidate_workflow_run": "{CANDIDATE_RUN}",\n        "af02_candidate_artifact_id": "{CANDIDATE_ARTIFACT}",\n        "af02_candidate_artifact_digest": "{CANDIDATE_DIGEST}",\n        "af02_candidate_validation_report_sha256": "{CANDIDATE_REPORT}",\n        "af02_candidate_merge": "{CANDIDATE_MERGE}",\n        "af02_acceptance_record": str(AF02_ACCEPTANCE),\n        "af03_status": "ready_not_started",')
replace_once("tools/check_archive_formation.py", '"completed formations: 1",\n        "accepted archive records: 9",\n        "blocked completed outcomes: 1",\n        "active formation: AF02",\n        "AF02 accepted archive records: 0",\n        "AF02 remaining evidence: 10",', '"completed formations: 2",\n        "accepted archive records: 19",\n        "blocked completed outcomes: 1",\n        "next formation: AF03 READY / NOT STARTED",')
replace_once("tools/check_archive_formation.py", '"accepted_archive_record_count": 9,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 1,\n        "af01_status": "accepted_complete",\n        "af02_status": "active",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_accepted_archive_record_count": 0,\n        "af02_remaining_evidence_count": 10,\n        "af03_status": "not_started",', '"accepted_archive_record_count": 19,\n        "blocked_archive_record_count": 1,\n        "completed_formation_count": 2,\n        "af01_status": "accepted_complete",\n        "af02_status": "accepted_complete",\n        "af02_started": True,\n        "af02_authorized": True,\n        "af02_accepted_archive_record_count": 10,\n        "af02_remaining_evidence_count": 0,\n        "af03_status": "ready_not_started",')

# Governing regression expectations.
replace_once("tools/test_check_archive_formation.py", 'self.assertEqual(result["accepted_archive_record_count"], 9)', 'self.assertEqual(result["accepted_archive_record_count"], 19)')
replace_once("tools/test_check_archive_formation.py", 'self.assertEqual(result["completed_formation_count"], 1)', 'self.assertEqual(result["completed_formation_count"], 2)')
replace_once("tools/test_check_archive_formation.py", 'self.assertEqual(result["af02_status"], "active")', 'self.assertEqual(result["af02_status"], "accepted_complete")')
replace_once("tools/test_check_archive_formation.py", 'self.assertEqual(result["af02_accepted_archive_record_count"], 0)', 'self.assertEqual(result["af02_accepted_archive_record_count"], 10)')
replace_once("tools/test_check_archive_formation.py", 'self.assertEqual(result["af02_remaining_evidence_count"], 10)', 'self.assertEqual(result["af02_remaining_evidence_count"], 0)')

print("AF02 acceptance synchronization applied")
