# Native Source Promotion Status — 2026-10-01

## Verified source batch
15 Java files under `sources/com/cerebellummobileapp/` were extracted from the exact 104,477,964-byte decompiler archive and scanned locally.

Files:
MainActivity.java
MainApplication.java
BuildConfig.java
R.java
DeXModule.java
DeXPackage.java
DevOptionsModule.java
DevOptionsPackage.java
FullscreenChipOverlayModule.java
FullscreenChipOverlayPackage.java
PipActionReceiver.java
PipHelperModule.java
PipHelperPackage.java
ScreenshotModule.java
ScreenshotPackage.java

## Contamination scan
PASS.
Scanned all 15 extracted files for:
- com.marrow
- marrow
- com/prepladder
- prepladder

No matches.

## Important provenance distinction
The archive contains exact decompiler output. The two promoted shell files in this repository are functional transcriptions of the verified decompiler source, not byte-for-byte source reproductions; the original archive remains the authoritative source for exact source text.

## Bundle
Verified exact Hermes bundle:
resources/assets/index.android.bundle
SHA-256: d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2

The bundle is compiled Hermes bytecode. It is not treated as original JSX/TypeScript.

## Next gates
1. Promote remaining native modules/packages without altering semantics.
2. Recover exact AndroidManifest/resource dependencies needed by the native shell.
3. Establish RN 0.81.0 + Hermes + New Architecture Gradle host.
4. Attach the verified Hermes bundle only after host compatibility is established.
5. Run repository-wide zero-contamination gate.
6. Build/runtime verification.
7. Keep PYQ layer isolated and unchanged throughout.
