---
summary: Generate a mobile app package for your mobile app to publish in the Google Play Store. 
tags: runtime-mobile; support-mobile
locale: en-us
guid: 49613761-0f66-4d87-b41a-bf600081e654
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=310:17
---

# Publish Your Mobile Android Application to the Google Play Store

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

This article describes the process you must follow to publish your application to the Google Play Store. Before you proceed, ensure your app fulfills the general [pre-requirements](publish-app-stores.md).

To publish your app to the Google Play store you must have a developer account. If you don't, [create a new Google Developer Account here](https://developer.android.com/distribute/googleplay/start.html).

## Preparation Checklist

Google [provides a checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist) with instructions to ensure your application is compliant with the publishing rules and the quality required.

Pre-requirements for Android include [graphics assets](https://developer.android.com/distribute/best-practices/launch/store-listing.html#best-practices) and an [app package](https://support.google.com/googleplay/android-developer/answer/113469?hl=en).

Google also provides a video with a [list of 10 tips](https://www.youtube.com/watch?v=psu3pPdfYSM) you should  follow to ensure the success of your application.

## Publishing Android Applications to Google Play

### Generate an Android build

You can generate the release (final) version of your mobile app in Service Studio or Service Center.

#### Service Studio

To generate an Android build in the Service Studio, perform the following steps:

1. Go to the app detail screen of the mobile application for which you want to generate the mobile application package. Open the **Distribute** tab.

1. Click on the **Generate Android App** button, or the Android cog icon button if you've already generated a previous Android app.

    ![Screenshot of the Service Studio showing the Configure Android App Menu with the Generate Android App button highlighted](images/ss-native-platforms-tab-android2.png "Configure Android App Menu in Service Studio")

1. In the **Build type** list, select the **Release** option.

1. Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, for example, **com.domain.appname**).

1. Select the keystore to sign your app and introduce the passwords. If you don't have a keystore to sign your Android apps, [check here](more-information.md#For_Android) how to do it.

1. Fill in the alias name and password of the private/public key pair to use. The alias you must use is the one generated when creating the keystore.

1. Click **Generate Android app**.

    ![Screenshot of the Service Studio interface for configuring Android app settings including Build type, App identifier, and Keystore information](images/ss-native_platforms-configure-android-app.png "Configure Android App Settings in Service Studio")    

#### Service Center

 To Generate an Android build in the Service Center, perform the following steps:

1. Access Service Center console of the environment (`https://<environmentdomain>/ServiceCenter`).

1. Go to **Factory**, click on the **Applications** tab, and open your application from the applications list.

    ![Screenshot of the OutSystems Service Center showing the Factory Applications menu with the Applications tab selected](images/outsystems-service-center-factory-applications-menu.png "Service Center Factory Application Menu")

1. Select the **Distribute** tab and click on the **Configure** link for the Android entry in the **Native Platforms** section.

    ![Screenshot of the OutSystems Service Center's Native Platforms section with the Configure link for Android highlighted](images/outsystems-service-center-factory-native-platform-tab-android.png "Service Center Factory Application Configure Android")

1. In the **Build type** drop-down menu, select the **Release** option.

    Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, for example, **com.domain.appname**).

1. Select the keystore to sign your app and introduce the passwords. If you don't have a keystore to sign your Android apps, [check here](more-information.md#For_Android) how to do it.

1. Fill in the alias name and password of the private/public key pair to use. The alias you must use is the one generated when creating the keystore.

    ![Screenshot of the Android settings in the Service Center with options for Build type, App identifier, and Keystore configuration](images/sc-configure-android-settings.png "Service Center Factory Application Android Settings")

1. Click **Save** to save your settings.

1. Click **Save and Generate** and wait a few moments while the app is being generated.

    ![Screenshot of the Service Center showing the Save and Generate button for creating an Android build of the mobile app](images/sc-select-mabs-version.png "Service Center Factory Application Generate")

1. After the app is generated, click the **download** icon near the version information to download the Android build.

    ![Screenshot of the Service Center with the download icon for the generated Android build near the version information](images/outsystems-service-center-factory-native-platform-download-android.png "Service Center Factory Application Download")

## Distribute the Mobile App through the Google Play store

After the generation has been completed, scan the QR code or copy the created installation link using your device to download the Android build.

You need now to access the [Google Play Console](https://play.google.com/apps/publish) to upload your mobile app.

You have to provide the following information: 

* To create the application:
    * The name
    * The default language

* To release the application:
    * Choose whether to roll out to Beta testing or Production.
    * Calculate the content rating by answering a few questions.
    * Define the pricing.
    * Define the countries and regions where it’s going to be available.
    * Define a few more requirements.
    * Fill the Google Data safety form. Check [User Privacy in OutSystems Android apps section](#privacy) for more information.

* To define the store listing:
    * The title, short description, and full description
    * The application screenshots
    * Your contacts
    * The URL of your privacy policy, if any

* Provide information for [Google Play's Data safety section](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#types&zippy=%2Cdata-types).
    * By default, OutSystems apps collect the following data:

        | Category | Data Type | Description |
        |---|---|---| 
        | App info and performance | Crash logs | Crash logs are collected in the Service center for troubleshoot purposes|
        | Device or other IDs | Device or other IDs | We’re using the DeviceUUID which is solely respective to the current application installation and we're collecting it for troubleshoot purposes |

    * In this form, you must also add entries for any data that you are collecting on top of the above mentioned ones, leveraged by either custom or supported plugins.

At the final steps, you need to release the app to Beta Testing or Production, according to your choice, confirm the version and the build (APK/AAB), and start the rollout.

After completing this process your application is published and available for download at the Google Play Store.

## User Privacy in OutSystems Android apps { #privacy }

When submitting a mobile app to the store, you have to answer a few questions about the user sensitive data being collected or shared by the app. You can obtain more details about the Google Safety data form [here](https://support.google.com/googleplay/android-developer/answer/10787469?hl=en).

We understand that OutSystems customers may not be fully aware on how OutSystems base apps may collect or share user data. The following table shows what kinds of data contain or may contain user sensitive data and their purposes:

<table>
<thead>
<tr>
<th>Data Type</th>
<th>Purpose</th>
<th>Detailed reason</th>
</tr>
</thead>
<tbody>
<tr>
<td>Crash logs</td>
<td>Analytics<br/>
Fraud prevention, security, and compliance
</td>
<td>Crash logs are collected for troubleshooting purposes</td>
</tr>
<tr>
<td>Device or other IDs</td>
<td>Analytics</td>
<td>The deviceUUID is collected for troubleshooting purposes</td>
</tr>
<tr>
<td>Files and docs<br/>
Videos<br/>
Voice or sound recordings<br/>
Music files<br/>
Other audio files</td>
<td>App functionality</td>
<td>The OutSystems upload widget requires the <code>READ_EXTERNAL_STORAGE</code> permission to access user file system. This permission can be disregarded by setting the preference <code>AddUploadWidgetPermissions</code> as <code>false</code> in the application extensibility configurations</td>
</tr>
</tbody>
</table>

Every network request trigger by the OutSystems runtime is performed via HTTPS which uses TLS (Transport Layer Security) to ensure secure communication channels.

This section may be updated overtime, so we recommend you check this section when uploading a new app version to the store.

We highly recommend you to review the usage of user sensitive data in other parts of your application that do not belong to the OutSystems domain by following the [Google guidelines](https://developer.android.com/guide/topics/data/collect-share).

______________________________________________________________
_QR CODE is a registered trademark of Denso Wave Incorporated._
