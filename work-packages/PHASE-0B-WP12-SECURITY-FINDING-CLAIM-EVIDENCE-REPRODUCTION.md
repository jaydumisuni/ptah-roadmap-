# Phase 0B WP12 — Security, Finding, Claim, Evidence and Reproduction

**Status:** CANDIDATE BLUEPRINT
**Implementation authorization:** NONE

## Required entities

- Observation, Finding, Claim, Evidence Item and Evidence Bundle;
- Scanner/analyst/tool identity and exact revision;
- Finding subject, scope, severity observation and confidence;
- validation request/run, reviewer decision and authoritative disposition;
- remediation proposal, patch Object, application run and post-fix verification;
- false-positive, disputed, accepted-risk, superseded and withdrawn states;
- reproduction Protocol, Request, Run and Comparison;
- disclosure/audience/redaction and legal-hold controls.

## Core laws

1. Observation is not Finding; Finding is not Claim; Claim is not Verdict.
2. Tool severity is evidence, not universal truth.
3. Every Finding binds exact immutable subjects, scope, tool revision and evidence.
4. Absence of findings is never proof of absence outside declared coverage.
5. Remediation generation, application and verified effectiveness remain separate.
6. Negative, failed and inconclusive results remain immutable history.
7. Reproduction requires frozen Protocol and independently classified conditions.
8. Security workloads run inside Ptah and cannot define Ptah Core identity or policy.
9. Public disclosure is separate from internal evidence retention.

## Proof cases

- two scanners disagree without overwriting either result;
- stale-subject Finding cannot be applied to a newer Object Revision without explicit revalidation;
- failed reproduction does not delete the original claim;
- remediation patch existence does not imply applied or effective;
- accepted risk preserves Finding and authority decision;
- redacted export preserves internal evidence lineage;
- same environment/cache rerun is classified as repeated execution, not independent reproduction;
- backend replacement preserves Finding/Claim/Evidence identity.

## Outputs

Conventions, entity kinds, schemas/catalog, lifecycle machines, migration, fixtures, safety net, package record and ADR-0029.
