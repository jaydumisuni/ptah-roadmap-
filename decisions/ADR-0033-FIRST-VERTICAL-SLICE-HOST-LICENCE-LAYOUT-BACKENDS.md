# ADR-0033 — First vertical-slice host, licence, layout and backend selections

Status: proposed — Rust dependencies, distributed backend artifacts, signers, host collector, physical-proof and durable-retention tooling complete; physical pinned-host result, package and retention acceptance, licence acceptance and closure review remain open

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
- `work-packages/PHASE-0C-10-FROZEN-CATALOG-AND-GENERATED-BINDING-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-RUNTIME-DEPENDENCY-BACKEND-SIGNER-AND-HOST-COLLECTOR-EVIDENCE.md`;
- `work-packages/PHASE-0C-11-EVIDENCE-MANIFEST.json`;
- `work-packages/PHASE-0C-12-PINNED-HOST-PROOF-INTEGRITY-AND-PACKAGE-ARTIFACT-READINESS.md`;
- `work-packages/PHASE-0C-13-DURABLE-PINNED-HOST-RETENTION-READINESS.md`.

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

## Merged runtime dependency, backend signer and host-collector evidence

`Ptah-space` PR `#6` was tested at exact head:

```text
bc12885ce41844b05481628543219c3a8d3574ba
```

and squash-merged at:

```text
c2cd803b5e5c50787b3d8c2d24392d693afdbb3c
```

The merged evidence closes the candidate/evidence sub-gates for:

- ten exact direct Rust dependencies and final `Cargo.lock`;
- 99 resolved packages, 81 registry packages and zero Git dependencies;
- cargo-deny advisory, ban, licence and source policy;
- authoritative digests for all nine selected distributed/source backend artifacts;
- reproducible Playwright Chromium version `148.0.7778.96`, revision `1223` and installed-tree digest;
- pinned signing authorities and successful cryptographic verification for Node.js, runc, Git and libarchive;
- implementation of the fail-closed eighteen-capability host collector and realistic Ubuntu identity finalizer;
- exact-head host, dependency, backend, signer, source, Rust, Browser, frozen-contract, generated-binding and WP13 workflows;
- review regression coverage for malformed locks, realistic host identity and malformed blocker records.

The final `Cargo.lock` SHA-256 is:

```text
d68a06272d417d67049c7879570e3735607166ce1e7eff58e43df21e20c9117a
```

The locked Playwright Chromium installed-tree SHA-256 is:

```text
953a2e9c1fb18d1e698f0903a62c23c835264e939cdd08a85c41d57719a5de7a
```

All eight final workflows passed at the exact candidate head. The backend-signature workflow's first attempt retained an upstream libarchive HTTP `504` as negative evidence. The independent immutable artifact lane had passed the same lock, and the unchanged-lock retry completed all four cryptographic checks.

A generic hosted Ubuntu report remains `proof_eligible: false` unless the exact point release, architecture and `6.8.0-136-generic` kernel identity match. The selected distributed artifact evidence does not replace the installed package manifest and package-artifact proof required from the real pinned host.

Every merged evidence record keeps runtime implementation unauthorized.

## Merged pinned-host proof integrity and package-artifact readiness

The proof-integrity repair was tested in `Ptah-space` PR `#9` at exact head:

```text
4e871b2bad8c4054ef1e9a1245219fa231338458
```

and squash-merged at:

```text
b97c2defbba17d75e32cb0a02cda9bbb2b1c6649
```

The exact installed-package artifact evidence gate was tested in PR `#10` at exact head:

```text
74aef4b6a4ddebb7f2491fc0eb127d945ac05a14
```

and squash-merged at:

```text
50969c414b55460b6ff7a7d12fd7ae88f5ef5c0a
```

The merged proof tooling now:

- accepts only the canonical host-capability collector;
- validates the capability report's own required-capability and pinned-host result;
- records one clean unchanged exact Git commit before and after collection;
- excludes only the fresh selected output directory from generated untracked-file evaluation;
- hashes retained hostname, machine ID and boot ID values;
- captures exact installed `dpkg` package/version/architecture identities;
- resolves exact local APT binary-artifact `Filename`, `Size` and SHA-256 metadata in bounded queries;
- requires both APT release metadata and package-index evidence;
- fails closed on malformed package identities, missing or conflicting artifact records, absent index classes, capability failures or repository changes;
- emits host, capability, installed-package, package-artifact, APT-source and aggregate bundle records;
- preserves `network_used: false` for package-artifact collection and `runtime_implementation_authorized: false` throughout.

All eight exact-head workflows passed for both PRs. Final host workflow run `29811724538` checked out `74aef4b6a4ddebb7f2491fc0eb127d945ac05a14` and passed the host collector, identity finalizer, package-artifact and pinned-host proof regressions.

This evidence proves that the physical-host proof kit is ready and fail-closed. It does not prove that the real frozen host or its installed package boundary has passed.

## Merged durable pinned-host retention readiness

The repository-bound retention lane was tested in `Ptah-space` PR `#11` at exact head:

```text
f0c1aafb58b33fcc8338081244996ced9260ce5c
```

and squash-merged at:

```text
49f6035a93bf704d775dc437e8a8b25c95145ae1
```

The merged retention tooling now:

- independently re-verifies every source file, aggregate digest and cross-record proof condition;
- requires exact host, capability, installed-package, package-artifact, APT-index and non-empty APT-source evidence;
- binds the source bundle to the current clean exact repository commit and canonical collector bytes;
- records the reviewed proof-runner digest;
- rejects wrong commits, collector mismatch, authorizing records, symlinks, nested paths, overwrite attempts and unexpected repository changes;
- preserves exact source bytes in a durable base64 candidate;
- emits an exact repository binding;
- emits a separate review record with `review_status: pending` and every physical-host, package, retention, ADR and runtime acceptance field `false`;
- verifies the final durable directory contains exactly the expected four records and rechecks clean unchanged repository state.

All eight exact-head workflows passed. Host workflow run `29813401728` checked out `f0c1aafb58b33fcc8338081244996ced9260ce5c` and passed the complete collection and retention regression suite.

This evidence proves that a future physical-host bundle can be independently verified and durably prepared without conflating storage with acceptance. It does not prove or accept the real host, package boundary or retained bundle.

## Conditions before acceptance

### Completed at candidate/evidence level

1. exact host image, kernel line and capability requirements;
2. direct external dependency version and licence candidates;
3. implementation repository and source layout;
4. implementation task graph mapped to WP14 proof obligations;
5. required CI and immutable exact-head evidence shape;
6. a merged non-claiming Rust/Browser workspace scaffold;
7. exact Playwright npm lock and final Rust `Cargo.lock`;
8. passing source-policy, Rust and Browser scaffold jobs;
9. immutable GitHub Action commit pins;
10. passing frozen WP13 unit, structural and semantic conformance from `Ptah-space`;
11. retained exact-head artifact IDs and digests;
12. complete frozen public catalog inventory by path, URN, size and original-byte digest;
13. deterministic offline generated metadata bindings;
14. generated manifest, index, Rust-module and output-tree digests;
15. two independent byte-identical generation runs;
16. generated Rust formatting, Clippy, compilation and tests at the same exact head;
17. minimal exact Rust crate/features graph selection;
18. registry source/checksum inventory and zero-Git-dependency enforcement;
19. cargo-deny advisory, ban, licence and source policy;
20. authoritative identity and digest verification for all nine selected distributed/source artifacts;
21. reproducible Playwright Chromium revision and installed-tree lock;
22. stable signer locks and cryptographic verification for Node.js, runc, Git and libarchive;
23. fail-closed host capability collector and realistic Ubuntu identity finalizer;
24. exact-head dependency, backend, signer and host-collector workflows;
25. review regressions for malformed lock, host identity and blocker data;
26. canonical, privacy-preserving pinned-host bundle generation at one clean unchanged commit;
27. exact installed-package inventory generation;
28. local exact version/architecture APT artifact SHA-256 collection;
29. fail-closed package-artifact and APT index completeness validation;
30. exact-head integration coverage for the physical-host proof command;
31. independent exact-byte and cross-record source-bundle verification;
32. clean exact-repository and canonical collector binding before and after retention;
33. deterministic durable candidate, repository binding and pending review record generation;
34. fail-closed separation between durable storage and owner/reviewer acceptance;
35. exact-head adversarial coverage for the full durable-retention path.

### Still open

This ADR remains proposed until all of the following are complete:

1. the owner accepts the Apache-2.0 public/private boundary;
2. `Ptah-space` adds the accepted public `LICENSE`, final `NOTICE` and contribution/security boundary;
3. a proof-eligible capability report is produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
4. the exact installed Ubuntu package manifest and package-artifact digests are recorded from that host and accepted by review;
5. that host's exact source bundle is independently verified, durably committed and explicitly accepted through its review record;
6. a Phase 0C closure review confirms no frozen contract was weakened;
7. this ADR is changed to accepted;
8. `CURRENT_STATE.md` is updated to `Runtime implementation: AUTHORIZED` in the same reviewed closure change.

## Consequences

- the first slice remains one-Node and local-first;
- distributed transport, PostgreSQL, ORAS, BuildKit and stronger isolation remain replaceable later backends;
- backend IDs remain Aliases;
- public Ptah Core remains separate from private THETECHGUY Domain Packs and restricted recovery adapters;
- concrete implementation may not weaken any frozen Phase 0B identity, lifecycle, migration or proof boundary;
- security updates or dependency rebases create new Host/Provider revisions and require the relevant proof rerun;
- generated bindings are metadata only and cannot authorize T01 runtime work;
- the current scaffold, catalog lock, generated bindings, dependency graph, backend artifacts, signer proofs, host collector, physical-proof tooling and durable-retention tooling do not authorize T01 runtime work;
- durable retention does not equal evidence acceptance;
- failure of any open condition leaves implementation unauthorized.

## Acceptance form

When the open conditions pass, the acceptance change must record:

- exact `Ptah-space` commit;
- exact dependency and host-lock digests;
- generated binding input/output digests;
- installed host package manifest and package-artifact digests;
- source bundle, durable bundle and repository-binding digests;
- explicit physical-host, package, artifact and retention review acceptance;
- CI workflow/report and durable evidence digests;
- WP13 exact-head result;
- Phase 0C closure review;
- explicit implementation authorization.

A decision text without those artifacts is insufficient.
