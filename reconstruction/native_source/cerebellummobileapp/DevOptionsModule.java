package com.cerebellummobileapp;

import android.provider.Settings;
import com.facebook.react.bridge.Promise;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;

public final class DevOptionsModule extends ReactContextBaseJavaModule {
    private static ReactApplicationContext reactContext;
    public DevOptionsModule(ReactApplicationContext reactContext2) { super(reactContext2); reactContext = reactContext2; }
    @Override public String getName() { return "DevOptions"; }
    @ReactMethod public final void isDevelopmentSettingsEnabled(Promise promise) {
        try {
            promise.resolve(Boolean.valueOf(Settings.Secure.getInt(getReactApplicationContext().getContentResolver(), "development_settings_enabled", 0) == 1));
        } catch (Exception e) { promise.reject("Error", e); }
    }
}
