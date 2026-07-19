# WP14 entity-kind registry completion

Status: candidate

## New canonical kinds

- `conformance.corpus`
- `conformance.corpus_revision`
- `conformance.fixture_manifest`
- `conformance.fixture_admission`
- `conformance.expected_proof`
- `conformance.proof_plan`
- `conformance.proof_plan_revision`
- `conformance.freeze_decision`

## Reuse

WP14 reuses WP03 Content/Object/Artifact for fixture bytes and immutable storage; WP02 Activity/Operation/Attempt/Receipt for execution evidence; WP12 Evidence and Claim for bounded proof; and WP13 Conformance Run, Check Result and Report for executable validation.

A fixture filename, directory path, test title or CI job ID is never canonical identity. Every admitted fixture is digest-bound, licence/audience classified and linked to an immutable corpus revision.
