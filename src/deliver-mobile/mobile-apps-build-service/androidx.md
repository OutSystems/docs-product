---
summary: AndroidX replaces the old Android Support Library. In MABS 6, AndroidX is optional and this document shows how to activate the AndroidX support for native mobile apps.
tags: runtime-mobile
---

# Building apps with AndroidX

AndroidX is a new and much improved support library. The old Support Library is no longer maintained after Android 9.0 (API level 28). This document shows how to create native builds with AndroidX, which is optional in MABS 6.

<div class="info" markdown="1">

To build your apps and custom mobile plugins with AndroidX, you need to meet the following requirements:

* You're using MABS 6.3 Beta or later
* You enabled the AndroidX support library

</div>

When you enable AndroidX, MABS replaces the legacy dependencies from Support Library with the corresponding dependencies from the new AndroidX library. This migration is necessary because Support Libraries and AndroidX packages can't be in the same Android project.

Once you enable the AndroidX support, you should test your apps and make sure that all features are working as expected. Testing is particularly relevant for the features that depend on Support Library, such as custom Cordova plugins.

For more information about AndroidX migration check out [Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate) and [Migrating to AndroidX: tips, tricks, and guidance](https://medium.com/androiddevelopers/migrating-to-androidx-tip-tricks-and-guidance-88d5de238876) by Android Developers.

<div class="info" markdown="1">

The content in this document applies only to the native Android apps.

</div>

## How to enable AndroidX 

To build a mobile app with AndroidX enabled, do the following: 

1. Open your mobile app in Service Studio.
   
1. Open the **main module** of the app. You need to open the main module because MABS ignores the AndroidX setting in a dependency module.

1. Go to the mobile properties and edit the **Extensibility Configurations**. Add a new key-value pair in the android section, and set **AndroidXEnabled** to **true**. 

        {
            "preferences": {
                "android": [{
                    "name": "AndroidXEnabled",
                    "value": "true"
                }]
            }
        }

1. Publish the app in your environment. This lets MABS acquire updated resources.
   
1. Create native mobile builds of the app.