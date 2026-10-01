# Cerebellum UI Implementation Lock — 2026-10-01

## Provenance
Source: genuine Cerebellum APK/decompiler evidence for package `com.cerebellummobileapp`, version 1.16.2 (172), React Native 0.81.0, Hermes, New Architecture.

## Compiled UI identifiers recovered from the original Hermes bundle
- HomePage
- CustomModule
- ChapterList
- QbankQuestions
- TestAnalytics
- Review
- Subject
- SubjectDetails
- SubjectOverview
- SubjectAccess
- SubjectCard
- Video
- Profile
- Notes
- Flashcard
- Flashcards
- PlanList

## Verified navigation vocabulary
`/home`, `/qbank`, `/pyq`, `/grand-test`, `/chapter`, `/subject`, `/video-category`, `/video-category-units`, `/live-tests`, `/test`, `/test-analytics`, `/qbank/performance-analytics`, `/notes`, `/notes-page`, `/flashcard`, `/profile`, `/plans`, `/subscription`.

## Verified API vocabulary
`/qbank`, `/questions-data`, `/question-details`, `/questions`, `/subject`, `/subjects`, `/chapter`, `/subject-video-detail`, `/video-category`, `/video-category-units`, `/video-session`, `/latest-video-session`, `/qbank-detail`, `/qbank-annotations`, `/qbank/performance-analytics`, `/testSessions`, `/test`, `/test-analytics`, `/session-result-summary`, `/mock_test/session-result-summary`, `/live-tests`, `/grand-test`, `/flashcard`, `/notes-page`, `/bookmarked-questions`, `/bookmarked-videos`, `/profile`, `/user-profile/me`, `/latest-session`, `/attempted-question`, `/subject-wise-qbank-analysis`.

## UI design evidence
Verified token vocabulary includes Inter, OpenSauceOne and Besley fonts plus icon fonts; primary/secondary/error/success scales; custom gray/background tokens; rounded-xl/2xl/full; and p/px/py spacing tokens.

## Implementation boundary
1. These identifiers are evidence, not permission to invent screen layouts.
2. Screens/components must be implemented only when their structure is supported by APK resources, compiled-bundle evidence, recovered native source, or verified runtime/reference evidence.
3. Dynamic question/video media remains a data-source slot unless APK ownership is proven.
4. Do not import Marrow, Prepladder, or unrelated reconstruction assets/classes.
5. PYQ extraction/content is a protected layer and must not be rewritten by UI work.
6. The exact Hermes bundle remains authoritative; readable strings are not treated as reconstructed JavaScript source.

## Current native host state
The Android shell contains the verified Cerebellum package boundary, MainActivity/MainApplication, native module/package transcriptions, PiP receiver/helper, screenshot module, and exact overlay drawable resources. Exact FullscreenChipOverlayModule.java and generated R.java remain gated and must not be manually guessed.

## Next promotion gate
Promote the exact Hermes bundle and remaining exact app-owned resources only from verified source bytes. Then wire the RN 0.81 host/dependencies and run package/build/runtime verification before claiming the reconstructed UI is functional.
