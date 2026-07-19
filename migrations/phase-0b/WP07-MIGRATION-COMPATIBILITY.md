# WP07 Migration and Compatibility Record

**Status:** CANDIDATE  
**Date:** 2026-07-19

Existing Dockerfiles, CI workflows, Dagger modules, BuildKit definitions, package manifests, SBOMs, attestations, signatures and registry records enter Ptah as immutable source Objects plus scoped Aliases and detector observations. Recognition never grants canonical Ptah identity or execution authority.

## Directional migration

1. Import exact source bytes and digests.
2. Record detector/importer proposal, evidence and limitations.
3. Create stable Recipe identity and immutable Recipe Revision.
4. Require explicit acceptance before execution.
5. Compile backend-specific plans without changing Recipe identity.
6. Bind runs and retries to exact WP02 Operations and Attempts.
7. Register outputs through WP03 Objects before optional Artifact promotion.
8. Preserve backend IDs, paths, tags and job IDs as scoped Aliases.

Compatibility is directional, target-specific and expiring. Compatibility with one backend revision does not imply compatibility with another provider generation, platform, isolation policy or proof requirement.

Backend replacement must preserve stable Recipe, Object, Artifact, proof and release identity while creating new compatibility assessments, compiled plans, runs, attempts and evidence.

Unsupported fields, hidden CI behavior, mutable tags, missing lockfiles, unpinned toolchains, undeclared network access and secret-contamination risks remain explicit limitations. Import fails closed or yields a proposal requiring correction; it never silently claims determinism or reproducibility.

No public WP07 contract depends on a donor-specific API. Adapters can be removed while preserving Ptah records, Objects, bundles and migration aliases.
