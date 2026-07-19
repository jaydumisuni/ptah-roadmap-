# WP09 Consolidated Safety Net

**Status:** CANDIDATE TEST PLAN  
**Catalog:** `urn:ptah:schema-catalog:application:0.1.0`

WP09 is candidate-complete only when the Phase 0B conformance harness can load the package offline, validate all structural and lifecycle records, execute the pinned scenario corpus and prove the semantic invariants below.

## Structural gates

- Parse all WP09 schemas as JSON Schema 2020-12.
- Resolve every `$ref` from local Phase 0B catalogs without network access.
- Require unique absolute schema URNs, schema names, entity kinds and lifecycle-machine names.
- Require the common Entity Envelope and exact registered `entity_kind` in every entity schema.
- Reject unknown top-level fields except through `extensions`.
- Validate lifecycle initial states, transition reachability, authority classes, side-effect flags, evidence requirements and unknown-state policy.
- Verify every lifecycle-bearing schema references an existing namespaced/versioned machine.
- Verify every mutable runtime/control record contains exact Provider/materialization/process/context/page generation, connection epoch or control Lease/fence where required.
- Verify ordinary/public records contain no raw credentials, cookies, secrets, clipboard values or unrestricted private text/screenshots/traces.

## Catalog and identity gates

The active package must contain exactly:

- 51 unique schema entries including shared definitions;
- 18 unique lifecycle machines;
- eight exact dependency catalogs;
- explicit reuse of `runtime.process`, `runtime.lease`, WP05 checkpoint/restore, WP02 execution, WP03 bytes/evidence and WP06 transfer truth.

Reject:

- executable path/package/bundle/PID/window handle/browser target/element handle/panel ID as canonical identity;
- duplicate Process, Lease, checkpoint, transfer or Object identity;
- UI projection or backend handle replacing canonical runtime/source truth.

## Application assertions

- Application identity is stable across Revision/Installation/Provider changes.
- Compatibility is directional, exact-context and expiring.
- install/uninstall acknowledgement is not verified installed/absent state.
- every physical install/launch/repair/uninstall retry uses a new WP02 Attempt.
- Application Session, Process, Window and Display remain separate.
- visible Window and streaming pixels cannot prove application readiness.
- optional display/semantic loss degrades only affected scope.
- checkpoint integrity/compatibility cannot prove functional recovery.
- Recovery Verification binds a new generation and fresh postconditions.

## Browser assertions

- Binary/Profile may persist while Process/Context/Page/Frame generations change.
- writable Profile sharing is Lease/fence controlled and forbidden across mutually untrusted Workspaces.
- Process restart invalidates old Context/Page/Frame/backend handles and semantic targets.
- Context isolation/storage/network/permission policy is explicit.
- Popup preserves opener/new Page identities.
- Navigation is immutable and sequence-bound; URL is not identity.
- Challenge State fences automation only for affected scope.
- Download completes only after WP06/WP03 byte/digest/Object/Location verification.
- restored Profile/cookies do not prove live authentication.
- Evidence Bundle preserves disagreement among DOM/accessibility/pixels/network/application state.

## Semantic assertions

- Context/Snapshot/Node/Event/Selector/Target/Target Result/Action/Attempt/Result/Visual Evidence remain separate.
- Selector is durable; Target Result is fresh and generation-bound.
- ambiguity, expiry, event invalidation, Provider restart or source-generation drift blocks mutation.
- every Action Attempt binds exact current Context/Snapshot/Target Result/Provider generation/Lease/fence and a new WP02 Attempt.
- Provider ACK cannot produce verified Action Result.
- required postconditions are verified from fresh semantic/visual/API/external evidence.
- fallback method and reduced assurance are explicit.
- uncertain effects are reconciled before retry.

## Shell assertions

- Shell Client/Session/Panel/Binding/Layout/View State/Projection/Control Transfer remain separate.
- Shell presentation never mutates canonical runtime truth without a separate authorized Operation.
- client disconnect/background/panel close does not stop runtime work.
- responsive projections are derived and never rewrite canonical Layout Revision.
- Control Transfer fences/quiesces old authority before issuing new Lease/fence.
- uncertain control ownership blocks all mutation.
- primary operations satisfy keyboard, screen-reader semantics, touch, text scaling, reduced motion, contrast, RTL/localization, safe-area and low-bandwidth requirements.

## Migration and replacement assertions

- legacy paths/handles/IDs remain scoped Aliases.
- legacy action logs become verified results only with exact historical context and post-condition evidence.
- backend replacement creates new Compatibility, Provider bindings, Processes, Sessions, generations, Snapshots, Target Results and Attempts.
- stable Application, Browser Binary/Profile, Selector/Target, Panel Type/Layout and Object identity is preserved.
- negative, stale, challenged, ambiguous, partial and inconclusive history remains immutable.

## Required fixture execution

Execute every case in:

- `conformance/fixtures/phase-0b/wp09/application-browser-semantic-shell-cases.v0.1.0.json`;
- WP02 retry/Attempt/Receipt fixtures;
- WP04 Provider-generation/Dispatch-Eligibility/Lease/fence fixtures;
- WP05 checkpoint/restore/recovery fixtures;
- WP06 transfer/download/finalize fixtures;
- WP08 Device Session/Screen Context/control-generation fixtures where semantic UI targets a Device.

## Proof output

A passing WP13 harness run produces immutable:

- catalog-resolution and collision report;
- structural-schema report;
- lifecycle reachability/authority report;
- positive/negative scenario results with expected error codes;
- migration/backend-replacement report;
- privacy/secret/export scan;
- accessibility and responsive-projection report;
- exact harness/tool/environment revisions and Receipts.

Until those executable reports exist, WP09 is candidate contract design—not implemented or proven runtime capability.
