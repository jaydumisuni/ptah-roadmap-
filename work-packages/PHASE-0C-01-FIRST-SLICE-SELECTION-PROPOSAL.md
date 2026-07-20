# Phase 0C-01 — First vertical-slice implementation selection proposal

Status: proposed — implementation remains unauthorized

## Purpose

Select the smallest concrete implementation set capable of proving the frozen WP14 first vertical slice without allowing donor or backend identity to replace Ptah contracts.

## Proposed host baseline

- Linux distribution family: Ubuntu Server 24.04 LTS or a binary-compatible minimal derivative.
- CPU baseline: x86_64 first; architecture-neutral contracts preserved for later arm64 Nodes.
- Service model: systemd-managed local services.
- Filesystem assumption: ordinary local POSIX filesystem; shared/distributed filesystem semantics remain out of scope for the first slice.
- Isolation prerequisites: cgroups v2, namespaces and OCI-compatible container support.

The final implementation must pin the exact image/build digest and kernel capability profile before authorization.

## Proposed implementation language and repository layout

Primary language: Rust for the Node agent, durable control core and native service boundaries.

Repository: `jaydumisuni/Ptah-space`

Proposed workspace layout:

```text
crates/
  ptah-contracts/
  ptah-identifiers/
  ptah-ledger/
  ptah-node-agent/
  ptah-activity-runtime/
  ptah-workspace/
  ptah-object-store/
  ptah-transfer/
  ptah-provider-api/
  ptah-receipts/
services/
  ptah-node/
  ptah-control/
adapters/
  container-oci/
  browser-playwright/
  git-cli/
  decomposition-libarchive/
conformance/
  phase-0b/
  vertical-slice/
docs/
```

Rules:

- generated schema bindings remain derived from the frozen catalogs;
- adapters cannot own canonical identity;
- every adapter exposes a replacement boundary and capability declaration;
- backend-specific IDs are stored only as scoped Aliases/evidence.

## Proposed first backends

### Durable metadata and ledger

- SQLite in WAL mode for the one-Node first slice.
- A repository-owned storage interface must prevent SQLite assumptions from entering public contracts.
- PostgreSQL remains the first planned multi-Node replacement candidate, not a v1 contract dependency.

### Event and command transport

- In-process typed channels for same-process first-slice execution.
- Unix-domain socket or local HTTP/gRPC boundary for service separation.
- NATS remains a later distributed transport candidate; it is not required to prove one-Node Ptah.

### Process and terminal supervision

- Native Linux process supervision with PTY support.
- systemd is host service supervision only; Activity, Operation and Attempt lifecycle remains Ptah-owned.

### Container execution

- OCI/containerd-compatible adapter boundary.
- Initial local implementation may use containerd directly or a compatible local CLI bridge only when the exact command, version, runtime identity and Receipt evidence are retained.
- Build execution remains separate and may later use BuildKit behind the WP07 contracts.

### Browser

- Playwright with Chromium as the first interactive Browser implementation.
- Browser Profile, Process, Context, Page, Frame, Navigation and Download identities remain Ptah-owned.
- Playwright/browser IDs remain Aliases.

### Git

- hardened Git CLI adapter with protocol allow-listing, hook suppression and explicit submodule policy.
- repository/worktree identities remain Ptah Objects and Revisions.

### Decomposition

- libarchive-backed archive adapter for the first decomposition proof.
- unknown, partial, encrypted and malformed coverage must remain explicit.
- parser output cannot overwrite source Object truth.

### Transfer

- repository-owned resumable local/file transfer engine first.
- streaming digest, partial-state retention and destination read-back are mandatory.

### Artifact bytes

- local content-addressed storage directory for the first slice.
- exact digest and Artifact identity remain independent of storage path.
- ORAS/OCI registry support remains a later WP07/WP03 adapter.

### Observability

- structured JSON logs and Ptah Event/Receipt records are mandatory.
- OpenTelemetry export is optional in the first slice but the correlation fields must be preserved.

## Proposed public licence

Recommendation: Apache License 2.0 for public Ptah-owned source, subject to owner acceptance and a final licence-compatibility review.

Reasons:

- permissive commercial and community use;
- explicit patent grant;
- clear notice and modification requirements;
- compatible with a modular adapter ecosystem when third-party components retain their own licences.

Private THETECHGUY Domain Packs, credentials, proprietary protocol knowledge, customer data and restricted device workflows are not automatically included in the public licence.

No donor code may be copied merely because this licence is selected. Every dependency and adapted source retains its own licence/extraction decision.

## Frozen first-slice proof obligations

Authorization must bind implementation tasks to the WP14 proof plan, including:

1. Node identity and generation survive restart.
2. Workspace identity survives client disconnect and runtime restart.
3. ten concurrent Activities do not collapse into one job state.
4. each retry creates a new Attempt and correlation nonce.
5. multiple terminals remain independently supervised.
6. upload/download resume from retained partial state.
7. Git clone/mirror records hardened policy and exact result identity.
8. container backend identity remains an Alias.
9. Browser profile and Page generations are recoverable and fenced.
10. decomposition preserves originals, partial coverage and unknown gaps.
11. Artifact registration binds exact Content digest.
12. checkpoint does not equal restored runtime until verification.
13. stale generation, stale fence and acknowledgement-only cases fail with retained evidence.
14. all contract changes pass WP13 exact-head conformance.

## Authorization blockers

Implementation must remain unauthorized until all are merged:

- public licence acceptance;
- exact Linux image/kernel capability pin;
- exact initial dependency versions and licence records;
- source layout acceptance;
- implementation task graph mapped to WP14 proof cases;
- CI workflow for Rust, schema generation and WP13 conformance;
- ADR accepting or amending this proposal;
- explicit authorization line in `CURRENT_STATE.md`.

## Exit strategy

Every proposed backend is replaceable:

- SQLite → PostgreSQL or another ledger backend;
- local channels/socket → NATS or another transport;
- containerd-compatible adapter → another OCI runtime;
- Playwright/Chromium → another Browser Provider;
- Git CLI → libgit2 or another hardened implementation;
- libarchive → format-specific Domain Pack adapters;
- local CAS → ORAS/object storage.

Replacement must preserve canonical IDs, migration history, Receipts and conformance evidence.
