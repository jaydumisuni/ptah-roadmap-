# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — frozen catalogs and generated bindings complete; runtime dependencies, host proof, licence acceptance and closure review remain open

## Context

Phase 0B is frozen and Phase 0C is active. Runtime implementation remains unauthorized until the first concrete implementation set, public licence, source layout, dependency locks, generated contract bindings, host evidence, CI gates and proof obligations are accepted and demonstrated.

## Proposed decision

Adopt the selections recorded in the following Phase 0C records as the baseline for the first Ptah vertical slice:

- `work-packages/PHASE-0C-01-FIRST-SLICE-SELECTION-PROPOSAL.md`;
- `work-packages/PHASE-0C-02-HOST-BASELINE-PIN.md`;
- `work-packages/PHASE-0C-03-DIRECT-DEPENDENCY-LICENCE-RECORD.md`;
- `work-packages/PHASE-0C-04-SOURCE-LAYOUT-AND-BOUNDARY-ACCEPTANCE.md`;
- `work-packages/PHASE-0C-05-WP14-IMPLEMENTATION-TASK-AND-PROOF-MAP.md`;
- `work-packages/PHASE-0C-06-CI-EXACT-HEAD-ACCEPTANCE-GATE.md`;
- `work-packages/PHASE-0C-08-NONCLAIMING-SCAFFOLD-EVIDENCE-REVIEW.md`;
- `work-packages/PHASE-0C-09-IMMUTABLE-ACTION-AND-FROZEN-CONFORMANCE-EVIDENCE.md`;
- `work-packages/PHASE-0C-10-FROZEN-CATALOG-AND-GENERATED-BINDING-EVIDENCE.md`.

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

## Merged non-claiming scaffold evidence

The initial `Ptah-space` scaffold merged at:

```text
ff26fa93d1b60781b49f33f5d1758680e1282d5f
```

The initial exact head `2f1fcedaa398254e5fa4b82583675a08755fa953` passed workflow run `29717770393`, including the no-build guard, Rust `1.97.1` formatting/Clippy/tests and locked Browser Provider syntax/tests.

Evidence hardening was then tested at exact head:

```text
900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc
```

Workflow run `29717942201` passed:

- exact-head source-policy/no-build checks;
- Rust formatting, Clippy, tests and locked metadata;
- Browser locked installation, syntax, tests and dependency inventory;
- frozen WP13 harness unit, structural and semantic conformance from local files;
- retained per-lane reports under immutable GitHub Action commit pins.

The hardening merged at:

```text
23fc97ff0acd2b219990411ec4fb84d8a8c0a567
```

This evidence proves only the repository/toolchain scaffold and frozen-contract conformance gate. It does not prove a Ptah runtime.

## Merged frozen-catalog and generated-binding evidence

The frozen catalog and generated binding package was tested at exact head:

```text
33043eaadb0f074d8867cb8ce999f16ea4c06a8b
```

and merged at:

```text
f45c96e3f667b463042b6a8b714066236fde703d
```

The accepted lock records:

- fourteen active catalog paths, canonical URNs and original-byte digests;
- catalog-set SHA-256 `f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d`;
- final binding generator `ptah-phase0c-contract-bindings-final` version `0.3.0`;
- generated manifest SHA-256 `63fd0cb0fd4ef172271aa7a114e74bb24c0a9e70cc247faeff1db95f7a67d97d`;
- generated catalog-index SHA-256 `0f97e222d9baf9f90721d2a30dd2b31920b53489ae343b0430cc9089c8fdaf9c`;
- generated Rust-module SHA-256 `748e87f1a8cf2ed20d694aa716dd8f18b7ea4b3016372386202aeeaff687ae50`;
- output-tree SHA-256 `8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2`;
- fourteen catalogs, 346 canonical schemas and 99 lifecycle machines.

Exact-head runs `29727701958`, `29727701960` and `29727701999` passed the catalog lock, two independent byte-identical generations, source-policy/no-build guard, Browser scaffold, Rust formatting/Clippy/tests and frozen WP13 unit/structural/semantic conformance.

The generated crate provides metadata and lookup bindings only. It does not implement Ptah runtime behavior.

## Conditions before acceptance

### Completed at candidate/evidence level

1. exact host image, kernel line and capability requirements;
2. direct external dependency version and licence candidates;
3. implementation repository and source layout;
4. implementation task graph mapped to WP14 proof obligations;
5. required CI and immutable exact-head evidence shape;
6. a merged non-claiming Rust/Browser workspace scaffold;
7. exact empty Rust and Playwright npm locks for the scaffold;
8. passing source-policy, Rust and Browser scaffold jobs;
9. immutable GitHub Action commit pins;
10. passing frozen WP13 unit, structural and semantic conformance from `Ptah-space`;
11. retained exact-head artifact IDs and digests;
12. complete frozen public catalog inventory by path, URN, size and original-byte digest;
13. deterministic offline generated metadata bindings;
14. generated manifest, index, Rust-module and output-tree digests;
15. two independent byte-identical generation runs;
16. generated Rust formatting, Clippy, compilation and tests at the same exact head.

### Still open

This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` adds the accepted public `LICENSE`, final `NOTICE` and contribution/security boundary;
3. every selected external Rust crate, system package and distributed binary/source artifact has an exact lock, authoritative hash/signature, licence inventory and advisory review;
4. the host capability collector is implemented and a report is produced on the pinned host image revision;
5. CI runs dependency policy at the exact candidate commit;
6. final accepted reports are retained in a durable proof Location beyond temporary workflow artifact expiry;
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
- generated bindings are metadata only and cannot authorize T01 runtime work;
- the current scaffold, catalog lock and binding evidence do not authorize T01 runtime work;
- failure of any open condition leaves implementation unauthorized.

## Acceptance form

When the open conditions pass, the acceptance change must record:

- exact `Ptah-space` commit;
- exact dependency and host-lock digests;
- generated binding input/output digests;
- CI workflow/report and durable evidence digests;
- WP13 exact-head result;
- Phase 0C closure review;
- explicit implementation authorization.

A decision text without those artifacts is insufficient.