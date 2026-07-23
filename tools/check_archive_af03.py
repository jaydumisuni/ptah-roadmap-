#!/usr/bin/env python3
"""Validate Campaign 001 AF03 candidate evidence without accepting AF03."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

MISSION = Path("archive/campaign-001/af03/MISSION.md")
CHECKPOINT_05 = Path("archive/campaign-001/af03/CHECKPOINT-05.md")
CHECKPOINT_10 = Path("archive/campaign-001/af03/CHECKPOINT-10.md")
RESULT_JSON = Path("archive/campaign-001/af03/RESULT.json")
RESULT_MD = Path("archive/campaign-001/af03/RESULT.md")
SERGEANT_REVIEW = Path("archive/campaign-001/af03/SERGEANT-REVIEW.md")
ACCEPTANCE = Path("archive/campaign-001/af03/ACCEPTANCE.md")
MANIFEST = Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md")
DONOR_REGISTER = Path("DONOR_RECOVERY.md")
CURRENT_STATE = Path("CURRENT_STATE.md")
MASTER_INDEX = Path("master-plan-index.json")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")

SERGEANT_TARGET_HEAD = "a6a1d9aa13f619c2f8ff4c1c6c0cadea331df3d6"
SERGEANT_RESULT = "pass_with_mandatory_retained_restrictions"
BASE_AUTHORITY = "a7186bfb45cb885c8afc7165f67641e8725cc989"
CANDIDATE_HEAD = "4916f79ff3a0cbac8ee4ae53f9ac09a0065d7b7d"
CANDIDATE_RUN = "30003085272"
CANDIDATE_ARTIFACT = "8561809711"
CANDIDATE_ARTIFACT_DIGEST = "sha256:fa36506e788958d4b3d134f6f1286e4c2d47d309aa15529e6f1d384c9bdcd6a6"
CANDIDATE_REPORT_SHA256 = "e437e8785a846710e2e2434fb3e537a3566fc6baf68b420da6610dd20571f302"
CANDIDATE_MERGE = "d86218e1127c57bacfb4d88eff15b81d326995ba"

EXPECTED: dict[str, dict[str, str]] = {
    "D052": {"source": "NeoZorK/NeoZorK", "branch": "main", "commit": "a4e38cc6824a18a9dbe0c7bbc786f070d2450b79", "outcome": "accepted_for_archive_research_profile_and_reproducibility_catalogue_only", "primary": "AF03-P01", "verifier": "AF03-V01", "path": "archive/campaign-001/af03/records/D052-NEOZORK-PROJECTS.md"},
    "D059": {"source": "semgrep/semgrep", "branch": "develop", "commit": "b1b15360b40ec84164f077712053b88dc2c38e31", "outcome": "accepted_for_archive_with_lgpl_and_security_finding_restrictions", "primary": "AF03-P02", "verifier": "AF03-V02", "path": "archive/campaign-001/af03/records/D059-SEMGREP.md"},
    "D063": {"source": "tmimmanuel/tmimmanuel", "branch": "main", "commit": "ff77b66da8c75b573da2247034e66f98a0f8b39d", "outcome": "accepted_for_archive_contributor_profile_and_discovery_only", "primary": "AF03-P03", "verifier": "AF03-V03", "path": "archive/campaign-001/af03/records/D063-TMIMMANUEL-PROFILE.md"},
    "D067": {"source": "squidfunk/mkdocs-material", "branch": "master", "commit": "b3e6dd886a974aa8200759ecfd7db28c598a2894", "outcome": "accepted_for_archive_mit_documentation_presentation_framework", "primary": "AF03-P04", "verifier": "AF03-V04", "path": "archive/campaign-001/af03/records/D067-MKDOCS-MATERIAL.md"},
    "D003": {"source": "temporalio/temporal", "branch": "main", "commit": "a813c6193d24b91cce5b929d199e89340d63e2ac", "outcome": "accepted_for_archive_durable_execution_donor_with_identity_and_effect_boundaries", "primary": "AF03-P05", "verifier": "AF03-V05", "path": "archive/campaign-001/af03/records/D003-TEMPORAL.md"},
    "D014": {"source": "coder/coder", "branch": "main", "commit": "591edcb050f384a8ccfba3b04b78d061c7111b92", "outcome": "accepted_for_archive_with_agpl_control_plane_and_premium_surface_restrictions", "primary": "AF03-P06", "verifier": "AF03-V06", "path": "archive/campaign-001/af03/records/D014-CODER.md"},
    "D018": {"source": "browser-use/browser-use", "branch": "main", "commit": "96ec5dc1378d26f7dd155df0cef9d6c3e32752dc", "outcome": "accepted_for_archive_mit_agent_browser_adapter_with_model_and_external_effect_restrictions", "primary": "AF03-P07", "verifier": "AF03-V07", "path": "archive/campaign-001/af03/records/D018-BROWSER-USE.md"},
    "D022": {"source": "DeviceFarmer/minicap", "branch": "master", "commit": "f3d40d65da0cc7168846c4ae7466ada970441d4e", "outcome": "accepted_for_archive_legacy_android_screen_capture_with_private_api_and_compatibility_restrictions", "primary": "AF03-P08", "verifier": "AF03-V08", "path": "archive/campaign-001/af03/records/D022-MINICAP.md"},
    "D032": {"source": "firecracker-microvm/firecracker", "branch": "main", "commit": "ae5bf5b68fc41927b3efeca91d220ab11e01f9dc", "outcome": "accepted_for_archive_optional_kvm_microvm_isolation_provider", "primary": "AF03-P09", "verifier": "AF03-V09", "path": "archive/campaign-001/af03/records/D032-FIRECRACKER.md"},
    "D037": {"source": "docker/cli", "branch": "master", "commit": "7a54334eb038871b45c2377baf8c12beaa14839c", "outcome": "accepted_for_archive_apache_cli_adapter_with_daemon_and_context_boundaries", "primary": "AF03-P10", "verifier": "AF03-V10", "path": "archive/campaign-001/af03/records/D037-DOCKER-CLI.md"},
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


def reject(text: str, token: str, label: str) -> None:
    if token in text:
        raise ValidationError(f"forbidden {label}: {token}")


def validate_repo(root: Path) -> dict[str, Any]:
    mission = read(root, MISSION)
    checkpoint05 = read(root, CHECKPOINT_05)
    checkpoint10 = read(root, CHECKPOINT_10)
    result_md = read(root, RESULT_MD)
    sergeant = read(root, SERGEANT_REVIEW)
    acceptance = read(root, ACCEPTANCE)
    result = json.loads(read(root, RESULT_JSON))
    manifest = read(root, MANIFEST)
    donor = read(root, DONOR_REGISTER)
    current = read(root, CURRENT_STATE)
    index = json.loads(read(root, MASTER_INDEX))
    adr0033 = read(root, ADR0033)

    require(mission, "Status: ACCEPTED COMPLETE", "mission accepted state")
    require(mission, "candidate accepted outcomes: 10", "mission candidate count")
    require(mission, "remaining evidence: 0", "mission remaining count")
    require(mission, SERGEANT_TARGET_HEAD, "mission Sergeant target")
    require(mission, SERGEANT_RESULT, "mission Sergeant result")
    require(mission, "AF03 is accepted complete", "mission acceptance")

    require(checkpoint05, "FIRST FIVE RECORDS RECONCILED", "checkpoint 05 state")
    require(checkpoint10, "ALL TEN ASSIGNED RECORDS RECONCILED", "checkpoint 10 state")
    require(checkpoint10, "candidate accepted outcomes: 10", "checkpoint 10 count")
    require(checkpoint10, "Sergeant review", "checkpoint Sergeant gate")

    require(result_md, "Status: ACCEPTED COMPLETE", "human result state")
    require(result_md, SERGEANT_TARGET_HEAD, "human result Sergeant target")
    require(result_md, SERGEANT_RESULT, "human result Sergeant result")
    require(result_md, "Sergeant found zero blocking findings", "human result no blockers")
    require(result_md, "AF03 was accepted separately", "human result acceptance")

    require(sergeant, "Status: PASS WITH MANDATORY RETAINED RESTRICTIONS", "Sergeant status")
    require(sergeant, SERGEANT_TARGET_HEAD, "Sergeant exact target")
    require(sergeant, SERGEANT_RESULT, "Sergeant machine result")
    require(sergeant, "Sergeant did not participate in producing", "Sergeant independence")
    require(sergeant, "blocking review findings: 0", "Sergeant zero blockers")
    require(sergeant, "does not accept AF03", "Sergeant non-acceptance")

    require(acceptance, "Status: ACCEPTED EVIDENCE RECORD", "acceptance record state")
    require(acceptance, CANDIDATE_HEAD, "acceptance candidate head")
    require(acceptance, CANDIDATE_MERGE, "acceptance candidate merge")
    require(acceptance, "AF04 status: `READY / NOT STARTED`", "acceptance AF04 state")

    expected_top = {
        "schema_version": "1.0.0",
        "record_type": "ptah.archive_campaign_formation_result",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF03",
        "status": "accepted_complete_non_authorizing",
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": str(ACCEPTANCE),
        "base_authority_commit": BASE_AUTHORITY,
        "protocol_version": "1.0.0",
        "efficient_worker_protocol_version": "1.0.0",
        "assigned_record_count": 10,
        "reconciled_record_count": 10,
        "accepted_archive_record_count": 10,
        "blocked_record_count": 0,
        "parked_record_count": 0,
        "rejected_record_count": 0,
        "remaining_evidence_count": 0,
        "primary_worker_count": 10,
        "verifier_worker_count": 10,
        "checkpoint_05": str(CHECKPOINT_05),
        "checkpoint_10": str(CHECKPOINT_10),
        "sergeant_review": str(SERGEANT_REVIEW),
        "sergeant_review_complete": True,
        "sergeant_review_target_head": SERGEANT_TARGET_HEAD,
        "sergeant_review_result": SERGEANT_RESULT,
        "sergeant_blocking_finding_count": 0,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "af03_accepted": True,
        "af04_status": "ready_not_started",
        "af04_started": False,
        "af04_authorized": False,
    }
    for key, value in expected_top.items():
        if result.get(key) != value:
            raise ValidationError(f"AF03 result mismatch: {key}")

    records = result.get("records")
    if not isinstance(records, list) or len(records) != 10:
        raise ValidationError("AF03 result must contain exactly ten records")
    ids = [record.get("id") for record in records]
    if ids != list(EXPECTED) or len(ids) != len(set(ids)):
        raise ValidationError(f"AF03 record coverage/order mismatch: {ids}")

    primaries: list[str] = []
    verifiers: list[str] = []
    for record in records:
        record_id = record["id"]
        expected = EXPECTED[record_id]
        for key, value in expected.items():
            if record.get(key) != value:
                raise ValidationError(f"{record_id} mismatch: {key}")
        if not record["outcome"].startswith("accepted_for_archive"):
            raise ValidationError(f"unexpected AF03 outcome: {record_id}")
        primaries.append(record["primary"])
        verifiers.append(record["verifier"])

        text = read(root, Path(record["path"]))
        require(text, f"# {record_id} —", f"{record_id} heading")
        require(text, expected["source"], f"{record_id} source")
        require(text, expected["commit"], f"{record_id} exact commit")
        require(text, f"Primary Archivist: `{expected['primary']}`", f"{record_id} primary")
        require(text, f"Independent Verifier: `{expected['verifier']}`", f"{record_id} verifier")
        require(text, "## Primary evidence packet", f"{record_id} primary packet")
        require(text, "## Independent verification packet", f"{record_id} verifier packet")
        require(text, "## Contradiction and supersession", f"{record_id} contradiction")
        require(text, "## Bounded outcome", f"{record_id} bounded outcome")
        require(text, expected["outcome"], f"{record_id} outcome")
        require(manifest, f"`{expected['primary']}` | `{expected['verifier']}`", f"{record_id} manifest pair")

    if len(set(primaries)) != 10 or len(set(verifiers)) != 10:
        raise ValidationError("AF03 worker identity reused")
    if set(primaries).intersection(verifiers):
        raise ValidationError("AF03 primary/verifier identities overlap")

    af03_ids = re.findall(r"^\| `(D\d{3})` \|.*\| `AF03-P\d{2}` \| `AF03-V\d{2}` \|$", manifest, re.MULTILINE)
    if af03_ids != list(EXPECTED):
        raise ValidationError(f"campaign manifest AF03 order mismatch: {af03_ids}")

    # Mandatory retained restrictions.
    d052 = read(root, Path(EXPECTED["D052"]["path"]))
    require(d052, "root `LICENSE`: absent", "D052 no-licence evidence")
    require(d052, "do not copy or adapt profile text", "D052 reuse restriction")
    d059 = read(root, Path(EXPECTED["D059"]["path"]))
    require(d059, "LGPL-2.1", "D059 LGPL boundary")
    require(d059, "do not treat findings as final vulnerability truth", "D059 non-verdict boundary")
    d063 = read(root, Path(EXPECTED["D063"]["path"]))
    require(d063, "root `LICENSE`: absent", "D063 no-licence evidence")
    require(d063, "exact upstream evidence", "D063 upstream proof boundary")
    d067 = read(root, Path(EXPECTED["D067"]["path"]))
    require(d067, "successful build as proof that documentation content is accurate or approved", "D067 presentation boundary")
    d003 = read(root, Path(EXPECTED["D003"]["path"]))
    require(d003, "do not map Temporal Workflow or Activity IDs directly", "D003 identity boundary")
    require(d003, "do not treat retry completion", "D003 effect boundary")
    d014 = read(root, Path(EXPECTED["D014"]["path"]))
    require(d014, "AGPL-3.0", "D014 AGPL boundary")
    require(d014, "Premium features", "D014 premium boundary")
    d018 = read(root, Path(EXPECTED["D018"]["path"]))
    require(d018, "hosted Browser Use capabilities", "D018 hosted boundary")
    require(d018, "post-condition evidence", "D018 external-effect boundary")
    d022 = read(root, Path(EXPECTED["D022"]["path"]))
    require(d022, "private Android APIs", "D022 private API boundary")
    require(d022, "do not claim modern Android, emulator or universal-device compatibility", "D022 compatibility boundary")
    d032 = read(root, Path(EXPECTED["D032"]["path"]))
    require(d032, "requires Linux KVM", "D032 KVM boundary")
    require(d032, "do not treat API start acknowledgement as guest workload success", "D032 acknowledgement boundary")
    d037 = read(root, Path(EXPECTED["D037"]["path"]))
    require(d037, "not Docker Engine", "D037 daemon boundary")
    require(d037, "do not treat CLI success as workload", "D037 success boundary")

    # Accepted package must retain its separate promotion record.
    if not (root / ACCEPTANCE).is_file():
        raise ValidationError("AF03 acceptance record is missing")
    af04 = manifest.split("## AF04", 1)[1].split("## AF05", 1)[0]
    require(af04, "- status: READY / NOT STARTED", "AF04 ready state")
    reject(af04, "- status: ACTIVE", "AF04 activation")
    reject(af04, "- status: ACCEPTED", "AF04 acceptance")

    require(donor, "**Status:** COMPLETE AND FROZEN", "Phase 0A frozen")
    reject(donor, "**Status:** REOPENED", "Phase 0A reopened")
    require(adr0033, "Status: proposed", "ADR-0033 proposed")
    if re.search(r"^Status:\s+accepted", adr0033, re.MULTILINE | re.IGNORECASE):
        raise ValidationError("ADR-0033 became accepted")
    require(current, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    reject(current, "**Runtime implementation:** AUTHORIZED", "runtime authorization")

    # Until a separate control-state synchronization is reviewed, operative totals stay unchanged.
    archive = index.get("operational_protocols", {}).get("tenfold_archive_formation", {})
    if archive.get("accepted_archive_record_count") != 29 or archive.get("completed_formation_count") != 3:
        raise ValidationError("AF03 accepted campaign totals are invalid")
    if archive.get("af03_status") != "accepted_complete" or archive.get("af03_started") is not True or archive.get("af03_authorized") is not True:
        raise ValidationError("AF03 is not accepted in the machine index")
    if archive.get("af04_status") != "ready_not_started" or archive.get("af04_started") is not False or archive.get("af04_authorized") is not False:
        raise ValidationError("AF04 state is invalid")

    return {
        "schema_version": "1.0.0",
        "record_type": "ptah.archive_campaign_af03_validation",
        "status": "accepted_complete_valid_non_authorizing",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF03",
        "record_count": 10,
        "accepted_archive_record_count": 10,
        "candidate_exact_head": CANDIDATE_HEAD,
        "candidate_workflow_run": CANDIDATE_RUN,
        "candidate_artifact_id": CANDIDATE_ARTIFACT,
        "candidate_artifact_digest": CANDIDATE_ARTIFACT_DIGEST,
        "candidate_validation_report_sha256": CANDIDATE_REPORT_SHA256,
        "candidate_merge": CANDIDATE_MERGE,
        "acceptance_record": str(ACCEPTANCE),
        "blocked_record_count": 0,
        "primary_worker_count": 10,
        "verifier_worker_count": 10,
        "checkpoint_count": 2,
        "remaining_evidence_count": 0,
        "sergeant_review_complete": True,
        "sergeant_review_result": SERGEANT_RESULT,
        "sergeant_blocking_finding_count": 0,
        "af03_accepted": True,
        "af04_started": False,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
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
