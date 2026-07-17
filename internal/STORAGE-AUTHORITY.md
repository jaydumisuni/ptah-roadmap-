# Internal Recovery Record — Storage Authority and Recovery Roles

**Phase:** 0A / WP04  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Sources considered

- `jaydumisuni/hunter` at `cd7c3ce015ad8a5f421b81cb953b13a51c1cc521`
  - `docs/HUNTER_CLOUDFLARE_GIT_SOURCE_OF_TRUTH.md`
  - `tools/sync_hunter_local_from_github.ps1`
  - `cloudflare/hunter-api-worker/src/events_backend_v3/schema.ts`
  - `cloudflare/hunter-api-worker/src/events_backend_v3/delivery.ts`
  - local file/process and Workflow implementations recovered in `internal/HUNTER-RUNTIME-SYNC.md`
- Accepted ecosystem storage decision indexed as `D-009` in `DECISIONS.md`
- Existing Ptah Build/Artifact and Session decisions through ADR-0005

## Recovered authority map

### Git/version control

- Tracked source and reviewable repository documentation use Git/GitHub as source history.
- Local source update is status-first, explicit and fast-forward-only.
- Dirty, ahead or divergent state is surfaced rather than overwritten.
- Git rollback/deployment history is separate from local runtime data rollback.

### Hot local storage

- Runtime memory, databases, models, logs, build caches, temporary workspaces, mounted filesystems and active Project files remain local to the machine performing work.
- Local file access is rooted, bounded and secret-aware.
- Generated/cache directories are distinguished from source.
- Software Builder rules keep shared SDKs/caches/toolchains outside individual Project repositories.

### Shared durable metadata

- Hunter Events V3 uses D1 as authoritative metadata for cases, requests, messages, outbox records and delivery attempts.
- Unique idempotency keys, conditional claim transitions, attempt history, retry/dead states and stale-lock recovery are implemented.
- This demonstrates that durable metadata/state and large file bytes should remain separate.

### Durable Object/file bytes

- R2 is used for temporary uploaded attachments in the inspected Events path.
- Object keys and cleanup state are referenced from durable metadata.
- Successful delivery attempts trigger cleanup; failed cleanup remains explicit for later expiry.
- This demonstrates Object bytes with metadata references and independent lifecycle rather than embedding large bytes in D1.

### Local recovery and checkpoints

- Hunter Workflow Manager stores file-backed Workflow states/checkpoints and retry/resume relationships.
- This proves the need for local recovery state but also demonstrates the limits of direct JSON files for multi-process/multi-Node truth.
- Local source and runtime state are intentionally not overwritten by online deployment rollback.

### Google Drive

- Accepted ecosystem architecture assigns Drive to human-readable export/recovery copies rather than active source, build, database, cache or container storage.
- The inspected Hunter code pass did not establish a universal Drive sync engine; Drive integration remains an adapter requirement, not an already proven implementation.

## Strong internal rules for Ptah

1. Every data class has an explicit authority; there is no single universal storage truth.
2. Source history, active Workspace bytes, durable metadata, durable Object bytes, cache and recovery copies remain separate classes.
3. Source/local divergence is surfaced, never force-resolved automatically.
4. Large bytes stay outside metadata databases and workflow/event histories.
5. Temporary Objects have explicit cleanup state and lifecycle receipts.
6. Optional storage/provider failure degrades only dependent capabilities when safe.
7. Provider configuration/secrets remain references, not stored file contents.
8. Google Drive is export/recovery, not a live execution filesystem.
9. Cache and generated temporary files are disposable and never the only copy of truth.
10. Online rollback and local runtime rollback are separate operations.

## Important gaps

- D1, R2 and local JSON implementations are deployment-specific and cannot become mandatory public Ptah backends.
- There is no universal content-addressed Object catalogue across local/R2/Drive/OCI locations.
- Mutable Workspace revisions and conflicts are not yet modeled generally.
- Local Workflow files are not transactional or multi-Node safe.
- R2 attachment cleanup is not a full retention/replication/repair system.
- Drive export/import and recovery verification are not yet implemented as a neutral Ptah Facility.
- There is no generic backup recipe, encrypted repository or restore-drill record in Hunter.
- No universal storage-health state or location-repair workflow exists.
- Source Git sync cannot substitute for arbitrary binary/Object synchronization.

## What Ptah should retain

- explicit authority and storage-class mapping;
- local-first active execution;
- SQL metadata separate from Object bytes;
- Object keys/locations referenced from metadata;
- safe status-first source synchronization;
- temporary Object cleanup states;
- retry/outbox state for provider transfers;
- Drive as export/recovery;
- replaceable Cloudflare deployment adapters;
- honest degraded/partial states.

## What Ptah must not inherit

- Cloudflare D1/R2/KV as universal public requirements.
- Local JSON files as shared catalogue truth.
- Git fast-forward rules used as the conflict model for all mutable Objects.
- Temporary attachment handling treated as a complete Object-storage subsystem.
- Drive folders used as active Workspaces.
- Provider-specific Object keys exposed as canonical Object IDs.
- Failed cleanup hidden or retried without receipts.

## Classification

**ADAPT AUTHORITY, LAYERING, OUTBOX AND SAFE-SYNC RULES; BUILD A NATIVE BACKEND-NEUTRAL STORAGE FABRIC.**

This record informs `STORE-001` through `STORE-005`, `SYNC-001`, `SESSION-001`, `OFFLINE-001` and the Object-storage portion of `CORE-003`.

## Validation inherited into Ptah

- loss of one storage location does not change Object identity;
- local active work continues during optional cloud/Drive outage where dependencies permit;
- metadata never claims bytes are durable until location verification succeeds;
- failed temporary cleanup remains visible and recoverable;
- source/local divergence is surfaced without force overwrite;
- Drive export is restorable but never used as the live Build/DB filesystem;
- public Ptah can switch from D1/R2 to other SQL/S3-compatible backends without schema identity changes.
