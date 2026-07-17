# Donor/Recovery Record — P5C Firmware Format Status

**Phase:** 0A / WP06  
**Status:** UNRESOLVED — PARKED PENDING VERIFIED SAMPLE OR AUTHORITATIVE TOOL EVIDENCE  
**Inspected:** 2026-07-17

## Question

The roadmap previously listed `P5C` as an unresolved firmware format requiring recovery from a verified sample/tool.

## Search performed

- searched public web sources for `.p5c`, P5C firmware, Spreadtrum/Unisoc, UpgradeDownload/ResearchDownload and extractor/parser references;
- searched GitHub/public source results for P5C format/parser code;
- compared results against the PAC/FDL donor composition already inspected.

## What was found

- Several third-party download/tool pages claim some Spreadtrum/Unisoc flash tools can load `.P5C` alongside `.PAC`.
- Other third-party pages explicitly conflict, claiming particular SPD tools support PAC only or referring ambiguously to `PAC5`/`PAC.5C`.
- Commercial-service pages mention PAC, P5C and CPB as possible Spreadtrum firmware packages without publishing a format definition.
- A generic file-extension database labels `.p5c` as unknown binary data and provides no technical structure.
- Search results are polluted by device model names such as “Doopro P5C” and Teclast model codes, which are not evidence of a `.p5c` file format.
- No authoritative Unisoc specification, source implementation, trustworthy header definition, open parser or reproducible sample hash was found.
- No inspected open PAC parser or FDL tool in the current donor set documents `.P5C` support.

## What is **not** established

The current evidence does not establish whether `.P5C` is:

- a distinct Unisoc/Spreadtrum package format;
- a PAC variant/revision;
- an encrypted/signed wrapper;
- a tool-specific container;
- a mislabeled extension;
- a confused reference to a device/model or `PAC5` generation.

No header magic, version fields, table layout, CRC/signature rules, compression/encryption scheme, entry format or tool-version compatibility can be recorded honestly.

## Decision

**PARK P5C FORMAT SUPPORT.**

Ptah must not:

- classify `.p5c` by extension alone;
- route it through the PAC parser silently;
- advertise P5C extraction/flashing support;
- convert or flash an unknown P5C package;
- rely on third-party tool-download pages as format authority.

A `.p5c` input may be registered as an immutable Object and receive generic Tika/Binwalk/libarchive/LIEF detector claims. It remains `unknown_or_unverified_firmware_container` until format evidence closes the gap.

## Reopening criteria

Re-open this requirement only when at least one of the following is available:

1. a legally usable P5C sample with recorded source, device/SoC/model/build and SHA-256;
2. an authoritative Unisoc/vendor tool that loads it plus captured version/log/behavior evidence;
3. a clean-room binary comparison against an equivalent PAC package;
4. a source implementation or technically credible format specification;
5. repeatable header/table/entry extraction from multiple unrelated samples;
6. verification of checksums/signatures/encryption and exact payload boundaries;
7. evidence distinguishing the extension from device/model names and PAC5 terminology.

## Required recovery procedure

When a sample becomes available:

1. preserve and hash the original;
2. record acquisition/provenance and legal handling constraints;
3. run generic detector/entropy/string/embedded-region analysis;
4. compare first/last sectors, tables, strings and payload hashes with PAC/CPB equivalents;
5. observe an authoritative tool loading the package without flashing;
6. capture package inventory and temporary extracted files where legally permitted;
7. derive a bounded parser only after repeated structural confirmation;
8. keep package analysis separate from device flashing;
9. add golden positive/negative/malformed samples and exact compatibility evidence.

## Current requirement status

- `FW-003` Unisoc PAC/FDL can proceed without P5C.
- `.P5C` support is `PARKED`, not required for Ptah v1 design closure.
- The roadmap must retain this record so the gap is not forgotten or falsely closed later.
