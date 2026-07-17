# Ptah Accepted Decisions

This file records decisions that must not be silently reversed during implementation.

---

## D-001 — Ptah is independent

**Status:** ACCEPTED

Ptah Space is an independent open-source project. It is not publicly owned by or branded around any private system that uses it.

Private consumers may integrate through neutral APIs, SDKs, CLI, MCP adapters, event streams, files, and facility contracts.

---

## D-002 — Ptah is the world, not the thinker

**Status:** ACCEPTED

Ptah provides workspaces, tools, files, applications, storage, internet, execution, rendering, devices, and artifacts.

The user or calling system provides intent, reasoning, priorities, instructions, restrictions, and acceptance criteria.

Ptah does not contain a universal reasoning council, engineering authority, or product-approval system.

---

## D-003 — Roadmap and implementation are separate

**Status:** ACCEPTED

- `ptah-roadmap-` is the private canonical plan, progress ledger, donor register, decisions, and recovery memory.
- `Ptah-space` is the public implementation repository.

The public repository contains what is being built and public-safe earned progress. It must not contain the full private roadmap or private integration relationships.

---

## D-004 — Online first, local later, same contracts

**Status:** ACCEPTED

Ptah begins as an online workspace before the permanent mini-PC environment exists.

The future local node and larger operating environment must reuse the same objects, activities, sessions, facility contracts, storage identities, and APIs rather than replacing the online system.

---

## D-005 — Workspace and activity are different

**Status:** ACCEPTED

A workspace is persistent. Activities start, stop, fail, pause, recover, and complete inside it.

One workspace must support many simultaneous terminals, downloads, builds, browsers, media jobs, decomposition jobs, applications, and services.

---

## D-006 — Object-first architecture

**Status:** ACCEPTED

Files are registered objects with hashes, types, metadata, storage locations, provenance, parent/child relationships, derivatives, views, and producing activities.

Original objects remain preserved unless explicitly replaced.

---

## D-007 — Domain packs

**Status:** ACCEPTED

Decomposition and runtime support are extended through domain packs with a shared contract:

- detect;
- inventory;
- decompose;
- preview;
- open/mount;
- transform;
- validate;
- compare;
- rebuild where supported;
- execute through an appropriate runtime.

Firmware and disks/filesystems are first-class domain packs.

---

## D-008 — Internet is normally available

**Status:** ACCEPTED

Ptah behaves like a capable operating environment: Git, package registries, websites, APIs, downloads, browser sessions, and remote services work normally.

Restrictions originate from the user, caller, explicit workspace configuration, or hosting environment. Ptah does not autonomously decide what the programmer may access.

---

## D-009 — Storage is layered

**Status:** ACCEPTED

- Fast local storage performs active work.
- Object storage retains durable remotely available bytes.
- Git owns source history.
- SQL/metadata stores catalogue objects, activities, sessions, nodes, and artifacts.
- Google Drive is an export and readable recovery destination, not an active build filesystem.

---

## D-010 — Integration first, not greenfield pride

**Status:** ACCEPTED

Every facility begins with recovery of:

1. existing internal work;
2. external donor projects;
3. mature upstream machinery;
4. the remaining native Ptah gap.

Repositories are classified as adopt, adapt, wrap, fork, protocol-compatible, study-only, hosted workload, reject, or further inspection.

No donor is selected from README claims alone.

---

## D-011 — Polyglot operational chassis

**Status:** ACCEPTED

Rust is preferred for long-running Ptah core and node services where it improves performance, reliability, and portability.

Mature tools may remain in Go, Python, TypeScript, Java, C/C++, Kotlin, or other appropriate languages behind stable adapters.

---

## D-012 — Evidence before completion

**Status:** ACCEPTED

Source presence is not proof of capability.

Each phase has explicit gates, frozen checkpoints, live proof, artifacts, logs, hashes, and known limitations.

Negative, blocked, and partial outcomes remain recorded as evidence.

---

## D-013 — No work before placement and approval

**Status:** ACCEPTED

A useful idea is preserved, but it is not automatically active work.

Before implementation it must be placed, assigned to a phase, checked against existing work, dependency-ordered, selected in `CURRENT_STATE.md`, and approved for build.

---

## D-014 — Build cycle

**Status:** ACCEPTED

Every work item follows:

1. Understand
2. Build
3. Review
4. Freeze
5. Prove
6. Submit / Ship

Runtime experiments may confirm a design but must not replace understanding and architecture recovery.

---

## D-015 — Ptah public repo remains neutral

**Status:** ACCEPTED

Public documentation may describe humans, applications, agents, automation clients, IDEs, generic external systems, and execution nodes.

It must not expose private operation chains, private consumers, credentials, private deployment topology, customer data, or unpublished company decisions.

---

## D-016 — Operating-system assembly is a later private lane

**Status:** ACCEPTED

Ptah remains OS-neutral and independently useful.

A future local operating environment may package Ptah, but the distribution, boot, drivers, updates, hardware profiles, and private integrations are decided separately after the online and node services are proven.

---

## D-017 — Composite donor closure

**Status:** ACCEPTED

No Ptah subsystem is completed by choosing one repository.

Every requirement must be closed through internal foundation, primary capability donor, completion donors, mature machinery, native Ptah layer, fallback/exit and proof.

Research, decisions, unresolved gaps and progress are saved continuously.

Full decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

## D-018 — Activity, event and observability guarantees remain separate

**Status:** ACCEPTED

Ptah owns a neutral Activity contract and Activity Ledger.

- Temporal is the primary durable-orchestration backend candidate.
- NATS is the primary low-latency internal Event Fabric candidate.
- JetStream is the primary bounded replayable-event candidate.
- OpenTelemetry is the telemetry specification and Collector pipeline candidate.
- Dedicated transports carry PTY, Object/file, display and media streams.
- Ptah-owned receipts provide durable proof of side effects and produced Artifacts.

No workflow engine, message broker, telemetry backend or stream is universal Ptah truth.

Side effects require stable operation IDs, idempotency keys, explicit retry classes and durable receipts. Disconnected Nodes keep a Ptah-owned local journal/outbox and reconcile by identity and sequence.

Full decision: `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`.

---

## D-019 — Operation state, evidence and authority levels remain separate

**Status:** ACCEPTED

Ptah distinguishes Activity state, operation identity, events, telemetry, durable receipts, Object/Artifact proof, reviewer verdicts and authoritative external results.

Every asynchronous or side-effecting operation is correlated through stable Activity/operation/attempt identities, idempotency where applicable, nonce, Node connection epoch, producer identity and version.

Command acceptance, process or interface launch, runtime readiness, operation completion, output creation, read-back verification, independent review and authoritative external result are separate proof levels. A weaker level is never promoted automatically into a stronger one.

Receipts are append-only and reference large evidence through Objects/Artifacts. Reviews are bound to exact checkpoints/content hashes. Stale, uncorrelated, unauthenticated, UNKNOWN or incompatible evidence never becomes PASS.

Full decision: `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`.

---

## D-020 — Build, Artifact and provenance guarantees remain separate

**Status:** ACCEPTED

Ptah owns separate but linked Build Recipe, Build Activity Graph, Object/Artifact Graph and Provenance/Verification Graph contracts.

- BuildKit is the primary low-level graph/cache/worker candidate for suitable OCI builds.
- Dagger is the primary typed recipe/module donor and optional execution backend.
- The internal Software Builder contributes source detection, readiness, target planning, shared-machinery and private release requirements, not the complete engine.
- ORAS/OCI is an Artifact transport and relationship backend.
- Syft is the primary SBOM/package-inventory candidate.
- Witness and in-toto provide attestor, materials/products and supply-chain verification compatibility.
- Cosign/Sigstore/Fulcio/Rekor provide digest signing, signer identity, trust roots, offline bundles and transparency evidence.

Cache is reusable derived state, not source truth or independent reproduction. Mutable tags do not define Artifact identity. Secrets remain opaque references and must not enter logs, caches, SBOMs, attestations or public recipes.

Build planning, execution, Artifact hash verification, SBOM generation, attestation, signature verification, review, independent reproduction and release acceptance are distinct levels. A stronger level is never inferred automatically.

Full decision: `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`.

---

## D-021 — Storage, transfer, synchronization and backup guarantees remain separate

**Status:** ACCEPTED

Ptah owns a backend-neutral Storage Fabric with explicit classes for hot Workspace bytes, immutable Objects, mutable revisions, Artifacts, caches, provider volumes/snapshots, partial landing data, sync replicas, encrypted backups and exports.

- local SSD/NVMe is the default active Workspace storage;
- local content-addressed storage plus SQLite/shared SQL and R2/S3-compatible Object storage is the initial storage direction;
- aria2 is the primary segmented/multi-source download backend candidate;
- tus/tusd is the primary resumable-upload candidate;
- rclone is the primary broad cloud/provider transport adapter;
- Syncthing is an optional direct Node-sync backend and version-vector donor;
- restic is the primary encrypted backup/restore candidate;
- Google Drive remains export/recovery, not a live Build/database/container filesystem;
- JuiceFS and SeaweedFS are evaluated and parked until measured distributed shared-storage need.

Transfer completion and Object verification are separate. Synchronization transports revisions but does not decide conflict authority. Concurrent mutable changes produce preserved divergent revisions rather than silent last-write-wins. Synchronization is not backup, provider snapshots are not backups, caches are not truth and cloud mounts are not local active storage.

Object identity is content-based and independent of provider path, tag or storage location. Backups and destructive retention/prune operations require explicit recipes and receipts.

Full decision: `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`.

---

## D-022 — Object identity, detector claims, decomposition views and rebuilds remain separate

**Status:** ACCEPTED

Ptah owns an immutable Object Graph and versioned Domain Pack contract.

- original Object bytes and identity remain preserved;
- filename, extension, MIME, parser output and caller labels are claims or attributes rather than identity;
- multiple detector claims and conflicts remain retained while route selection is a separate decision;
- unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque are valid states;
- decomposition progresses through registration, detection, inventory, child extraction, enrichment, transform, rebuild and verification;
- child Objects, semantic elements, views, previews, transformed derivatives, rebuild projects and rebuilt outputs have distinct relationships;
- source-like results declare original, embedded, decoded, disassembled, smali, decompiled, generated-skeleton or human-edited origin;
- recursive decomposition inherits hard resource and extraction-safety budgets;
- native parsers run in bounded providers rather than the control plane;
- partial valid children remain after timeout, crash, cancellation or budget exhaustion;
- competing parser/decompiler/OCR views remain separately addressable;
- rebuilt output receives a new Object identity and explicit signature/trust consequences.

libarchive, Tika, Unstructured, LIEF, Binwalk, JADX, Apktool, libvips, FFmpeg/ffprobe and Tree-sitter are selected as replaceable Domain Pack machinery. Internal App Recover, APK Extractor, Creative Studio and Document Generator remain specialist products and requirement donors over neutral Ptah contracts.

Parser success, extracted text, decoded resources, decompiled source, previews, rebuilt outputs and reviews never become universal Object truth automatically.

Full decision: `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`.
