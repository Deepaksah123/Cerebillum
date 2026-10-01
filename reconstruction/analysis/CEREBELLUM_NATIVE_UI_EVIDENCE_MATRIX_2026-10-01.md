# Cerebellum Native UI Evidence Matrix — 2026-10-01

## Purpose
This file is a source-backed UI recovery matrix. It does not promote screenshot-derived HTML or guessed React/JS into native implementation.

## Proven native/client architecture
- Application ID: com.cerebellummobileapp
- Version: 1.16.2 / versionCode 172
- React Native: 0.81.0
- Hermes: enabled
- New Architecture: enabled
- RN root component: cerebellumMobileApp
- MainActivity: com.cerebellummobileapp.MainActivity
- MainApplication: com.cerebellummobileapp.MainApplication
- Native modules evidenced: DeX, DevOptions, FullscreenChipOverlay, PiP, Screenshot
- Original Hermes bundle: assets/index.android.bundle, 11,206,868 bytes

## Source-backed screen/component vocabulary
| Component | Evidence status | Allowed use |
|---|---|---|
| HomePage | verified in Hermes bundle | navigation/UI evidence |
| CustomModule | verified in Hermes bundle | navigation/UI evidence |
| ChapterList | verified in Hermes bundle | navigation/UI evidence |
| QbankQuestions | verified in Hermes bundle | navigation/UI evidence |
| TestAnalytics | verified in Hermes bundle | navigation/UI evidence |
| Review | verified in Hermes bundle | navigation/UI evidence |
| Subject | verified in Hermes bundle | navigation/UI evidence |
| Video | verified in Hermes bundle | navigation/UI evidence |
| Profile | verified in Hermes bundle | navigation/UI evidence |
| Notes | verified in Hermes bundle | navigation/UI evidence |
| Flashcard | verified in Hermes bundle | navigation/UI evidence |
| PlanList | verified in Hermes bundle | navigation/UI evidence |

## Source-backed route vocabulary
/home, /qbank, /pyq, /grand-test, /chapter, /subject,
/video-category, /video-category-units, /live-tests, /test,
/test-analytics, /qbank/performance-analytics, /notes,
/notes-page, /flashcard, /profile, /plans, /subscription

No additional route should be invented without new evidence.

## Source-backed API vocabulary
/qbank
/questions-data
/question-details
/questions
/subject
/subjects
/chapter
/subject-video-detail
/video-category
/video-category-units
/video-session
/latest-video-session
/qbank-detail
/qbank-annotations
/qbank/performance-analytics
/testSessions
/test
/test-analytics
/session-result-summary
/mock_test/session-result-summary
/live-tests
/grand-test
/flashcard
/notes-page
/bookmarked-questions
/bookmarked-videos
/profile
/user-profile/me
/latest-session
/attempted-question
/subject-wise-qbank-analysis

API base: https://app.cerebellumacademy.com/api/v1

## Verified app-owned visual/font evidence
The forensic inventory documents 65 app-owned visual assets and 12 original font files. Examples include:
- images_custommodule_qbankquestions.webp
- images_custommodule_previousyearquestions.webp
- images_custommodule_grandtestquestions.webp
- images_custommodule_allquestions.webp
- images_subjectdetailbackground.webp
- images_videoicon.webp
- images_notesicon.webp
- images_profilecardbg.png
- images_defaultuserprofile.png
- images_transparentlogo.webp
- Inter / OpenSauceOne / Besley and icon fonts

Asset names are evidence of ownership/existence, not proof of their exact placement or full screen layout.

## Native evidence gaps
The Hermes bundle is compiled bytecode. Its readable strings can establish vocabulary, routes, API names and styling tokens, but do not recover original TypeScript/JSX source or exact component hierarchy. Therefore:
- exact original JSX structure is not claimed;
- exact spacing/layout is not guessed;
- screenshot-only UI is not promoted;
- dynamic API media is not copied into APK-owned static assets unless ownership is proven.

## Contamination barrier
Never use:
- reconstruction/apk_root as Cerebellum implementation source (its decoded package is com.marrow);
- Marrow classes/assets/resources/navigation;
- screenshot-derived HTML as native source;
- guessed Java/Kotlin/React source;
- unresolved PYQ mappings.

## PYQ protection
The validated PYQ layer remains untouched:
- 9,354 records
- 7,288 safely mapped
- 2,066 unresolved
- 0 ambiguous
- 19 subjects
- 2015–2025

Native UI recovery must not rewrite or force-map this layer.

## Promotion gate
A UI element is promoted to implementation only when its provenance is one of:
1. exact Cerebellum APK/decompiler resource or native source;
2. exact Hermes/native evidence that establishes the behavior/identifier;
3. verified runtime observation from the genuine Cerebellum package.

Otherwise it remains an evidence gap.
