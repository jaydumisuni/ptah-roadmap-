# Internal Recovery Record — Lumi Download Manager

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE — SUBSTANTIAL TRANSFER IMPLEMENTATION  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/lumi-dm`
- Visibility: Public
- Default branch: `main`
- Pinned commit: `6a79ecaa045980236d211e44b152c01d50598fc4`
- Licence: No root `LICENSE` file was found at the inspected pin. Code must not be extracted into public Ptah until ownership/licence is documented.
- Ptah relevance: HTTP/FTP/torrent/video intake, segmented downloads, aria2 integration, persistence, pause/resume/cancel, checksum verification, browser handoff and cross-platform client surfaces.

## Files inspected

- `README.md`
- `server.py`
- `core/engine.py`
- API routes, state loading/saving and download workers

## Verified implemented behavior

### Unified transfer surfaces

- Flask API and web UI expose capabilities and download management.
- Entry points exist for HTTP/HTTPS/FTP, magnet/torrent and video platforms.
- Browser extension, Electron desktop wrapper and Android/iOS project scaffolds are present at repository level.
- Video formats are inspected through `yt-dlp`; FFmpeg is discovered for merged video/audio output.
- Torrent support selects libtorrent or aria2c when available.

### Concurrency and scheduling

- Global concurrent-download limit is controlled by a semaphore and can be changed at runtime.
- Per-download segment/connection count is configurable up to a bounded maximum.
- Network receive/transmit statistics and periodic connection-capacity probing run in background threads.
- Capacity probes avoid running while downloads are active where possible.
- Pause all, resume all and cancel all are exposed.

### HTTP download engine

- Prefers bundled/system aria2c as a fast path.
- aria2c is configured for parallel connections, resume, retries, timeouts, disk cache and speed limits.
- If aria2c fails, the engine probes content length/range support and falls back to native Python transfer.
- Native parallel mode preallocates one `.part` file and writes independent byte ranges into it.
- A shared HTTP session and connection pool are used across segments.
- Single-connection mode resumes from an existing partial file when supported.
- Disk-free-space checks occur before known-size downloads.
- Content-Disposition filename recovery and auto-renaming avoid overwriting existing files by default.
- Partial files are retained for resumable work unless delete/cancel paths remove them explicitly.

### Job lifecycle and persistence

- Jobs have IDs, type, URL, target, status, progress, total/downloaded bytes, speed, error and timestamps.
- Pause, resume, cancel, retry, delete and checksum verification are implemented.
- State is saved to JSON using temporary-file replacement.
- On restart, running/probing/queued/pausing/cancelling jobs are converted to paused so the user can resume.
- Staged downloads allow probe/preview and user confirmation before execution.
- Duplicate staged URLs return the existing staged job.
- Staged jobs expire after a configured period.
- Settings use temporary-file replacement and include concurrency, connections and completion actions.

### Verification and outcomes

- Completed files can be verified with caller-selected hash algorithms such as SHA-256.
- Checksum result records expected and actual digest plus match/mismatch state.
- Download success, failure, pause and cancellation are explicit states.
- aria2 subprocess progress is parsed into byte, percentage and speed updates.
- Post-completion actions include none, sleep, shutdown or restart.

## Strong internal patterns for Ptah

1. One Transfer Facility can route several protocols to specialized engines.
2. Capability discovery should report optional engine availability.
3. Segmented transfer, ordinary resume and torrent/video work need different adapters behind one job model.
4. Partial files survive interruption and become resumable state.
5. Intake can be staged for confirmation before execution.
6. Large transfers run in background and expose independent status/progress.
7. A mature external engine may be preferred with a native fallback.
8. Completion and checksum verification remain separate states.
9. Settings and job state use atomic replacement rather than direct overwrite.
10. Existing files are not overwritten silently.
11. Disk capacity and download concurrency are operational inputs.
12. Download Manager product surfaces can remain separate while a neutral engine is extracted/wrapped.

## Important limitations

- Most runtime state remains an in-memory dictionary with process-local locks and daemon threads.
- JSON persistence is not transactional, multi-process or multi-Node safe.
- Restart changes active jobs to paused but does not preserve exact segment/task/thread state.
- Retry deletes the old job record and creates a new ID without a durable retry-of relationship.
- There is no stable Ptah Activity/operation/idempotency identity or attempt history.
- Worker threads have no lease/fencing token, durable queue or control-plane recovery.
- Several exception handlers silently ignore persistence/settings/probe failures.
- Target paths are caller-supplied and need a stronger Workspace-root/storage-class policy.
- URL intake has no comprehensive SSRF/private-network policy boundary for online multi-user deployment.
- TLS/proxy/certificate/authentication handling is not a neutral credential-reference model.
- aria2 progress is parsed from human-oriented console text rather than JSON-RPC/event APIs.
- Pausing aria2 terminates the subprocess and depends on `.aria2`/partial state rather than a retained engine session.
- Native segmented transfer needs stronger validation of server range behavior, ETag/Last-Modified changes and segment integrity.
- A completed byte count does not automatically verify the expected remote identity or checksum.
- Torrent/video engine state and metadata are not represented as durable child Objects/Artifacts.
- Completion actions can shut down/restart the host and must remain caller/operator configuration, not ordinary Ptah Transfer defaults.
- Global network statistics include all host traffic rather than per-Activity resource accounting.
- Product UI, Flask server and engine are tightly coupled.
- No root licence was found.

## What Ptah should reuse or adapt

- protocol-routing and capability-discovery concepts;
- staged intake and user-confirmed parameters;
- aria2/yt-dlp/libtorrent/FFmpeg adapter boundaries;
- segmented/resumable transfer behavior;
- `.part`/partial-state preservation;
- pause/resume/cancel/retry/checksum state distinctions;
- filename collision handling and disk-capacity checks;
- background progress and concurrency controls;
- separate Transfer result and checksum-verification receipts;
- browser handoff and cross-platform client requirements.

## What Ptah must not inherit

- Lumi product identity/UI in public Ptah Core.
- Process-local dictionary/threads as durable Activity truth.
- JSON files as shared metadata catalogue.
- Console-output parsing as the preferred aria2 integration.
- Silent exception swallowing.
- Retry without a linked operation/attempt chain.
- Caller paths outside approved Workspace/storage roots.
- Host shutdown/restart as an unrestricted Transfer completion action.
- Completed bytes treated as verified Object identity.
- One-machine/global network statistics as per-Activity accounting.
- Unlicensed source extraction.

## Classification

**EXTRACT REQUIREMENTS AND ADAPTER PATTERNS; WRAP MATURE ENGINES; REBUILD DURABLE PTAH TRANSFER CORE.**

Lumi is substantial internal evidence for `XFER-002`, parts of `XFER-001`, `CORE-002`, `STORE-001`, `STORE-004`, `OBS-001` and browser handoff. It remains a product/client while Ptah owns the neutral Transfer Facility.

## Native Ptah completion required

- Activity/operation/attempt/idempotency identities;
- durable Transfer ledger, queue, leases and restart recovery;
- Object intake/landing and storage-location records;
- streaming content hash and remote identity validators such as ETag/Last-Modified;
- per-segment integrity and changed-source detection;
- JSON-RPC/native engine adapters instead of console parsing where possible;
- credential/proxy/certificate references and online SSRF boundary;
- Workspace/storage-class path resolution;
- retry-of/resume-of and attempt history;
- per-Activity telemetry/resource accounting;
- Node-to-Node and object-store transport;
- torrent/video child Object/Artifact graph;
- licence and public/private extraction decision.

## Validation inherited into Ptah

1. Interrupt and resume large HTTP transfers without restarting completed ranges.
2. Detect remote content changes during resume and refuse unsafe concatenation.
3. Run several independent transfers while terminal/browser/build Activities remain responsive.
4. Restart control plane and Node, then recover exact Transfer state without duplicate files.
5. Retry creates a linked attempt and preserves earlier failure evidence.
6. Verify final digest separately from transfer completion.
7. Reject path escapes, private-network SSRF and unauthorized credential use according to explicit deployment/caller configuration.
8. Prove aria2 failure falls back safely without corrupting partial state.
9. Preserve torrent/video metadata and outputs as Objects/Artifacts.
10. Replace Lumi/aria2 backend without changing Ptah Transfer or Object identity.
