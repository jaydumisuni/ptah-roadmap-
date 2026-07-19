# Phase 0B WP13 Consolidated Safety Net

**Status:** CANDIDATE

WP13 is accepted only when the exact-head workflow proves all required checks.

## Structural gates

- every discovered JSON file parses;
- every schema is valid JSON Schema 2020-12;
- every schema has a unique versioned Ptah URN;
- every Ptah `$ref` resolves locally;
- every catalog entry names an existing file and known schema ID;
- every lifecycle machine has unique identity, declared initial state, valid transitions and reachable states;
- every fixture suite has unique case IDs, explicit valid/invalid expectation and stable failure codes.

## Semantic gates

- raw secrets are rejected;
- stale Provider generations and fence tokens are rejected;
- retries require new Attempt identity;
- acknowledgement cannot become verification;
- citations require exact revision/range/digest identity;
- accepted risk must expire and cannot erase Findings;
- independent reproduction requires new execution and environment evidence;
- negative and inconclusive evidence is retained;
- backend IDs cannot replace stable Ptah identity.

## Exact-head proof

The workflow must run unit tests, repository structural conformance and semantic fixtures against the pull-request SHA. Both reports are uploaded as commit-specific artifacts. A missing report, skipped required suite or non-zero failure count blocks acceptance.
