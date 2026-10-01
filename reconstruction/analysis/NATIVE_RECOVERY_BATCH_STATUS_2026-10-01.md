# Cerebellum Native Recovery — Batch Status 2026-10-01

## Current verified state

Exact forensic source:
- Archive: `base (1).apk_Decompiler.com.zip`
- Size: 104,477,964 bytes
- Package: `com.cerebellummobileapp`
- Version: 1.16.2 / versionCode 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- Exact Hermes bundle SHA-256: `d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731e8f8b5ff9c` 

## Native-source repository batch

Verified Cerebellum native Java files currently represented under:
`reconstruction/native_source/cerebellummobileapp/`

- BuildConfig.java
- DeXModule.java
- DeXPackage.java
- DevOptionsModule.java
- DevOptionsPackage.java
- FullscreenChipOverlayPackage.java
- MainActivity.java
- MainApplication.java
- PipActionReceiver.java
- PipHelperModule.java
- PipHelperPackage.java
- ScreenshotModule.java
- ScreenshotPackage.java

All 13 files were re-read from the repository and scanned for:
- `com.marrow`
- `marrow`
- `com/prepladder`
- `prepladder`

Result: **PASS — zero forbidden identifiers found.**

## Explicitly gated

1. FullscreenChipOverlayModule.java
   - Exact decompiler source exists in the forensic archive.
   - It contains substantial reflection/native overlay logic.
   - It must not be recreated from a partial/truncated transcription.
   - Remains gated until the complete verified source is promoted intact.

2. R.java
   - Exact decompiler source is large (~923 KB).
   - It is not to be hand-recreated.
   - Exact archive remains the authority.
   - Promote only through a byte-preserving extraction path.

## Provenance rule

The exact forensic archive remains the source of truth. Existing repository Java files may be functional transcriptions unless explicitly marked byte-exact; they must not be represented as byte-for-byte decompiler output.

## Next execution gate

1. Preserve exact-source provenance.
2. Recover/promote remaining gated native files through byte-preserving extraction.
3. Recover exact AndroidManifest/resource dependencies.
4. Establish RN 0.81.0 + Hermes + New Architecture host.
5. Integrate the verified Hermes bundle.
6. Run repository-wide Cerebellum zero-contamination scan.
7. Build/runtime verification.
8. Keep PYQ layer isolated and unchanged.

**No Marrow/Prepladder implementation is permitted in the Cerebellum native layer.**
