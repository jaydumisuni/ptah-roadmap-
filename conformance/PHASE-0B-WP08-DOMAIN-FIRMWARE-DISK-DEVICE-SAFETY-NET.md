# Phase 0B WP08 — Domain Pack, Firmware, Disk, Filesystem and Device Safety Net

**Status:** CANDIDATE SPECIFICATION  
**Date:** 2026-07-19  
**Executable harness:** DEFERRED TO WP13  
**Fixture suite:** `conformance/fixtures/phase-0b/wp08/domain-firmware-disk-device-cases.v0.1.0.json`  
**Authoritative catalog:** `schemas/phase-0b/domain/schema-catalog.v0.1.0.json`

## Purpose

Define structural, cross-record, temporal, range, generation, authority, privacy and proof invariants for every WP08 Pack/parser, firmware/disk/filesystem adapter and Device Provider.

## A. Domain Pack and detection

1. Pack, immutable Pack Revision, Compatibility, Operation Request, Run and Coverage remain separate.
2. operation support is capability-specific; static support does not imply rebuild/execute/mutation support.
3. detector observations remain plural and immutable.
4. filename/extension/metadata/model/caller hints cannot override stronger content/parser/live evidence silently.
5. Classification Decision retains selected routes and conflicting observations.
6. unknown, ambiguous, polyglot, encrypted, malformed, truncated, unsupported and opaque are valid outcomes.
7. Pack replacement preserves source Object identity and creates new observations/Runs/results.

## B. Budgets and decomposition

1. every recursive operation has explicit hard budgets.
2. descendants inherit remaining budget; they never reset it.
3. valid partial outputs remain registered when limits/errors occur.
4. Coverage retains requested, processed, skipped and unknown scope plus consumed budget.
5. budget exhaustion/partial output cannot become complete requested scope.
6. content/ancestor identity prevents cycles and repeated expansion.
7. child Objects/Views/Relationships retain exact path/range/page/coordinate/extent and parser provenance.
8. parser output never silently replaces original bytes.

## C. Validation, compare and rebuild

1. Inventory, Validation Run, Compare Run and Rebuild Run remain distinct.
2. Validation is bounded to a frozen Protocol.
3. Compare retains exact subjects, methods, differences and tolerances.
4. Rebuild uses immutable source materials/Recipe/Pack Revision and produces new Object Revisions.
5. reopening, hash comparison, semantic comparison, execution, review and authoritative external result remain separate proof domains.

## D. Firmware package and manifest

1. Firmware Package is an Object/Artifact role over exact bytes.
2. filename/model/build/chip strings remain claims.
3. Manifest retains parser/Pack Revision, components, operations, source/destination ranges/digests, order and source requirements.
4. Components retain exact locator/bytes/digests/roles/provenance.
5. delta/patch operations cannot proceed without exact source revision/layout.
6. unsupported/opaque package sections remain visible.
7. `.P5C` remains parked/unsupported until lawful authoritative evidence exists.

## E. Executable assets and compatibility

1. loader/programmer/DA/FDL/preloader/ramdisk/payload assets are first-class Objects.
2. asset selection requires exact source/licence/provenance/digest/role/target/mode/capability evidence.
3. filename or chipset-family similarity is insufficient.
4. Compatibility Result binds exact package/manifest/components, Device Profile, connection epoch, layout digest, assets/tools/Provider generation, requested operation/ranges and proof capabilities.
5. static/read compatibility cannot become write compatibility.
6. stale Profile/layout/epoch/generation invalidates compatibility.
7. write compatibility requires backup and read-back capability evidence or explicit reviewed exception.

## F. Disk and partition geometry

1. encoded image bytes, expanded logical content and backing Objects remain separate.
2. sparse/zero/hole/compressed/backing extents are explicit.
3. untrusted backing paths never resolve outside an approved Object allowlist.
4. Partition Table retains scheme, sector size, table ranges/copies/checks and parser provenance.
5. every Partition range is within the image/logical container bounds.
6. ordinary overlaps, duplicate IDs, bad CRCs, inconsistent backup tables and logical extent conflicts remain errors/warnings.
7. partition names/GUIDs/labels are metadata/aliases, not byte identity.
8. parser replacement creates new table/partition records and comparisons, not in-place mutation.

## G. Filesystem

1. Filesystem Observations remain plural; canonical Filesystem identity is a separate selection.
2. UUID/label/type claims remain evidence-bound.
3. untrusted images/filesystems open through isolated Providers/appliances.
4. Session mode is explicit; read-only cannot call mutating backend functions.
5. writable overlay records changes separately and preserves original bytes.
6. direct writable mode requires explicit authority.
7. backing Object allowlist, Provider/Node/generation, isolation and cleanup/unmount are mandatory.
8. host mount/open paths remain aliases.
9. inspection result/coverage does not imply filesystem repair or clean state.

## H. Device identity and Profile

1. Device identity is stable across Interface, transport, mode, address, Provider and Session changes.
2. ADB/Fastboot serial, USB path, COM port, VID/PID, IP and backend ID remain aliases/observations.
3. cross-mode correlation requires multiple evidence sources or explicit operator review.
4. Profile Revision is immutable and time/source-bound.
5. sensitive identifiers are protected references, not public fields.
6. layout/security/firmware/capability changes create new Profile Revisions.
7. Device lifecycle remains independent from current reachability.

## I. Interface, Connection and generation

1. every transport/mode incarnation is a Device Interface.
2. every continuity period is a Device Connection with monotonic epoch.
3. reconnect, re-enumeration, mode change without proven continuity, Provider restart/fence or re-pair advances epoch.
4. old epoch/generation evidence cannot authorize/complete current work.
5. Interface presence/reachability is not protocol/service readiness.
6. Connection observations expire and remain separate from lifecycle.
7. stale aliases cannot merge distinct Devices automatically.

## J. Device Session, Lease and capabilities

1. Session binds exact Workspace, Device/Profile, typed Device Lease, fence, Provider generation and current connections.
2. Session creation/continuation requires current Lease/fence; stale holders are rejected.
3. Session capability snapshot is expiring and connection/generation-bound.
4. Session may be partial/recovering while Device identity remains active.
5. Session availability does not imply every Stream or mutation capability.
6. cleanup/Lease release/stream stop are separately receipted.
7. WP11 will complete generic Lease semantics; WP08 cannot invent or weaken them.

## K. Streams and Screen Context

1. video/audio/control/clipboard/log/shell/file/semantic streams are separate records.
2. each binds Session, connection epoch, Provider generation, format/geometry and privacy policy.
3. Stream observation/health remains separate from Session lifecycle/capability.
4. Screen Context is one captured observation with screenshot/coverage/redaction/limitations.
5. pixels/visible text/semantic refs do not prove input authority or action outcome.
6. stale Screen Context cannot be used after connection/Provider/display generation change without reacquisition.
7. WP09 owns semantic selector/action and Shell behavior.

## L. Backup and mutation exception

1. destructive/uncertain mutation requires verified operation-specific immutable backup unless an exact reviewed exception exists.
2. backup binds Device/Profile/Session/epoch/generation, exact expected/actual ranges/sizes, Objects/digests, Locations and restoration Recipe.
3. file/folder presence or tool success log is not backup verification.
4. partial/missing coverage produces degraded backup.
5. protected backup data is restricted by audience/retention policy.
6. exception records exact scope, consequences, compensating controls, authority and expiry.
7. exception never converts missing backup/read-back into verified safety.

## M. Mutation authorization and Plan

1. Compatibility, Mutation Authorization, Operation Plan and physical Operation remain separate.
2. Authorization binds exact Device/Profile/Session/Lease/fence, compatibility, target/source ranges, policy basis, backup/read-back requirements and expiry.
3. Plan binds executable assets/tools, ordering, source/target digests and retry policy but grants no authority.
4. stale/expired/revoked authority blocks before mutation.
5. generic raw shell/XML/payload/memory-write escape hatches require separate high-risk capability and are disabled by default.
6. read-only capability cannot reach physical mutation functions.

## N. Physical operation and protocol proof

1. Firmware Operation maps one Plan to WP02 logical Operation and physical Attempts.
2. every retry receives new Attempt/nonce; non-idempotent mutation defaults to never automatic/manual/read-back-gated.
3. stage observations are correlated to exact Device/Session/Interface/Connection epoch/Provider generation/Attempt.
4. interface presence is not protocol handshake; handshake is not loaded service; service is not write completion.
5. protocol ACK/process exit is intermediate evidence only.
6. `completed_verified` requires Operation Verification under exact current context.
7. unavailable read-back yields acknowledged-with-limitations/uncertain/manual verification, never silent verified.
8. partial protocol/output evidence is retained on failure/cancellation.

## O. Disconnect, uncertainty and recovery

1. disconnect/provider restart/Lease expiry fences old Attempts and receipts.
2. non-idempotent active operation becomes uncertain unless authoritative evidence resolves it.
3. blind retry after uncertainty is forbidden.
4. recovery uses new Session/Connection epoch/Attempts where needed.
5. recovery explicitly answers whether effect occurred, state matches, backup is restorable and retry is safe.
6. old Attempts/history are never rewritten.
7. unrelated Devices/Workspaces/Providers continue.

## P. Privacy and security

1. serials, IMEI, hardware IDs, keys, NV/calibration/RPMB/eFuse, partition bytes, screenshots/logs and operator actions are restricted by default.
2. raw credentials never enter schemas, fixtures, logs, telemetry or public export.
3. untrusted parsers/images/packages execute under bounded isolation.
4. extracted content is non-executable by default.
5. device-side executable assets require exact provenance/licence/trust/compatibility.
6. public export is allowlisted/redacted and preserves proof limitations.

## Q. Backend/Pack replacement

1. source Object and Device identity survive Pack/parser/filesystem appliance/firmware adapter/Device Provider replacement.
2. replacement creates new revisions, generations, observations, compatibility, Runs, Profiles and relationships.
3. old Connections/Leases/Receipts are fenced.
4. conflicting/negative evidence remains.
5. equivalence requires frozen comparison/conformance evidence.
6. physical outcomes and prior acknowledgements/verifications are never rewritten.

## R. Property-based invariants for WP13

- every Pack Compatibility binds exact Pack Revision, operation and current Provider context;
- complete Coverage has no required skipped/unknown/budget-exhausted scope;
- every child/partition/component range is within its source address space;
- no undeclared ordinary partition overlap exists;
- writable filesystem Session has authority and, for overlay, change Artifact;
- every Device Connection epoch is monotonic per continuity lineage;
- current Device Session Lease/fence/Provider generation/connection epoch match every mutation record;
- stale Receipts cannot satisfy new epoch/generation Operations;
- write-compatible firmware result includes backup/read-back capability evidence;
- required-backup authorization has verified Backup or exact exception;
- `completed_verified` Operation references matching Verification;
- ACK-only evidence cannot produce verified decision;
- non-idempotent uncertain Operation cannot auto-retry;
- Screen Context/Stream observations are rejected after generation/epoch expiry;
- sensitive fields never appear in public fixtures/Views;
- Pack/Provider replacement preserves canonical Object/Device IDs.

## Exit condition

WP08 is candidate-complete only when:

1. all 44 schemas resolve through catalog `0.1.0`;
2. 13 lifecycle machines use registered identities/proof vocabulary;
3. Operation Plan kind correction `0.1.1` is active;
4. fixtures cover mandatory positive/negative cases;
5. migration preserves identity, ranges, generations, privacy and negative evidence;
6. work package and ADR reference this safety net;
7. implementation/dependency selection remain blocked until Phase 0C.
