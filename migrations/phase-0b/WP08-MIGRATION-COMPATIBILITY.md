# WP08 Migration and Compatibility Record

**Status:** CANDIDATE  
**Date:** 2026-07-19

WP08 migration preserves Ptah identity while importing or replacing parsers, firmware tools, disk/filesystem engines, Device transports and physical-operation backends.

## Import boundary

Existing archives, firmware packages, disk images, manifests, scatter/XML/config files, loaders/programmers/FDLs, device profiles, ADB/Fastboot/META/DIAG records, screenshots, logs and backups enter Ptah as exact WP03 Objects/Object Revisions plus scoped Aliases and observations.

Recognition never grants:

- canonical Pack, Device or Operation identity;
- execution or mutation authority;
- compatibility for a stronger operation;
- complete decomposition or manifest coverage;
- successful physical state.

## Directional migration sequence

1. Register exact source bytes, qualified digests, origin, audience and privacy.
2. Preserve legacy path, filename, serial, VID/PID, job/session and backend identifiers as scoped Aliases.
3. Emit detector or connection observations with exact producer revision/generation and limitations.
4. Create or resolve stable Domain Pack, Object, Device and role identity.
5. Create immutable Pack, Profile, Manifest, Partition Table or other revisions.
6. Record Classification and compatibility decisions separately from observations.
7. Require new accepted Requests, Activities, Operations and Attempts for execution.
8. Register all derived children, Views, Relationships, Inventories and Coverage without replacing source truth.
9. For physical mutation, require current Session, Connection epoch, Provider generation, Lease/fence, Plan, Authorization, backup and verification strategy.
10. Preserve partial, failed, uncertain and contradictory evidence during migration.

## Backend replacement

Replacing a parser, Pack implementation, mount appliance, Device worker, flasher, loader/programmer transport or display backend must:

- preserve stable Pack, Object, Firmware Package, Disk/Image, Partition, Filesystem and Device identity;
- preserve historical Runs, Attempts, observations, Receipts and proof;
- create new Pack/Provider revisions, compatibility results, Sessions, connection epochs and Runs;
- recompute derived Views/children as new revisions or competing outputs;
- fence stale generations and invalidate expiring capability/compatibility snapshots;
- never reuse backend job/session IDs as Ptah identity.

## Compatibility direction

Compatibility is exact, directional, operation-specific and expiring. It binds:

- source Object/Device/Profile/Manifest/layout revisions;
- requested operation, mutation class and target ranges;
- Pack/Facility/Provider revisions and Provider generation;
- Node/runtime/platform/isolation context;
- executable assets, toolchain, security/rollback/key state;
- resource, network, credential, backup and read-back capability;
- policy, audience and privacy requirements.

Compatibility for detection, inventory, read, static validation or rebuild-copy does not imply compatibility for write, erase, repartition, security-state change or protected-region mutation.

## State and schema evolution

Breaking schema or lifecycle changes require:

- explicit source and target schema versions;
- field and enum mapping;
- state-transition mapping;
- proof/authority preservation;
- unmapped-value behavior of reject, preserve-as-extension or manual review;
- fixture-backed migration tests;
- no silent conversion of unknown/partial/uncertain to success.

## Legacy physical records

Legacy tool logs that only show device detection, handshake, loader acceptance, service return code or write acknowledgement migrate as observations/Receipts at the proven level. They do not become verified success without exact target identity, generation correlation and post-condition read-back.

## Exit strategy

No public WP08 contract depends on one donor API or vendor protocol. An adapter may be removed while preserving source Objects, Pack/Device identity, manifests, backups, proof history and migration Aliases. Unsupported replacement paths remain explicit negative compatibility evidence.
