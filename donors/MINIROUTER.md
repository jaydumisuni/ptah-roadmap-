# Donor Record — MiniRouter

**Phase:** 0A / WP10 boundary check; later distributed routing/evaluation cluster  
**Status:** CANONICAL REPOSITORY RECOVERED — STUDY-ONLY, LICENCE UNRESOLVED, NOT REQUIRED FOR WP10 CLOSURE  
**Inspected:** 2026-07-18

## Identity

- Canonical repository recovered from the original `tmimmanuel` discovery source: https://github.com/tmimmanuel/minirouter
- Default branch: `main`
- Pinned commit: `bf3ea957f6ef3de358528f73e0518ec51e39d8f3`
- Package name: `trinity-coordinator`
- Package version: `0.0.1`
- Licence: **UNRESOLVED — no root `LICENSE` file found and no licence field was recovered from `pyproject.toml`**
- Activity: Active
- Classification: experimental query router, model-role coordinator, evaluation pipeline and competition-validator donor
- Ptah targets: future routing-quality evaluation, provider-selection experiments, submission/evaluation Activities and proof dashboards; not Ptah Core reasoning and not a required Knowledge/Data/Search/Plugin donor

## Files/components inspected

- `README.md`
- `pyproject.toml`
- `validator/README.md`
- current commit/activity evidence
- routing, model-pool, benchmark, trainer, submission and validator boundaries described by the repository

## Verified capabilities and patterns

### Router and evaluation direction

- Adapts the earlier TinyRouter/TRINITY direction into an SN74/Gittensor miner workspace.
- Uses a frozen 0.6B encoder and a small routing head to select a model and role.
- The coordinator is intentionally separated from the answering models.
- Supports a multi-turn loop with a Verifier role able to stop execution.
- Uses benchmark-specific automatic graders for math, multiple-choice and code tasks.
- Tracks model-pool performance, random routing and single-model baselines.
- Includes an oracle-ceiling diagnostic intended to determine whether routing headroom exists before spending effort on router improvement.
- Retains negative/inconclusive conclusions rather than claiming that an implemented change caused an improvement without a clean control.
- Tracks API cost and evaluation results.

### Submission and validator workflow

- Keeps submit-ready model checkpoints and metadata in a defined bundle.
- PR automation can package a submission, upload it to the validator, wait for status, comment results and optionally merge.
- The validator accepts PR/webhook or direct archive submissions.
- Submission metadata and artifact hashes are stored in Postgres.
- API intake and worker execution are separate processes.
- Evaluation runs through queued submission states and visible progress fields.
- The default path attempts remote GPU evaluation and falls back to local CPU execution.
- Submission-only and train-then-evaluate pipeline modes are explicit.
- Repeated webhook intake for the same PR is documented as idempotent.

## What MiniRouter contributes

- A concrete low-cost model/role routing experiment.
- Oracle-ceiling analysis before optimizing the router.
- Honest comparison with single-model and random baselines.
- Separation of coordinator, worker models and verifier role.
- Cost-aware evaluation.
- Submission bundles, queued validator jobs, progress reporting and result publication.
- A useful future workload for testing Ptah provider routing and evaluation Facilities.

## Important limitations for Ptah

- No repository licence was recovered, so code reuse, adaptation or distribution is not approved.
- The repository is a competition/miner workspace, not a general scheduler, Knowledge Facility or provider-neutral production router.
- The model pool, provider assumptions and role vocabulary are product/competition specific.
- Routing scores depend on benchmark, model pool, sampling, grader and provider availability.
- The published results explicitly include inconclusive and noisy comparisons.
- The validator shells out to local/remote repository environments and depends on prepared secrets and infrastructure.
- Remote GPU then local CPU fallback does not prove equivalent numerical/runtime behavior.
- A Verifier acceptance is a model/workload result, not Ptah proof or caller acceptance.
- Postgres queue state and GitHub PR automation are implementation details, not Ptah Activity identity.
- Automatic merge after evaluation is a competition workflow and cannot become a normal Ptah approval rule.
- The repository does not close provider permissions, credential isolation, durable retries, reproducibility or independent review.

## Must not be inherited

- MiniRouter as Ptah's reasoning or model-selection authority;
- its model names, roles, prompts or competition assumptions;
- benchmark scores generalized beyond the inspected experiment;
- Verifier acceptance treated as Sergeant review, operation proof or caller acceptance;
- GitHub PR merge treated as successful Activity proof;
- remote/local fallback reported as equivalent without conformance evidence;
- unlicensed source copied, adapted or distributed;
- Postgres submission IDs used as Ptah Activity or Artifact identity;
- automatic merge enabled by default;
- API keys or provider secrets stored in repo-root files as a Ptah pattern.

## Integration decision

**STUDY ONLY AND HOST LATER AS AN EXPERIMENTAL ROUTING/EVALUATION WORKLOAD.**

MiniRouter is not required to close WP10. It should move to the later distributed placement/routing and evaluation cluster, where Ptah can host its training/evaluation as receipted Activities and compare routing policies without embedding one router into Core.

No source reuse is permitted unless the owner publishes an explicit compatible licence or grants written permission.

## Native Ptah gap

Ptah must independently define:

- provider/model capability and cost snapshots;
- routing-policy identity and version;
- query/task classification inputs;
- caller-owned routing constraints;
- evaluation corpus, grader and oracle-ceiling records;
- attempt, seed, model/provider revision and sampling provenance;
- budget/resource controls;
- result comparison and confidence intervals;
- submission/checkpoint Artifact identities;
- durable validator Activities and independent review;
- promotion/activation gates for a routing policy;
- rollback and fallback policy.

## Exit strategy

Ptah routing/evaluation contracts remain independent and can use rules, learned routers, provider policies, MiniRouter, Ray workloads or future systems. MiniRouter remains an optional hosted workload.

## Validation required before any later adoption

1. Resolve the repository licence.
2. Pin the full model pool, prompts, grader, datasets, seeds and provider versions.
3. Reproduce baseline, random-router and learned-router results with confidence intervals.
4. Run oracle-ceiling analysis before accepting a routing-improvement claim.
5. Compare remote GPU and local CPU fallback behavior.
6. Treat every model/Verifier decision as workload evidence rather than Ptah proof.
7. Store checkpoints and submissions as immutable Artifacts with hashes.
8. Run validator jobs as durable Activities with attempts, cancellation and resource accounting.
9. Disable automatic merge until independent acceptance policy approves it.
10. Remove MiniRouter without changing Ptah provider, routing-policy or Activity identity.
