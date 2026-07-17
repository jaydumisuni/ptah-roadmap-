# Donor Record — Tree-sitter

**Phase:** 0A / WP05  
**Status:** FIRST-PASS COMPLETE — OPTIONAL SOURCE-STRUCTURE DONOR  
**Inspected:** 2026-07-17

## Identity

- Canonical URL: https://github.com/tree-sitter/tree-sitter
- Default branch: `master`
- Pinned commit: `8b7c213443204357308415ed5059cf21e469f790`
- Licence: MIT
- Activity: Active and mature
- Classification: Incremental concrete-syntax-tree parser runtime and grammar interface
- Ptah targets: source-file syntax trees, named nodes/ranges, incremental edit views, structural search/highlighting and source decomposition

## Files/components inspected

- `README.md`
- `LICENSE`
- `lib/binding_rust/README.md`
- documented parser/language, incremental edit, callback input, UTF-8/UTF-16 and Wasm grammar boundaries

## Verified capabilities and patterns

- Parser generator and incremental parsing library.
- Builds a concrete syntax tree for source code and updates it efficiently after edits.
- Designed to be general across programming languages, fast enough for editor use, useful in the presence of syntax errors and dependency-free at the core C runtime.
- Rust bindings support parser/language assignment and node positions/kinds.
- Previous trees can be edited with exact byte/point ranges and reused for faster incremental parsing.
- Source text can be supplied through strings, byte slices, vectors or callbacks keyed by byte/row/column positions.
- UTF-8 and UTF-16 input paths are supported.
- Wasm grammar loading is supported through an optional feature and Wasmtime-backed store.
- Separate language grammars are dependencies rather than hard-coded into the core runtime.

## What Tree-sitter completes

- A neutral syntax-tree view for source files recovered by App Recover, JADX exports, repositories and document/code packs.
- Stable byte/range relationships from syntax nodes back to immutable source Objects.
- Incremental parsing useful for Ptah editor/Workspace views.
- Error-tolerant partial structure rather than all-or-nothing compiler parsing.
- A language-grammar Facility model that can be loaded selectively.
- An embedded Rust-compatible path aligned with Ptah's core language preference.

## Important limitations for Ptah

- A concrete syntax tree is not semantic analysis, type checking, compilation or runtime behavior.
- Grammar quality, node names and coverage vary by language repository/version.
- Language grammars have their own licences, release cadence and security risks.
- Error recovery can produce useful but approximate trees; error/missing nodes must be retained.
- Preprocessor/macros/generated code and embedded languages may require specialist handling.
- A file extension/language guess is not sufficient to select a grammar without detector evidence.
- Wasm/native grammar loading is executable code and requires trust/version/resource controls.
- Tree-sitter node IDs are transient and not durable Ptah Object identities.
- Incremental parse reuse depends on accurate edits and exact prior source identity.
- Very large/minified/generated source still requires time/memory/node-count limits.
- The runtime does not resolve imports, dependencies, symbols across files or Build systems.

## Must not be inherited

- Syntax tree presented as semantic correctness or compilability.
- Grammar node IDs used as durable Ptah IDs.
- Grammars downloaded/executed implicitly.
- Extension-only language selection.
- Error-recovered tree described as fully parsed without error/missing-node evidence.
- All language grammars bundled into every Node.
- Source structure used as proof of original source when the input was decompiled/generated.
- Native/Wasm grammar code loaded in the control plane without capability isolation.

## Integration decision

**ADOPT AS AN OPTIONAL SOURCE STRUCTURE FACILITY FOR VERIFIED TEXT/SOURCE OBJECTS.**

Ptah should create syntax-tree views only after a source/text detector selects one or more candidate languages. Grammar/version/configuration and parse errors remain part of the derivative receipt.

Tree-sitter is not required for binary, document, image, media or firmware decomposition and does not replace language servers, compilers or Build Facilities.

## Native Ptah gap

Ptah must define:

- source language detector claims and candidate grammar routing;
- grammar Facility/version/hash/licence/capability manifest;
- syntax-tree view schema with byte ranges, positions, kinds, named/error/missing state and parent/child links;
- relationship to original, generated or decompiled source Object;
- incremental edit/revision identity and previous-tree compatibility;
- node-count/depth/time/memory limits;
- embedded-language and preprocessor relationships;
- semantic/language-server/compiler views kept separate;
- native versus Wasm grammar trust/isolation policy;
- search/query/highlight derivative contracts where needed.

## Exit strategy

Ptah's Source Structure contract can support Tree-sitter, compiler ASTs, language servers or specialist parsers. Source Objects and node-range relationships remain backend-neutral.

## Validation required

1. Parse representative source files in several languages with exact byte/range relationships.
2. Retain syntax errors/missing nodes and compare against compiler diagnostics.
3. Apply an incremental edit to a new source revision and verify unchanged/changed ranges.
4. Parse decompiled/generated source and label its origin accurately.
5. Handle embedded-language and preprocessor-heavy files through explicit completion adapters.
6. Enforce node/depth/time/memory limits on huge/minified/generated inputs.
7. Load only pinned approved native/Wasm grammars and record licences/hashes.
8. Replace one grammar/parser without changing source Object identity.
9. Prove syntax-tree success does not imply Build/test/runtime success.
