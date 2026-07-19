# WP10 Migration and Compatibility

**Status:** CANDIDATE

## Legacy knowledge and search

- Preserve source bytes as WP03 Objects/Revisions before creating Source/Source Revision.
- Legacy chunks become Segments only when exact source revision, range and extraction configuration are known; otherwise retain them as opaque derived Objects.
- Vector-store IDs and shard IDs become scoped Aliases, never canonical Index or Segment identity.
- Existing search results migrate only with exact Query Run, Index Revision and source evidence; otherwise preserve as historical observations.
- Existing citations based only on URL/title remain weak legacy references and cannot be upgraded to exact Citations without revision/range/digest evidence.
- Generated answers remain separate Artifacts and require new Verification records.

## Data

- Existing CSV/Parquet/database exports become Dataset Revisions over exact Objects.
- Live connection strings migrate to secret-free Connection References plus external credential grants.
- Database dumps become immutable Snapshots; they cannot be labelled current live state.
- Transform scripts map to WP07 Recipes and WP02 execution only when inputs/configuration/tool revisions are recoverable.

## Package

- Package-manager name/version/path records become scoped Aliases until ecosystem, namespace, source and digest are known.
- Requirements files and manifests become dependency constraints, not Resolved Graphs.
- Existing resolved installations become Resolved Graph/Lock records only when exact versions, sources and digests are recoverable.
- Install command success remains `installed_unverified` until independent Package Verification.

## Plugin

- Existing extensions/modules become Plugin/Revisions only after source Object, manifest, dependency and permission recovery.
- Enabled flags do not become Activation without policy decision and capability grants.
- Running process/handle records become Plugin Instances only with exact Plugin Revision, Installation, Activation, Workspace and Provider generations.
- Existing health flags remain observations with explicit expiry.
- Open ports/listeners migrate as Port Registrations only with network scope, exposure policy and grants.
- Removal records cannot be upgraded to verified removal without grant revocation, process/service stop, unregister, uninstall and cleanup evidence.

## Backend replacement

RAGFlow, LlamaIndex, Dify, MCP servers, databases, vector stores, package managers and Plugin hosts may be replaced. Replacement preserves Source/Dataset/Package/Plugin logical identity while producing new revisions, indexes, resolved graphs, installations, instances, generations and evidence.

## Directionality

All migrations are directional and evidence-gated. Missing evidence results in preserved legacy records, manual review, partial/inconclusive classification or re-ingestion/re-resolution/reinstallation. No migration infers success, freshness, authority, health or cleanup.
