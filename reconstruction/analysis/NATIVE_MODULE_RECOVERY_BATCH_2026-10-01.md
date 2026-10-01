# Cerebellum Native Module Recovery Batch — 2026-10-01

## Scope
This batch promotes only evidence derived from the verified Cerebellum decompiler archive:
- package: `com.cerebellummobileapp`
- version: `1.16.2`
- versionCode: `172`
- archive: `base (1).apk_Decompiler.com.zip`
- archive size: `104,477,964` bytes

## Native classes recovered
Verified archive inventory contains 15 app-owned Java classes:
- BuildConfig
- MainActivity
- MainApplication
- DeXModule
- DeXPackage
- DevOptionsModule
- DevOptionsPackage
- FullscreenChipOverlayModule
- FullscreenChipOverlayPackage
- PipActionReceiver
- PipHelperModule
- PipHelperPackage
- ScreenshotModule
- ScreenshotPackage
- R

## Current repository promotion state
### Functional/native transcriptions promoted
- MainActivity
- MainApplication
- BuildConfig
- DeXModule
- DeXPackage
- DevOptionsModule
- DevOptionsPackage
- PipActionReceiver
- PipHelperPackage
- ScreenshotPackage

### Exact decompiler source remains authoritative for
- FullscreenChipOverlayModule
- FullscreenChipOverlayPackage
- PipHelperModule
- ScreenshotModule
- R.java

The promoted MainActivity/MainApplication and the newly promoted module files are implementation transcriptions, not claims of byte-for-byte decompiler identity. Decompiler metadata/comments may be simplified where explicitly documented.

## Evidence-backed native behavior
- MainActivity uses ReactActivity with Fabric/New Architecture delegate.
- Main component name: `cerebellumMobileApp`.
- Picture-in-picture support is wired through PipActionReceiver/PipHelper.
- MainApplication enables Hermes and New Architecture and registers the recovered native packages.
- DeXModule exposes `checkDeXEnabled`.
- DevOptionsModule exposes `isDevelopmentSettingsEnabled`.
- ScreenshotPackage registers ScreenshotModule.
- PipHelperPackage registers PipHelperModule.
- FullscreenChipOverlay remains pending exact promotion because its source is substantially larger and must not be reconstructed by guesswork.

## Contamination barrier
No Marrow implementation source is used as a source for this batch. `reconstruction/apk_root/` remains quarantined/evidence-only and is not a Cerebellum implementation source.

## PYQ barrier
The protected PYQ extraction/content layer is not modified by this batch.

## Next gates
1. Promote/verify remaining large native modules from the exact archive.
2. Verify exact manifest/resource/native dependency relationships.
3. Recover the RN 0.81.0/Hermes/New Architecture Android host required to build the native shell.
4. Integrate the exact Hermes bundle only after host identity is verified.
5. Run zero-contamination scan.
6. Run build/runtime gate.
7. Only then reconnect the protected PYQ layer.
