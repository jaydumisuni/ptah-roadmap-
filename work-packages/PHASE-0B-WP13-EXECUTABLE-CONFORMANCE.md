# Phase 0B WP13 — Executable Conformance

**Status:** CANDIDATE-COMPLETE PENDING EXACT-HEAD WORKFLOW

## Scope

WP13 turns Phase 0B contracts into mechanically checked artifacts.

## Delivered

- installable Python conformance harness;
- JSON and JSON Schema validation;
- local schema reference checks;
- catalog integrity checks;
- lifecycle reachability checks;
- fixture-suite integrity checks;
- semantic rule engine and fixture runner;
- unit tests;
- exact-head GitHub Actions workflow;
- typed Plan, Run, Check Result, Report, Migration Case and Migration Result schemas;
- Conformance Run lifecycle;
- offline schema catalog;
- migration execution contract;
- consolidated safety net.

## Acceptance gate

Candidate completion becomes accepted only when the PR-head workflow succeeds and publishes both structural and semantic reports with zero required failures. Any discovered defect must be repaired on this branch and re-run before merge.

## Non-goals

WP13 does not select production runtime backends, authorize implementation, freeze the golden corpus, or claim domain correctness beyond the encoded contracts and fixtures.
