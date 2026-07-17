# Ptah Current State

**Last updated:** 2026-07-17  
**Overall status:** ACTIVE PLANNING  
**Current phase:** Phase 0A — Internal and external donor recovery  
**Runtime implementation:** NOT STARTED  
**Public implementation repository:** `jaydumisuni/Ptah-space`

---

# Recovered position

Ptah is an independent, open-source, online-first concurrent digital world built around persistent Workspaces, Objects, Activities, Facilities, Nodes, Devices, Applications, Browsers, Sessions and Artifacts.

Ptah supplies the working world. Humans and compatible systems supply intent, reasoning, restrictions and acceptance criteria.

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

One repository never closes a subsystem. Research, corrections and decisions are committed after every meaningful inspection unit.

Canonical method: `decisions/ADR-0002-COMPOSITE-DONOR-CLOSURE.md`.

---

# Completed Phase 0A work packages

## WP01 — Node and Workspace boundary

Closed:

- Node Protocol versus Workspace Provider;
- separate Node, Workspace, Activity, Object and Session identities;
- large-stream separation.

## WP02A–WP02C — Core runtime

Closed for Phase 0B design:

- provider-neutral Workspaces;
- durable concurrent Activities;
- live/replayable Events;
- Node Protocol and Facility manifests;
- terminal/process and OCI-provider foundations;
- observability and local reconnect journal;
- operation/attempt/nonce/receipt/proof-level boundaries.

Primary external machinery: OpenClaw, Daytona, Coder, E2B, Dev Containers, DevPod, containerd/OCI, OpenHands, Temporal, NATS/JetStream and OpenTelemetry.

Internal completion evidence: AgentOps, Foreman, Sergeant, Relay, CodeOps, MIBU and Hunter runtime/outbox/sync.

## WP03 — Build, Artifact and provenance

Closed for Phase 0B design:

- Build Recipe and backend compilation;
- BuildKit low-level graph/cache/worker direction;
- Dagger typed recipes/modules;
- ORAS Artifact relationships;
- Syft SBOMs;
- Witness/in-toto attestations;
- Sigstore signing/trust;
- independent reproduction and acceptance levels.

## WP04 — Storage, transfer, synchronization and backup

Closed for Phase 0B design:

- hot local Workspace storage;
- local CAS + SQLite/shared SQL + R2/S3 direction;
- immutable Objects and mutable revisions/conflicts;
- resumable upload/download;
- cloud and Node transfer;
- encrypted backup/restore;
- Drive export/recovery;
- JuiceFS/SeaweedFS parked until measured distributed need.

Primary machinery: Lumi, aria2, tusd, rclone, Syncthing and restic.

## WP05 — Universal Object and decomposition

Closed for Phase 0B design:

- immutable Object graph and plural detector claims;
- progressive bounded decomposition;
- child, View, preview, transform, decompilation and rebuild relationships;
- document, archive, image, media, binary, Android package and source-structure Domain Packs.

## WP06 — Firmware, disks and filesystems

Closed for Phase 0B design:

- Apple IPSW/BuildManifest analysis;
- MediaTek META/BROM/Preloader/DA separation;
- Qualcomm Sahara/Firehose;
- Unisoc PAC/FDL;
- Android OTA payload/sparse/dynamic-partition/AVB;
- Samsung and generic vendor routing;
- GPT/MBR and isolated filesystem inspection;
- static analysis versus physical mutation;
- exact compatibility, immutable backup and read-back proof;
- `.P5C` parked pending verified sample/spec/tool.

## WP07A — Android Device Runtime

Closed for Phase 0B design:

- stable Device identity and interface connection epochs;
- Device Provider, worker generation, lease/fencing and Device Session;
- independently scoped inventory, shell, file, package, log, display, audio, input, clipboard, semantic UI, policy/admin and firmware capabilities;
- scrcpy modern display/audio/control;
- AndroidX UI Automator official semantics;
- Appium/UIAutomator2 and TouchPilot adapters;
- privacy, stale-result rejection and verified cleanup/quarantine.

Saved:

- `decisions/ADR-0009-DEVICE-SESSION-DISPLAY-INPUT-SEMANTIC-UI-BOUNDARY.md`
- `work-packages/PHASE-0A-WP07A-ANDROID-DEVICE-RUNTIME.md`

## WP07B — Desktop and Apple Application Runtime

Closed for Phase 0B design:

- Application Object, Provider, Installation, Session, Process, Window, Display Gateway and Semantic Context separation;
- Xpra Linux individual-window display;
- Guacamole and noVNC browser remote-desktop paths;
- QEMU/libvirt Windows VM Provider;
- FreeRDP RDP machinery;
- FlaUI direct Windows semantics and NovaWindows W3C compatibility;
- Peekaboo macOS visual/accessibility adapter;
- Appium XCUITest and IDB Apple adapters;
- Apple Xcode/Simulator/XCTest/Virtualization platform dependency boundary;
- explicit application proof and checkpoint levels.

Known retained gap: dedicated Linux AT-SPI semantic automation requires a later completion pass.

Saved:

- `decisions/ADR-0010-APPLICATION-PROVIDER-WINDOW-DISPLAY-BOUNDARY.md`
- `work-packages/PHASE-0A-WP07B-DESKTOP-APPLE-APPLICATION-RUNTIME.md`

## WP08 — Browser and Live Research

**Status:** COMPLETE; closed for Phase 0B contract design, not build.

Inspected and saved:

- Playwright;
- Playwright MCP;
- Browser-Use;
- TurboWebFetch;
- internal Lumi/Hunter browser, Transfer, secret, degradation and receipt requirements.

TurboWebFetch is resolved to:

- `https://github.com/aza-ali/turbowebfetch`
- pinned commit `fa18a9f9db1e1640ff6111176ec49aa88ea211f4`
- package `1.1.0`
- MIT licence.

Accepted direction:

1. Browser Provider, Binary, Profile, Process, Context, Page, Frame, Popup, Download and Evidence remain separate.
2. Playwright is the primary Browser Facility foundation.
3. Mutable Profiles require exclusive lease, encryption and scoped ownership.
4. Browser Processes may host isolated ephemeral Contexts only after conformance proves no cross-Workspace leakage.
5. Profile clones exclude transient locks/journals and create new identity/provenance.
6. Existing personal-browser attachment requires explicit consent.
7. Navigation/process generations invalidate stale Page, Frame and locator references.
8. Source response, raw HTML, rendered DOM, accessibility, visible text, screenshot, PDF, video, trace, console, network and HAR remain separate Views/Artifacts.
9. Browser downloads enter the Transfer/Object pipeline.
10. TurboWebFetch becomes rendered batch retrieval over supervised pooled Contexts rather than process-per-fetch.
11. Playwright MCP is an optional external adapter.
12. Browser-Use may run as a caller/workload; its agent/reasoning identity stays outside Ptah Core.
13. Live Research Results are source-linked claims for external callers; Ptah does not decide conclusions.
14. Authentication, MFA, passkeys, CAPTCHA, restricted access and human completion are explicit states.
15. Browser crash recovery preserves safe evidence/partial results and never blindly replays non-idempotent actions.

Saved:

- `donors/PLAYWRIGHT.md`
- `donors/PLAYWRIGHT-MCP.md`
- `donors/BROWSER-USE.md`
- `donors/TURBOWEBFETCH.md`
- `internal/BROWSER-LIVE-RESEARCH-FOUNDATIONS.md`
- `decisions/ADR-0011-BROWSER-PROFILE-CONTEXT-PAGE-EVIDENCE-BOUNDARY.md`
- `work-packages/PHASE-0A-WP08-BROWSER-LIVE-RESEARCH.md`

Closed for Phase 0B design:

- `BROWSE-001`, `BROWSE-002` and `BROWSE-003`;
- Browser/Profile/Context/Page extensions to `SESSION-001`;
- browser-panel/download extensions to `UI-001`, `UI-002` and `XFER-002`;
- browser evidence extensions to `OBS-001` and `PROV-001`.

No Browser runtime dependency or implementation is approved yet.

---

# Active inspection unit

## WP09 — Human Workspace Shell and Operator Interface Composition

Inspect as one complementary group:

1. Eclipse Theia;
2. OpenVSCode Server;
3. code-server as an optional compatibility path;
4. xterm.js and terminal-panel patterns;
5. Monaco/editor integration where not already inherited through Theia/VS Code;
6. Golden Layout or equivalent multi-panel layout machinery only if needed;
7. internal Hunter, Foreman, Sergeant, website, Device Manager, MIBU and THETECHGUY Tool interfaces;
8. public documentation/UI patterns only after runtime requirements are placed.

Resolve:

- Ptah Home and Workspace switcher;
- Object/file/tree/search/preview views;
- many simultaneous terminals, browsers, Devices and Applications;
- Activity Centre and evidence/proof views;
- Window/panel/tab/dock identities and saved layouts;
- direct human and automation coexistence;
- handoff and ownership of focused input/control;
- responsive desktop/mobile/browser layouts;
- reconnect and degraded-capability presentation;
- honest planned/configured/connected/running/verified labels;
- private/public UI boundaries;
- accessibility, keyboard navigation and reduced-motion behavior;
- plugin contribution points without making an IDE framework Ptah Core.

Required saved output:

- internal and external donor records;
- Human Workspace Shell composition record;
- Workspace Shell / Panel / Human-Control boundary ADR;
- Requirement Closure Matrix updates for `UI-001`, `UI-002`, Human Workspace portions of `SESSION-001`, `CORE-004`, `OBS-001`, Device/Application/Browser panels and direct-human proof;
- continuous `PROGRESS.md` and Current State updates.

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
- ADR-0011 — Browser Profile, Context, Page and Evidence Boundary

---

# No-build boundary

Allowed now:

- donor/internal recovery;
- source inspection, canonical pins and licence review;
- composite requirement closure;
- ADR, schema and proof planning after Phase 0A review.

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
