# WP08 Cross-Machine Invariants

**Status:** CANDIDATE  
**Date:** 2026-07-19

These rules compose the WP08 Domain Pack, firmware, disk, filesystem and Device records with WP01–WP07 without collapsing identity, execution or proof.

1. `domain.pack`, immutable Pack Revision, compatibility, detector observation, classification, request, run, inventory, coverage, validation, comparison, rebuild and decomposition remain separately addressable.
2. A filename, extension, MIME claim, model string, VID/PID, serial, USB path or backend parser result is evidence or Alias only; none is canonical Object, Device, Pack or Operation identity.
3. Conflicting detector and Device observations are preserved. A Classification Decision selects a route without deleting contrary evidence.
4. Every Domain Run binds an exact input Object Revision or Device context, accepted Pack Revision, current compatibility result, Facility/Provider revision and generation, Activity, Operations, Attempts, budgets and proof requirements.
5. Partial decomposition retains valid children, Views and Relationships plus explicit unknown, skipped, unsupported and budget-exhausted coverage. Partial output is never silently upgraded to complete coverage.
6. Parser or Pack replacement preserves source Object identity and creates new observations, runs, children/Views and revisions rather than rewriting historical results.
7. A Firmware Package, Manifest Revision, Component, executable asset, compatibility claim and reviewed compatibility result remain separate.
8. Static analyzability, readability, rebuild-copy compatibility and physical write compatibility are distinct outcomes. Any weaker capability must not authorize a stronger operation.
9. Disk/Image byte identity remains WP03 Content/Object identity. Disk Image Revision, Extent Map, Partition Table, Partition and Filesystem records are interpreted roles over exact revisions and ranges.
10. Partition and extent records must retain exact sector size, byte/LBA ranges, backing relationships, overlap, bounds, alignment and validation evidence. Names, labels and GUIDs are metadata, not identity.
11. Read-only mount/inspection cannot become writable without a new compatible request, authorization, Provider capability and isolated writable target/overlay. Cleanup and unmount evidence remain explicit.
12. Device identity survives Interface, mode, transport, Provider and connection changes. Interface incarnation and Connection epoch advance whenever continuity is not proven.
13. Old connection epochs, Provider generations, Session capability snapshots, Leases or fencing tokens cannot authorize or complete newer physical operations.
14. A Device Session may remain alive while one Interface or Stream is unavailable. Session lifecycle, reachability, stream health and Screen Context freshness are distinct.
15. Every physical retry receives a new WP02 Attempt identity and nonce. A non-idempotent write with uncertain outcome is reconciled before any retry.
16. Protocol presence, handshake, service configuration, write acknowledgement, completion response and post-operation read-back are separate observations/proof levels.
17. Physical mutation requires exact Device, Profile Revision, Session, Connection epoch, Provider generation, current Lease/fence, Compatibility Result, immutable Operation Plan, Mutation Authorization, backup policy and verification strategy.
18. A destructive operation is blocked unless the required immutable backup exists and is verified, or a narrowly scoped Mutation Exception records authority, reason, compensating controls and expiry.
19. Backup creation does not prove restoration compatibility. Backup bytes, verification, durable Locations and restoration Recipe remain separately evidenced.
20. Write acknowledgement never equals verified physical state. Success requires operation-specific read-back or an explicit policy-bounded inconclusive result.
21. Disconnect, Provider restart, mode transition, timeout or conflicting read-back during non-idempotent mutation produces `uncertain` physical outcome and Device Operation Recovery—not blind success or retry.
22. Recovery, cleanup, reboot, transport release, lease release and post-recovery capability/profile refresh remain independently receipted.
23. Screen Context is an immutable observation tied to exact Session, connection/display epoch and Provider generation. WP09 actions must reject stale or ambiguous contexts.
24. Sensitive identifiers, calibration/NV data, credentials, keys and private screen/log content follow audience, privacy, redaction, retention and export policy; raw secrets never enter ordinary records.
25. Backend replacement creates new compatibility decisions, Provider bindings, Sessions, Runs and Attempts while preserving stable Pack, Object, Device, Artifact and proof history.
26. Negative, unsupported, contradictory, partial and inconclusive outcomes are immutable evidence and cannot be deleted or overwritten to manufacture success.
