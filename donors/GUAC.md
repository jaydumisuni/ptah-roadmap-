# Donor Record — GUAC

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — PRIMARY SOFTWARE-SUPPLY-CHAIN METADATA GRAPH AND CORRELATION DONOR  
**Inspected:** 2026-07-18

## Identity

- Canonical URL: https://github.com/guacsec/guac
- Default branch: `main`
- Pinned commit: `c66a25f6f15819609fc8bbf4d961d1e0ec78d671`
- Licence: Apache-2.0
- Activity: Active
- Primary language: Go
- Classification: security-metadata ingestion, normalization, graph assembly, GraphQL query and supply-chain analysis donor
- Ptah targets: security/provenance graph projection, SBOM/attestation/vulnerability ingestion, relationship normalization, cross-document correlation and derived security knowledge

## Files/components inspected

- `README.md`
- `LICENSE`
- GraphQL/backend locations for dependency, SBOM, occurrence, vulnerability and certification relationships
- SPDX, CycloneDX, deps.dev and common parser/graph-builder locations
- backend and analytics structure described by the repository

## Verified capabilities and patterns

### Ingestion and normalization

- GUAC ingests multiple software-supply-chain document and service formats into a normalized graph.
- Supported source families include SPDX, CycloneDX, in-toto/DSSE attestations, SLSA/provenance, Scorecard, OSV, deps.dev, CSAF/VEX and OpenVEX-related data.
- Parsers convert source-specific identifiers and relationships into common graph entities.
- Package, source, artifact, builder, vulnerability and document identities are correlated across inputs.
- Identifier normalization uses standards and heuristics; correlation is therefore useful but not infallible.

### Relationship graph

- The graph can retain relationships such as package dependencies, artifact/package occurrences, SBOM association and vulnerability/certification assertions.
- Relationships carry source/provenance context rather than only flattened labels.
- Query and analytics paths can traverse dependency and vulnerability relationships for impact or patch planning.
- GraphQL exposes structured query operations over the assembled graph.
- Independent source documents can support, supplement or conflict with one another.

### Backend separation

- GUAC separates ingestion/parsing, graph assembly, query API and storage backends.
- An in-memory key-value backend is useful for tests/conformance but is not durable.
- The ent/Postgres path is the primary supported persistent direction in the inspected project.
- Additional graph backends exist with differing maturity/support status.
- A shared GraphQL shape does not prove every backend has equivalent persistence, indexing or query semantics.

### Security-knowledge lesson

- Security metadata becomes more useful when document origin, package/artifact identity and relationships are retained together.
- Aggregation can reveal dependency paths and affected artifacts that one scanner report cannot.
- Correlated graph state remains derived knowledge; the original SBOMs, attestations, vulnerability records and scan reports must remain available.
- A graph edge is an assertion produced by a parser/source, not independent proof that the relation is correct.

## What GUAC contributes

- A mature supply-chain security graph model.
- Ingestion of several common SBOM, provenance, attestation and vulnerability formats.
- Normalized package/source/artifact/vulnerability relationships.
- GraphQL query and analytics patterns.
- Dependency-path and patch-planning concepts.
- Separation of source documents, parsers, graph assembly and storage backends.
- A useful optional Security Knowledge Facility over Ptah Objects, Artifacts, Claims and Evidence.

## Important limitations for Ptah

- GUAC is an aggregation/query system, not authoritative source truth or a scanner.
- Identifier correlation can produce false joins, missed joins or ambiguous package/artifact mappings.
- Parser bugs and source-document errors propagate into graph relationships.
- Source freshness, revocation and deletion require explicit reconciliation.
- Different backends vary in maturity and supported semantics.
- The in-memory backend is not durable.
- GraphQL IDs and backend keys are GUAC-local identities.
- A vulnerability edge does not establish reachability, exploitability, impact, current deployment exposure or acceptance.
- VEX/certification statements are claims from named issuers and may disagree.
- GUAC does not perform independent cryptographic verification of every ingested assertion by default.
- Large graphs need resource, tenancy, permission and retention controls not supplied by the graph shape alone.
- Ingestion from external services introduces network, credential and data-freshness dependencies.
- GUAC does not replace Ptah Objects, Activity history, provenance receipts, scanner evidence or Sergeant review.

## Must not be inherited

- GUAC node/edge/backend IDs as canonical Ptah identities;
- the graph treated as source truth after original documents are discarded;
- heuristic package/source joins treated as certain identity;
- vulnerability association treated as exploitability or release-blocking proof;
- VEX or certification statements accepted without issuer, signature, scope and revision checks;
- all backends described as semantically equivalent;
- in-memory graph state used as durable evidence;
- stale/revoked source documents left active without reconciliation;
- cross-Workspace/private security data combined without permission filtering;
- GraphQL access exposed without tenant/object authorization;
- GUAC made mandatory for the first one-Node Ptah slice.

## Integration decision

**ADOPT GUAC AS AN OPTIONAL SECURITY/PROVENANCE GRAPH FACILITY AND PRIMARY CORRELATION DONOR; KEEP ORIGINAL DOCUMENTS, PTAH IDENTITIES, CLAIMS, EVIDENCE AND REVIEW AUTHORITATIVE.**

Recommended Ptah role:

1. every ingested SBOM, attestation, vulnerability feed, VEX or scan report remains an immutable Ptah Object/Artifact;
2. ingestion is a receipted Activity retaining parser/version, source hash and normalization warnings;
3. GUAC entities map to stable Ptah package/source/artifact/vulnerability references through an adapter;
4. every relationship retains the originating document and parser assertion;
5. conflicting and uncertain mappings remain visible;
6. graph-derived paths and patch suggestions become derived Claims with explanation;
7. Workspace, source and audience permissions filter ingestion and query;
8. freshness, revocation, tombstone and rebuild operations are explicit;
9. GUAC can be rebuilt from retained source Objects;
10. a lighter SQL/native graph path remains available for the first slice.

## Native Ptah gap

Ptah must define:

- Security Source Document and Source Revision;
- parser/normalizer identity and version;
- Package, Source, Artifact, Vulnerability and Advisory references;
- relationship Claim with confidence and source support;
- identifier-alias and uncertain-identity records;
- conflicting relationship/assertion handling;
- graph/index revision and rebuild recipe;
- freshness, revocation, deletion and tombstone behavior;
- issuer/signature/scope records for VEX and certifications;
- Workspace/object permissions and query filtering;
- derived impact/path/patch-planning Claim records;
- backend conformance and migration tests;
- source-to-graph lineage and retained raw documents.

## Exit strategy

Ptah security/provenance graph contracts remain independent. GUAC, native SQL/graph views, Neo4j, another graph engine or direct queries can implement them without changing source Objects, Claims, Evidence, Artifacts or Findings.

## Validation required

1. Ingest SPDX, CycloneDX, in-toto/SLSA, OSV and VEX examples and retain exact source lineage.
2. Correlate one package across conflicting identifiers and retain uncertainty rather than silently merging.
3. Produce a dependency/vulnerability path and trace every edge to source evidence.
4. Revoke or replace one source document and rebuild/reconcile affected edges.
5. Compare at least two supported backends for query and persistence semantics.
6. Deny cross-Workspace graph access.
7. Keep contradictory VEX/advisory claims simultaneously visible.
8. Delete the GUAC database and rebuild it from Ptah Objects.
9. Prove a graph vulnerability association does not automatically become exploitable or release-blocking.
10. Replace GUAC without changing Ptah identities or historical evidence.
