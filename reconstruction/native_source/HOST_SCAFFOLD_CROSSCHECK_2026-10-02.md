# Host Scaffold Evidence Update — 2026-10-02

Cross-check against exact Cerebellum forensic lock:
- AGP 8.11.0 is directly recorded in APK metadata and matches repository root build.gradle.
- compileSdk/targetSdk 36, minSdk 26, package com.cerebellummobileapp, version 1.16.2/versionCode 172 match.
- MainApplication/MainActivity/PiP receiver boundary is present.
- Current app/build.gradle intentionally has no guessed React Native/Hermes dependency graph.
- Exact RN 0.81.0, Hermes and New Architecture remain evidence-backed but cannot be converted into a reproducible Gradle dependency graph from APK artifact presence alone.
- Exact Hermes bundle remains gated by SHA-256 d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2.
- Exact FullscreenChipOverlayModule.java and generated R.java remain gated.
- PYQ layer is unchanged.
- Contamination barrier remains mandatory.

Decision:
The current host scaffold is internally consistent with the verified package/SDK/AGP boundary. Do not add placeholder RN dependency versions merely to force a build.
