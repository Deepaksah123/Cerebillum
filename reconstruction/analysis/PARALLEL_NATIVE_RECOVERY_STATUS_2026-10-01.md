# Parallel Native Recovery Status — 2026-10-01

## Lane A — Verified Cerebellum native host
PASS at forensic-evidence level:
- package: com.cerebellummobileapp
- MainActivity: com.cerebellummobileapp.MainActivity
- MainApplication: com.cerebellummobileapp.MainApplication
- RN component: cerebellumMobileApp
- React Native 0.81.0
- Hermes: enabled
- New Architecture: enabled
- bundle: resources/assets/index.android.bundle

Source basis: verified Cerebellum decompiler forensic artifacts in Library. No Marrow evidence used.

## Lane B — Repository native root
BLOCKED:
- reconstruction/apk_root package is com.marrow.
- It is permanently excluded from Cerebellum integration.
- Contamination gate remains intentionally blocking.

## Lane C — Four repository archive chunks
PROBED:
- 01_core_dex.zip
- 02_dex_3_4.zip
- 03_dex5_lib_assets.zip
- 04_remaining_resources.zip
- Manifest candidate found in 03_dex5_lib_assets.zip, 46,464 bytes.
- Raw archive probe did NOT prove com.cerebellummobileapp.
- No exact com.cerebellummobileapp MainActivity/MainApplication source paths found.
- Therefore these archives are not promoted to native host.

## Lane D — PYQ layer
UNCHANGED / PROTECTED:
- 9,354 total questions
- 7,288 mapped
- 2,066 unresolved
- 0 ambiguous
- 19 subjects
- 2015–2025
- validated HTML generated
- unresolved records remain unresolved; no force mapping.

## Lane E — Required next native action
Recover/materialize the verified Cerebellum decompiler archive and exact source bytes into the working repository or otherwise obtain the verified com.cerebellummobileapp native evidence tree.

Then:
1. verify manifest/package SHA
2. recover MainActivity/MainApplication + native modules
3. recover exact Hermes bundle
4. reconstruct RN 0.81.0 Gradle project
5. run contamination scan
6. build
7. only then wire the validated PYQ layer

## Zero-contamination rule
No com.marrow DEX, resources, assets, media, classes, navigation, or UI implementation may enter the Cerebellum build.
No screenshot-derived implementation.
No guessing where native evidence is absent.
