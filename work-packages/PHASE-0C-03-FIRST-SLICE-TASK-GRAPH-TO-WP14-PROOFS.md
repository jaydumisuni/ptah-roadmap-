# Phase 0C-03 — First-slice implementation task graph mapped to WP14 proofs

Status: candidate delivery plan — runtime implementation remains unauthorized

## Purpose

Turn the frozen WP14 proof burden into an ordered implementation graph. A task is not complete merely because code compiles; it closes only when its exact positive and negative proof artifacts are retained at one implementation commit.

## Proof identifiers

### Required positive proofs

- `P01` — one Linux Node has stable canonical identity and exact generation evidence;
- `P02` — one persistent Workspace survives detach and reconnect;
- `P03` — Object registration preserves stable identity and immutable Revision identity;
- `P04` — at least ten concurrent Activities retain independent cancellation and failure;
- `P05` — multiple terminals remain independently supervised with streamed output;
- `P06` — upload and resumable download retain partial state and verify digest;
- `P07` — hardened Git clone or mirror is a receipted Activity;
- `P08` — one isolated container path executes without backend identity leakage;
- `P09` — one persistent Browser path retains Profile/Page generation evidence;
- `P10` — one decomposition adapter preserves original bytes, coverage and unknown gaps;
- `P11` — Artifact registration binds exact Content digest and provenance;
- `P12` — checkpoint, restart and recovery are independently verified;
- `P13` — one backend replacement preserves stable Ptah identity;
- `P14` — one full run succeeds with no network schema resolution;
- `P15` — exact-head structural and semantic conformance reports are retained.

### Mandatory negative proofs

- `N01` — stale Provider generation is rejected;
- `N02` — stale Lease/fence is rejected;
- `N03` — retry Attempt identity or nonce reuse is rejected;
- `N04` — raw secrets in prohibited records/logs are rejected;
- `N05` — acknowledgement without independent verification cannot become success;
- `N06` — incomplete citation/claim support is rejected where knowledge proof is exercised;
- `N07` — expired Accepted Risk is rejected where security proof is exercised;
- `N08` — same-environment execution cannot claim independent reproduction;
- `N09` — path traversal is rejected;
- `N10` — partial transfer cannot claim complete verification;
- `N11` — stale semantic UI target is rejected;
- `N12` — checkpoint restore without new-generation recovery verification is rejected.

The first slice must execute every applicable frozen semantic fixture even when some higher-domain features are represented by the conformance harness rather than a public UI.

## Ordered task graph

## T00 — Repository and toolchain scaffold

Outputs:

- accepted Rust workspace layout;
- pinned `rust-toolchain.toml`;
- root workspace manifest with `publish = false` until the public licence is accepted;
- dependency policy and lockfile checks;
- CI workflow skeleton;
- frozen contract checkpoint reference;
- no claim of runtime implementation.

Proof binding: `P15`.

Blockers:

- licence field must not falsely claim owner acceptance;
- no generated binding may alter frozen schema identity.

## T01 — Contract bindings and canonical identifiers

Implement only derived bindings and common identifier utilities needed by the first slice.

Required behaviours:

- canonical UUIDv7 identity;
- scoped Alias support;
- schema/version metadata;
- typed entity-kind validation;
- no backend ID accepted as canonical identity.

Proof binding: `P01`, `P03`, `P11`, `P13`, `P15`.

Negative binding: reject malformed IDs, unknown entity kinds and backend-ID substitution.

## T02 — Durable ledger and migration boundary

Implement the repository-owned ledger interface with SQLite WAL as the first backend.

Required behaviours:

- transactional writes;
- append/immutable-record handling where contracts require it;
- schema migration table and directional migration evidence;
- canonical ID storage independent of SQLite row IDs;
- crash/restart durability tests;
- exact backend generation record.

Proof binding: `P01`, `P02`, `P03`, `P11`, `P12`, `P13`.

Negative binding: `N01`, `N05`, `N12`.

## T03 — Node agent and capability admission

Implement one Linux Node process and the Phase 0C host capability probe.

Required behaviours:

- Node identity persists;
- Node generation advances on host/runtime change;
- boot and machine evidence is collected without becoming canonical identity;
- health/readiness/pressure remain distinct;
- unsupported optional capabilities remain explicit negative evidence.

Proof binding: `P01`, `P14`.

Negative binding: `N01`.

## T04 — Activity, Operation, Attempt and Receipt runtime

Implement the smallest scheduler/executor that preserves WP02 boundaries.

Required behaviours:

- Activity versus Operation versus physical Attempt separation;
- ten concurrent Activities;
- independent cancellation/failure;
- new Attempt and nonce for every retry;
- Events do not become Receipts;
- acknowledgement does not become success;
- exact Provider generation retained.

Proof binding: `P04`, `P15`.

Negative binding: `N01`, `N03`, `N05`.

## T05 — Persistent Workspace and terminal supervision

Implement one persistent Workspace with multiple PTYs.

Required behaviours:

- Workspace identity survives client disconnect;
- Session/client/layout identity remains separate;
- multiple terminals have independent process and stream identity;
- output can be replayed or retained according to policy;
- detaching does not stop Activities;
- restart creates new runtime generations and requires recovery verification.

Proof binding: `P02`, `P05`, `P12`.

Negative binding: `N12`.

## T06 — Object, Content, Revision and local CAS

Implement source-byte intake and immutable identity.

Required behaviours:

- Content digest owns exact bytes;
- Object owns logical/source identity;
- Revision owns one immutable version;
- storage path is a Location, not identity;
- local CAS write uses temporary path, streaming digest, fsync and atomic promotion;
- Artifact registration remains a separate decision.

Proof binding: `P03`, `P11`, `P13`, `P14`.

Negative binding: `N09`, `N10` where intake is partial.

## T07 — Resumable transfer

Implement local upload/download transfer first.

Required behaviours:

- Request, Run, Attempt, progress, partial state and verification remain separate;
- resume uses retained manifest/state;
- streaming digest and destination read-back;
- interrupted transfer remains partial;
- complete status requires exact verification.

Proof binding: `P06`.

Negative binding: `N03`, `N05`, `N09`, `N10`.

## T08 — Hardened Git adapter

Implement Git 2.55.0 as an external CLI Provider.

Required behaviours:

- protocol allow-list;
- hooks disabled or explicitly governed;
- submodule policy explicit;
- unsafe paths rejected;
- exact command, version, exit and resulting repository evidence retained;
- Git commit/tree/blob IDs remain evidence/Aliases rather than Ptah Object IDs.

Proof binding: `P07`, `P03`, `P11`.

Negative binding: `N04`, `N09`.

## T09 — OCI container adapter

Implement containerd 2.3.1 LTS with runc 1.4.2 through a replaceable Provider boundary.

Required behaviours:

- exact image digest;
- Ptah-owned execution identity;
- container/task/backend IDs retained only as Aliases;
- cgroup/isolation profile evidence;
- stdout/stderr/exit and cleanup evidence;
- acknowledgement versus running/exit verification;
- stale Provider generation rejection.

Proof binding: `P08`, `P13`.

Negative binding: `N01`, `N02`, `N05`.

Backend-replacement proof:

- execute equivalent workload through a deterministic fake/reference adapter or second invocation path while preserving the same accepted Recipe/Object identity and producing a distinct Provider generation/Attempt set.

## T10 — Persistent Browser adapter

Implement Node.js 24.18.0 LTS plus Playwright 1.60.0 and its pinned browser revision.

Required behaviours:

- Browser Profile, Process, Context, Page and Frame remain Ptah-owned records;
- backend IDs are Aliases;
- browser/profile generation evidence retained;
- detach/reconnect preserves profile while fencing stale Page/Target generations;
- navigation acknowledgement does not equal postcondition success;
- sensitive storage/profile data is privacy-governed.

Proof binding: `P09`, `P12`.

Negative binding: `N04`, `N05`, `N11`, `N12`.

## T11 — libarchive decomposition adapter

Implement one archive decomposition path with libarchive 3.8.8.

Required behaviours:

- original Content/Object remains unchanged;
- child records bind exact parent Revision and ranges/entry identity;
- budgets for entries, bytes, recursion and time;
- encrypted, malformed and unsupported gaps retained;
- traversal and absolute-path extraction rejected;
- parser completion does not imply full coverage.

Proof binding: `P10`, `P03`, `P11`.

Negative binding: `N05`, `N09`.

## T12 — Checkpoint, restart and verified recovery

Implement a bounded checkpoint over first-slice components.

Required behaviours:

- checkpoint request, components, bundle and integrity verification remain separate;
- restart creates new Node/Provider/Workspace materialization generations where required;
- restored bytes/state do not imply recovered runtime;
- terminals, Activities and Browser state each report recoverability independently;
- uncertain external effects remain unresolved until reconciled.

Proof binding: `P02`, `P05`, `P09`, `P12`.

Negative binding: `N01`, `N02`, `N05`, `N12`.

## T13 — Offline and exact-head proof execution

Required behaviours:

- contracts/catalogs are available locally at the frozen checkpoint;
- no network schema resolution;
- all structural and semantic fixtures execute;
- reports are deterministic and include exact implementation commit;
- logs, Receipts and Artifacts are uploaded even on failure;
- green summary without reports is rejected.

Proof binding: `P14`, `P15` and all `Nxx` fixtures.

## Delivery order and concurrency

Hard dependency chain:

```text
T00 -> T01 -> T02 -> T03 -> T04
                    |      |
                    |      +-> T05 -> T12
                    +-> T06 -> T07
                           -> T08
                           -> T11
T03 -> T09
T03 -> T10
all implementation tasks -> T13
```

After T03/T04/T06 stabilize, T07 through T11 may proceed in parallel, but no adapter may invent missing canonical records locally.

## Required evidence per task

Every task must retain:

- source commit;
- Build Run and test Attempt identity;
- toolchain/backend versions and digests;
- positive case results;
- negative case results;
- structured logs;
- Receipts and verification decisions;
- known limitations;
- migration/replacement notes;
- cleanup result.

## First-slice acceptance gate

The first slice is accepted only when:

1. `P01` through `P15` pass at one exact implementation commit;
2. every mandatory negative proof is exercised and retained;
3. no backend identifier owns canonical Ptah identity;
4. the dependency and licence inventory matches the exact build;
5. failed/inconclusive evidence is preserved;
6. WP13 structural and semantic conformance passes offline;
7. a human review accepts the immutable proof bundle.

This plan closes the Phase 0C task-to-proof mapping condition. It does not authorize T01 or later implementation until ADR-0033 is accepted and `CURRENT_STATE.md` explicitly authorizes runtime implementation.