---
summary: Generate a mobile app package for a mobile app and distribute it. Generate builds for tests purposes, to distribute to a selected group of end users, or to publish in mobile app stores.
tags:
locale: en-us
guid: 1aacc771-f914-4f95-889a-31f1dde06a38
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=307:232
---

# Generate and distribute your mobile app

<div class="info" markdown="1">

Applies only to mobile apps.

</div>

Before generating your mobile app for the first time, you have to configure specific iOS and/or Android settings. Check first the details about different scenarios, such as [development tests](development-tests.md), distributing your app to a [limited group of end users](limited-group-end-users.md), or publishing your app in [Mobile App Stores](publish-app-stores.md).

<div class="info" markdown="1">

To generate Android App Bundle you need to use the following:

*  Platform Server version 11.12.0 or later
*  MABS 7 or later
*  Up-to-date Service Studio

</div>

The following sections show how to configure and generate iOS and Android app packages of your mobile apps in Service Studio or in Service Center. For additional information about generating and distributing iOS and Android app packages, see [More information on generating and distributing mobile apps](more-information.md).

<div class="warning" markdown="1">

Don't tamper with the iOS or Android mobile builds once the platform generates them. For example, don't use a third-party tool to add new functionality like performance monitoring. If you modify a mobile build, you're risking having an app that doesn't run correctly and that fails to pass integrity checks. 

</div>

## Configure and generate a mobile app package in Service Studio { #config-generate-service-studio }

To configure or generate your mobile app package (iOS or Android) in Service Studio, do the following:

1. Navigate to the app detail screen of your mobile app. 

1. Select the **Distribute** tab. The native mobile settings are in the **Native Platforms** section.

1. When configuring your mobile app for the first time for a given platform (iOS or Android), click the **Generate Android app** or **Generate iOS app** button, according to the platform. Follow the configuration steps for your desired scenario: distribute for [development tests](development-tests.md), distributing your app to a [limited group of end users](limited-group-end-users.md), or publishing your app in [Mobile App Stores](publish-app-stores.md). If you have previously defined your mobile app's iOS or Android configuration settings, click on the cog icon for the correct platform to change your configuration. 

1. After defining or changing your mobile app iOS or Android settings, click **Generate Android app** or **Generate iOS app**. 

    ![Screenshot of the native mobile settings tab in Service Studio for configuring mobile app packages](images/native-platforms-tab-ss.png "Native app settings in Service Studio")

## Configure and generate a mobile app package in Service Center { #config-generate-service-center }

To configure or generate your mobile app package (iOS or Android) in Service Center, do the following:

1. Open the Service Center console of the environment (`https://<environmentdomain>/ServiceCenter`) and navigate to **Factory**.

1. Click the **Applications** tab, open your mobile app from the app list, then select the **Distribute** tab. The native mobile settings are in the **Native Platforms** section.

    ![Screenshot showing the native mobile settings section in Service Center for mobile app distribution](images/native-platform-section-sc.png "Native app settings in Service Center")

1. To configure your mobile app package for the first time or to change the current configuration for a given platform (iOS or Android), click the **Configure** link for the iOS or Android entry.

    ![Screenshot of the Android configuration options in Service Center for mobile app packages](images/configure-android-settings-sc.png "Android settings in Service Center")

1. After defining or changing your mobile app iOS or Android settings, click **Save**.

1. At the end of the configuration settings page, select the MABS version you wish to use for generating the mobile app package for the mobile platform you're configuring (iOS or Android) in the current environment.  

    <div class="info" markdown="1">

    For more information about MABS check [Choosing the MABS Version to Build Your Mobile Packages](#choose-mabs-version)

    </div>

1. Click **Save and Generate** and wait a few moments while OutSystems generates your mobile app package.

Now that you have configured the app, the next time you need to generate a new mobile app package, just click the **Generate** button.

### Customizing the mobile app domain name { #customizing-the-mobile-app-domain-name }

For some cases, you might need to change the domain name associated with your mobile app, like when you have internal security policies dictating that different mobile apps should have different associated domain names and SSL certificates.

You can customize the domain name for each mobile app in Service Center. By default, OutSystems uses the hostname set for the environment in Administration > Environment Configuration.

**Note:** The domain name set for your mobile app should match the Common Name (CN) or a Subject Alternative Name (SAN) specified in the SSL certificate you have configured in your web server for serving HTTPS requests.

To define a different domain name for your mobile app, do the following:

1. In the **Distribute** tab, under the section **Native Platforms**, click the **Change** link in the **Domain Name** column.

    ![Screenshot depicting the process of changing the hostname for mobile apps in Service Center](images/change-hostname-sc.png "Hostname settings for mobile apps")

1. Enter the new domain name for the mobile app and click **Apply**. 

1. **Regenerate the mobile app** for the changes to take effect.

### Customizing the mobile app version code { #customizing-the-mobile-app-version-code }

The mobile app version code is an internal number associated with the generation of the mobile app package. App stores use this number to determine whether one version is more recent than another. See more detailed information in [Android](https://developer.android.com/studio/publish/versioning) and [iOS](https://help.apple.com/app-store-connect/#/dev82a6a9d79) documentation.

By default, OutSystems **increments the version code by one** every time the MABS generates the mobile app package.

For some cases, you might need to change the default mobile app version code. For example, if you are migrating an existing mobile app from another technology provider to OutSystems, the current version code of your app in the app store is higher than the first OutSystems app version code. In this case, you can set the version code of your OutSystems mobile app to a different value.

To set a different version code for your mobile app, do the following:

1. In the **Distribute** tab, under the section **Native Platforms**, click the **Change** link in the **Code** column for the iOS or Android entry.

    ![Screenshot showing where to change the app version code for mobile apps in Service Center](images/change-versioncode-sc.png "App code version settings for mobile apps")

1. Enter the new code for the mobile app and click **Apply**.

The next time you generate a new app package, the version code increments by one.

### Choosing the MABS version to build your mobile packages { #choose-mabs-version }

The [Mobile Apps Build Service (MABS)](../mobile-apps-build-service/intro.md) is a **cloud service** used by OutSystems to generate the mobile packages of your mobile apps developed in OutSystems for iOS and Android. 

MABS is continuously improved and OutSystems regularly makes available new versions of this cloud service. However, you might not want to use the latest version, since different MABS versions support different mobile stacks and therefore different ranges of devices and mobile platform versions.

You can select the MABS version used to generate the mobile packages **by mobile app** and **by mobile platform** (iOS and Android), for a given environment. You can do this in Service Center at the app level.

To choose a MABS version do the following:

1. In Service Center, click the **Applications** tab, open your mobile app from the app list and select the **Distribute** tab. The native mobile settings are in the **Native Platforms** section.

1. In the **Settings** column, click the **Configure** link for the iOS or Android entry.

    ![Screenshot of the mobile app settings screen with options to configure MABS version in Service Center](images/open-mabs-version-selection-sc.png "Mobile app settings screen")

1. At the end of the configuration settings page, select the MABS version you wish to use for generating the mobile app package for the mobile platform you're configuring (iOS or Android) in the current environment, either the latest available version or a specific version (see below for details).

    ![Screenshot of the MABS version selection options in Service Center for mobile app package generation](images/select-mabs-version-sc.png "Mobile Apps Build Service (MABS) version selection")

    **Note:** The MABS version selection is only available for apps whose native platform settings are already configured.

1. Click **Save and Generate** and wait a few moments while OutSystems generates your mobile app package.

When choosing a MABS version you have the following options available:

* **Always use the latest version available**: Always use the most recent MABS version available to generate the mobile package of the app for the current platform and in the current environment.

* **Specific version _(select from list)_**: Generate mobile app packages (in the current environment) with the MABS version selected from the list.

Whether you selected the option of using the latest MABS version or using a specific MABS version for the app package generation, when you generate and tag a mobile app version, OutSystems records the MABS version used to generate the mobile package.

**To fully understand the impacts of this setting, be sure to check [Understanding MABS Versions](../mobile-apps-build-service/intro.md#understanding-mabs-versions).**

## Download mobile app build logs { #download-mobile-app-build-logs }

You can obtain the build logs of your mobile apps in Service Center. Build logs are available for both successful and unsuccessful builds, and each platform (Android and iOS) has its own build log.

To obtain a mobile app build log:

1. Access the Service Center of the environment (`https://<environmentdomain>/ServiceCenter`).
1. Go to **Factory** and click the **Applications** tab.
1. Click your mobile app name to navigate to the mobile app detail page.
1. In the **Distribute** tab, under the **Native Platforms** section, click the log icon for the desired platform to download the build log.

![Icon for downloading the build log of a mobile app in Service Center](images/download-build-logs-sc.png "Download build log")

## Updating your mobile app package

Users usually don't have to update the app manually after installing it, since OutSystems automatically pushes the updates to user devices when you publish a new version of the mobile app.

However, in some specific situations, the users must install a new mobile app package. For more information check [Mobile App Update Scenarios](<../mobile-app-update-scenarios.md>).

## Distribute your app as PWA { #distribute-your-app-as-pwa }

You can use the settings in Service Center to configure your app as progressive web app (PWA). PWAs run from your server and don't require distribution though the app stores.

For more information check out [Distribute as a progressive web app (PWA)](../distribute-pwa/intro.md).

To set an app for the PWA distribution in Service Center, do the following:

1. Open the Service Center console of the environment (`https://<environmentdomain>/ServiceCenter`) and navigate to **Factory**.

1. Click the **Applications** tab, open your mobile app from the app list, then select the **Distribute** tab. The PWA settings are in the **Progressive Web Application (PWA)** section.

    ![Screenshot of the Progressive Web Application settings in Service Center for mobile app distribution](images/pwa-settings-sc.png "PWA settings in Service Center")

1. Select the checkbox **Distribute as PWA**, then click **Apply**.
