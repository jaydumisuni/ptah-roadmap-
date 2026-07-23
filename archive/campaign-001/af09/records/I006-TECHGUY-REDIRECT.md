# I006 — TechGuy Redirect

Status: candidate record — paired evidence complete

Primary Archivist: `AF09-P08`
Independent Verifier: `AF09-V08`
Inspected: 2026-07-23

## Canonical source identity
- source: `jaydumisuni/TTG-usb-redirect-`;
- branch: `main`;
- exact commit: `bb877636d76f85d5718d23f8da68d0169ac34432`;
- role: USB/screen/port redirection workload and product evidence;
- source licence and third-party redirect components require exact file/dependency review before reuse.

## Evidence and boundary
The repository proves a concrete redirect project and requirements for endpoint selection, connection state, transport evidence and cleanup. The verifier confirmed that redirection can expose devices, ports and data across trust boundaries and must be explicitly authorized and fenced.

## Bounded outcome
`accepted_for_archive_redirect_workload_with_endpoint_transport_privacy_lease_cleanup_and_licence_review_boundaries`

Restrictions: no source reuse until exact licence/component inventory passes; require explicit endpoints, authentication, Lease/Fence and network/privacy Policy; verify teardown and stale-session cleanup; do not expose backend endpoint IDs as canonical identities.

This outcome does not authorize implementation.