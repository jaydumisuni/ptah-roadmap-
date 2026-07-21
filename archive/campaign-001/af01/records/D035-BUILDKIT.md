# D035 — BuildKit Archive Record

Outcome: ACCEPTED FOR ARCHIVE — build service donor; no default provider or runtime authorization

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P06`

Independent Verifier: `AF01-V06`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `moby/buildkit`;
- owner: Moby organization;
- visibility: public;
- archived: false;
- default branch: `master`;
- inspected commit: `4f4f9d52fcf3d58553fa5327452240c7ad7dd853`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root licence: Apache License 2.0;
- licence evidence: `LICENSE` blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`;
- frontend images, exporters, worker backends, toolchains and transitive dependencies require component review;
- activity state: active; inspected head is a merged maintenance change in an actively developed repository with BuildKit/frontend CI.

## Primary evidence packet — AF01-P06

Inspected:

- `README.md` blob `9699db6d1c62ee85832135d53edccd4ad5e67c07`;
- `cmd/buildkitd/main.go` blob `439a3d113fd5d8086c80004b9764024615ea7eaf`;
- root `LICENSE`;
- exact current head.

Verified:

- BuildKit converts source code to build artifacts with caching, concurrency, multiple outputs, distributable workers and pluggable frontends;
- runtime is split into the `buildkitd` daemon and `buildctl` client;
- daemon worker backends include OCI/runc and containerd;
- the daemon exposes gRPC and includes health/reflection, session, solver, frontend, cache, exporter and tracing machinery;
- source supports local/registry/inline/S3/Azure/GitHub Actions cache paths and OCI/image/local outputs;
- rootless operation exists but has distinct configuration and host capability requirements;
- daemon availability differs by platform and macOS normally requires a Linux VM for the daemon.

Primary conclusion:

BuildKit remains a foundation-grade build/artifact machinery donor and optional wrapped build service. Its solver, cache, worker, exporter and metadata patterns are useful, but BuildKit's daemon/session identities and cache success cannot become Ptah Activity/Object truth.

## Independent verification packet — AF01-V06

Repeated checks:

- canonical identity, `master` branch and exact inspected head;
- Apache-2.0 root licence;
- real daemon entry point and imported runtime subsystems;
- client/daemon separation, gRPC exposure and worker backends;
- rootless and host/platform limitations.

Challenges retained:

- remote cache and registry paths require credential, integrity and retention controls;
- build outputs must be registered as Ptah Objects/Artifacts with independent digests and Receipts;
- BuildKit cache hits are optimization evidence, not proof of source, policy or release acceptance;
- privileged/rootless worker behavior and backend compatibility require exact-host tests;
- frontend images and distributed artifacts require pins and provenance review.

Verifier conclusion: primary findings supported. No contradiction with WP03/ADR-0005 placement.

## Ptah relationship

- frozen donor group: Runtime, builds and isolation / build machinery;
- current classification: wrapped upstream build service or direct client dependency behind native Ptah contracts;
- requirements supported: concurrent builds, LLB/solver patterns, cache import/export, multiple outputs, worker selection, telemetry and build sessions;
- prohibited inheritance: donor daemon identity as Activity identity, cache state as canonical Object truth, unaudited frontend execution, unreceipted artifact promotion;
- replacement/exit strategy: preserve provider-neutral Build Activity/Artifact contracts and support BuildKit, Dagger or another backend through adapters.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current `master` branch and exact head supersede generic branch assumptions;
- current evidence confirms BuildKit is a service/toolkit component, not Ptah's whole build or proof architecture.

## Bounded outcome

`accepted for archive` does not select BuildKit as the default build backend, authorize daemon deployment, approve remote caches/frontends, reopen Phase 0A, accept ADR-0033 or authorize Ptah runtime implementation.
