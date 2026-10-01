package com.cerebellummobileapp;

import android.app.Activity;
import android.hardware.display.DisplayManager;
import com.facebook.react.bridge.BaseJavaModule;
import com.facebook.react.bridge.Promise;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;

/* JADX INFO: compiled from: ScreenshotModule.kt */
/* JADX INFO: loaded from: classes2.dex */
@Metadata(d1 = {"\u0000,\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0004\n\u0002\u0010\u000e\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u000b\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u000f\u0012\u0006\u0010\u0002\u001a\u00020\u0003¢\u0006\u0004\b\u0004\u0010\u0005J\b\u0010\u0007\u001a\u00020\bH\u0016J\u0010\u0009\u001a\u00020\n2\u0006\u0010\u000b\u001a\u00020\fH\u0007J\u0010\u000d\u001a\u00020\n2\u0006\u0010\u000e\u001a\u00020\u000fH\u0007R\u000e\u0010\u0006\u001a\u00020\u0003X\u0082\u0004¢\u0006\u0002\n\u0000¨\u0006\u0010"}, d2 = {"Lcom/cerebellummobileapp/ScreenshotModule;", "Lcom/facebook/react/bridge/ReactContextBaseJavaModule;", "reactContext", "Lcom/facebook/react/bridge/ReactApplicationContext;", "<init>", "(Lcom/facebook/react/bridge/ReactApplicationContext;)V", "context", "getName", "", "setSecureFlag", "", "secure", "", "isScreenMirrored", BaseJavaModule.METHOD_TYPE_PROMISE, "Lcom/facebook/react/bridge/Promise;", "app_release"}, k = 1, mv = {2, 1, 0}, xi = 48)
public final class ScreenshotModule extends ReactContextBaseJavaModule {
    private final ReactApplicationContext context;
    public ScreenshotModule(ReactApplicationContext reactContext) {
        super(reactContext);
        Intrinsics.checkNotNullParameter(reactContext, "reactContext");
        this.context = reactContext;
    }
    @Override public String getName() { return "Screenshot"; }
    @ReactMethod
    public final void setSecureFlag(final boolean secure) {
        final Activity currentActivity = getReactApplicationContext().getCurrentActivity();
        if (currentActivity != null) {
            currentActivity.runOnUiThread(new Runnable() {
                @Override public final void run() { ScreenshotModule.setSecureFlag$lambda$0(secure, currentActivity); }
            });
        }
    }
    private static final void setSecureFlag$lambda$0(boolean z, Activity activity) {
        if (z) activity.getWindow().setFlags(8192, 8192);
        else activity.getWindow().clearFlags(8192);
    }
    @ReactMethod
    public final void isScreenMirrored(Promise promise) {
        Intrinsics.checkNotNullParameter(promise, "promise");
        Object systemService = getReactApplicationContext().getSystemService("display");
        Intrinsics.checkNotNull(systemService, "null cannot be cast to non-null type android.hardware.display.DisplayManager");
        promise.resolve(Boolean.valueOf(((DisplayManager) systemService).getDisplays().length > 1));
    }
}
