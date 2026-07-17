# Donor Record — Qualcomm EDL / Sahara / Firehose

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY QUALCOMM EDL BACKEND CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/bkerler/edl
- Default branch: `master`
- Pinned commit: `51e11022455d26bcf0b8305b930c474e9b3c81ad`
- Licence: GPL-3.0
- Activity: Active
- Classification: Qualcomm Sahara, Firehose, GPT/LUN, partition, raw XML and diagnostic backend
- Ptah targets: EDL transport/protocol detection, chip/HWID/PKHash inventory, programmer compatibility, eMMC/UFS/NAND/SPI storage, GPT/LUN/partition reads, rawprogram/patch plans and strictly gated writes/erases

## Files/components inspected

- `README.md`
- `LICENSE`
- `edlclient/Library/sahara.py`
- `edlclient/Library/firehose_client.py`
- search-located Sahara definitions, Firehose, loader database, XML parser and diagnostic tooling

## Verified capabilities and patterns

### Sahara transport and chip identity

- Detects Sahara, Firehose and legacy NAND programmer modes separately.
- Sahara handshake records protocol version and packet size.
- Command mode reads serial number, HWID/MSM ID, OEM ID, model ID, PKHash and selected SBL/debug information where supported.
- Sahara V3 handling reads extended chip information through command `0x0A` and reconstructs V1/V2-compatible HWID fields for loader lookup.
- Loader database matching uses hardware identity and public-key hash evidence.
- A caller may supply a loader explicitly when automatic selection fails.
- Sahara is responsible for loading/transferring the programmer before Firehose operations.

### Firehose session and capability discovery

- Firehose configuration distinguishes eMMC, UFS, NAND and SPI NOR plus sector/page/payload parameters.
- Connect/configure reports supported Firehose functions and target name.
- Memory type may be caller-selected or inferred from chipset/functions, with warnings where the tool is guessing.
- UFS LUNs are represented independently; eMMC normally uses LUN/physical partition zero.
- Storage information can be queried.
- `skipwrite` and related backend options exist, although Ptah must not rely on flags alone for read-only safety.

### GPT, partitions and XML

- Prints and exports primary/backup GPT per LUN.
- Reads whole flash/LUN, partitions, sectors, offsets and crypto footer.
- Dumps all selected partitions and can generate `rawprogram[lun].xml` from observed GPT.
- Detects partitions across LUNs and retains exact sector/count values.
- XML parser and raw Firehose XML execution support rawprogram/patch or arbitrary command plans.
- Bootable partitions such as XBL/SBL can be identified from rawprogram XML.

### Mutation breadth

- Writes partitions, GPT, full flash/LUN and directory sets.
- Erases partitions.
- Executes caller-provided raw XML and reset operations.
- Exposes server/TCP, memory-dump, diagnostic and attack-oriented capabilities.
- Loaders can be converted/imported into a lookup database.

### Platform/driver behavior

- EDL generally expects Qualcomm USB PID `9008`; other states require device-specific recovery methods.
- Windows uses Qualcomm serial/COM or UsbDk paths; Linux/macOS use libusb/serial dependencies.
- ModemManager/SELinux/driver configuration can interfere with communication.

## What this donor completes

- A mature open-source Qualcomm EDL protocol and Firehose backend.
- Separate transport, Sahara identity, programmer and Firehose-session layers.
- Exact eMMC/UFS/LUN/GPT/partition relationships.
- Rawprogram/patch XML compatibility and generation from observed layout.
- Read-only full-device/partition backup foundations.
- Programmer/HWID/PKHash compatibility evidence.
- Completion path for private Qualcomm/DIAG/Firehose work that is not yet auditable in a separate internal handoff.

## Important limitations for Ptah

- GPL-3.0 requires a separate service/executable or deliberate compatible-licence boundary.
- The framework combines read-only inventory with attacks, arbitrary XML, write, erase, reset and memory operations.
- A programmer is executable device-side code; provenance, signature, source and exact target compatibility are critical.
- Loader databases/community binaries can contain duplicates, mislabeled or untrusted programmers.
- Newer Sahara versions may not expose all identity fields; autodetection may remain incomplete.
- Tool inference of memory type is explicitly a guess in some paths.
- HWID/PKHash/serial are sensitive device identifiers and must not enter public logs.
- USB PID `9008` proves EDL transport presence, not correct programmer or Firehose readiness.
- Firehose `ACK` or command completion does not by itself prove flash content after write.
- Rawprogram/patch XML can describe destructive ranges and must be parsed/validated before execution.
- GPT generation from the live device is useful evidence but not proof that a candidate firmware XML matches the target.
- Sector size, LUN, physical partition and storage type must be exact; wrong assumptions can corrupt data.
- `skipresponse`, arbitrary raw XML and TCP server modes weaken verification/security and should not be exposed by default.
- Several code paths use broad exception handling and human-oriented output.
- Driver/kernel/service changes suggested by installation docs are host-wide and require separate Node administration approval.
- Main-branch tool state and external loader submodules need stable pins, SBOMs and licence review.
- Device operation laws/authorization and ownership are caller/operator responsibilities; Ptah remains neutral infrastructure.

## Must not be inherited

- Sahara/EDL presence described as successful Firehose session.
- programmer filename used as sufficient identity or compatibility.
- automatic loader selection trusted without HWID/PKHash and provenance evidence.
- rawprogram/patch XML executed before parsing ranges and comparing device layout.
- write/erase/reset/raw XML/server capabilities exposed through read-only inventory.
- memory type/LUN/sector assumptions hidden from receipts.
- `skipresponse` or missing ACK treated as normal proof.
- full-flash/partition writes without immutable backup and post-write read-back.
- public logs containing serial/HWID/PKHash or raw sensitive partition data.
- GPL source copied into permissive Ptah Core.
- driver/SELinux/ModemManager changes applied silently.

## Integration decision

**WRAP AS THE PRIMARY QUALCOMM EDL/SAHARA/FIREHOSE BACKEND THROUGH A SEPARATE GPL FACILITY.**

Ptah should expose separate capability sets:

- EDL transport/protocol inventory;
- Sahara chip/HWID/PKHash identity;
- programmer selection/verification;
- read-only Firehose storage/GPT/LUN/partition inventory;
- read-only backup;
- rawprogram/patch plan parsing/comparison;
- separately authorized write/erase/reset/raw-XML operations.

Private internal Qualcomm/DIAG engines can later conform to the same contracts without changing public schemas.

## Native Ptah gap

Ptah must define:

- Qualcomm device/chip/HWID/OEM/model/PKHash and EDL mode schema;
- programmer Object identity, digest, source, signature, licence and compatibility;
- transport→Sahara→programmer-loaded→Firehose-configured proof levels;
- storage type, sector size, LUN, GPT and partition relationships;
- rawprogram/patch XML parsed operation graph with exact ranges/files/digests;
- package/device-layout compatibility result;
- full-flash/partition backup Objects and sensitive-data classes;
- read/write/erase/reset/raw-XML retry policy and authorization;
- immutable backup/read-before-write and post-write read-back receipts;
- USB connection epoch and mode transition correlation;
- driver/host dependency manifests and admin-change receipts;
- typed backend errors/partial/cancel/timeout states;
- GPL service/SBOM/stable release and loader-submodule pins;
- DIAG operations kept separate from EDL/Firehose.

## Exit strategy

Ptah's Qualcomm contracts remain backend-neutral. bkerler/edl, internal DIAG/Firehose engines, vendor tools or future native implementations can replace one another without changing Device, Programmer, LUN, Partition, Plan or Receipt identities.

## Validation required

1. Detect EDL/Sahara version and exact chip/HWID/OEM/model/PKHash without exposing sensitive values publicly.
2. Select a programmer only from immutable verified compatibility evidence and reject mismatches.
3. Prove PID 9008, Sahara identity and Firehose configured state as separate levels.
4. Inventory eMMC and multi-LUN UFS devices with exact sector size and GPT/backup GPT hashes.
5. Parse rawprogram/patch XML into a reviewed range graph and compare it with the live GPT/layout.
6. Read full flash/selected partitions into immutable backup Objects before any mutation.
7. Disconnect/re-enumerate mid-operation and reject stale receipts from the prior connection epoch.
8. Perform one explicitly authorized partition write, then read back and verify exact digest/range.
9. Prove read-only users cannot invoke arbitrary XML, write, erase, reset, server or attack capabilities.
10. Run the GPL backend and loader set in an isolated Facility with exact source/SBOM/licence/provenance.
11. Replace the backend for one read-only operation without changing Ptah contracts.
