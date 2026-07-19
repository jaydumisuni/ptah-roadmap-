# WP12 Consolidated Safety Net

WP12 passes only when structural, lifecycle and semantic checks agree.

Required checks:

- every schema and lifecycle resolves offline with unique URN/name;
- Observation cannot satisfy Finding;
- scanner output cannot become confirmed Finding without review;
- Claim authority and bounded scope are mandatory;
- Evidence Item binds exact Content, digest, collector and Attempt;
- Evidence Bundle cannot overclaim coverage or authority;
- validation and reproduction retries use new WP02 Attempts;
- Review cannot rewrite evidence history;
- Accepted Risk retains Finding and enforces expiry;
- Dispute preserves all positions and contradictory evidence;
- Disclosure enforces audience, redaction and privacy;
- Proposal, Patch, Remediation Run and Post-Fix Verification remain distinct;
- patch/tool acknowledgement cannot become verified repair;
- failed rollback, uncertain mutation and regression remain visible;
- reproduction independence is demonstrated rather than asserted;
- same-cache/same-hidden-environment reruns are rejected as independent;
- failed, negative, partial and inconclusive reproduction is retained;
- backend replacement preserves canonical identity and creates new work/evidence.

Executable enforcement is WP13 work.
