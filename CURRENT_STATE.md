# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Sessions and Artifacts.

Ptah supplies the working world; humans and compatible systems supply intent and reasoning.

The complete roadmap is stored in `MASTER_ROADMAP.md`.

---

# Mandatory closure method

Every requirement combines:

1. internal THETECHGUY foundation and intentional constraints;
2. primary capability donor;
3. completion donors;
4. mature upstream machinery and standards;
5. native Ptah contracts and integration;
6. fallback or exit path;
7. proof of the complete assembled subsystem.

One repository never closes a subsystem by itself. Research and decisions are committed after every meaningful inspection unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

# Completed and saved work packages

## WP01 — Node and Workspace boundary

Established separate Node Protocol and Workspace Provider contracts, distinct Node/Workspace/Activity/Object/Session identities and separate large-data streams.

## WP02A — Workspace and execution composition

Inspected OpenClaw, Daytona, Coder, E2B/Desktop, Dev Containers/CLI, DevPod, containerd/OCI and OpenHands.

Direction:

- Ptah owns the provider-neutral Workspace Provider contract.
- Native local-process and OCI providers are first owned implementations.
- Dev Containers is a compatibility format, not Ptah's universal schema.
- External workspace systems remain optional adapters/exit paths.

## WP02B — Activities, events, recovery and observability

Inspected Temporal, NATS/JetStream and OpenTelemetry.

Direction:

- Ptah owns the Activity contract and Activity Ledger.
- Temporal is the primary durable-orchestration backend candidate.
- NATS/JetStream is the primary live/replayable internal Event Fabric candidate.
- OpenTelemetry/OTLP is the telemetry standard and Collector pipeline candidate.
- PTY, Object, display and media bytes remain separate streams.

## WP02C — Internal core-runtime recovery

Inspected and saved Hunter AgentOps, Foreman, Sergeant, TechGuy Relay, Software Builder, CodeOps, MIBU and Hunter runtime/sync/outbox implementations.

Core-runtime requirements are closed for Phase 0B contract design, not build.

Key accepted additions:

- operation/attempt/nonce/Node epoch/producer identity are distinct;
- Activity state, Event, telemetry, Receipt, Artifact proof, review and authoritative result are distinct;
- stale/uncorrelated/unauthenticated/UNKNOWN evidence never passes;
- idempotency, outbox attempts, retry/dead states and stale-lease recovery are first-class;
- source/local synchronization is status-first and never silently overwrites divergence;
- optional Facility failure may degrade one capability without stopping unrelated safe work.

Saved ADRs through ADR-0004.

## WP03 — Build, Artifact and provenance composition

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- internal Software Builder;
- BuildKit;
- Dagger;
- ORAS;
- Witness;
- in-toto;
- Cosign, Rekor, Fulcio and sigstore-go;
- Syft.

Accepted direction:

1. Ptah owns Build Recipe, Build Activity Graph, Object/Artifact Graph and Provenance/Verification Graph contracts.
2. BuildKit is the primary low-level graph/cache/worker candidate for suitable OCI builds.
3. Dagger is the primary typed recipe/module donor and optional backend.
4. Software Builder contributes scanner/readiness/shared-environment and private release requirements, not the complete engine.
5. ORAS is an Artifact transport/referrer backend, not universal Object storage.
6. Syft inventories packages/files and emits SBOMs with explicit coverage limits.
7. Witness/in-toto provide attestor and planned supply-chain interoperability.
8. Sigstore provides digest signing, identity, trusted roots, offline bundles and transparency evidence.
9. Cache is derived reusable state, not independent reproduction.
10. Build, hash verification, SBOM, attestation, signature, review, reproduction and release acceptance remain separate levels.

Saved:

- `donors/BUILDKIT.md`
- `donors/DAGGER.md`
- `donors/ORAS.md`
- `donors/WITNESS.md`
- `donors/IN-TOTO.md`
- `donors/SIGSTORE-COSIGN-REKOR-FULCIO.md`
- `donors/SYFT.md`
- `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`
- `work-packages/PHASE-0A-WP03-BUILD-ARTIFACT-PROVENANCE.md`

Requirements moved to Phase 0B design closure:

- `EXEC-003`;
- Build-side `STORE-002` and `STORE-004` foundations;
- `PROV-001`;
- Build-related portions of `CORE-003`, `PLUGIN-001` and `OBS-001`.

This does not approve runtime dependencies or implementation.

---

# Active inspection unit

## WP04 — Storage, transfer, synchronization and backup composition

Inspect as one complementary group:

1. internal Download Manager/Lumi implementation;
2. aria2;
3. tus/tusd;
4. rclone;
5. Syncthing;
6. restic;
7. current Hunter R2/D1/local/Drive storage patterns;
8. local content-addressed storage and metadata-catalogue options;
9. optional future shared-filesystem donors only where they close an actual requirement.

Resolve:

- hot active Workspace bytes versus durable Objects/Artifacts;
- resumable upload and download protocols;
- segmented/multi-source download and partial-file recovery;
- cloud/Object-store and Node-to-Node transport;
- streaming hashes, deduplication and content-addressed identity;
- backup, retention, encryption and restore;
- online/local authority, Object revisions and explicit conflicts;
- direct sync versus archive/export;
- storage-location health and repair;
- Drive as export/recovery rather than live Build filesystem;
- whether future JuiceFS/SeaweedFS-like shared layers are needed or parked;
- backend replacement and offline behavior.

Required saved output:

- donor/internal records after each inspection;
- composite Storage/Transfer/Sync work-package record;
- Storage Classes / Object Transfer / Sync boundary ADR;
- Requirement Closure Matrix updates for `STORE-001` through `STORE-005`, `XFER-001` through `XFER-003`, `SYNC-001`, remaining `SESSION-001`, `OFFLINE-001` and Object-storage portions of `CORE-003`;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels
- ADR-0005 — Build Recipe, Artifact and Provenance Boundary

---

# No-build boundary

Allowed now:

- donor/internal-work recovery;
- source inspection, canonical pins and licence review;
- composite requirement closure;
- ADRs, schemas and proof planning after Phase 0A review.

Not allowed yet:

- copying donor code;
- declaring closure from one donor;
- beginning runtime or large UI implementation;
- selecting dependencies from README claims alone;
- replacing internal work without evidence;
- exposing private consumers publicly.

---

# Phase 0A completion gate

Every v1 requirement must have a composite closure path, internal overlap, canonical pins/licences, native gap, exit strategy and validation plan, or be explicitly parked/rejected with a replacement.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
