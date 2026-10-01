# Cerebellum UI Recovery Batch — Source-Backed State Matrix — 2026-10-01

## Provenance
Primary evidence: verified Cerebellum forensic artifacts for `base (1).apk`, the exact APK path tree, and the Hermes-derived GROUND_TRUTH_UI_MAP. Screenshots/old HTML reconstructions are not implementation authority.

## Native shell
- Package: `com.cerebellummobileapp`
- React Native 0.81.0
- Hermes enabled
- New Architecture enabled
- Root component: `cerebellumMobileApp`
- MainActivity/MainApplication verified
- HotUpdater evidence present
- Native modules: DeX, DevOptions, FullscreenChipOverlay, PiP, Screenshot

## Screen/state lanes

### Home
Evidence identifiers:
- HomePage
- /home
Related verified navigation vocabulary includes QBank, Test, Video, Profile routes.
Status: component/route proven; exact JSX hierarchy remains unproven.

### QBank
Evidence identifiers:
- QbankQuestions
- /qbank
- /questions-data
- /question-details
- /bookmarked-questions
- /qbank/performance-analytics
Question-related evidence also includes:
- answer/reveal handling vocabulary
- bookmark state vocabulary
- next/previous handler vocabulary
- report-question handler vocabulary
- question analytics/performance routes
Status: behavior vocabulary proven; exact original component tree remains unproven.

### Subject / Chapter
Evidence identifiers:
- Subject
- SubjectDetails
- SubjectOverview
- SubjectCard
- ChapterList
- /subject
- /chapter
Status: subject/chapter navigation and component vocabulary proven.

### Tests / Analytics
Evidence identifiers:
- TestAnalytics
- /test
- /test-analytics
- /testSessions
- /grand-test
- /live-tests
- /session-result-summary
- /mock_test/session-result-summary
Status: route/component vocabulary proven. Exact test-state implementation requires native source/runtime evidence.

### Video
Evidence identifiers:
- Video
- VideoCard
- VideoDetail
- VideoPlayback
- VideoSession
- VideoQuality
- VideoProgress
- /video-category
- /video-category-units
- /video-session
- /latest-video-session
- /bookmarked-videos
Status: video component/state vocabulary is strongly represented in Hermes strings. Exact layout remains unpromoted.

### Notes / Flashcards
Evidence identifiers:
- Notes
- Flashcard / Flashcards
- /notes
- /notes-page
- /flashcard
Status: component and route vocabulary proven.

### Profile / Plans
Evidence identifiers:
- Profile
- PlanList
- /profile
- /plans
- /subscription
- /user-profile/me
Status: component and route vocabulary proven.

## Design-system evidence
Recovered class vocabulary proves the original bundle uses:
- Inter
- OpenSauceOne
- Besley
- primary-blue / primary-dark / primary-* scales
- customGray scales
- error / success / secondary / extras scales
- rounded-xl / rounded-2xl / rounded-full
- spacing families p-*, px-*, py-*
These are evidence of token vocabulary, not permission to invent exact numeric mappings where the bundle does not expose them cleanly.

## Dynamic content boundary
Question/video media and API-returned content remain runtime/data-source content unless exact APK ownership is proven. Do not embed screenshot crops or unrelated static media.

## Promotion rule
A screen/state can move from evidence to implementation only when:
1. exact native source/resource is recovered, OR
2. compiled-bundle evidence establishes the identifier/behavior and the implementation is explicitly marked as reconstructed rather than original, OR
3. genuine runtime observation verifies the state.

No invented component hierarchy, fake API response, Marrow-derived UI, or screenshot-derived implementation is allowed.

## Current hard blocker
The verified 104,477,964-byte decompiler archive is documented in Library forensic reports but is not currently available as a materialized binary/source tree in the Cerebillum repository. Therefore MainActivity/MainApplication source bytes, native module source, exact Hermes bundle bytes, and Gradle host source must not be fabricated.

## PYQ barrier
Protected:
- 9,354 records
- 7,288 mapped
- 2,066 unresolved
- 0 ambiguous
- 19 subjects
- 2015–2025
No native UI batch may modify these mappings.
