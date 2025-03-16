---
summary: Learn how OutSystems 11 (O11) supports mobile app packaging and delivery through native builds and progressive web app (PWA) distribution.
tags: mobile app distribution, native mobile builds, progressive web apps, ios deployment, android deployment
locale: en-us
guid: b6da547f-4ef6-4bd3-bffc-365d5630da64
app_type: mobile apps
platform-version: o11
figma:
audience:
  - mobile developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
topic:
  - app-distribution
---

# Mobile apps packaging and delivery

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Once your mobile app has reached a stable state, you should distribute it to your users.  
  
In OutSystems, there are two ways to distribute a mobile app:

* Generate a **mobile application package** (IPA and AAB/APK) for a target mobile operating system (iOS and Android). An OutSystems cloud service generates the packages for you, so you don't need the SDKs, only the configuration for the apps. Check the iOS and Android documentation to learn more about native builds and distribution to the Apple App Store and Google Play. 

* Activate the **progressive web app (PWA) distribution**. PWA is a lightweight distribution option for mobile apps, as it doesn't depend on the app stores and uses modern browser capabilities.
