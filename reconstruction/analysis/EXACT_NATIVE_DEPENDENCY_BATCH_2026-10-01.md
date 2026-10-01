# Exact Native Dependency Batch — 2026-10-01

Source-of-truth: `base (1).apk_Decompiler.com.zip`
Size: 104477964 bytes
Package: `com.cerebellummobileapp`
Version: 1.16.2 / 172

## Gated module dependencies verified directly from archive

`sources/com/cerebellummobileapp/FullscreenChipOverlayModule.java`
- exact archive size: 21116 bytes
- exact SHA-256: `b513c855f4bd8c1a912ffc8481ee4348326491d3ae0a9ec7987cf968f281db18`
- source annotation identifies original Kotlin file: `FullscreenChipOverlayModule.kt`
- React Native module name: `FullscreenChipOverlayModule`
- React methods: `show`, `hide`, `addListener`, `removeListeners`
- lifecycle interface: `LifecycleEventListener`
- native drawable dependencies used by the module:
  - `@drawable/ic_watch_paused`
  - `@drawable/ic_chip_close`
- verified archive resources:
  - `resources/res/drawable/ic_watch_paused.xml` — 1449 bytes
  - `resources/res/drawable/ic_chip_close.xml` — 603 bytes
- asset font dependency referenced by the module:
  - `fonts/Inter-Medium.ttf`

## Important fidelity gate
The module is NOT recreated or approximated in repository source from partial output. The exact archive remains authoritative until a byte-preserving promotion path is available.

## Host-project finding
The forensic decompiler archive contains the decoded manifest/resources and native/decompiled source, but no `build.gradle`, `settings.gradle`, `gradlew`, or equivalent original Gradle project files were found at archive root/source paths.

Therefore:
- original Gradle project structure is not evidenced by this archive;
- RN 0.81.0 host reconstruction must be evidence-backed from package/version/dependency metadata and verified Android build requirements;
- no invented original JSX/TypeScript source is permitted.

## Contamination rule
Do not read from or promote `reconstruction/apk_root/` into Cerebellum implementation.
Do not import Marrow/Prepladder assets, classes, routes, or UI.
PYQ layer remains isolated and unchanged.
