# Ptah Roadmap

Private canonical roadmap, recovery memory, progress ledger, and decision control for **Ptah Space**.

This repository answers four questions:

1. What is Ptah meant to become?
2. What phase is active now?
3. What has been completed and proven?
4. What must the next chat read before continuing work?

## Repository boundary

- `jaydumisuni/Ptah-space` contains the public implementation, public-safe technical documentation, current build slice, and completed code.
- `jaydumisuni/ptah-roadmap-` contains the complete private roadmap, donor recovery, internal progress, sequencing, decisions, and chat recovery state.
- The public Ptah repository must not expose private consumers, private operating-system use, internal company chains, or this private control repository.

## Recovery order for every new chat

Read these files in order before proposing or performing Ptah work:

1. `CURRENT_STATE.md`
2. `MASTER_ROADMAP.md`
3. `PROGRESS.md`
4. `DECISIONS.md`
5. `MEMORY_PROTOCOL.md`
6. `DONOR_RECOVERY.md`
7. The current files and open work in `jaydumisuni/Ptah-space`

Do not ask the user to repeat information recoverable from these files.

## Highest rules

- Ptah is the world where work happens, not the intelligence deciding what work should happen.
- Ptah is independent and open source. Private systems may use it, but they do not define its public identity.
- A workspace is persistent and can host many concurrent activities.
- Files are structured objects, not opaque blobs.
- Internet access is a normal workspace capability.
- Active work uses fast local storage; durable objects and artifacts may be synchronized remotely.
- Existing internal and external work must be recovered before a facility is rebuilt.
- No implementation begins merely because an idea is interesting. It must be in the roadmap, selected as current work, and approved.
- Every work item follows: **Understand → Build → Review → Freeze → Prove → Submit/Ship**.

## Status vocabulary

- `NOT STARTED`
- `ACTIVE`
- `BLOCKED`
- `IN REVIEW`
- `FROZEN`
- `PROVEN`
- `COMPLETE`
- `PARKED`
- `REJECTED`

## Update rule

After every approved Ptah work session:

1. Update `CURRENT_STATE.md` with the exact active checkpoint and next action.
2. Tick only evidence-backed items in `PROGRESS.md`.
3. Record architecture changes in `DECISIONS.md`.
4. Update donor records when a repository is inspected, pinned, adopted, wrapped, adapted, rejected, or replaced.
5. Update `MASTER_ROADMAP.md` only when the accepted plan genuinely changes.
6. Update the public `Ptah-space` repository only with the implementation slice being built and the public-safe progress it has actually earned.

## Current position

The architecture has been accepted in principle. Runtime implementation has not begun. The active stage is **Phase 0A — Recovery and donor closure**.
