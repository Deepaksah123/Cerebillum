package com.cerebellummobileapp;

import android.app.Activity;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import com.facebook.appevents.internal.ViewHierarchyConstants;
import com.facebook.react.bridge.Arguments;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import com.facebook.react.bridge.WritableMap;
import com.facebook.react.modules.core.DeviceEventManagerModule;
import com.facebook.react.uimanager.ViewProps;
import kotlin.Metadata;
import kotlin.Unit;
import kotlin.jvm.internal.DefaultConstructorMarker;
import kotlin.jvm.internal.Intrinsics;

public final class PipHelperModule extends ReactContextBaseJavaModule {
    public static final Companion INSTANCE = new Companion(null);
    private static PipHelperModule instance;
    private static boolean isAppLevelPipEnabled;
    private static boolean isVideoPlaying;
    private static boolean requiresCustomPipActions;
    private final ReactApplicationContext reactContext;
    @ReactMethod public final void addListener(String eventName) { Intrinsics.checkNotNullParameter(eventName, "eventName"); }
    @ReactMethod public final void removeListeners(int count) {}
    public PipHelperModule(ReactApplicationContext reactContext) { super(reactContext); Intrinsics.checkNotNullParameter(reactContext, "reactContext"); this.reactContext = reactContext; instance = this; }
    public static final class Companion {
        public /* synthetic */ Companion(DefaultConstructorMarker m) { this(); }
        private Companion() {}
        public final boolean isVideoPlaying() { return PipHelperModule.isVideoPlaying; }
        public final void setVideoPlaying(boolean z) { PipHelperModule.isVideoPlaying = z; }
        public final boolean getRequiresCustomPipActions() { return PipHelperModule.requiresCustomPipActions; }
        public final void setRequiresCustomPipActions(boolean z) { PipHelperModule.requiresCustomPipActions = z; }
        public final boolean isAppLevelPipEnabled() { return PipHelperModule.isAppLevelPipEnabled; }
        public final void setAppLevelPipEnabled(boolean z) { PipHelperModule.isAppLevelPipEnabled = z; }
        public final PipHelperModule getInstance() { return PipHelperModule.instance; }
    }
    @Override public String getName() { return "PipHelperModule"; }
    @ReactMethod public final void setVideoPlaying(boolean isPlaying) { isVideoPlaying = isPlaying; requiresCustomPipActions = false; }
    @ReactMethod public final void setVideoPlayingWithCustomActions(boolean isPlaying, boolean requiresCustomActions) {
        isVideoPlaying = isPlaying; requiresCustomPipActions = requiresCustomActions;
        Activity currentActivity = this.reactContext.getCurrentActivity();
        if (currentActivity instanceof MainActivity) ((MainActivity) currentActivity).updatePictureInPictureActions(isPlaying);
    }
    @ReactMethod public final void setAppLevelPipEnabled(boolean enabled) { isAppLevelPipEnabled = enabled; }
    private final void traverseAndPauseVdoPlayer(View view, boolean playWhenReady) {
        String simpleName = view.getClass().getSimpleName();
        if (Intrinsics.areEqual(simpleName, "ReactVdoPlayerUIView") || Intrinsics.areEqual(simpleName, "ReactVdoPlayerView") || Intrinsics.areEqual(simpleName, "ReactVideoView")) {
            try {
                try { view.getClass().getMethod("setPlayWhenReady", Boolean.TYPE).invoke(view, Boolean.valueOf(playWhenReady)); return; }
                catch (Exception unused) { view.getClass().getMethod("setPausedModifier", Boolean.TYPE).invoke(view, Boolean.valueOf(!playWhenReady)); return; }
            } catch (Exception unused2) { Unit unit = Unit.INSTANCE; return; }
        }
        if (view instanceof ViewGroup) {
            ViewGroup viewGroup = (ViewGroup) view; int childCount = viewGroup.getChildCount();
            for (int i=0;i<childCount;i++) { View childAt=viewGroup.getChildAt(i); Intrinsics.checkNotNullExpressionValue(childAt,"getChildAt(...)"); traverseAndPauseVdoPlayer(childAt,playWhenReady); }
        }
    }
    public final void handlePipPlayPauseAction() {
        Window window; View decorView; View rootView; boolean z=!isVideoPlaying;
        Activity currentActivity=this.reactContext.getCurrentActivity();
        if (currentActivity instanceof MainActivity) ((MainActivity)currentActivity).updatePictureInPictureActions(z);
        if (currentActivity!=null && (window=currentActivity.getWindow())!=null && (decorView=window.getDecorView())!=null && (rootView=decorView.getRootView())!=null) traverseAndPauseVdoPlayer(rootView,z);
        isVideoPlaying=z; sendPipPlayPauseEvent(z);
    }
    public final void sendPipModeChangedEvent(boolean isInPip) {
        WritableMap m=Arguments.createMap(); m.putBoolean("isInPip",isInPip);
        ((DeviceEventManagerModule.RCTDeviceEventEmitter)this.reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)).emit("PipModeChanged",m);
    }
    public final void sendPipPlayPauseEvent(boolean isPlaying) {
        WritableMap m=Arguments.createMap(); m.putBoolean("isPlaying",isPlaying);
        ((DeviceEventManagerModule.RCTDeviceEventEmitter)this.reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)).emit("PipPlayPause",m);
    }
}
