package com.cerebellummobileapp;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;

public class MainActivity extends Activity {
    @Override protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView web = new WebView(this);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setAllowFileAccess(false);
        s.setAllowContentAccess(false);
        s.setAllowFileAccessFromFileURLs(false);
        s.setAllowUniversalAccessFromFileURLs(false);
        setContentView(web);
        try {
            String html = readUi();
            web.loadDataWithBaseURL(
                "https://appassets.androidplatform.net/assets/",
                html, "text/html", "UTF-8", null
            );
        } catch (Exception e) {
            web.loadDataWithBaseURL(null,
                "<html><body><h3>Cerebellum UI load error</h3><pre>"
                + escape(e.toString()) + "</pre></body></html>",
                "text/html", "UTF-8", null);
        }
    }

    private String readUi() throws Exception {
        String[] names = getAssets().list("");
        Arrays.sort(names);
        ByteArrayOutputStream out = new ByteArrayOutputStream();
        for (String name : names) {
            if (name.matches("\\d{2}\\.part")) {
                try (InputStream in = getAssets().open(name)) {
                    byte[] buf = new byte[8192];
                    int n;
                    while ((n = in.read(buf)) != -1) out.write(buf, 0, n);
                }
            }
        }
        return out.toString(StandardCharsets.UTF_8.name());
    }

    private static String escape(String s) {
        return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
    }
}