#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "19d390e22807a8540c7c4c5c3a94a37b93f5e3be"
MERGE = "da35986327010cba575093d905875ee966e3d755"
RECEIPT = "0000-ptah-a03-pass-b-physical-proof-20260816-1528z"
RECEIPT_BLOB = "dd78ee595abfec5a96250f060505df8e5d19765b"
PROOF = "26d684fb63e36b159e5a83c373bcd3a02dee04e893e00e282ae60b1cf400f861"
SERGEANT = "520f82f371e3a0b39183044ead54331542d82ea85c27ee2226496e23a8256ad5"
SQLITE = "c43daabc6597cb20c84ae5b785d7c6072220966bd79dd12b961b98fb48ba224a"

REQUIRED_FILES = [
    "planning/A03-LEDGER-SCHEMA-MIGRATIONS-ACCEPTANCE.md",
    "master-plan-index-amendment-2026-08-15.json",
    "AI_START_HERE.md",
]


class ValidationError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read(root: Path, path: str) -> str:
    target = root / path
    require(target.is_file(), f"missing required file: {path}")
    return target.read_text(encoding="utf-8")


def validate(root: Path) -> dict:
    acceptance = read(root, REQUIRED_FILES[0])
    index = json.loads(read(root, REQUIRED_FILES[1]))
    start = read(root, REQUIRED_FILES[2])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A03 acceptance status missing")
    for token in [CANDIDATE, MERGE, RECEIPT, RECEIPT_BLOB, PROOF, SERGEANT, SQLITE]:
        require(token in acceptance, f"A03 acceptance evidence token missing: {token}")
    require("19/19 PASS" in acceptance, "A03 ledger unit proof missing")
    require("4/4 PASS" in acceptance, "A03 crash/recovery proof missing")
    require(
        "A03-specific GitHub Actions runtime-proof workflows were removed before freeze" in acceptance,
        "A03 MCP/RPC proof-route boundary missing",
    )
    require(
        "A04 — Activity, Operation, Attempt, Event and Receipt runtime — is **READY**" in acceptance,
        "A04 readiness decision missing",
    )

    require(
        index.get("status") == "operative_p01d_accepted_a01_complete_a02_complete_a03_complete_a04_ready",
        "machine authority status mismatch",
    )
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(
        index.get("active_work_unit") == "A04-activity-operation-attempt-event-receipt-runtime",
        "machine active work is not A04",
    )
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")

    a03 = index.get("a03")
    require(isinstance(a03, dict), "machine A03 acceptance record missing")
    expected = {
        "status": "accepted_complete",
        "candidate_exact_head": CANDIDATE,
        "merge_commit": MERGE,
        "physical_proof_receipt": RECEIPT,
        "physical_proof_receipt_blob_sha": RECEIPT_BLOB,
        "physical_proof_manifest_sha256": PROOF,
        "physical_proof_transport": "oracle.live.v1",
        "sqlite_runtime_sha256": SQLITE,
        "sergeant_review_packet_sha256": SERGEANT,
    }
    for key, value in expected.items():
        require(a03.get(key) == value, f"machine A03 field mismatch: {key}")
    require(a03.get("github_interactive_path_used") is False, "interactive Git path falsely recorded")
    require(
        a03.get("ledger_unit_tests_passed") == a03.get("ledger_unit_tests_total") == 19,
        "A03 ledger test count mismatch",
    )
    require(
        a03.get("crash_recovery_tests_passed") == a03.get("crash_recovery_tests_total") == 4,
        "A03 crash/recovery count mismatch",
    )
    require(a03.get("workspace_tests_passed") is True, "A03 workspace tests not passed")
    require(a03.get("scoped_clippy_warnings_denied_passed") is True, "A03 scoped Clippy proof missing")
    require(a03.get("sergeant_review_status") == "pass", "A03 Sergeant review is not PASS")
    require(a03.get("sergeant_admitted_findings") == 0, "A03 Sergeant admitted findings present")
    require(a03.get("sergeant_unresolved_assurances") == 0, "A03 Sergeant unresolved assurances present")
    require(a03.get("a04_activity_execution_implemented") is False, "A03 falsely claims A04 implementation")
    require(a03.get("prime_integration_qualified") is False, "A03 falsely claims Prime qualification")
    require(a03.get("production_or_release_accepted") is False, "A03 falsely claims production/release")

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    for key in ["A01", "A02", "A03"]:
        require(programmes.get(key) == "accepted_complete", f"{key} accepted prerequisite drifted")
    require(programmes.get("A04") == "ready", "A04 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    require(boundaries.get("node_runtime_proven") is True, "accepted A02 Node runtime proof missing")
    require(boundaries.get("ledger_runtime_proven") is True, "accepted A03 ledger proof missing")
    for key in [
        "activity_runtime_proven",
        "prime_deployment_qualified",
        "production_authorized",
        "release_accepted",
        "historical_ubuntu_proof_passed",
        "prime_host_id_equals_ptah_node_id",
    ]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require(
        "A03 — Ledger, schema versions and crash-safe migrations: **FROZEN / PROVEN / COMPLETE**" in start,
        "AI recovery entry lacks A03 completion",
    )
    require(
        "Active work unit: **A04 — Activity, Operation, Attempt, Event and Receipt runtime**" in start,
        "AI recovery entry is not on A04",
    )
    require("A04 status: **READY**" in start, "AI recovery entry lacks A04 readiness")
    for token in [CANDIDATE, MERGE, RECEIPT, PROOF, SERGEANT]:
        require(token in start, f"AI recovery A03 evidence missing: {token}")

    return {
        "record_type": "ptah.a03.acceptance_current_authority_validation",
        "status": "a03_accepted_complete_a04_ready",
        "a03_candidate": CANDIDATE,
        "a03_merge": MERGE,
        "a03_complete": True,
        "a04_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_runtime_proven": True,
        "activity_runtime_proven": False,
        "p01p_open": True,
        "prime_deployment_qualified": False,
        "production_authorized": False,
        "release_accepted": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output")
    args = parser.parse_args()
    report = validate(Path(args.repo_root).resolve())
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
