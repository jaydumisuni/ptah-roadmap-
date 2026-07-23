#!/usr/bin/env python3
"""Validate the non-authorizing Ptah tenfold archive formation package."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SERGEANT_COMMIT = "44c8f47f4bb50a73ef3b4d81d7b849a5aab37dfd"
PROTOCOL = Path("planning/PTAH-TENFOLD-ARCHIVE-FORMATION-PROTOCOL.md")
MANIFEST = Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md")
TEMPLATE = Path("archive/ARCHIVE-RECORD-TEMPLATE.md")
ADR = Path("decisions/ADR-0035-TENFOLD-ARCHIVE-FORMATION-AND-EVIDENCE-PROMOTION.md")
WORK_PACKAGE = Path("work-packages/PHASE-0C-17-TENFOLD-ARCHIVE-FORMATION.md")
DONOR_REGISTER = Path("DONOR_RECOVERY.md")
MEMORY_PROTOCOL = Path("MEMORY_PROTOCOL.md")
DECISIONS = Path("DECISIONS.md")
PROGRESS = Path("PROGRESS.md")
CURRENT_STATE = Path("CURRENT_STATE.md")
AI_HANDOFF = Path("AI_HANDOFF.md")
MASTER_INDEX = Path("master-plan-index.json")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")
ACCEPTANCE_RECORD = Path("planning/TENFOLD-ARCHIVE-AUTHORITY-ACCEPTANCE-MERGE.md")
AF01_ACCEPTANCE = Path("archive/campaign-001/af01/ACCEPTANCE.md")
AF02_ACCEPTANCE = Path("archive/campaign-001/af02/ACCEPTANCE.md")
AF03_ACCEPTANCE = Path("archive/campaign-001/af03/ACCEPTANCE.md")

REQUIRED_FILES = (
    PROTOCOL,
    MANIFEST,
    TEMPLATE,
    ADR,
    WORK_PACKAGE,
    DONOR_REGISTER,
    MEMORY_PROTOCOL,
    DECISIONS,
    PROGRESS,
    CURRENT_STATE,
    AI_HANDOFF,
    MASTER_INDEX,
    ADR0033,
    ACCEPTANCE_RECORD,
    AF01_ACCEPTANCE,
    AF02_ACCEPTANCE,
    AF03_ACCEPTANCE,
)

ROW_RE = re.compile(
    r"^\| `(?P<record>[DI]\d{3})` \| (?P<name>.*?) \| (?P<family>.*?) \| "
    r"`(?P<primary>AF\d{2}-P\d{2})` \| `(?P<verifier>AF\d{2}-V\d{2})` \|$",
    re.MULTILINE,
)
RESERVE_RE = re.compile(
    r"^\| reserve \| overflow/complexity escalation \| reserve \| "
    r"`(?P<primary>AF\d{2}-P\d{2})` \| `(?P<verifier>AF\d{2}-V\d{2})` \|$",
    re.MULTILINE,
)
FORMATION_RE = re.compile(r"^## (AF\d{2})$", re.MULTILINE)


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
    texts = {relative: read(root, relative) for relative in REQUIRED_FILES}
    protocol = texts[PROTOCOL]
    manifest = texts[MANIFEST]
    template = texts[TEMPLATE]
    adr = texts[ADR]
    work_package = texts[WORK_PACKAGE]
    donor_register = texts[DONOR_REGISTER]
    memory_protocol = texts[MEMORY_PROTOCOL]
    decisions = texts[DECISIONS]
    progress = texts[PROGRESS]
    current_state = texts[CURRENT_STATE]
    handoff = texts[AI_HANDOFF]
    master_index = json.loads(texts[MASTER_INDEX])
    adr0033 = texts[ADR0033]
    acceptance_record = texts[ACCEPTANCE_RECORD]
    af01_acceptance = texts[AF01_ACCEPTANCE]
    af02_acceptance = texts[AF02_ACCEPTANCE]
    af03_acceptance = texts[AF03_ACCEPTANCE]

    # Exact borrowed source and force doctrine.
    for document, label in (
        (protocol, "protocol"),
        (adr, "ADR-0035"),
        (work_package, "Phase 0C-17"),
    ):
        require(document, SERGEANT_COMMIT, f"{label} Sergeant pin")
        require(document, "multiplier", f"{label} force multiplier doctrine")
        require(document, "minimum", f"{label} minimum formation doctrine")

    require(protocol, "private force = max(20, human-equivalent workers × 10)", "force equation")
    require(protocol, "Focused | 2 | 20", "focused formation")
    require(protocol, "Component | 4 or more | 40+", "component formation")
    require(protocol, "Subsystem | 6 or more | 60+", "subsystem formation")
    require(protocol, "System | 8–10 or more | 80–100+", "system formation")
    require(protocol, "Complex large | up to 12 | up to 120", "complex formation")
    require(protocol, "after every five reconciled records", "five-record checkpoint")
    require(protocol, "after every ten accepted records", "ten-record checkpoint")
    require(protocol, "They may not:", "private authority boundary")
    require(protocol, "declare a donor adopted or rejected", "private verdict prohibition")
    require(protocol, "does not mean the source is adopted", "archive/adoption separation")

    # Template must preserve evidence, challenge, privacy and bounded outcome.
    for token in (
        "Primary evidence packet",
        "Independent verification packet",
        "Contradiction and supersession",
        "Privacy and retention",
        "Archive Officer outcome",
        "does not by itself",
    ):
        require(template, token, "archive template boundary")

    # Candidate states and non-authorizing boundary.
    require(adr, "Status: accepted", "ADR-0035 accepted state")
    require(work_package, "Status: accepted and complete", "Phase 0C-17 accepted state")
    require(donor_register, "Status:** COMPLETE AND FROZEN", "frozen Phase 0A donor register")
    require(donor_register, "Tenfold archival-completeness rule", "donor archive protocol link")
    require(donor_register, "69 external and 29 internal", "donor campaign coverage")
    if "Phase 0A reopened" in donor_register or "Status:** REOPENED" in donor_register:
        raise ValidationError("Phase 0A donor register was reopened")

    require(memory_protocol, "## 5.1 Tenfold archive formation rule", "memory archive rule")
    require(memory_protocol, "private force = max(20, human-equivalent workers × 10)", "memory force equation")
    require(memory_protocol, "after five reconciled records", "memory five-record checkpoint")
    require(memory_protocol, "after ten accepted records", "memory ten-record checkpoint")

    require(decisions, "### D-051 — Tenfold archive formation separates parallel evidence from promotion authority", "accepted decision index entry")
    require(decisions, "**ACCEPTED.**", "ADR-0035 accepted index state")
    require(progress, "## Tenfold archive formation — accepted", "progress archive section")
    require(progress, "200 private slots allocated", "progress force count")
    require(progress, "AF01 completed ten paired source reviews", "progress AF01 accepted state")
    require(progress, "AF02 completed ten paired source reviews", "progress AF02 accepted state")
    require(progress, "AF03 accepted complete", "progress AF03 accepted state")
    require(progress, "AF04 is READY / NOT STARTED", "progress AF04 ready state")

    require(current_state, "P01", "active P01 physical-host work")
    require(current_state, "## Accepted Phase 0C-17 tenfold archive formation", "current archive acceptance")
    require(current_state, "ADR-0035: ACCEPTED", "current accepted ADR")
    require(current_state, "AF01: ACCEPTED COMPLETE", "current AF01 accepted state")
    require(current_state, "AF02: ACCEPTED COMPLETE", "current AF02 accepted state")
    require(current_state, "AF03: ACCEPTED COMPLETE", "current AF03 accepted state")
    require(current_state, "AF04: READY / NOT STARTED", "current AF04 ready state")
    require(current_state, "replace P01 as the active implementation-authorization work", "current P01 boundary")
    require(current_state, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    if "**Runtime implementation:** AUTHORIZED" in current_state:
        raise ValidationError("runtime implementation became authorized")

    require(handoff, "## Accepted cross-cutting archive formation", "handoff archive acceptance")
    require(handoff, "ADR-0035: ACCEPTED", "handoff accepted ADR")
    require(handoff, "AF01: ACCEPTED COMPLETE", "handoff AF01 accepted state")
    require(handoff, "AF02: ACCEPTED COMPLETE", "handoff AF02 accepted state")
    require(handoff, "AF03: ACCEPTED COMPLETE", "handoff AF03 accepted state")
    require(handoff, "AF04: READY / NOT STARTED", "handoff AF04 ready state")
    require(handoff, "Campaign 001 covers 98 source obligations", "handoff campaign scope")
    require(handoff, "P01 physical-host closure remains the exact next authorization action", "handoff P01 boundary")

    require(acceptance_record, "Status: accepted evidence record", "acceptance record state")
    require(acceptance_record, "40ca127c6d3054bda785061090acefaefcf4cd42", "operative acceptance merge")
    require(acceptance_record, "accepted archive record count `0`", "initial zero accepted archive records")
    require(af01_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF01 acceptance record state")
    require(af01_acceptance, "0a35a8a904bdf235fa4989ea05b684443d5a879a", "AF01 candidate merge")
    require(af01_acceptance, "operative AF01 acceptance merge: `ea2424bb5bc2bdb698bfc1bf389601457abd3c89`", "AF01 operative merge")
    require(af01_acceptance, "AF02: ACCEPTED COMPLETE", "AF02 subsequent state")
    require(af01_acceptance, "AF03: READY / NOT STARTED", "AF03 subsequent state")
    require(af02_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF02 acceptance state")
    require(af02_acceptance, "58d89dfd1d5348cc8423222e3aff256ee041dce2", "AF02 candidate merge")
    require(af02_acceptance, "AF03: READY / NOT STARTED", "historical AF03 state at AF02 acceptance")
    require(af03_acceptance, "Status: ACCEPTED EVIDENCE RECORD", "AF03 acceptance state")
    require(af03_acceptance, "d86218e1127c57bacfb4d88eff15b81d326995ba", "AF03 candidate merge")
    require(af03_acceptance, "AF04 status: `READY / NOT STARTED`", "AF04 next state")

    require(adr0033, "Status: proposed", "ADR-0033 proposed state")
    if re.search(r"^Status:\s+accepted", adr0033, re.MULTILINE | re.IGNORECASE):
        raise ValidationError("ADR-0033 became accepted")

    # Machine-readable recovery index must preserve active authorization work.
    if master_index.get("active_work_unit") != "P01-physical-host-and-ADR-0033-closure":
        raise ValidationError("master-plan index active work unit drifted")
    if master_index.get("runtime_implementation_authorized") is not False:
        raise ValidationError("master-plan index authorized runtime")
    if str(PROTOCOL) not in master_index.get("recovery_order", []):
        raise ValidationError("archive protocol missing from machine recovery order")
    archive_index = master_index.get("operational_protocols", {}).get("tenfold_archive_formation")
    if not isinstance(archive_index, dict):
        raise ValidationError("archive protocol missing from machine index")
    expected_index = {
        "status": "accepted_operational_protocol_af03_complete_af04_ready",
        "source_branch": "main",
        "pull_request": 26,
        "protocol": str(PROTOCOL),
        "campaign_manifest": str(MANIFEST),
        "record_template": str(TEMPLATE),
        "work_package": str(WORK_PACKAGE),
        "decision": str(ADR),
        "sergeant_source_commit": SERGEANT_COMMIT,
        "private_force_multiplier": 10,
        "minimum_private_force": 20,
        "formation_count": 10,
        "allocated_private_count": 200,
        "assigned_record_count": 98,
        "phase_0a_reopened": False,
        "runtime_implementation_authorized": False,
        "protocol_version": "1.0.0",
        "candidate_exact_head": "58b577b6793ec28de084e6d712c3c1e88bfe2d3a",
        "candidate_workflow_run": "29853954659",
        "candidate_artifact_id": "8504497355",
        "candidate_artifact_digest": "sha256:936740e8087e6f7f0a58b3d731117fcb9a4861edfd20c396fb1bb20a7d4f18f4",
        "validation_report_sha256": "de38af1e63a76e02552e4f93ad2bac2d86d05239a77dc92cc27d794a8b9b010f",
        "candidate_merge": "c4973cbf4d02a34f14a7aefa85b8e2ea7b392752",
        "adr_0035_accepted": True,
        "phase0c_17_complete": True,
        "af01_status": "accepted_complete",
        "accepted_archive_record_count": 29,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 3,
        "af02_status": "accepted_complete",
        "af02_started": True,
        "af02_authorized": True,
        "af02_mission": "archive/campaign-001/af02/MISSION.md",
        "af02_accepted_archive_record_count": 10,
        "af02_remaining_evidence_count": 0,
        "af02_candidate_exact_head": "b710574b99269647cdd9029db5a2b217642aa344",
        "af02_candidate_workflow_run": "29875542752",
        "af02_candidate_artifact_id": "8512821506",
        "af02_candidate_artifact_digest": "sha256:78c5b702aa6025f088e2c54002bbe84fead003c92e0bb98ec18fcd0220b1d81c",
        "af02_candidate_validation_report_sha256": "e18dac8a154547deb30c4482027b10c40dd892fd8a1024cba78f7366b44c6fd9",
        "af02_candidate_merge": "58d89dfd1d5348cc8423222e3aff256ee041dce2",
        "af02_acceptance_record": str(AF02_ACCEPTANCE),
        "af03_status": "accepted_complete",
        "af03_started": True,
        "af03_authorized": True,
        "af03_accepted_archive_record_count": 10,
        "af03_blocked_record_count": 0,
        "af03_remaining_evidence_count": 0,
        "af03_candidate_exact_head": "4916f79ff3a0cbac8ee4ae53f9ac09a0065d7b7d",
        "af03_candidate_workflow_run": "30003085272",
        "af03_candidate_artifact_id": "8561809711",
        "af03_candidate_artifact_digest": "sha256:fa36506e788958d4b3d134f6f1286e4c2d47d309aa15529e6f1d384c9bdcd6a6",
        "af03_candidate_validation_report_sha256": "e437e8785a846710e2e2434fb3e537a3566fc6baf68b420da6610dd20571f302",
        "af03_candidate_merge": "d86218e1127c57bacfb4d88eff15b81d326995ba",
        "af03_acceptance_record": str(AF03_ACCEPTANCE),
        "af03_sergeant_review_result": "pass_with_mandatory_retained_restrictions",
        "af03_sergeant_blocking_finding_count": 0,
        "af04_status": "ready_not_started",
        "af04_started": False,
        "af04_authorized": False,
        "accepted_state_exact_head": "b96b84d17cf03e905bd0b1baf3c46b8aec09334a",
        "accepted_state_workflow_run": "29855000427",
        "accepted_state_artifact_id": "8504901567",
        "accepted_state_artifact_digest": "sha256:9d96a1f299060e50ab63132d1bb1da0903d5435f73acdf4fa9e394cdcccf21d2",
        "accepted_state_validation_report_sha256": "21d5338a7049dbc3a3af2e684efa21e19c281c52355007346291c74dfb7a1d3a",
        "operative_acceptance_merge": "40ca127c6d3054bda785061090acefaefcf4cd42",
        "acceptance_record": str(ACCEPTANCE_RECORD),
        "af01_candidate_exact_head": "f60e340cb856d50e88b4279147a933d838fce759",
        "af01_candidate_workflow_run": "29862087745",
        "af01_candidate_artifact_id": "8507695005",
        "af01_candidate_artifact_digest": "sha256:4ea6bf77131834b48b9e35ad5eb88538a87b6f376f2be4984f077eb3eeed1267",
        "af01_candidate_validation_report_sha256": "4a8cf20f3aacf8628c1de1b774cc93018705d0aa256a65208a8abf4311edc691",
        "af01_candidate_merge": "0a35a8a904bdf235fa4989ea05b684443d5a879a",
        "af01_acceptance_record": str(AF01_ACCEPTANCE),
        "af01_acceptance_merge": "ea2424bb5bc2bdb698bfc1bf389601457abd3c89",
    }
    for key, value in expected_index.items():
        if archive_index.get(key) != value:
            raise ValidationError(f"machine archive protocol mismatch: {key}")

    # Manifest counts and formations.
    for token in (
        "external obligations: 69",
        "internal THETECHGUY obligations: 29",
        "total obligations: 98",
        "standard formations: 10",
        "allocated privates: 200",
        "private verdict authority: none",
        "no Phase 0A reopening",
        "no runtime authorization",
        "completed formations: 3",
        "accepted archive records: 29",
        "blocked completed outcomes: 1",
        "next formation: AF04 READY / NOT STARTED",
    ):
        require(manifest, token, "manifest invariant")

    formations = FORMATION_RE.findall(manifest)
    expected_formations = [f"AF{i:02d}" for i in range(1, 11)]
    if formations != expected_formations:
        raise ValidationError(f"formation sequence mismatch: {formations}")

    rows = [match.groupdict() for match in ROW_RE.finditer(manifest)]
    reserves = [match.groupdict() for match in RESERVE_RE.finditer(manifest)]
    if len(rows) != 98:
        raise ValidationError(f"expected 98 assigned records, found {len(rows)}")
    if len(reserves) != 2:
        raise ValidationError(f"expected two reserve pairs, found {len(reserves)}")

    record_ids = [row["record"] for row in rows]
    expected_ids = [f"D{i:03d}" for i in range(1, 70)] + [f"I{i:03d}" for i in range(1, 30)]
    if sorted(record_ids) != sorted(expected_ids):
        missing = sorted(set(expected_ids) - set(record_ids))
        extra = sorted(set(record_ids) - set(expected_ids))
        raise ValidationError(f"record coverage mismatch; missing={missing}, extra={extra}")
    if len(set(record_ids)) != len(record_ids):
        raise ValidationError("duplicate archive record assignment")

    primary_workers = [row["primary"] for row in rows] + [row["primary"] for row in reserves]
    verifier_workers = [row["verifier"] for row in rows] + [row["verifier"] for row in reserves]
    if len(primary_workers) != 100 or len(verifier_workers) != 100:
        raise ValidationError("worker formation must contain 100 primary and 100 verifier slots")
    if len(set(primary_workers)) != 100:
        raise ValidationError("primary worker reused")
    if len(set(verifier_workers)) != 100:
        raise ValidationError("verifier worker reused")
    if set(primary_workers).intersection(verifier_workers):
        raise ValidationError("primary and verifier worker identities overlap")

    assigned_by_formation: dict[str, int] = {formation: 0 for formation in expected_formations}
    for row in rows:
        primary_formation = row["primary"].split("-", 1)[0]
        verifier_formation = row["verifier"].split("-", 1)[0]
        if primary_formation != verifier_formation:
            raise ValidationError(f"record pair crosses formations: {row['record']}")
        assigned_by_formation[primary_formation] += 1
    for reserve in reserves:
        if reserve["primary"].split("-", 1)[0] != "AF10" or reserve["verifier"].split("-", 1)[0] != "AF10":
            raise ValidationError("reserve pairs must belong to AF10")

    expected_counts = {f"AF{i:02d}": 10 for i in range(1, 10)} | {"AF10": 8}
    if assigned_by_formation != expected_counts:
        raise ValidationError(f"formation assignment count mismatch: {assigned_by_formation}")

    for formation in expected_formations:
        section_start = manifest.index(f"## {formation}")
        next_heading = manifest.find("\n## ", section_start + 4)
        section = manifest[section_start:] if next_heading == -1 else manifest[section_start:next_heading]
        require(section, "private count: 20", f"{formation} private count")

    result = {
        "schema_version": "1.0.0",
        "record_type": "ptah.phase0c.archive_formation_validation",
        "status": "accepted_valid_non_authorizing",
        "sergeant_source_commit": SERGEANT_COMMIT,
        "private_force_multiplier": 10,
        "minimum_private_force": 20,
        "formation_count": 10,
        "allocated_private_count": 200,
        "assigned_record_count": 98,
        "external_record_count": sum(1 for record_id in record_ids if record_id.startswith("D")),
        "internal_record_count": sum(1 for record_id in record_ids if record_id.startswith("I")),
        "primary_worker_slots": len(primary_workers),
        "verifier_worker_slots": len(verifier_workers),
        "reserve_pair_count": len(reserves),
        "authority_sync_complete": True,
        "accepted_archive_record_count": 29,
        "blocked_archive_record_count": 1,
        "completed_formation_count": 3,
        "af01_status": "accepted_complete",
        "af02_status": "accepted_complete",
        "af02_started": True,
        "af02_authorized": True,
        "af02_accepted_archive_record_count": 10,
        "af02_remaining_evidence_count": 0,
        "af03_status": "accepted_complete",
        "af03_started": True,
        "af03_authorized": True,
        "af03_accepted_archive_record_count": 10,
        "af03_remaining_evidence_count": 0,
        "af04_status": "ready_not_started",
        "af04_started": False,
        "af04_authorized": False,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
    }
    return result


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
