# Cerebellum Native Recovery — Batch Status 2026-10-01

## Current verified state
- Exact forensic archive: `base (1).apk_Decompiler.com.zip`
- Size: 104,477,964 bytes
- Package: `com.cerebellummobileapp`
- Version: 1.16.2 / versionCode 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- Exact Hermes bundle SHA-256: `d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2`

## Repository native batch
13 Cerebellum native Java files are currently represented under `reconstruction/native_source/cerebellummobileapp/`:
BuildConfig.java, DeXModule.java, DeXPackage.java, DevOptionsModule.java, DevOptionsPackage.java, FullscreenChipOverlayPackage.java, MainActivity.java, MainApplication.java, PipActionReceiver.java, PipHelperModule.java, PipHelperPackage.java, ScreenshotModule.java, ScreenshotPackage.java.

All 13 were re-read from GitHub and scanned for `com.marrow`, `marrow`, `com/prepladder`, and `prepladder`.
**Result: PASS — zero forbidden identifiers.**

## Explicitly gated
- `FullscreenChipOverlayModule.java`: exact source exists in the forensic archive but contains substantial reflection/native overlay logic; do not recreate from partial output.
- `R.java`: exact source is ~923 KB; do not hand-recreate. Promote only through byte-preserving extraction.

## Provenance
The forensic archive is authoritative. Existing repository Java files may be functional transcriptions unless explicitly marked byte-exact.

## Next gate
1. Byte-preserving promotion of gated native files.
2. Exact AndroidManifest/resource dependency recovery.
3. RN 0.81.0 + Hermes + New Architecture host.
4. Verified Hermes bundle integration.
5. Repository-wide zero-contamination scan.
6. Build/runtime verification.
7. PYQ layer remains isolated and unchanged.

**No Marrow/Prepladder implementation is permitted in the Cerebellum native layer.**
