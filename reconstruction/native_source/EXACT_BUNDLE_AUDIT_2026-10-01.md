# Exact Cerebellum Bundle Audit — 2026-10-01

## Exact bundle
- Path: resources/assets/index.android.bundle
- Size: 11,206,868 bytes
- SHA-256: d0e2d33a709316ae8fc55afd24b2540f6ab50e72ab2a9dbcaac419731be5afe2
- Hermes bytecode; printable strings are evidence vocabulary, not reconstructed JS source.

## Verified components
- cerebellumMobileApp
- HomePage
- QbankQuestions
- SubjectDetails
- TestAnalytics
- ChapterList
- CustomModule
- Review
- Video
- Profile
- Notes
- Flashcard
- PlanList

## Verified route vocabulary
- /home
- /qbank
- /qbank/performance-analytics
- /subject
- /chapter
- /video-session
- /profile
- /test
- /test-analytics
- /notes
- /flashcard

## Contamination check
- prepladder: 0 occurrences
- marrow: 1 textual occurrence, inside a color/hex-name string and not a package, class, route, asset, or content identifier.

## Promotion boundary
The Hermes bundle is exact source evidence. Do not decompile it into invented JavaScript and treat that as original source.