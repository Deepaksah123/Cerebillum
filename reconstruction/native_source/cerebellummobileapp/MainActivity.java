package com.cerebellummobileapp;

import android.app.PendingIntent;
import android.app.PictureInPictureParams;
import android.app.RemoteAction;
import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.res.Configuration;
import android.graphics.drawable.Icon;
import android.os.Build;
import android.os.Bundle;
import android.util.Rational;
import com.facebook.react.ReactActivity;
import com.facebook.react.ReactActivityDelegate;
import com.facebook.react.defaults.DefaultNewArchitectureEntryPoint;
import com.facebook.react.defaults.DefaultReactActivityDelegate;
import java.util.ArrayList;
import kotlin.jvm.internal.Intrinsics;

public final class MainActivity extends ReactActivity {
    private BroadcastReceiver pipReceiver;
    @Override protected String getMainComponentName() { return "cerebellumMobileApp"; }
    @Override protected ReactActivityDelegate createReactActivityDelegate() {
        return new DefaultReactActivityDelegate(this, getMainComponentName(), DefaultNewArchitectureEntryPoint.getFabricEnabled());
    }
    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(null);
        this.pipReceiver = new PipActionReceiver();
        IntentFilter intentFilter = new IntentFilter("PIP_MEDIA_PLAY_PAUSE");
        if (Build.VERSION.SDK_INT >= 33) registerReceiver(this.pipReceiver, intentFilter, 2);
        else registerReceiver(this.pipReceiver, intentFilter);
    }
    @Override protected void onDestroy() {
        super.onDestroy();
        BroadcastReceiver broadcastReceiver = this.pipReceiver;
        if (broadcastReceiver != null) unregisterReceiver(broadcastReceiver);
    }
    public final void updatePictureInPictureActions(boolean isPlaying) {
        Intent intent = new Intent("PIP_MEDIA_PLAY_PAUSE");
        intent.setPackage(getPackageName());
        PendingIntent broadcast = PendingIntent.getBroadcast(this, 0, intent, 201326592);
        int i = isPlaying ? R.drawable.ic_pip_pause : R.drawable.ic_pip_play;
        String str = isPlaying ? "Pause" : "Play";
        Icon iconCreateWithResource = Icon.createWithResource(this, i);
        Intrinsics.checkNotNullExpressionValue(iconCreateWithResource, "createWithResource(...)");
        RemoteAction remoteAction = new RemoteAction(iconCreateWithResource, str, str, broadcast);
        ArrayList arrayList = new ArrayList();
        arrayList.add(remoteAction);
        setPictureInPictureParams(new PictureInPictureParams.Builder().setActions(arrayList).build());
    }
    @Override public void onUserLeaveHint() {
        super.onUserLeaveHint();
        if (PipHelperModule.INSTANCE.isVideoPlaying() && PipHelperModule.INSTANCE.isAppLevelPipEnabled()) {
            PictureInPictureParams.Builder aspectRatio = new PictureInPictureParams.Builder().setAspectRatio(new Rational(16, 9));
            if (PipHelperModule.INSTANCE.getRequiresCustomPipActions()) {
                Intent intent = new Intent("PIP_MEDIA_PLAY_PAUSE");
                intent.setPackage(getPackageName());
                PendingIntent broadcast = PendingIntent.getBroadcast(this, 0, intent, 201326592);
                Icon iconCreateWithResource = Icon.createWithResource(this, R.drawable.ic_pip_pause);
                Intrinsics.checkNotNullExpressionValue(iconCreateWithResource, "createWithResource(...)");
                RemoteAction remoteAction = new RemoteAction(iconCreateWithResource, "Pause", "Pause", broadcast);
                ArrayList arrayList = new ArrayList();
                arrayList.add(remoteAction);
                aspectRatio.setActions(arrayList);
            }
            enterPictureInPictureMode(aspectRatio.build());
        }
    }
    @Override public void onPictureInPictureModeChanged(boolean isInPictureInPictureMode, Configuration newConfig) {
        Intrinsics.checkNotNullParameter(newConfig, "newConfig");
        super.onPictureInPictureModeChanged(isInPictureInPictureMode, newConfig);
        PipHelperModule companion = PipHelperModule.INSTANCE.getInstance();
        if (companion != null) companion.sendPipModeChangedEvent(isInPictureInPictureMode);
    }
}