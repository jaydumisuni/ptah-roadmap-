#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "fad9029504258c773f5ab496c79cfceea17c0b5e"
MERGE = "a63eb8f2c73f961b8466b844c6f194f2381a8139"
FREEZE = "6d69f74a209e95ab7faa9ab7a543b247dfc00d170e9d0af5be0f573d4eb5aa1f"
PASS_B = "db3f3561b85de30c001ac405261d2507128cfd2a87687f955ac6a862f9ebfda1"
SQLITE_SUPPLEMENT = "bd65b89e5cc1180b96612b18901c530892d5b753123c5b1ea237a0bd8a1fb734"
SERGEANT = "8f471eee95374fcad509aff88b80be08b95eae22dd719934978feac70ddb53d4"
SQLITE_ARCHIVE = "c1978ab409aa5195e1819e4fe9d3fc8634de3fc9a5a6fc2bfdde69acaa8fab10"
TENFOLD_LANES = 190

REQUIRED_FILES = [
    "planning/A04-ACTIVITY-OPERATION-ATTEMPT-RUNTIME-ACCEPTANCE.md",
    "master-plan-index-amendment-2026-08-15.json",
    "AI_START_HERE.md",
    "AI_HANDOFF.md",
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
    handoff = read(root, REQUIRED_FILES[3])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A04 acceptance status missing")
    for token in [CANDIDATE, MERGE, FREEZE, PASS_B, SQLITE_SUPPLEMENT, SERGEANT, SQLITE_ARCHIVE]:
        require(token in acceptance, f"A04 acceptance evidence token missing: {token}")
    require("Tenfold private lanes: 190" in acceptance, "A04 Tenfold lane evidence missing")
    require(
        "GitHub Actions are **not** the A04 runtime execution or proof authority" in acceptance,
        "A04 MCP/RPC proof-route boundary missing",
    )
    require("A05 — Native process, PTY and multi-terminal Provider — is **READY**" in acceptance, "A05 readiness decision missing")
    require("A04 is **FROZEN / PROVEN / COMPLETE**" in acceptance, "A04 completion decision missing")

    require(index.get("schema_version") == "1.4.0", "machine index schema version mismatch")
    require(
        index.get("status") == "operative_p01d_accepted_a01_complete_a02_complete_a03_complete_a04_complete_a05_ready",
        "machine authority status mismatch",
    )
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")
    require(
        index.get("active_work_unit") == "A05-native-process-pty-multi-terminal-provider",
        "machine active work is not A05",
    )

    a04 = index.get("a04")
    require(isinstance(a04, dict), "machine A04 acceptance record missing")
    expected = {
        "status": "accepted_complete",
        "ptah_space_pr": 26,
        "candidate_exact_head": CANDIDATE,
        "merge_commit": MERGE,
        "freeze_manifest_sha256": FREEZE,
        "pass_b_proof_manifest_sha256": PASS_B,
        "sqlite_supplement_sha256": SQLITE_SUPPLEMENT,
        "physical_proof_transport": "oracle.live.v1",
        "rust_toolchain": "1.97.1",
        "tenfold_private_lanes": TENFOLD_LANES,
        "sergeant_review_packet_sha256": SERGEANT,
        "sqlite_static_archive_sha256": SQLITE_ARCHIVE,
    }
    for key, value in expected.items():
        require(a04.get(key) == value, f"machine A04 field mismatch: {key}")
    require(a04.get("github_interactive_path_used") is False, "interactive Git path falsely recorded")
    require(a04.get("a04_package_tests_passed") is True, "A04 package tests not passed")
    require(a04.get("workspace_tests_passed") is True, "A04 workspace regression not passed")
    require(a04.get("scoped_clippy_warnings_denied_passed") is True, "A04 scoped Clippy proof missing")
    require(a04.get("sergeant_review_status") == "pass", "A04 Sergeant review is not PASS")
    require(a04.get("sergeant_admitted_findings") == 0, "A04 Sergeant admitted findings present")
    require(a04.get("sergeant_unresolved_assurances") == 0, "A04 Sergeant unresolved assurances present")
    require(a04.get("a05_native_process_pty_implemented") is False, "A04 falsely claims A05 implementation")
    require(a04.get("prime_integration_qualified") is False, "A04 falsely claims Prime qualification")
    require(a04.get("production_or_release_accepted") is False, "A04 falsely claims production/release")

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    for key in ["A01", "A02", "A03", "A04"]:
        require(programmes.get(key) == "accepted_complete", f"{key} accepted prerequisite drifted")
    require(programmes.get("A05") == "ready", "A05 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    require(boundaries.get("node_runtime_proven") is True, "accepted A02 Node runtime proof missing")
    require(boundaries.get("ledger_runtime_proven") is True, "accepted A03 ledger proof missing")
    require(boundaries.get("activity_runtime_proven") is True, "accepted A04 Activity runtime proof missing")
    for key in [
        "prime_deployment_qualified",
        "production_authorized",
        "release_accepted",
        "historical_ubuntu_proof_passed",
        "prime_host_id_equals_ptah_node_id",
    ]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require(
        "A04 — Activity, Operation, Attempt, Event and Receipt runtime: **FROZEN / PROVEN / COMPLETE**" in start,
        "AI recovery entry lacks A04 completion",
    )
    require(
        "Active work unit: **A05 — Native process, PTY and multi-terminal Provider**" in start,
        "AI recovery entry is not on A05",
    )
    require("A05 status: **READY**" in start, "AI recovery entry lacks A05 readiness")
    require("A04 runtime execution/proof authority is Oracle MCP/RPC" in start, "AI recovery proof route drifted")
    for token in [CANDIDATE, MERGE, FREEZE, PASS_B, SQLITE_SUPPLEMENT, SERGEANT]:
        require(token in start, f"AI recovery A04 evidence missing: {token}")

    require("A05 — READY / CURRENT WORK UNIT" in handoff, "durable handoff is not on A05")
    require("GitHub Actions are not the A04 runtime execution/proof authority" in handoff, "handoff proof route drifted")
    for token in [CANDIDATE, MERGE, FREEZE, PASS_B, SQLITE_SUPPLEMENT, SERGEANT]:
        require(token in handoff, f"durable handoff A04 evidence missing: {token}")

    return {
        "record_type": "ptah.a04.acceptance_current_authority_validation",
        "status": "a04_accepted_complete_a05_ready",
        "a04_candidate": CANDIDATE,
        "a04_merge": MERGE,
        "a04_complete": True,
        "a05_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_runtime_proven": True,
        "activity_runtime_proven": True,
        "tenfold_private_lanes": TENFOLD_LANES,
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
