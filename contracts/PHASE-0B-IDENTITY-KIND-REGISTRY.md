# Ptah Phase 0B — Identity and Authority Kind Registry

**Parent registry:** `ptah.entity-kind` `0.1.0`  
**Namespace:** `identity`  
**Status:** CANDIDATE — normative supplement to `PHASE-0B-ENTITY-KIND-REGISTRY.md`  
**Date:** 2026-07-18

## Purpose

Define canonical identities used for ownership, authorization, policy, approval and credential references.

Usernames, email addresses, OAuth subjects, API keys, operating-system UIDs and provider account IDs remain Aliases or credential metadata. They are not canonical Ptah identities by themselves.

## Registered entity kinds

| Token | Meaning |
|---|---|
| `identity.principal` | Human, service, caller or workload identity that may receive authority |
| `identity.organization` | Organization/tenant/trust-domain identity |
| `identity.group` | Versioned membership group |
| `identity.role` | Named role definition, not a person |
| `identity.policy` | Versioned authorization/retention/risk/placement/etc. policy identity |
| `identity.permission_grant` | Scoped capability permission granted to a Principal/Group/Role |
| `identity.approval` | Explicit approval/rejection/acceptance decision over exact subject/scope |
| `identity.credential_reference` | Opaque reference to externally stored credential material |
| `identity.trust_anchor` | Key, issuer, certificate root or other accepted trust anchor record |
| `identity.authentication_session` | Authentication result/session separate from authorization |

## Principal kinds

`identity.principal` uses a typed `principal_kind` field:

```text
human
service
caller
workload
node
provider
external_system
```

A Principal can have several Aliases, for example:

- email address;
- GitHub account;
- OAuth issuer and subject;
- operating-system UID;
- certificate subject;
- API client ID;
- external account number.

Aliases remain scoped by source/issuer and validity period.

## Authority rules

1. Authentication proves one issuer/session assertion; it does not create permission automatically.
2. A Role is a policy input, not a Principal.
3. Group membership is versioned and time-scoped.
4. Permission Grants name exact subject, capability, resource scope, issuing authority, validity and revocation.
5. Approvals name exact subject revision/checkpoint and do not mutate it automatically.
6. Credential References never contain raw credential values.
7. Trust Anchors can be revoked/deprecated without rewriting historical verification evidence.
8. External/provider identity claims retain issuer and verification evidence.
9. Public exports may remap Principal IDs and omit identifying Aliases.
10. Organization policy acceptance remains separate from technical Provider capability.

## Permission Grant minimum direction

```text
permission_grant_id
subject_principal_or_group_ref
capability_scope
resource_scope_refs
issuing_authority_ref
policy_ref
issued_at
valid_from
expires_at
revoked_at
revocation_reason
delegation_constraints
receipt_and_evidence_refs
```

## Approval minimum direction

```text
approval_id
decision
subject_refs
subject_revision_or_hash
scope
approver_principal_ref
authority_basis_ref
policy_ref
reason
created_at
expires_at
supersedes_ref
evidence_refs
```

Initial decision values:

```text
approved
rejected
accepted
declined
revoked
expired
superseded
```

The meaning of `accepted` belongs to the named policy/subject and never becomes a generic Activity or proof state.

## Credential Reference minimum direction

```text
credential_reference_id
provider_or_vault_ref
credential_kind
destination_scope
allowed_facilities_or_workloads
issued_for_principal_ref
created_at
expires_at
rotation_version
revocation_state
redaction_class
```

Credential values are retrieved only through a separately authorized secure-delivery Operation and never serialized in ordinary entities, logs, Events, Receipts or exports.

## Conformance requirements

- reject an email/OAuth subject used as canonical `entity_id`;
- preserve two Aliases from different issuers without merging Principals automatically;
- reject an expired/revoked Grant;
- prove authentication does not imply authorization;
- bind Approval to exact subject revision/hash;
- reject stale Approval after subject revision changes where policy requires freshness;
- revoke a Credential Reference without rewriting historical use Receipts;
- public-export a Principal using remapped ID and removed private Aliases while preserving restricted lineage.

These identity entities are contract vocabulary only. No authentication service, vault or authorization engine is selected by this registry.
