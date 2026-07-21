#!/usr/bin/env python3
"""Validate Campaign 001 AF01 archive evidence without authorizing implementation."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

MISSION = Path("archive/campaign-001/af01/MISSION.md")
CHECKPOINT_05 = Path("archive/campaign-001/af01/CHECKPOINT-05.md")
CHECKPOINT_10 = Path("archive/campaign-001/af01/CHECKPOINT-10.md")
RESULT_JSON = Path("archive/campaign-001/af01/RESULT.json")
RESULT_MD = Path("archive/campaign-001/af01/RESULT.md")
MANIFEST = Path("archive/CAMPAIGN-001-FORMATION-MANIFEST.md")
DONOR_REGISTER = Path("DONOR_RECOVERY.md")
CURRENT_STATE = Path("CURRENT_STATE.md")
ADR0033 = Path("decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md")

EXPECTED: dict[str, dict[str, str]] = {
    "D001": {
        "source": "openclaw/openclaw",
        "branch": "main",
        "commit": "4400f4ca91b2a58096353197337427d824856963",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P01",
        "verifier": "AF01-V01",
        "path": "archive/campaign-001/af01/records/D001-OPENCLAW.md",
    },
    "D012": {
        "source": "e2b-dev/E2B",
        "branch": "main",
        "commit": "be1ffa19f6ad6d7b1003d714ce45faf3cf2c3e21",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P02",
        "verifier": "AF01-V02",
        "path": "archive/campaign-001/af01/records/D012-E2B.md",
    },
    "D016": {
        "source": "microsoft/playwright",
        "branch": "main",
        "commit": "129717a626d6ff1c870b19f285db7771f3b33a59",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P03",
        "verifier": "AF01-V03",
        "path": "archive/campaign-001/af01/records/D016-PLAYWRIGHT.md",
    },
    "D020": {
        "source": "DeviceFarmer/stf",
        "branch": "master",
        "commit": "36d1a3e4336f2ecdf7885e3644fe34d0a4282c87",
        "outcome": "accepted_for_archive_with_security_restrictions",
        "primary": "AF01-P04",
        "verifier": "AF01-V04",
        "path": "archive/campaign-001/af01/records/D020-DEVICEFARMER-STF.md",
    },
    "D030": {
        "source": "google/gvisor",
        "branch": "master",
        "commit": "9f653e577965df2ddd13875b5530cd2588661f1c",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P05",
        "verifier": "AF01-V05",
        "path": "archive/campaign-001/af01/records/D030-GVISOR.md",
    },
    "D035": {
        "source": "moby/buildkit",
        "branch": "master",
        "commit": "4f4f9d52fcf3d58553fa5327452240c7ad7dd853",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P06",
        "verifier": "AF01-V06",
        "path": "archive/campaign-001/af01/records/D035-BUILDKIT.md",
    },
    "D042": {
        "source": "infiniflow/ragflow",
        "branch": "main",
        "commit": "6a85d1c5c4f96933cd91214a080460baa9252976",
        "outcome": "accepted_for_archive",
        "primary": "AF01-P07",
        "verifier": "AF01-V07",
        "path": "archive/campaign-001/af01/records/D042-RAGFLOW.md",
    },
    "D047": {
        "source": "mini-router/minirouter",
        "branch": "main",
        "commit": "6b283fed773556eb034f052a17dc0f3318f0a76b",
        "outcome": "blocked_for_source_reuse",
        "primary": "AF01-P08",
        "verifier": "AF01-V08",
        "path": "archive/campaign-001/af01/records/D047-MINIROUTER.md",
    },
    "D051": {
        "source": "gittensor-model-hub/SparkDistill",
        "branch": "main",
        "commit": "6fb8857fba4bfa29dd74f1ab43619e517b601225",
        "outcome": "accepted_for_archive_with_rights_and_proof_restrictions",
        "primary": "AF01-P09",
        "verifier": "AF01-V09",
        "path": "archive/campaign-001/af01/records/D051-SPARKDISTILL.md",
    },
    "D058": {
        "source": "usestrix/strix",
        "branch": "main",
        "commit": "48b4821f6960f38a289118a5c17b7e88e3a168b2",
        "outcome": "accepted_for_archive_with_offensive_security_restrictions",
        "primary": "AF01-P10",
        "verifier": "AF01-V10",
        "path": "archive/campaign-001/af01/records/D058-STRIX.md",
    },
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
    result = json.loads(read(root, RESULT_JSON))
    manifest = read(root, MANIFEST)
    donor_register = read(root, DONOR_REGISTER)
    current_state = read(root, CURRENT_STATE)
    adr0033 = read(root, ADR0033)

    # Formation state and counts.
    require(mission, "Status: CANDIDATE COMPLETE", "mission candidate state")
    require(mission, "accepted for archive: 9", "mission accepted count")
    require(mission, "blocked completed outcomes: 1", "mission blocked count")
    require(mission, "remaining in evidence collection: 0", "mission remaining count")
    require(mission, "AF02 is not authorized", "AF02 boundary")
    require(checkpoint05, "first five records reconciled", "checkpoint 05 state")
    require(checkpoint10, "all ten assigned records reconciled", "checkpoint 10 state")
    require(checkpoint10, "accepted for archive: 9", "checkpoint 10 accepted count")
    require(checkpoint10, "blocked completed outcomes: 1", "checkpoint 10 blocked count")
    require(result_md, "CANDIDATE COMPLETE", "result candidate state")
    require(result_md, "MiniRouter", "blocked record narrative")
    require(result_md, "no root `LICENSE`", "MiniRouter licence block")

    expected_top = {
        "schema_version": "1.0.0",
        "record_type": "ptah.archive_campaign_formation_result",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF01",
        "status": "candidate_complete_pending_exact_head_review",
        "base_authority_commit": "856c9859e8faca959f2a38ce33d4607af33e90c1",
        "protocol_version": "1.0.0",
        "assigned_record_count": 10,
        "reconciled_record_count": 10,
        "accepted_archive_record_count": 9,
        "blocked_record_count": 1,
        "parked_record_count": 0,
        "rejected_record_count": 0,
        "remaining_evidence_count": 0,
        "primary_worker_count": 10,
        "verifier_worker_count": 10,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "af02_authorized": False,
    }
    for key, value in expected_top.items():
        if result.get(key) != value:
            raise ValidationError(f"AF01 result mismatch: {key}")

    records = result.get("records")
    if not isinstance(records, list) or len(records) != 10:
        raise ValidationError("AF01 result must contain exactly ten records")
    ids = [record.get("id") for record in records]
    if set(ids) != set(EXPECTED) or len(ids) != len(set(ids)):
        raise ValidationError(f"AF01 record coverage mismatch: {ids}")

    primary_ids: list[str] = []
    verifier_ids: list[str] = []
    accepted = 0
    blocked = 0
    for record in records:
        record_id = record["id"]
        expected = EXPECTED[record_id]
        for key, value in expected.items():
            if record.get(key) != value:
                raise ValidationError(f"{record_id} mismatch: {key}")
        primary_ids.append(record["primary"])
        verifier_ids.append(record["verifier"])
        if record["outcome"].startswith("accepted_for_archive"):
            accepted += 1
        elif record["outcome"] == "blocked_for_source_reuse":
            blocked += 1
        else:
            raise ValidationError(f"unexpected AF01 outcome: {record_id}")

        record_path = Path(record["path"])
        text = read(root, record_path)
        require(text, f"# {record_id} —", f"{record_id} heading")
        require(text, expected["source"], f"{record_id} canonical source")
        require(text, expected["commit"], f"{record_id} exact commit")
        require(text, f"Primary Archivist: `{expected['primary']}`", f"{record_id} primary")
        require(text, f"Independent Verifier: `{expected['verifier']}`", f"{record_id} verifier")
        require(text, "## Primary evidence packet", f"{record_id} primary packet")
        require(text, "## Independent verification packet", f"{record_id} verifier packet")
        require(text, "## Contradiction and supersession", f"{record_id} contradiction section")
        require(text, "## Bounded outcome", f"{record_id} bounded outcome")
        require(text, "does not", f"{record_id} non-effect boundary")

    if accepted != 9 or blocked != 1:
        raise ValidationError(f"AF01 outcome counts invalid: accepted={accepted}, blocked={blocked}")
    if len(set(primary_ids)) != 10 or len(set(verifier_ids)) != 10:
        raise ValidationError("AF01 worker identity reused")
    if set(primary_ids).intersection(verifier_ids):
        raise ValidationError("AF01 primary and verifier identities overlap")

    # Hard record-specific restrictions.
    minirouter = read(root, Path(EXPECTED["D047"]["path"]))
    require(minirouter, "root `LICENSE`: not present", "MiniRouter missing licence evidence")
    require(minirouter, "public visibility is not a licence grant", "MiniRouter public/licence boundary")
    require(minirouter, "copying or adapting source", "MiniRouter reuse prohibition")
    stf = read(root, Path(EXPECTED["D020"]["path"]))
    require(stf, "little to no security/encryption", "STF security warning")
    strix = read(root, Path(EXPECTED["D058"]["path"]))
    require(strix, "only owned or explicitly authorized targets", "Strix target authorization")
    spark = read(root, Path(EXPECTED["D051"]["path"]))
    require(spark, "root code licence", "SparkDistill rights separation")
    require(spark, "attestation proves bounded measured claims", "SparkDistill proof boundary")

    # Manifest and frozen authority boundaries.
    af01_ids = re.findall(r"^\| `(D\d{3})` \|.*\| `AF01-P\d{2}` \| `AF01-V\d{2}` \|$", manifest, re.MULTILINE)
    if af01_ids != list(EXPECTED):
        raise ValidationError(f"campaign manifest AF01 order mismatch: {af01_ids}")
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
        "record_type": "ptah.archive_campaign_af01_validation",
        "status": "candidate_complete_valid_non_authorizing",
        "campaign_id": "CAMPAIGN-001",
        "formation_id": "AF01",
        "record_count": len(records),
        "accepted_archive_record_count": accepted,
        "blocked_record_count": blocked,
        "primary_worker_count": len(primary_ids),
        "verifier_worker_count": len(verifier_ids),
        "checkpoint_count": 2,
        "remaining_evidence_count": 0,
        "phase_0a_reopened": False,
        "adr_0033_accepted": False,
        "runtime_implementation_authorized": False,
        "af02_authorized": False,
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
