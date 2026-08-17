#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "4be4f170219701841aca367dd98c7b746fdd444c"
MERGE = "34bc4beed57517532a1d79ae64131835a395f7b2"
FREEZE_RECEIPT = "0000-ptah-a05-freeze-quality-20260817-0155z"
PROOF_RECEIPT = "0000-ptah-a05-frozen-proof-fast-20260817-0204z"
SERGEANT = "627074b11c36014d8f8c391bdbcecbb5130a68e0fbbe8151d8af03aa700b9061"
CARGO_LOCK = "cbcec35bac0fb9c08782390e28398d0f451cbd97e35381ee418f66574c6e4f0e"
PORTABLE_PTY = "b4a596a2b3d2752d94f51fac2d4a96737b8705dddd311a32b9af47211f08671e"
NATIVE_SOURCE = "994d47d4db7c30973be12d5653e2e1bbe62e85b640e85fa05e6e43b81d06105b"
ACCEPTANCE_TEST = "1f5246af783d2f75413532778a347f280a903303e41f9cbeed4d22baa06d2530"
PROVIDER_API = "8422c7cd6640615c3243483758c1241660a0c5979d3e09006014c0ea903e5a60"
TENFOLD_LANES = 150

REQUIRED_FILES = [
    "planning/A05-NATIVE-PROCESS-PTY-PROVIDER-ACCEPTANCE.md",
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

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A05 acceptance status missing")
    for token in [
        CANDIDATE,
        MERGE,
        FREEZE_RECEIPT,
        PROOF_RECEIPT,
        SERGEANT,
        CARGO_LOCK,
        PORTABLE_PTY,
        NATIVE_SOURCE,
        ACCEPTANCE_TEST,
        PROVIDER_API,
    ]:
        require(token in acceptance, f"A05 acceptance evidence token missing: {token}")
    require("Tenfold private lanes: 150" in acceptance, "A05 Tenfold evidence missing")
    require(
        "GitHub Actions are **not** the A05 runtime execution or proof authority" in acceptance,
        "A05 MCP/RPC proof-route boundary missing",
    )
    require("A05 is **FROZEN / PROVEN / COMPLETE**" in acceptance, "A05 completion decision missing")
    require(
        "A06 — Persistent Workspace, Session and authority projection — is **READY**" in acceptance,
        "A06 readiness decision missing",
    )

    require(index.get("schema_version") == "1.5.0", "machine index schema version mismatch")
    require(
        index.get("status")
        == "operative_p01d_accepted_a01_complete_a02_complete_a03_complete_a04_complete_a05_complete_a06_ready",
        "machine authority status mismatch",
    )
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")
    require(
        index.get("active_work_unit") == "A06-persistent-workspace-session-authority-projection",
        "machine active work is not A06",
    )

    a05 = index.get("a05")
    require(isinstance(a05, dict), "machine A05 acceptance record missing")
    expected = {
        "status": "accepted_complete",
        "ptah_space_pr": 27,
        "candidate_exact_head": CANDIDATE,
        "merge_commit": MERGE,
        "freeze_quality_receipt": FREEZE_RECEIPT,
        "frozen_exact_head_proof_receipt": PROOF_RECEIPT,
        "physical_proof_transport": "oracle.live.v1",
        "rust_toolchain": "1.97.1",
        "tenfold_private_lanes": TENFOLD_LANES,
        "sergeant_review_packet_sha256": SERGEANT,
        "cargo_lock_sha256": CARGO_LOCK,
        "portable_pty_version": "0.9.0",
        "portable_pty_checksum": PORTABLE_PTY,
        "native_process_source_sha256": NATIVE_SOURCE,
        "acceptance_test_sha256": ACCEPTANCE_TEST,
        "provider_api_source_sha256": PROVIDER_API,
    }
    for key, value in expected.items():
        require(a05.get(key) == value, f"machine A05 field mismatch: {key}")
    require(a05.get("github_interactive_path_used") is False, "interactive Git path falsely recorded")
    for key in [
        "freeze_fmt_passed",
        "scoped_clippy_warnings_denied_passed",
        "dependency_lock_passed",
        "a02_regression_passed",
        "a03_regression_passed",
        "a04_regression_passed",
        "a05_package_tests_passed",
        "workspace_tests_passed",
        "prior_phase_surface_unchanged",
        "git_tracked_status_clean",
    ]:
        require(a05.get(key) is True, f"A05 proof field not passed: {key}")
    require(a05.get("sergeant_review_status") == "pass", "A05 Sergeant review is not PASS")
    require(a05.get("sergeant_admitted_findings") == 0, "A05 Sergeant admitted findings present")
    require(a05.get("sergeant_unresolved_assurances") == 0, "A05 Sergeant unresolved assurances present")
    require(a05.get("a06_workspace_session_implemented") is False, "A05 falsely claims A06 implementation")
    require(a05.get("prime_integration_qualified") is False, "A05 falsely claims Prime qualification")
    require(a05.get("production_or_release_accepted") is False, "A05 falsely claims production/release")

    a04 = index.get("a04")
    require(isinstance(a04, dict), "machine A04 acceptance record missing")
    require(
        a04.get("a05_native_process_pty_implemented") is False,
        "A04 historical A05 non-claim was rewritten",
    )

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    for key in ["A01", "A02", "A03", "A04", "A05"]:
        require(programmes.get(key) == "accepted_complete", f"{key} accepted prerequisite drifted")
    require(programmes.get("A06") == "ready", "A06 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    for key in ["node_runtime_proven", "ledger_runtime_proven", "activity_runtime_proven", "native_process_pty_runtime_proven"]:
        require(boundaries.get(key) is True, f"accepted runtime proof missing: {key}")
    require(boundaries.get("workspace_runtime_proven") is False, "A06 Workspace runtime falsely proven")
    for key in [
        "prime_deployment_qualified",
        "production_authorized",
        "release_accepted",
        "historical_ubuntu_proof_passed",
        "prime_host_id_equals_ptah_node_id",
    ]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require(
        "A05 — Native process, PTY and multi-terminal Provider: **FROZEN / PROVEN / COMPLETE**" in start,
        "AI recovery entry lacks A05 completion",
    )
    require(
        "Active work unit: **A06 — Persistent Workspace, Session and authority projection**" in start,
        "AI recovery entry is not on A06",
    )
    require("A06 status: **READY**" in start, "AI recovery entry lacks A06 readiness")
    require("A05 runtime execution/proof authority is Oracle MCP/RPC" in start, "AI recovery proof route drifted")
    for token in [CANDIDATE, MERGE, FREEZE_RECEIPT, PROOF_RECEIPT, SERGEANT]:
        require(token in start, f"AI recovery A05 evidence missing: {token}")

    require("A06 — READY / CURRENT WORK UNIT" in handoff, "durable handoff is not on A06")
    require("GitHub Actions are not the A05 runtime execution/proof authority" in handoff, "handoff proof route drifted")
    for token in [CANDIDATE, MERGE, FREEZE_RECEIPT, PROOF_RECEIPT, SERGEANT]:
        require(token in handoff, f"durable handoff A05 evidence missing: {token}")

    return {
        "record_type": "ptah.a05.acceptance_current_authority_validation",
        "status": "a05_accepted_complete_a06_ready",
        "a05_candidate": CANDIDATE,
        "a05_merge": MERGE,
        "a05_complete": True,
        "a06_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_runtime_proven": True,
        "activity_runtime_proven": True,
        "native_process_pty_runtime_proven": True,
        "workspace_runtime_proven": False,
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
