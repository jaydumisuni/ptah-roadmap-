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
    require(adr, "Status: proposed", "ADR-0035 proposed state")
    require(work_package, "Status: candidate under review", "Phase 0C-17 candidate state")
    require(donor_register, "Status:** COMPLETE AND FROZEN", "frozen Phase 0A donor register")
    require(donor_register, "Tenfold archival-completeness rule", "donor archive protocol link")
    require(donor_register, "69 external and 29 internal", "donor campaign coverage")
    if "Phase 0A reopened" in donor_register or "Status:** REOPENED" in donor_register:
        raise ValidationError("Phase 0A donor register was reopened")

    require(memory_protocol, "## 5.1 Tenfold archive formation rule", "memory archive rule")
    require(memory_protocol, "private force = max(20, human-equivalent workers × 10)", "memory force equation")
    require(memory_protocol, "after five reconciled records", "memory five-record checkpoint")
    require(memory_protocol, "after ten accepted records", "memory ten-record checkpoint")

    require(decisions, "### ADR-0035 — Tenfold archive formation and evidence promotion", "decision index entry")
    require(decisions, "**PROPOSED.**", "ADR-0035 proposed index state")
    require(progress, "## Tenfold archive formation candidate", "progress archive section")
    require(progress, "200 private slots allocated", "progress force count")
    require(progress, "no source record is pre-ticked as archived", "progress earned-completion rule")

    require(current_state, "P01", "active P01 physical-host work")
    require(current_state, "## Active Phase 0C-17 tenfold archive formation candidate", "current archive candidate")
    require(current_state, "PR #26", "current archive PR")
    require(current_state, "does not replace P01", "current P01 boundary")
    require(current_state, "**Runtime implementation:** NOT AUTHORIZED", "runtime non-authorization")
    if "**Runtime implementation:** AUTHORIZED" in current_state:
        raise ValidationError("runtime implementation became authorized")

    require(handoff, "## Cross-cutting archive formation candidate", "handoff archive candidate")
    require(handoff, "pull request: #26", "handoff archive PR")
    require(handoff, "Campaign 001 covers 98 source obligations", "handoff campaign scope")
    require(handoff, "P01 physical-host closure remains the exact next authorization action", "handoff P01 boundary")

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
        "status": "candidate_under_review",
        "source_branch": "phase0c-tenfold-archive-formation",
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
        "status": "candidate_valid_non_authorizing",
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
