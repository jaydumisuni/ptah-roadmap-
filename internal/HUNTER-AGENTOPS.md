# Internal Recovery Record — Hunter AgentOps

**Phase:** 0A / WP02C  
**Status:** FIRST-PASS COMPLETE  
**Inspected:** 2026-07-17

## Identity

- Repository: `jaydumisuni/Hunter-AgentOps`
- Visibility: Private
- Default branch: `main`
- Pinned commit: `bb392ba09dca09217a2538783121b142d2d6d768`
- Licence: No root `LICENSE` file found at the inspected pin; internal/private-use status must be preserved until ownership/licence documentation is added.
- Ptah relevance: operation packets, approvals, evidence ownership, caller/worker boundaries and loop-control patterns.

## Files inspected

- `README.md`
- `hunter_agentops/code_ops_switcher_runner.py`
- `docs/CODE_OPS_SWITCHER_RUNNER_CONTRACT.md`

## Verified implemented behavior

- AgentOps explicitly owns operation state, approval, evidence and loop control while Code Ops owns coding work.
- `CodeOpsOperationPacket` carries a stable `operation_id`, task, client/mode, provider/capability requirements, review route, Workspace path, files, plan and approval state.
- Empty operation IDs/tasks are rejected.
- File paths are constrained to remain relative to the selected Workspace.
- Applying a plan is blocked unless approval state is explicitly `approved`.
- Runner results contain operation ID, sanitized command, return code, payload and evidence.
- Commands are executed with a bounded timeout and stdout/stderr capture.
- Invalid/non-object JSON responses become explicit error payloads.
- Evidence records retain event type, operation ID, success, return code, sanitized command, payload keys and route/file/review outputs.
- Key/token-looking command values are masked in evidence.
- The contract identifies expected route, provider, file-edit and Sergeant evidence records.

## Documented but unfinished

- The runner is not yet wired into the real AgentOps lifecycle.
- Final durable audit/log storage is pending.
- Sergeant verdicts are not yet connected to the correction loop.
- Owner approval policy is not yet connected to the production UI/runtime gates.
- The runner uses synchronous `subprocess.run`, one 120-second timeout and final-output capture rather than streaming, cancellation, checkpoints or durable worker recovery.
- No retry classification, idempotency receipt, worker lease or outbox/reconciliation implementation is present in the inspected adapter.

## Strong internal patterns for Ptah

1. Stable operation ID separate from task text.
2. Caller/orchestrator ownership separate from specialist execution ownership.
3. Approval and evidence are first-class fields rather than hidden control flow.
4. Workspace path confinement is validated before execution.
5. Result and evidence records remain separate.
6. Commands are sanitized before evidence storage.
7. A specialist route can be invoked through a neutral packet without moving specialist ownership into the orchestrator.
8. A result may feed review/correction rather than becoming automatic completion.

## What Ptah should reuse or adapt

- Operation IDs and idempotency linkage in the Activity schema.
- A generic Facility invocation packet carrying required capability, Workspace, inputs, caller references and review/proof expectations.
- Separate execution result, evidence receipt and review verdict references.
- Secret-safe command/result capture.
- Path validation before a Facility receives Workspace-relative inputs.
- Caller-supplied approval/restriction references without embedding private policy into Ptah.

## What Ptah must not inherit

- Hunter, AgentOps, Code Ops, Sergeant or private department names in public Ptah contracts.
- AgentOps approval policy as universal Ptah policy.
- Synchronous subprocess execution as the Activity Runtime.
- A single 120-second timeout as universal lifecycle behavior.
- Final stdout JSON as the only result/evidence channel.
- Operation completion inferred only from process return code.
- Private provider routing or internal operation chains in public documentation.

## Classification

**ADAPT INTERNAL CONTRACT PATTERNS; REBUILD RUNTIME IN PTAH-NATIVE FORM.**

AgentOps is internal evidence for `CORE-002`, `CORE-004`, `EXEC-001`, `PROV-001` and the Activity receipt model. It is not a Ptah dependency.

## Native Ptah completion required

- versioned Activity/Facility request schema;
- idempotency and retry class;
- streaming events and logs;
- cancellation, pause/wait and durable recovery;
- backend-independent receipt schema;
- Object/Artifact references rather than raw result-only payloads;
- Node/Provider/Facility correlation;
- local outbox and replay;
- public-neutral terminology.

## Validation inherited into Ptah

- reject missing operation IDs and Workspace escapes;
- block side-effecting execution without caller-supplied authorization when a caller requires it;
- redact secret-bearing command values;
- preserve evidence on timeout, invalid output and non-zero exit;
- prove specialist execution, evidence and review remain separately addressable.
