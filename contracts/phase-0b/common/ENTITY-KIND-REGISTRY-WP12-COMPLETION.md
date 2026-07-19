# WP12 Entity-Kind Registry Completion

**Status:** CANDIDATE

## Security and evidence

- `security.observation`
- `security.finding`
- `security.claim`
- `security.evidence_item`
- `security.evidence_bundle`
- `security.validation_run`
- `security.review_decision`
- `security.accepted_risk`
- `security.dispute`
- `security.disclosure_record`

## Remediation

- `security.remediation_proposal`
- `security.patch`
- `security.remediation_run`
- `security.post_fix_verification`

## Reproduction

- `security.reproduction_protocol`
- `security.reproduction_request`
- `security.reproduction_run`
- `security.reproduction_comparison`

## Non-collapse rules

1. Observation is raw/bounded evidence, not a Finding.
2. Finding is a reviewed interpretation, not a universal truth.
3. Claim states an assertion and authority scope; it is not Evidence.
4. Evidence Item, Bundle, Validation and Review remain separate.
5. Severity, confidence, exploitability, policy impact and acceptance remain separate dimensions.
6. Accepted Risk does not erase or close the Finding.
7. Dispute preserves competing positions and evidence.
8. Remediation Proposal and Patch are not execution or verified repair.
9. Post-fix verification cannot be inferred from patch application success.
10. Reproduction requires new WP02 Attempts and independent environment evidence.
11. Failed, negative, partial and inconclusive reproduction remains immutable history.
12. Scanner IDs, rule IDs, CVEs, issue numbers, report paths and backend run IDs remain scoped Aliases/evidence.
