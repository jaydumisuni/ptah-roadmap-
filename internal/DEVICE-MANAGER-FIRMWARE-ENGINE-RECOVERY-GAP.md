# Internal Recovery Record — Device Manager Firmware Engine Source Gap

**Phase:** 0A / WP06  
**Status:** PARTIAL RECOVERY — EXACT PRIVATE MODULE SOURCE NOT YET INSPECTED  
**Inspected:** 2026-07-17

## Known repository

- Repository: `jaydumisuni/thetechguy-device-manager`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `e40189f6a4832124c91172b77967c46c06b5c66a`
- Commit form: very large initial source import

## Known intended/internal scope

Project history and prior operating evidence indicate that this private project contains or is intended to contain shared engines and profiles for:

- ADB;
- Fastboot;
- MTP;
- USB/serial;
- MediaTek/META;
- SPD/Unisoc;
- Qualcomm/DIAG;
- brand/device profiles;
- Android device operations.

However, the current GitHub connector/search index did not expose a complete repository tree or discover exact source paths for the private Qualcomm and Unisoc engine modules.

## What was attempted

- repository metadata and latest commit were read;
- repository code search was attempted for MTK, META, Qualcomm, DIAG, Firehose, SPD, Unisoc, PAC, FDL and OTA terms;
- installed repository search was used to locate separate handoffs/forks;
- separate MTK META research and Android OTA repositories were found and inspected;
- no separate auditable internal Qualcomm or Unisoc engine repository/handoff was found;
- the very large initial commit diff was insufficient to recover a reliable complete module list.

## What can be credited now

- Internal MTK META evidence is credited only through `internal/MTK-META-FOUNDATIONS.md`.
- Internal Android OTA package-state control is credited only through `internal/ANDROID-OTA-CONTROL.md`.
- MIBU's operation-correlation and device-proof patterns are already credited through `internal/MIBU.md`.
- General device-manager architecture requirements may inform future inspection, but no exact private Qualcomm/Unisoc implementation capability is marked complete from this monorepo.

## What cannot be claimed

Until exact files are inspected, the roadmap must not claim that the private monorepo already provides:

- a working Qualcomm Sahara/Firehose/DIAG engine;
- a working Unisoc BootROM/FDL/PAC engine;
- a complete shared USB/serial abstraction;
- production-safe write/erase/reset operations;
- exact driver/profile/loader databases;
- durable Activity/receipt integration;
- public-reusable or licensable engine source.

## Decision

**DO NOT BLOCK PTAH CONTRACT DESIGN, BUT DO NOT REPLACE OR DISCARD THE PRIVATE SOURCE.**

WP06 may close its neutral schemas and donor composition using the inspected external/open backends and proven internal handoffs.

Before any implementation/fork/extraction decision involving the private device-manager engines, a later recovery pass must obtain the local repository or a materialized tree and inspect exact modules source-by-source.

## Required future recovery procedure

1. obtain a local/materialized copy or repository-tree listing;
2. identify shared core/engine/profile directories;
3. pin exact files and commits;
4. inspect transport, protocol, parser, read/write and safety paths separately;
5. run available tests or live read-only proof;
6. compare every engine against WP06 schemas and donor records;
7. classify each component as extract, wrap, adapt, rebuild, retain private or reject;
8. document licence/ownership and bundled vendor binary/driver dependencies;
9. preserve any stronger intentional behavior by amending ADR-0008 rather than silently replacing it.

## Phase 0A status

- Internal overlap is recorded honestly as partial.
- The exact source recovery task remains in the donor/internal recovery backlog.
- It is not critical to Phase 0B schema design because backend-neutral contracts and exit paths are available.
- It becomes mandatory before Phase 0C selects any internal Device Manager engine as an implementation dependency.
