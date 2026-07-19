# Phase 0B WP10 — Knowledge, Data, Package and Plugin

**Status:** CANDIDATE COMPLETE

## Accepted candidate inventory

- Catalog `urn:ptah:schema-catalog:knowledge:0.1.0`.
- 50 candidate schemas.
- Nine namespaced lifecycle machines.
- 27 cross-machine invariants.
- Directional migration and backend-replacement record.
- 54 positive/negative/adversarial conformance cases.
- Consolidated structural, semantic, privacy, lifecycle and replacement safety net.

## Contract families

### Knowledge

Stable Source and immutable Source Revision; bounded Ingestion Request/Run; Segment and Coverage; stable Index and immutable Index Revision; Embedding Record; Query/Run; Result Set/Result; exact Citation; Generated Output; independent Verification.

### Data

Dataset and immutable Revision; plural Schema/Table Observations; Processing Run; secret-free Database Connection Reference; immutable Snapshot; bounded Quality Report; privacy-governed Export.

### Package

Stable Package and immutable Revision; declared Manifest and Dependency Constraints; environment-specific Resolved Graph; immutable Lock Record; Registry Source/trust policy; Installation lifecycle; independent verification scopes.

### Plugin

Stable Plugin and immutable Revision; Manifest; exact-context Compatibility; Installation; Activation; running Instance generation; expiring Health; scoped Capability Grants; Dependency Bindings; Service and Port Registrations; Update Decision; Rollback; Removal.

## Critical laws

- Source, index, result, citation and generated output remain distinct.
- Search rank cannot become truth.
- Citation requires exact source revision/range/digest.
- Snapshot cannot become live database truth.
- Constraint, resolution and lock remain distinct.
- Install acknowledgement cannot become verified package/plugin state.
- Plugin installed, activated, running, healthy and authorized remain distinct.
- Grants, bindings, registrations and health expire/fence with authority and generation.
- Rollback and removal require new execution evidence and post-condition verification.
- Raw credentials remain outside contracts and evidence.
- RAG, vector, workflow, MCP, package-manager and Plugin-host backends remain replaceable adapters/workloads.

## Deferred

- Executable validation harness and actual corpus execution: WP13.
- Dependency selection and implementation: Phase 0C.
