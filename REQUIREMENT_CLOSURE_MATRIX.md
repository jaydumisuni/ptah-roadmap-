# Ptah Requirement Closure Matrix

**Phase:** 0A  
**Status:** NOT POPULATED

This file becomes the decisive map between the accepted Ptah requirements, internal work, external donors, mature upstream machinery, and native Ptah implementation.

A requirement is not closed by naming a repository. It is closed only when the exact implementation boundary and proof path are known.

---

# Status values

- `OPEN`
- `RECOVERING INTERNAL WORK`
- `INSPECTING DONORS`
- `CANDIDATE SELECTED`
- `LICENCE REVIEW`
- `VALIDATION REQUIRED`
- `CLOSED FOR DESIGN`
- `REJECTED PATH`
- `PARKED`

---

# Matrix

| ID | Requirement | Roadmap phase | Internal evidence | Primary donor | Secondary / exit donor | Mature upstream machinery | Native Ptah gap | Public/private boundary | Licence decision | Integration classification | Validation activity | Evidence | Status |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| CORE-001 | Persistent workspace model | 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| CORE-002 | Concurrent activity runtime | 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| CORE-003 | Object graph and catalogue | 1–3 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| CORE-004 | Facility and plugin host | 0B–1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| CORE-005 | Node protocol and capability reporting | 1, 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| RELAY-001 | Live event transport | 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| RELAY-002 | Durable activity recovery | 1, 8 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| STORE-001 | Hot local workspace storage | 1–2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| STORE-002 | Durable object storage | 2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| STORE-003 | Metadata catalogue | 1–2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| STORE-004 | Content hashing and deduplication | 1–2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| STORE-005 | Drive export and recovery | 2, 8 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| XFER-001 | Resumable uploads | 2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| XFER-002 | Fast resumable downloads | 2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| XFER-003 | Cloud and node synchronization | 2, 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| GIT-001 | Mirrors, worktrees, branches, tags, commits | 5 | TBD | TBD | TBD | Git | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| EXEC-001 | Terminal and process supervision | 1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| EXEC-002 | OCI/container workspace provider | 5 | TBD | TBD | TBD | containerd/OCI | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| EXEC-003 | Reproducible build graph | 5 | TBD | TBD | TBD | BuildKit | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| EXEC-004 | Stronger isolation backends | 5, 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| BROWSE-001 | Interactive persistent browser | 6 | TBD | TBD | TBD | Playwright/Chromium | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| BROWSE-002 | Rendered extraction and research | 6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| BROWSE-003 | Screenshots, recordings, traces, network, console | 6 | TBD | TBD | TBD | Playwright | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DECOMP-001 | True-type detection | 3 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DECOMP-002 | Recursive archive decomposition | 3 | TBD | TBD | TBD | libarchive | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DOC-001 | Document extraction, structure, rendering, proof | 3, 10 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| MEDIA-001 | Video/audio inspection and transformation | 3 | TBD | TBD | TBD | FFmpeg | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| IMAGE-001 | Fast image processing and previews | 3 | TBD | TBD | TBD | libvips | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| BIN-001 | PE/ELF/Mach-O and binary decomposition | 3 | TBD | TBD | TBD | LIEF | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| APP-001 | APK/AAB/DEX decomposition | 3, 9 | TBD | TBD | TBD | JADX/Apktool | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-001 | Apple firmware family | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-002 | MediaTek firmware family | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-003 | Unisoc firmware family | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-004 | Qualcomm firmware family | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-005 | Generic Android OTA and dynamic partitions | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FW-006 | Other vendor and embedded firmware packs | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| FS-001 | Disk, partition, image, and filesystem facility | 4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DEVICE-001 | Android device inventory and ADB | 9 | TBD | TBD | TBD | Android platform tools | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DEVICE-002 | Android screen, input, semantic UI, and recording | 9 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| APP-002 | Linux graphical and native application runtime | 9 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| APP-003 | Windows EXE/MSI runtime | 9 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| APP-004 | Apple IPA/macOS runtime | 9 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| UI-001 | Human workspace shell | 7 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| UI-002 | Activity Centre | 7 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| SESSION-001 | Checkpoint, archive, export, import, resume | 8 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| SYNC-001 | Online/local synchronization and conflicts | 8, 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| SEARCH-001 | Unified search and indexing | 10 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DATA-001 | Structured data and database pack | 10 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| PLUGIN-001 | Plugin discovery, pinning, health, upgrade, rollback | 10 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| OBS-001 | Logs, metrics, traces, correlation, resource accounting | 1, 11 | TBD | TBD | TBD | OpenTelemetry | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| PROV-001 | Provenance, attestations, signing, and proof bundles | 11 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| SEC-001 | Security workload hosting and evidence | 11 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| DIST-001 | Multi-node capability placement and transfer | 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |
| OFFLINE-001 | Local-first and intermittent-connectivity operation | 12 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN |

---

# Completion rule

Phase 0A cannot close until every v1 row is either:

- `CLOSED FOR DESIGN`, with evidence and exit strategy;
- explicitly `PARKED` outside v1;
- or `REJECTED PATH`, with reason and replacement.
