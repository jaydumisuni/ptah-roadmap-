# Phase 0C-11 — Runtime dependency, backend signer and host-collector evidence

Status: passed for exact Rust dependency, distributed backend artifact, signer and host-collector scope — pinned-host package proof and runtime authorization remain open

Reviewed: 2026-07-20

## Purpose

Record the exact Phase 0C evidence merged from `jaydumisuni/Ptah-space` PR `#6` without treating a generic hosted runner, a dependency lock, a downloaded backend, a cryptographic signature or a green workflow as proof that the Ptah runtime exists.

## Accepted implementation evidence

Repository: `jaydumisuni/Ptah-space`

Pull request: `#6`

Exact tested head:

```text
bc12885ce41844b05481628543219c3a8d3574ba
```

Squash merge commit:

```text
c2cd803b5e5c50787b3d8c2d24392d693afdbb3c
```

Every accepted record and report retains `runtime_implementation_authorized: false` or the equivalent host `runtime_authorized: false` boundary.

## Exact Rust dependency graph

The selected evidence-only Rust graph records:

- direct dependency count: `10`;
- resolved package count: `99`;
- crates.io registry package count: `81`;
- Git dependency count: `0`;
- toolchain: Rust `1.97.1`;
- `Cargo.lock` SHA-256: `d68a06272d417d67049c7879570e3735607166ce1e7eff58e43df21e20c9117a`;
- exact manifest versions with no wildcard or unknown-registry dependencies;
- default features disabled where practical;
- private unpublished Ptah workspace crates excluded from public-licence inference until the owner decision.

The ten direct crates are `nix`, `rusqlite`, `serde`, `serde_json`, `sha2`, `thiserror`, `tokio`, `tracing`, `tracing-subscriber` and `uuid`, each at the exact version, feature set, registry source and checksum recorded in `dependencies/rust-direct-lock.json`.

`cargo-deny 0.19.4` passed advisory, ban, licence and source policy. The allowed external licence set includes the selected MIT, Apache-2.0, dual MIT/Apache-2.0 and required transitive Zlib terms. This does not grant a public licence to Ptah-owned source.

## Locked distributed backend artifacts

`dependencies/backend-artifact-lock.json` contains nine selected artifact identities with authoritative digests:

1. Ubuntu Server 24.04.4 amd64 installation image;
2. containerd `2.3.1` Linux amd64 archive;
3. runc `1.4.2` amd64 binary;
4. Node.js `24.18.0` Linux x64 archive;
5. SQLite `3.53.3` source archive;
6. libarchive `3.8.7` source archive;
7. Git `2.55.0` source archive;
8. Playwright `1.60.0` npm package;
9. Playwright Core `1.60.0` npm package.

The exact-head verifier downloaded each selected artifact from its recorded authoritative source, recomputed its digest and compared the result with the immutable lock. Node.js and Git archive digests were extracted from their downloaded signed checksum manifests in the same run.

This closes distributed/source artifact identity for the selected first-slice candidates. It does not close the exact installed Ubuntu package manifest or package-artifact digest set from the pinned host.

## Playwright Chromium evidence

The first Browser Provider binary is locked as:

- Playwright: `1.60.0`;
- Chromium version: `148.0.7778.96`;
- revision: `1223`;
- descriptor SHA-256: `aa17537f6cd5f342009e330606349a6ca8c4bf3e02bf5318d607c865def2b947`;
- installed-tree SHA-256: `953a2e9c1fb18d1e698f0903a62c23c835264e939cdd08a85c41d57719a5de7a`;
- installed file count: `599`;
- installed size: `669473388` bytes;
- Chromium executable SHA-256: `adc1c21ceed5c2a67184766376fe816ac03e556cc0ca3f782e8212235fe05c6f`.

The tree was recreated and compared with the immutable lock at the final exact head. This proves selected Browser artifact reproducibility, not an implemented Browser Facility.

## Cryptographic signing authority evidence

`dependencies/signing-key-lock.json` pins stable signing authority for:

- Node.js through exact commit `b28073028e6d6855cfb53bf7fa0137599c01f967` of `nodejs/release-keys`;
- runc through the `v1.4.2` release keyring, keyring SHA-256 `9bd9742cb79b215cf5f7f71ea71a51a2a95ab573412d54c2905be072d8fcab7c` and verified primary fingerprint `C2428CD75720FACDCF76B6EA17DE5ECB75A1100E`;
- Git through Junio C Hamano primary fingerprint `96E07AF25771955980DAD10020D04E5A713660A7`, independently anchored by kernel.org;
- libarchive through fingerprint `659C84C0E23EA1FA97E0B58CC040B508D63D2B36`, independently anchored by Gentoo project-key metadata.

The final signature workflow cryptographically verified Node.js, runc, Git and libarchive at the exact candidate head. Its first attempt encountered an upstream HTTP `504` while redownloading libarchive; the independent immutable artifact lane had already passed the same locked archive. The failed signature job alone was rerun, and attempt `2` completed all four signature checks without changing any lock.

## Host capability collector evidence

The deliberate host-collector placeholder was replaced with a stdlib-only, fail-closed collector covering all eighteen required capabilities:

- systemd;
- unified cgroups v2;
- PID, mount, UTS, IPC, network and user namespaces;
- seccomp;
- overlayfs;
- Unix-domain sockets;
- PTY resize;
- file and directory `fsync`;
- atomic rename;
- advisory locking;
- inotify;
- monotonic clock;
- offline schema resolution.

AppArmor remains conditional under the explicit `required_or_explicit_reduced_isolation_limitation` policy.

The collector and separate identity finalizer use realistic Ubuntu fields:

- `ID=ubuntu` for distribution identity;
- `VERSION_ID=24.04` for the base release;
- `VERSION` or `PRETTY_NAME` for the exact `24.04.4` point release;
- normalized `amd64`/`x86_64` architecture identity;
- exact prefix match for `6.8.0-136-generic`.

Malformed or missing frozen-contract input produces a normal failed observation rather than aborting the report. A generic GitHub-hosted Ubuntu runner may validate collector behavior and observable capabilities, but it is not proof-eligible unless the complete frozen image and kernel identity match.

The final hosted-run report passed every required capability and retained `proof_eligible: false` because hosted-runner identity is not the accepted pinned-host proof.

## Exact-head workflow and artifact evidence

All eight workflows passed at exact head `bc12885ce41844b05481628543219c3a8d3574ba`:

| Lane | Workflow run | Accepted artifact ID | Artifact SHA-256 |
|---|---:|---:|---|
| Static backend artifacts | `29753904165` | `8465773509` | `3f9321ae3dd7c8b75e896e0617c8c0a5aeacffa10ae9d861aa3a6e2f722f0030` |
| Playwright Browser artifact | `29753904165` | `8465777588` | `8bdf6aaea0a5b12835c1ad3a85389585de36ba684609b75b5a7b6b55b9cdf74b` |
| Rust scaffold | `29753904248` | `8465784889` | `1ca20cd3f1f2545e0e0afa6448f5cbb267dc74247239caddec200c780de48c0c` |
| Browser scaffold | `29753904248` | `8465772620` | `47231c5b95aa7a9e3105edd0932d3e0439e5fc745d1274d236661dcb246aea63` |
| Source/no-build policy | `29753904248` | `8465767734` | `80c8e9ea5789f95d79ed0754ba23013b558b700a41622edb591c35f0e38603be` |
| Frozen WP13 conformance | `29753904248` | `8465775702` | `6284ad270f3de2f30624053a9e309a02dfabae7d62c98f8950dde1afce7afa3a` |
| Frozen contract lock | `29753904209` | `8465769568` | `37e0b35c974f5eca2478dd9b4dafeea8a42cad855df38e520f852b7dab13dcaf` |
| Generated contract bindings | `29753904343` | `8465770240` | `ca98a8cdc6c0d407f3ca678c324aa30faa84c9305262ebc6c6e850a33c0b8af3` |
| Signing-lock boundary | `29753904295` | `8465768371` | `5f3a7b44c55083de45859cf4ee4229869939f262436bdec4b48728e91469b666` |
| Host capabilities | `29753904322` | `8465769622` | `de7e0bc3ed839fbd8b940b5663df59343c5522671d7a9df5e3896f6e343cf395` |
| Rust dependency policy | `29753904225` | `8465841717` | `83375db163158dfab55f3f50290e76c57f154919e4df2b2319f1f11723641725` |
| Backend signatures, successful retry | `29753904185` | `8465852502` | `8b0c63152ec23db0ea7af3555cbf918297b792bf49944acf9580a611e117cb02` |

The first failed backend-signature attempt artifact `8465790976` is retained as negative evidence with SHA-256 `ae90e01762f9721bae05ad82a8e78e3f845cfb93f3641ceb38b2d490935c51ed`.

## Conditions closed

This evidence closes, at Phase 0C candidate/evidence scope:

1. selection of the minimal direct Rust crate/features graph;
2. exact final `Cargo.lock` generation for that graph;
3. crates.io source and checksum inventory;
4. zero-Git-dependency enforcement;
5. crate advisory, ban, licence and source policy at the exact candidate head;
6. authoritative identity and digest verification for all nine selected distributed/source artifacts;
7. reproducible Playwright Chromium revision and installed-tree evidence;
8. stable signing-authority locks and cryptographic verification for Node.js, runc, Git and libarchive;
9. implementation and unit validation of the fail-closed host capability collector;
10. realistic Ubuntu point-release and frozen-kernel identity matching;
11. exact-head CI coverage for dependency, backend, signer, host, source, Rust, Browser, frozen-contract, generated-binding and WP13 lanes;
12. review correction of malformed-lock, unrealistic host-fixture and malformed-blocker failure paths.

## Conditions still open

This evidence does not close:

- owner acceptance of the Apache-2.0 public/private boundary;
- accepted public `LICENSE`, final `NOTICE`, contribution and security files;
- a proof-eligible report produced on the exact frozen Ubuntu Server 24.04.4 and `6.8.0-136-generic` host;
- the exact installed Ubuntu package manifest and package-artifact digests from that host;
- durable retention of the final accepted Phase 0C evidence beyond temporary GitHub artifact expiry;
- the final Phase 0C closure consistency review;
- ADR-0033 acceptance;
- explicit runtime implementation authorization;
- any WP14 runtime proof or implemented Node, Workspace, Activity, Provider, Browser, transfer, container, decomposition or UI behavior.

## Conclusion

The exact Rust dependency, distributed backend artifact, Browser binary, signing-authority and host-collector sub-gates are complete. The remaining technical proof is now concentrated on the real pinned host and its installed package set. Governance and retention blockers remain unchanged. ADR-0033 stays proposed and runtime implementation remains unauthorized.
