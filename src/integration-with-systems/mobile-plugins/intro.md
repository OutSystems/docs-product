---
summary: Extend the functionalities of your mobile apps by using plugins.
tags: article-page; runtime-mobile; support-application_development; support-Mobile_Apps; support-Mobile_Apps-featured
locale: en-us
guid: 5543e1d8-095e-45d1-aef6-d3c054649421
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=410:31
---

# Mobile Plugins

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Plugins provide important functionalities to native mobile apps, letting you use many of the hardware capabilities of mobile devices. You can add notifications, use camera or global positioning services, read QR codes, and more.

## The list of supported mobile plugins

The table shows the OutSystems-supported mobile plugins that you can find in the Forge repository. Some of them are already supported when distributing your app as a Progressive Web App (PWA).

You may also create mobile plugins by [wrapping an Apache Cordova plugin into a module](./cordova-plugin/intro.md).

Plugin | Description | Supported in PWA
-------|-------------|---
[Analytics](https://www.outsystems.com/forge/component-overview/10704/firebase-analytics-plugin) | Firebase-based plugin that lets you gather information about app use. | No
[AppShield](<https://www.outsystems.com/forge/component-overview/9379//>) | Protect your mobile apps from tampering. OutSystems AppShield hardens the native mobile build, enabling the app to detect attempts of modification and misuse. | No
[Calendar](<https://www.outsystems.com/forge/component/1566/calendar-plugin/>) | Access the calendar of your device. | No
[Camera](<https://www.outsystems.com/forge/component-overview/1390/camera-plugin>) | Enable your application to access the camera capabilities of the device. | Yes
[Card IO](<https://www.outsystems.com/forge/component/1438/card-io-plugin/>) | Automatically get the details of a credit card by taking a picture. | No
[Ciphered Local Storage](<https://www.outsystems.com/forge/component-details/1500/ciphered-local-storage-plugin/>) | Keep your mobile application's sensitive data safe using a ciphered local storage database. | No
[Contacts](<https://www.outsystems.com/forge/component-overview/1394/contacts-plugin>) | Access the contacts of your device. | No
[Crash Reporting](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10705) | Firebase-based plugin that provides realtime crash reporting to help you track, prioritize, and fix stability issues.  | No
[Dynamic Links](https://www.outsystems.com/forge/component-overview/10988/dynamic-links-plugin-firebase) | Firebase-based plugin that lets you manage links outside of your app. | No
[File Transfer](<https://www.outsystems.com/forge/component-overview/1409/file-transfer-plugin>) | Lets users upload and download files in the background. | Yes
[File Viewer](<https://www.outsystems.com/forge/component-overview/1606/file-viewer-plugin>) | Lets users view remote or app resource files. | Yes
[File](<https://www.outsystems.com/forge/component-overview/1633/file-plugin>) | Lets you manage files and folders on a mobile device within the app sandbox. | No
[Cloud Messaging Plugin (Firebase)](https://www.outsystems.com/forge/component-overview/12174/cloud-messaging-plugin-firebase) |  Give your app users a state-of-the-art notifications experience. | No
[Health & Fitness](<https://www.outsystems.com/forge/component-overview/11715/health-fitness-plugin>) | Provides access to health and fitness data. Uses HealthKit API for iOS and Google Fit API for Android. | No
[InApp Browser](<https://www.outsystems.com/forge/component/1558/inappbrowser-plugin/>) | Open external URLs directly in your application. | No
[Key Store](<https://www.outsystems.com/forge/component/1550/Key+Store+Plugin/>) | Store small amounts of sensitive information on your device. Key Store secures data by encrypting the data before storing it, and the platform itself carefully controls access to stored items. | No
[Local Notifications](<http://www.outsystems.com/forge/component/1541/local-notifications-plugin/>) | Send app notifications to the device when the application isn't running in the foreground. | No
[Location](<https://www.outsystems.com/forge/component/1395/location-plugin/>) | Access the GPS capabilities of the user's device to show, for example, the present latitude, longitude, and  altitude. | Yes
[OneSignal Notifications](<http://www.outsystems.com/forge/component/2119/onesignal-plugin/>) | Push notifications using OneSignal, with deep-linking and actions. | No
[Payments](https://www.outsystems.com/forge/component-overview/13678/payments-plugin) | Allows addition of payments experience using Apple Pay and Google Pay | No
[Performance Monitoring](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10706) | Firebase-based plugin that lets you understand how you can improve the performance of your app.  | No
[QR/Barcode scanner](<https://www.outsystems.com/forge/component/1403/barcode-plugin/>) | Scan barcodes and QR codes. | Yes
[Social Login Mobile](<https://www.outsystems.com/forge/component-overview/7895/social-login-mobile>) | Lets you set a login experience that resorts to an external provider, namely Google, Apple, Facebook, or LinkedIn. | Yes
[SSL Pinning](<https://www.outsystems.com/forge/component-overview/1873/ssl-pinning-plugin>) | Provide an extra layer of security to HTTPS communications by adding a verification of the server certificate against hashes of public keys. | No
[Touch ID](<https://www.outsystems.com/forge/component-details/1431/Touch+ID+Plugin/>) | Use authentication with Touch ID in your application. | No

### Notes

When working with the plugins:

* Use the plugin that supports iOS or Android, depending on your target platform. The app generation fails if you use a plugin that isn't supported on the target platform. For more information on app generation errors check our [list of MABS errors](<https://success.outsystems.com/support/errors/mabs_errors/>).
* Each time you add, remove, or modify the plugin in an app, OutSystems [rebuilds the native shell](<../../deploying-apps/mobile-app-packaging-delivery/mobile-app-update-scenarios.md#Situations_When_the_User_Must_Install_a_New_Build>) which you then have to distribute to the end users for installation.
* [Include the plugin license](<../../deploying-apps/mobile-app-packaging-delivery/compliance-with-third-party-licenses.md#Include_the_Third_Party_Licenses_Used_by_Plug-ins_or_Components>) in your app to respect the license agreements of that plugin. These license agreements are usually placed in the About page of the app that uses them.

## Adding plugins

The plugins are available from the Forge repository. To use a plugin in your app, you need to [install the plugin](#installing-a-plugin) and [add the plugin elements to your module](#referencing-a-plugin).

### Installing a plugin

To install a supported plugin from Forge:

1. Find the plugin you want to use in the [list of supported mobile plugins](#the-list-of-supported-mobile-plugins).

1. Click the plugin name in the column **Plugin**. The Forge page opens.

1. In the Forge plugin page, click **INSTALL** and follow the instructions to install the plugin and optionally the demo app that comes with the plugin.

    ![Screenshot showing the INSTALL button on a Forge plugin page](images/forge-install.png "Forge Plugin Installation")

1. Once the installation finishes, [reference the plugin in your module](#referencing-a-plugin).

<div class="info" markdown="1">

Find the plugin documentation in the table of content next to this page, or check out the **Documentation** tab in the plugin Forge page.

</div>

### Referencing a plugin

Referencing an [installed plugin](#installing-a-plugin) lets you use the plugin functionalities in the app logic. Follow these steps to reference a mobile plugin:

1. In Service Studio, open **Manage Dependencies** (**Ctrl+Q**).

1. Enter the plugin name in the **Search producers** field. If the plugin name is **Camera Plugin**, try searching for `CameraPlugin`.

1. In the results, in the producers list, select the plugin.

1. In the plugin elements, in the public elements list, select the elements you want to use in your app. If you're unsure which elements to select, select all by selecting the plugin handle at the top of the list.

    ![Screenshot of the Manage Dependencies window in OutSystems Service Studio with plugin elements selected](images/manage-dependencies-plugin-ss.png "Service Studio Manage Dependencies")

1. Click **Apply** to confirm adding the plugin to the app.

1. Verify Service Studio added the plugin elements. Most plugins have logic in **Logic** > **Client Actions** > **plugin handle**. Some plugins come with user interface elements that you can find in **Interface** > **UI Flows** > **plugin handle**.

## Built-in plugins

All mobile apps generated by OutSystems include a native shell with the following built-in plugins that are used internally, handling a variety of housekeeping and infrastructure tasks.

Plugin | Description
-------|-----------------
OS Auth           | Handles OAuth flows and ensures compliance with the guidelines for SSO using the right WebView instances types for Android and iOS.
OS Cache       | Lets your application to run offline or with bad network conditions.
OS Cordova Loader | Loads the Cordova engine on your app.
OS Deeplinks   | Opens hyperlinks to specific screens of your app.
OS DB Upgrader | Manages the local storage of your app.
OS Manifest    | Provides a parser for the app manifest.
OS Pre-Bundle  | Handles the content of the app pre-bundled resources.
OS Security    | Provides the APIs for the security layer.
Mobile AppFeedback | Enables the user to invoke App Feedback for submitting feedback about the app.
NetworkStatus  | Lets your app know when the device is online/offline and informs of the type of network available (for example, WiFi, 3G, 4G).

While you may see the names of these built-in plugins in the [native mobile shell logs](<../../monitor-and-troubleshoot/monitoring-an-environment.md>) they're not user-configurable. The only exception is [Mobile AppFeedback](<../../monitor-and-troubleshoot/app-feedback/user-feedback-enable.md>), which is present in the native shell if you enable the App Feedback feature.
