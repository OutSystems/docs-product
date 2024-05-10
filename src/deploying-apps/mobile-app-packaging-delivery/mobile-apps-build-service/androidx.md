---
summary: Explore building mobile apps with AndroidX in OutSystems 11 (O11) using MABS 6.3 to MABS 9.
tags: runtime-mobile
locale: en-us
guid: 1544fe43-3dbd-427e-bfd2-69ab0594f2e2
app_type: mobile apps
platform-version: o11
figma:
---

# Building apps with AndroidX

<div class="info" markdown="1">

Applies only to Mobile Apps using MABS 6.3 to MABS 9.

</div>

AndroidX is an improved Android support library. The Android developers no longer maintain Support Library after Android 9.0 (API level 28). This document shows how to create native builds with AndroidX.

<div class="info" markdown="1">

To build your apps and custom mobile plugins with AndroidX, you need to be using MABS 6.3 Beta or later. MABS releases after 6.3 Beta have AndroidX enabled by default. 

</div>

With AndroidX support, MABS replaces the legacy dependencies from Support Library with the corresponding dependencies from the new AndroidX library. This migration is necessary because Support Libraries and AndroidX packages can't be in the same Android project.

You should test your apps and make sure that all features are working as expected. Testing is particularly relevant for the features that depend on Support Library, such as custom Cordova plugins.

For more information about AndroidX migration check out [Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate) and [Migrating to AndroidX: tips, tricks, and guidance](https://medium.com/androiddevelopers/migrating-to-androidx-tip-tricks-and-guidance-88d5de238876) by Android Developers.

<div class="info" markdown="1">

The content in this document applies only to the native Android apps.

</div>

## How to enable AndroidX 

<div class="warning" markdown="1">

The `AndroidXEnabled` preference no longer has any effect starting with MABS 10. For more details, please check the **[release notes](https://success.outsystems.com/support/release_notes/mobile_apps_build_service_versions/mabs_10_release_notes/#breaking-changes)**.

</div>

<div class="info" markdown="1">

You need to enable AndroidX if you're using MABS 6.3 Beta. AndroidX is **enabled by default in MABS 7 Beta**.  

</div>

To build a mobile app with AndroidX enabled, do the following: 

1. Open your mobile app in Service Studio.
   
1. Open the **main module** of the app. You need to open the main module because MABS ignores the AndroidX setting in a dependency module.

1. Go to the mobile properties and edit the **Extensibility Configurations**. Add a new key-value pair in the Android section, and set **AndroidXEnabled** to **true**. 

        {
            "preferences": {
                "android": [{
                    "name": "AndroidXEnabled",
                    "value": "true"
                }]
            }
        }

1. Publish the app in your environment so MABS can acquire the updated resources.
   
1. Create native mobile builds of the app.
