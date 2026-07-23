#!/usr/bin/env python3
"""Validate Campaign 001 AF02 archive evidence without authorizing implementation."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

MISSION = Path("archive/campaign-001/af02/MISSION.md")
CHECKPOINT_05 = Path("archive/campaign-001/af02/CHECKPOINT-05.md")
CHECKPOINT_10 = Path("archive/campaign-001/af02/CHECKPOINT-10.md")
RESULT_JSON = Path("archive/campaign-001/af02/RESULT.json")
RESULT_MD = Path("archive/campaign-001/af02/RESULT.md")
ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")
MANIFEST = Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md")
DONOR_REGISTER = Path("DONOR_RECOVERY.md")
CURRENT_STATE = Path("CURRENT_STATE.md")
MASTER_INDEX = Path("master-plan-index.json")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")

CANDIDATE_HEAD = "b710574b99269647cdd9029db5a2b217642aa344"
CANDIDATE_RUN = "29875542752"
CANDIDATE_ARTIFACT = "8512821506"
CANDIDATE_DIGEST = "sha256:78c5b702aa6025f088e2c54002bbe84fead003c92e0bb98ec18fcd0220b1d81c"
CANDIDATE_REPORT = "e18dac8a154547deb30c4482027b10c40dd892fd8a1024cba78f7366b44c6fd9"
CANDIDATE_MERGE = "58d89dfd1d5348cc8423222e3aff256ee041dce2"

EXPECTED: dict[str, dict[str, str]] = {
    "D062": {"source": "aza-ali/awesome-ai-product-management", "branch": "main", "commit": "b0f971eb38f6f76e5762f0bab5d92df394370b73", "outcome": "accepted_for_archive_research_navigation_only", "primary": "AF02-P01", "verifier": "AF02-V01", "path": "archive/campaign-001/af02/records/D062-AWESOME-AI-PRODUCT-MANAGEMENT.md"},
    "D066": {"source": "aza-ali/github-readme-crisp-links", "branch": "main", "commit": "1503b45546a9b50777e5755aa2368be9297cf719", "outcome": "accepted_for_archive_documentation_tool_only", "primary": "AF02-P02", "verifier": "AF02-V02", "path": "archive/campaign-001/af02/records/D066-GITHUB-README-CRISP-LINKS.md"},
    "D002": {"source": "daytonaio/daytona", "branch": "main", "commit": "ec4c21b2d597091ac09ecc278f3bcc172575a987", "outcome": "accepted_for_archive_with_discontinuation_and_copyleft_restrictions", "primary": "AF02-P03", "verifier": "AF02-V03", "path": "archive/campaign-001/af02/records/D002-DAYTONA.md"},
    "D013": {"source": "e2b-dev/desktop", "branch": "main", "commit": "e4800ef873cacc0eeb91770a419b77de0ea26903", "outcome": "accepted_for_archive_hosted_desktop_adapter_only", "primary": "AF02-P04", "verifier": "AF02-V04", "path": "archive/campaign-001/af02/records/D013-E2B-DESKTOP.md"},
    "D017": {"source": "microsoft/playwright-mcp", "branch": "main", "commit": "55679f5f3d4b4f3e2534ec0ce2fc5683ba2eaf3f", "outcome": "accepted_for_archive_mcp_browser_adapter_only", "primary": "AF02-P05", "verifier": "AF02-V05", "path": "archive/campaign-001/af02/records/D017-PLAYWRIGHT-MCP.md"},
    "D021": {"source": "DeviceFarmer/adbkit", "branch": "master", "commit": "f474b57f6b1b1b41edd4abbfa1dd9bfad6420d6a", "outcome": "accepted_for_archive_with_device_authority_restrictions", "primary": "AF02-P06", "verifier": "AF02-V06", "path": "archive/campaign-001/af02/records/D021-ADBKIT.md"},
    "D031": {"source": "kata-containers/kata-containers", "branch": "main", "commit": "809ab7d90f7dc8c10f51e5b0eef55b9bd33cdbc5", "outcome": "accepted_for_archive_optional_isolation_backend", "primary": "AF02-P07", "verifier": "AF02-V07", "path": "archive/campaign-001/af02/records/D031-KATA-CONTAINERS.md"},
    "D036": {"source": "moby/moby", "branch": "master", "commit": "722d76e76b5363691379ab6fe0ccbc8111f49b0e", "outcome": "accepted_for_archive_modular_engine_donor", "primary": "AF02-P08", "verifier": "AF02-V08", "path": "archive/campaign-001/af02/records/D036-MOBY.md"},
    "D043": {"source": "run-llama/llama_index", "branch": "main", "commit": "d88c2c9ed3cb057e056546c46800adaad16824d1", "outcome": "accepted_for_archive_with_integration_and_knowledge_truth_restrictions", "primary": "AF02-P09", "verifier": "AF02-V09", "path": "archive/campaign-001/af02/records/D043-LLAMAINDEX.md"},
    "D048": {"source": "ray-project/ray", "branch": "master", "commit": "eae2ad02ebdd1b9698e1613f4ef3f683e4e8ebbb", "outcome": "accepted_for_archive_with_distributed_authority_restrictions", "primary": "AF02-P10", "verifier": "AF02-V10", "path": "archive/campaign-001/af02/records/D048-RAY.md"},
}


class ValidationError(RuntimeError):
    pass


def read(root: Path, relative: Path) -> str:
    path = root / relative
    if not path.is_file():
        raise ValidationError(f"missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def require(text: str, token: str, label: str) -> None:
    if token not in text:
        raise ValidationError(f"missing {label}: {token}")


def validate_repo(root: Path) -> dict[str, Any]:
    mission = read(root, MISSION)
    checkpoint05 = read(root, CHECKPOINT_05)
    checkpoint10 = read(root, CHECKPOINT_10)
    result_md = read(root, RESULT_MD)
    acceptance = read(root, ACCEPTANCE)
    result = json.loads(read(root, RESULT_JSON))
    manifest = read(root, MANIFEST)
    donor_register = read(root, DONOR_REGISTER)
    current_state = read(root, CURRENT_STATE)
    master_index = json.loads(read(root, MASTER_INDEX))
    adr0033 = read(root, ADR0033)

    require(mission, "Status: ACCEPTED COMPLETE", "mission accepted state")
    require(mission, "accepted for archive: 10", "mission accepted count")
    require(mission, "remaining in evidence collection: 0", "mission remaining count")
    require(mission, "AF03 is READY / NOT STARTED", "AF03 ready boundary")
    require(checkpoint05, "first five records reconciled", "checkpoint 05 state")
    require(checkpoint10, "all ten assigned records reconciled", "checkpoint 10 state")
    require(checkpoint10, "accepted archive records: 10", "checkpoint 10 accepted count")
    require(result_md, "ACCEPTED COMPLETE", "result accepted state")
    require(acceptance, "Status: ACCEPTED EVIDENCE RECORD", "acceptance state")
    require(acceptance, CANDIDATE_MERGE, "candidate merge evidence")
    require(acceptance, "AF03: READY / NOT STARTED", "AF03 next state")
    require(result_md, "public core development stopped", "Daytona lifecycle correction")

    expected_top = {
        "schema_version": "1.0.0",
        "record_type": "ptah.archive_campaign_formation_result",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF02",
        "status": "accepted_complete_non_authorizing",
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": str(ACCEPTANCE),
        "base_authority_commit": "ccde8b45b333bafed4f55512b3b4e3a39a709721",
        "protocol_version": "1.0.0",
        "assigned_record_count": 10,
        "reconciled_record_count": 10,
        "accepted_archive_record_count": 10,
        "blocked_record_count": 0,
        "parked_record_count": 0,
        "rejected_record_count": 0,
        "remaining_evidence_count": 0,
        "primary_worker_count": 10,
        "verifier_worker_count": 10,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "af03_ready": True,
        "af03_started": False,
        "af03_authorized": False,
    }
    for key, value in expected_top.items():
        if result.get(key) != value:
            raise ValidationError(f"AF02 result mismatch: {key}")

    records = result.get("records")
    if not isinstance(records, list) or len(records) != 10:
        raise ValidationError("AF02 result must contain exactly ten records")
    ids = [record.get("id") for record in records]
    if set(ids) != set(EXPECTED) or len(ids) != len(set(ids)):
        raise ValidationError(f"AF02 record coverage mismatch: {ids}")

    primaries: list[str] = []
    verifiers: list[str] = []
    for record in records:
        record_id = record["id"]
        expected = EXPECTED[record_id]
        for key, value in expected.items():
            if record.get(key) != value:
                raise ValidationError(f"{record_id} mismatch: {key}")
        primaries.append(record["primary"])
        verifiers.append(record["verifier"])
        if not record["outcome"].startswith("accepted_for_archive"):
            raise ValidationError(f"unexpected non-accepted AF02 outcome: {record_id}")

        text = read(root, Path(record["path"]))
        require(text, f"# {record_id} —", f"{record_id} heading")
        require(text, expected["source"], f"{record_id} source")
        require(text, expected["commit"], f"{record_id} commit")
        require(text, f"Primary Archivist: `{expected['primary']}`", f"{record_id} primary")
        require(text, f"Independent Verifier: `{expected['verifier']}`", f"{record_id} verifier")
        require(text, "## Primary evidence packet", f"{record_id} primary packet")
        require(text, "## Independent verification packet", f"{record_id} verifier packet")
        require(text, "## Contradiction and supersession", f"{record_id} contradiction")
        require(text, "## Bounded outcome", f"{record_id} bounded outcome")

        require(manifest, f"`{expected['primary']}` | `{expected['verifier']}`", f"{record_id} exact manifest pair")

    if len(set(primaries)) != 10 or len(set(verifiers)) != 10:
        raise ValidationError("AF02 worker identity reused")
    if set(primaries).intersection(verifiers):
        raise ValidationError("AF02 primary/verifier identities overlap")

    daytona = read(root, Path(EXPECTED["D002"]["path"]))
    require(daytona, "public core development stopped in June 2026", "Daytona discontinuation")
    require(daytona, "v0.190.0", "Daytona public snapshot")
    require(daytona, "AGPL-3.0", "Daytona copyleft boundary")
    adbkit = read(root, Path(EXPECTED["D021"]["path"]))
    require(adbkit, "not an ADB server", "ADBKit server boundary")
    require(adbkit, "explicit device/customer authorization", "ADBKit authorization boundary")
    moby = read(root, Path(EXPECTED["D036"]["path"]))
    require(moby, "not intended as an imported Go library", "Moby root-module boundary")
    llama = read(root, Path(EXPECTED["D043"]["path"]))
    require(llama, "more than 300 separately packaged integrations", "LlamaIndex integration boundary")
    require(llama, "cannot automatically become canonical Ptah Object/Knowledge truth", "LlamaIndex truth boundary")
    ray = read(root, Path(EXPECTED["D048"]["path"]))
    require(ray, "must not become Ptah's global scheduler", "Ray scheduler boundary")
    catalogue = read(root, Path(EXPECTED["D062"]["path"]))
    require(catalogue, "CC0 applies to the catalogue work", "catalogue linked-rights boundary")

    af02_ids = re.findall(r"^\| `(D\d{3})` \|.*\| `AF02-P\d{2}` \| `AF02-V\d{2}` \|$", manifest, re.MULTILINE)
    if af02_ids != list(EXPECTED):
        raise ValidationError(f"campaign manifest AF02 order mismatch: {af02_ids}")
    require(current_state, "AF02: ACCEPTED COMPLETE", "current AF02 accepted state")
    require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")
    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")

    archive = master_index.get("operational_protocols", {}).get("tenfold_archive_formation", {})
    if archive.get("af02_status") != "accepted_complete" or archive.get("af02_started") is not True:
        raise ValidationError("machine index AF02 is not accepted complete")
    if archive.get("af02_accepted_archive_record_count") != 10 or archive.get("af02_remaining_evidence_count") != 0:
        raise ValidationError("machine index AF02 accepted counts are invalid")
    if archive.get("completed_formation_count") != 3 or archive.get("accepted_archive_record_count") != 29:
        raise ValidationError("campaign accepted totals are invalid")
    if archive.get("af03_status") != "accepted_complete" or archive.get("af03_started") is not True or archive.get("af03_authorized") is not True:
        raise ValidationError("AF03 follow-on acceptance is invalid")
    if archive.get("af03_accepted_archive_record_count") != 10 or archive.get("af03_remaining_evidence_count") != 0:
        raise ValidationError("AF03 accepted counts are invalid")
    if archive.get("af04_status") != "ready_not_started" or archive.get("af04_started") is not False or archive.get("af04_authorized") is not False:
        raise ValidationError("AF04 follow-on state is invalid")

    require(donor_register, "**Status:** COMPLETE AND FROZEN", "frozen Phase 0A")
    if "**Status:** REOPENED" in donor_register or "Phase 0A reopened" in donor_register:
        raise ValidationError("Phase 0A was reopened")
    require(current_state, "P01", "active P01")
    require(current_state, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    if "**Runtime implementation:** AUTHORIZED" in current_state:
        raise ValidationError("runtime implementation became authorized")
    require(adr0033, "Status: proposed", "ADR-0033 proposed state")
    if re.search(r"^Status:\s+accepted", adr0033, re.MULTILINE | re.IGNORECASE):
        raise ValidationError("ADR-0033 became accepted")

    return {
        "schema_version": "1.0.0",
        "record_type": "ptah.archive_campaign_af02_validation",
        "status": "accepted_complete_valid_non_authorizing",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF02",
        "record_count": 10,
        "accepted_archive_record_count": 10,
        "blocked_record_count": 0,
        "primary_worker_count": 10,
        "verifier_worker_count": 10,
        "checkpoint_count": 2,
        "remaining_evidence_count": 0,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "af03_accepted": True,
        "af03_started": True,
        "af03_authorized": True,
        "af04_ready": True,
        "af04_started": False,
        "af04_authorized": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    result = validate_repo(Path(args.repo_root).resolve())
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
