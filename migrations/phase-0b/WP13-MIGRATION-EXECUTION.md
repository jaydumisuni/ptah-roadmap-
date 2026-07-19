# Phase 0B WP13 Migration Execution Contract

**Status:** CANDIDATE

WP13 executes migration evidence; it does not merely record migration prose.

## Required rules

1. Every version-changing schema migration is directional and names exact source and target schema URNs.
2. A migration case binds immutable input, expected output or expected failure code, and the migration implementation identity.
3. Lossy migration must declare lost fields, authority impact and rollback limitations.
4. Unknown enum values, stale generations, unresolved aliases and missing evidence fail closed.
5. A migrated record is validated against the target schema and all applicable semantic invariants.
6. Migration success never proves domain correctness; it proves only declared structural and semantic preservation.
7. Negative and inconclusive migration results remain immutable evidence.
8. Backend replacement tests must preserve Ptah identity while changing backend-scoped aliases only.
9. Reports bind the exact repository commit, catalog set, harness version and fixture digest.
10. Phase 0B cannot freeze while any required migration case is absent, skipped without reviewed reason, or failing.
