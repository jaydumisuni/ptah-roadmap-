# Phase 0C — GitHub Actions immutable pins

Status: accepted for the Phase 0C scaffold evidence workflow

Verified: 2026-07-20

## Purpose

Record every third-party GitHub Action used by the first Ptah implementation-repository scaffold as an exact commit rather than a floating tag.

The action name or release tag is descriptive metadata. The commit SHA is the executed source identity.

## Accepted pins

| Action | Release label | Exact commit | Licence | Scaffold role |
|---|---:|---|---|---|
| `actions/checkout` | `v6.0.2` | `de0fac2e4500dabe0009e67214ff5f5447ce83dd` | MIT | Check out the exact Ptah PR head and the frozen roadmap checkpoint |
| `actions/setup-python` | `v6.2.0` | `a309ff8b426b58ec0e2a45f0f869d46889d02405` | MIT | Install the Python versions used by source-policy and frozen WP13 conformance jobs |
| `actions/setup-node` | `v6.4.0` | `48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e` | MIT | Install Node.js `24.18.0` for the locked Browser scaffold |
| `actions/upload-artifact` | `v7.0.1` | `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a` | MIT | Retain exact-head source-policy, Rust, Browser and frozen-conformance reports |

## Executed evidence

Implementation repository: `jaydumisuni/Ptah-space`

Evidence-hardening PR: `#3`

Tested head:

`900153ea3bf38a6c8f6f13e89e7bab2f7b22f5fc`

Workflow run:

`29717942201`

Result:

- source-policy job: passed;
- Rust scaffold job: passed;
- Browser scaffold job: passed;
- frozen WP13 structural and semantic conformance job: passed;
- all four jobs checked out the exact PR head;
- all four jobs uploaded retained artifacts;
- runtime authorization remained false.

Artifact records:

| Artifact | Artifact ID | SHA-256 digest |
|---|---:|---|
| Rust scaffold evidence | `8451258083` | `7fd85f969beb175ae60b97b88bcc807fff4e293b0efc7ad7a3bf8756a438fb9f` |
| Frozen conformance evidence | `8451257268` | `07c0783ce0320ae1bb1e49cfb8b6fea000643525fc520be88d46c8935b74bd6e` |
| Browser scaffold evidence | `8451256217` | `6e40ddb84117eb82826f677434091be388e068835b9fd5011ff9b94b805e11ac` |
| Source-policy evidence | `8451256102` | `2d1684b64e6c9c02cae7ca0983b33735cb0ea3b2a688d1783144e3c34dd89a28` |

Merged implementation commit:

`23fc97ff0acd2b219990411ec4fb84d8a8c0a567`

The passing PR-head evidence remains the acceptance source for the exact change. The merge commit establishes the canonical `main` history.

## Update policy

An action change requires:

1. an exact new commit SHA;
2. confirmation of upstream repository and licence;
3. review of the action diff or release boundary;
4. an exact-head workflow run;
5. retained artifacts from every affected job;
6. update of this record before Phase 0C or release acceptance.

Floating tags such as `@v4`, `@v5`, `@v6` or `@main` are prohibited in the acceptance workflow.

## Trust boundary

A pinned action reduces mutable-reference risk but does not make the action part of Ptah Core or prove it harmless. Workflow permissions remain least-privilege, credentials are not persisted unless explicitly required, and produced reports must still be inspected.