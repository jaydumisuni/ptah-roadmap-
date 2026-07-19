# WP08 Consolidated Safety Net

**Status:** CANDIDATE TEST PLAN  
**Contract families:** `ptah.domain`, `ptah.firmware`, `ptah.disk`, `ptah.device` `0.1.0`

WP08 is candidate-complete only when every structural and semantic gate below is implemented by the Phase 0B conformance harness and all pinned fixtures pass.

## Structural gates

- Parse every WP08 JSON document as JSON Schema 2020-12 or the registered lifecycle format.
- Require unique absolute Ptah URNs, schema names, versions, entity kinds and state-machine names.
- Resolve every reference from local catalogs without network access.
- Require the common Entity Envelope and exact registered `entity_kind`.
- Reject unknown top-level fields except through `extensions`.
- Validate state-machine initial states, transitions, authority, evidence and unknown-state policy.
- Prove all generation, connection-epoch, Attempt, Lease/fence and target-range fields are represented where required.
- Prove ordinary records contain no raw credentials, keys or unrestricted sensitive identifiers.

## Positive proof cases

1. **Detector conflict retained:** magic-byte and filename detectors disagree; both observations survive and an explicit Classification Decision selects a route with limitations.
2. **Polyglot input:** two compatible Packs produce separate Inventories/Views without either becoming sole source truth.
3. **Budgeted decomposition:** recursion or expansion budget is reached; valid children remain and Coverage identifies skipped/unknown ranges and budget exhaustion.
4. **Parser replacement:** a second Pack/Provider revision produces a competing decomposition while source Object identity remains unchanged.
5. **Disk hierarchy:** raw image, extent map, GPT/MBR copies, partitions and filesystem observations retain exact sector/byte ranges, checks and overlap findings.
6. **Isolated inspection:** an untrusted filesystem opens read-only in an isolated Provider; visible root, backing allowlist and cleanup evidence are recorded.
7. **Firmware static analysis:** package, manifest, components and executable assets are inventoried without granting physical write compatibility.
8. **Exact write compatibility:** package/component, Device Profile, layout digest, executable asset, tool/Provider revision, security state and target ranges all match.
9. **Required backup:** immutable backup bytes, ranges, digest verification, durable Locations and restoration Recipe exist before destructive authorization.
10. **Connection fencing:** Device re-enumeration advances connection epoch; stale Receipts and capability snapshots cannot complete the new Operation.
11. **New retry identity:** a safe retry creates a new Attempt/nonce and exact Provider-generation binding.
12. **Read-back verification:** protocol acknowledgement is followed by operation-specific read-back and comparison before verified success.
13. **Uncertain physical outcome:** disconnect during a non-idempotent write preserves partial evidence and creates Device Operation Recovery instead of blind retry.
14. **Stream independence:** video stream fails while shell/log stream and Device Session remain available with explicit degraded scope.
15. **Fresh Screen Context:** screenshot/semantic observation binds exact Session, display/connection epoch and Provider generation.
16. **Backend replacement:** stable Pack/Object/Device history survives a parser, mount, transport or flasher adapter replacement.

## Negative proof cases

Reject or classify explicitly:

- filename, extension, model string or MIME claim used as authoritative classification without evidence;
- one detector observation deleting or overwriting a conflicting observation;
- partial decomposition claimed complete without bounded Coverage;
- child/View output replacing the source Object Revision;
- parser/backend ID used as canonical Pack, Object, Device or Operation identity;
- malformed partition or extent outside image bounds;
- unreported overlapping partitions/extents;
- untrusted host backing path selected from image metadata;
- read-only mount silently upgraded to writable;
- mount/inspection without isolation or cleanup evidence;
- firmware filename/chipset similarity used as write compatibility;
- untrusted or mismatched loader/programmer/FDL selected for execution;
- static-analysis compatibility reused for physical mutation;
- mutation with stale Profile, connection epoch, Provider generation, Lease or fence;
- mutation without exact target ranges and immutable Plan;
- destructive operation without verified backup or a valid narrow exception;
- backup existence treated as proof of restoration compatibility;
- physical retry reusing Attempt identity;
- protocol handshake, loader acceptance, service return or write acknowledgement treated as verified success;
- disconnect during non-idempotent write followed by automatic retry;
- stale Screen Context used for semantic input;
- raw secret/key/calibration value exported in ordinary records or public proof;
- negative, unsupported, partial or inconclusive evidence removed to manufacture success.

## Required semantic assertions

The harness must assert, beyond JSON Schema:

- timestamps and expiry ordering;
- exact subject/revision consistency across references;
- range bounds, overlap, alignment and coverage arithmetic;
- current Provider generation and connection epoch;
- Lease/fence validity at dispatch and completion;
- new Attempt identity for every physical retry;
- compatibility strength is at least the requested operation strength;
- backup coverage contains every policy-required target range;
- Mutation Exception scope cannot exceed its authority or expiry;
- write/read-back comparison covers every declared critical range;
- stale/late/duplicate/contradictory evidence is reconciled, not overwritten;
- public/private export follows audience, privacy and redaction policy.

## Proof artifacts

A passing run produces immutable:

- catalog-resolution report;
- structural-validation report;
- lifecycle-validation report;
- positive/negative fixture results;
- semantic-invariant report;
- migration and backend-replacement report;
- secret/privacy scan report;
- exact tool/harness revision, environment and receipt set.

Until these reports exist and pass, WP08 remains candidate contract design—not implemented or proven runtime capability.
