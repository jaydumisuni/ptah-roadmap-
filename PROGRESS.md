# Ptah Progress Ledger

Tick only work backed by source inspection, pinned commits, accepted decisions, tests or live evidence.

- `[ ]` Not started
- `[-]` Active
- `[?]` Blocked or unresolved
- `[x]` Completed and evidenced

---

# Phase 0A — Donor recovery and requirement closure

**Status:** COMPLETE AND FROZEN

- [x] donor, internal-workload and licence recovery;
- [x] requirement closure and consistency review;
- [x] public/private boundary recorded;
- [x] ADR-0017 accepted;
- [x] frozen at `7d2dffee48f1400ba1cf88823343f09a3895ad33`.

---

# Phase 0B — Contracts, migrations, conformance and proof design

**Status:** COMPLETE AND FROZEN

- [x] WP01 — Common identity, versioning and typed families;
- [x] WP02 — Activity, Operation, Attempt, Event, Receipt and proof;
- [x] WP03 — Object, Revision, View, Artifact and storage;
- [x] WP04 — Node, Facility, Provider, capability and health;
- [x] WP05 — Workspace, Session, checkpoint and recovery;
- [x] WP06 — Transfer, synchronization, conflict, backup and restore;
- [x] WP07 — Recipe, Build, provenance, SBOM, signature and verification;
- [x] WP08 — Domain Pack, firmware, disk, filesystem and Device;
- [x] WP09 — Application, Browser, semantic UI and Shell;
- [x] WP10 — Knowledge, Data, Package and Plugin;
- [x] WP11 — Isolation, placement, reservation, Lease and secure grants;
- [x] WP12 — Security, Finding, Claim, Evidence, remediation and reproduction;
- [x] WP13 — executable cross-contract conformance;
- [x] WP14 — golden/negative corpus and first-slice proof-plan freeze;
- [x] all active schemas versioned and locally traceable;
- [x] lifecycle machines explicit and namespaced;
- [x] directional migrations and backend-replacement rules defined;
- [x] lawful positive, negative and adversarial fixtures pinned;
- [x] privacy, audience, redaction and retention represented;
- [x] WP13 found and forced correction of real cross-package defects;
- [x] WP13 exact-head unit, structural and semantic gates passed;
- [x] WP14 exact-head conformance passed;
- [x] ADR-0032 accepted;
- [x] frozen at `dc2db457f1705d0cba80f17ab76e5e93f808aee0`.

Key implementation-proof checkpoints:

- WP13 merge: `261b3e4a71657898643271a1625e14560a5bc769`;
- WP14 merge: `fef387c4f074af7fcf86f2d99f7f9b7637e91f88`.

Phase 0B completion defines implementation laws. It does not prove a Ptah runtime exists.

---

# Phase 0C — First vertical-slice approval

**Status:** ACTIVE — RUNTIME IMPLEMENTATION NOT AUTHORIZED

## Candidate selections and architecture records

- [x] implementation repository selected: `jaydumisuni/Ptah-space`;
- [x] Ubuntu Server 24.04.4 amd64 image pinned by SHA-256;
- [x] Noble GA 6.8 kernel line and mandatory capability requirements recorded;
- [x] Rust `1.97.1` selected for Node/control implementation;
- [x] SQLite `3.53.3` candidate selected behind repository-owned ledger boundary;
- [x] containerd `2.3.1` and runc `1.4.2` candidates selected behind OCI Provider boundary;
- [x] Node.js `24.18.0`, Playwright `1.60.0` and candidate Chromium build selected;
- [x] hardened Git `2.55.0` process adapter candidate selected;
- [x] libarchive `3.8.7` decomposition candidate selected;
- [x] source layout and public/private boundary recorded;
- [x] T00–T13 mapped to WP14 proof obligations;
- [x] exact-head CI acceptance shape recorded;
- [x] real workload candidates registered without promoting them into Ptah Core;
- [-] ADR-0033 remains proposed.

Selection/evidence package merge:

`79e83be0c340e871521d574719cdf6d20d52f4c9`

## Non-claiming implementation scaffold

- [x] 17 non-publishable Rust package boundaries merged;
- [x] initial empty third-party Rust dependency lock committed as non-claiming scaffold evidence;
- [x] private Browser scaffold and npm lock committed;
- [x] candidate cargo-deny policy committed;
- [x] initial host capability collector placeholder recorded as deliberately nonfunctional;
- [x] no-build and no-private-gateway guards merged;
- [x] initial exact-head scaffold workflow passed;
- [x] scaffold merge `ff26fa93d1b60781b49f33f5d1758680e1282d5f`.

## Hardened exact-head scaffold evidence

- [x] checkout Action pinned to `de0fac2e4500dabe0009e67214ff5f5447ce83dd`;
- [x] setup-python Action pinned to `a309ff8b426b58ec0e2a45f0f869d46889d02405`;
- [x] setup-node Action pinned to `48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e`;
- [x] upload-artifact Action pinned to `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`;
- [x] exact pull-request head checked out and verified in reports;
- [x] source-policy/no-build job passed;
- [x] Rust formatting, Clippy, tests and locked metadata passed;
- [x] Browser locked install, syntax, tests and dependency inventory passed;
- [x] frozen WP13 harness unit tests passed from `Ptah-space`;
- [x] frozen structural conformance passed from local files;
- [x] frozen semantic fixtures passed from local files;
- [x] four digest-addressed artifacts retained;
- [x] exact tested head `900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`;
- [x] passing workflow run `29717942201`;
- [x] hardening merge `23fc97ff0acd2b219990411ec4fb84d8a8c0a567`.

## Frozen catalog and generated binding closure

- [x] all fourteen frozen public catalogs locked by path, canonical URN and original-byte SHA-256;
- [x] catalog-set SHA-256 recorded as `f0668a5f5d5c68cabf623176608c627a94482faa4f4460e4f0fe0f0969d7c64d`;
- [x] 346 canonical schema bindings generated offline;
- [x] 99 lifecycle-machine bindings generated offline;
- [x] legacy catalog identifiers retained only as aliases;
- [x] generated manifest SHA-256 recorded;
- [x] generated catalog-index SHA-256 recorded;
- [x] generated Rust-module SHA-256 recorded;
- [x] generated output-tree SHA-256 `8f3355e0eac19715ea34e06ea227a826ac727d2e5b9ebf231a672927350c8db2` recorded;
- [x] two independent generated trees proved byte-identical;
- [x] generated Rust formatting, Clippy, compilation and tests passed;
- [x] no-build guard accepts the binding-locked state and still rejects runtime claims;
- [x] exact tested head `33043eaadb0f074d8867cb8ce999f16ea4c06a8b`;
- [x] catalog-lock workflow run `29727701958` passed;
- [x] binding-generation workflow run `29727701960` passed;
- [x] source/Rust/Browser/frozen-WP13 workflow run `29727701999` passed;
- [x] binding package merge `f45c96e3f667b463042b6a8b714066236fde703d`.

## Runtime dependency, backend signer and host-collector evidence

- [x] minimal exact Rust crate/features graph selected: ten direct crates;
- [x] final `Cargo.lock` committed with 99 resolved packages, 81 registry packages and zero Git dependencies;
- [x] crates.io sources and checksums recorded;
- [x] cargo-deny advisory, ban, licence and source policy passed at the exact candidate head;
- [x] nine selected distributed/source backend artifacts locked and verified against authoritative identities;
- [x] Playwright Chromium version `148.0.7778.96`, revision `1223` and installed-tree digest locked and reproduced;
- [x] Node.js, runc, Git and libarchive signing authorities pinned;
- [x] all four selected backend signatures cryptographically verified;
- [x] fail-closed host capability collector implemented for eighteen required capabilities;
- [x] realistic Ubuntu point-release and frozen-kernel identity finalizer implemented;
- [x] malformed contract-lock and malformed-blocker paths fail with controlled evidence diagnostics;
- [x] all eight workflows passed at exact head `bc12885ce41844b05481628543219c3a8d3574ba`;
- [x] negative HTTP `504` signature-attempt evidence retained and successful unchanged-lock retry passed;
- [x] implementation evidence squash-merged as `c2cd803b5e5c50787b3d8c2d24392d693afdbb3c`;
- [x] runtime authorization remained false in every accepted record.

## Active Phase 0C closure work

- [x] select the minimal external Rust crate/features graph;
- [x] produce the final runtime-candidate `Cargo.lock`;
- [x] run crate licence, advisory, ban and source policy;
- [x] lock authoritative hashes for every selected distributed/source backend artifact;
- [x] pin and cryptographically verify Node.js, runc, Git and libarchive signing authorities;
- [x] implement the host capability collector and identity finalizer;
- [x] add dependency, backend, signer and host-collector evidence to exact-head CI;
- [ ] produce a proof-eligible report from the exact pinned Ubuntu image/kernel revision;
- [ ] record the exact installed package manifest and package-artifact digests from that host;
- [ ] persist final evidence beyond temporary CI artifact retention;
- [?] owner acceptance of Apache License 2.0 and the public/private contribution boundary;
- [ ] add accepted public `LICENSE`, `NOTICE`, contribution and security files;
- [ ] conduct the Phase 0C closure consistency review;
- [ ] accept ADR-0033;
- [ ] change `CURRENT_STATE.md` to `Runtime implementation: AUTHORIZED`.

## No-build boundary

- [x] scaffold remains non-claiming;
- [x] generated bindings remain metadata-only;
- [x] dependency, backend, signer and host evidence remain non-authorizing;
- [x] no Node, Workspace, Activity, Provider or UI runtime is claimed;
- [x] no public licence is claimed before owner acceptance;
- [x] donor/workload identity remains outside Ptah Core;
- [x] WP13 and WP14 proof burdens remain unchanged;
- [ ] runtime implementation authorized.

---

# Implementation phases

No implementation phase may begin or be ticked before Phase 0C authorization.

- [ ] Phase 1 — Concurrent one-Node substrate.
- [ ] Phase 2 — Intake and transfer.
- [ ] Phase 3 — Universal decomposition.
- [ ] Phase 4 — Firmware, disks and filesystems.
- [ ] Phase 5 — Git, containers, environments and Builds.
- [ ] Phase 6 — Browser and live web.
- [ ] Phase 7 — Human Workspace shell.
- [ ] Phase 8 — Session Vault.
- [ ] Phase 9 — Applications and devices.
- [ ] Phase 10 — Knowledge, data, search, Recipes and Plugins.
- [ ] Phase 11 — Provenance and security workloads.
- [ ] Phase 12 — Distributed Ptah.
- [ ] Phase 13 — OS readiness.
