# Cerebellum Parallel Batch — Native/UI Evidence Lock
Date: 2026-10-01

## Batch A — Native shell evidence
LOCKED TO CEREBELLUM:
- package: com.cerebellummobileapp
- RN component: cerebellumMobileApp
- React Native 0.81.0
- Hermes enabled
- New Architecture enabled
- HotUpdater present
- MainActivity / MainApplication verified by forensic report
- native modules: DeX, DevOptions, FullscreenChipOverlay, PiP, Screenshot
- exact bundle: assets/index.android.bundle, 11,206,868 bytes

## Batch B — UI/navigation evidence
Source-backed component identifiers include:
HomePage, CustomModule, ChapterList, QbankQuestions, TestAnalytics, Review,
Subject, Video, Profile, Notes, Flashcard, PlanList.

Verified route vocabulary includes:
 /home
 /qbank
 /pyq
 /grand-test
 /chapter
 /subject
 /video-category
 /video-category-units
 /live-tests
 /test
 /test-analytics
 /qbank/performance-analytics
 /notes
 /notes-page
 /flashcard
 /profile
 /plans
 /subscription

Do not invent routes not evidenced by the forensic bundle.

## Batch C — Dynamic/content boundary
Verified API vocabulary includes qbank/questions/question-details,
subject/chapter/video/test analytics/bookmark/profile routes.
Dynamic question media is NOT promoted to static APK content unless ownership is proven.

## Batch D — exact APK resource inventory
The exact Cerebellum APK tree is separately documented as:
- source: cere_org_ui_voad.zip
- 2,205 entries
- six DEX files
- assets/index.android.bundle
- bundled fonts including Inter, OpenSauceOne, Besley and icon fonts
- AndroidManifest.xml
This evidence is Cerebellum-only.

## Batch E — contamination barrier
EXCLUDED:
- reconstruction/apk_root current contents, because its decoded manifest is com.marrow.
- any Marrow source/UI/assets/navigation/data.
- screenshot-derived implementation.
- guessed React/Java/Kotlin source.
- unresolved PYQ subject mappings.

## Batch F — PYQ protection
PYQ remains unchanged:
9,354 total records; 7,288 safely mapped; 2,066 unresolved; 0 ambiguous; 19 subjects; 2015–2025.
Native work must not rewrite or force-map these records.

## Gate
The project can proceed to native implementation only from exact Cerebellum APK/decompiler bytes. The forensic reports establish the architecture and evidence, but do not justify fabricating missing source bytes.
