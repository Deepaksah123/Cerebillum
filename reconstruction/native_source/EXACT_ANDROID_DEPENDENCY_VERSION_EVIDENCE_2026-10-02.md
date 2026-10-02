# Exact Android Dependency Version Evidence — 2026-10-02

Source: exact Cerebellum decompiler archive `base (1).apk_Decompiler.com.zip`.

Verified `resources/META-INF/*.version` values include:
- AndroidX Core 1.17.0; Core-KTX 1.17.0
- Activity 1.9.3; Activity-KTX 1.9.3
- AppCompat 1.7.1; AppCompat resources 1.7.1
- Fragment 1.8.9; Fragment-KTX 1.8.9
- Lifecycle version files present; some are Gradle-generated placeholders and are NOT assigned a version here
- Work Runtime 2.10.4; Work Runtime-KTX 2.10.4
- WebKit 1.14.0
- RecyclerView 1.4.0
- ConstraintLayout 2.2.1
- Material Components 1.13.0
- Room runtime/KTK 2.6.1
- DataStore 1.1.7
- Browser 1.8.0
- Media 1.7.0
- MediaRouter 1.8.1
- SavedState 1.2.1
- Credentials 1.2.2
- Credentials Play Services Auth 1.2.2
- Kotlin Coroutines core/android/play-services 1.9.0
- ProfileInstaller 1.4.0

Additional manifest evidence previously locked:
- Google Play Billing Client 7.1.1

Important boundary:
- These versions are artifact-level evidence from the packaged APK, not a reconstructed Gradle dependency graph.
- No React Native/Hermes Gradle version is invented from this list.
- Exact RN evidence remains RN 0.81.0, Hermes enabled, New Architecture enabled.
- Exact Hermes bundle remains locked by SHA and is not replaced with generated JS.
- PYQ and Cerebellum content layers remain untouched.
