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

Ptah owns the provider-neutral Workspace Provider contract. Native local-process and OCI providers are first owned implementations. Dev Containers is a compatibility format, while external workspace systems remain optional adapters/exit paths.

## WP02B — Activities, events, recovery and observability

Inspected Temporal, NATS/JetStream and OpenTelemetry.

Ptah owns the Activity Ledger; Temporal is the durable-orchestration candidate; NATS/JetStream is the live/replayable Event Fabric candidate; OpenTelemetry/OTLP is the telemetry standard; large PTY/Object/display/media data uses separate streams.

## WP02C — Internal core-runtime recovery

Inspected Hunter AgentOps, Foreman, Sergeant, TechGuy Relay, Software Builder, CodeOps, MIBU and Hunter runtime/sync/outbox implementations.

Core-runtime requirements are closed for Phase 0B contract design, not build.

Key additions include separate operation/attempt/nonce/Node epoch/producer identities, separate Activity/Event/telemetry/Receipt/proof/review/authoritative-result states, stale-proof rejection, idempotent outbox attempts and safe status-first synchronization.

## WP03 — Build, Artifact and provenance composition

Inspected Software Builder, BuildKit, Dagger, ORAS, Witness, in-toto, Sigstore/Cosign/Rekor/Fulcio and Syft.

Closed for Phase 0B design: Build Recipes, backend compilation, low-level graph/cache/worker direction, typed modules, Artifact relationships, SBOMs, attestations, signatures, trust and reproduction levels.

Saved ADR-0005 and WP03 record.

## WP04 — Storage, transfer, synchronization and backup composition

Inspected internal Lumi/Hunter storage work plus aria2, tus/tusd, rclone, Syncthing, restic, JuiceFS and SeaweedFS.

Closed for Phase 0B design:

- hot local Workspace storage classes;
- local CAS + SQLite/shared SQL + R2/S3 direction;
- immutable Object/location identity;
- mutable revision/conflict model;
- resumable uploads and downloads;
- cloud and Node transport;
- encrypted backup/restore;
- Drive export/recovery;
- explicit parking of distributed shared filesystems until measured Phase 12 need.

Saved ADR-0006 and WP04 record.

## WP05 — Universal Object and decomposition composition

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

### Internal

- App Recover;
- APK Extractor;
- TTG Creative Studio;
- TTG Document Generator Templates.

### External/upstream

- libarchive;
- Apache Tika;
- Unstructured;
- LIEF;
- Binwalk v3;
- JADX;
- Apktool;
- libvips;
- FFmpeg/ffprobe;
- Tree-sitter.

Accepted direction:

1. Immutable original Object bytes and identity remain preserved.
2. Filename, extension, MIME, parser output and caller labels are claims/attributes rather than identity.
3. Multiple detector claims and conflicts remain retained; route selection is separate.
4. Unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque are valid states.
5. Decomposition is progressive: registration, detection, inventory, decomposition, enrichment, transform, rebuild and verification.
6. Child Objects, semantic elements, Views, previews, transforms, rebuild projects and rebuilt outputs have distinct relationships.
7. Decompiled/generated source declares its origin and never masquerades as original source.
8. Recursive extraction inherits hard depth, bytes, child-count, expansion, time, memory and disk budgets.
9. Native parsers run in bounded providers, not the control plane.
10. Partial valid children survive timeout, crash, cancellation or budget exhaustion.
11. Competing parser/OCR/decompiler views remain separately addressable.
12. Rebuilt outputs receive new Object identity and explicit signature/trust consequences.
13. Internal products remain specialist callers/products over neutral Ptah Domain Packs.

Saved:

- `internal/APP-RECOVER.md`
- `internal/APK-EXTRACTOR.md`
- `internal/CREATIVE-STUDIO.md`
- `internal/DOCUMENT-GENERATOR.md`
- `donors/LIBARCHIVE.md`
- `donors/APACHE-TIKA.md`
- `donors/UNSTRUCTURED.md`
- `donors/LIEF.md`
- `donors/BINWALK.md`
- `donors/JADX.md`
- `donors/APKTOOL.md`
- `donors/LIBVIPS.md`
- `donors/FFMPEG-FFPROBE.md`
- `donors/TREE-SITTER.md`
- `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`
- `work-packages/PHASE-0A-WP05-UNIVERSAL-OBJECT-DECOMPOSITION.md`

Closed for Phase 0B design:

- `CORE-003`;
- Domain Pack portions of `CORE-004`;
- `DECOMP-001` and `DECOMP-002`;
- `DOC-001`;
- `MEDIA-001`;
- `IMAGE-001`;
- `BIN-001`;
- `APP-001`;
- source-structure portions of search/editor requirements.

This does not approve runtime dependencies or implementation.

---

# Active inspection unit

## WP06 — Firmware, disks and filesystems composition

Inspect as one complementary group:

1. internal Apple firmware/tool work;
2. blacktop/ipsw and Apple metadata sources;
3. internal MediaTek/META engines and MTKClient;
4. internal Qualcomm/DIAG/Firehose engines and EDL donors;
5. internal Unisoc/SPD/PAC/FDL engines and donors;
6. internal Android OTA Manager;
7. Android payload, sparse-image and dynamic-partition tooling;
8. GPT/MBR and filesystem parsers;
9. libguestfs and related mounting/extraction machinery;
10. Binwalk/LIEF/libarchive reuse from WP05;
11. other vendor/embedded firmware coverage;
12. P5C format recovery from a verified sample/tool, or explicit unresolved/parked status.

Resolve:

- disk/image/partition/filesystem Object relationships;
- firmware package, manifest, partition image, region, file and metadata relationships;
- static decomposition versus mounted/opened views;
- read-only safe defaults and isolated mount helpers;
- sparse/compressed/encrypted image handling;
- payload/dynamic-partition reconstruction;
- vendor download/restore metadata and cryptographic verification;
- comparison and rebuild levels;
- exact device profile/SoC/platform compatibility claims;
- backup/read-before-write and operation receipts;
- strict separation between firmware analysis and destructive device flashing;
- unsupported/proprietary format and missing-key states;
- private product/engine code versus neutral public Domain Pack adapters.

Required saved output:

- internal/donor records after each inspection unit;
- Firmware/Disk/Filesystem composition record;
- Disk Image / Firmware Package / Device Operation boundary ADR;
- Requirement Closure Matrix updates for `FW-001` through `FW-006`, `FS-001`, firmware portions of `CORE-003`/`CORE-004`, `DEVICE-001` boundaries and `SESSION-001` snapshot/image relationships;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels
- ADR-0005 — Build Recipe, Artifact and Provenance Boundary
- ADR-0006 — Storage Classes, Object Transfer, Synchronization and Backup Boundary
- ADR-0007 — Object Graph, Decomposition, Views and Derivatives Boundary

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
