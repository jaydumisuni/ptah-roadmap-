# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — four supporting selection records completed; implementation remains unauthorized

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, dependency lock and proof obligations are accepted.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-IMAGE-AND-CAPABILITY-PIN.md`;
- `dependencies/PHASE-0C-FIRST-SLICE-EXTERNAL-DEPENDENCY-AND-LICENCE-MATRIX.md`;
- `work-packages/PHASE-0C-03-FIRST-SLICE-TASK-GRAPH-TO-WP14-PROOFS.md`;
- `conformance/phase-0c/FIRST-SLICE-EXACT-HEAD-CI-GATE.md`.

Candidate selections:

- Ubuntu Server 24.04.4 LTS amd64 installation image pinned by SHA-256;
- runtime kernel and host capabilities measured per exact Node generation;
- Rust 1.97.1 as the primary Node/control implementation toolchain;
- `jaydumisuni/Ptah-space` as the implementation repository;
- SQLite 3.53.3 WAL behind a repository-owned ledger interface;
- native Linux PTY/process supervision;
- containerd 2.3.1 LTS with runc 1.4.2 behind an OCI Provider boundary;
- Node.js 24.18.0 LTS and Playwright 1.60.0 with its pinned browser revision;
- hardened Git 2.55.0 CLI adapter;
- libarchive 3.8.8 first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge, restricted adapters, credentials and customer data.

## Current condition status

1. **Owner licence decision — open.** Apache-2.0 remains a recommendation only.
2. **Host image/capability pin — candidate complete.** The exact ISO digest and mandatory acceptance profile are recorded.
3. **Dependency versions/licences — partial.** External tools/backends are pinned; the direct Rust crate graph, immutable CI action pins, exact installed package inventory and downloaded browser digest remain open.
4. **Task graph to WP14 — candidate complete.** T00–T13 map P01–P15 and N01–N12 to code and evidence.
5. **CI gate — design complete, implementation open.** The workflow must exist and pass on the exact `Ptah-space` scaffold commit.
6. **Runtime authorization — blocked.** `CURRENT_STATE.md` remains `Runtime implementation: NOT AUTHORIZED`.

The detailed status is maintained in `work-packages/PHASE-0C-SELECTION-CLOSURE-STATUS.md`.

## Conditions before acceptance

This ADR remains proposed until:

1. the owner accepts or amends the public licence and contribution boundary;
2. the Phase 0C scaffold exists in `jaydumisuni/Ptah-space` without claiming runtime completion;
3. the direct Rust crate/features graph and `Cargo.lock` are reviewed and pinned;
4. CI actions are pinned to immutable commits and their licences are recorded;
5. the exact-head scaffold CI passes Rust, dependency policy and frozen WP13 conformance jobs with retained artifacts;
6. exact installed host package/kernel and browser executable evidence can be produced by the acceptance procedure;
7. the final Phase 0C review accepts the source layout, toolchain, backend and proof plan;
8. this ADR changes to accepted;
9. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED`.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- the initial workload candidates reviewed from THETECHGUY repositories remain deferred until their exact commits, interfaces, licences and proof roles are accepted;
- failure of any condition leaves implementation unauthorized.