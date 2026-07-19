# Phase 0B WP12 — Security, Finding, Claim, Evidence and Reproduction

**Status:** CANDIDATE COMPLETE ON BRANCH

## Inventory

- catalog `urn:ptah:schema-catalog:security:0.1.0`;
- 19 schemas including shared definitions;
- five lifecycle machines;
- 24 cross-machine invariants;
- directional migration and backend-replacement rules;
- 40 positive/negative/adversarial conformance scenarios;
- consolidated safety net;
- final consistency review;
- ADR-0029.

## Boundary

WP12 defines security Observation, Finding, Claim, Evidence, Validation, Review, Accepted Risk, Dispute, Disclosure, remediation and independent reproduction without allowing any scanner, vulnerability database, agent or report format to replace Ptah Core identity.

Semgrep, Trivy, Grype, ZAP, Strix-like workers and future security systems remain workloads/adapters. They may emit Observations and Evidence but cannot directly create universal truth.

## Closure claim

Builders no longer need to invent false-positive handling, claim authority, evidence coverage, accepted-risk expiry, disputed findings, patch verification, disclosure boundaries or reproduction independence.
