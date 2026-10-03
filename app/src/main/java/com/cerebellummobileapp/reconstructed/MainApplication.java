package com.cerebellummobileapp.reconstructed;

import android.app.Application;
import android.content.Context;
import com.facebook.react.ReactApplication;
import com.facebook.react.ReactHost;
import com.facebook.react.ReactNativeHost;
import com.facebook.react.ReactPackage;
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint;
import com.facebook.react.defaults.DefaultReactHost;
import com.facebook.react.defaults.DefaultReactNativeHost;
import com.facebook.soloader.SoLoader;
import java.util.ArrayList;
import java.util.List;

public final class MainApplication extends Application implements ReactApplication {
    private final ReactNativeHost reactNativeHost = new DefaultReactNativeHost(this) {
        @Override public boolean getUseDeveloperSupport() { return false; }
        @Override protected List<ReactPackage> getPackages() { return new ArrayList<>(); }
        @Override protected String getJSMainModuleName() { return "index"; }
        @Override protected boolean isNewArchEnabled() { return true; }
        @Override protected boolean isHermesEnabled() { return true; }
    };

    @Override public ReactNativeHost getReactNativeHost() { return reactNativeHost; }

    @Override public ReactHost getReactHost() {
        Context applicationContext = getApplicationContext();
        return DefaultReactHost.getDefaultReactHost(applicationContext, reactNativeHost, null);
    }

    @Override public void onCreate() {
        super.onCreate();
        SoLoader.init(this, false);
        DefaultNewArchitectureEntryPoint.load();
    }
}
