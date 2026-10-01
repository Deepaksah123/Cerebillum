# Cerebellum Native Source Recovery Map — 2026-10-01

## Purpose
Record the current native-source gate without importing or treating unrelated APK evidence as Cerebellum evidence.

## Verified repository state
- Repository: Deepaksah123/Cerebillum
- Branches verified: main, cerebellum-pyq-phase1
- Root contains four recovered APK ZIP archives and reconstruction/ analysis trees.
- No root Android Gradle project was found at the expected paths: settings.gradle(.kts), build.gradle(.kts), app/build.gradle(.kts), gradlew.
- No Kotlin/Java application source tree was verified in the repository.
- WEBREPLITX5 searches for Cerebellum-specific AndroidManifest.xml, build.gradle, and MainActivity returned no results.

## Critical evidence contamination finding
The decoded manifest stored at reconstruction/analysis/deep/manifest.md identifies:
- package="com.marrow"
- Marrow-specific themes such as Marrow2/AppTheme
- Marrow activity namespaces such as com.marrow.* and com.marrow2.*

Therefore the current recovered APK/decompiler tree must NOT be used as Cerebellum native implementation evidence. This is a hard provenance gate.

## Safe state
- Cerebellum PYQ extraction remains valid and separate: 41 source files, 9,354 records, 7,288 safely mapped, 2,066 unresolved.
- Generated PYQ HTML/native handoff remains staging only.
- No native Android integration is claimed.
- No Gradle project, Activity, Manifest, package identity, WebView path, or navigation path will be invented from the contaminated recovered tree.

## Required recovery target
A verified Cerebellum-native source/evidence package is required before integration:
1. Original Cerebellum APK whose decoded manifest/package identity is Cerebellum-specific, OR
2. A verified Cerebellum decompiler/reconstruction tree whose package/classes/assets can be provenance-linked to that APK, OR
3. A rebuildable Cerebellum Android source tree containing Gradle + Manifest + Kotlin/Java source.

## Verification gate once recovered
- Verify APK package/applicationId and signing metadata.
- Verify launcher Activity and navigation/content-loading path.
- Verify QBank/PYQ asset-loading mechanism from native evidence.
- Verify no Marrow identifiers/assets/classes enter the Cerebellum build.
- Only then place the already-validated Cerebellum PYQ layer into the verified native content layer.
- Build through GitHub Actions, then runtime-test PYQ launch/navigation/content and installation coexistence.

## Prohibited
Do not use screenshots, WEBREPLITX5 web-only architecture, Marrow source/assets, or the currently decoded com.marrow APK tree to fabricate missing native implementation.
