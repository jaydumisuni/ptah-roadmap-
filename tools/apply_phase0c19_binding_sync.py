#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCEPTED_HEAD = "02e3ea2d26e39362ac8a90ad0bb7b248396476a6"
ACCEPTED_RUN = "30097738203"
ACCEPTED_ARTIFACT = "8598283488"
ACCEPTED_ARTIFACT_DIGEST = "sha256:1d571edbe7da273c98c01ec452c005d86dfda723f9483c44f54403d40ad7747c"
ACCEPTED_VALIDATION_SHA = "258a0ea7aa8bf20ca744dbca546d2de34ab0f7cb61cfa9e7d780d1401717158f"
ACCEPTED_REGRESSION_SHA = "39ac2470fa7140e9c0b3c65cc687d79838a70ddb6286a869da218cf8d36b1d23"
OPERATIVE_MERGE = "8f04e38f34df8c847af5548d0a31f63e8b396f6b"
BINDING_PATH = "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-OPERATIVE-BINDING.md"


class SyncError(RuntimeError):
    pass


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    (ROOT / path).write_text(content, encoding="utf-8")


def replace_once(content: str, old: str, new: str, label: str) -> str:
    count = content.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one source fragment, found {count}")
    return content.replace(old, new, 1)


def update_acceptance() -> None:
    path = "planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md"
    content = read(path)
    content = replace_once(
        content,
        "Status: ACCEPTED COMPLETE — accepted-state proof and operative merge pending",
        "Status: ACCEPTED COMPLETE — accepted-state proof and operative merge bound",
        "acceptance status",
    )
    anchor = "All eight permanent roadmap lanes passed at the exact candidate head. The Phase 0C-19 suite passed 30 valid and adversarial cases.\n"
    section = f"""All eight permanent roadmap lanes passed at the exact candidate head. The Phase 0C-19 suite passed 30 valid and adversarial cases.\n\n## Accepted-state proof and operative binding\n\n```text\naccepted exact head: {ACCEPTED_HEAD}\naccepted workflow run: {ACCEPTED_RUN}\naccepted artifact: {ACCEPTED_ARTIFACT}\naccepted artifact digest: {ACCEPTED_ARTIFACT_DIGEST}\naccepted validation SHA-256: {ACCEPTED_VALIDATION_SHA}\naccepted regression SHA-256: {ACCEPTED_REGRESSION_SHA}\noperative acceptance merge: {OPERATIVE_MERGE}\noperative binding: {BINDING_PATH}\n```\n\nAll nine permanent workflows passed at the accepted exact head. The accepted-state suite passed 25 cases; the guarded synchronization also passed 85 inherited regressions.\n"""
    content = replace_once(content, anchor, section, "acceptance evidence insertion")
    write(path, content)


def update_handoff() -> None:
    path = "AI_HANDOFF.md"
    content = read(path)
    marker = "## Accepted Phase 0C-19 planning-load reconciliation"
    if marker not in content:
        raise SyncError("handoff Phase 0C-19 section missing")
    if ACCEPTED_HEAD not in content:
        insertion = f"""

Accepted-state evidence:

```text
exact head: {ACCEPTED_HEAD}
workflow run: {ACCEPTED_RUN}
artifact: {ACCEPTED_ARTIFACT}
artifact digest: {ACCEPTED_ARTIFACT_DIGEST}
validation SHA-256: {ACCEPTED_VALIDATION_SHA}
regression SHA-256: {ACCEPTED_REGRESSION_SHA}
operative acceptance merge: {OPERATIVE_MERGE}
operative binding: {BINDING_PATH}
```
"""
        anchor = "Do not run the physical proof until Phase 0C-19 is accepted and the proof commit is confirmed or superseded."
        if anchor in content:
            raise SyncError("handoff still contains pre-acceptance instruction")
        next_action = "The next action is to run the proof kit"
        pos = content.find(next_action)
        if pos < 0:
            raise SyncError("handoff Phase 0C-19 next-action anchor missing")
        content = content[:pos] + insertion + "\n" + content[pos:]
    write(path, content)


def update_index() -> None:
    path = ROOT / "master-plan-index.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    record = data.get("phase0c19_deep_workspace_reconciliation")
    if not isinstance(record, dict) or record.get("status") != "accepted_complete":
        raise SyncError("accepted machine Phase 0C-19 record missing")
    record.update({
        "accepted_state_exact_head": ACCEPTED_HEAD,
        "accepted_state_workflow_run": ACCEPTED_RUN,
        "accepted_state_artifact_id": ACCEPTED_ARTIFACT,
        "accepted_state_artifact_digest": ACCEPTED_ARTIFACT_DIGEST,
        "accepted_state_validation_sha256": ACCEPTED_VALIDATION_SHA,
        "accepted_state_regression_sha256": ACCEPTED_REGRESSION_SHA,
        "operative_acceptance_merge": OPERATIVE_MERGE,
        "operative_binding": BINDING_PATH,
        "accepted_state_proof_pending": False,
        "operative_acceptance_merge_pending": False,
    })
    for key in ["master_plan", "implementation_roadmap"]:
        plan = data.get("plan_documents", {}).get(key)
        if not isinstance(plan, dict) or plan.get("version") != "1.1.0":
            raise SyncError(f"{key} version 1.1.0 authority missing")
        plan["phase0c19_operative_acceptance_merge"] = OPERATIVE_MERGE
    recovery = data.get("recovery_order")
    if not isinstance(recovery, list):
        raise SyncError("recovery order missing")
    if BINDING_PATH not in recovery:
        recovery.insert(3, BINDING_PATH)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def validate_boundary() -> None:
    acceptance = read("planning/PHASE0C19-DEEP-WORKSPACE-ROADMAP-ACCEPTANCE.md")
    handoff = read("AI_HANDOFF.md")
    current = read("CURRENT_STATE.md")
    for token in [ACCEPTED_HEAD, ACCEPTED_RUN, ACCEPTED_ARTIFACT, ACCEPTED_ARTIFACT_DIGEST, ACCEPTED_VALIDATION_SHA, ACCEPTED_REGRESSION_SHA, OPERATIVE_MERGE, BINDING_PATH]:
        if token not in acceptance:
            raise SyncError(f"acceptance binding missing: {token}")
        if token not in handoff:
            raise SyncError(f"handoff binding missing: {token}")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current:
        raise SyncError("runtime non-authorization missing")
    if "ADR-0033: PROPOSED" not in current or "physical-host collection: NOT STARTED" not in current:
        raise SyncError("P01 fail-closed boundary changed")
    data = json.loads((ROOT / "master-plan-index.json").read_text(encoding="utf-8"))
    record = data["phase0c19_deep_workspace_reconciliation"]
    if record.get("accepted_state_proof_pending") is not False or record.get("operative_acceptance_merge_pending") is not False:
        raise SyncError("binding pending flags not cleared")
    if record.get("runtime_implementation_authorized") is not False or record.get("adr_0033_accepted") is not False:
        raise SyncError("binding altered authorization")


def main() -> None:
    update_acceptance()
    update_handoff()
    update_index()
    validate_boundary()
    print("Phase 0C-19 operative acceptance binding synchronized")


if __name__ == "__main__":
    main()
