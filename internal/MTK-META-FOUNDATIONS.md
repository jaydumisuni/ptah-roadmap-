# Internal Recovery Record — MediaTek META and Flash Foundations

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PROVEN READ-ONLY META ATTACH/INVENTORY PLUS BROADER GPL FLASH BACKEND  
**Inspected:** 2026-07-17

## Sources inspected

### Sanitized META research handoff

- Repository: `jaydumisuni/mtk-meta-boot-research-handoff`
- Visibility: Public
- Pinned commit: `4c1b061b1fe4b8d0b1cb9f8e1f255b6ce98ff2d1`
- Files inspected:
  - `README.md`
  - `tools/mtk_meta/RUN_D4_SAFE_READ_ORCHESTRATOR.ps1`
- Licence: no root licence was found; preserve research/source ownership boundaries.

### MTKClient META-mode fork

- Repository: `jaydumisuni/mtkclient-meta-mode`
- Visibility: Public
- Pinned commit: `2c9f4d78601e2b223cacfed773a5c4cbb1808189`
- Files inspected:
  - `README.md`
  - `mtk.py`
  - `LICENSE`
- Licence: GPL-3.0
- Relationship: boot/flash helper and broad MTK backend; the handoff explicitly states it is **not** the proven D4 read path.

## Verified read-only META evidence

- Native existing-META attach succeeded through `SP_META_ConnectInMetaModeByUSB` on MediaTek USB VID `0E8D`, Kernel META PID `2007`.
- `SP_META_GetTargetVerInfo_r` and `SP_META_GetChipID_r` succeeded.
- SP modem inventory through the AP handle succeeded for capability, type, information, image, mode, status and database paths.
- Device APDB directories were enumerated and matched APDB filenames were identified.
- The research bundle deliberately excludes vendor DLL/EXE binaries, compiled probes, downloaded APDB binaries, raw unique device identifiers and destructive-operation output.
- Serial/chip identifiers were sanitized/redacted in the handoff.
- `SP_META_NVRAM_Init_r` accepted a matched local APDB, but identifier getters still returned result `2` during the previous run.
- The separate modem/NVRAM service connection remains unresolved; `META_ConnectWithMultiModeTarget_r` / `META_Connect_Ex_Req` recovery is the next documented research direction.

## Verified orchestration and safety behavior

- The orchestrator locates the real project root and validates the expected MTK runtime profile/DLL directory.
- It detects an existing Kernel META COM port through VID/PID and COM-name evidence.
- Boot-to-META is optional and only used when explicitly requested with `-BootIfNeeded`.
- `mtkclient-meta-mode` is cloned/updated with fast-forward-only Git pull and given a dedicated Python virtual environment.
- The fork is invoked only to boot the device into META; the D4 native MetaCore runner performs read-only inventory.
- Boot success is not inferred from process exit alone: PID_2007 must appear afterward.
- Each D4 mode receives its own stdout/stderr files, timeout, exit code and summary record.
- Timed-out processes are killed and recorded with a dedicated timeout result.
- Baseline, database inventory, database acquire/init, barcode and IMEI read attempts are separate modes.
- Additional vendor BT/Wi-Fi/IMEI reads are excluded unless explicitly requested.
- The orchestrator creates timestamped audit folders and a JSON summary.
- A documented safety lock prohibits NVRAM writes, factory reset, FRP/format/unlock, shell commands, reboot/reset and Enable ADB without later explicit approval after a valid read-only handle.

## Verified broader MTKClient capabilities

- MTKClient exposes GPT inventory/export, partition/full-flash/sector/offset reads, FUSE mounting, writes, erases, crypto-footer read, BROM/SRAM/preloader dumps, META modes, payload/stage operations, target configuration and logs.
- It distinguishes read, write, erase, reset, exploit/payload, DA and META operation families.
- V6 chipsets such as MT6789 require a proper loader and preloader-mode workflow rather than assuming classic BROM access.
- Connection options include VID/PID, serial port, auth/certificate, loaders, preloaders, DA/exploit settings, sector sizes and partition/LUN types.
- Tool source is GPL-3.0 and must remain a separate executable/service boundary unless Ptah adopts compatible licensing for modified integration files.

## Strong internal patterns for Ptah

1. Boot/transport establishment and service/read session are separate proof levels.
2. PID_2007 is transport presence, not proof of a valid META service handle or successful read.
3. Read-only inventory is the default research lane; destructive operations require a separate explicit capability and authorization path.
4. Every native mode should produce isolated stdout/stderr, timeout, exit and structured summary evidence.
5. APDB/MDDB files are compatibility dependencies with exact filenames/build relationships, not generic resources.
6. Device identifiers and vendor databases must be redacted/excluded from public handoffs.
7. Boot helper and read backend can be different Facilities with independently proven capabilities.
8. Unknown/unresolved service connectors must remain explicit rather than being replaced by guessed read/write claims.
9. V6/preloader/BROM/META/DA modes and loaders are distinct compatibility dimensions.
10. A successful process call must be followed by observed USB/service-state verification.

## Important limitations

- The D4 runner depends on vendor DLLs, ABI exports and APDB/MDDB files that are excluded from the public handoff and require separate licence/source/distribution review.
- The proven read path is Windows/x86/native-DLL/COM-port specific.
- Device APDB identification is filename/database matching, not yet a full cryptographically verified package/provenance model.
- NVRAM identifier reads remain unresolved despite accepted NVRAM initialization.
- The MD/NVRAM multi-mode connector is not proven.
- Barcode/IMEI read attempts appear in orchestration, but a scheduled attempt is not proof of successful authoritative values.
- The PowerShell orchestrator still discovers project paths and binaries through filesystem conventions rather than a neutral Facility manifest.
- Git clone/pull and pip installation occur dynamically without immutable commit/package hashes in the script.
- Vendor reads can expose highly sensitive device identifiers and require strict private evidence classification.
- MTKClient includes destructive flash/erase/exploit operations far beyond the safe read-only handoff.
- FUSE and raw read/write operations need exact partition/LUN bounds and provider isolation.
- Device connection loss, mode transitions and USB re-enumeration require stronger operation/epoch correlation.
- No root licence exists for the sanitized handoff; MTKClient's GPL-3.0 licence constrains source reuse/distribution.

## What Ptah should reuse or adapt

- separate Boot-to-Mode and Attach/Read Facilities;
- exact USB VID/PID/mode/COM transport evidence;
- target/chip/modem/database inventory as typed read receipts;
- loader/APDB/MDDB/profile compatibility records;
- read-only default and destructive-capability separation;
- per-mode audit folders/records, timeouts and structured summaries;
- public sanitization/redaction discipline;
- explicit unresolved/unsupported result codes;
- MTKClient as a replaceable GPL service/CLI backend for appropriate read/GPT/partition operations;
- exact V6/preloader/BROM/DA/META capability reporting.

## What Ptah must not inherit

- PID_2007 presence described as successful META service execution.
- mtkclient-meta-mode described as the proven D4 read path.
- write/erase/reset/unlock operations mixed into the default analysis/read interface.
- vendor DLL/APDB/MDDB redistribution without rights/provenance review.
- dynamic unpinned Git/pip updates during a trusted operation.
- device identifiers emitted to public logs/telemetry.
- project-local path conventions as public contracts.
- automatic retries of non-idempotent physical operations.
- GPL source copied into permissive Ptah Core without a deliberate licence-compatible boundary.
- failed NVRAM identifier getters described as working.

## Classification

**ADAPT THE READ-ONLY SESSION, MODE/PROFILE, AUDIT AND SAFETY CONTRACTS; HOST MTKCLIENT/VENDOR BACKENDS AS SEPARATE FACILITIES; CONTINUE NATIVE CONNECTOR RESEARCH.**

This is strong internal evidence for `FW-002`, firmware-side `DEVICE-001`, `CORE-004`, `RELAY-002`, `OBS-001` and `PROV-001`.

## Native Ptah completion required

- MediaTek device/profile/SoC/mode/loader schema;
- transport→boot mode→service session→read/write proof levels;
- APDB/MDDB/loader Object identity, digests, provenance and compatibility;
- scatter/GPT/partition/LUN/region relationships;
- target/chip/modem/database inventory receipts;
- sensitive-field classification/redaction;
- read/write/erase/reset/unlock operation classes and retry policy;
- read-before-write backup/checkpoint and post-write read-back verification;
- USB connection epoch/re-enumeration correlation;
- provider-neutral timeouts/cancellation/recovery;
- GPL/vendor binary Facility packaging and exit strategy;
- unresolved MD/NVRAM service state and result-code taxonomy;
- static firmware package analysis independent of device connection.

## Validation inherited into Ptah

1. Boot one supported device to META and prove PID/mode separately from service-session attach.
2. Read target/chip/modem/database inventory through a read-only session and retain exact backend/profile versions.
3. Reject an incompatible loader/APDB/MDDB/profile before device mutation.
4. Disconnect/re-enumerate USB mid-operation and reject stale receipts from the prior connection epoch.
5. Timeout/crash one native backend while preserving audit evidence and unrelated Ptah Activities.
6. Prove no write/reset/erase/unlock command is reachable from the read-only capability set.
7. Keep identifiers private/redacted while retaining verifiable proof references.
8. Read GPT/partitions through an optional backend and register immutable backup Objects before any authorized write.
9. Preserve the unresolved NVRAM connector/result state honestly until live proof closes it.
10. Replace MTKClient/vendor DLL backend without changing Ptah device/profile/operation/receipt contracts.
