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

# Completed and saved core-runtime work

## WP01 — Node and Workspace boundary

Established separate Node Protocol and Workspace Provider contracts, distinct Node/Workspace/Activity/Object/Session identities and separate large-data streams.

## WP02A — Workspace and execution composition

Inspected and saved OpenClaw, Daytona, Coder, E2B/Desktop, Dev Containers/CLI, DevPod, containerd/OCI and OpenHands.

Direction:

- Ptah owns the provider-neutral Workspace Provider contract.
- Native local-process and OCI providers are first owned implementations.
- Dev Containers is a compatibility format, not Ptah's universal schema.
- External workspace systems remain optional adapters/exit paths.

## WP02B — Activities, events, recovery and observability

Inspected and saved Temporal, NATS/JetStream and OpenTelemetry.

Direction:

- Ptah owns the Activity contract and Activity Ledger.
- Temporal is the primary durable-orchestration backend candidate.
- NATS/JetStream is the primary live/replayable internal Event Fabric candidate.
- OpenTelemetry/OTLP is the telemetry standard and Collector pipeline candidate.
- PTY, Object, display and media bytes remain separate streams.

## WP02C — Internal core-runtime recovery

**Status:** FIRST-PASS COMPLETE; core runtime closed for Phase 0B contract design, not build.

Internal sources inspected and saved:

- Hunter AgentOps;
- Hunter Foreman;
- Sergeant;
- TechGuy Relay;
- THETECHGUY Software Builder;
- Hunter CodeOps;
- MIBU;
- Hunter source/local sync, background tasks, persistent Workflows, local file/process bridge and Events V3 D1 outbox.

Key internal improvements added to Ptah design:

1. Orchestrator, specialist executor, evidence producer and reviewer retain separate ownership.
2. Operation, attempt, nonce, Node epoch, producer identity/version and idempotency are distinct.
3. Result, Event, telemetry, Receipt, Object/Artifact proof, review verdict and authoritative external outcome are separate.
4. Command accepted, process/interface launched, runtime ready, operation armed, completed, output created, read-back verified, independently reviewed and authoritative result are separate proof levels.
5. Stale, uncorrelated, unauthenticated, incompatible or UNKNOWN evidence never becomes PASS.
6. D1 outbox patterns contribute unique idempotency, claim, attempt history, retry/dead states, partial delivery and stale-lock recovery.
7. Source/local synchronization is status-first, explicit and fast-forward-only; divergence is never silently overwritten.
8. Workspace-relative paths, dry-run/apply, before-mutation backups and secret-aware file boundaries are retained.
9. Shared toolchains/caches and heavy background-work requirements are retained, while the current Builder is not treated as a completed engine.
10. Optional Facility failure may degrade one capability without stopping unrelated safe work.

Saved:

- `internal/HUNTER-AGENTOPS.md`
- `internal/HUNTER-FOREMAN.md`
- `internal/SERGEANT.md`
- `internal/TECHGUY-RELAY.md`
- `internal/SOFTWARE-BUILDER.md`
- `internal/HUNTER-CODEOPS.md`
- `internal/MIBU.md`
- `internal/HUNTER-RUNTIME-SYNC.md`
- `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`
- `work-packages/PHASE-0A-WP02C-INTERNAL-CORE-RUNTIME-RECOVERY.md`

Core-runtime requirements now closed for Phase 0B contract design:

- `CORE-001`
- `CORE-002`
- `CORE-004`
- `CORE-005`
- `RELAY-001`
- `RELAY-002`
- `EXEC-001`
- `EXEC-002`
- core `SESSION-001`
- `OBS-001`
- `OFFLINE-001`

This is design closure only. No runtime dependency or implementation is approved until Phase 0B schemas/proofs and Phase 0C slice approval.

---

# Active inspection unit

## WP03 — Deterministic build, Artifact and provenance composition

Inspect as one complementary group:

1. BuildKit;
2. Dagger;
3. internal Software Builder comparison;
4. ORAS and OCI Artifact/referrer relationships;
5. Witness;
6. in-toto and its specifications;
7. Cosign, Rekor, Fulcio and Sigstore;
8. Syft/SBOM machinery where needed for build outputs.

Resolve:

- typed recipes versus low-level build graphs;
- local, CI and remote worker portability;
- caching and cache identity;
- secret inputs and exclusion from outputs/logs;
- exact source, environment, tool and image identity;
- Artifact/Object relationship and storage format;
- build receipts, SBOMs and attestations;
- signing and transparency records;
- reproduction versus ordinary build success;
- how private signing/provider adapters remain outside public Ptah;
- exit strategies if any build/provenance service changes.

Required saved output:

- donor records after each source-level inspection;
- internal Builder comparison against BuildKit/Dagger;
- composite Build/Artifact/Provenance work-package record;
- Build Recipe / Artifact / Attestation boundary ADR;
- Requirement Closure Matrix updates for `EXEC-003`, `STORE-002`, `STORE-004`, `PROV-001`, `PLUGIN-001` where relevant;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels

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
