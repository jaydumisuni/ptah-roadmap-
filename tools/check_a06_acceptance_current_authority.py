#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

CANDIDATE = "28444aa2331c4c170df62f4de9499e93009f0f41"
MERGE = "55cb08cffec10a2ee560014133d393be55f98d05"
FINAL_REVIEW = "0000-ptah-a06-final-review-20260817-0428z"
FREEZE_RECEIPT = "0000-ptah-a06-freeze-gate-20260817-0429z"
FREEZE_MANIFEST = "6cb32c2210927fc4fe1449bb8ac40502666a55071259157c431c13d76c963494"
PASS_B_RECEIPT = "0000-ptah-a06-pass-b-proof-20260817-0430z"
PASS_B_MANIFEST = "26e7d031f444c4943e5ffcd36b484bd3d1a9265f9132b58d9d2d8b420f8e8d01"
CARGO_LOCK = "b7e2a30fc0660160fd330a9e1272ff195554b52b76f619c886826b933fb0c90e"
WORKSPACE_MANIFEST = "2c2dc997762f89d2fa7894f631fa42eae7fbcf599e1432694f78a0ae4aee6cbb"
WORKSPACE_SOURCE = "8b3d6383011aaf9422050b3c4a6a8b777a28c366e7c167b2818099976b830667"
ACCEPTANCE_TEST = "4bd1bc24d5bf7cc493839e50f22bfd0c5b02bb242be280c817915eb5a4d4e97b"
TENFOLD_LANES = 110

REQUIRED_FILES = [
    "planning/A06-PERSISTENT-WORKSPACE-SESSION-AUTHORITY-ACCEPTANCE.md",
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
    a05_acceptance = read(root, REQUIRED_FILES[1])
    index = json.loads(read(root, REQUIRED_FILES[2]))
    start = read(root, REQUIRED_FILES[3])
    handoff = read(root, REQUIRED_FILES[4])

    require("**Status:** ACCEPTED COMPLETE" in acceptance, "A06 acceptance status missing")
    for token in [
        CANDIDATE,
        MERGE,
        FINAL_REVIEW,
        FREEZE_RECEIPT,
        FREEZE_MANIFEST,
        PASS_B_RECEIPT,
        PASS_B_MANIFEST,
        CARGO_LOCK,
        WORKSPACE_MANIFEST,
        WORKSPACE_SOURCE,
        ACCEPTANCE_TEST,
    ]:
        require(token in acceptance, f"A06 acceptance evidence token missing: {token}")
    require("Tenfold private lanes: 110" in acceptance, "A06 Tenfold evidence missing")
    require("Sergeant verdict: APPROVE" in acceptance, "A06 Sergeant verdict missing")
    require(
        "GitHub Actions are **not** the A06 runtime execution or proof authority" in acceptance,
        "A06 MCP/RPC proof-route boundary missing",
    )
    require("A06 is **FROZEN / PROVEN / COMPLETE**" in acceptance, "A06 completion decision missing")
    require(
        "A07 — Object, Revision, Artifact, Location and local CAS — is **READY**" in acceptance,
        "A07 readiness decision missing",
    )

    require(index.get("schema_version") == "1.6.0", "machine index schema version mismatch")
    require(
        index.get("status")
        == "operative_p01d_accepted_a01_complete_a02_complete_a03_complete_a04_complete_a05_complete_a06_complete_a07_ready",
        "machine authority status mismatch",
    )
    require(index.get("runtime_implementation_authorized") is True, "runtime authorization was lost")
    require(index.get("authorization_blockers") == [], "unexpected authorization blockers remain")
    require(
        index.get("active_work_unit") == "A07-object-revision-artifact-location-local-cas",
        "machine active work is not A07",
    )

    a06 = index.get("a06")
    require(isinstance(a06, dict), "machine A06 acceptance record missing")
    expected = {
        "status": "accepted_complete",
        "ptah_space_pr": 28,
        "candidate_exact_head": CANDIDATE,
        "merge_commit": MERGE,
        "final_review_receipt": FINAL_REVIEW,
        "freeze_gate_receipt": FREEZE_RECEIPT,
        "freeze_manifest_sha256": FREEZE_MANIFEST,
        "pass_b_receipt": PASS_B_RECEIPT,
        "pass_b_proof_manifest_sha256": PASS_B_MANIFEST,
        "physical_proof_transport": "oracle.live.v1",
        "rust_toolchain": "1.97.1",
        "tenfold_private_lanes": TENFOLD_LANES,
        "sergeant_review_status": "pass",
        "sergeant_verdict": "APPROVE",
        "cargo_lock_sha256": CARGO_LOCK,
        "workspace_manifest_sha256": WORKSPACE_MANIFEST,
        "workspace_source_sha256": WORKSPACE_SOURCE,
        "acceptance_test_sha256": ACCEPTANCE_TEST,
    }
    for key, value in expected.items():
        require(a06.get(key) == value, f"machine A06 field mismatch: {key}")
    require(a06.get("github_interactive_path_used") is False, "interactive Git path falsely recorded")
    for key in [
        "freeze_fmt_passed",
        "scoped_clippy_warnings_denied_passed",
        "a06_acceptance_tests_passed",
        "workspace_tests_passed",
        "direct_acceptance_binary_proof_passed",
        "registry_dependency_set_unchanged_from_a05",
        "git_tracked_status_clean",
    ]:
        require(a06.get(key) is True, f"A06 proof field not passed: {key}")
    require(a06.get("sergeant_required_actions") == [], "A06 Sergeant required actions remain")
    require(a06.get("a07_object_cas_implemented") is False, "A06 falsely claims A07 implementation")
    require(
        a06.get("a13_checkpoint_restore_execution_implemented") is False,
        "A06 falsely claims A13 checkpoint/restore execution",
    )
    require(a06.get("prime_integration_qualified") is False, "A06 falsely claims Prime qualification")
    require(a06.get("production_or_release_accepted") is False, "A06 falsely claims production/release")

    a05 = index.get("a05")
    require(isinstance(a05, dict), "machine A05 acceptance record missing")
    require(
        a05.get("a06_workspace_session_implemented") is False,
        "A05 historical A06 non-claim was rewritten",
    )
    require(
        "A06 persistent Workspace, Session or authority-projection implementation" in a05_acceptance,
        "A05 historical A06 non-claim text missing",
    )

    programmes = index.get("programmes")
    require(isinstance(programmes, dict), "machine programme states missing")
    for key in ["A01", "A02", "A03", "A04", "A05", "A06"]:
        require(programmes.get(key) == "accepted_complete", f"{key} accepted prerequisite drifted")
    require(programmes.get("A07") == "ready", "A07 readiness missing")
    require(programmes.get("P01P") == "open_deferred", "P01P boundary drifted")

    boundaries = index.get("claim_boundaries")
    require(isinstance(boundaries, dict), "claim boundaries missing")
    for key in [
        "node_runtime_proven",
        "ledger_runtime_proven",
        "activity_runtime_proven",
        "native_process_pty_runtime_proven",
        "workspace_runtime_proven",
    ]:
        require(boundaries.get(key) is True, f"accepted runtime proof missing: {key}")
    require(boundaries.get("object_cas_runtime_proven") is False, "A07 Object/CAS runtime falsely proven")
    for key in [
        "prime_deployment_qualified",
        "production_authorized",
        "release_accepted",
        "historical_ubuntu_proof_passed",
        "prime_host_id_equals_ptah_node_id",
    ]:
        require(boundaries.get(key) is False, f"forbidden claim became true: {key}")

    require(
        "A06 — Persistent Workspace, Session and authority projection: **FROZEN / PROVEN / COMPLETE**" in start,
        "AI recovery entry lacks A06 completion",
    )
    require(
        "Active work unit: **A07 — Object, Revision, Artifact, Location and local CAS**" in start,
        "AI recovery entry is not on A07",
    )
    require("A07 status: **READY**" in start, "AI recovery entry lacks A07 readiness")
    require("A06 runtime execution/proof authority is Oracle MCP/RPC" in start, "AI recovery proof route drifted")
    for token in [CANDIDATE, MERGE, FINAL_REVIEW, FREEZE_MANIFEST, PASS_B_MANIFEST]:
        require(token in start, f"AI recovery A06 evidence missing: {token}")

    require("A07 — READY / CURRENT WORK UNIT" in handoff, "durable handoff is not on A07")
    require(
        "GitHub Actions are not the A06 runtime execution/proof authority" in handoff,
        "handoff proof route drifted",
    )
    for token in [CANDIDATE, MERGE, FINAL_REVIEW, FREEZE_MANIFEST, PASS_B_MANIFEST]:
        require(token in handoff, f"durable handoff A06 evidence missing: {token}")

    return {
        "record_type": "ptah.a06.acceptance_current_authority_validation",
        "status": "a06_accepted_complete_a07_ready",
        "a06_candidate": CANDIDATE,
        "a06_merge": MERGE,
        "a06_complete": True,
        "a07_ready": True,
        "runtime_implementation_authorized": True,
        "node_runtime_proven": True,
        "ledger_runtime_proven": True,
        "activity_runtime_proven": True,
        "native_process_pty_runtime_proven": True,
        "workspace_runtime_proven": True,
        "object_cas_runtime_proven": False,
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
