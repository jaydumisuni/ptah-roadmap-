# ADR-0032 — Phase 0B freeze and Phase 0C entry

Status: proposed pending control-book merge

## Context

All fourteen ordered Phase 0B packages are candidate-complete. WP13 provides executable offline structural and semantic conformance. WP14 freezes a lawful golden/negative corpus and the first vertical-slice proof plan.

## Decision

Freeze the Phase 0B contract set at the merge commit containing WP14 and enter Phase 0C for explicit implementation selection and authorization.

The freeze includes all active schema catalogs, lifecycle machines, migrations, safety nets, fixtures, ADRs, the WP13 harness and the WP14 proof plan. Historical superseded schemas and machines remain immutable and discoverable.

Phase 0C may select concrete backends, languages, libraries and deployment topology only when the selected implementation preserves the frozen public identities and passes the WP14 proof plan.

## Non-authorization

This ADR does not by itself authorize runtime implementation. Authorization becomes effective only when Phase 0C selections, licence, repository layout and implementation proof plan are accepted and recorded in `CURRENT_STATE.md`.

## Consequences

- architecture invention during coding is prohibited where Phase 0B already defines the boundary;
- backend-specific identifiers remain aliases;
- implementation changes that require contract changes reopen Phase 0B through a versioned ADR and migration;
- exact-head conformance remains mandatory for every contract change.
