# Native Promotion Closure Matrix — 2026-10-02

## Exact source inventory
15 Cerebellum-native Java source files are confirmed in the exact decompiler archive.

### Represented in repository as evidence-backed transcriptions
- BuildConfig
- DeXModule / DeXPackage
- DevOptionsModule / DevOptionsPackage
- FullscreenChipOverlayPackage
- MainActivity
- MainApplication
- PipActionReceiver
- PipHelperModule / PipHelperPackage
- ScreenshotModule / ScreenshotPackage

### Still hard-gated
- FullscreenChipOverlayModule.java — exact source is available in archive, but must not be manually reconstructed from partial/truncated retrieval.
- R.java — generated/resource symbol source is very large and remains archive-authoritative.

## Exact app-owned UI assets
66 verified drawable assets are locked from the exact archive.
PiP/fullscreen-chip drawable XMLs already represented in the implementation.

## UI implementation boundary
The Hermes bundle is the authoritative UI artifact. Component names/routes/API strings are evidence for mapping only, not source code.

## Current closure state
- Native package identity: LOCKED
- Manifest/package/version/SDK/AGP: LOCKED
- Native Java inventory: LOCKED
- App-owned asset inventory: LOCKED
- Contamination barrier: ACTIVE
- PYQ layer: PROTECTED
- Exact Hermes bundle: AVAILABLE IN FORENSIC ARCHIVE, NOT YET PROMOTED
- RN host dependency graph: NOT CLAIMED REPRODUCIBLE
- FullscreenChipOverlayModule/R.java: GATED

## Rule
Do not create a synthetic React Native bundle or manually recreate gated native code merely to make the build pass. Promotion requires exact provenance.
