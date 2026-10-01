# Cerebellum Native Recovery Gate — 2026-10-01 (Batch Update)

## Parallel verification result

### Lane A — Genuine Cerebellum forensic package
VERIFIED from Library forensic artifacts:
- Source: `base (1).apk_Decompiler.com.zip`
- ZIP size: 104,477,964 bytes
- Entries: 46,647
- Application ID: `com.cerebellummobileapp`
- Version: 1.16.2 / versionCode 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- RN component: `cerebellumMobileApp`
- MainActivity: `com.cerebellummobileapp.MainActivity`
- MainApplication: `com.cerebellummobileapp.MainApplication`
- Bundle: `resources/assets/index.android.bundle`
- Bundle size: 11,206,868 bytes
- Native classes evidenced: BuildConfig, DeXModule/Package, DevOptionsModule/Package, FullscreenChipOverlayModule/Package, MainActivity, MainApplication, PipActionReceiver, PipHelperModule/Package, ScreenshotModule/Package.

### Lane B — Current repository APK root
HARD BLOCK / EXCLUDED:
- `reconstruction/apk_root/manifest/AndroidManifest.xml` decodes to package `com.marrow`.
- This tree is not Cerebellum evidence and must never be used for implementation.
- No Marrow classes, assets, resources, navigation or UI may be copied into the Cerebellum host.

### Lane C — Four repository archive chunks
PROBE RESULT:
- 01_core_dex.zip: 24,455,320 bytes / 3 members
- 02_dex_3_4.zip: 24,959,658 bytes / 2 members
- 03_dex5_lib_assets.zip: 25,052,685 bytes / 67 members
- 04_remaining_resources.zip: 25,127,803 bytes / 5,005 members
- Only one AndroidManifest.xml candidate was found (03_dex5_lib_assets.zip, 46,464 bytes).
- Raw package-string evidence did not prove `com.cerebellummobileapp`.
- Exact `MainActivity` / `MainApplication` source paths were not present.
- Therefore these chunks remain UNVERIFIED and are not promoted.

### Lane D — PYQ
PROTECTED / DO NOT MODIFY during native recovery.
- 41 source files
- 9,354 records
- 7,288 safely mapped
- 2,066 unresolved
- 0 ambiguous
- 19 canonical subjects
- 2015–2025
- validated interactive HTML exists
- unresolved records remain unresolved.

## Current gate
The verified Cerebellum forensic source is documented and independently identifiable, but the actual 104 MB decompiler ZIP/source bytes are not currently available as a repository binary. Do not fabricate or synthesize missing Java/Kotlin/source/bundle bytes.

## Next executable gate
When the verified decompiler archive or equivalent exact source bytes become available:
1. SHA/manifest/package verification.
2. Extract only Cerebellum-provenance paths.
3. Recover MainActivity/MainApplication and all app-owned native modules.
4. Recover exact Hermes bundle and app-owned assets.
5. Reconstruct RN 0.81.0 Gradle host.
6. Run full Marrow contamination scan.
7. Build and verify APK.
8. Only after native gate passes, attach the protected PYQ layer.
