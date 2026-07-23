# Campaign 001 — AF03 Sergeant Review

Review system: Sergeant independent adversarial review

Status: PASS WITH MANDATORY RETAINED RESTRICTIONS

Reviewed: 2026-07-23

Frozen candidate head reviewed: `a6a1d9aa13f619c2f8ff4c1c6c0cadea331df3d6`

Sergeant did not participate in producing the AF03 Primary or Verifier packets. This is Sergeant's review result, not a Ptah verdict or AF03 acceptance.

## Review scope

Sergeant checked:

- all ten assigned record identities, default branches and exact source commits;
- one distinct Primary and one distinct Verifier per record;
- licence and no-licence boundaries;
- hosted, premium, model, plugin, binary, image and linked-project separation;
- capability overclaims and missing negative evidence;
- canonical Ptah identity and authority leakage;
- acknowledgement-versus-post-condition boundaries;
- AF04, Phase 0A, P01, ADR-0033 and runtime state.

## Coverage result

- assigned records found: 10 / 10;
- Primary packets found: 10 / 10;
- Verifier packets found: 10 / 10;
- exact source pins found: 10 / 10;
- bounded outcomes found: 10 / 10;
- missing records: 0;
- reused Primary workers: 0;
- reused Verifier workers: 0;
- blocking review findings: 0.

## Mandatory retained findings

### SRG-AF03-01 — Profile catalogues are not source licences

`D052` and `D063` have no root repository licence. Their accepted scope must remain discovery, research-method and navigation evidence only. Linked repositories and claimed contributions require separate exact review.

Disposition: correctly retained; no change required.

### SRG-AF03-02 — Open repositories do not contain every advertised service capability

Semgrep proprietary rules/platform features, Coder Premium and registry surfaces, browser-use Cloud/hosted models/proxies/integrations, Temporal SDK/UI/Cloud surfaces, and related Docker services remain separate products or repositories.

Disposition: correctly retained; no change required.

### SRG-AF03-03 — Backend success is not Ptah proof

Semgrep findings, Temporal workflow completion, browser actions, minicap stream connection, Firecracker VM start and Docker CLI success remain producer/backend evidence. None may equal accepted truth, external-effect proof, secure isolation, cleanup success or caller approval.

Disposition: correctly retained; no change required.

### SRG-AF03-04 — Compatibility and host requirements must remain explicit

minicap is legacy/private-API Android capture with narrow SDK/device support. Firecracker requires exact KVM/hardware/host-security proof. Coder, browser-use and Docker CLI depend on separately configured infrastructure and endpoints.

Disposition: correctly retained; no change required.

### SRG-AF03-05 — Donor identities remain aliases

Temporal Workflows, Coder Workspaces, browser-use agents, minicap processes, Firecracker microVMs and Docker contexts/objects cannot become canonical Ptah identities.

Disposition: correctly retained; no change required.

## Negative review

Sergeant found no evidence that AF03:

- reopened Phase 0A;
- changed WP01–WP14;
- accepted source reuse without an explicit licence boundary;
- made a donor mandatory or authoritative;
- started AF04;
- accepted ADR-0033;
- authorized runtime implementation.

## Sergeant result

`pass_with_mandatory_retained_restrictions`

The candidate is suitable for exact-head closure validation. This result does not accept AF03. A separate owner/calling-authority promotion change remains required after exact-head proof.