package com.cerebellummobileapp;

import android.app.Activity;
import android.content.res.ColorStateList;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.GradientDrawable;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewParent;
import android.widget.FrameLayout;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import androidx.constraintlayout.core.motion.utils.TypedValues;
import androidx.core.view.ViewCompat;
import com.facebook.appevents.internal.ViewHierarchyConstants;
import com.facebook.hermes.intl.Constants;
import com.facebook.react.bridge.Arguments;
import com.facebook.react.bridge.LifecycleEventListener;
import com.facebook.react.bridge.ReactApplicationContext;
import com.facebook.react.bridge.ReactContextBaseJavaModule;
import com.facebook.react.bridge.ReactMethod;
import com.facebook.react.bridge.ReadableMap;
import com.facebook.react.modules.core.DeviceEventManagerModule;
import com.facebook.react.uimanager.ViewProps;
import com.reactcommunity.rndatetimepicker.Common;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import kotlin.Metadata;
import kotlin.Result;
import kotlin.ResultKt;
import kotlin.Unit;
import kotlin.jvm.internal.Intrinsics;

/* JADX INFO: compiled from: FullscreenChipOverlayModule.kt */
/* JADX INFO: loaded from: classes2.dex */
@Metadata(d1 = {"\u0000R\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0003\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0003\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\b\n\u0002\b\u0005\n\u0002\u0010\u0006\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\b\u0012\u0018\u0000 52\u00020\u0001\u0002\u00020\u0002:\u00015B\u000f\u0012\u0006\u0010\u0003\u001a\u00020\u0004\u00a2\u0006\u0004\b\u0005\u0010\u0006J\b\u0010\f\u001a\u00020\nH\u0016J\u0010\u0010\r\u001a\u00020\u000e2\u0006\u0010\u000f\u001a\u00020\u0010H\u0007J\b\u0010\u0011\u001a\u00020\u000eH\u0007Jr\u0010\u0012\u001a\u00020\u000e2\u0006\u0010\u0013\u001a\u00020\u00142\u0006\u0010\u0015\u001a\u00020\n2\u0006\u0010\u0016\u001a\u00020\u00172\u0006\u0010\u0018\u001a\u00020\u00172\u0006\u0010\u0019\u001a\u00020\u00172\u0006\u0010\u001a\u001a\u00020\u00172\u0006\u0010\u001b\u001a\u00020\u00172\u0006\u0010\u001c\u001a\u00020\u001d2\u0006\u0010\u001e\u001a\u00020\u001d2\u0006\u0010\u001f\u001a\u00020\u001d2\u0006\u0010 \u001a\u00020\u001d2\u0006\u0010!\u001a\u00020\u001d2\b\u0010"\u001a\u0004\u0018\u00010\nH\u0002J\u0012\u0010#\u001a\u0004\u0018\u00010$2\u0006\u0010\u0013\u001a\u00020\u0014H\u0002J\u001a\u0010%\u001a\u0004\u0018\u00010\b2\u0006\u0010&\u001a\u00020\b2\u0006\u0010'\u001a\u00020\nH\u0002J\b\u0010(\u001a\u00020\u000eH\u0002J\u001a\u0010)\u001a\u00020\u00172\b\u0010*\u001a\u0004\u0018\u00010\n2\u0006\u0010+\u001a\u00020\u0017H\u0002J\u0010\u0010,\u001a\u00020\u000e2\u0006\u0010-\u001a\u00020\nH\u0002J\b\u0010.\u001a\u00020\u000eH\u0016J\b\u0010/\u001a\u00020\u000eH\u0016J\b\u00100\u001a\u00020\u000eH\u0016J\u0010\u00101\u001a\u00020\u000e2\u0006\u00102\u001a\u00020\nH\u0007J\u0010\u00103\u001a\u00020\u000e2\u0006\u00104\u001a\u00020\u0017H\u0007R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082\u0004\u00a2\u0006\u0002\n\u0000R\u0010\u0007\u001a\u0004\u0018\u00010\bX\u0082\u000e\u00a2\u0006\u0002\n\u0000R\u0010\t\u001a\u0004\u0018\u00010\nX\u0082\u000e\u00a2\u0006\u0002\n\u0000R\u0010\u000b\u001a\u0004\u0018\u00010\nX\u0082\u000e\u00a2\u0006\u0002\n\u0000\u00a8\u00066"}, d2 = {"Lcom/cerebellummobileapp/FullscreenChipOverlayModule;", "Lcom/facebook/react/bridge/ReactContextBaseJavaModule;", "Lcom/facebook/react/bridge/LifecycleEventListener;", "reactContext", "Lcom/facebook/react/bridge/ReactApplicationContext;", "<init>", "(Lcom/facebook/react/bridge/ReactApplicationContext;)V", "overlayView", "Landroid/view/View;", "lastShownMessage", "", "lastShownTarget", "getName", "show", "", "config", "Lcom/facebook/react/bridge/ReadableMap;", "hide", "addOrUpdateOverlay", "activity", "Landroid/app/Activity;", "message", "Landroidx/constraintlayout/core/motion/utils/TypedValues;", "backgroundColor", "", "secondaryTextColor", "accentColor", "fontSize", "", "chipMaxWidth", "labelMaxWidth", "closeIconSize", "closeTileSize", "target", "findExoPlayerOverlayFrameLayout", "Landroid/view/ViewGroup;", "findViewByClassName", "view", "simpleName", "removeOverlay", "parseColorOrDefault", "value", "default", "emitEvent", "name", "onHostResume", "onHostPause", "onHostDestroy", "addListener", "eventName", "removeListeners", "count", "Companion", "app_release"}, k = 1, mv = {2, 1, 0}, xi = 48)
public final class FullscreenChipOverlayModule extends ReactContextBaseJavaModule implements LifecycleEventListener {
    private static final int ACCENT_FALLBACK = -16481289;
    private static final double CLOSE_ICON_SIZE_FALLBACK = 18.0d;
    private static final double CLOSE_TILE_SIZE_FALLBACK = 26.0d;
    private static final double FONT_SIZE_FALLBACK = 13.0d;
    private static final double LABEL_MAX_WIDTH_FALLBACK = 176.0d;
    private static final double MAX_WIDTH_FALLBACK = 260.0d;
    private static final String TAG = "FullscreenChipOverlay";
    private static final String TARGET_PLAYER_OVERLAY = "playerOverlay";
    private String lastShownMessage;
    private String lastShownTarget;
    private View overlayView;
    private final ReactApplicationContext reactContext;

    private static final int addOrUpdateOverlay$dp(float f, double d) {
        return (int) (d * ((double) f));
    }

    @ReactMethod
    public final void addListener(String eventName) {
        Intrinsics.checkNotNullParameter(eventName, "eventName");
    }

    @Override
    public void onHostPause() {
    }

    @Override
    public void onHostResume() {
    }

    @ReactMethod
    public final void removeListeners(int count) {
    }

    public FullscreenChipOverlayModule(ReactApplicationContext reactContext) {
        super(reactContext);
        Intrinsics.checkNotNullParameter(reactContext, "reactContext");
        this.reactContext = reactContext;
        reactContext.addLifecycleEventListener(this);
    }

    @Override
    public String getName() {
        return "FullscreenChipOverlayModule";
    }

    @ReactMethod
    public final void show(ReadableMap config) {
        Intrinsics.checkNotNullParameter(config, "config");
        final Activity currentActivity = this.reactContext.getCurrentActivity();
        if (currentActivity == null) {
            Log.w(TAG, "show() called with no current activity");
            return;
        }
        String string = config.hasKey("message") ? config.getString("message") : null;
        String str = string;
        if (str == null || str.length() == 0) {
            Log.w(TAG, "show() called with empty message");
            return;
        }
        final int colorOrDefault = parseColorOrDefault(config.hasKey("backgroundColor") ? config.getString("backgroundColor") : null, -1);
        final int colorOrDefault2 = parseColorOrDefault(config.hasKey(Common.TEXT_COLOR) ? config.getString(Common.TEXT_COLOR) : null, ViewCompat.MEASURED_STATE_MASK);
        final int colorOrDefault3 = parseColorOrDefault(config.hasKey(ViewProps.BORDER_COLOR) ? config.getString(ViewProps.BORDER_COLOR) : null, -3355444);
        final int colorOrDefault4 = parseColorOrDefault(config.hasKey("secondaryTextColor") ? config.getString("secondaryTextColor") : null, colorOrDefault2);
        final int colorOrDefault5 = parseColorOrDefault(config.hasKey("accentColor") ? config.getString("accentColor") : null, ACCENT_FALLBACK);
        double d = config.hasKey("fontSize") ? config.getDouble("fontSize") : FONT_SIZE_FALLBACK;
        double d2 = config.hasKey(ViewProps.MAX_WIDTH) ? config.getDouble(ViewProps.MAX_WIDTH) : MAX_WIDTH_FALLBACK;
        double d3 = config.hasKey("labelMaxWidth") ? config.getDouble("labelMaxWidth") : LABEL_MAX_WIDTH_FALLBACK;
        double d4 = config.hasKey("closeIconSize") ? config.getDouble("closeIconSize") : CLOSE_ICON_SIZE_FALLBACK;
        final String str2 = string;
        final double d5 = config.hasKey("closeTileSize") ? config.getDouble("closeTileSize") : CLOSE_TILE_SIZE_FALLBACK;
        final String string2 = config.hasKey(TypedValues.AttributesType.S_TARGET) ? config.getString(TypedValues.AttributesType.S_TARGET) : null;
        final double d6 = d;
        final double d7 = d2;
        final double d8 = d3;
        final double d9 = d4;
        currentActivity.runOnUiThread(new Runnable() {
            @Override
            public final void run() {
                this.f$0.addOrUpdateOverlay(currentActivity, str2, colorOrDefault, colorOrDefault2, colorOrDefault3, colorOrDefault4, colorOrDefault5, d6, d7, d8, d9, d5, string2);
            }
        });
    }

    @ReactMethod
    public final void hide() {
        Activity currentActivity = this.reactContext.getCurrentActivity();
        if (currentActivity == null) {
            return;
        }
        currentActivity.runOnUiThread(new Runnable() {
            @Override
            public final void run() {
                this.f$0.removeOverlay();
            }
        });
    }

    private final void addOrUpdateOverlay(final Activity activity, String message, int backgroundColor, int textColor, int borderColor, int secondaryTextColor, int accentColor, double fontSize, double chipMaxWidth, double labelMaxWidth, double closeIconSize, double closeTileSize, String target) {
        ViewGroup viewGroupFindExoPlayerOverlayFrameLayout;
        View view = this.overlayView;
        if (view != null) {
            if ((view != null ? view.getParent() : null) != null && Intrinsics.areEqual(this.lastShownMessage, message) && Intrinsics.areEqual(this.lastShownTarget, target)) {
                return;
            }
        }
        removeOverlay();
        float f = activity.getResources().getDisplayMetrics().density;
        final int iAddOrUpdateOverlay$dp = addOrUpdateOverlay$dp(f, chipMaxWidth);
        LinearLayout r11 = new LinearLayout(activity) {
            final int chipMaxWidthPx = iAddOrUpdateOverlay$dp;
            @Override
            protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
                super.onMeasure(View.MeasureSpec.makeMeasureSpec(this.chipMaxWidthPx, Integer.MIN_VALUE), heightMeasureSpec);
            }
        };
        r11.setOrientation(0);
        r11.setGravity(16);
        r11.setPadding(addOrUpdateOverlay$dp(f, 8.0d), addOrUpdateOverlay$dp(f, 8.0d), addOrUpdateOverlay$dp(f, 8.0d), addOrUpdateOverlay$dp(f, 8.0d));
        GradientDrawable gradientDrawable = new GradientDrawable();
        gradientDrawable.setCornerRadius(addOrUpdateOverlay$dp(f, 999.0d));
        gradientDrawable.setColor(backgroundColor);
        gradientDrawable.setStroke(1, borderColor);
        r11.setBackground(gradientDrawable);
        r11.setElevation(addOrUpdateOverlay$dp(f, 6.0d));
        r11.setClickable(true);
        r11.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view2) {
                FullscreenChipOverlayModule.this.emitEvent("FullscreenChipOverlayPress");
            }
        });
        FrameLayout frameLayout = new FrameLayout(activity);
        GradientDrawable gradientDrawable2 = new GradientDrawable();
        gradientDrawable2.setShape(1);
        gradientDrawable2.setColor(accentColor);
        frameLayout.setBackground(gradientDrawable2);
        ImageView imageView = new ImageView(activity);
        imageView.setImageResource(R.drawable.ic_watch_paused);
        FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(addOrUpdateOverlay$dp(f, 14.0d), addOrUpdateOverlay$dp(f, 14.0d));
        layoutParams.gravity = 17;
        frameLayout.addView(imageView, layoutParams);
        TextView textView = new TextView(activity);
        textView.setText(message);
        textView.setTextColor(textColor);
        textView.setTextSize(1, (float) fontSize);
        textView.setMaxWidth(addOrUpdateOverlay$dp(f, labelMaxWidth));
        textView.setIncludeFontPadding(false);
        try {
            textView.setTypeface(Typeface.createFromAsset(activity.getAssets(), "fonts/Inter-Medium.ttf"));
        } catch (Throwable th) {
        }
        FrameLayout frameLayout2 = new FrameLayout(activity);
        frameLayout2.setClickable(true);
        frameLayout2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view2) {
                FullscreenChipOverlayModule.this.emitEvent("FullscreenChipOverlayDismiss");
            }
        });
        ImageView imageView2 = new ImageView(activity);
        imageView2.setImageResource(R.drawable.ic_chip_close);
        imageView2.setImageTintList(ColorStateList.valueOf(secondaryTextColor));
        FrameLayout.LayoutParams layoutParams2 = new FrameLayout.LayoutParams(addOrUpdateOverlay$dp(f, closeIconSize), addOrUpdateOverlay$dp(f, closeIconSize));
        layoutParams2.gravity = 17;
        frameLayout2.addView(imageView2, layoutParams2);
        r11.addView(frameLayout, new LinearLayout.LayoutParams(addOrUpdateOverlay$dp(f, CLOSE_TILE_SIZE_FALLBACK), addOrUpdateOverlay$dp(f, CLOSE_TILE_SIZE_FALLBACK)));
        LinearLayout.LayoutParams layoutParams3 = new LinearLayout.LayoutParams(-2, -2);
        layoutParams3.setMarginStart(addOrUpdateOverlay$dp(f, 8.0d));
        r11.addView(textView, layoutParams3);
        LinearLayout.LayoutParams layoutParams4 = new LinearLayout.LayoutParams(addOrUpdateOverlay$dp(f, closeTileSize), addOrUpdateOverlay$dp(f, closeTileSize));
        layoutParams4.setMarginStart(addOrUpdateOverlay$dp(f, 8.0d));
        r11.addView(frameLayout2, layoutParams4);
        if (Intrinsics.areEqual(target, TARGET_PLAYER_OVERLAY)) {
            viewGroupFindExoPlayerOverlayFrameLayout = findExoPlayerOverlayFrameLayout(activity);
        } else {
            View decorView = activity.getWindow().getDecorView();
            viewGroupFindExoPlayerOverlayFrameLayout = decorView instanceof ViewGroup ? (ViewGroup) decorView : null;
        }
        if (viewGroupFindExoPlayerOverlayFrameLayout == null) {
            Log.w(TAG, "no host view for target=" + target + "; cannot attach overlay");
            return;
        }
        FrameLayout.LayoutParams layoutParams5 = new FrameLayout.LayoutParams(-2, -2);
        layoutParams5.gravity = 49;
        layoutParams5.topMargin = addOrUpdateOverlay$dp(f, 12.0d);
        layoutParams5.setMarginStart(addOrUpdateOverlay$dp(f, 16.0d));
        layoutParams5.setMarginEnd(addOrUpdateOverlay$dp(f, 16.0d));
        View view2 = r11;
        viewGroupFindExoPlayerOverlayFrameLayout.addView(view2, layoutParams5);
        r11.bringToFront();
        viewGroupFindExoPlayerOverlayFrameLayout.requestLayout();
        this.overlayView = view2;
        this.lastShownMessage = message;
        this.lastShownTarget = target;
    }

    private final ViewGroup findExoPlayerOverlayFrameLayout(Activity activity) {
        Object objM2816constructorimpl;
        Class<?> cls;
        Method method;
        Class<?> cls2;
        Method method2;
        View decorView = activity.getWindow().getDecorView();
        ViewGroup viewGroup = decorView instanceof ViewGroup ? (ViewGroup) decorView : null;
        if (viewGroup == null) {
            return null;
        }
        View viewFindViewByClassName = findViewByClassName(viewGroup, "ReactExoplayerView");
        if (viewFindViewByClassName == null) {
            Log.w(TAG, "ReactExoplayerView not found in view tree");
            return null;
        }
        try {
            FullscreenChipOverlayModule fullscreenChipOverlayModule = this;
            Field declaredField = viewFindViewByClassName.getClass().getDeclaredField("exoPlayerView");
            declaredField.setAccessible(true);
            Object obj = declaredField.get(viewFindViewByClassName);
            Object objInvoke = (obj == null || (cls2 = obj.getClass()) == null || (method2 = cls2.getMethod("getPlayerView", new Class[0])) == null) ? null : method2.invoke(obj, new Object[0]);
            Object objInvoke2 = (objInvoke == null || (cls = objInvoke.getClass()) == null || (method = cls.getMethod("getOverlayFrameLayout", new Class[0])) == null) ? null : method.invoke(objInvoke, new Object[0]);
            objM2816constructorimpl = objInvoke2 instanceof ViewGroup ? (ViewGroup) objInvoke2 : null;
        } catch (Throwable th) {
            objM2816constructorimpl = null;
        }
        return (ViewGroup) objM2816constructorimpl;
    }

    private final View findViewByClassName(View view, String simpleName) {
        if (Intrinsics.areEqual(view.getClass().getSimpleName(), simpleName)) {
            return view;
        }
        if (!(view instanceof ViewGroup)) {
            return null;
        }
        ViewGroup viewGroup = (ViewGroup) view;
        int childCount = viewGroup.getChildCount();
        for (int i = 0; i < childCount; i++) {
            View childAt = viewGroup.getChildAt(i);
            Intrinsics.checkNotNullExpressionValue(childAt, "getChildAt(...)");
            View viewFindViewByClassName = findViewByClassName(childAt, simpleName);
            if (viewFindViewByClassName != null) {
                return viewFindViewByClassName;
            }
        }
        return null;
    }

    private final void removeOverlay() {
        View view = this.overlayView;
        if (view != null) {
            ViewParent parent = view.getParent();
            ViewGroup viewGroup = parent instanceof ViewGroup ? (ViewGroup) parent : null;
            if (viewGroup != null) {
                viewGroup.removeView(view);
            }
        }
        this.overlayView = null;
        this.lastShownMessage = null;
        this.lastShownTarget = null;
    }

    private final int parseColorOrDefault(String value, int i) {
        String str = value;
        if (str != null && str.length() != 0) {
            try {
                return Color.parseColor(value);
            } catch (IllegalArgumentException unused) {
            }
        }
        return i;
    }

    private final void emitEvent(String name) {
        ((DeviceEventManagerModule.RCTDeviceEventEmitter) this.reactContext.getJSModule(DeviceEventManagerModule.RCTDeviceEventEmitter.class)).emit(name, Arguments.createMap());
    }

    @Override
    public void onHostDestroy() {
        removeOverlay();
    }
}
