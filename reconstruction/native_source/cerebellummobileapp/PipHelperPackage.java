package com.cerebellummobileapp;

import com.facebook.react.ReactPackage;
import com.facebook.react.bridge.NativeModule;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.uimanager.ViewManager;
import java.util.List;
import kotlin.collections.CollectionsKt;

public final class PipHelperPackage implements ReactPackage {
    @Override public List<NativeModule> createNativeModules(ReactApplicationContext reactContext) {
        return CollectionsKt.listOf(new PipHelperModule(reactContext));
    }
    @Override public List<ViewManager<?, ?>> createViewManagers(ReactApplicationContext reactContext) {
        return CollectionsKt.emptyList();
    }
}
