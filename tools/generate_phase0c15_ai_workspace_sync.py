#!/usr/bin/env python3
"""Generate the guarded Phase 0C-15 AI Project Workspace roadmap sync."""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated-sync"
SOURCE_COMMIT = "11afadd2907f72a99c4cee57362a50195189e11f"
PTAH_SPACE_HEAD = "2a2c28d17abd9ad52c8d850f8bbcdba57074194e"
PTAH_SPACE_MERGE = "d05653c5948727b58ead91088447d0b8ac4d9d9b"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def write(relative: str, text: str) -> dict[str, object]:
    path = OUT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    raw = text.encode("utf-8")
    path.write_bytes(raw)
    return {
        "path": relative,
        "size_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def current_state() -> str:
    text = (ROOT / "CURRENT_STATE.md").read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;\n- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        "- `work-packages/PHASE-0C-14-APACHE-2.0-OWNER-ACCEPTANCE.md`;\n- `work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md`;\n- proposed `decisions/ADR-0033-FIRST-VERTICAL-SLICE-HOST-LICENCE-LAYOUT-BACKENDS.md`.",
        "current-state record list",
    )
    section = f"""## Merged AI Project Workspace behavioural donor and Hunter bridge candidate

`Ptah-space` PR `#14` was tested at exact head:

```text
{PTAH_SPACE_HEAD}
```

and squash-merged at:

```text
{PTAH_SPACE_MERGE}
```

The merged non-operative design package records:

- OpenAI ChatGPT Projects and Work as a public-documentation behavioural donor only;
- no OpenAI source-code reuse, proprietary implementation claim or runtime dependency;
- profile identity `ptah.workspace.ai_project.v1`;
- sixteen existing Ptah primitives composed into a human-and-agent project Workspace;
- fourteen donor behaviours: four directly covered, eight covered by profile composition, zero Core extensions and two rejected patterns;
- explicit rejection of hidden provider memory and implicit global tool access;
- a Hunter–Ptah bridge where Ptah owns durable truth and Grants while Hunter coordinates through bounded context packets;
- ten positive/negative proof fixtures for isolation, authority, provider replacement, scheduled access, handoff and Artifact lineage;
- ten fail-closed regressions and exact-head evidence under immutable Action pins;
- a corrected public README licence statement while retaining the non-claiming runtime boundary.

All ten exact-head workflows passed, including the new AI Project Workspace candidate lane, source/no-build, Rust policy, frozen contracts, generated bindings, host, licence, backend artifact, backend signature and signer-lock gates.

This candidate is a non-blocking future composition design. It neither closes nor adds an ADR-0033 acceptance condition, changes a frozen WP01–WP14 contract, implements a Workspace/context runtime or authorizes Hunter integration.

---

"""
    text = replace_once(
        text,
        "---\n\n## Active Phase 0C blockers",
        "---\n\n" + section + "## Active Phase 0C blockers",
        "current-state candidate section",
    )
    text = replace_once(
        text,
        "- accepted licence, contribution, security and third-party-notice boundary maintenance;\n- exact physical pinned-host and installed-package evidence;",
        "- accepted licence, contribution, security and third-party-notice boundary maintenance;\n- non-operative behavioural donor, Workspace-profile and Hunter-bridge maintenance;\n- exact physical pinned-host and installed-package evidence;",
        "current-state allowed work",
    )
    if "**Runtime implementation:** NOT AUTHORIZED" not in text:
        raise RuntimeError("current-state runtime block missing")
    if "**Runtime implementation:** AUTHORIZED" in text:
        raise RuntimeError("candidate attempted runtime authorization")
    return text


def progress() -> str:
    text = (ROOT / "PROGRESS.md").read_text(encoding="utf-8")
    section = f"""## AI Project Workspace behavioural donor and Hunter bridge candidate

- [x] ChatGPT Projects, project memory, Library, Work, Canvas and Scheduled Tasks recorded from official public documentation as behavioural sources only;
- [x] code reuse fixed at none and OpenAI excluded as a runtime dependency;
- [x] `ptah.workspace.ai_project.v1` candidate profile recorded over sixteen existing Ptah primitives;
- [x] fourteen behaviours mapped with zero frozen-contract extensions;
- [x] hidden provider memory and implicit global tool access explicitly rejected;
- [x] bounded context, source authority, Workspace isolation, Facility Grants and model-independent handoff requirements recorded;
- [x] Hunter–Ptah bridge responsibilities and candidate-to-truth promotion boundary recorded;
- [x] ten positive/negative fixtures and ten adversarial validator regressions passed;
- [x] all ten workflows passed at exact head `{PTAH_SPACE_HEAD}`;
- [x] donor/profile package squash-merged as `{PTAH_SPACE_MERGE}`;
- [x] candidate remains non-operative, non-blocking and runtime implementation remains unauthorized.

"""
    text = replace_once(
        text,
        "## Active Phase 0C closure work",
        section + "## Active Phase 0C closure work",
        "progress candidate section",
    )
    text = replace_once(
        text,
        "- [x] donor/workload identity remains outside Ptah Core;\n- [x] WP13 and WP14 proof burdens remain unchanged;",
        "- [x] donor/workload identity remains outside Ptah Core;\n- [x] AI Project Workspace donor/profile remains non-operative and provider-independent;\n- [x] WP13 and WP14 proof burdens remain unchanged;",
        "progress no-build boundary",
    )
    if "- [ ] runtime implementation authorized." not in text:
        raise RuntimeError("progress runtime block missing")
    return text


def work_package() -> str:
    return f"""# Phase 0C-15 — AI Project Workspace donor and Hunter bridge candidate

Status: accepted as non-operative design evidence — not an ADR-0033 blocker or runtime authorization

Recorded: 2026-07-21

## Purpose

Record the successful behavioural-donor study and frozen-contract composition candidate that makes a future Ptah Workspace easier for Hunter, humans and replaceable specialist agents to continue across Sessions, files, tools, Activities and restarts.

## Source boundary

The donor is OpenAI ChatGPT Projects and Work, observed only through official public documentation for Projects, project memory, Library, Work, Canvas and Scheduled Tasks.

The accepted integration class is `Study only`:

- no source-code reuse;
- no hidden prompt, schema, policy or proprietary implementation inference;
- no OpenAI runtime dependency;
- no ChatGPT-specific Core entity;
- no model-provider ownership of Workspace truth.

## Merged implementation-repository evidence

`Ptah-space` PR `#14` exact tested head:

```text
{PTAH_SPACE_HEAD}
```

Squash merge:

```text
{PTAH_SPACE_MERGE}
```

## Candidate identity

```text
ptah.workspace.ai_project.v1
```

The profile composes sixteen frozen Ptah primitives:

- Workspace, Session, Activity, Event and Attempt;
- Object, Revision, View and Artifact;
- Knowledge and Policy;
- Facility, Provider and Grant;
- Recipe and Receipt.

No new Core entity or frozen-contract change is proposed.

## Gap-map conclusion

Fourteen donor behaviours were classified:

- four covered directly by existing primitives;
- eight covered by profile composition;
- zero candidate extensions;
- two rejected or deliberately not adopted.

Rejected patterns:

1. hidden provider memory — Ptah context must be inspectable, exportable and source-bound;
2. implicit global tool access — Facilities require explicit Workspace or role Grants.

Any later implementation discovery that cannot be represented by the frozen primitive set must stop and request a versioned reopening ADR with migrations, fixtures and conformance evidence.

## Hunter bridge conclusion

The candidate responsibility split is:

- **Ptah:** Workspace identity, authority, Objects, Artifacts, Activities, Grants, privacy, Receipts, handoffs and recovery;
- **Hunter:** intent interpretation, planning, coordination, context requests, Activity proposals, Provider selection and candidate Artifact production;
- **Owner:** goals, protected-action approval, authority promotion, private-release decisions and final runtime authorization.

Hunter receives bounded context packets. A model response starts as `generated_candidate` and cannot directly change canonical truth.

## Proof package

The candidate includes ten positive/negative fixtures covering:

- cross-Workspace memory isolation;
- accepted-decision inheritance;
- superseded-source conflict handling;
- model-independent resume;
- Grant stability on agent replacement;
- least-privilege scheduled Artifact access;
- private Hunter/public Workspace separation;
- archived Session context selection;
- visible failed Activities and partial Artifacts;
- Artifact-to-Activity lineage.

Ten adversarial validator regressions enforce source completeness, no contract reopening, no new Core entity, non-authorization, authority classes, fixture identity, privacy and rejected hidden-memory behaviour.

## Exact-head workflow evidence

All ten workflows passed at `{PTAH_SPACE_HEAD}`:

| Lane | Workflow run |
|---|---:|
| AI Project Workspace candidate | `29824495268` |
| Frozen contract lock | `29824495206` |
| Generated contract bindings | `29824495326` |
| Host capability evidence | `29824495178` |
| Apache-2.0 acceptance | `29824495211` |
| Rust dependency policy | `29824495244` |
| Backend artifact evidence | `29824495186` |
| Backend signature evidence | `29824495190` |
| Signer lock boundary | `29824495223` |
| Scaffold, source, Browser and WP13 | `29824495166` |

The new lane checked out the exact head, ran all ten regressions, validated the donor/profile/gap/fixture package, bound report digests and retained evidence.

## Placement in Phase 0C

This candidate is useful future architecture but is deliberately not added to ADR-0033's physical-host acceptance conditions.

It does not:

- change the active physical-host proof blocker;
- close or add an ADR-0033 condition;
- change the first-slice proof burden;
- implement a context compiler, Workspace runtime, Artifact Library or Hunter bridge;
- authorize T01 or any WP14 runtime work.

## Conclusion

Ptah now has an evidence-bound, provider-independent composition candidate for the continuing project experience demonstrated by ChatGPT Projects and Work. Runtime implementation remains `NOT AUTHORIZED`, and the immediate continuation remains the exact physical Ubuntu host proof.
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    files = [
        write("CURRENT_STATE.md", current_state()),
        write("PROGRESS.md", progress()),
        write(
            "work-packages/PHASE-0C-15-AI-PROJECT-WORKSPACE-DONOR-AND-HUNTER-BRIDGE.md",
            work_package(),
        ),
    ]
    manifest = {
        "schema_version": "0.1.0",
        "record_type": "ptah.phase0c.ai_project_workspace_roadmap_sync",
        "source_commit": SOURCE_COMMIT,
        "ptah_space_exact_head": PTAH_SPACE_HEAD,
        "ptah_space_merge": PTAH_SPACE_MERGE,
        "files": files,
        "adr_0033_conditions_changed": False,
        "runtime_implementation_authorized": False,
    }
    write("sync-manifest.json", json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    main()
