# Donor Record — MTKClient

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY MTK FLASH/GPT/PARTITION BACKEND CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/bkerler/mtkclient
- Default branch: `main`
- Pinned commit: `a6a7147e92907b2017027ae404b84101444ee502`
- Licence: GPL-3.0
- Activity: Active
- Classification: MediaTek BROM/Preloader/DA, GPT, flash, memory and device-configuration backend
- Ptah targets: device/profile/mode inventory, GPT/partition reads, full-flash backups, loaders/preloaders, raw offset operations, FUSE views and carefully gated write/erase operations

## Files/components inspected

- `README.md`
- `README-USAGE.md`
- `LICENSE`
- `mtkclient/Library/DA/mtk_da_handler.py`
- search-located DA loader/config, BROM config, preloader and xflash libraries

## Verified capabilities and patterns

### Connection and compatibility

- Supports Windows, Linux and macOS paths with different driver/kernel requirements.
- Distinguishes BROM, Preloader, DA, stock and exploit-backed operation paths.
- Newer V6 chipsets such as MT6781/MT6789/MT6855/MT6886/MT6895/MT6983/MT8985 require a proper V6 loader and Preloader mode rather than classic BROM assumptions.
- Chip details/configuration and USB VID/PID detection are explicit configuration surfaces.
- Loader, preloader, auth, certificate, VID/PID/interface, DA mode, storage part type, pagesize/sector behavior and exploit settings are caller-configurable.
- Device protection state includes SBC/SLA/DAA and may lead to stock-loader or exploit/bypass paths.

### Read and inventory

- Reads individual partitions, all partitions, full flash, boot1/boot2 areas, sectors and arbitrary offsets.
- Reads/dumps preloader, BROM, eFuses, RPMB and selected memory/key material through appropriate modes.
- Prints/exports GPT and backup GPT.
- Can mount exposed flash through a FUSE-like filesystem path.
- GUI supports basic partition/full-flash dumping.
- DA handler maps GPT entries to exact sector/page ranges for partition reads.
- Preloader RAM dumping searches for MTK bootloader headers and can recover a named preloader image.

### Write/mutation breadth

- Writes individual partitions, all partition files, full flash, sectors and arbitrary offsets.
- Erases partitions/sectors.
- Patches vbmeta verification/verity flags.
- Locks/unlocks `seccfg`, performs reset and exposes memory poke/payload/stage operations.
- Handles RPMB writes/key-related actions, although some operations are documented as broken/limited.
- DA handler performs direct read-modify-write on vbmeta and raw partition writes.

### State and tooling

- Can run command scripts/multi-command sequences.
- Writes/reuses DA state for reinitialization.
- Supports debug logs and progress output.
- Includes loaders, device configuration and exploit/payload machinery.

## What MTKClient completes

- A mature open-source MTK GPT/partition/full-flash backend.
- Explicit BROM/Preloader/DA/V6/stock/exploit capability dimensions.
- Loader/preloader/device/SoC compatibility requirements.
- Read-only backup and GPT inventory foundations missing from the internal D4 META path.
- FUSE/raw offset and memory views for specialist analysis.
- A backend for static device-state backup before authorized writes.
- Completion of internal META work without pretending the two protocols are the same.

## Important limitations for Ptah

- GPL-3.0 requires a separate executable/service or deliberate compatible-licence integration boundary.
- The tool combines safe reads with exploit, bypass, unlock, erase, patch, key extraction and arbitrary memory/payload operations.
- Stock/exploit/loader behavior varies heavily by SoC, device security state and firmware version.
- A loader/preloader with the wrong target can fail or damage the device.
- Bundled/community loaders and payloads require independent provenance, rights, hashes and malware review.
- Device protection bypass/exploit paths are not required for static firmware analysis and must not be enabled by default.
- GPT/partition names alone do not prove compatibility with a package/image intended for another build/device.
- FUSE views and raw memory/flash operations expose sensitive device data.
- RPMB/efuse/key operations may be irreversible or security-sensitive.
- Some operations are explicitly documented as broken or limited.
- State files are backend implementation state, not durable Ptah Activity/session identity.
- Several code paths call `sys.exit`, catch broad exceptions or print human-oriented progress rather than returning typed receipts.
- Read success must still produce content hashes, exact ranges and source-device identity.
- Write success requires post-write read-back; process/log success alone is insufficient.
- Automatic retries are unsafe for erase/write/payload/reset operations.
- Driver/USB mode identity and connection epochs remain critical external dependencies.
- Main branch is not automatically the stable release choice for Phase 0C.

## Must not be inherited

- One capability exposing read, exploit, unlock, erase, patch and arbitrary payload operations together.
- BROM/Preloader/DA/META/stock modes collapsed into one state.
- Loader/preloader filename used as sufficient compatibility/provenance.
- exploit/bypass paths enabled by default.
- GPT partition name alone used to authorize a write.
- full-flash/partition write without immutable backup and caller authorization.
- RPMB/efuse/key operations treated as ordinary retries.
- backend state/GID/path used as Ptah identity.
- raw identifiers/keys/partitions emitted to public logs or telemetry.
- GPL source copied into permissive Ptah Core without licence-compatible design.
- tool exit/log success promoted to verified physical state.

## Integration decision

**WRAP AS THE PRIMARY MTK GPT/PARTITION/FLASH BACKEND THROUGH A SEPARATE GPL FACILITY.**

Ptah should expose narrowly scoped capability sets:

- MTK transport/mode/profile inventory;
- read-only GPT/partition/full-flash backup;
- read-only memory/region views where approved;
- optional stock loader operation;
- separately gated write/erase/reset/unlock/exploit Facilities.

The internal native META path remains a separate read-only service/session Facility. MTKClient does not replace it.

## Native Ptah gap

Ptah must define:

- device/SoC/hwcode/mode/security/storage/profile schema;
- loader/preloader/DA/payload Object identity, hashes, source, licence and compatibility;
- transport→mode→DA/service-session proof levels;
- GPT/backup-GPT/LUN/partition/region relationships;
- full-flash and partition backup Objects with exact offsets/sizes/hashes;
- read/write/erase/reset/unlock/payload/RPMB/efuse operation classes and retry policy;
- read-before-write checkpoint and post-write read-back verification;
- signed caller authorization and device-selection receipt;
- connection epoch/re-enumeration handling;
- sensitive data classification and controlled export;
- typed backend errors/partial states/cancellation/timeouts;
- GPL service packaging, SBOM and stable-release pin;
- static firmware-package/scatter analysis independent of device connection;
- compatibility comparison between selected package/image and observed device profile.

## Exit strategy

Ptah's MTK Device/Firmware contracts remain backend-neutral. Vendor DLL services, MTKClient, custom Rust/native engines or future stock protocols can replace one another without changing Device, GPT, Partition, Operation or Receipt identities.

## Validation required

1. Identify BROM/Preloader/DA/V6 mode and exact device/SoC/security/profile before operation.
2. Read GPT/backup GPT and all selected partitions into immutable hashed Objects.
3. Compare GPT/partition layout with a candidate firmware package before any write.
4. Reject incompatible loader/preloader/DA/payload Objects by exact profile evidence.
5. Disconnect/re-enumerate during read and reject stale backend output through connection epoch.
6. Prove exploit/unlock/erase/write/RPMB/efuse capabilities are unreachable from read-only analysis.
7. Perform one explicitly authorized partition write only after backup, then read back and verify exact digest/range.
8. Preserve partial read evidence after timeout/crash without duplicating completed Objects.
9. Run the GPL backend in an isolated service/container with exact source/SBOM/licence evidence.
10. Replace MTKClient with the internal/vendor backend for one supported read without changing Ptah contracts.
