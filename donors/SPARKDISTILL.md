# Donor Record — SparkDistill

**Phase:** 0A / Security and reproduction completion  
**Status:** FIRST-PASS COMPLETE — OPTIONAL MODEL-TRAINING REPRODUCTION/CLAIM-VERIFICATION WORKLOAD, NOT PTAH CORE  
**Inspected:** 2026-07-18

## Identity

- Canonical organization repository: https://github.com/gittensor-model-hub/SparkDistill
- Default branch: `main`
- Pinned commit: `8721faaf9e7a6464df32a74a6fa0e9ff6435e878`
- Licence: MIT for repository source; datasets, teacher outputs, models, checkpoints and external services require independent terms/licence review
- Activity: Active
- Primary language: Python/configuration/CI workflows
- Classification: model-distillation, dataset proof, reproducible training recipe, attested claim, evaluation gate and immutable run-ledger workload donor
- Ptah targets: reproducible AI workload claims, recipe/dataset/checkpoint separation, held-out evaluation, attested claim binding and retrain/read-back proof

## Canonical-repository finding

- GitHub search returns many near-identical `SparkDistill` forks/copies.
- The inspected repository identifies `gittensor-model-hub/SparkDistill` and related `gittensor-model-hub/SparkProof`/dataset resources as the project-owned paths.
- Ptah must retain exact owner/repository/commit and must never resolve this donor from name alone.

## Files/components inspected

- `README.md`
- `LICENSE`
- current repository/commit activity
- documented teacher, recipe, evaluation, proof, dataset registry and immutable run-ledger flows

## Verified capabilities and patterns

### Recipe and data as source truth

- Training submissions center on a public recipe plus dataset rather than trusting submitted checkpoint weights.
- Miners train/score locally and submit recipe, dataset reference and claimed evaluation results.
- The evaluator can retrain from the exact recipe/dataset and re-score against the current frontier.
- Trained weights are not the merged source artifact in the described workflow.
- Canonical dataset aggregation retains a mix manifest/provenance and is gated before merge.

### Claim and attestation path

- A proof bundle can carry evaluation/training claims and per-file checkpoint hashes without uploading the weights.
- The claim digest can be bound as a nonce to confidential-computing/GPU attestation.
- A validator locally reproduces the checkpoint from recipe/data and re-runs a held-out subset or full path according to policy.
- Attestation is therefore one input to validation rather than a replacement for recipe/data availability and local re-check.
- Unattested submissions follow a slower full retrain path.

### Evaluation and ledger

- Evaluation compares students against teacher/frontier checkpoints over named benchmark suites.
- Marginal improvement and dataset quality are evaluated through deterministic harness/gate policy as described by the project.
- Merged verified runs are appended to an immutable JSONL ledger.
- Dataset proof bundles can be verified offline from published proof directories, while optional online checks validate attestation signatures.
- The repository explicitly distinguishes claims, proof bundle, recipe/dataset, checkpoint and validator re-execution.

## What SparkDistill contributes

- Strong separation of recipe/data, checkpoint bytes, evaluation claim and validation.
- Retrain-from-source as a higher evidence level than accepting uploaded weights.
- Per-file checkpoint hashes and claim-digest binding.
- Confidential-computing/GPU attestation as contextual evidence.
- Held-out re-score and full-retrain verification paths.
- Immutable run ledger and canonical dataset registry/mix manifest patterns.
- A realistic AI-training workload for Ptah reproduction, placement, GPU and evidence Facilities.
- Evidence that reward/merge policy should be based on verified marginal improvement rather than self-reported metrics.

## Important limitations for Ptah

- SparkDistill is a specialist AI-mining/training product, not a generic reproduction or security system.
- Current teacher/student models, Triton/GPU targets, benchmark suites and reward tiers are product-specific.
- Teacher trajectories may include proprietary provider outputs or reasoning traces with contractual, privacy and policy restrictions.
- A public recipe/dataset does not guarantee identical weights across GPU, kernel, library, compiler, seed and nondeterministic execution differences.
- Held-out re-score is a bounded check and can miss training-data leakage, benchmark gaming or broader regressions.
- Confidential-computing attestation proves a measured environment/nonce under one trust chain, not semantic correctness of training or claims.
- Hardware/driver/attestation dependencies are vendor- and version-specific.
- Dataset registry and Hugging Face resources are external mutable/availability dependencies unless exact revisions/hashes are retained.
- Hash manifests prove byte identity, not quality, licence or absence of malicious content.
- CI/validator policy and maintainer-owned harness can change.
- Run-ledger append/merge does not equal independent review or universal model quality.
- Many similarly named repositories increase hallucination/supply-chain risk.
- SparkDistill does not own Ptah reasoning, model policy, Build identity, Activity proof or release acceptance.

## Must not be inherited

- SparkDistill/miner/PR/run IDs as canonical Ptah identities;
- repository name resolved without exact owner/commit;
- teacher reasoning/chain-of-thought captured, published or trained on without explicit rights/policy;
- current model names, reward tiers, benchmarks or GPU vendor embedded into Ptah Core;
- attestation interpreted as proof that the model/claim is correct;
- per-file hash manifest interpreted as licence/safety/quality proof;
- held-out subset re-score reported as full reproduction;
- successful retraining assumed byte-identical across environments;
- Hugging Face URL/tag used without exact dataset revision and hashes;
- verifier/CI merge treated as Sergeant review or caller acceptance;
- generated/trained model automatically activated in Hunter or another caller.

## Integration decision

**HOST SPARKDISTILL ONLY AS AN OPTIONAL AI-TRAINING/REPRODUCTION WORKLOAD AND ADAPT ITS RECIPE–DATA–CHECKPOINT–CLAIM–ATTESTATION–RECHECK SEPARATION; DO NOT USE IT AS PTAH CORE.**

Recommended Ptah role:

1. recipe, dataset, base model, toolchain, environment and evaluation protocol are immutable versioned Objects;
2. training is a GPU/accelerator Activity with exact Node/Provider/hardware/software/seed/resource receipts;
3. checkpoints are immutable Artifacts with manifests and optional restricted storage;
4. self-reported metrics are Claims, never accepted results;
5. attestation evidence binds exact claim/environment but remains one evidence input;
6. validation runs are new independent Activities using frozen protocols and held-out data;
7. full retrain, partial re-score and artifact-only verification retain different reproduction levels;
8. dataset/model/provider licences and usage rights are release gates;
9. benchmark leakage, stochastic variance and environment drift are explicit;
10. promotion into a caller product requires separate owner/department decision and review;
11. exact canonical repository/source pins prevent hallucinated/fork substitution;
12. SparkDistill can be removed without changing Ptah Recipe, Dataset, Model Artifact, Claim or Evidence identities.

## Native Ptah gap

Ptah must define:

- Model Training Recipe and Revision;
- Dataset and Dataset Revision/mix manifest;
- Base Model and licence/source revision;
- Training Activity, Node/accelerator/software/seed/resource evidence;
- Checkpoint Artifact and per-file manifest;
- Evaluation Protocol, corpus, split and contamination controls;
- Metric Claim and allowed claim boundary;
- Attestation Evidence, trust chain, nonce binding and freshness;
- validation levels: manifest-only, re-score, partial retrain, full retrain, independent reproduction;
- stochastic comparison/confidence and tolerance policy;
- model/dataset/provider rights and privacy records;
- run ledger/supersession without historical rewrite;
- promotion/release/activation review separate from benchmark gate;
- canonical repository/package resolution and anti-hallucination controls.

## Exit strategy

Ptah's AI-training/reproduction contracts remain workload-neutral. SparkDistill, Axolotl, TRL, custom training pipelines, Ray jobs or future systems can run without changing Dataset, Recipe, Training Activity, Model Artifact, Claim or Validation identity.

## Validation required

1. Pin recipe, dataset, base model, toolchain, seed and exact accelerator/software environment.
2. run the same recipe twice and quantify expected nondeterminism rather than assuming byte identity.
3. verify checkpoint hashes without treating that as metric correctness.
4. bind a claim digest to valid, invalid, stale and mismatched attestation evidence.
5. compare held-out re-score, partial retrain and full retrain as separate reproduction levels.
6. detect a mutable/forked/hallucinated repository or dataset reference.
7. run contamination/leakage and benchmark-gaming checks.
8. reject teacher/dataset/model content with unresolved licence or privacy rights.
9. preserve a failed or regressed reproduction in the run ledger.
10. prove model activation requires a separate caller/department decision.
11. replace SparkDistill without identity loss.
