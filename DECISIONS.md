# Ptah Accepted Decisions

This file indexes decisions that must not be silently reversed. Full architectural detail lives in the referenced ADRs.

---

## D-001 — Ptah is independent

**Status:** ACCEPTED

Ptah Space is an independent open-source project. Private consumers integrate through neutral APIs, SDKs, CLI, MCP adapters, streams, files and Facility contracts.

## D-002 — Ptah is the world, not the thinker

**Status:** ACCEPTED

Ptah supplies Workspaces, tools, files, applications, storage, internet, execution, rendering, devices and Artifacts. The caller supplies intent, reasoning, priorities, restrictions and acceptance criteria.

## D-003 — Roadmap and implementation are separate

**Status:** ACCEPTED

- `ptah-roadmap-` is the private canonical plan, research, decisions, sequencing and recovery memory.
- `Ptah-space` is the public implementation repository.

## D-004 — Online first, local later, same contracts

**Status:** ACCEPTED

The future local mini-PC/OS deployment reuses the online system's Objects, Activities, Sessions, Facilities, storage identities and APIs rather than replacing them.

## D-005 — Workspace and Activity are different

**Status:** ACCEPTED

A Workspace persists while many independent Activities start, pause, fail, recover and complete inside it.

## D-006 — Object-first architecture

**Status:** ACCEPTED

Files are registered Objects with hashes, types, locations, provenance, relationships, derivatives and producing Activities. Originals remain preserved.

## D-007 — Domain Packs

**Status:** ACCEPTED

Domain Packs implement detect, inventory, decompose, preview, open/mount, transform, validate, compare, rebuild where supported and execute through appropriate runtimes.

## D-008 — Internet is normally available

**Status:** ACCEPTED

Ptah behaves like a capable operating environment. Restrictions come from the caller, Workspace, deployment or provider—not autonomous Ptah policy.

## D-009 — Storage is layered

**Status:** ACCEPTED

Fast local storage performs active work; Object storage retains durable bytes; Git owns source history; SQL owns metadata; Drive is export/recovery rather than active Build storage.

## D-010 — Integration first, not greenfield pride

**Status:** ACCEPTED

Every Facility begins with internal recovery, external donor inspection, mature upstream machinery and identification of the remaining native Ptah gap.

## D-011 — Polyglot operational chassis

**Status:** ACCEPTED

Rust is preferred where it improves long-running core reliability, but mature Go, Python, TypeScript, Java, C/C++, Kotlin, Swift, .NET and other tools remain behind stable adapters.

## D-012 — Evidence before completion

**Status:** ACCEPTED

Source presence is not capability proof. Phases require frozen checkpoints, live evidence, Artifacts, hashes, limitations and retained negative results.

## D-013 — No work before placement and approval

**Status:** ACCEPTED

Ideas are preserved but not automatically activated. Implementation requires placement, dependency ordering, `CURRENT_STATE.md` selection and explicit approval.

## D-014 — Build cycle

**Status:** ACCEPTED

Understand → Build → Review → Freeze → Prove → Submit/Ship.

## D-015 — Public Ptah remains neutral

**Status:** ACCEPTED

Public source must not expose private consumers, operation chains, credentials, deployment topology, customer data or unpublished company decisions.

## D-016 — Operating-system assembly is a later private lane

**Status:** ACCEPTED

Ptah stays OS-neutral. The future operating-system distribution is decided after online and Node services are proven.

## D-017 — Composite donor closure

**Status:** ACCEPTED

No subsystem closes through one repository. Closure combines internal foundation, primary donor, completion donors, mature machinery, native Ptah layer, exit strategy and proof.

Full decision: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

## D-018 — Activity, Event and observability guarantees remain separate

**Status:** ACCEPTED

Ptah owns the Activity Ledger. Temporal is the durable-orchestration candidate; NATS/JetStream is the live/replayable Event candidate; OpenTelemetry is telemetry; large streams and proof receipts remain separate.

Full decision: `decisions/ADR-0003-ACTIVITY-EVENT-OBSERVABILITY-BOUNDARY.md`.

## D-019 — Operation state, evidence and authority levels remain separate

**Status:** ACCEPTED

Activity state, operation/attempt identity, Events, telemetry, Receipts, Artifact proof, reviewer verdict and authoritative external result are distinct. Stale, uncorrelated, unauthenticated or UNKNOWN evidence never becomes PASS.

Full decision: `decisions/ADR-0004-OPERATION-RECEIPTS-PROOF-LEVELS.md`.

## D-020 — Build, Artifact and provenance guarantees remain separate

**Status:** ACCEPTED

Build Recipe, execution graph, Object/Artifact graph and provenance/verification graph are separate. BuildKit, Dagger, ORAS, Syft, Witness/in-toto and Sigstore remain replaceable machinery.

Full decision: `decisions/ADR-0005-BUILD-ARTIFACT-PROVENANCE-BOUNDARY.md`.

## D-021 — Storage, transfer, synchronization and backup guarantees remain separate

**Status:** ACCEPTED

Hot Workspace bytes, immutable Objects, mutable revisions, cache, transfer landing, replicas, backups and exports have different guarantees. aria2, tusd, rclone, Syncthing and restic remain backend adapters. Drive is export/recovery.

Full decision: `decisions/ADR-0006-STORAGE-TRANSFER-SYNC-BOUNDARY.md`.

## D-022 — Object identity, detector claims, Views and rebuilds remain separate

**Status:** ACCEPTED

Original bytes remain immutable; multiple detector claims and disagreements are retained; progressive decomposition is bounded; children, Views, previews, transformations, decompilations and rebuilds receive explicit origin and relationships.

Full decision: `decisions/ADR-0007-OBJECT-GRAPH-DECOMPOSITION-DERIVATIVE-BOUNDARY.md`.

## D-023 — Firmware packages, disk images and physical operations remain separate

**Status:** ACCEPTED

Static package/image analysis is separate from connected-device mutation. Device presence, protocol handshake, loader/programmer stage, configured service, write acknowledgement and read-back are distinct proof levels. Mutation requires exact compatibility, immutable backup and explicit authorization.

Full decision: `decisions/ADR-0008-DISK-FIRMWARE-DEVICE-OPERATION-BOUNDARY.md`.

## D-024 — Device identity, lease, display, input and semantic UI remain separate

**Status:** ACCEPTED

Ptah owns stable Device identity, interface connection epochs, Provider worker generation, scoped lease/fencing, Device Session and Application Session.

- ADB/Fastboot/USB paths, serials, Appium sessions, scrcpy processes and accessibility elements are backend aliases.
- inventory, shell, files, packages, logs, display, audio, input, clipboard, semantic UI, policy/admin and firmware are independently authorized capabilities;
- scrcpy is the primary modern Android video/audio/control candidate;
- AndroidX UI Automator is the official semantic foundation;
- Appium/UIAutomator2 and TouchPilot are complementary adapters;
- stale interface/context results are rejected;
- input acknowledgement, application launch and stream start do not prove intended state;
- cleanup is a verified Activity and failure quarantines the Device.

Full decision: `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`.

## D-025 — Application Provider, Window, display gateway and semantic context remain separate

**Status:** ACCEPTED

Ptah owns Application Object, Provider, Installation, Session, Process, Window, Display Gateway, Semantic Context and checkpoint identities.

- Xpra is the primary individual Linux application/window display candidate;
- Guacamole is the primary cross-protocol browser remote-desktop gateway;
- noVNC/websockify is the lightweight VNC fallback;
- QEMU/libvirt is the primary Windows VM Provider candidate;
- FreeRDP supplies RDP protocol machinery;
- FlaUI is the primary direct Windows semantic donor and NovaWindows the modern W3C candidate; WinAppDriver remains legacy compatibility;
- Peekaboo is the primary macOS visual/accessibility candidate without its agent identity;
- Appium XCUITest and IDB supply Apple semantic/device-lab adapters;
- Apple Xcode, Simulator, XCTest and Virtualization remain proprietary platform foundations;
- package install, process launch, first window, first frame, semantic readiness and expected state are distinct proof levels;
- display reconnect is not application recovery;
- display, input, clipboard, files, audio, printing, device redirection and recording are independently scoped.

Full decision: `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`.
