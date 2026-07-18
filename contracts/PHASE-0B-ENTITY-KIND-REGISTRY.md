# Ptah Phase 0B — Entity Kind Registry

**Registry:** `ptah.entity-kind`  
**Candidate version:** `0.1.0`  
**Status:** CANDIDATE  
**Date:** 2026-07-18

## Purpose

Provide the initial controlled `entity_kind` vocabulary used by canonical Ptah references.

This registry is intentionally broader than the first implementation slice because Phase 0B must make cross-contract identity unambiguous. Registration does not authorize implementation of the capability.

## Token format

```text
<namespace>.<name>
```

Pattern:

```regex
^[a-z][a-z0-9]*(?:\.[a-z][a-z0-9_-]*)+$
```

Rules:

1. Tokens are lowercase and immutable after frozen publication.
2. Renames create a new token plus an explicit supersession/migration mapping.
3. Tokens identify entity semantics, not database tables, UI routes or donor classes.
4. A subtype requiring a different authority/state machine should receive a distinct token.
5. Provider/Session/Lease and other typed-family kinds remain fields within their family entity unless the subtype itself needs a stable independently referenced entity kind.
6. Registration does not imply public visibility.

---

# Core world

| Token | Meaning |
|---|---|
| `core.node` | Physical or virtual machine identity contributing capabilities |
| `core.workspace` | Persistent namespace/world boundary |
| `core.activity` | Durable caller-visible unit of work |
| `core.operation` | Logical side effect or observation inside an Activity |
| `core.attempt` | One physical execution try of an Operation |
| `core.facility` | Stable capability contract |
| `core.capability` | Versioned capability definition/claim |
| `core.relationship` | First-class relationship between typed entities |
| `core.alias` | Scoped non-canonical identifier/name |
| `core.tombstone` | Lifecycle record marking an entity unavailable/retired under policy |
| `core.migration_definition` | Versioned schema/data migration definition |
| `core.migration_run` | One execution/evidence record for a migration |

# Events, proof and review

| Token | Meaning |
|---|---|
| `event.event` | Typed Event envelope instance |
| `event.cursor` | Replay/sequence cursor record |
| `proof.receipt` | Durable producer evidence for one correlated operation/observation |
| `proof.evidence` | Immutable support/contradiction/limitation reference entity |
| `proof.claim` | Bounded proposition under scope/protocol |
| `proof.review` | Evaluator review over exact evidence/checkpoint |
| `proof.verdict` | Versioned conclusion produced by a Review |
| `proof.external_result` | Result whose authority belongs to an external system/device |
| `proof.protocol` | Frozen method for evaluating a claim/result |
| `proof.reproduction_run` | Independent or repeated execution under a Protocol |
| `proof.comparison` | Exact/semantic/tolerance comparison between runs/outputs |
| `proof.evidence_card` | Permission-filtered bounded presentation View |

# Runtime and Providers

| Token | Meaning |
|---|---|
| `runtime.provider` | Typed Provider definition/instance/generation root |
| `runtime.provider_revision` | Immutable Provider contract/configuration revision |
| `runtime.session` | Typed runtime/presentation Session root |
| `runtime.lease` | Typed scoped time-bounded authority root |
| `runtime.reservation` | Promised resource bundle before execution |
| `runtime.placement_request` | Hard constraints/preferences for workload placement |
| `runtime.placement_candidate` | Evaluated placement candidate and rejection/score evidence |
| `runtime.placement_decision` | Selected placement result under policy revision |
| `runtime.secure_grant` | Typed Object/network/device/credential grant |
| `runtime.process` | Supervised operating-system process identity |
| `runtime.pty` | Terminal/PTY runtime identity |
| `runtime.service` | Supervised service and endpoint registration |
| `runtime.checkpoint` | Prepared state for resume/recovery |
| `runtime.checkpoint_bundle` | Multi-component checkpoint/export manifest |
| `runtime.isolation_class` | Threat/containment class independent of implementation |

# Objects, Artifacts and storage

| Token | Meaning |
|---|---|
| `object.object` | Universal immutable content/logical Object identity |
| `object.revision` | Immutable logical Object/source revision |
| `object.view` | Derived representation over an exact Object/revision |
| `object.preview` | Human/consumer-oriented derivative View |
| `object.derivative` | Output transformed/derived from source Objects |
| `object.detector_observation` | One detector's type/structure assertion |
| `object.decomposition_run` | Progressive decomposition Activity result |
| `object.artifact` | Durable promoted result role over one or more Objects |
| `object.artifact_release` | Immutable released/published Artifact revision |
| `storage.location` | Physical/logical storage location or replica |
| `storage.transfer` | Transfer intent/session root |
| `storage.transfer_attempt` | One physical transfer try |
| `storage.partial_state` | Resumable partial-range/chunk state |
| `storage.sync_revision` | Sync-vector/reconciliation revision |
| `storage.conflict` | Retained concurrent revision conflict |
| `storage.backup_set` | Versioned backup collection/manifest |
| `storage.restore_run` | Restore execution and read-back evidence |

# Build and provenance

| Token | Meaning |
|---|---|
| `build.recipe` | Backend-neutral intended Build/test/render/package work |
| `build.compiled_plan` | Backend-specific compiled graph/plan reference |
| `build.run` | One Build execution result root |
| `build.cache_record` | Reusable derived cache entry and producer evidence |
| `provenance.sbom` | Versioned SBOM document Artifact role |
| `provenance.package_observation` | One package/file inventory assertion |
| `provenance.attestation` | Versioned attestation statement/envelope |
| `provenance.signature` | Signature over exact subject bytes/digest |
| `provenance.verification_run` | Signature/attestation/provenance verification execution |
| `provenance.graph_revision` | Derived provenance/security relationship graph revision |

# Domain Packs and specialist objects

| Token | Meaning |
|---|---|
| `domain.pack` | Versioned Domain Pack capability definition |
| `domain.pack_revision` | Immutable Pack implementation/contract revision |
| `domain.inventory` | Domain-specific structure/inventory result |
| `domain.validation_run` | Domain validation result over exact inputs |
| `domain.compare_run` | Domain-specific comparison execution |
| `domain.rebuild_run` | Domain rebuild execution/evidence |

# Firmware, disks and filesystems

| Token | Meaning |
|---|---|
| `firmware.package` | Firmware bundle/package logical identity |
| `firmware.manifest` | Parsed package manifest revision |
| `firmware.component` | Independently addressable firmware component |
| `firmware.compatibility_claim` | Target/tool compatibility assertion |
| `firmware.operation` | Specialist inspect/transform/write/read-back operation root |
| `disk.image` | Disk/block image logical Object role |
| `disk.partition_table` | GPT/MBR/etc. parsed table revision |
| `disk.partition` | Partition identity within an exact image/device generation |
| `filesystem.filesystem` | Filesystem identity/observation within image/device |
| `filesystem.mount_session` | Scoped open/mount runtime session |

# Devices

| Token | Meaning |
|---|---|
| `device.device` | Stable physical/emulated Device identity |
| `device.interface` | USB/network/ADB/Fastboot/etc. interface incarnation |
| `device.connection` | Connection/epoch record |
| `device.session` | Active Device Session |
| `device.stream` | Display/log/input stream identity |
| `device.screen_context` | Semantic/visual Device screen context |
| `device.application_installation` | App/package installation on one Device revision |
| `device.protocol_operation` | Correlated physical/device protocol operation |
| `device.backup` | Immutable device/NV/partition backup Artifact role |

# Applications and semantic UI

| Token | Meaning |
|---|---|
| `application.application` | Application/package Object role |
| `application.installation` | Installed application in one Provider/environment |
| `application.session` | Running Application Session |
| `application.window` | Window identity under Application/provider generation |
| `application.display_session` | Remote/local display session |
| `semantic.context` | Provider-scoped semantic UI context |
| `semantic.snapshot` | Captured semantic tree/state revision |
| `semantic.target` | Reacquirable target specification/result |
| `semantic.selector` | Versioned selector/query specification |
| `semantic.action` | Requested semantic/raw/visual action intent |
| `semantic.action_result` | Provider result plus post-condition evidence |

# Browser and live research

| Token | Meaning |
|---|---|
| `browser.binary` | Browser executable/build identity |
| `browser.profile` | Persistent browser profile/storage identity |
| `browser.process` | Browser process/provider generation |
| `browser.context` | Isolated browser context |
| `browser.page` | Top-level page/tab identity |
| `browser.frame` | Frame identity under page generation |
| `browser.popup` | Popup/new-page relationship record |
| `browser.download` | Download intent/result identity |
| `browser.challenge` | Authentication/challenge/manual-completion state |
| `research.source` | External source identity/revision |
| `research.retrieval` | Source acquisition Activity/result |
| `research.citation` | Exact source-revision/range reference |

# Human Workspace shell

| Token | Meaning |
|---|---|
| `shell.client` | Presentation implementation identity |
| `shell.session` | Authenticated human presentation session |
| `shell.panel_type` | Versioned Panel contribution contract |
| `shell.panel` | Panel Instance bound to exact entities |
| `shell.layout_profile` | Logical presentation profile |
| `shell.layout_revision` | Immutable logical layout revision |
| `shell.view_state` | Client/panel presentation-state reference |
| `shell.control_transfer` | Human/automation takeover or return record |

# Knowledge and data

| Token | Meaning |
|---|---|
| `knowledge.source` | Versioned knowledge-source identity |
| `knowledge.corpus` | Curated collection of permitted sources/documents |
| `knowledge.document_revision` | Exact ingested source/document revision |
| `knowledge.chunk` | Derived bounded segment under one revision |
| `knowledge.index_revision` | Rebuildable lexical/vector/graph index revision |
| `knowledge.query` | Retrieval/search intent |
| `knowledge.result` | Ranked result set and explanation |
| `knowledge.citation` | Exact source/revision/range grounding |
| `data.dataset` | Logical structured dataset |
| `data.dataset_revision` | Immutable dataset snapshot/revision |
| `data.table` | Typed table identity within dataset revision |
| `data.schema` | Column/field schema revision |
| `data.query` | Structured analytical query intent |
| `data.transformation` | Versioned data transformation recipe/run |
| `data.result` | Analytical output and lineage |

# Package and Plugin lifecycle

| Token | Meaning |
|---|---|
| `package.package` | Logical package/plugin identity |
| `package.release` | Immutable Package Release |
| `package.registry_entry` | Discovery/index assertion about a release |
| `plugin.installation` | Installed Package Release in a scope |
| `plugin.activation` | Enabled contribution/runtime binding |
| `plugin.manifest` | Contribution/permission/resource manifest revision |
| `plugin.health` | Health/conformance observation |
| `plugin.migration_run` | Plugin configuration/state migration execution |

# Security assessment and Findings

| Token | Meaning |
|---|---|
| `security.authorization` | Explicit assessment/test authority and scope |
| `security.assessment_plan` | Frozen target/machinery/coverage plan |
| `security.assessment_run` | One authorized assessment Activity/result |
| `security.coverage` | Requested/resolved/scanned/skipped/error scope |
| `security.scanner_revision` | Exact tool/engine/rules/database/policy/model revision |
| `security.raw_report` | Immutable restricted scanner/workload report Artifact role |
| `security.finding_observation` | One detector/agent/manual security assertion |
| `security.finding` | Stable correlated reviewed issue identity |
| `security.risk_assessment` | Multidimensional risk analysis revision |
| `security.disposition` | Confirmed/false-positive/not-affected/accepted-risk/etc. decision |
| `security.exception` | Scoped expiring suppression/exception/accepted-risk record |
| `security.remediation_proposal` | Proposed change and rationale |
| `security.verification_run` | Targeted re-test/read-back execution |

# Documentation and publication

| Token | Meaning |
|---|---|
| `documentation.source` | Authoritative documentation source revision |
| `documentation.build_recipe` | Static docs/diagram build recipe |
| `documentation.build` | Documentation build execution/result |
| `documentation.publication` | Audience/target-specific published Artifact release |
| `documentation.link_check` | Link/source freshness validation result |

---

# Typed-family kind registries

The following values are family `kind` fields, not independent `entity_kind` tokens unless a later schema promotes them.

## Provider kinds

```text
workspace
process
oci_runtime
isolation_runtime
storage
transfer
build
browser
application
device
display
semantic_ui
knowledge
data
plugin_runtime
scheduler
security_scanner
reproduction
```

## Session kinds

```text
workspace_recovery
shell
terminal
browser_process
browser_context
browser_page
device
application
display
semantic_context
```

## Lease kinds

```text
resource_reservation
provider_execution
device_ownership
interactive_control
```

## Snapshot kinds

```text
node_capability
resource_pressure
semantic_ui
filesystem
container
sandbox
microvm
full_vm
knowledge_index
assessment_coverage
```

## Evidence kinds

```text
object
artifact
receipt
source_range
http_exchange
screenshot
video
log
trace
report
sbom
attestation
signature
physical_readback
external_result
comparison
review
```

---

# Registry change process

A registry change proposal must state:

- proposed token/kind;
- exact semantics and authority;
- owning schema/state machine;
- why an existing token/kind is insufficient;
- privacy/retention implications;
- compatibility/migration impact;
- conformance fixtures;
- affected ADRs/requirements.

Frozen tokens are never silently repurposed. Deprecation creates a mapping and migration rule.

## Candidate review checks

Before this registry becomes frozen:

1. every Phase 0B schema references a registered token/kind;
2. no two tokens claim the same canonical identity;
3. aliases and presentation Views are not promoted as truth entities;
4. every mutable token identifies its state-machine owner;
5. every runtime token identifies generation/epoch requirements;
6. public/private and retention requirements are mapped;
7. unused speculative tokens are either justified or removed before Phase 0B freeze.

Registration is architecture vocabulary, not implementation authorization.
