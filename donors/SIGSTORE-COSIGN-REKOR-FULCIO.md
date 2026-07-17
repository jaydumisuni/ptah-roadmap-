# Donor Record — Sigstore, Cosign, Rekor and Fulcio

**Phase:** 0A / WP03  
**Status:** FIRST-PASS COMPLETE — SIGNING, IDENTITY AND TRANSPARENCY DONOR SET  
**Inspected:** 2026-07-17

## Identity

### Cosign

- Canonical URL: https://github.com/sigstore/cosign
- Pinned commit: `089731c31f750153e9d91ec248c990e3b1991c2b`
- Licence: Apache-2.0

### Rekor

- Canonical URL: https://github.com/sigstore/rekor
- Pinned commit: `39fd5386c9c9b5cffbd63a61f34cb1f8e8b8b0e7`
- Licence: Apache-2.0
- Current note: Rekor v1 is in maintenance mode while v2/tile-based development advances.

### Fulcio

- Canonical URL: https://github.com/sigstore/fulcio
- Pinned commit: `4d394f41b281f65bed55e5dad5c78956078fec3b`
- Licence: Apache-2.0

### sigstore-go

- Canonical URL: https://github.com/sigstore/sigstore-go
- Pinned commit: `55aa6240784677449a564e66a0fca7a6a3605ecd`
- Status: Stable/production-ready library according to the inspected README
- Classification: Signing, verification, short-lived identity certificate, transparency and trusted-root machinery
- Ptah targets: Artifact/blob/image signing, identity-bound verification, offline bundles, transparency evidence, trusted roots and custom/private signing adapters

## Files/components inspected

- Cosign `README.md` and `LICENSE`
- Rekor `README.md` and `LICENSE`
- Fulcio `README.md` and `LICENSE`
- sigstore-go `README.md`
- keyless, keypair, KMS/PKI, bundle, registry, offline and trust-root boundaries

## Verified capabilities and patterns

### Cosign

- Signs and verifies OCI images and other Artifacts.
- Supports keyless OIDC/Fulcio/Rekor signing, hardware/KMS signing, encrypted keypairs and bring-your-own PKI.
- Signatures should bind to digests rather than mutable tags.
- Verification can require expected certificate identity and OIDC issuer.
- Signed payloads include the covered image digest.
- Blob signing and verification can use portable Sigstore bundles.
- Offline verification is possible when the Artifact, bundle and trusted root are available.
- Signatures/certificates may be stored alongside OCI Artifacts.
- Public transparency logs may permanently retain signer PII such as email identity.

### Fulcio

- Issues short-lived code-signing certificates for OIDC identities.
- Public certificates are valid for approximately ten minutes.
- Trust chains are distributed through a TUF-backed trusted-root process.
- Issued certificates are published to a Certificate Transparency log.
- API is available over HTTP/gRPC.
- Private/compliant certificate chains and KMS-backed Certificate Maker paths are documented.

### Rekor

- Provides an immutable/tamper-resistant transparency ledger for signed supply-chain metadata.
- Supports validation, log entry storage, querying, inclusion proof and log-integrity verification.
- Can operate independently and supports extensible manifest/PKI types.
- Public-instance upload size is limited, reinforcing that the log stores compact metadata rather than large Artifacts.
- v1 maintenance/v2 transition must be tracked as an implementation risk.

### sigstore-go

- Provides a smaller programmatic library for Sigstore bundle signing/verification.
- Supports TSA, Rekor, structured certificate metadata, TUF trusted roots and custom trusted roots.
- Passes Sigstore conformance tests.
- Deliberately omits some Cosign legacy/container/KMS surface while supporting custom key interfaces.

## What this donor set completes

- Cryptographic binding of signatures to exact Artifact digests.
- Identity-bound keyless signing and verification.
- Short-lived signing certificates rather than long-lived local keys for suitable environments.
- Transparency inclusion and non-repudiation evidence.
- Portable offline verification bundles.
- Trusted-root distribution and rotation.
- Support for public-good services, private infrastructure and bring-your-own keys/PKI.
- A programmatic integration path through sigstore-go instead of only invoking a CLI.

## Important limitations for Ptah

- A valid signature proves possession/identity and payload binding, not functional correctness or trustworthy input.
- Public keyless signing may expose immutable personal identity information in transparency logs.
- Public Sigstore services and OIDC providers require network availability during signing.
- Trusted roots must be updated and pinned carefully, especially for offline verification.
- Rekor v1 maintenance/v2 transition creates API/deployment evolution risk.
- Transparency logs are not Ptah Artifact storage or Activity ledgers.
- Cosign's container-image legacy and CLI surface are broader than the minimal Ptah signing API needs.
- Key management, identity policy and allowed signers belong to caller/operator configuration.
- Some private/internal releases may require non-public logs and company-controlled identity/KMS.
- Verification against a signer identity does not prove that the signer was authorized for a specific Ptah Build Recipe unless policy/attestation links establish that.

## Must not be inherited

- Public Sigstore services made mandatory.
- Signer email or private identity published without explicit informed configuration.
- Mutable tags signed or trusted instead of immutable digests.
- Signature existence promoted to review PASS or functional acceptance.
- Rekor as the only durable provenance record.
- Cosign CLI output as the only signing receipt.
- Private signing keys, OIDC tokens or KMS configuration stored in public Ptah recipes/logs.
- One trust root, issuer or signing method made universal.
- Rekor v1 APIs embedded directly into public Ptah contracts.

## Integration decision

**ADOPT SIGSTORE BUNDLE/VERIFICATION COMPATIBILITY; WRAP COSIGN OR SIGSTORE-GO AS SIGNING FACILITIES.**

Ptah should define a neutral Signing Facility and Signature/Verification receipt. Suitable backends include:

- keyless Fulcio/Rekor public-good flow;
- private Fulcio/Rekor/Sigstore deployment;
- KMS/HSM/hardware keys;
- encrypted project keypairs;
- caller-provided PKI;
- offline bundle verification.

The public Ptah project exposes generic credential/trust references. Private company signing identities, issuers, keys and release policy stay outside public source.

## Native Ptah gap

Ptah must define:

- Signature Artifact and verification receipt schemas;
- exact subject Object/Artifact digest and type;
- signer identity, issuer, certificate, key reference and trust-root reference;
- signing method and privacy classification;
- transparency entry/inclusion proof references;
- offline bundle Object reference;
- trusted-root version and retrieval time;
- caller/project authorization policy reference;
- signature verification state separate from Artifact quality/review state;
- redaction/consent for identity information;
- private/public signing backend adapter boundary;
- Rekor v1/v2 and alternate transparency-log compatibility.

## Exit strategy

Ptah stores signatures, certificates, bundles and verification receipts as standard Objects/Artifacts. Backends can change among Cosign, sigstore-go, another DSSE/signing implementation, private PKI or hardware KMS without changing Ptah Artifact identity.

## Validation required

1. Sign an Artifact by immutable digest and reject a moved mutable tag.
2. Verify keyless identity/issuer and separately verify an offline bundle.
3. Verify a private key/KMS-backed signature through the same Ptah contract.
4. Reject a valid signature from an unauthorized signer for the selected recipe/policy.
5. Retain trusted-root version and transparency inclusion proof.
6. Remove network access and verify from local Artifact, bundle and trusted root.
7. Prove signer identity/PII is not published without explicit configuration.
8. Rotate or replace the signing backend without changing Artifact/Object identity.
9. Treat signature verification, attestation verification and independent review as separate states.
10. Test compatibility across Rekor evolution or an alternate transparency backend.
