#!/usr/bin/env python3
"""Bind the operative Phase 0C-17 / ADR-0035 merge into recovery authority."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPERATIVE_MERGE = "40ca127c6d3054bda785061090acefaefcf4cd42"
ACCEPTED_HEAD = "b96b84d17cf03e905bd0b1baf3c46b8aec09334a"
ACCEPTED_RUN = "29855000427"
ACCEPTED_ARTIFACT = "8504901567"
ACCEPTED_ARTIFACT_DIGEST = "sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2"
ACCEPTED_REPORT_DIGEST = "21d5338a7049dbc3a3af2e684efa21e19c281c52355007346291c74dfb7a1d3a"
ACCEPTANCE_RECORD = "planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md"


class SyncError(RuntimeError):
    pass


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def sync_handoff() -> None:
    path = ROOT / "AI_HANDOFF.md"
    replace_once(
        path,
        "protocol version: 1.0.0\ncandidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752\nAF01: READY / NOT STARTED",
        f"protocol version: 1.0.0\ncandidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752\noperative acceptance merge: {OPERATIVE_MERGE}\nAF01: READY / NOT STARTED",
        "handoff operative merge",
    )
    replace_once(
        path,
        "Evidence: exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`, run `29853954659`, artifact `8504497355`, digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`.",
        f"Candidate evidence: exact head `58b577b6793ec28de084e6d712c3c1e88bfe2d3a`, run `29853954659`, artifact `8504497355`, digest `sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4`.\n\nAccepted-state evidence: exact head `{ACCEPTED_HEAD}`, run `{ACCEPTED_RUN}`, artifact `{ACCEPTED_ARTIFACT}`, digest `{ACCEPTED_ARTIFACT_DIGEST}`. Operative merge: `{OPERATIVE_MERGE}`. Full record: `{ACCEPTANCE_RECORD}`.",
        "handoff accepted evidence",
    )


def sync_current_state() -> None:
    path = ROOT / "CURRENT_STATE.md"
    replace_once(
        path,
        "campaign: archive/CAMPAIGN-001-FORMATION-MANIFEST.md\ncandidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752",
        f"campaign: archive/CAMPAIGN-001-FORMATION-MANIFEST.md\ncandidate merge: c4973cbf4d02a34f14a7aefa85b8e2ea7b392752\noperative acceptance merge: {OPERATIVE_MERGE}",
        "current state operative merge",
    )
    replace_once(
        path,
        "- 21 regression cases and exact-head validation passed;\n- exact fifteen-file boundary directly reviewed.",
        f"- 21 candidate regression cases and exact-head validation passed;\n- exact fifteen-file candidate boundary directly reviewed;\n- accepted exact head `{ACCEPTED_HEAD}` passed 23 regression cases in run `{ACCEPTED_RUN}`;\n- retained accepted artifact `{ACCEPTED_ARTIFACT}` with digest `{ACCEPTED_ARTIFACT_DIGEST}`;\n- accepted validation report SHA-256 `{ACCEPTED_REPORT_DIGEST}`;\n- operative acceptance merge `{OPERATIVE_MERGE}`;\n- full acceptance record `{ACCEPTANCE_RECORD}`.",
        "current accepted evidence",
    )


def sync_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise SyncError("active P01 work drifted")
    archive = data["operational_protocols"]["tenfold_archive_formation"]
    if archive.get("status") != "accepted_operational_protocol_af01_ready":
        raise SyncError("archive protocol is not accepted")
    if archive.get("accepted_archive_record_count") != 0:
        raise SyncError("archive records were pre-accepted")
    archive.update(
        {
            "accepted_state_exact_head": ACCEPTED_HEAD,
            "accepted_state_workflow_run": ACCEPTED_RUN,
            "accepted_state_artifact_id": ACCEPTED_ARTIFACT,
            "accepted_state_artifact_digest": ACCEPTED_ARTIFACT_DIGEST,
            "accepted_state_validation_report_sha256": ACCEPTED_REPORT_DIGEST,
            "operative_acceptance_merge": OPERATIVE_MERGE,
            "acceptance_record": ACCEPTANCE_RECORD,
        }
    )
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sync_validator() -> None:
    path = ROOT / "tools/check_archive_formation.py"
    replace_once(
        path,
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")',
        'ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")\nACCEPTANCE_RECORD = Path("planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md")',
        "validator acceptance record constant",
    )
    replace_once(
        path,
        "    MASTER_INDEX,\n    ADR0033,\n)",
        "    MASTER_INDEX,\n    ADR0033,\n    ACCEPTANCE_RECORD,\n)",
        "validator required acceptance record",
    )
    replace_once(
        path,
        "    adr0033 = texts[ADR0033]\n",
        "    adr0033 = texts[ADR0033]\n    acceptance_record = texts[ACCEPTANCE_RECORD]\n",
        "validator acceptance record text",
    )
    anchor = '    require(adr0033, "Status: proposed", "ADR-0033 proposed state")\n'
    check = f'''    require(acceptance_record, "Status: accepted evidence record", "acceptance record state")
    require(acceptance_record, "{OPERATIVE_MERGE}", "operative acceptance merge")
    require(acceptance_record, "accepted archive record count `0`", "zero accepted archive records")

'''
    replace_once(path, anchor, check + anchor, "validator acceptance evidence checks")
    replace_once(
        path,
        '        "accepted_archive_record_count": 0,\n    }',
        f'        "accepted_archive_record_count": 0,\n        "accepted_state_exact_head": "{ACCEPTED_HEAD}",\n        "accepted_state_workflow_run": "{ACCEPTED_RUN}",\n        "accepted_state_artifact_id": "{ACCEPTED_ARTIFACT}",\n        "accepted_state_artifact_digest": "{ACCEPTED_ARTIFACT_DIGEST}",\n        "accepted_state_validation_report_sha256": "{ACCEPTED_REPORT_DIGEST}",\n        "operative_acceptance_merge": "{OPERATIVE_MERGE}",\n        "acceptance_record": str(ACCEPTANCE_RECORD),\n    }}',
        "validator machine acceptance evidence",
    )


def main() -> int:
    sync_handoff()
    sync_current_state()
    sync_index()
    sync_validator()

    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    donor = (ROOT / "DONOR_RECOVERY.md").read_text(encoding="utf-8")
    adr0033 = (ROOT / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md").read_text(encoding="utf-8")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current or "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("runtime non-authorization boundary failed")
    if "**Status:** COMPLETE AND FROZEN" not in donor:
        raise SyncError("Phase 0A donor register is not frozen")
    if "Status: proposed" not in adr0033:
        raise SyncError("ADR-0033 is not proposed")

    print("operative tenfold archive acceptance merge synchronized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
