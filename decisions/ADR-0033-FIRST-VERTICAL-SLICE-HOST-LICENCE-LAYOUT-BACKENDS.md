# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — selection records substantially complete; runtime implementation remains unauthorized

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, dependency locks, CI gates and proof obligations are accepted and demonstrated.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`.

The selected baseline is:

- Ubuntu Server 24.04.4 LTS amd64 installation image pinned by SHA-256;
- Noble GA 6.8 generic kernel line for the first proof image;
- Rust `1.97.1` as the primary Node/control implementation toolchain;
- `jaydumisuni/Ptah-space` as the implementation repository;
- SQLite `3.53.3` in WAL mode behind a repository-owned ledger interface;
- native Linux PTY/process supervision;
- containerd `2.3.1` with runc `1.4.2` behind an OCI Provider boundary;
- Node.js `24.18.0` LTS with Playwright `1.60.0` and its pinned Chromium build as the first Browser Provider;
- hardened Git `2.55.0` process adapter;
- libarchive `3.8.7` first decomposition adapter;
- repository-owned resumable transfer and local content-addressed storage;
- Apache License 2.0 recommendation for public Ptah-owned source, excluding private THETECHGUY knowledge, customer/device data and restricted workflows.

## Non-core workload registry

`work-packages/PHASE-0C-07-REAL-WORKLOAD-CANDIDATE-REGISTRY.md` records useful later proof workloads including `linux-0.11-rs`, MIBU, TTG Device X-Ray and TTG Device Manager. That registry does not select those projects as Ptah Core or first-slice dependencies.

## Conditions before acceptance

### Specified by candidate records

The following conditions now have concrete candidate decisions:

1. exact host image, kernel line and capability profile;
2. direct external dependency versions and licence boundaries;
3. implementation repository and source layout;
4. implementation task graph mapped to WP14 proof obligations;
5. required CI and immutable exact-head evidence shape.

### Still open

This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` contains the accepted non-claiming workspace scaffold;
3. exact `Cargo.lock`, `package-lock.json`, dependency inventory, authoritative artifact hashes/signatures and licence report are produced;
4. host image/package lock and capability-report generator are committed;
5. generated bindings are bound to the frozen roadmap catalogs and reproduce offline;
6. CI implements and passes Rust, Browser Provider, dependency-policy, WP13 and proof-plan preparation gates at the exact scaffold commit;
7. a Phase 0C closure review confirms no frozen contract was weakened;
8. this ADR is changed to accepted;
9. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- public Ptah Core remains separate from private THETECHGUY Domain Packs and restricted recovery adapters;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- security updates or dependency rebases create new Host/Provider revisions and require the relevant proof rerun;
- failure of any open condition leaves implementation unauthorized.

## Acceptance form

When the open conditions pass, the acceptance change must record:

- exact `Ptah-space` commit;
- exact dependency and host-lock digests;
- CI workflow/report digests;
- WP13 exact-head result;
- Phase 0C closure review;
- explicit implementation authorization.

A decision text without those artifacts is insufficient.