# WP14 consolidated safety net

A Corpus Revision cannot freeze unless:

- every fixture has exact Content identity and digest;
- source, licence or permission is recorded;
- audience, privacy and redaction are explicit;
- each fixture has an Admission decision;
- each fixture has typed Expected Proof;
- structural, semantic and migration coverage are reviewed;
- negative and inconclusive cases remain retained;
- WP13 passes against the exact candidate head;
- no unresolved high-risk exception exists;
- the first vertical-slice Proof Plan is immutable and backend-neutral.

A filename, directory, CI job, donor test name or screenshot is not fixture identity. A test that unexpectedly passes is a corpus defect until reviewed; it is not silently converted into a golden case.
