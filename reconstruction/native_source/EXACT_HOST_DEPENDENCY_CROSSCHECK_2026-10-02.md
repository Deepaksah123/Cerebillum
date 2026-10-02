# Exact Host Dependency Crosscheck — 2026-10-02

Authoritative decompiler archive crosscheck:

- Android Gradle Plugin metadata: 8.11.0
- React Native BuildConfig source is present in the exact archive.
- Hermes executor/classes are present.
- The archive does not contain a Gradle project graph or original build.gradle/settings.gradle files.
- Therefore AGP 8.11.0 remains safe to use, but React Native/Hermes Gradle dependency declarations are not promoted as exact until their original graph is recovered or independently byte/evidence verified.

No dependency declaration was fabricated in this batch.
