# Exact Cerebellum Native Dependency Evidence — 2026-10-02

Source of truth:
- Archive: base (1).apk_Decompiler.com.zip
- Size: 104,477,964 bytes
- Package: com.cerebellummobileapp
- Version: 1.16.2 (172)
- React Native evidence: 0.81.0 (exact bytecode/source annotation evidence)
- Hermes: enabled
- New Architecture: enabled
- Compile/target SDK: 36
- min SDK: 26

Verified package-family inventory from the exact decompiler archive:
- com/facebook/react/: 1,753 entries
- com/hotupdater/: 110 entries
- com/reactnativecommunity/: 139 entries
- com/razorpay/: 190 entries
- com/otpless/: 362 entries
- io/invertase/: 138 entries
- androidx/media3/: 2,062 entries
- androidx/work/: 528 entries
- com/google/firebase/: 1,576 entries
- com/google/android/gms/: 8,861 entries

Exact manifest evidence:
- Google Play Billing client metadata: 7.1.1
- Application: com.cerebellummobileapp.MainApplication
- Main activity: com.cerebellummobileapp.MainActivity
- HotUpdater recovery receiver/activity are app-owned runtime dependencies.
- React Native WebView FileProvider is present.
- usesCleartextTraffic=true
- resizeableActivity=true
- supportsPictureInPicture=true
- screen orientation is unspecified.

Exact bundle evidence:
- resources/assets/index.android.bundle
- size: 11,206,868 bytes
- SHA-256: d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2

Promotion rule:
- This inventory is evidence only.
- No dependency version is promoted unless directly supported by the exact archive or an independently verified project source.
- The Hermes bundle must be the exact binary above; regenerated JS, screenshot-derived UI, or a guessed bundle is prohibited.
- PYQ content remains protected and is not modified by this batch.
- Marrow/Prepladder content is excluded.
