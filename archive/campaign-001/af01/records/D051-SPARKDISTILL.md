# D051 — SparkDistill Archive Record

Outcome: ACCEPTED FOR ARCHIVE WITH RIGHTS/PROOF RESTRICTIONS — optional reproduction workload only

Campaign: `CAMPAIGN-001`

Formation: `AF01`

Primary Archivist: `AF01-P09`

Independent Verifier: `AF01-V09`

Archive Officer outcome date: 2026-07-21

## Canonical source

- repository: `gittensor-model-hub/SparkDistill`;
- owner: Gittensor Model Hub organization;
- visibility: public;
- archived: false;
- default branch: `main`;
- inspected commit: `6fb8857fba4bfa29dd74f1ab43619e517b601225`;
- inspected repository state: current head recovered on 2026-07-21.

## Rights and maintenance

- root code licence: MIT;
- licence evidence: `LICENSE` blob `43eec995fa9bc2fc3b8ade76f99fef47a11b5817`;
- dataset, teacher-output, model, benchmark, API-provider, checkpoint, Hugging Face and generated reasoning rights are independent and are not granted by the root code licence;
- confidential-computing/attestation SDK and service dependencies require separate lifecycle review;
- activity state: active; inspected head strengthens TDX claim binding to quote REPORTDATA rather than editable JSON.

## Primary evidence packet — AF01-P09

Inspected:

- `README.md` blob `099c3004ff656656ed3af4a9fb99a617e21ad0f0`;
- `eval/attestation.py` blob `5dff16cbef005f01b820bac71099e912f42ebf91`;
- root `LICENSE`;
- exact current head.

Verified:

- SparkDistill is a competition/research system for dataset generation, training recipes, evaluation claims and reproducibility workflows around Triton-focused student models;
- repository separates recipes/datasets/eval claims from trained checkpoints and uses retraining or bounded re-scoring as verification paths;
- proof bundles include claims and checkpoint file digests rather than merging model weights;
- attestation code binds a claim digest through NVIDIA remote attestation nonce handling and supports TDX REPORTDATA extraction;
- the source explicitly distinguishes unverified JWT decoding for display from signature/policy validation that determines pass/fail;
- production proof paths depend on specific GPUs, confidential-computing infrastructure and remote attestation services;
- the installed Python NVIDIA attestation SDK is noted as EOL on 2026-09-15, with replacement-language/binding constraints.

Primary conclusion:

SparkDistill is a useful proof/reproduction workload donor for claim/dataset/recipe/checkpoint separation, retraining, recheck and attestation-binding patterns. Its internal “trustless” language and competition gates must not be treated as universal proof, Ptah Receipt authority or a licence for datasets/models/provider outputs.

## Independent verification packet — AF01-V09

Repeated checks:

- canonical identity, `main` branch and exact inspected head;
- MIT root code licence;
- actual attestation source and trust-boundary comments;
- nonce/claim binding and TDX quote parsing;
- external NVIDIA service/SDK and GPU requirements;
- root code rights are distinct from model/dataset/output rights.

Challenges retained:

- cryptographic attestation proves bounded measured claims, not semantic quality, lawful data provenance or universal reproducibility;
- remote services, hardware, drivers, policies and SDK lifecycle are dependencies that may fail or change;
- teacher reasoning/outputs and datasets may carry provider or copyright restrictions;
- competition scoring and frontier status are not Ptah truth;
- claims, recipes, datasets, checkpoints, eval runs and attestations must remain separate Objects/Receipts.

Verifier conclusion: primary findings supported. Frozen proof/reproduction donor placement remains correct with stronger rights and dependency restrictions.

## Ptah relationship

- frozen donor group: Provenance, artifact integrity and security evidence / proof and reproducibility;
- current classification: optional research/reproduction workload and architecture study;
- requirements supported: claim/evidence separation, recipe/dataset/checkpoint lineage, retrain/recheck gates, content-digest binding, attestation and negative-path proof ideas;
- prohibited inheritance: competition ledger as Ptah authority, attestation pass as universal proof, model/dataset rights inferred from MIT code, provider reasoning traces as automatically reusable data;
- replacement/exit strategy: retain native Ptah Receipt/Artifact/claim contracts and use independently verified attestation/reproduction backends.

## Contradiction and supersession

- no canonical-identity contradiction found;
- current source confirms the frozen `gittensor-model-hub/SparkDistill` identity;
- current TDX/claim-binding implementation supersedes earlier generic proof descriptions while preserving the rule that recipe, dataset, checkpoint, claim and attestation are separate.

## Bounded outcome

`accepted for archive with rights/proof restrictions` does not authorize training, dataset/model/provider use, attestation-service reliance, source deployment, Phase 0A reopening, ADR-0033 acceptance or Ptah runtime implementation.
