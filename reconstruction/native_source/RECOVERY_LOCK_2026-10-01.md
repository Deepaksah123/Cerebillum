# Cerebellum Exact Native Source Recovery — 2026-10-01

Source-of-truth archive:
- Library file: base (1).apk_Decompiler.com.zip
- Size: 104477964 bytes
- ZIP entries: 46647
- Package: com.cerebellummobileapp
- Version: 1.16.2 (172)
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- MainActivity: com.cerebellummobileapp.MainActivity
- MainApplication: com.cerebellummobileapp.MainApplication
- Bundle: resources/assets/index.android.bundle

Exact extracted Cerebellum-owned native source paths:
- MainActivity.java
- MainApplication.java
- BuildConfig.java
- R.java
- DeXModule.java
- DeXPackage.java
- DevOptionsModule.java
- DevOptionsPackage.java
- FullscreenChipOverlayModule.java
- FullscreenChipOverlayPackage.java
- PipActionReceiver.java
- PipHelperModule.java
- PipHelperPackage.java
- ScreenshotModule.java
- ScreenshotPackage.java

Exact SHA-256:
- AndroidManifest.xml: 249d2276fc75f23c6bd310f3c0da5bcbbf0ea48ffa3e31539045e0eae718c098
- index.android.bundle: d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2
- MainActivity.java: ad76fc26e28b589bbcf75b2102851a91bab607018a3e57fd44efb9d0a74906f4
- MainApplication.java: 6112da8da95b211d3c660b165f43a48c9204d0586230b13e8ee3eb7bdcc0c029
- PipHelperModule.java: 211c87e720706e17a52cb3970715bd73ac2ff9e70649274b2ca912d1707b95d9
- ScreenshotModule.java: e86498916625b247c874195b3bb75d3371d7bd2e14cc5665fae8e1f8f8b5ff9c
- FullscreenChipOverlayModule.java: b513c855f4bd8c1a912ffc8481ee4348326491d3ae0a9ec7987cf968f281db18

Contamination barrier:
- reconstruction/apk_root/ remains quarantined.
- No Marrow source/assets/classes are promoted into this native_source layer.
- PYQ layer remains untouched.
- Hermes bundle is evidence/source input; it is not treated as original JSX/TypeScript.

Promotion status:
- Exact archive: VERIFIED and materialized.
- Native source extraction: VERIFIED.
- Manifest/package identity: VERIFIED.
- Hermes bundle: VERIFIED.
- Gradle host/project reconstruction: PENDING.
- Runtime/build verification: PENDING.
- Original JSX/TypeScript: NOT present in decompiler archive; do not fabricate.
