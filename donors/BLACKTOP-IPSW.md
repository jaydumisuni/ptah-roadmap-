# Donor Record — blacktop/ipsw

**Phase:** 0A / WP06  
**Status:** FIRST-PASS COMPLETE — PRIMARY APPLE FIRMWARE ANALYSIS CANDIDATE  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/blacktop/ipsw
- Default branch: `master`
- Pinned commit: `c34addaf45f13e4bdcf71c701dd8994a3cb71085`
- Licence: MIT
- Activity: Active
- Classification: Apple IPSW/OTA/macOS firmware catalogue, manifest, extraction, diff and research donor
- Ptah targets: Apple product/build/board identity, BuildManifest/component graph, local/remote package extraction, DMGs/cryptexes/kernelcache/bootloader/device-tree relationships, encrypted IMG4/AEA states and firmware comparison

## Files/components inspected

- `README.md`
- `LICENSE`
- `pkg/plist/build_manifest.go`
- `pkg/info/info.go`
- `internal/commands/extract/extract.go`
- `cmd/ipsw/cmd/download/download_ipsw.go`
- `internal/download/downloader.go`
- search-located TSS, diff and extraction boundaries

## Verified capabilities and patterns

### Firmware catalogue and package operations

- Downloads and analyzes IPSW, OTA, macOS installer, Xcode, KDK and related Apple packages from several sources.
- Supports extract, diff, mount and metadata operations.
- Local and remote ZIP/IPSW access paths exist; remote readers can inspect/extract selected members without always downloading the full package first.
- Download filters include product identifier, board/model, version and build.
- Resumable `.download` files are supported when servers advertise byte ranges.
- Expected SHA-1 values are verified before atomic rename/finalization unless explicitly disabled.
- Checksum mismatch retains the partial/downloaded file and returns an explicit failure.

### Apple build and compatibility model

- `BuildManifest` models product version, build version, manifest version, supported product types and multiple Build Identities.
- Each Build Identity records application board/chip/security domain/product/target fields, baseband identity/security fields, unique build identity, restore information and a named component manifest.
- Component manifest entries can carry path, digest, build string, trust/production/development state, payload hashes, raw-data digests, personalization and restore-request rules.
- Device/board information can be combined with DeviceTree and processor data.
- Package info exposes product/build/OS plus supported device/product/board/CPU and component paths.
- Helpers identify kernelcaches, bootloaders, filesystem DMGs, SystemOS/AppOS/RosettaOS/ExclaveOS cryptexes and restore ramdisks.
- OTA metadata can record prerequisite build, restore version and Rapid Security Response-like state.

### Extraction and encryption

- Extraction targets include kernelcache, dyld shared caches, DMGs, IMG4/IMG3 payloads, iBoot, SEP and other firmware components.
- Config separates local IPSW and remote URL input, output directory, pattern, device identity selector, architectures, DMG type, JSON output and decryption-key sources.
- Firmware keys can be supplied by the caller or looked up from The Apple Wiki.
- Encrypted IM4P/IMG3 payloads are matched to filenames and decrypted only when known IV/key or KBAG material exists.
- Missing keys remain explicit rather than being represented as successful decryption.
- AEA encrypted archives and caller-supplied/private-key database paths are represented separately.

### Broader research/runtime surface

- Includes Mach-O, dyld shared cache, kernelcache, IMG4, iBoot, SEP and co-processor analysis.
- Includes code-signing/entitlement, binary patching, device interaction, backup/restore, SSH/Frida, App Store Connect and optional AI-assisted decompilation features.
- CLI and REST daemon boundaries exist.
- SQLite and PostgreSQL storage options exist.

## What blacktop/ipsw completes

- The Apple BuildManifest/product/board/component graph absent from the internal Apple tools.
- Local and remote package inspection/extraction.
- Apple-specific component and encrypted-payload parsing.
- Firmware-to-device/build compatibility evidence.
- IPSW/OTA comparison and selected component extraction.
- A mature Apple research backend that can remain a replaceable Facility.
- A direct completion path for internal ramdisk/tool compatibility tables.

## Important limitations for Ptah

- `ipsw` is a broad security-research/device-management framework, not a neutral Apple Firmware Domain Pack by itself.
- Device interaction, binary patching, jailbreak/debugging and App Store operations must not be enabled through the default static-analysis capability.
- The README acknowledges macOS compatibility gaps, resource-intensive operations and incomplete comprehensive testing across firmware variants.
- Main-branch development is not the stable release choice for Phase 0C.
- Remote URL/proxy/insecure TLS options require Ptah network/credential policy and receipts.
- SHA-1 is catalogue compatibility evidence, not Ptah's preferred immutable Object identity; Ptah must also compute a stronger qualified digest.
- `--ignore-sha1` weakens download verification and must produce an explicit degraded/unverified state.
- Resumption uses size/range state; Ptah must also retain ETag/version/source identity to reject changed remote content safely.
- Download locking is not active in the inspected code, so concurrent writers need Ptah-owned leases/path isolation.
- Remote key lookup and firmware-key databases are third-party claims requiring source/version/privacy records.
- Decryption keys and Apple private-key databases are sensitive credential Objects and must not enter logs/telemetry/public records.
- Extraction can remove the encrypted file after decryption; Ptah must preserve the immutable encrypted original and create a separate decrypted child.
- Extracted paths/files are tool outputs until Ptah registers hashes and relationships.
- BuildManifest `Trusted` or signature fields do not automatically establish current Apple signing/restore eligibility.
- TSS/SHSH/APTicket and SEP/baseband compatibility require separate authoritative and time-sensitive checks.
- Mounting DMGs/filesystems has host/platform and malicious-image risks.
- Apple licence/export/payload rights remain separate from the tool's MIT licence.
- Optional AI analysis is outside Ptah's world/runtime identity and cannot become required.

## Must not be inherited

- One giant Apple Facility exposing static analysis, patching, device restore, jailbreak, SSH and App Store operations together.
- SHA-1-only Object identity.
- `--ignore-sha1` treated as normal verified download.
- decrypted output replacing/removing the preserved encrypted original.
- mutable URLs, filenames or tool output paths used as canonical identity.
- third-party firmware keys treated as authoritative without provenance.
- device/build compatibility inferred only from marketing product name.
- BuildManifest trust flags promoted to live signing/restore eligibility.
- remote extraction or mount operations without budgets, source validators and isolation.
- `--insecure` TLS use without explicit caller/deployment authorization and receipt.
- main-branch or optional research dependencies selected without stable-release/SBOM/licence review.

## Integration decision

**ADOPT AS THE PRIMARY APPLE FIRMWARE ANALYSIS BACKEND CANDIDATE, BEHIND A PTAH APPLE FIRMWARE DOMAIN PACK.**

Ptah should initially invoke pinned `ipsw` CLI/library/daemon operations in bounded providers and map their outputs into native Objects, detector claims, compatibility records and receipts.

The default public capability set should be read-only/static:

- catalogue and download metadata;
- package/manifest inventory;
- component extraction;
- metadata/signature/encryption state;
- diff/comparison;
- read-only mounted views where supported.

Device interaction, patching, decryption-key acquisition, restore, TSS and jailbreak/debug operations require separate Facilities and caller-authorized Activities.

## Native Ptah gap

Ptah must define:

- Apple product/build/board/chip/security-domain schema;
- IPSW/OTA/package Object and source-catalogue records;
- Build Identity and component relationship schema;
- component path, size, digest, role, trust, personalization and restore-rule records;
- kernelcache/bootloader/DeviceTree/SEP/baseband/cryptex/DMG/filesystem relationships;
- encrypted/credential-required/decrypted-child states;
- strong content digest plus source SHA-1 claim;
- remote source URL/ETag/Last-Modified/catalogue identity and resumable transfer receipts;
- exact `ipsw` release/build/features/configuration receipt;
- mount/extraction budgets and provider isolation;
- TSS/signing/restore-eligibility record separate from static manifest trust;
- ramdisk/tool asset links to exact product/board/build/components;
- device-operation capability separation and read-before-write backup rules;
- stable-release selection, SBOM and optional-dependency review.

## Exit strategy

Ptah's Apple Firmware Domain Pack remains implementable with `ipsw`, libipsw/libimobiledevice tooling, Apple plist/IMG4/DMG parsers or specialist services. Apple Object/component identities and receipts remain backend-neutral.

## Validation required

1. Download one IPSW and one OTA with source metadata, resume support, SHA-1 compatibility verification and independent SHA-256 Object identity.
2. Reject changed remote content during resume using source validators.
3. Parse BuildManifest and map every Build Identity/component to exact product/board/build relationships.
4. Extract kernelcache, DeviceTree, bootloaders, restore ramdisk, filesystem/cryptex and SEP/baseband components while preserving encrypted originals.
5. Handle missing/unknown decryption keys as explicit locked states.
6. Compare two builds and retain component-level added/removed/changed digest evidence.
7. Mount/open a filesystem image read-only in an isolated provider and register files without host escape.
8. Compare internal ramdisk compatibility records against exact BuildManifest/device evidence.
9. Prove static analysis works without connected devices, exploitation, restore or App Store credentials.
10. Keep TSS/current signing eligibility separate from package metadata and test time-sensitive authoritative lookup independently.
11. Disable optional AI/device/patching capabilities in the hardened firmware-analysis worker.
12. Replace `ipsw` for one component parser without changing Ptah Apple schemas or Object identity.
