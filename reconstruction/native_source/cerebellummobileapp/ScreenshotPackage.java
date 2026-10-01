package com.cerebellummobileapp;

import com.facebook.react.ReactPackage;
import com.facebook.react.bridge.NativeModule;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.uimanager.ViewManager;
import java.util.ArrayList;
import java.util.List;
import kotlin.collections.CollectionsKt;

public final class ScreenshotPackage implements ReactPackage {
    @Override public List<ViewManager<?, ?>> createViewManagers(ReactApplicationContext reactContext) { return CollectionsKt.emptyList(); }
    @Override public List<NativeModule> createNativeModules(ReactApplicationContext reactContext) {
        ArrayList arrayList = new ArrayList();
        arrayList.add(new ScreenshotModule(reactContext));
        return arrayList;
    }
}
