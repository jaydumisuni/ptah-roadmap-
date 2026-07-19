# Ptah Phase 0B — Entity Kind Registry WP08 Correction 0.1.1

**Parent supplement:** `ENTITY-KIND-REGISTRY-WP08-SUPPLEMENT.md`  
**Status:** CANDIDATE CORRECTION  
**Date:** 2026-07-19

## Purpose

Add one independently addressable entity omitted from the first WP08 supplement while preserving earlier registry history.

## Added entity kind

| Token | Meaning |
|---|---|
| `firmware.operation_plan` | Immutable reviewable plan binding exact package/component/Device/range/tool/authority/backup/read-back requirements before a physical protocol Operation |

## Rules

1. Parsed scatter/rawprogram/patch/PIT/payload instructions may contribute to an Operation Plan but do not become execution authority.
2. Plan identity is separate from `firmware.operation`, WP02 Operation/Attempt, `firmware.mutation_authorization` and `firmware.operation_verification`.
3. A Plan binds exact Device Profile, Interface/Connection epoch, Provider generation, target ranges, source Objects/digests, tools/assets, Compatibility Result, Lease/fence requirements, backup policy, retry class and verification Protocol.
4. Changing target range, source bytes, Device/Profile/layout, connection epoch, Provider generation, selected asset/tool, authority or verification strategy creates/supersedes a Plan and invalidates stale execution authority.
5. Static package interpretation can create a draft Plan without a connected Device, but physical execution requires a current exact-context Plan.
6. Generic raw backend commands remain separate high-risk capabilities and cannot bypass the Plan.
7. Registration does not authorize implementation or physical mutation.

## Conformance requirements

- reject physical firmware Operation without an immutable Plan;
- reject Plan reused after target/generation/epoch/source/tool change;
- reject Plan creation reported as execution or physical proof;
- reject Mutation Authorization used as a replacement for the Plan;
- reject parsed vendor operation graph executed directly without reviewable Plan identity.

## Do-not-break rule

> A plan describes intended physical work; an Operation/Attempt performs it; Verification proves bounded outcome. These identities never collapse.
