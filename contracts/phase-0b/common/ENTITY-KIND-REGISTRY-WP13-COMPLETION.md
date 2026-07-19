# WP13 Entity-Kind Registry Completion

**Status:** CANDIDATE

- `conformance.plan` — immutable selected catalog, rule, migration and fixture scope.
- `conformance.run` — one logical offline conformance execution mapped to WP02.
- `conformance.check_result` — immutable result for one structural/lifecycle/semantic/migration check.
- `conformance.report` — immutable exact-head summary over Check Results.
- `conformance.migration_case` — directional source/target migration expectation and fixture binding.
- `conformance.migration_result` — immutable migration execution and round-trip/semantic result.

Backend CI job IDs, workflow-run IDs, local paths and test framework IDs remain scoped Aliases. A green workflow is evidence for a specific commit and plan only; it is not universal implementation correctness.
