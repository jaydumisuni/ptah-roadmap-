# Phase 0C-04 — Implementation source layout and boundary acceptance

Status: candidate — runtime implementation remains unauthorized

## Repository decision

The public implementation repository remains:

```text
jaydumisuni/Ptah-space
```

The roadmap/control repository remains the authority for frozen contracts, ADRs, work-package history, conformance source and implementation authorization. `Ptah-space` must remain implementation-focused and must not absorb private recovery memory, customer data or proprietary THETECHGUY operating knowledge.

## Accepted top-level layout

```text
Cargo.toml
Cargo.lock
rust-toolchain.toml
LICENSE
NOTICE
README.md
SECURITY.md
CONTRIBUTING.md
deny.toml

crates/
  ptah-contracts/
  ptah-identifiers/
  ptah-ledger/
  ptah-events/
  ptah-receipts/
  ptah-node-agent/
  ptah-activity-runtime/
  ptah-workspace/
  ptah-object-store/
  ptah-transfer/
  ptah-provider-api/
  ptah-checkpoint/

services/
  ptah-node/
  ptah-control/

adapters/
  container-oci/
  browser-playwright/
  git-cli/
  decomposition-libarchive/

browser-provider/
  package.json
  package-lock.json
  src/

contracts/
  upstream-lock.json
  generated/

conformance/
  phase-0b/
  vertical-slice/

host/
  image-lock.json
  capability-profile.json
  systemd/
  scripts/

docs/
  architecture/
  operations/
  development/
```

## Ownership boundaries

### `ptah-contracts`

- generated or hand-maintained bindings derived from frozen public schema catalogs;
- stores source catalog URNs, versions and digests;
- may not redefine a schema locally without the roadmap reopening process;
- generated code must be reproducible from the recorded catalog revision.

### `ptah-identifiers`

- typed Ptah IDs and URN parsing;
- no backend IDs, paths or process IDs may masquerade as canonical identity;
- backend identifiers are represented only as scoped Aliases or evidence.

### `ptah-ledger`

- repository-owned persistence interfaces and migrations;
- SQLite implementation is private to the backend module;
- public domain objects cannot expose SQL row IDs as identity.

### `ptah-activity-runtime`

- Ptah Activity, Operation and Attempt lifecycle authority;
- systemd, process IDs, container task IDs and browser task IDs are evidence only;
- retries always create new Attempt identity.

### `ptah-workspace`

- persistent Workspace/Session state, attachments and recovery projections;
- client disconnect cannot equal Workspace termination.

### `ptah-object-store`

- Object, Revision, Artifact and Location persistence;
- paths and storage-provider keys are Locations/Aliases, not Artifact identity.

### `ptah-transfer`

- partial-state retention, resume, streaming digest and destination verification;
- transfer backend acknowledgements cannot become completion without verification.

### `ptah-provider-api`

- capability declarations, Provider generation, health, replacement and fencing boundary;
- adapters depend inward on this boundary; core crates do not depend on adapter implementation packages.

### adapters

- own backend translation only;
- cannot own canonical Ptah identity or lifecycle truth;
- must expose capability, version, generation, limitations and replacement metadata;
- must retain exact command/API evidence and sanitized logs.

## Dependency-direction rule

```text
services -> domain/runtime crates -> contract/identifier crates
adapters -> provider API + contract crates
core crates -X-> concrete adapters
```

Circular dependencies between core crates and adapters are prohibited.

## Public/private boundary

Permitted in the public implementation repository:

- Ptah-owned generic runtime source;
- public schemas or generated bindings from frozen public catalogs;
- generic adapters for publicly documented tools and protocols;
- lawful generic fixtures;
- public operations and development documentation;
- third-party notices and licence inventories.

Prohibited from automatic publication:

- private THETECHGUY Domain Packs;
- customer/device identifiers and evidence;
- credentials, approval grants and signing material;
- proprietary repair protocol knowledge;
- restricted recovery adapters;
- Hunter private prompts, memory or internal operating data;
- donor source not cleared for redistribution.

Private extensions must consume public Ptah Plugin/Domain Pack/Provider boundaries rather than require private forks of canonical identity.

## Contract import rule

`contracts/upstream-lock.json` must record:

- roadmap repository;
- exact freeze commit;
- selected catalog paths and URNs;
- file digests;
- generator version;
- generated-output digest;
- conformance harness version.

CI must fail when generated bindings do not match the locked frozen catalogs.

## Versioning and migrations

- ledger migrations are directional, numbered and immutable after release;
- every persisted record includes schema/entity version information required by the frozen contracts;
- destructive migration shortcuts are prohibited;
- rollback means restoring a compatible checkpoint or applying a reviewed reverse/compensating migration, not editing migration history.

## Implementation staging rule

Before runtime authorization, the repository may receive only non-claiming scaffolding needed to prove selection closure:

- workspace manifests;
- empty crate/service boundaries;
- licence and notice files;
- dependency locks;
- generated bindings;
- CI and conformance wiring;
- host/dependency lock records.

It may not claim a working Node, Workspace, Provider or UI until authorization is explicitly merged.

## Acceptance tests

The layout is acceptable only if automated checks prove:

1. core crates do not import concrete adapter crates;
2. backend IDs are not exposed as canonical identifier types;
3. generated contracts match the upstream lock;
4. public packaging excludes private/restricted paths;
5. every direct dependency appears in the licence inventory;
6. no credential-like fixture enters source control;
7. roadmap/control documents are linked rather than copied as mutable authority.

## Replacement and split strategy

The monorepo layout is selected for the first slice to keep atomic contract/runtime changes and reproducible CI. Individual Providers may later move to separate repositories when their API, release and compatibility boundaries are proven. Repository movement must not change canonical Ptah identity.