# Internal Recovery Record — Hunter Runtime, Sync and Outbox

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/hunter`
- Visibility: Private
- Default branch: `master`
- Pinned commit: `cd7c3ce015ad8a5f421b81cb953b13a51c1cc521`
- Licence: No root `LICENSE` file was found at the inspected pin; preserve internal/private status.
- Ptah relevance: local/online separation, safe source synchronization, background tasks, persistent workflows, D1 outbox/retry, local file bridge, process control and graceful optional-component failure.

## Files inspected

- `README.md`
- `docs/HUNTER_CLOUDFLARE_GIT_SOURCE_OF_TRUTH.md`
- `tools/sync_hunter_local_from_github.ps1`
- `cloudflare/hunter-api-worker/src/events_backend_v3/index.ts`
- `cloudflare/hunter-api-worker/src/events_backend_v3/schema.ts`
- `cloudflare/hunter-api-worker/src/events_backend_v3/delivery.ts`
- `task_runner.py`
- `workflow_manager.py`
- `hunter_local_shell_runtime.py`
- `hunter_codeops_switcher_bridge.py`
- relevant imports and runtime boundaries in `controller.py`

## Verified implementation layers

### 1. Source and deployment authority

- GitHub `master` is the tracked-source authority.
- Cloudflare Workers Builds deploys the online Worker from the repository.
- Local runtime memory, secrets, logs, databases, models and machine state remain local-only.
- Local source catch-up is explicit, not automatic.
- The sync script first fetches and reports ahead/behind/dirty state without changing files.
- Apply is allowed only on the expected branch, with a clean worktree, no unpushed local commits and a fast-forward-only update.
- It never force-resets, force-checkouts, auto-stashes or auto-merges divergent history.
- Cloudflare version history is the online rollback path; local source is not blindly rewritten to solve deployment failures.

### 2. In-memory background Task Runner

- `task_runner.py` creates short UUID-derived IDs and runs callables on daemon threads.
- It retains label, status, result, error and start time in a process-local dictionary.
- Success/failure may feed outcome learning.
- Status and list APIs expose process-local state.

This runner is non-blocking but not durable. Restart loses all Task state, daemon threads may terminate with the process, there is no cancellation or progress stream, and success detection partly relies on labels/result text.

### 3. File-backed persistent Workflow Manager

- Workflows use UUID-derived IDs and one JSON state file per Workflow.
- State includes type, label, status, current step, timestamps, parameters, steps, checkpoints, result, error, cancel request, retry-of and resume-of.
- Writes are protected by a process lock and update timestamps.
- Steps are upserted; checkpoints are appended and capped to the most recent forty.
- Running repair Workflows receive `should_cancel` and checkpoint callbacks.
- Retry and resume create new Workflow IDs linked to the earlier Workflow.
- Outcome events are recorded for terminal states including completed, failed, retry recommended, cancelled, waiting and confirmation states.

This is materially stronger than the in-memory Task Runner, but still has limitations: local JSON files, non-atomic direct writes, one-process lock only, daemon-thread execution, no worker lease, no restart pickup of an in-flight thread, no idempotency key and no multi-Node coordinator.

### 4. D1 authoritative Events and transactional outbox pattern

- D1 is authoritative for cases, requests, messages, outbox rows and delivery attempts.
- Requests have a unique idempotency key.
- Outbox rows have a uniqueness constraint across request, purpose, channel and recipient.
- Delivery rows are claimed with a conditional status update to `processing`.
- Every attempt is appended to a delivery-attempts table with provider status, error and response JSON.
- Failed delivery uses bounded exponential-style delay, configurable attempts and a dead state.
- Scheduled processing resets stale `processing` locks older than ten minutes to retry.
- Request status distinguishes fully delivered, partial delivery, pending and failed.
- Missing provider configuration becomes an explicit blocked result rather than a false success.
- Temporary R2 attachments are deleted after successful delivery or later expired; cleanup failure is recorded.
- Status endpoints reveal storage readiness, retry mode and configured channel booleans without exposing secret values.

This is the strongest internal durable-work pattern recovered so far and directly supports Ptah's outbox, idempotency, attempt-history and stale-lease recovery design.

### 5. Local file and process bridge

- Local file root is configurable and paths are resolved beneath it.
- Secret-like files and local-token directories are blocked.
- Tree, read and search operations have explicit item/byte/result limits.
- Generated/cache directories are excluded.
- Local write is explicitly disabled in the first version and redirected to an approval/proof layer.
- Voice process start/stop/status/log functions demonstrate local process discovery, PID/log files and direct process control.
- CodeOps UI bridge shells out to the separate CodeOps CLI, keeping ownership outside the UI.
- Arguments are sanitized before returning error evidence.

## Strong internal patterns for Ptah

1. Different truth domains have different authorities: tracked source, local runtime data and online durable records.
2. Local update is explicit and fast-forward-only; divergence is surfaced rather than overwritten.
3. Optional service/module import failure can degrade a capability while the rest of the controller continues.
4. Durable outbox rows, attempt history and stale-lock recovery are distinct from live process execution.
5. Unique idempotency keys and outbox uniqueness prevent duplicate intake/delivery.
6. Partial delivery, blocked configuration, pending retry and dead delivery are distinct states.
7. Retry policy is bounded and recorded.
8. Checkpoints, retry-of and resume-of relationships are retained.
9. Local file access is rooted, bounded and secret-aware.
10. Writes are separated from read/inspect operations until an approval/proof path exists.
11. UI/bridge code delegates specialist work rather than absorbing its ownership.
12. Online deployment can roll back independently of local runtime state.

## Important limitations

- Three execution systems have inconsistent state models: in-memory Tasks, JSON Workflows and D1 outbox rows.
- The in-memory Task Runner is not durable and has no cancellation, progress, lease or restart recovery.
- File-backed Workflow writes are not transactional/atomic and cannot safely coordinate multiple processes or Nodes.
- Workflow resume/retry starts a new execution from parameters rather than restoring an exact process checkpoint.
- Checkpoint retention is capped without a separate archival Object/Artifact policy.
- D1 outbox claim uses a conditional update but does not show a globally unique lease owner or fencing token.
- Provider delivery itself remains an external side effect and must rely on provider/idempotency behavior where supported.
- D1/R2/KV roles are specific to Hunter deployment and cannot become mandatory public Ptah backends.
- Local controller and file bridge contain Windows/local-path assumptions.
- Voice and CodeOps subprocess bridges are synchronous or process-local and not a general PTY/stream Facility.
- `controller.py` is broad and monolithic, mixing many facilities and UI policies.
- Role/business policy is Hunter-specific and must not enter neutral Ptah Core.

## What Ptah should reuse or adapt

- explicit authority map for source, local state, metadata and Object bytes;
- status-before-apply and fast-forward-only safe sync principles;
- D1 outbox schema concepts: idempotency key, unique delivery intent, claim, attempt history, retry/dead states and stale-lock recovery;
- separate Task, Workflow and delivery-attempt identities;
- retry-of/resume-of relationships;
- rooted, bounded and secret-aware local file APIs;
- capability degradation without total system failure;
- specialist bridge delegation;
- temporary Object lifecycle and cleanup status;
- honest partial/pending/blocked/failed delivery states.

## What Ptah must not inherit

- Hunter, role, Events, provider or private deployment identities in public contracts.
- Process-local dictionaries as Activity truth.
- Direct JSON-file mutation as multi-Node Workflow storage.
- Daemon-thread execution as durable worker infrastructure.
- Result-text heuristics as proof of success.
- Cloudflare D1/R2/KV as mandatory public Ptah implementation.
- A single monolithic controller containing every Facility.
- Automatic source sync or conflict overwrite.
- Retry without an Activity-specific retry class and idempotency receipt.
- Provider HTTP response alone treated as authoritative external completion.

## Classification

**ADAPT OUTBOX, AUTHORITY, CHECKPOINT, SAFE-SYNC AND DEGRADATION PATTERNS; REPLACE THE EXECUTION SUBSTRATE.**

This repository is major internal evidence for `CORE-002`, `CORE-004`, `RELAY-001`, `RELAY-002`, `STORE-002`, `STORE-003`, `SESSION-001`, `SYNC-001`, `OBS-001`, `PROV-001`, `OFFLINE-001` and local file/process Facilities.

## Native Ptah completion required

- one versioned Activity Ledger spanning live and durable execution;
- transactional metadata store and backend adapters;
- atomic state transitions, worker leases and fencing tokens;
- reconnect/restart pickup and exact reconciliation;
- Activity-specific retry/idempotency classes;
- dedicated PTY/Object/display streams;
- Object/Artifact storage and lifecycle references;
- local Node journal/outbox for offline work;
- versioned conflict/revision model rather than Git-only source sync;
- modular Facility processes/services;
- platform-neutral paths and process APIs;
- proof receipts independent of operational telemetry.

## Validation inherited into Ptah

1. Status-only synchronization changes no tracked or mutable Workspace state.
2. Divergence and dirty state are surfaced; no force reset or silent merge occurs.
3. Duplicate intake with one idempotency key produces one durable operation.
4. A stale worker lease is recovered with a fencing token and no duplicate side effect.
5. Every retry attempt is retained; partial/pending/dead remain distinguishable.
6. Optional Facility failure does not stop unrelated safe capabilities.
7. Node/control-plane restart recovers durable Activities, not merely their metadata files.
8. Protected local files cannot be read or emitted through telemetry.
9. Temporary Objects are either cleaned up or left with an explicit cleanup-failed state.
10. Public Ptah backends remain replaceable even when the first deployment uses Cloudflare services.
