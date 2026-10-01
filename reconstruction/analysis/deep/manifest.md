# Manifest Deep Analysis

## Decoded AndroidManifest.xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" android:compileSdkVersion="35" android:compileSdkVersionCodename="15" package="com.marrow" platformBuildVersionCode="35" platformBuildVersionName="15">
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS"/>
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    <uses-permission android:name="android.permission.READ_MEDIA_VISUAL_USER_SELECTED"/>
    <uses-permission android:maxSdkVersion="32" android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:maxSdkVersion="32" android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.VIBRATE"/>
    <uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.READ_PHONE_STATE"/>
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE"/>
    <uses-permission android:name="android.permission.WAKE_LOCK"/>
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE_DATA_SYNC"/>
    <uses-feature android:name="android.hardware.camera" android:required="false"/>
    <uses-feature android:name="android.hardware.telephony" android:required="false"/>
    <uses-feature android:name="android.hardware.location" android:required="false"/>
    <uses-feature android:name="android.hardware.location.gps" android:required="false"/>
    <queries>
        <package android:name="me.weishu.kernelsu"/>
        <package android:name="com.termtux.kernelsu"/>
        <package android:name="com.rifsxd.ksunext"/>
        <package android:name="com.sukisu.ultra"/>
        <package android:name="me.bmax.apatch"/>
        <package android:name="me.garfieldhan.hiapatch"/>
        <package android:name="com.termux"/>
        <package android:name="com.twj.wksu"/>
        <package android:name="me.yuki.folk"/>
        <package android:name="com.dergoogler.mmrl"/>
        <package android:name="io.github.a13e300.ksuwebui"/>
        <package android:name="com.fox2code.mmm"/>
        <package android:name="com.tsng.hidemyapplist"/>
        <package android:name="org.lsposed.manager"/>
        <package android:name="com.varuns2002.disable_flag_secure"/>
        <package android:name="io.github.lsposed.disableflagsecure"/>
        <package android:name="top.canyie.settingsfirewall"/>
        <intent>
            <data android:host="pay" android:pathPattern=".*" android:scheme="upi"/>
        </intent>
        <intent>
            <action android:name="android.support.customtabs.action.CustomTabsService"/>
        </intent>
        <intent>
            <data android:host="mandate" android:pathPattern=".*" android:scheme="upi"/>
        </intent>
        <intent>
            <data android:pathPattern=".*" android:scheme="upi"/>
        </intent>
        <intent>
            <data android:host="pay" android:pathPattern=".*" android:scheme="juspay"/>
        </intent>
        <intent>
            <data android:host="checkout" android:pathPattern=".*" android:scheme="credpay"/>
        </intent>
        <package android:name="com.tatadigital.tcp.dev"/>
        <package android:name="com.tatadigital.tcp"/>
        <intent>
            <action android:name="android.intent.action.VIEW"/>
            <data android:mimeType="application/uri"/>
        </intent>
        <intent>
            <action android:name="android.intent.action.VIEW"/>
            <data android:mimeType="*/*" android:scheme="*"/>
        </intent>
        <intent>
            <action android:name="android.intent.action.VIEW"/>
            <category android:name="android.intent.category.BROWSABLE"/>
            <data android:host="pay" android:mimeType="*/*" android:scheme="upi"/>
        </intent>
        <intent>
            <action android:name="android.intent.action.MAIN"/>
        </intent>
        <intent>
            <action android:name="android.intent.action.SEND"/>
            <data android:mimeType="*/*"/>
        </intent>
        <intent>
            <action android:name="rzp.device_token.share"/>
        </intent>
        <intent>
            <action android:name="android.intent.action.VIEW"/>
            <data android:scheme="upi"/>
        </intent>
    </queries>
    <uses-permission android:name="android.permission.READ_BASIC_PHONE_STATE"/>
    <uses-permission android:name="android.permission.NFC"/>
    <uses-permission android:name="com.google.android.providers.gsf.permission.READ_GSERVICES"/>
    <uses-feature android:name="android.hardware.nfc" android:required="false"/>
    <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE"/>
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
    <uses-feature android:glEsVersion="0x20000" android:required="true"/>
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    <uses-permission android:name="com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE"/>
    <uses-permission android:name="android.permission.REORDER_TASKS"/>
    <permission android:name="com.marrow.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION" android:protectionLevel="signature"/>
    <uses-permission android:name="com.marrow.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION"/>
    <uses-feature android:name="android.hardware.camera.front" android:required="false"/>
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false"/>
    <uses-feature android:name="android.hardware.camera.flash" android:required="false"/>
    <uses-feature android:name="android.hardware.screen.landscape" android:required="false"/>
    <uses-feature android:name="android.hardware.wifi" android:required="false"/>
    <application android:allowBackup="false" android:appComponentFactory="o._coerceBooleanFromInt" android:extractNativeLibs="false" android:hardwareAccelerated="true" android:icon="@mipmap/ic_launcher" android:label="@string/app_name" android:name=".TrainingApplication" android:supportsRtl="true" android:theme="@style/AppTheme" android:usesCleartextTraffic="true">
        <activity android:exported="false" android:name="o.getMethodTimingTelemetryEnabled" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.LastLocationRequestBuilder" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.concatByteArrays" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.ActivityTransitionSupportedActivityTransition" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.onConnected" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.BaseImplementation" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:launchMode="singleTop" android:name="o.scaleLargeTimestamps" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.isAtLeastV" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.getCredentialList" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.createStringSparseArray" android:theme="@style/Marrow2.Transparent"/>
        <activity android:exported="false" android:name="o.setRatingTags" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zzlb" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zzna" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zzpk" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zat" android:theme="@style/Marrow2"/>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|layoutDirection" android:exported="false" android:name="o.ResolvableApiException" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.isTransferHdr" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.MediaCodecVideoRendererVideoFrameProcessorManagerExternalSyntheticLambda0" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zaac" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.RegisterListenerMethod" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.setForceApplySystemWindowInsetTop" android:theme="@style/Marrow2"/>
        <activity android:name="o.setCheckedIconEnabled" android:theme="@style/Marrow2"/>
        <activity android:name="o.zzbn" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.addAllowedCountryCodes" android:theme="@style/Marrow2"/>
        <activity android:name="o.StreetViewPanoramaFragmentzza" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.serializeIterableToIntentExtra" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zzab" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.getRemoteCreator" android:theme="@style/Marrow2"/>
        <activity android:name="o.setTokenBinding" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.WalletConstantsPaymentMethod" android:theme="@style/Marrow2"/>
        <activity android:name="o.setActionUri" android:theme="@style/Marrow2"/>
        <activity android:name="o.logEventInternalNoInterceptor" android:theme="@style/Marrow2"/>
        <activity android:launchMode="singleTop" android:name="o.createBundleFromClientSettings" android:theme="@style/Marrow2"/>
        <activity android:name="o.SuccessContinuation" android:theme="@style/Marrow2"/>
        <activity android:name="o.zzr" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:launchMode="singleTask" android:name=".ui.activities.plan.renew.RenewActivity" android:screenOrientation="portrait" android:theme="@style/AppTheme"/>
        <activity android:launchMode="singleTask" android:name="o.Cea708DecoderCea708CueInfo" android:screenOrientation="portrait"/>
        <meta-data android:name="a" android:value=""/>
        <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id"/>
        <meta-data android:name="CLEVERTAP_ACCOUNT_ID" android:value="@string/clevertap_account_id"/>
        <meta-data android:name="CLEVERTAP_TOKEN" android:value="@string/clevertap_account_token"/>
        <meta-data android:name="CLEVERTAP_BACKGROUND_SYNC" android:value="1"/>
        <meta-data android:name="CLEVERTAP_NOTIFICATION_ICON" android:value="ic_notification_default"/>
        <meta-data android:name="com.razorpay.ApiKey" android:value="@string/razor_pay_api_key"/>
        <service android:label="Network service" android:name=".services.NetworkAvailableJobService" android:permission="android.permission.BIND_JOB_SERVICE"/>
        <receiver android:exported="true" android:name=".receivers.OSNetworkChangeListener">
            <intent-filter>
                <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
                <action android:name="android.net.wifi.WIFI_STATE_CHANGED"/>
            </intent-filter>
        </receiver>
        <receiver android:exported="true" android:name=".receivers.SystemDevicePlugInReceiver">
            <intent-filter>
                <action android:name="android.hardware.usb.action.USB_STATE"/>
            </intent-filter>
        </receiver>
        <receiver android:exported="true" android:name=".receivers.sms.GooglePlaySMSReceiver">
            <intent-filter>
                <action android:name="com.google.android.gms.auth.api.phone.SMS_RETRIEVED"/>
            </intent-filter>
        </receiver>
        <provider android:authorities="com.marrow.fileprovider" android:exported="false" android:grantUriPermissions="true" android:name="o._isNegInf">
            <meta-data android:name="android.support.FILE_PROVIDER_PATHS" android:resource="@xml/provider_paths"/>
        </provider>
        <provider android:authorities="com.marrow.data.provider" android:exported="false" android:name="o.parseSelectionFlags"/>
        <activity android:name=".ui.activities.plan.PlanActivity" android:screenOrientation="portrait" android:theme="@style/AppThemeV2"/>
        <activity android:exported="true" android:name=".ui.activities.onboarding.deeplinkroute.DeeplinkActivity" android:theme="@style/SplashTheme">
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="link.marrow.com" android:scheme="https"/>
            </intent-filter>
        </activity>
        <activity android:name=".kt.ui.activities.sync.SyncingActivity" android:theme="@style/AppTheme"/>
        <activity android:name=".ui.activities.web.payment.PaymentInternalWebActivity" android:screenOrientation="portrait" android:theme="@style/AppTheme"/>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|layoutDirection" android:name="o.parseRequiredLong" android:theme="@style/AppTheme"/>
        <activity android:exported="true" android:launchMode="singleTask" android:name=".ui.activities.onboarding.deeplinkroute.DeeplinkProcessorActivity" android:theme="@style/SplashTheme">
            <intent-filter android:autoVerify="true">
                <data android:scheme="@string/app_scheme"/>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
            </intent-filter>
            <intent-filter android:autoVerify="true">
                <data android:host="www.marrow.com" android:pathPrefix="/route" android:scheme="http"/>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
            </intent-filter>
            <intent-filter android:autoVerify="true">
                <data android:host="@string/app_share_url_dns" android:pathPrefix="/" android:scheme="https"/>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
            </intent-filter>
            <intent-filter android:autoVerify="true">
                <data android:host="@string/app_share_url_dns" android:pathPrefix="/" android:scheme="http"/>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
            </intent-filter>
        </activity>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|layoutDirection" android:exported="true" android:launchMode="singleTask" android:name=".ui.activities.onboarding.splash.SplashActivity" android:screenOrientation="portrait" android:theme="@style/SplashTheme">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
        <activity android:configChanges="keyboardHidden|orientation" android:name="o.Rstyle" android:theme="@android:style/Theme.Translucent.NoTitleBar"/>
        <activity android:exported="false" android:name="o.getDefaultBindFlags" android:theme="@style/Theme.Marrow2.Dark"/>
        <activity android:exported="false" android:name="com.marrow2.ui.payment.PaymentActivity" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <meta-data android:name="CLEVERTAP_INAPP_EXCLUDE" android:value="com.marrow.ui.activities.onboarding.splash.SplashActivity, LoginActivity"/>
        <activity android:exported="false" android:launchMode="singleTop" android:name="o.zadb" android:theme="@style/Marrow2" android:windowSoftInputMode="adjustPan"/>
        <activity android:name="o.CeaDecoderExternalSyntheticLambda0" android:theme="@style/AppTheme.FullScreen"/>
        <activity android:name="o.parseNextToken" android:screenOrientation="portrait" android:theme="@style/AppTheme"/>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|layoutDirection" android:launchMode="singleTop" android:name=".ui.activities.learn.video.LessonVideoActivity" android:supportsPictureInPicture="true" android:theme="@style/AppTheme.Video" android:windowSoftInputMode="adjustResize"/>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|layoutDirection" android:name="o.paintPixelDataSubBlocks" android:screenOrientation="portrait" android:theme="@style/AppThemeV2" android:windowSoftInputMode="adjustResize"/>
        <activity android:name="o.onSingleTapUp" android:theme="@style/Marrow2"/>
        <activity android:name="o.onTouch" android:theme="@style/Marrow2"/>
        <activity android:launchMode="singleTask" android:name="o.AuthorizationRequestBuilder" android:theme="@style/Marrow2"/>
        <activity android:launchMode="singleTask" android:name="o.buildSpannableString" android:theme="@style/AppThemeV2.Transparent"/>
        <activity android:name="o.setThumbRadius" android:theme="@style/Marrow2"/>
        <service android:exported="true" android:name=".bgservices.PushReceiverService">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT"/>
            </intent-filter>
        </service>
        <activity android:name="o.NavigationViewSavedState" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.getOriginalPriority" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.getSenderId" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.onLoaderReset" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <service android:name="o.maybeNotifyDownstreamFormat"/>
        <service android:name="o.setUpstreamFormat"/>
        <service android:name="o.getAdjustedUpstreamFormat"/>
        <service android:name=".bgservices.imageupload.ImageUploadService"/>
        <service android:name="o.SampleQueueSharedSampleMetadata"/>
        <service android:foregroundServiceType="dataSync" android:name="com.marrow2.ui.settings.kyc.upload.service.ImageUploadService"/>
        <service android:foregroundServiceType="dataSync" android:name="com.marrow2.core.services.video_download.VideoDownloadFGService"/>
        <activity android:name=".kt.ui.activities.plan.UpgradePlanActivity" android:screenOrientation="portrait" android:theme="@style/AppTheme"/>
        <activity android:launchMode="singleTask" android:name="o.SsChunkSource" android:screenOrientation="portrait" android:theme="@style/AppTheme"/>
        <activity android:exported="false" android:name="o.zzaz" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.setClientDataHash" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.getStreetViewPanoramaCamera" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.ActivityLifecycleObserver" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.setSmallestDisplacement" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:exported="false" android:name="o.zzel" android:theme="@style/Marrow2"/>
        <activity android:configChanges="orientation|screenSize" android:name="o.SafeParcelReaderParseException" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:configChanges="orientation|screenSize" android:launchMode="singleTop" android:name="o.createFloatList" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:configChanges="orientation|screenSize" android:name="o.StringResourceValueReader" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:configChanges="orientation|screenSize" android:name="o.writeDoubleArray" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:configChanges="orientation|screenSize" android:name="o.writeLongList" android:screenOrientation="portrait" android:theme="@style/Theme.Marrow2"/>
        <activity android:name="o.setAppId" android:theme="@style/Marrow2"/>
        <activity android:name="o.icon" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.StreetViewSource" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.color" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.getAnchorU" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:launchMode="singleTask" android:name="o.setWatermarkEnabled" android:screenOrientation="portrait" android:theme="@style/Marrow2"/>
        <activity android:name="o.isAtLeastKitKatWatch" android:theme="@style/Marrow2"/>
        <activity android:name="o.ah" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.getSubMeshCount" android:theme="@style/Marrow2"/>
        <activity android:name="o.toInteger" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.packageManager" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.zzfl" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.SupportStreetViewPanoramaFragmentzzb" android:theme="@style/Marrow2"/>
        <activity android:exported="false" android:name="o.getTokenExpiration" android:theme="@android:style/Theme.Translucent.NoTitleBar"/>
        <activity android:exported="false" android:launchMode="singleTask" android:name="in.juspay.hypersdk.core.CustomtabActivity"/>
        <activity android:exported="true" android:launchMode="singleTask" android:name="in.juspay.hypersdk.core.CustomtabResult">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="com.marrow" android:scheme="juspay"/>
            </intent-filter>
        </activity>
        <activity android:exported="false" android:launchMode="singleTop" android:name="in.juspay.hypernfc.NfcActivity">
            <intent-filter>
                <action android:name="android.nfc.action.TECH_DISCOVERED"/>
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>
        <service android:directBootAware="true" android:exported="false" android:name="o.calculatePacketSize">
            <meta-data android:name="com.google.firebase.components:com.google.firebase.crashlytics.ktx.FirebaseCrashlyticsKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.perf.ktx.FirebasePerfKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.perf.FirebasePerfRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.messaging.ktx.FirebaseMessagingKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.remoteconfig.ktx.FirebaseRemoteConfigKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.database.ktx.FirebaseDatabaseKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.analytics.ktx.FirebaseAnalyticsKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.messaging.FirebaseMessagingRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.remoteconfig.RemoteConfigRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.crashlytics.CrashlyticsRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.sessions.FirebaseSessionsRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.analytics.connector.internal.AnalyticsConnectorRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.installations.FirebaseInstallationsRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.database.DatabaseRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.abt.component.AbtRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.datatransport.TransportRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
            <meta-data android:name="com.google.firebase.components:com.google.firebase.ktx.FirebaseCommonKtxRegistrar" android:value="com.google.firebase.components.ComponentRegistrar"/>
        </service>
        <receiver android:enabled="true" android:exported="false" android:name="o.onLoadCompleted"/>
        <receiver android:enabled="true" android:exported="false" android:name="o.onLoadError"/>
        <meta-data android:name="com.mixpanel.android.MPConfig.EnableDebugLogging" android:value="false"/>
        <provider android:authorities="com.marrow.clevertap.fileprovider" android:exported="false" android:grantUriPermissions="true" android:name="o.setPayload">
            <meta-data android:name="android.support.FILE_PROVIDER_PATHS" android:resource="@xml/clevertap_notification_file_paths"/>
        </provider>
        <activity android:configChanges="keyboardHidden" android:name="o.SimpleBasePlayerPlaceholderUid" android:theme="@style/Theme.AppCompat.DayNight.DarkActionBar"/>
        <receiver android:enabled="true" android:exported="false" android:name="o.toBundleWithOneWindowOnly"/>
        <receiver android:exported="true" android:name="com.clevertap.android.sdk.pushnotification.fcm.CTFirebaseMessagingReceiver" android:permission="com.google.android.c2dm.permission.SEND">
            <intent-filter android:priority="-1">
                <action android:name="com.google.android.c2dm.intent.RECEIVE"/>
            </intent-filter>
        </receiver>
        <provider android:authorities="com.marrow.FacebookInitProvider" android:exported="false" android:name="o.DefaultAnalyticsCollectorExternalSyntheticLambda53"/>
        <receiver android:exported="false" android:name="o.lambdaonMaxSeekToPreviousPositionChanged47">
            <intent-filter>
                <action android:name="com.facebook.sdk.ACTION_CURRENT_ACCESS_TOKEN_CHANGED"/>
            </intent-filter>
        </receiver>
        <activity android:configChanges="keyboard|keyboardHidden|orientation|screenSize" android:exported="false" android:name="com.razorpay.CheckoutActivity" android:theme="@style/CheckoutTheme">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
            </intent-filter>
        </activity>
        <activity android:exported="false" android:name="com.razorpay.MagicXActivity" android:theme="@android:style/Theme.Translucent.NoTitleBar"/>
        <activity android:exported="true" android:name="androidx.compose.ui.tooling.PreviewActivity"/>
        <meta-data android:name="com.bumptech.glide.integration.okhttp3.OkHttpGlideModule" android:value="GlideModule"/>
        <receiver android:exported="true" android:name="com.google.firebase.iid.FirebaseInstanceIdReceiver" android:permission="com.google.android.c2dm.permission.SEND">
            <intent-filter>
                <action android:name="com.google.android.c2dm.intent.RECEIVE"/>
            </intent-filter>
        </receiver>
        <service android:directBootAware="true" android:exported="false" android:name="com.google.firebase.messaging.FirebaseMessagingService">
            <intent-filter android:priority="-500">
                <action android:name="com.google.firebase.MESSAGING_EVENT"/>
            </intent-filter>
        </service>
        <activity android:excludeFromRecents="true" android:exported="false" android:name="com.google.android.gms.auth.api.signin.internal.SignInHubActivity" android:theme="@android:style/Theme.Translucent.NoTitleBar"/>
        <service android:exported="true" android:name="com.google.android.gms.auth.api.signin.RevocationBoundService" android:permission="com.google.android.gms.auth.api.signin.permission.REVOCATION_NOTIFICATION" android:visibleToInstantApps="true"/>
        <uses-library android:name="org.apache.http.legacy" android:required="false"/>
        <activity android:exported="false" android:name="com.google.android.gms.common.api.GoogleApiActivity" android:theme="@android:style/Theme.Translucent.NoTitleBar"/>
        <provider android:authorities="com.marrow.firebaseinitprovider" android:directBootAware="true" android:exported="false" android:initOrder="100" android:name="com.google.firebase.provider.FirebaseInitProvider"/>
        <service android:directBootAware="false" android:enabled="@bool/enable_system_job_service_default" android:exported="true" android:name="androidx.work.impl.background.systemjob.SystemJobService" android:permission="android.permission.BIND_JOB_SERVICE"/>
        <service android:directBootAware="false" android:enabled="@bool/enable_system_foreground_service_default" android:exported="false" android:name="o.BundleableCreator"/>
        <receiver android:directBootAware="false" android:enabled="true" android:exported="false" android:name="androidx.work.impl.utils.ForceStopRunnable$BroadcastReceiver"/>
        <receiver android:directBootAware="false" android:enabled="false" android:exported="false" android:name="o.seekToNext">
            <intent-filter>
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>
        <receiver android:directBootAware="false" android:enabled="true" android:exported="true" android:name="androidx.work.impl.diagnostics.DiagnosticsReceiver" android:permission="android.permission.DUMP">
            <intent-filter>
                <action android:name="androidx.work.diagnostics.REQUEST_DIAGNOSTICS"/>
            </intent-filter>
        </receiver>
        <receiver android:enabled="true" android:exported="false" android:name="com.google.android.gms.measurement.AppMeasurementReceiver"/>
        <service android:enabled="true" android:exported="false" android:name="com.google.android.gms.measurement.AppMeasurementService"/>
        <service android:enabled="true" android:exported="false" android:name="com.google.android.gms.measurement.AppMeasurementJobService" android:permission="android.permission.BIND_JOB_SERVICE"/>
        <uses-library android:name="androidx.window.extensions" android:required="false"/>
        <uses-library android:name="androidx.window.sidecar" android:required="false"/>
        <activity android:exported="true" android:name="androidx.test.core.app.InstrumentationActivityInvoker$BootstrapActivity" android:theme="@android:style/Theme">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
            </intent-filter>
        </activity>
        <activity android:exported="true" android:name="androidx.test.core.app.InstrumentationActivityInvoker$EmptyActivity" android:theme="@android:style/Theme">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
            </intent-filter>
        </activity>
        <activity android:exported="true" android:name="androidx.test.core.app.InstrumentationActivityInvoker$EmptyFloatingActivity" android:theme="@android:style/Theme.Dialog">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
            </intent-filter>
        </activity>
        <service android:directBootAware="true" android:exported="false" android:name="o.asULong"/>
        <meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version"/>
        <receiver android:directBootAware="false" android:enabled="true" android:exported="true" android:name="androidx.profileinstaller.ProfileInstallReceiver" android:permission="android.permission.DUMP">
            <intent-filter>
                <action android:name="androidx.profileinstaller.action.INSTALL_PROFILE"/>
            </intent-filter>
            <intent-filter>
                <action android:name="androidx.profileinstaller.action.SKIP_FILE"/>
            </intent-filter>
            <intent-filter>
                <action android:name="androidx.profileinstaller.action.SAVE_PROFILE"/>
            </intent-filter>
            <intent-filter>
                <action android:name="androidx.profileinstaller.action.BENCHMARK_OPERATION"/>
            </intent-filter>
        </receiver>
        <service android:exported="false" android:name="com.google.android.datatransport.runtime.backends.TransportBackendDiscovery">
            <meta-data android:name="backend:com.google.android.datatransport.cct.CctBackendFactory" android:value="cct"/>
        </service>
        <service android:exported="false" android:name="com.google.android.datatransport.runtime.scheduling.jobscheduling.JobInfoSchedulerService" android:permission="android.permission.BIND_JOB_SERVICE"/>
        <receiver android:exported="false" android:name="o.lambdareleaseManagerOnHandlerThread4comgoogleandroidexoplayer2drmOfflineLicenseHelper"/>
        <activity android:exported="false" android:name="o.assertInTrackEntry" android:stateNotNeeded="true" android:theme="@style/Theme.PlayCore.Transparent"/>
        <activity android:exported="true" android:name="com.razorpay.DeeplinkActivity" android:theme="@style/CheckoutTheme">
            <intent-filter>
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="com.marrow" android:scheme="razorpay"/>
            </intent-filter>
        </activity>
        <receiver android:exported="false" android:name="com.razorpay.UpiChooserSelectionReceiver"/>
    </application>
</manifest>

## Apktool log
I: Using Apktool 3.0.3 on cerebillum.apk with 4 threads
I: Baksmaling classes2.dex...
I: Baksmaling classes3.dex...
I: Loading resource table...
I: Baksmaling classes4.dex...
I: Decoding value resources...
I: Loading resource table from file: /home/runner/.local/share/apktool/framework/1.apk
I: Decoding file resources...
I: Generating values XMLs...
I: Decoding AndroidManifest.xml with resources...
I: Baksmaling classes5.dex...
I: Baksmaling classes.dex...
I: Copying original files...
I: Copying assets...
I: Copying lib...
I: Copying unknown files...

## Resource directory counts
380
