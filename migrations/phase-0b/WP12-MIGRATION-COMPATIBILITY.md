# WP12 Migration and Compatibility

**Status:** CANDIDATE

- Legacy scanner output migrates to Observation and Evidence Item first; it becomes a Finding only after bounded review.
- Issue IDs, CVEs, rule IDs, report paths and scanner run IDs migrate as scoped Aliases.
- Historical findings without source evidence remain `unverified_legacy` and cannot gain invented confidence.
- Existing risk acceptances require authority, scope, rationale and expiry; otherwise preserve as unsupported history.
- Existing patches require exact base revision and Object identity; patch paths alone are insufficient.
- Existing remediation records migrate as `applied_unverified` unless independent post-fix checks exist.
- Reproduction claims require exact protocol, environment, Attempt and independence evidence; same-run retries do not qualify.
- Public exports preserve audience/redaction policy and never import raw secrets or private evidence.

Security scanners, SAST/DAST tools, vulnerability databases and reproduction backends may be replaced while canonical Observation, Finding, Claim, Evidence and Reproduction identities remain stable. Replacement always creates new Activities/Attempts and preserves contradictory history.
