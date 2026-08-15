# AI Start Here — Ptah

You are continuing the Ptah Space project.

Do not answer from chat memory alone. Recover the project from this repository before proposing, designing, editing, or building anything.

## Required reading order

1. `CURRENT_STATE_AMENDMENT_2026-08-15.md`
2. `CURRENT_STATE.md`
3. `MASTER_PLAN.md`
4. `IMPLEMENTATION_ROADMAP.md`
5. `MASTER_ROADMAP.md`
6. `PROGRESS.md`
7. `DECISIONS.md`
8. `decisions/ADR-0038-PRIME-HOST-DEVELOPMENT-QUALIFICATION.md`
9. `MEMORY_PROTOCOL.md`
10. `DONOR_RECOVERY.md`
11. `REQUIREMENT_CLOSURE_MATRIX.md`
12. `WORK_ITEM_TEMPLATE.md`
13. Current source and public-safe technical documentation in `jaydumisuni/Ptah-space`
14. Any donor or internal repository directly related to the selected work item

The 2026-08-15 current-state amendment supersedes only the stale P01 standalone-Ubuntu host interpretation in `CURRENT_STATE.md`. Historical evidence remains preserved.

## Current position

- Ptah architecture: accepted planning baseline
- Active phase: Phase 0C
- Active work unit: P01D — Kratos physical development-host qualification
- Runtime implementation: not authorized until P01D physical evidence is reviewed and accepted
- Prime-native integration proof: P01P — deferred/open; does not block A01 after P01D closure
- Public implementation repo: `jaydumisuni/Ptah-space`
- Private roadmap and recovery repo: this repository

## Core identity

Ptah is an independent, open-source, online-first and later local-first concurrent digital working world.

Ptah provides the workplace, tools, files, internet, storage, terminals, browsers, containers, applications, firmware, devices, rendering, sessions and artifacts.

The human or compatible calling system supplies intent, reasoning, priorities, instructions, restrictions and acceptance criteria.

Ptah is the world where work happens, not the intelligence deciding what work should happen.

Ptah stays OS-neutral. In the intended Prime deployment, Prime owns machine authority and Ptah consumes Prime-exposed capabilities through an explicit integration boundary. `Prime Host ID` and `Ptah Node ID` remain distinct.

## Current host/testing rule

- Use Kratos's current installed system for P01D physical development testing.
- Do not install or boot a second server OS solely for Ptah.
- Do not create a dedicated guest VM solely to satisfy the old host pin.
- Use Oracle MCP/RPC as the current private control path for the Kratos proof.
- Keep public Ptah proof tooling provider-neutral; private machine/control topology stays in this roadmap/recovery authority.
- Preserve the old Ubuntu 24.04.4 / `6.8.0-136-generic` proof kit as historical evidence; do not claim it passed.
- Move Prime-owned Linux isolation/resource mechanisms to the later P01P Prime-native capability proof rather than binding Ptah to an Ubuntu distribution identity.

## Mandatory rules

- Do not put the complete private roadmap into the public Ptah repository.
- Do not expose private consumers, machine names, private control topology or private operating-system integration publicly.
- Do not start implementation unless the exact item is on the roadmap, selected in current authority, dependency-ready and approved.
- Recover existing internal work before recommending a rebuild.
- Inspect donors beyond README claims.
- Record canonical upstream, pinned version, licence, exact components, limitations, code boundary, exit strategy and proof.
- Treat a workspace as persistent and capable of many concurrent activities.
- Treat files as structured objects with originals, children, derivatives, previews and provenance.
- Preserve live internet as a normal capability.
- Use fast local storage for active work and remote/object storage for durable copies and artifacts.
- Preserve `Prime Host ID != Ptah Node ID` and the Prime-machine/Ptah-mechanical authority split.
- Follow: Understand → Build → Review → Freeze → Prove → Submit/Ship.

## Before doing work

State:

1. recovered current phase;
2. exact roadmap item;
3. existing internal foundation;
4. donor evidence;
5. native Ptah gap;
6. dependencies;
7. public/private boundary;
8. proof plan;
9. whether build permission has been given.

## After approved work

Update:

1. implementation and evidence;
2. `PROGRESS.md`;
3. current-state authority;
4. `DECISIONS.md` when architecture changes;
5. `DONOR_RECOVERY.md` and the closure matrix when donor understanding changes;
6. `MASTER_ROADMAP.md` only when the accepted plan genuinely changes.

Do not ask the user to repeat information recoverable from these sources.
