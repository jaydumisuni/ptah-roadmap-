# ADR-0025 — Domain Pack, Firmware, Disk, Filesystem and Device Boundary

**Status:** PROPOSED  
**Date:** 2026-07-19

## Context

Ptah must inspect, decompose, validate, compare, rebuild and sometimes physically apply complex files, firmware, disks/filesystems and Device operations across interchangeable parsers, Providers, Nodes and vendor protocols.

Without a fixed boundary, implementations tend to collapse:

- filename/type claims into source truth;
- parser output into complete decomposition;
- firmware package claims into exact Device compatibility;
- transient USB/ADB/Fastboot/vendor aliases into Device identity;
- protocol acknowledgement into verified success;
- read-only inspection into mutation capability;
- backend session IDs into canonical Ptah identity;
- reconnect/retry into continuation of stale authority.

Those collapses would make recovery, migration, audit and safe physical work unreliable.

## Decision

Adopt the WP08 candidate boundary:

- stable Domain Pack identity plus immutable Pack Revision;
- separate compatibility, detector observation and Classification Decision;
- separate Domain Request, Run, Inventory, Coverage, decomposition, Validation, Compare and Rebuild;
- bounded progressive decomposition with retained partial results and unknown gaps;
- Firmware Package/Manifest/Component/executable-asset roles over exact Objects;
- separate source compatibility claims and reviewed exact-context compatibility results;
- Disk/Image/Object byte identity separate from interpreted image, extent, partition and filesystem records;
- isolated read-only filesystem inspection and explicit writable target/overlay authority;
- stable Device identity separate from Profile Revision, Interface incarnation, Connection epoch, Session, capability snapshot, Stream and Screen Context;
- current Lease/fencing, Provider generation and connection epoch for physical mutation;
- immutable Operation Plan, target ranges, Mutation Authorization, backup/read-back policy and exact Attempts;
- verified immutable backup before destructive mutation unless an explicitly reviewed narrow exception applies;
- protocol-stage observations, write acknowledgement and post-condition read-back Verification as separate proof;
- uncertain physical outcomes and explicit recovery/reconciliation instead of blind retry;
- privacy/redaction for sensitive Device, credential, calibration, log and screen data;
- backend replacement preserving canonical Pack/Object/Device/proof history.

## Consequences

### Positive

- Implementation teams receive precise contracts for parsers, firmware tools and Device adapters.
- Static analysis and physical mutation cannot be confused.
- Re-enumeration, reconnect and Provider restart fence stale work.
- Destructive operations have enforceable backup, authorization and read-back gates.
- Vendor tools can be replaced without changing public Ptah identity.
- Partial and unsupported results remain useful and honest.
- THETECHGUY ADB/Fastboot/MTP/META/DIAG workflows can map into one neutral Device model without exposing private internal policy as Ptah identity.

### Cost

- More records and correlations are required than a simple tool log or boolean success flag.
- Adapters must emit exact generation, epoch, target-range, Attempt and proof references.
- Some legacy operations will remain inconclusive because their logs do not prove identity or post-condition state.
- Executable conformance must test semantic invariants beyond JSON Schema.

## Rejected alternatives

1. **One generic file/device operation record** — loses identity, coverage, authority and proof boundaries.
2. **Treat backend sessions or USB/ADB serials as Device identity** — unstable across reconnect, mode and Provider changes.
3. **Treat package/model/chipset match as write compatibility** — unsafe and insufficiently specific.
4. **Treat write acknowledgement as success** — proves only one protocol response, not physical post-condition.
5. **Permit destructive work without backup by default** — conflicts with recoverability and evidence requirements.
6. **Use host-kernel writable mounts for untrusted images as the default** — weakens isolation and mutation boundaries.
7. **Discard conflicting/negative results** — manufactures false confidence and breaks reproducibility.

## Acceptance gate

ADR-0025 may become `ACCEPTED` only after:

- the WP08 catalog and schemas pass collision/offline-resolution review;
- lifecycle machines and cross-machine invariants are complete;
- migration, privacy and backend-replacement review passes;
- the WP08 positive/negative fixture manifest and consolidated safety net cover the required proof cases;
- any entity-kind/schema mismatch is corrected explicitly.

Acceptance authorizes downstream contract use only. It does not authorize runtime implementation, dependency selection or live Device mutation.
