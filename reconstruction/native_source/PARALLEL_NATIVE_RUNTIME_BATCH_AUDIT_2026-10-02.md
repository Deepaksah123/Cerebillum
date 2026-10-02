# Cerebellum Parallel Native/Runtime Batch Audit — 2026-10-02

## Batch result

- Corrected commit: 8c53550ebe60419927fe11d0372a56170544cb19
- Contamination Barrier run: 37026136016 — SUCCESS
- Fallback build run: 37026136175 — SUCCESS
- APK artifact: app-debug.apk
- APK size: 5,087,091 bytes
- APK SHA-256: 4dc8fc5c5e28f66a22e22c37723c961ed41697d6c8b4f3bd08cfb74ed3b830ad
- Artifact ID: 11234574351
- Artifact expiry: 2026-10-16

## Native-source batch audit

13 repository-native Java sources under reconstruction/native_source/cerebellummobileapp were checked.

All 13:
- declare package com.cerebellummobileapp
- contain no com.marrow / marrow / prepladder identifiers
- remain inside the Cerebellum native-source boundary

Checked:
BuildConfig.java, DeXModule.java, DeXPackage.java, DevOptionsModule.java,
DevOptionsPackage.java, FullscreenChipOverlayPackage.java, MainActivity.java,
MainApplication.java, PipActionReceiver.java, PipHelperModule.java,
PipHelperPackage.java, ScreenshotModule.java, ScreenshotPackage.java.

## Repository boundary

Current recursive tree contains no quarantined legacy paths or forbidden Marrow/Prepladder paths.
The active app manifest declares package com.cerebellummobileapp.
Application ID/namespace remain com.cerebellummobileapp, version 1.16.2, versionCode 172,
minSdk 26, targetSdk 36.

## Exact Hermes runtime gate

The exact recovered Cerebellum Hermes bundle remains NOT PROMOTED.

Authoritative recovered artifact:
- resources/assets/index.android.bundle
- size 11,206,868 bytes
- SHA-256 d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2

The current fallback APK is a buildable fallback shell, not a byte-identical React Native/Hermes runtime.
No regenerated JavaScript or guessed UI is being promoted as native reconstruction.

## UI evidence lock

The evidence registry still defines the verified Cerebellum component/route/API vocabulary.
No unresolved behavior is being invented from screenshots.
PYQ mappings remain protected; unresolved records remain unresolved.

## Next consolidated gate

Do not perform another cosmetic/mini implementation step.
The next meaningful promotion gate is either:
1. transfer/promote the exact Hermes bundle into the repository and build the real RN runtime, or
2. if exact-bundle transfer remains technically unavailable, perform a single consolidated fallback APK runtime/content audit and record the boundary explicitly.

No Marrow/Prepladder assets, routes, classes, or content are to enter either path.

## Gate correction

The Host Source Gate initially failed because it incorrectly required all 13 forensic native classes under app/src/main/java. The exact forensic class set is intentionally retained under reconstruction/native_source/cerebellummobileapp until dependency/resource promotion is proven. The gate was corrected to validate the 13-class evidence set there while requiring the two active fallback host classes in app/. No forensic source was copied into the active fallback runtime merely to satisfy the gate.

## Artifact-level QA

The downloaded fallback artifact payload was inspected:
- 11 UI parts plus README present
- concatenated UI payload: 7,467,114 bytes
- concatenated UI payload SHA-256: 0cc6dad1bdc4506971d5d80fbd6ac4208562e27f53e294dd6794c352d17c739d
- major Cerebellum route vocabulary present: home, qbank, pyq, grand-test, chapter, subject, video-category, video-category-units, test, test-analytics, notes, notes-page, flashcard, profile and related API routes
- zero com.marrow/marrow/prepladder strings found in classes.dex, classes2.dex, or concatenated UI payload

This artifact is still the fallback HTML runtime and is not represented as the exact recovered Hermes runtime.
