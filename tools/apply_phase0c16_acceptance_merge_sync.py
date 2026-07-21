#!/usr/bin/env python3
"""Bind the operative Phase 0C-16 / ADR-0034 acceptance merge into recovery records."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE_HEAD = "37d23449fda9a426f56ee8b09042dda91587a6d1"
CANDIDATE_RUN = "29842137511"
CANDIDATE_ARTIFACT = "8499790872"
CANDIDATE_DIGEST = "sha256:82d6b452777e2c5e60c4d08bf88dd2c848d6b2570650b70a4eede633c8065d9f"
CANDIDATE_MERGE = "2c24f9e6b0fc98d5e03605596db75d7495796353"
ACCEPTED_HEAD = "5860b4bfe177aa375fb2fa4305d62dbe3d2141e1"
ACCEPTED_RUN = "29844040274"
ACCEPTED_ARTIFACT = "8500540358"
ACCEPTED_DIGEST = "sha256:6f5229fe850d8b6f6f083b09f2c5f53189f3edbf38d4f28b9d2878ab0c78862d"
ACCEPTANCE_MERGE = "66bd2410d4c777cd3fd3278107f40fe425e875e9"


class SyncError(RuntimeError):
    pass


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SyncError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def update_text(relative: str, old: str, new: str, label: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, old, new, f"{relative}: {label}")
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def update_current_state() -> None:
    old = f"""Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

ADR-0034 is accepted."""
    new = f"""Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

Accepted-state exact head:

```text
{ACCEPTED_HEAD}
```

Permanent accepted-state workflow run: `{ACCEPTED_RUN}`.

Retained accepted-state artifact: `{ACCEPTED_ARTIFACT}` with archive digest `{ACCEPTED_DIGEST}`.

Operative authority acceptance merge:

```text
{ACCEPTANCE_MERGE}
```

ADR-0034 is accepted."""
    update_text("CURRENT_STATE.md", old, new, "operative acceptance evidence")


def update_adr34() -> None:
    old = f"""Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

Direct review found no unresolved review threads or changed-file boundary violations. CodeRabbit review was requested but rate-limited and produced no findings."""
    new = f"""Candidate squash merge:

```text
{CANDIDATE_MERGE}
```

Direct review found no unresolved review threads or changed-file boundary violations. CodeRabbit review was requested but rate-limited and produced no findings.

Accepted-state exact head:

```text
{ACCEPTED_HEAD}
```

Permanent accepted-state workflow run: `{ACCEPTED_RUN}`.

Retained accepted-state artifact: `{ACCEPTED_ARTIFACT}` with archive digest `{ACCEPTED_DIGEST}`.

The accepted-state lane passed thirteen positive/adversarial regressions, standalone validation over seventeen durable authority files and all non-authorization checks.

Operative authority acceptance merge:

```text
{ACCEPTANCE_MERGE}
```
"""
    update_text(
        "decisions/ADR-0034-MASTER-PLAN-ROADMAP-AND-HANDOFF-AUTHORITY.md",
        old,
        new,
        "operative acceptance evidence",
    )


def update_wp16() -> None:
    old = f"""- candidate squash merge: `{CANDIDATE_MERGE}`;
- twelve positive/adversarial regressions passed;"""
    new = f"""- candidate squash merge: `{CANDIDATE_MERGE}`;
- accepted-state exact head: `{ACCEPTED_HEAD}`;
- permanent accepted-state workflow run: `{ACCEPTED_RUN}`;
- retained accepted-state artifact: `{ACCEPTED_ARTIFACT}`;
- retained accepted-state archive digest: `{ACCEPTED_DIGEST}`;
- operative authority acceptance merge: `{ACCEPTANCE_MERGE}`;
- twelve candidate positive/adversarial regressions passed;
- thirteen accepted-state positive/adversarial regressions passed;"""
    update_text(
        "work-packages/PHASE-0C-16-MASTER-PLAN-AND-IMPLEMENTATION-ROADMAP-CLOSURE.md",
        old,
        new,
        "operative acceptance evidence",
    )


def update_handoff() -> None:
    old = f"- candidate squash merge: `{CANDIDATE_MERGE}`."
    new = f"""- candidate squash merge: `{CANDIDATE_MERGE}`;
- accepted-state exact head: `{ACCEPTED_HEAD}`;
- permanent accepted-state workflow run: `{ACCEPTED_RUN}`;
- retained accepted-state artifact: `{ACCEPTED_ARTIFACT}`;
- accepted-state archive digest: `{ACCEPTED_DIGEST}`;
- operative authority acceptance merge: `{ACCEPTANCE_MERGE}`."""
    update_text("AI_HANDOFF.md", old, new, "operative acceptance evidence")


def update_index() -> None:
    path = ROOT / "master-plan-index.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("runtime_implementation_authorized") is not False:
        raise SyncError("master-plan index cannot authorize runtime")
    evidence = value.get("acceptance_evidence")
    if not isinstance(evidence, dict):
        raise SyncError("acceptance evidence object is missing")
    if evidence.get("candidate_merge") != CANDIDATE_MERGE:
        raise SyncError("candidate merge binding mismatch")
    evidence.update(
        {
            "accepted_state_exact_head": ACCEPTED_HEAD,
            "accepted_state_workflow_run": ACCEPTED_RUN,
            "accepted_state_artifact_id": ACCEPTED_ARTIFACT,
            "accepted_state_artifact_digest": ACCEPTED_DIGEST,
            "operative_acceptance_merge": ACCEPTANCE_MERGE,
        }
    )
    for key in (
        "requirements_and_decisions",
        "master_plan",
        "implementation_roadmap",
        "reconciliation",
    ):
        value["plan_documents"][key]["operative_acceptance_merge"] = ACCEPTANCE_MERGE
    value["plan_documents"]["handoff"]["operative_acceptance_merge"] = ACCEPTANCE_MERGE
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def write_merge_record() -> None:
    path = ROOT / "planning/MASTER-PLAN-AUTHORITY-ACCEPTANCE-MERGE.md"
    if path.exists():
        raise SyncError("operative acceptance merge record already exists")
    text = f"""# Ptah Master Plan authority acceptance merge

Status: operative evidence record — runtime implementation remains unauthorized

Recorded: 2026-07-21

## Candidate closure

- exact head: `{CANDIDATE_HEAD}`;
- workflow run: `{CANDIDATE_RUN}`;
- artifact: `{CANDIDATE_ARTIFACT}`;
- archive digest: `{CANDIDATE_DIGEST}`;
- candidate squash merge: `{CANDIDATE_MERGE}`.

## Accepted-state closure

- exact head: `{ACCEPTED_HEAD}`;
- permanent workflow run: `{ACCEPTED_RUN}`;
- artifact: `{ACCEPTED_ARTIFACT}`;
- archive digest: `{ACCEPTED_DIGEST}`;
- operative authority acceptance merge: `{ACCEPTANCE_MERGE}`.

The final accepted-state lane tested exactly seventeen durable authority/validation files, passed thirteen positive/adversarial regressions and standalone validation, accepted ADR-0034, made Master Plan and implementation roadmap version `1.0.0` operative, closed P00 and selected P01.

## Remaining boundary

This merge does not accept the physical host, installed packages, package artifacts, durable host bundle, final Phase 0C closure review or ADR-0033. It does not authorize runtime implementation.

```text
Physical-host proof: OPEN
ADR-0033: PROPOSED
Runtime implementation: NOT AUTHORIZED
```
"""
    path.write_text(text, encoding="utf-8")


def verify() -> None:
    current = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    handoff = (ROOT / "AI_HANDOFF.md").read_text(encoding="utf-8")
    adr33 = (
        ROOT
        / "decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md"
    ).read_text(encoding="utf-8")
    for text, label in ((current, "CURRENT_STATE"), (handoff, "AI_HANDOFF")):
        if ACCEPTANCE_MERGE not in text:
            raise SyncError(f"{label}: operative acceptance merge missing")
    if "**Runtime implementation:** NOT AUTHORIZED" not in current:
        raise SyncError("CURRENT_STATE non-authorization missing")
    if "**Runtime implementation:** AUTHORIZED" in current:
        raise SyncError("CURRENT_STATE runtime authorization appeared")
    if "Status: proposed" not in adr33:
        raise SyncError("ADR-0033 changed from proposed")


def main() -> None:
    update_current_state()
    update_adr34()
    update_wp16()
    update_handoff()
    update_index()
    write_merge_record()
    verify()
    print("operative Master Plan authority acceptance merge synchronized")


if __name__ == "__main__":
    try:
        main()
    except SyncError as exc:
        raise SystemExit(str(exc)) from exc
