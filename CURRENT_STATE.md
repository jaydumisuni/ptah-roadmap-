# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Sessions and Artifacts.

Ptah supplies the working world; humans and compatible systems supply intent, reasoning, restrictions and acceptance criteria.

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

One repository never closes a subsystem. Research and decisions are committed after every meaningful inspection unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

# Completed and saved Phase 0A work packages

## WP01 — Node and Workspace boundary

- Node Protocol and Workspace Provider are separate.
- Node, Workspace, Activity, Object and Session identities are separate.
- Large streams remain outside ordinary control messages.

## WP02A–WP02C — Core runtime

Closed for Phase 0B design:

- provider-neutral Workspaces;
- durable concurrent Activities;
- live/replayable Events;
- Node Protocol and Facility manifests;
- terminal/process and OCI-provider foundations;
- observability;
- local journal/reconnect;
- operation IDs, attempts, nonces, receipts, proof levels and stale-result rejection.

Primary machinery: OpenClaw, Daytona, Coder, E2B, Dev Containers, DevPod, containerd/OCI, OpenHands, Temporal, NATS/JetStream and OpenTelemetry, completed by internal AgentOps/Foreman/Sergeant/Relay/CodeOps/MIBU/Hunter evidence.

## WP03 — Build, Artifact and provenance

Closed for Phase 0B design:

- Build Recipe and backend compilation;
- BuildKit low-level graph/cache/worker direction;
- Dagger typed recipe/module direction;
- Artifact relationships and ORAS transport;
- SBOM, attestation, signature, trust, review and independent-reproduction levels.

## WP04 — Storage, transfer, synchronization and backup

Closed for Phase 0B design:

- hot local Workspace storage;
- local CAS + SQLite/shared SQL + R2/S3 direction;
- immutable Objects and mutable revisions/conflicts;
- resumable upload/download;
- cloud and Node transport;
- encrypted backup/restore;
- Drive export/recovery;
- distributed shared filesystems parked until measured need.

Primary machinery: Lumi, aria2, tusd, rclone, Syncthing and restic.

## WP05 — Universal Object and decomposition

Closed for Phase 0B design:

- immutable Object graph;
- plural detector claims;
- progressive bounded decomposition;
- child, View, preview, transform, decompilation and rebuild relationships;
- document, archive, image, media, binary, Android application and source-structure Domain Packs.

## WP06 — Firmware, disks and filesystems

Closed for Phase 0B design:

- Apple IPSW/BuildManifest package analysis;
- MediaTek META/BROM/Preloader/DA separation;
- Qualcomm Sahara/Firehose composition;
- Unisoc PAC/FDL composition;
- Android OTA payload/sparse/dynamic-partition/AVB handling;
- Samsung/generic other-vendor routing;
- GPT/MBR, disk and isolated filesystem inspection;
- static analysis versus physical mutation boundary;
- exact compatibility, loader/programmer identity, backup and read-back requirements;
- `.P5C` parked pending verified sample/spec/tool.

## WP07A — Android Device Runtime

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- internal THETECHGUY Device Manager and MIBU;
- DeviceFarmer STF and adbkit;
- minicap and minitouch;
- scrcpy;
- Appium and UIAutomator2;
- TouchPilot;
- official Android ADB/Fastboot sources;
- AndroidX UI Automator.

Accepted direction:

1. stable Device identity is separate from USB path, ADB serial, endpoint, worker and automation session;
2. every interface has a connection epoch;
3. Device Provider, worker generation, lease/fencing and Device Session are separate;
4. inventory, shell, files, packages, logs, display, audio, input, clipboard, semantic UI, policy/admin and firmware are separately authorized;
5. scrcpy is the primary modern Android display/audio/control candidate;
6. minicap/minitouch remain legacy compatibility paths;
7. AndroidX UI Automator is the official semantic foundation;
8. Appium/UIAutomator2 and TouchPilot are complementary adapters;
9. semantic hierarchy and pixels/raw input are complementary evidence;
10. input acknowledgement, launch and stream start are not verified outcome;
11. sensitive device evidence has explicit privacy/retention;
12. cleanup is a verified Activity and failure quarantines the Device.

Saved:

- `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`
- `work-packages/PHASE-0A-WP07A-ANDROID-DEVICE-RUNTIME.md`

## WP07B — Desktop and Apple Application Runtime

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- Xpra/Xpra HTML5;
- Apache Guacamole;
- noVNC/websockify;
- QEMU/libvirt;
- FreeRDP;
- FlaUI;
- NovaWindows and legacy Appium Windows/WinAppDriver;
- Peekaboo;
- Appium XCUITest;
- IDB;
- official Apple Xcode, Simulator/Device Hub, XCTest and Virtualization foundations.

Accepted direction:

1. Application Object, Provider, Installation, Session, Process, Window, Display Gateway and Semantic Context are separate;
2. Xpra is the primary individual Linux application/window display candidate;
3. Guacamole is the primary cross-protocol browser remote-desktop gateway;
4. noVNC/websockify is the lightweight VNC fallback;
5. QEMU/libvirt is the primary Windows VM Provider candidate;
6. native Windows Node remains separate from a VM provider;
7. FreeRDP supplies RDP protocol machinery;
8. FlaUI is the primary direct Windows semantic donor;
9. NovaWindows is the primary modern W3C candidate, while WinAppDriver is legacy compatibility only;
10. Peekaboo is the primary macOS visual/accessibility candidate without its agent identity;
11. Appium XCUITest and IDB supply Apple semantic/device-lab adapters;
12. Apple Xcode/Simulator/XCTest/Virtualization remain proprietary platform foundations;
13. package install, process launch, first window, first frame, semantic readiness and expected state are distinct proof levels;
14. display reconnect is not application recovery;
15. display, input, clipboard, files, audio, printing, device redirection and recording are separately scoped;
16. provider snapshots declare exact checkpoint class and limitations.

Saved:

- `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`
- `work-packages/PHASE-0A-WP07B-DESKTOP-APPLE-APPLICATION-RUNTIME.md`

### WP07 closure

Closed for Phase 0B design:

- `DEVICE-001` and `DEVICE-002`;
- `APP-002`, `APP-003` and `APP-004`;
- Device/Application Session extensions;
- application/display portions of `UI-001`, `UI-002`, `SESSION-001`, `OBS-001`, `PROV-001`, `DIST-001` and `OFFLINE-001`.

Known retained gap: Linux semantic automation still requires an AT-SPI-specific completion pass before claiming parity with Android, Windows and macOS semantics.

---

# Active inspection unit

## WP08 — Browser and Live Research Composition

Inspect as one complementary group:

1. Playwright core and relevant language bindings;
2. Playwright MCP;
3. Browser-Use;
4. TurboWebFetch canonical repository and implementation;
5. internal website/browser/download/research bridges where discoverable;
6. Chromium persistent profiles and browser-process pools;
7. authenticated contexts, cookies, local/session storage and extensions;
8. downloads, screenshots, video, trace, console and network evidence;
9. rendered extraction, source citation and live-search contracts;
10. browser crash/restart, reconnect and stale-page rejection;
11. concurrency across unrelated browser Activities;
12. live-search caller/council-member boundary without embedding reasoning into Ptah.

Resolve:

- Browser Profile versus Browser Process versus Context versus Page/Tab identity;
- persistent authenticated profiles and safe profile sharing;
- interactive browsing versus rendered batch retrieval;
- Playwright/CDP/browser-native capability boundaries;
- browser pools and process reuse without cross-Workspace data leakage;
- downloads landing as Objects through the Transfer Facility;
- screenshots/video/traces/network/console as separate Artifacts;
- DOM/accessibility/pixels/source-response as competing Views;
- citation/provenance of live research results;
- challenge, authentication and human-completion states;
- browser and page recovery after process or Node failure;
- privacy, credential and session-cookie treatment;
- external MCP/tool exposure versus native Ptah Browser contracts.

Required saved output:

- donor/internal records after each inspection unit;
- Browser/Live Research composition record;
- Browser Profile / Context / Page / Evidence boundary ADR;
- Requirement Closure Matrix updates for `BROWSE-001`, `BROWSE-002`, `BROWSE-003`, browser portions of `SESSION-001`, `UI-001`, `UI-002`, `XFER-002`, `OBS-001` and `PROV-001`;
- `PROGRESS.md` and this file updated continuously.

---

# Accepted decisions

- ADR-0001 — Node Protocol and Workspace Provider Boundary
- ADR-0002 — Composite Donor Closure Method
- ADR-0003 — Activity, Event and Observability Boundary
- ADR-0004 — Operation Identity, Receipts and Proof Levels
- ADR-0005 — Build Recipe, Artifact and Provenance Boundary
- ADR-0006 — Storage, Transfer, Synchronization and Backup Boundary
- ADR-0007 — Object Graph, Decomposition, Views and Derivatives Boundary
- ADR-0008 — Disk Images, Firmware Packages and Physical Operations Boundary
- ADR-0009 — Device Session, Display, Input and Semantic UI Boundary
- ADR-0010 — Application Provider, Window and Display Boundary

---

# No-build boundary

Allowed now:

- donor/internal recovery;
- source inspection, pins and licence review;
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

Every v1 requirement must have internal overlap, composite donors, canonical pins/licences, native gap, exit strategy and proof plan, or be explicitly parked/rejected with a replacement.

---

# Chat continuation instruction

Read this file first, followed by `MASTER_ROADMAP.md`, `PROGRESS.md`, `DECISIONS.md`, `MEMORY_PROTOCOL.md`, `DONOR_RECOVERY.md`, `REQUIREMENT_CLOSURE_MATRIX.md`, relevant donor/internal records, work packages and ADRs before proposing or performing further work.
