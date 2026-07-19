# ADR-0029 — Security, Finding, Claim, Evidence and Reproduction Boundary

**Status:** ACCEPTED

## Decision

Ptah will represent Observation, Finding, Claim, Evidence Item, Evidence Bundle, Validation, Review, Accepted Risk, Dispute, Disclosure, remediation and reproduction as separate typed records.

Security tools and agents are evidence-producing workloads/adapters. Their IDs, rules, CVEs, reports and run handles never become canonical Ptah Finding identity.

A patch or remediation acknowledgement cannot satisfy post-fix verification. Accepted Risk cannot erase a Finding. Disputes preserve all positions. Reproduction requires new WP02 work, exact environment evidence and explicit independence criteria; negative and inconclusive outcomes remain immutable.

## Consequences

- false positives and contradictory observations are representable without data loss;
- authority and evidence coverage are bounded and reviewable;
- public disclosure can be privacy/redaction governed;
- scanner and reproduction backends remain replaceable;
- implementation later has explicit semantics for remediation uncertainty and reproduction claims.

## Deferred

Executable conformance is WP13. Golden corpus freeze is WP14. Production scanner and reproduction backend selection remains Phase 0C work.
