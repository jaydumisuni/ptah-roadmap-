# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — scaffold and CI conditions passed; implementation remains unauthorized

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, runtime dependency lock, installed environment and proof obligations are accepted.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-IMAGE-AND-CAPABILITY-PIN.md`;
- `dependencies/PHASE-0C-FIRST-SLICE-EXTERNAL-DEPENDENCY-AND-LICENCE-MATRIX.md`;
- `dependencies/PHASE-0C-GITHUB-ACTION-IMMUTABLE-PINS.md`;
- `work-packages/PHASE-0C-03-FIRST-SLICE-TASK-GRAPH-TO-WP14-PROOFS.md`;
- `conformance/phase-0c/FIRST-SLICE-EXACT-HEAD-CI-GATE.md`;
- `work-packages/PHASE-0C-04-SCAFFOLD-AND-CI-EVIDENCE-REVIEW.md`.

Candidate selections:

- Ubuntu Server 24.04.4 LTS amd64 installation image pinned by SHA-256;
- runtime kernel and host capabilities measured per exact Node generation;
- Rust 1.97.1 as the primary Node/control implementation toolchain;
- `jaydumisuni/Ptah-space` as the implementation repository;
- 17 Ptah-owned non-publishable Rust package boundaries for the first-slice architecture;
- SQLite 3.53.3 WAL behind a repository-owned ledger interface;
- native Linux PTY/process supervision;
- containerd 2.3.1 LTS with runc 1.4.2 behind an OCI Provider boundary;
- Node.js 24.18.0 LTS and Playwright 1.60.0 with a private, locked Browser scaffold;
- hardened Git 2.55.0 CLI adapter;
- libarchive 3.8.8 first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge, restricted adapters, credentials and customer data.

## Completed evidence

### Source layout and scaffold

The non-claiming implementation scaffold is merged at:

`ff26fa93d1b60781b49f33f5d1758680e1282d5f`

It contains the selected Rust package boundaries, Browser package boundary, host/contract candidate locks and no-build guard while explicitly keeping runtime implementation unauthorized.

### Exact-head CI and frozen conformance

Evidence hardening was tested at exact head:

`900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`

Workflow run:

`29717942201`

Passed jobs:

- source-policy/no-build boundary;
- Rust formatting, Clippy, tests and locked metadata;
- Browser locked install, syntax check, tests and dependency inventory;
- frozen WP13 harness unit, structural and semantic conformance.

All jobs retained exact-head artifacts, and the workflow hardening merged at:

`23fc97ff0acd2b219990411ec4fb84d8a8c0a567`

GitHub Actions are immutable-pinned in the accepted action record.

## Current condition status

1. **Owner licence decision — open.** Apache-2.0 remains a recommendation only.
2. **Host image/capability pin — candidate complete.** The exact ISO digest and mandatory acceptance profile are recorded.
3. **Implementation source layout/scaffold — complete.** The selected package boundaries are merged and non-claiming.
4. **Dependency versions/licences — partial.** External candidates, action commits, zero-external-dependency Rust scaffold and Browser npm graph are pinned; runtime Rust crates and installed binary/browser evidence remain open.
5. **Task graph to WP14 — candidate complete.** T00–T13 map P01–P15 and N01–N12 to code and evidence.
6. **CI gate — complete for the scaffold.** Exact-head source, Rust, Browser and frozen conformance jobs passed with retained artifacts.
7. **Installed host/backend/browser evidence — open.** No admitted physical/VM Node and no executable Browser/runtime backend inventory has yet passed acceptance.
8. **Runtime authorization — blocked.** `CURRENT_STATE.md` remains `Runtime implementation: NOT AUTHORIZED`.

The detailed status is maintained in `work-packages/PHASE-0C-SELECTION-CLOSURE-STATUS.md`.

## Conditions before acceptance

This ADR remains proposed until:

1. the owner accepts or amends the public licence and contribution boundary;
2. the runtime Rust crate/features graph and amended `Cargo.lock` are reviewed and pinned;
3. licence/advisory reports pass for every selected runtime crate;
4. exact installed Ubuntu package/kernel and mandatory capability evidence are produced;
5. exact installed SQLite, containerd, runc, Git and libarchive versions/digests are produced;
6. the selected Playwright Chromium executable, digest and notices are produced;
7. final Phase 0C consistency review accepts the source layout, toolchain, backends, dependencies and proof plan;
8. this ADR changes to accepted;
9. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED`.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- the current 17 Rust crates and Browser package are architectural boundaries, not completed runtime capabilities;
- the initial workload candidates reviewed from THETECHGUY repositories remain deferred until their exact commits, interfaces, licences and proof roles are accepted;
- failure of any condition leaves implementation unauthorized.