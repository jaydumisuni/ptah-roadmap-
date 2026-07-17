# Donor Record — aria2

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — SEGMENTED DOWNLOAD ENGINE DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/aria2/aria2
- Default branch: `master`
- Pinned commit: `9e7273583f83e881e3ec067b523ba88724088d2f`
- Licence: GNU GPL-2.0
- Activity: Active/maintenance development
- Classification: Mature segmented, multi-source and multi-protocol download engine
- Ptah targets: HTTP(S), FTP/SFTP, BitTorrent, Metalink, segmented downloading, daemon/RPC control, persistent sessions and chunk verification

## Files/components inspected

- `README.rst`
- `COPYING`
- manual/source references for JSON-RPC, session input/save, RPC secrets and runtime options
- current Lumi aria2 subprocess integration for comparison

## Verified capabilities and patterns

- Supports HTTP(S), FTP, SFTP, BitTorrent and Metalink.
- Can combine several sources/protocols for one file.
- Metalink chunk checksums allow piece-level validation while downloading.
- Segmented downloads, upload/download throttling and disk cache are built in.
- Supports proxy configuration and authentication, HTTP basic auth, client certificates, CA verification and cookie import/export.
- Supports persistent HTTP connections, IPv6/Happy Eyeballs and asynchronous DNS where built.
- BitTorrent includes DHT, PEX, encryption, multiple trackers, web seeding and selective file download.
- Exposes JSON-RPC over HTTP/WebSocket plus XML-RPC.
- Runs as a daemon and supports configuration files and batch input.
- Session input/save options exist for preserving incomplete downloads across restarts.
- Per-download and global options can be controlled through the engine rather than parsing console text.
- Cross-platform builds exist, including Windows, macOS and Android paths.

## What aria2 completes beyond Lumi

- A stable daemon and JSON-RPC control path instead of human console-output parsing.
- Mature session persistence and engine-owned resumption.
- SFTP and Metalink support.
- Multi-source/protocol download for one Object.
- Chunk-level verification through Metalink/BitTorrent.
- Mature authentication, certificates, cookies, proxy and network options.
- Better separation between engine and UI/product client.

## Important limitations for Ptah

- aria2 is a transfer engine, not Ptah's Activity Ledger, Object catalogue or synchronization authority.
- GPL-2.0 creates a strong code-reuse/distribution boundary; subprocess/RPC use is safer than source extraction but still requires packaging/licence review.
- Session files and GIDs are aria2 implementation state, not durable Ptah identities.
- JSON-RPC exposure requires strong authentication, network binding and origin controls.
- A completed aria2 transfer does not prove the expected Object identity unless digest/remote validators are checked.
- Server content can change between attempts; ETag, Last-Modified, expected size/digest and source identity must be retained by Ptah.
- Chunk verification strength varies by protocol/metadata; ordinary HTTP does not automatically provide trusted chunk hashes.
- aria2 is not an upload protocol, cloud sync engine, backup system or Node-to-Node Object transfer model.
- Torrent/privacy/network policy is caller/operator configuration, not Ptah autonomous policy.
- The project does not provide Ptah proof-level, receipt, Artifact or retention semantics.

## Must not be inherited

- aria2 GID/session state as canonical Ptah Activity identity.
- GPL source copied into Ptah Core without formal licence approval.
- RPC daemon exposed publicly without scoped credentials/TLS/network controls.
- Console-output parsing when JSON-RPC is available.
- Transfer completion promoted to Object verification.
- Remote source changes ignored during resume.
- All protocol options exposed without capability/security classification.
- aria2 configuration files used as public Ptah Transfer contracts.

## Integration decision

**WRAP ARIA2 AS THE PRIMARY SEGMENTED/MULTI-SOURCE DOWNLOAD BACKEND CANDIDATE THROUGH JSON-RPC.**

The Ptah Transfer Facility owns Activity/operation/attempt identity, Object landing, storage roots, receipts, expected remote validators and checksums. aria2 owns suitable protocol transfer mechanics.

Lumi remains an internal product/reference and may migrate from subprocess parsing to the same Ptah/aria2 adapter.

## Native Ptah gap

Ptah must define:

- Transfer request and source/mirror list schema;
- expected size, ETag, Last-Modified, digest and chunk-hash references;
- aria2 GID/session mapping to stable Activity/operation/attempt IDs;
- credential/proxy/certificate/cookie references;
- online deployment SSRF/private-network boundary;
- Workspace/storage-root resolution;
- partial-file Object and resume metadata;
- durable attempt history and retry class;
- per-Activity progress/telemetry and stream events;
- final Object registration and independent verification receipt;
- backend replacement path;
- licensing/package distribution record.

## Exit strategy

Ptah's Transfer contract remains implementable with native HTTP libraries, curl/libcurl, another segmented engine or cloud/provider APIs. aria2 session/GID details remain adapter metadata.

## Validation required

1. Control aria2 through authenticated JSON-RPC rather than console parsing.
2. Interrupt daemon/Node and restore incomplete transfers from session state.
3. Download one Object from several mirrors/protocols and retain source contribution evidence.
4. Verify Metalink/BitTorrent chunks and independently verify final Object digest.
5. Detect ETag/Last-Modified/content-length changes and reject unsafe resume.
6. Exercise proxy, client-certificate and cookie references without exposing secrets.
7. Prove slow/failed mirrors do not corrupt the final Object.
8. Keep transfer progress, completion and Object verification as separate states.
9. Replace aria2 with an alternate backend for one Transfer without changing public identity.
10. Complete GPL packaging/licence review before distributing bundled aria2 binaries.
