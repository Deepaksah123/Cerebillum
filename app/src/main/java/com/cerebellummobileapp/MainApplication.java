package com.cerebellummobileapp;

import android.app.Application;
import android.content.Context;
import com.facebook.react.PackageList;
import com.facebook.react.ReactApplication;
import com.facebook.react.ReactHost;
import com.facebook.react.ReactNativeApplicationEntryPoint;
import com.facebook.react.ReactNativeHost;
import com.facebook.react.ReactPackage;
import com.facebook.react.defaults.DefaultReactHost;
import com.facebook.react.defaults.DefaultReactNativeHost;
import com.google.firebase.analytics.FirebaseAnalytics;
import com.hotupdater.HotUpdater;
import java.util.ArrayList;
import java.util.List;
import kotlin.jvm.internal.Intrinsics;

public final class MainApplication extends Application implements ReactApplication {
    private final ReactNativeHost reactNativeHost = new DefaultReactNativeHost() {
        private final boolean isHermesEnabled;
        private final boolean isNewArchEnabled;
        @Override public boolean getUseDeveloperSupport() { return false; }
        { super(MainApplication.this); this.isNewArchEnabled = true; this.isHermesEnabled = true; }
        @Override protected List<ReactPackage> getPackages() {
            ArrayList<ReactPackage> packages = new PackageList(this).getPackages();
            packages.add(new DevOptionsPackage());
            packages.add(new DeXPackage());
            packages.add(new ScreenshotPackage());
            packages.add(new PipHelperPackage());
            packages.add(new FullscreenChipOverlayPackage());
            Intrinsics.checkNotNullExpressionValue(packages, "apply(...)");
            return packages;
        }
        @Override protected String getJSMainModuleName() { return FirebaseAnalytics.Param.INDEX; }
        @Override protected String getJSBundleFile() {
            HotUpdater.Companion companion = HotUpdater.INSTANCE;
            Context applicationContext = MainApplication.this.getApplicationContext();
            Intrinsics.checkNotNullExpressionValue(applicationContext, "getApplicationContext(...)");
            String jSBundleFile = companion.getJSBundleFile(applicationContext);
            return jSBundleFile == null ? super.getJSBundleFile() : jSBundleFile;
        }
        @Override protected boolean getIsNewArchEnabled() { return this.isNewArchEnabled; }
        @Override protected boolean getIsHermesEnabled() { return this.isHermesEnabled; }
    };
    @Override public ReactNativeHost getReactNativeHost() { return this.reactNativeHost; }
    @Override public ReactHost getReactHost() {
        Context applicationContext = getApplicationContext();
        Intrinsics.checkNotNullExpressionValue(applicationContext, "getApplicationContext(...)");
        return DefaultReactHost.getDefaultReactHost$default(applicationContext, getReactNativeHost(), null, 4, null);
    }
    @Override public void onCreate() {
        super.onCreate();
        ReactNativeApplicationEntryPoint.loadReactNative(this);
    }
}