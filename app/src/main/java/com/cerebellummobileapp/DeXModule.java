package com.cerebellummobileapp;

import android.content.res.Configuration;
import com.facebook.react.bridge.BaseJavaModule;
import com.facebook.react.bridge.Promise;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import com.google.android.gms.cast.MediaError;

public final class DeXModule extends ReactContextBaseJavaModule {
    public DeXModule(ReactApplicationContext reactContext) { super(reactContext); }
    @Override public String getName() { return "DeXModule"; }
    @ReactMethod public final void checkDeXEnabled(Promise promise) {
        Configuration configuration = getReactApplicationContext().getResources().getConfiguration();
        try {
            Class<?> cls = configuration.getClass();
            promise.resolve(Boolean.valueOf(cls.getField("SEM_DESKTOP_MODE_ENABLED").getInt(cls) == cls.getField("semDesktopModeEnabled").getInt(configuration)));
        } catch (Exception e) { promise.reject(MediaError.ERROR_TYPE_ERROR, e); }
    }
}
