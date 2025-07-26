[app]

version = 1.0

# (str) Title of your application
title = Payments

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,kivyMD,pillow,pyjnius

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable AndroidX support.
android.enable_androidx = True

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = True

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) The format used to package the app for release mode (aab or apk or aar).
android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk
