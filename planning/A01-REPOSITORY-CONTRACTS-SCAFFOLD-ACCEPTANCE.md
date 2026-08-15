# A01 — Repository, contracts and reproducible scaffold acceptance

**Status:** ACCEPTED COMPLETE  
**Recorded:** 2026-08-15  
**Dependency:** P01D accepted and runtime implementation authorized by ADR-0039

## Decision

A01 is accepted complete. A02 — Node identity, Generation and host truth — is READY.

A01 proves the repository/contracts/reproducible-scaffold layer only. It does not claim Node, ledger, Activity, Workspace, Provider, Prime-integration, production, or release behavior.

## Exact implementation evidence

- repository: `jaydumisuni/Ptah-space`;
- PR: `#23` — `A01: prove repository, contracts and reproducible scaffold`;
- exact candidate head: `d12feedb5b66a39d5649b1d3ffea752deb5692c6`;
- merge: `d33122c8cc625d38f2394d57fcbd2a3ef7027b08`;
- A01 workflow run: `31906473232`;
- all 13 workflows on the exact candidate head: PASS.

### Retained A01 artifacts

- final proof artifact: `9252486137`, digest `sha256:0cec2c980df82a7136fb9c2869eb8ee8ad1bf343faf054b2917a1bf4a5f59c19`;
- Rust/Browser artifact: `9252484615`, digest `sha256:dd26318a8efc946f9f96789bdc67da64f6bc085c249f5630f126bddb3c4ff138`;
- generated-binding artifact: `9252481776`, digest `sha256:e3985416625a8e4c60d01eb696a8a3d76a67d52bf64fb0d056aa4fdc86093901`;
- frozen-conformance artifact: `9252481161`, digest `sha256:080126f89d793232b99859377c0e9c6e1f06745d60928a7dd1356444f8bf35c2`;
- static/adversarial artifact: `9252478248`, digest `sha256:a3b3651a45fe7c6d8885759d11eea513c3fcaa89bf89d696a04fcf626d93fb68`.

## Proved A01 obligations

- accepted monorepo layout and Rust/Node package boundaries;
- Rust `1.97.1`, Node `24.18.0`, Playwright `1.60.0` and dependency locks;
- frozen 14-catalog / 346-schema / 99-lifecycle contract binding;
- generated bindings reproduced twice and byte-identical;
- deliberately altered catalog digest rejected fail-closed;
- contract/binding generation executed with Python network access denied;
- frozen WP13 unit, structural and semantic conformance passed;
- Apache-2.0/public-private source boundary remained enforced;
- immutable GitHub Action commit pins were verified across the repository;
- an older floating deep-study Action reference was corrected instead of exempted;
- Rust formatting, Clippy, workspace tests and metadata passed;
- Browser locked install, check, tests and dependency inventory passed;
- exact candidate repository state remained clean and exact-head bound.

## Claim boundary

```text
A01 scaffold: FROZEN / PROVEN / COMPLETE
Runtime implementation authorization: remains AUTHORIZED
A02: READY
Node runtime: NOT YET PROVEN
Prime-native integration: NOT QUALIFIED
P01P: OPEN / DEFERRED
Production: NOT AUTHORIZED
Release: NOT ACCEPTED
```

## Next action

Begin A02 from the frozen WP01, WP02, WP04 and WP11 contracts. Implement only stable Node identity, Generation/Revision, host evidence, bounded health/capability/resource projections, advisory generation, and Event/Receipt correlation required by the A02 roadmap.
