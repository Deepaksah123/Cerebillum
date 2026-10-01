# Cerebellum Contamination Rejection — 2026-10-01

## Rejected evidence path

`reconstruction/apk_root/` is NOT a Cerebellum source tree.

The repository's legacy deep-analysis output `reconstruction/analysis/deep/manifest.md` was inspected and contains Marrow-specific evidence including:
- `com.marrow`
- `Theme.Marrow2`
- Marrow activity/class identifiers
- `com.marrow` authorities/schemes

Therefore that output is rejected for Cerebellum reconstruction.

## Required rule

No implementation, resource, manifest, navigation, UI, dependency, or content decision may be derived from:
- `reconstruction/apk_root/`
- deep-analysis outputs generated from that tree
- any Marrow/Prepladder-derived reconstruction material

## Authoritative Cerebellum source

Use only the verified forensic archive:
`base (1).apk_Decompiler.com.zip`

Verified identity:
- package: `com.cerebellummobileapp`
- version: 1.16.2 / 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- exact bundle SHA-256: `d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2`
- exact AndroidManifest SHA-256: `249d2276fc75f23c6bd310f3c0da5bcbbf0ea48ffa3e31539045e0eae718c098`

## PYQ barrier

The protected PYQ layer remains untouched.

## Promotion gate

Only archive-backed, Cerebellum-identity-verified material may enter the implementation layer. Unknown or conflicting evidence remains gated rather than reconciled by guesswork.
