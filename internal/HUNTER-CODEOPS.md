# Internal Recovery Record — Hunter CodeOps

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/hunter-codeops`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `10a88608fd8e1aa8d09f320a0f90dcb01bd1b665`
- Licence: No root `LICENSE` file was found at the inspected pin; preserve internal/private status until documented.
- Ptah relevance: capability-aware routing, stable client bridge, credential references, controlled file edits, backups, audit events and review-result loops.

## Files inspected

- `README.md`
- `hunter_codeops/code_ops_switcher.py`
- `hunter_codeops/code_ops_bridge.py`
- `hunter_codeops/code_ops_provider.py`
- `hunter_codeops/code_ops_file_edit.py`
- `hunter_codeops/code_ops_sergeant.py`
- `hunter_codeops/code_ops_sergeant_ingest.py`

## Verified implemented behavior

### Capability and route model

- Provider routes declare ID, kind, model, priority, endpoint, enabled/local state, credential environment reference, capabilities and notes.
- Client routes declare stable IDs and interface kinds.
- Session requests include task, client kind, mode, optional provider selector, required capability and review preference.
- Route selection filters by enabled state, provider ID/kind and required capability, then selects by priority.
- Audit events retain route, client, mode, review requirement, reason, locality and capability list without secret values.
- Inline secret-looking keys are rejected from config; only credential environment-variable names are permitted.
- Terminal/UI/editor clients use one bridge response containing route, audit event, environment package and message.

### Provider execution

- The first provider helper calls an owner-configured OpenAI-compatible endpoint.
- API tokens are read from named environment variables and excluded from audit output.
- Missing endpoint, missing credential, transport failure, invalid JSON and missing response content become explicit errors.
- Provider execution output and audit metadata are separate.

### Controlled file edits

- File edits use explicit WRITE, REPLACE and DELETE operations.
- Plans support required/optional operations, reason and review-required flag.
- Dry run is the default.
- Absolute paths and Workspace escapes are rejected.
- Replace requires exact old text and only replaces one occurrence.
- Existing targets are backed up before write/replace/delete when apply mode is used.
- Result items retain path, action, changed state and message.
- Audit retains dry-run state, operation count, changed count, review requirement and paths.

### Review loop

- Sergeant invocation is represented as a command packet rather than hidden direct coupling.
- Review file paths are validated as Workspace-relative.
- Sergeant results are ingested into PASS, NEEDS WORK, BLOCK or UNKNOWN.
- NEEDS WORK, BLOCK and UNKNOWN explicitly require a loop; BLOCK is distinct.
- Audit output records verdict, loop need, block state and summary.

## Strong internal patterns for Ptah

1. Required capability is a first-class route selector.
2. Provider/client routing and physical execution are separate phases.
3. Public/stable bridge shape remains independent from internal modules.
4. Credential references are names, not stored secrets.
5. Dry-run and apply are separate Activity modes.
6. Workspace path confinement precedes modification.
7. Backups are created before side-effecting edits.
8. Result, audit evidence and review verdict are separate records.
9. UNKNOWN review output does not silently pass.
10. Evidence may include terminal output, files, commits, tests, logs, screenshots, archives and API responses, with different strengths.

## Important limitations

- Routing is currently deterministic priority selection rather than load/cost/health/quality-aware scheduling.
- Provider execution is one synchronous request with no streaming, cancellation, retry class or durable Activity state.
- File edits are not transactional across the full plan; an error after earlier operations can leave partial applied state.
- Backup storage uses `.hunter-codeops-backups/latest`, replacing the previous backup rather than durable versioned snapshots.
- File audit records paths but not before/after content hashes, Object IDs or patch artifacts.
- Route/session requests do not carry stable Ptah Activity/operation IDs in the inspected module itself; AgentOps wraps them externally.
- Sergeant ingestion accepts flexible text/JSON verdict discovery and does not verify result provenance, correlation nonce, schema version or signature.
- Client/environment variables are Hunter-specific and cannot become public Ptah contracts.
- Provider response `raw` may contain sensitive or large data and needs explicit storage/redaction rules.

## What Ptah should reuse or adapt

- Facility capability manifests and capability-based placement.
- Separation of route selection, execution, result, evidence and review.
- Credential-reference pattern.
- Stable generic client bridge.
- Dry-run/apply and caller approval references.
- Workspace-relative safe path resolution.
- Versioned backups/snapshots before mutation.
- Explicit review-loop outcomes including UNKNOWN.
- Evidence-strength and source-type classification.

## What Ptah must not inherit

- Hunter, CodeOps, provider-model or Sergeant identities in public Ptah contracts.
- Priority-only routing as final scheduler.
- A model/provider route as the definition of a Facility.
- Synchronous one-shot network/process execution as the Activity Runtime.
- `.hunter-codeops-backups/latest` as durable rollback.
- Non-transactional multi-file apply without checkpoint/rollback reporting.
- Unverified flexible verdict ingestion as proof.
- Environment-variable packages as the universal Node/Facility protocol.

## Classification

**ADAPT BRIDGE, CAPABILITY, EDIT-SAFETY AND REVIEW-LOOP PATTERNS; REBUILD AS PTAH-NEUTRAL FACILITIES.**

CodeOps provides internal evidence for `CORE-002`, `CORE-004`, `EXEC-001`, `DIST-001`, `PROV-001`, credential references, snapshots and caller/reviewer loops. It remains a caller/specialist system, not Ptah Core.

## Native Ptah completion required

- stable Activity and operation IDs in every invocation;
- health/load/platform/cost/caller-aware capability placement;
- streamed execution, cancellation and durable recovery;
- transactional or checkpointed multi-object mutations;
- content hashes, Object versions and patch Artifacts;
- versioned rollback snapshots;
- signed/correlated review receipts and schema versions;
- backend-neutral Facility/Provider contracts;
- redaction and Object-storage rules for raw provider output.

## Validation inherited into Ptah

- route only to a Facility that advertises the required capability;
- reject inline secrets and missing credential references;
- dry-run creates no mutation;
- apply cannot escape Workspace and produces before/after hashes plus rollback reference;
- partial-plan failure is explicit and recoverable;
- review verdict is correlated to the exact Activity checkpoint;
- UNKNOWN or unverified review never becomes PASS;
- routing and review systems can be removed without changing Ptah Activity/Object contracts.
