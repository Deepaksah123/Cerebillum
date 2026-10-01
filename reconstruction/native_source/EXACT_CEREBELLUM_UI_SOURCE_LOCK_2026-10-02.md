# Exact Cerebellum UI Source Lock — 2026-10-02

## Exact decompiler archive
- Filename: `base (1).apk_Decompiler.com.zip`
- Size: 104,477,964 bytes
- Entries: 46,647
- Package: `com.cerebellummobileapp`
- Version: 1.16.2 / versionCode 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled

## Exact Hermes bundle
- Archive path: `resources/assets/index.android.bundle`
- Size: 11,206,868 bytes
- SHA-256: `d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2`

## Exact manifest
- Archive path: `resources/AndroidManifest.xml`
- Size: 41,228 bytes
- SHA-256: `249d2276fc75f23c6bd310f3c0da5bcbbf0ea48ffa3e31539045e0eae718c098`

## UI boundary
The Hermes bundle is the authoritative UI implementation artifact. Its readable strings provide verified component/route/API vocabulary but are not treated as recovered JSX/TypeScript source.

The repository currently promotes exact small native UI resources (PiP play/pause and fullscreen-chip resources) and evidence registries. The 11.2 MB Hermes bytecode is intentionally not replaced with a guessed or regenerated bundle.

## Promotion gate
Any future bundle promotion must reproduce the exact SHA above. Any mismatch is a hard stop. No screenshot, Marrow source, Prepladder source, or hand-written substitute may satisfy this gate.
