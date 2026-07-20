# Phase 0C-05 — WP14 implementation task and proof map

Status: candidate — runtime implementation remains unauthorized

## Purpose

Translate the frozen WP14 proof plan into an ordered implementation task graph. A task is not complete because code exists; it is complete only when its positive and negative proof evidence is retained at the exact implementation commit.

## Delivery rule

Every task below must produce:

- canonical Ptah records;
- exact backend/Provider generation evidence;
- Activities, Operations and Attempts where applicable;
- immutable reports and Artifacts;
- retained negative-path evidence;
- a deterministic conformance case;
- no internet schema resolution.

## Ordered task graph

### P0C-I001 — Repository and contract lock scaffold

Deliver:

- accepted workspace layout;
- Rust and Node toolchain pins;
- `contracts/upstream-lock.json` bound to the Phase 0B freeze;
- reproducible generated bindings;
- dependency and licence inventory;
- CI skeleton.

Proofs:

- generated output is identical on a clean run;
- altered catalog digest fails;
- network-disabled generation passes;
- private/restricted paths are absent from public packaging.

### P0C-I002 — Node identity and generation substrate

Deliver:

- stable Node identity;
- Node Generation record for each agent start;
- host capability report;
- structured Event/Receipt correlation.

Proofs:

- Node identity survives restart;
- generation changes after restart;
- stale-generation commands are rejected and retained;
- process ID and boot ID do not replace Node identity.

### P0C-I003 — Ledger and migration substrate

Deliver:

- SQLite WAL backend behind `ptah-ledger` interfaces;
- schema-version registry;
- directional migrations;
- crash-safe transaction and checkpoint policy.

Proofs:

- restart preserves records;
- incomplete transaction does not manufacture success;
- migration replay is deterministic;
- backend-specific row IDs never escape as canonical identity.

### P0C-I004 — Activity, Operation and Attempt runtime

Deliver:

- independent lifecycle machines;
- cancellation and failure propagation;
- retry creates a new Attempt;
- event streaming and Receipts.

Proofs:

- at least ten concurrent Activities execute independently;
- one failure does not collapse unrelated Activities;
- cancellation is scoped;
- reused Attempt identity is rejected;
- acknowledgement-only completion is rejected.

### P0C-I005 — PTY and multi-terminal Provider

Deliver:

- independent PTY-backed terminal Activities;
- streamed stdout/stderr;
- resize, detach and reconnect support;
- terminal Provider generation.

Proofs:

- multiple terminals remain independent;
- client disconnect does not terminate the terminal unless policy says so;
- stale terminal attachment is fenced;
- output ordering and truncation limitations are retained.

### P0C-I006 — Persistent Workspace and Session

Deliver:

- one persistent Workspace;
- Session attach/detach;
- Workspace-scoped Objects, Activities and terminals;
- restart recovery projection.

Proofs:

- Workspace identity survives client disconnect and runtime restart;
- Session identity changes where required without replacing Workspace identity;
- missing attachments are reported, not silently recreated;
- stale Session authority is rejected.

### P0C-I007 — Object, Revision, Artifact and local CAS

Deliver:

- Object registration;
- immutable Revision records;
- digest-addressed Artifact bytes;
- Location and provenance records.

Proofs:

- identical bytes may deduplicate without collapsing distinct logical Objects;
- changed bytes create distinct Content/Artifact identity;
- storage path changes preserve Artifact identity;
- digest mismatch blocks registration.

### P0C-I008 — Resumable transfer engine

Deliver:

- upload;
- resumable download;
- retained partial state;
- streaming digest and destination read-back.

Proofs:

- interrupted transfer resumes from retained state;
- corrupted partial data is detected;
- provider acknowledgement cannot claim completion;
- path traversal and destination escape are rejected;
- exact source/destination digests are retained.

### P0C-I009 — Hardened Git Provider

Deliver:

- clone or mirror as a receipted Activity;
- protocol allow-list;
- hook suppression;
- explicit submodule and LFS policy;
- repository Object/Revision projection.

Proofs:

- exact remote and resolved commit are retained;
- disallowed protocols fail closed;
- malicious hooks do not execute;
- backend worktree paths remain Locations/Aliases;
- failed clone evidence is retained.

### P0C-I010 — OCI container Provider

Deliver:

- isolated container execution through pinned containerd/runc;
- capability declaration;
- Provider generation;
- stdout/stderr and exit evidence;
- image digest binding.

Proofs:

- container backend IDs remain Aliases;
- image tag without digest is insufficient for exact proof;
- container start ACK does not equal workload success;
- stale Provider generation is rejected;
- one backend-replacement simulation preserves Ptah identity.

### P0C-I011 — Browser Provider

Deliver:

- Playwright/Chromium service;
- persistent Browser Profile;
- Browser Process, Context, Page and generation projections;
- navigation, download and reconnect evidence.

Proofs:

- persistent profile survives Provider restart where policy permits;
- stale Page/Context generation is rejected;
- navigation ACK does not equal postcondition success;
- private browser data is not emitted into public logs;
- browser/backend IDs remain Aliases.

### P0C-I012 — Archive decomposition Provider

Deliver:

- libarchive-backed read-only decomposition;
- child Object/View registration;
- coverage and limitation reporting;
- encrypted, malformed and partial handling.

Proofs:

- source Object remains unchanged;
- unknown and skipped ranges remain explicit;
- path traversal entries cannot escape materialization root;
- malformed archive does not produce complete coverage;
- backend replacement preserves source and decomposition identity rules.

### P0C-I013 — Checkpoint, restart and verified recovery

Deliver:

- checkpoint request/result;
- process/Workspace metadata capture;
- agent restart;
- recovery run and independent verification.

Proofs:

- checkpoint existence does not equal restored runtime;
- recovery creates a new generation;
- stale Leases/fences do not survive restart;
- missing or partial recovery evidence yields failed/inconclusive state;
- retained Activities and terminal attachments reconcile explicitly.

### P0C-I014 — Exact-head vertical-slice acceptance run

Deliver:

- clean host image revision;
- exact dependency lock;
- all required positive and negative cases;
- immutable report bundle;
- limitations record;
- implementation commit digest.

Proofs:

- WP13 structural and semantic conformance passes;
- WP14 first-slice suite passes at the exact commit;
- offline schema-resolution case passes;
- immutable reports, Receipts, logs and Artifacts are uploaded and digest-bound;
- a green summary without reports fails acceptance.

## Mandatory cross-cutting negative proofs

Every applicable task must cover:

- stale Provider generation;
- stale Lease/fence;
- reused Attempt;
- raw secret leakage;
- ACK-as-success;
- path traversal;
- partial transfer overclaim;
- stale semantic UI target;
- recovery without new-generation verification;
- backend ID promoted to canonical identity;
- deleted or hidden failure evidence.

## Sequencing

```text
I001
  -> I002 -> I003 -> I004
  -> I005 + I006
  -> I007 -> I008
  -> I009 + I010 + I011 + I012
  -> I013
  -> I014
```

Adapters may be developed in parallel only after I001-I004 establish the identity, ledger and execution substrate they must consume.

## Authorization boundary

This map authorizes no runtime code by itself. It becomes the implementation authority only after ADR-0033 is accepted and `CURRENT_STATE.md` explicitly changes to `Runtime implementation: AUTHORIZED`.