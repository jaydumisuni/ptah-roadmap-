# Donor Record — MiniRouter

**Phase:** 0A / WP10 boundary check; later distributed routing/evaluation cluster  
**Status:** CANONICAL REPOSITORY RECOVERED — STUDY-ONLY, LICENCE UNRESOLVED, NOT REQUIRED FOR WP10 CLOSURE  
**Inspected:** 2026-07-18

## Identity

- Current canonical repository: https://github.com/mini-router/minirouter
- Current owner/organisation: `mini-router`
- Default branch: `main`
- Pinned current commit: `520982b737f4fb78e855d042e85cd1e6c23fd75c`
- Prior discovery/lineage repository: https://github.com/tmimmanuel/minirouter
- Prior lineage pin inspected: `bf3ea957f6ef3de358528f73e0518ec51e39d8f3`
- Related competition repository: https://github.com/tmimmanuel/minirouter-competition
- Package name: `trinity-coordinator`
- Package version: `0.0.1`
- Licence: **UNRESOLVED — no root `LICENSE` file found and no licence field was recovered from `pyproject.toml`**
- Activity: Active
- Classification: experimental query router, model-role coordinator, evaluation pipeline and competition-validator donor
- Ptah targets: future routing-quality evaluation, provider-selection experiments, submission/evaluation Activities and proof dashboards; not Ptah Core reasoning and not required for Knowledge/Data/Search/Plugin closure

## Canonical-location decision

The organization repository contains the same MiniRouter/TinyRouter/TRINITY lineage and has newer active development than the earlier `tmimmanuel/minirouter` location. The organization repository is therefore the current canonical inspection target; the `tmimmanuel` repository is retained as lineage evidence rather than discarded.

This location correction does not change the licence decision: source reuse remains unapproved until an explicit compatible licence is published or written permission is obtained.

## Files/components inspected

- current and lineage `README.md`
- current `pyproject.toml`
- `src/trinity/eval.py`
- current provider-route evaluation commit evidence
- validator/competition workflow descriptions
- routing, model-pool, benchmark, trainer, submission and validator boundaries

## Verified capabilities and patterns

### Router and model-role separation

- Adapts the earlier TinyRouter/TRINITY direction into an SN74/Gittensor miner workspace.
- Uses a frozen 0.6B encoder and a small routing head to select a model and role.
- The coordinator is intentionally separated from the answering models and does not solve the task itself.
- Supports a multi-turn loop with thinker, worker and verifier-style roles and a Verifier able to stop execution.
- Model pools are external HTTP providers rather than one embedded model.
- Current provider configuration can combine multiple OpenAI-compatible services and logical model-route aliases.

### Evaluation design

- Compares a trained coordinator against each single model and random routing.
- Supports benchmark-specific automatic graders for math, multiple-choice and code tasks.
- Supports repeated runs, standard-deviation reporting, selected model routes and multiple benchmarks.
- Per-request and per-trajectory timeouts are explicit.
- Failed trajectories are retained as failed/zero-scored outcomes rather than disappearing.
- Evaluation outputs retain selected benchmarks, pool models, repeated values, aggregate metrics, runtime and cost.
- Includes an oracle-ceiling diagnostic intended to determine whether routing headroom exists before spending effort on router improvement.
- Retains negative/inconclusive conclusions rather than claiming that an implemented change caused an improvement without a clean control.
- Tracks API cost and evaluation results.

### Submission and validator workflow

- Keeps submit-ready model checkpoints and metadata in a defined bundle.
- PR automation can label and register submissions, leave them pending until manual dispatch, upload bundles to a validator worker and publish results back to the PR.
- The validator stores submissions and evaluation runs in Postgres.
- API intake and worker evaluation are separate processes.
- Submission-only and train-then-evaluate pipeline modes are explicit.
- Submit-ready content includes the trained routing head plus summary/history/evaluation metadata.
- Current evaluation improvements include provider-route evaluation jobs and configurable batching/repeats.

### Honest findings in the project record

- The router's reported advantage is across tasks with materially different model strengths, not automatically within every benchmark.
- Where models perform similarly, routing can tie random or best-single behavior.
- The project explicitly distinguishes detected theoretical headroom from demonstrated router improvement.
- A measured change is labelled inconclusive when sampling noise and missing controls prevent a causal claim.

## What MiniRouter contributes

- A concrete low-cost model/role routing experiment.
- Separation of coordinator, model pool and verifier role.
- Oracle-ceiling analysis before optimizing the router.
- Honest comparison with single-model and random baselines.
- Repeated-run and variance evidence rather than only one score.
- Cost-aware evaluation and provider-route comparison.
- Submission bundles, queued validator jobs, progress reporting and result publication.
- A useful future workload for testing Ptah Model Facility routing and evaluation contracts.
- Useful evidence that routing policy quality depends on the model pool and benchmark rather than one universal router.

## Important limitations for Ptah

- No repository licence was recovered, so code reuse, adaptation or distribution is not approved.
- The repository is a competition/miner workspace, not a general scheduler, Knowledge Facility or provider-neutral production router.
- The model pool, provider assumptions and role vocabulary are product/competition specific.
- Routing scores depend on benchmark, model pool, sampling, prompt, grader, provider and model revisions.
- The published results explicitly include inconclusive and noisy comparisons.
- Automatic graders can be wrong or incomplete and do not replace independent acceptance.
- The validator depends on prepared secrets, external providers, GPU/CPU environments and competition infrastructure.
- Remote GPU and local CPU execution do not prove equivalent numerical/runtime behavior.
- A Verifier acceptance is a model/workload result, not Ptah proof or caller acceptance.
- Postgres queue state and GitHub PR automation are implementation details, not Ptah Activity identity.
- Automatic merge after evaluation is a competition workflow and cannot become a normal Ptah approval rule.
- The repository does not close provider permissions, credential isolation, durable retries, reproducibility or independent review.
- The small router/head is trained for a specific model pool; replacing models can invalidate the learned policy.
- A model provider route name is not stable model identity.

## Must not be inherited

- MiniRouter as Ptah's reasoning or model-selection authority;
- its model names, roles, prompts or competition assumptions;
- benchmark scores generalized beyond the exact inspected experiment;
- Verifier acceptance treated as Sergeant review, operation proof or caller acceptance;
- GitHub PR merge treated as successful Activity proof;
- remote/local fallback reported as equivalent without conformance evidence;
- unlicensed source copied, adapted or distributed;
- Postgres submission IDs used as Ptah Activity or Artifact identity;
- automatic merge enabled by default;
- API keys or provider secrets stored in repo-root files as a Ptah pattern;
- a trained router reused after the model pool, provider or benchmark contract changes;
- failed trajectories omitted from evaluation evidence.

## Integration decision

**STUDY ONLY AND HOST LATER AS AN EXPERIMENTAL ROUTING/EVALUATION WORKLOAD.**

MiniRouter is not required to close WP10. It belongs in the later distributed placement/routing and evaluation cluster, where Ptah can host training/evaluation as receipted Activities and compare routing policies without embedding one router into Core.

No source reuse is permitted unless the owner publishes an explicit compatible licence or grants written permission.

Recommended future relationship:

1. Ptah owns Model Provider, Model Revision, Routing Policy, Evaluation Dataset and Run identities.
2. MiniRouter executes as a versioned workload against an exact model pool and benchmark revision.
3. Every provider/model response, seed, role decision, transcript, grader result, failure and cost becomes evidence.
4. Router promotion requires independent evaluation and caller policy approval.
5. Hunter or another caller may choose whether to use an approved routing policy; Ptah does not own that reasoning decision.

## Native Ptah gap

Ptah must independently define:

- provider/model capability and cost snapshots;
- stable Model Provider and Model Revision identity;
- routing-policy identity, revision and activation;
- query/task classification inputs;
- caller-owned routing constraints;
- evaluation corpus, grader and oracle-ceiling records;
- attempt, seed, prompt, model/provider revision and sampling provenance;
- transcript/role/decision evidence;
- budget/resource controls;
- result comparison and confidence intervals;
- submission/checkpoint Artifact identities;
- durable validator Activities and independent review;
- promotion/activation gates for a routing policy;
- rollback and fallback policy;
- model-pool change invalidation.

## Exit strategy

Ptah routing/evaluation contracts remain independent and can use static rules, learned routers, provider policies, MiniRouter, Ray workloads or future systems. MiniRouter remains an optional hosted workload.

## Validation required before any later adoption

1. Resolve the repository licence.
2. Pin the full model pool, provider endpoints, prompts, grader, datasets, seeds and model revisions.
3. Reproduce single-model, random-router and learned-router results with repeated runs and confidence intervals.
4. Run oracle-ceiling analysis before accepting a routing-improvement claim.
5. Compare remote GPU and local CPU behavior.
6. Treat every model/Verifier decision as workload evidence rather than Ptah proof.
7. Store checkpoints and submissions as immutable Artifacts with hashes.
8. Run validator jobs as durable Activities with attempts, cancellation and resource accounting.
9. Retain failures and timeouts in evaluation results.
10. Disable automatic merge until independent acceptance policy approves it.
11. Replace one model/provider and prove the prior routing policy is marked incompatible or re-evaluated.
12. Remove MiniRouter without changing Ptah provider, routing-policy or Activity identity.
