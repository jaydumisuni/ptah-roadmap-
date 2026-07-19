# WP10 Consolidated Safety Net

**Catalog:** `urn:ptah:schema-catalog:knowledge:0.1.0`

## Structural

- Resolve 50 unique schema URNs and nine lifecycle machines offline.
- Reject duplicate schema IDs, entity-kind collisions, missing paths and network fallback.
- Validate every lifecycle projection against a cataloged machine/version/state.
- Verify dependency catalogs and immutable version references.

## Knowledge

- Preserve Source/Object truth separately from Segments, Indexes, Results and generated outputs.
- Require exact coverage for every ingestion/index claim.
- Bind Citations to source revision, range and digest.
- Reject search rank as truth and generated output as self-verification.
- Retain stale, partial, contradicted, unsupported and unknown results.

## Data

- Preserve Dataset revisions and exact Objects.
- Block raw credentials in Connection References, logs and exports.
- Keep live database state separate from immutable snapshots.
- Require WP07 Recipe/Plan and WP02 Operation/Attempt mapping for processing.
- Require audience/privacy policy and WP03/WP06 verification for exports.

## Package

- Require ecosystem/namespace/source/digest for exact revision identity.
- Keep constraints, resolved graphs and locks separate.
- Require fresh Registry Source/trust policy evidence.
- Treat installation ACK as unverified until independent checks.
- Keep integrity, provenance, policy, installed state and functionality as separate verification scopes.

## Plugin

- Keep Plugin/Revision/Manifest/Compatibility/Installation/Activation/Instance/Health separate.
- Require explicit grants before activation and current grants during operation.
- Fence stale Provider/Instance generations, bindings, registrations and health.
- Require policy/grants for service and port exposure.
- Treat update decisions as decisions, not execution.
- Require new Attempts and verification for rollback.
- Require grant revocation, stop, unregister, uninstall, cleanup and verification for removal.
- Scan all records/evidence for raw credentials and private data.

## Migration and replacement

- Run every directional migration case.
- Preserve weak legacy records when evidence is insufficient.
- Verify RAG/vector/database/package-manager/Plugin-host replacement without canonical identity loss.
- Reject any adapter framework becoming Ptah Core identity, execution or policy truth.

## Corpus

Execute all cases in `conformance/fixtures/phase-0b/wp10/knowledge-data-package-plugin-cases.v0.1.0.json` and emit exact expected codes, schema/catalog digests, lifecycle digests, harness revision, environment evidence and immutable Receipts. Executability remains WP13 work.
