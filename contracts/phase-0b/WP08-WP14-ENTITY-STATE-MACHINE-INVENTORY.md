# WP08–WP14 Entity and State-Machine Inventory

**Status:** NORMATIVE CANDIDATE INVENTORY

This inventory is the minimum record set. A package cannot close by replacing these identities with generic status fields or backend IDs.

## WP08

Entities: Domain Pack, Pack Revision, Compatibility, Detector Observation, Classification Decision, Inventory Run, Decomposition Run, Coverage Record, Validation Run, Compare Run, Rebuild Run, Firmware Package/Manifest/Component, Firmware Compatibility, Disk Image, Partition Table, Partition, Filesystem, Mount Session, Device, Device Interface, Device Session, Device Lease, Protocol Stage, Display/Log/Input Stream, Screen Context, Device Backup, Physical Operation Verification.

Machines: pack revision; decomposition run; firmware compatibility; mount session; device connection; device session; device lease; physical operation; recovery verification.

## WP09

Entities: Application, Application Revision, Compatibility, Installation, Instance, Application Session, Browser Profile, Browser Context, Page, Browser Session, Semantic UI Snapshot, Element Observation, Screen Context, UI Action Request/Result, Display Stream, Input Stream, Clipboard Channel, Recording, Log Stream, Shell View, Panel, Attachment, Layout Revision, Remote Display Endpoint.

Machines: installation; application instance; application session; browser context; browser page; semantic snapshot freshness; UI action; display/input stream; shell attachment.

## WP10

Entities: Dataset, Dataset Revision, Data Profile, Index Definition/Revision, Ingestion Run, Segment, Coverage, Query Request/Run/Result Set, Citation Binding, Database Connection Reference, Database Snapshot, Package, Package Revision, Dependency Declaration, Resolution Graph, Lock Record, Plugin, Plugin Revision, Manifest, Installation, Activation, Instance, Health, Capability Grant.

Machines: ingestion; index revision; query run; package resolution; plugin installation; plugin activation; plugin instance; capability grant.

## WP11

Entities: Isolation Profile/Revision, Placement Request/Candidate/Decision, Resource Requirement, Capacity Snapshot, Reservation, Consumption Observation, Lease, Fence, Renewal, Revocation, Secure Grant, Credential Reference, Delivery, Cleanup Verification, Leakage Evidence, Network Exposure Grant, Admission Decision, Preemption, Eviction, Migration Decision.

Machines: placement; reservation; lease; secure grant; network exposure; admission; eviction/migration.

## WP12

Entities: Observation, Finding, Claim, Evidence Item, Evidence Bundle, Validation Request/Run, Review, Disposition, Remediation Proposal, Patch Object, Patch Application Run, Post-fix Verification, Risk Acceptance, Disclosure Decision, Reproduction Protocol/Request/Run/Comparison.

Machines: finding; claim review; validation; remediation; risk acceptance; disclosure; reproduction.

## WP13

Entities: Catalog Set, Conformance Suite, Fixture Manifest, Semantic Rule, Migration Definition, Harness Run, Test Case Result, Proof Report, Compatibility Matrix.

Machines: suite revision; harness run; migration verification; report review.

## WP14

Entities: Corpus, Corpus Revision, Fixture, Fixture Licence/Audience Review, Proof Plan, Proof Plan Revision, Freeze Review, Phase Readiness Decision.

Machines: corpus revision; fixture admission; proof-plan review; Phase 0B freeze; Phase 0C readiness.

## Global rejection rules

Reject generic `status` replacing typed lifecycle; backend IDs as canonical identity; state-changing execution without exact authority/generation/fence; success inferred from acknowledgement alone; secret values in ordinary records; deletion of negative/inconclusive history; public export without audience/redaction review; backend replacement that changes stable public identity.
