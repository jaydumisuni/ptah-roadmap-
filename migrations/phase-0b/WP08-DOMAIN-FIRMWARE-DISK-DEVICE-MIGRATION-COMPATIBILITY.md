# Phase 0B WP08 — Domain Pack, Firmware, Disk, Filesystem and Device Migration Compatibility

**Status:** CANDIDATE  
**Catalog:** `urn:ptah:schema-catalog:domain:0.1.0`  
**Date:** 2026-07-19

## Purpose

Define how legacy parsers, recovery/decomposition tools, firmware packages/manifests, disk images, partition/filesystem records, Device Manager/ADB/Fastboot/vendor-protocol sessions, backups and physical-operation logs enter Ptah without fabricating identity, compatibility, coverage, authority, continuity or physical proof.

## Preservation rules

1. source Content/Object/Revision remains authoritative across parser/Pack replacement;
2. Pack, Pack Revision, Compatibility, Request, Run and Coverage remain separate;
3. detector observations remain plural; migration never discards disagreements;
4. static analysis, workspace transformation and physical mutation remain separate;
5. firmware package, manifest, component and executable asset identity remain separate;
6. Device identity remains separate from serial, VID/PID, USB topology, mode and backend session IDs;
7. Interface incarnation, Connection epoch, Provider generation, Session and Lease/fence remain explicit;
8. physical Operation Plan, Authorization, WP02 Operation/Attempt, ACK and Verification remain separate;
9. backup file presence never becomes verified backup;
10. negative, partial, unsupported, stale, uncertain and failed evidence remains immutable.

## Legacy Domain Pack/tool migration

Legacy parser/tool binaries, DLLs, scripts and containers become source Objects plus Facility/Provider/Pack Revision references only when exact bytes, version, licence/dependencies and capabilities can be recovered.

A legacy `supported` flag becomes a capability or compatibility claim, not execution authority.

Unknown tool versions remain bounded legacy evidence and cannot prove equivalent output across reruns.

## Detection/classification migration

Filename, extension, MIME, magic, parser success, model output and caller labels become separate Detector Observations.

A legacy single `type` field may become a Classification Decision only when underlying evidence and selection policy are recovered; otherwise retain it as one observation.

Conflicts, polyglots, encrypted, malformed, truncated, opaque and unsupported states remain explicit.

## Inventory/decomposition migration

Legacy extracted files/children become WP03 Object Revisions only after exact bytes/digests are retained. Parser-only interpretations become Views.

Migration retains:

- parent/source revision;
- exact path/range/page/coordinate/extent locator;
- parser/Pack/Provider revision;
- operation/run/attempt correlation where available;
- coverage, budgets, skipped/unknown gaps;
- Relationships and overlaps.

Legacy `success` does not imply complete requested scope. Missing budget/coverage produces partial/unknown status.

## Firmware package migration

Legacy package directories, ZIPs, IPSWs, PAC/scatter/rawprogram/Odin packages, payloads and partition images become firmware package/component roles over exact Object Revisions.

Filenames, model names, build strings, chipset family and vendor labels remain claims.

Manifest migration retains parser revision, components, operation graph, source/destination ranges/digests, ordering, source-build/layout requirements, signatures/checksums and unknown sections.

`.P5C` remains unsupported/opaque unless a lawful sample/spec/parser is recovered; migration must not infer its structure from `.PAC` similarity.

## Loader/programmer/FDL migration

Legacy loaders, programmers, DA/FDL/preloader/ramdisk/payload binaries become `firmware.executable_asset` only with exact digest, source/licence/provenance, role, target claims, required mode/address/configuration, capability scope and verification evidence.

Unknown or unlicensed assets remain blocked/reference-only. Filename/SoC-family similarity cannot become compatibility.

## Disk/image migration

Legacy disk/sparse/virtual image records become Object Revision plus Disk Image Revision/Extent Map.

Migration retains exact bytes, logical/physical size, sector/alignment, format, sparse/backing extents and backing Object allowlist. Untrusted embedded backing paths are never resolved automatically.

Partition table/partition migration retains scheme, table ranges/copies/checks, exact LBA/byte ranges, partition index/type/GUID/name/attributes, overlaps, bounds and logical extent relationships.

Names, labels and GUIDs remain metadata/aliases, not byte identity.

## Filesystem migration

Legacy filesystem type/UUID/label/mount records become plural Filesystem Observations plus a selected Filesystem identity where evidence permits.

Host mount paths are aliases only. Read-only/writable mode, isolated Provider, generation, backing allowlist, overlay/change artifact and cleanup/unmount evidence are required for Session migration.

A legacy host loop/kpartx mount does not become approved isolated inspection. Unknown write effects remain limitations or uncertain state.

## Device identity migration

Legacy device records are correlated into stable Device identity only with multiple evidence sources such as hardware attestation, platform identifiers, prior profile/layout, operator confirmation and continuity records.

ADB/Fastboot serial, USB path, COM port, VID/PID, IP, service PID and backend device ID remain scoped Aliases/Interface observations.

Where identity cannot be proven across modes/reconnects, create distinct candidate Devices or require manual correlation rather than silently merging.

## Interface/connection migration

Each observed transport/mode incarnation becomes a Device Interface. A Device Connection requires one continuity epoch.

Re-enumeration, reconnect, re-pair, mode transition without proven continuity, Provider restart/fencing or lost transport advances epoch.

Legacy receipts/logs without epoch/generation become historical evidence only and cannot complete current Operations.

## Session/stream migration

Legacy ADB/scrcpy/Appium/vendor sessions become Device Sessions only with Workspace, Device, Lease/fence, Provider generation, current connection refs, capability snapshot and privacy policy.

Display/log/input/file/shell channels become separate Streams with format, connection epoch, generation, privacy and recording references.

UI screenshots become Screen Context observations; they do not establish semantic targets or input success.

## Backup migration

Legacy backup files become Device Backup candidates only after exact target/ranges, expected/actual size, Content/Object/digests, Location and verification are recovered.

File existence, tool log `backup complete`, or folder naming is insufficient. Unknown range/layout/device provenance remains degraded/unverified.

Protected data receives restricted audience/retention. Restoration compatibility remains explicit.

## Physical operation migration

Legacy flash/erase/read/reset/service logs map to:

- Operation Plan;
- Compatibility Result;
- Mutation Authorization/exception;
- Device Session/Lease/fence/Connection epoch/Provider generation;
- WP02 Operation and Attempts;
- protocol-stage observations;
- Firmware Operation;
- Operation Verification;
- recovery/cleanup.

A tool/process exit or protocol ACK maps only to acknowledged evidence. `verified` requires correlated read-back or authoritative result.

Disconnect during non-idempotent operation maps to uncertain unless authoritative reconciliation proves outcome. Never infer safe retry.

## Backend/Pack replacement

Replacement:

1. preserves source Object and Device identity;
2. creates new Pack/Facility/Provider revisions and generations;
3. creates new observations, compatibility results, Runs, Inventories, Profiles and Relationships;
4. fences old connections/Leases/Receipts;
5. retains conflicting and negative evidence;
6. compares outputs under frozen protocols before equivalence claims;
7. does not rewrite historical physical outcomes.

## Breaking changes

Require explicit migration when changing:

- Pack operation/capability/compatibility semantics;
- detector confidence/evidence/classification policy;
- coverage/budget/decomposition relationship semantics;
- firmware manifest/component/asset roles;
- disk range/extent/partition/filesystem identity rules;
- Device identity correlation/profile/interface/epoch semantics;
- Lease/fence/session capability requirements;
- backup coverage/verification rules;
- protocol-stage/ACK/read-back meanings;
- mutation authorization/retry/recovery policy;
- privacy/redaction/retention for sensitive Device evidence.

## Negative migration cases

Reject or require manual review when migration attempts to:

- use parser exit, extension or filename as authoritative type;
- discard competing detector observations;
- claim complete decomposition without coverage/budget evidence;
- treat extracted path as child Object identity without bytes/digest;
- infer `.P5C` structure or loader compatibility by family resemblance;
- resolve untrusted backing-file paths automatically;
- mount untrusted image writable without isolated authority;
- merge Devices across modes from one serial/VID/PID/IP;
- reuse old epoch/generation/Lease evidence;
- call USB mode presence protocol readiness;
- call ACK/process exit verified physical success;
- treat backup file existence as verified backup;
- retry uncertain non-idempotent mutation automatically;
- import raw credentials/keys/protected identifiers into public records;
- replace Pack/Provider while rewriting old results.

WP13/WP14 must execute representative legacy import, round-trip, Pack/backend replacement and negative cases. Structural validation alone is insufficient.
