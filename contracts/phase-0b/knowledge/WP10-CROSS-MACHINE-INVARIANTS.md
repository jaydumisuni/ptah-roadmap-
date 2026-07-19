# WP10 Cross-Machine Invariants

**Status:** CANDIDATE

1. Source, Source Revision, Segment, Index, Result, Citation and Generated Output remain distinct.
2. Coverage is bounded to exact Source Revisions and ingestion configuration; partial or failed scopes remain visible.
3. Index existence never proves completeness, freshness, correctness or authority.
4. Query rank never becomes truth, acceptance or a verified claim.
5. Citation binds exact source revision, range and digest; URL/title alone is insufficient.
6. Generated Output requires separate Verification for claim support, contradiction and missing coverage.
7. Dataset identity survives revisions; Database Snapshot never becomes current live database truth.
8. Raw credentials never enter Connection Reference, logs, exports, Plugin manifests or evidence.
9. Data Processing Run maps to WP07 Recipe/Plan and WP02 Operation/Attempt; retries create new Attempts.
10. Data Export is a privacy-governed act and reuses WP03/WP06 Object/Transfer truth.
11. Package coordinate is an Alias until ecosystem, namespace, source and digest are exact.
12. Dependency Constraint, Resolved Graph and Lock Record remain separate.
13. Package installation acknowledgement is not integrity, provenance, policy, installed-state or functionality verification.
14. Plugin identity, Revision, Manifest, Compatibility, Installation, Activation, Instance and Health remain separate.
15. Plugin installation never grants runtime authority.
16. Activation requires explicit policy and scoped capability grants.
17. Plugin Instance binds exact Provider and instance generations; process IDs and handles remain Aliases.
18. Health observations expire and cannot outlive the referenced generations.
19. Capability grants are scoped, expiring and revocable; stale grants cannot authorize work.
20. Dependency Bindings and Service/Port Registrations expire with Instance/Provider generation or grant revocation.
21. Port registration is not public exposure authority; network scope and policy remain explicit.
22. Update Decision is separate from update execution, verification, rollback and release acceptance.
23. Rollback creates new WP02 Attempts and requires post-rollback verification.
24. Removal requires disablement, grant revocation, instance stop, unregister, uninstall, cleanup and verification as separate proof stages.
25. Failed, partial, unsupported, stale and inconclusive results remain immutable history.
26. Backend, vector-store, registry, package-manager and Plugin-host replacement preserves canonical Ptah identities and creates new revisions/generations/evidence.
27. MCP, RAG, workflow and Plugin frameworks remain adapters or workloads; none replaces Ptah Core identity, Activity or policy truth.
