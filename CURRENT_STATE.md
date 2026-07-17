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

Every requirement combines internal foundation, primary capability donor, completion donors, mature machinery, native Ptah contracts, an exit path and proof. One repository never closes a subsystem by itself.

Research and decisions are committed after every meaningful inspection unit.

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

Inspected Hunter AgentOps, Foreman, Sergeant, TechGuy Relay, Software Builder, CodeOps, MIBU and Hunter runtime/sync/outbox implementations.

Core-runtime requirements are closed for Phase 0B contract design, not build.

Key additions:

- operation, attempt, nonce, Node epoch and producer identity are distinct;
- Activity state, Event, telemetry, Receipt, Artifact proof, review and authoritative result are distinct;
- stale, uncorrelated, unauthenticated and UNKNOWN evidence never passes;
- idempotency, outbox attempts, retry/dead states and stale-lease recovery are first-class;
- source/local synchronization is status-first and never silently overwrites divergence;
- optional Facility failure may degrade one capability without stopping unrelated safe work.

## WP03 — Build, Artifact and provenance composition

Inspected Software Builder, BuildKit, Dagger, ORAS, Witness, in-toto, Sigstore/Cosign/Rekor/Fulcio and Syft.

Closed for Phase 0B design:

- Build Recipe and backend compilation;
- low-level BuildKit graph/cache/worker direction;
- Dagger typed recipe/module direction;
- Artifact/Object relationships and ORAS transport;
- SBOM, attestation, signature, trust and reproduction records;
- distinction among planning, build, hash verification, SBOM, attestation, signature, review, reproduction and release acceptance.

Saved ADR-0005 and WP03 record.

## WP04 — Storage, transfer, synchronization and backup composition

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- internal Lumi Download Manager;
- internal Hunter storage authority and safe-sync patterns;
- aria2;
- tus/tusd;
- rclone;
- Syncthing;
- restic;
- JuiceFS and SeaweedFS as later shared-filesystem candidates.

Accepted direction:

1. Hot Workspace bytes, immutable Objects, mutable revisions, Artifacts, caches, provider volumes/snapshots, partial landing data, sync replicas, backups and exports remain separate classes.
2. Local SSD/NVMe is the default active Workspace storage.
3. Initial Storage Fabric is local CAS + local SQLite/shared SQL + R2/S3-compatible Object storage.
4. Object identity is content-based and independent of provider path/tag/location.
5. Mutable data uses revisions; concurrent offline changes create preserved conflicts rather than silent last-write-wins.
6. Transfer completion and Object verification/finalization are separate.
7. aria2 is the primary segmented/multi-source download backend candidate.
8. tus/tusd is the primary resumable-upload candidate.
9. rclone is the primary cloud/provider transport candidate.
10. Syncthing is an optional direct Node-sync backend; Ptah retains revision/conflict authority.
11. restic is the primary encrypted backup/restore candidate.
12. Google Drive is export/recovery, not active Build/database/container storage.
13. JuiceFS and SeaweedFS are evaluated and parked until measured distributed shared-storage need.
14. Synchronization is not backup; cache is not truth; provider snapshots are not backups.

Saved:

- `internal/LUMI-DM.md`
- `internal/STORAGE-AUTHORITY.md`
- `donors/ARIA2.md`
- `donors/TUSD.md`
- `donors/RCLONE.md`
- `donors/SYNCTHING.md`
- `donors/RESTIC.md`
- `donors/FUTURE-SHARED-FILESYSTEMS.md`
- `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`
- `work-packages/PHASE-0A-WP04-STORAGE-TRANSFER-SYNC-BACKUP.md`

Closed for Phase 0B design:

- `STORE-001` through `STORE-005`;
- `XFER-001` through `XFER-003`;
- `SYNC-001`;
- remaining storage/sync portions of `SESSION-001` and `OFFLINE-001`;
- Object-location portions of `CORE-003`.

This does not approve runtime dependencies or implementation.

---

# Active inspection unit

## WP05 — Universal Object and decomposition composition

Inspect as one complementary group:

1. internal App Recover;
2. internal APK Extractor;
3. internal Creative Studio/media asset handling;
4. internal Document Generator/rendering;
5. libarchive;
6. Apache Tika;
7. Unstructured;
8. LIEF;
9. Binwalk;
10. JADX;
11. Apktool;
12. libvips;
13. FFmpeg/ffprobe;
14. source-code structure donors such as Tree-sitter only where needed.

Resolve:

- true-type detection and confidence;
- immutable originals versus child Objects and derivatives;
- recursive decomposition and extraction budgets;
- archive/package/document/media/executable/application domain packs;
- progressive levels from immediate registration to deep decomposition;
- safe mounting/opening and generated previews;
- source/renderer/tool/version identity;
- comparison and rebuild proof levels;
- child/parent/subject/derived-from relationships;
- handling of malformed, encrypted, unsupported or intentionally opaque content;
- streaming decomposition before complete materialization where safe;
- concurrency without blocking unrelated Activities;
- which internal product code remains private and which neutral adapters may be public.

Required saved output:

- donor/internal records after each inspection;
- Object/Domain Pack composition record;
- Object Graph / Decomposition / Derivative boundary ADR;
- Requirement Closure Matrix updates for `CORE-003`, `DECOMP-001`, `DECOMP-002`, `DOC-001`, `MEDIA-001`, `IMAGE-001`, `BIN-001`, `APP-001` and Domain Pack portions of `CORE-004`;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels
- ADR-0005 — Build Recipe, Artifact and Provenance Boundary
- ADR-0006 — Storage Classes, Object Transfer, Synchronization and Backup Boundary

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
