# Internal Recovery Record — THETECHGUY Node, Worker, Resource and Placement Requirements

**Phase:** 0A / WP11  
**Status:** FIRST-PASS COMPLETE — INTERNAL REQUIREMENTS RECOVERED FOR ISOLATION/PLACEMENT COMPOSITION  
**Inspected:** 2026-07-18

## Purpose

Recover the real THETECHGUY operating constraints that WP11 must preserve before defining Ptah isolation classes, distributed placement, reservations, worker recovery and degraded one-Node behavior.

This record does not introduce a new private scheduler or worker product. It consolidates already inspected internal evidence into the exact WP11 boundary.

## Internal sources recovered

- `internal/TECHGUY-RELAY.md`
- `internal/SOFTWARE-BUILDER.md`
- `internal/HUNTER-RUNTIME-SYNC.md`
- `internal/HUNTER-AGENTOPS.md`
- `internal/MIBU.md`
- `internal/HUNTER-FOREMAN.md`
- `internal/SERGEANT.md`
- `internal/HUNTER-CODEOPS.md`
- `work-packages/PHASE-0A-WP02C-INTERNAL-CORE-RUNTIME-RECOVERY.md`
- accepted ADR-0001, ADR-0003, ADR-0004, ADR-0006 and ADR-0009 boundaries

## Recovered operating position

### Deployment and Node direction

- Ptah must work online first and later on THETECHGUY-owned hardware without changing public identities or contracts.
- A local mini-PC/Node may operate intermittently while the control plane remains online.
- A single Node must remain a complete supported deployment, not a degraded demo that requires a cluster.
- Additional Nodes, GPUs, Windows/macOS hosts, Devices and specialist machines extend capabilities rather than redefine Ptah.
- Stable Node identity must survive reconnect, process restart, address changes and temporary pairing-code expiry.
- Pairing/bootstrap identity, connection identity, connection epoch and durable Node identity are separate.
- Private deployment addresses, credentials and internal topology must not be exposed through public bootstrap or status surfaces.

### Worker and Activity requirements

- Heavy work must run outside the human UI thread.
- Work requires logs, progress, status, cancellation/request-stop and explicit terminal states.
- One failed worker or Facility must not stop unrelated Activities or Workspaces.
- Process-local dictionaries and daemon threads are not durable Activity truth.
- Local JSON workflow files are insufficient for multi-process or multi-Node coordination.
- Durable work needs stable Activity, operation and attempt identities plus retry/resume relationships.
- Worker claims require leases and fencing, not timestamp-only ownership.
- Every retry remains separately addressable and must not silently repeat an external side effect.
- Optional providers/F facilities may degrade independently while safe unrelated capabilities remain available.
- A provider or worker restart creates a new generation and does not authorize replay of prior side effects.

### Resource and capability requirements

- Planning/readiness happens before expensive execution.
- Target selection uses host platform, architecture, available tools, dependency health, runtime capability and blocked reasons.
- Missing tools block only affected targets and name the reason.
- Shared SDKs, caches, package stores, installer machinery and temporary workspaces should not be copied into every Project.
- Shared caches/toolchains and mutable Project Workspaces require separate ownership and integrity controls.
- CPU, RAM, storage, accelerator, attached Device and Facility availability are Node/Provider facts, not caller policy.
- Resource declarations must distinguish configured/logical capacity from measured availability and hard enforced limits.
- Platform compatibility, tool health and exact versions are first-class placement inputs.
- A Build plan/readiness result never proves the Build ran or produced a valid Artifact.

### Storage and data-locality requirements

- Active Workspace bytes prefer fast local storage.
- Immutable Objects, Artifacts, shared caches, provider volumes/snapshots, backups and transfer landing data have different storage classes.
- Provider filesystem state is an execution surface, not universal source truth.
- Large Objects, PTY, display and media streams use separate transports from the Node control protocol.
- Placement must consider whether required Objects, caches, toolchains, models, firmware packages, databases or Device interfaces are already local.
- Moving work to another Node does not silently move credentials, mutable Workspace state or attached physical Devices.
- Source synchronization reports status first and refuses dirty/divergent destructive updates.
- Offline divergence is preserved and reconciled rather than flattened through last-write-wins.

### Credential and network requirements

- Secrets and provider credentials remain opaque references rather than command text, logs, package metadata or public Node capability records.
- Local file access is rooted, bounded and secret-aware.
- Provider/Facility placement must identify which credential references can be delivered to which exact attempt.
- Credential delivery must be revocable and scoped by Workspace, Activity, Facility, Node and time.
- Public host/port resolution without secure identity/tunnel controls is rejected.
- Network availability is a capability, while egress restrictions and permitted destinations come from caller/Workspace/deployment policy.
- Network transport success does not prove the external operation completed.

### Physical Device and scarce-resource requirements

- Physical Devices are scarce, stateful resources requiring explicit leases for control.
- Read-shared observation and exclusive control/maintenance/admin modes remain distinct.
- Every mutating Device operation presents the current fencing token.
- ADB serial, USB path, provider worker ID and connection address are aliases/observations, not stable Device identity.
- Device interfaces carry connection epochs; stale proof from an earlier epoch cannot complete a current operation.
- Multiple-device ambiguity is surfaced unless the caller explicitly selected a target.
- Device/provider loss changes a Session to recovering/expired and never silently transfers ownership.
- Launch, runtime-ready, operation-complete, read-back and authoritative external result are different proof levels.
- Automatic retry is blocked for non-idempotent physical work unless evidence proves the previous attempt did not take effect.

### Evidence, review and authority requirements

- Stable operation ID is separate from task text.
- Activity, operation, attempt, nonce, connection epoch, provider/worker generation and producer version all participate in correlation.
- Result, evidence, review verdict and authoritative external result remain separate.
- Command acceptance, process launch, worker return code, message delivery and log presence are not completion proof.
- Stale, malformed, unsupported or uncorrelated evidence never becomes PASS.
- Existing authoritative results can reconcile a waiting Activity and can prevent accidental repeated physical actions.
- Static/CI proof and physical runtime proof are different authority classes.
- Complete release/Artifact bundles and checksum manifests are contractual.
- Review remains bound to exact Object/checkpoint hashes and does not mutate the underlying Activity automatically.

### Offline and degraded operation

- A disconnected Node requires a local journal/outbox for permitted work.
- Local state must retain operation IDs, attempts, connection epoch, event sequence, produced Object/Artifact references and pending acknowledgements.
- Reconnect negotiates identity/epoch, rejects duplicates, replays retained events and reconciles durable Activity state.
- Optional event, telemetry or provider failures do not automatically stop physical work when required durable state remains safe.
- Loss of required execution or authoritative state produces explicit degraded/recovering/unknown status.
- Local-first one-Node execution must continue when shared/distributed placement machinery is unavailable, subject to capability and policy.
- A cloud or cluster backend is never required merely to run safe local Activities.

## Strong internal patterns to preserve

1. Stable Node, Workspace, Activity, operation, attempt, Device and Object identities remain separate.
2. Node capabilities are observed facts with source/time/generation, not policy.
3. Provider/worker generations and connection epochs fence stale work.
4. Worker claims use leases, expiry and fencing tokens.
5. Heavy work is backgrounded, observable, cancellable and independently recoverable.
6. Shared caches/toolchains are reusable resources with separate integrity and ownership from mutable Workspaces.
7. Missing capabilities produce explicit blocked/degraded reasons.
8. Durable outbox rows, attempt history, retry/dead states and stale-lock recovery are distinct from live execution.
9. Retry policy is Activity-specific and side-effect aware.
10. Large streams and Object transfer remain outside ordinary control/event payloads.
11. Placement considers exact platform/tool/provider/device/object availability.
12. Secret delivery is scoped and never inferred from ambient process environment.
13. Physical Device control uses exclusive leases and proof-level separation.
14. Local one-Node operation and offline journals remain first-class.
15. Provider replacement never changes canonical Ptah identities.

## Internal implementations that must not become Ptah unchanged

- in-memory Node/Task registries as source of truth;
- timestamp-only heartbeat or worker ownership;
- pairing codes as durable authentication;
- direct public host/port resolution;
- daemon threads as durable workers;
- synchronous subprocess calls as universal execution;
- local JSON files as multi-Node transaction state;
- process-local locks as distributed leases;
- one active mission or priority-only routing across all work;
- path/time-derived IDs as canonical identities;
- result text or return code used as proof;
- Windows/local-path assumptions in public contracts;
- shared caches writable by every Workspace without integrity/ownership controls;
- ambient credentials copied into workers or logs;
- automatic source sync, force reset or silent conflict overwrite;
- automatic retry of physical, payment, destructive or external side effects;
- D1/R2/KV, one cloud, one provider or one internal product made mandatory;
- Hunter, AgentOps, Code Ops, Sergeant, MIBU, customer or department names in public schemas;
- a router/model deciding business priority or acceptance inside Ptah Core.

## WP11 classification

**ADAPT INTERNAL NODE/WORKER/LEASE/RESOURCE/DEGRADATION REQUIREMENTS; BUILD PTAH-NATIVE ISOLATION AND PLACEMENT CONTRACTS.**

The internal systems define real operational requirements and failure lessons. They do not supply a reusable distributed scheduler or strong isolation runtime by themselves.

## Native Ptah completion required

- Node capability and observed-resource snapshot identities;
- Provider capability/profile and runtime component-set identities;
- Isolation Class, threat profile and escalation decision;
- Placement Request, Candidate, Decision and rejection-reason records;
- Resource Reservation, Lease, Generation and Fence records;
- worker claim/heartbeat/expiry/reconciliation contract;
- physical versus logical CPU/RAM/disk/network/accelerator accounting;
- hard resource enforcement evidence;
- Object/cache/toolchain/model/device locality records;
- secure network/tunnel and egress policy;
- scoped credential delivery and revocation;
- one-Node local fallback and offline journal;
- multi-Node placement, interruption, rescheduling and data-transfer plans;
- checkpoint capability, Artifact bundle, compatibility and application read-back proof;
- Activity retry/idempotency/side-effect fencing across Node changes;
- Provider/Node drain, upgrade, rollback and removal lifecycle;
- placement explanation, cost/resource accounting and caller-policy references;
- backend replacement and cross-runtime conformance tests.

## Validation inherited into WP11

1. Restart a Node connection without changing durable Node identity and reject stale heartbeats/events from the prior epoch.
2. Kill a worker holding a lease, recover the claim with a new fencing token and prevent the stale worker from committing output.
3. Run two unrelated Activities concurrently; one worker/Facility failure does not stop the other.
4. Block only the target requiring a missing tool/platform/accelerator and retain the exact reason.
5. Share one verified tool/cache Artifact across two Projects without sharing mutable Workspace state.
6. Place work where required Objects/Devices exist or create an explicit transfer/rejection plan.
7. Deliver one credential only to the approved attempt/Facility and prove revocation after completion.
8. Disconnect the Node, continue permitted local work, then reconcile without duplicate side effects.
9. Retry an idempotent operation across Nodes and retain separate attempts under one operation identity.
10. Refuse automatic retry of a non-idempotent physical operation without proof of non-application.
11. Expire a Device/worker lease and prevent stale input or result submission.
12. Preserve launch, runtime-ready, operation-complete, read-back and authoritative-result proof separately.
13. Degrade distributed placement to local one-Node execution without changing Workspace/Activity/Object identity.
14. Replace one runtime/provider implementation while preserving public identities and evidence history.
