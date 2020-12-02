---
summary: Generate a production mobile app package for your mobile app to distribute to a group of selected end users.
tags: runtime-mobile; support-mobile
---

# Generate and Distribute Your Mobile App to a Limited Group of End Users

A way of to start the distribution of your production-ready mobile app is by making it initially available to a limited group of users.

In OutSystems, you can generate a mobile application package for your mobile app to be installed by the selected end users.

## For iOS

### Before You Start

* To generate your iOS mobile app you must be enrolled as an Apple Developer. If you haven’t enrolled yet, learn [how to enroll as an Apple developer](<more-information.md#enroll-as-an-apple-developer>). 

* To test your app, you must have a certificate generated and configured in your Apple Developer account. The exact type of certificate depends on the developer program you enrolled in:  
— `App Store and Ad Hoc` certificate for the Apple Developer Program, or  
— `In-House and Ad Hoc` certificate for the Apple Developer Enterprise Program  
If you don’t have one, learn [how you can create a certificate](<more-information.md#create-a-certificate>).

* To allow launching your app in the devices of the end users group, you must set up the `Ad Hoc` provisioning profile with the relevant device IDs. A provisioning profile allows your application to be launched on Apple devices and use app services. If you don't have one, learn [how you can create a provisioning profile](<more-information.md#create-a-provisioning-profile>).

For more information on registering devices on your Apple Developer account, check the [Apple Developer website](<https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW10>). For more information on the different provisioning profiles check the Medium blog post "[Cruising through the Complexities of Signing Native Mobile Apps](https://medium.com/outsystems-engineering/cruising-through-the-complexities-of-signing-native-mobile-apps-cc123eb2814b)" by OutSystems.

### Generate the iOS App Package (IPA)

You can generate your iOS app package in Service Studio or in Service Center.

To use Service Studio, do the following:

1. Go to the app detail screen of the mobile application for which you want to generate the mobile application package. Open the [Distribute](<intro.md#config-generate-service-studio>) tab, and check out the **Native Platforms** section.
1. Click on the **Configure iOS App** button or the iOS cog icon if you've already generated a previous iOS app. 
1. In the **Build type** dropdown, select the `Ad-Hoc` option. 
1. Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, e.g. `com.domain.appname`). You have to register the same app identifier in your Apple Developer Account. 
1. Provide a certificate of the correct type (see "Before You Start") and its password. The certificate should have a .p12 file extension. 
1. Provide an `Ad Hoc` provisioning profile that matches the certificate you provided. The provisioning profile should have a .mobileprovision extension. 
1. Click **Generate App** . 

When the app generation completes, scan the QR code or copy the created installation link using your device to install the generated iOS app.

To use Service Center, do the following:

1. Access Service Center of the environment (`https://<environmentdomain>/ServiceCenter`). 
1. Go to **Factory**, click on the **Applications** tab and open your application from the applications list. 
1. Select the [Distribute](<intro.md#config-generate-service-center>) tab and click on the **Configure** link for the iOS entry, in the **Native Platforms** section.
1. In the **Build type** dropdown, select the `Ad-Hoc` option. 
1. Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, e.g. `com.domain.appname`). 
1. Provide a certificate of the correct type (see "Before You Start") and its password. The certificate should have a .p12 file extension. 
1. Provide an `Ad Hoc` provisioning profile that matches the certificate you provided. The provisioning profile should have a .mobileprovision extension. 
1. Click **Save** to save your settings. 
1. Click **Generate** and wait a few moments while the app is being generated. 

After the app is generated, click the download icon near the version information to download the iOS app package (IPA).

### Distribute the App to the Group of End Users

There are several ways to distribute your iOS mobile app to a selected group of end users, such as:

* Send the end users the Service Studio generated QR code, the installation link or the mobile app package (IPA) itself. Have in mind that only selected devices specified for the provisioning profile will be able install and launch the app. If a given user’s device is not authorized to install the app, the user will get a "Unable to Download App" alert message. For more information on registering devices associated with a given provisioning profile, check the [Apple Developer website](<https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW10>).

* Use the TestFlight Beta Testing program available in [iTunes Connect](<https://itunesconnect.apple.com>). After you upload your mobile app package to TestFlight in iTunes Connect, you will be able to invite internal and external testers. If you invite external testers, your app will temporarily be held for Beta App Review. For more information on using TestFlight, check the [TestFlight help topic](<https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/DistributingYourAppUsingTestFlight/DistributingYourAppUsingTestFlight.html>) in the Apple Developer website. 


## For Android

### Before You Start

If you decide to create a closed beta program for distributing the mobile app to a limited group of end users, each participating end user must have a Google Account.

### Generate the Android App Package (APK)

You can generate your mobile app package in Service Studio or in Service Center.

To use Service Studio, do the following:

1. Go to the app detail screen of the mobile application for which you want to generate the mobile application package. Open the [Distribute](<intro.md#config-generate-service-studio>) tab, and check out the **Native Platforms** section.
2. Click on the **Configure Android App** button or the Android cog icon button if you've already generated a previous Android app. 
3. In the **Build type** dropdown, select the `Release` option. 
4. Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, e.g. `com.domain.appname`). 
5. Select the keystore to sign your app and introduce the passwords. If you don't have a keystore to sign your Android apps, [check how to do it](<more-information.md#create-a-keystore>). 
6. Fill in the alias name and password of the private/public key pair to use. The alias you must use is the one generated when creating the keystore. 
7. Click **Generate App**. 

After the generation has been completed, scan the QR code or copy the created installation link using your device to download the Android package (APK).

To use Service Center, do the following:

1. Access Service Center of the environment (`https://<environmentdomain>/ServiceCenter`). 
2. Go to **Factory**, click on the  Applications  tab and open your application from the applications list. 
3. Select the [Distribute](<intro.md#config-generate-service-center>) tab and click on the **Configure**  link for the Android entry, in the **Native Platforms** section.
4. In the **Build type** dropdown, select the `Release` option. 
5. Keep the default app identifier assigned by OutSystems or write your own (matching reverse domain name notation, e.g. `com.domain.appname`). 
6. Select the keystore to sign your app and introduce the passwords. If you don't have a keystore to sign your Android apps, [check how to do it](<more-information.md#create-a-keystore>). 
7. Fill in the alias name and password of the private/public key pair to use. The alias you must use is the one generated when creating the keystore. 
8. Click **Save** to save your settings. 
9. Click **Generate** and wait a few moments while the app is being generated. 

After the app is generated, click the download icon near the version information to download the Android package (APK).

### Distribute the App to the Group of End Users

There are several ways to distribute your Android mobile app to a selected group of end users, such as:

* Send the end users the Service Studio generated QR code, the installation link or the mobile app package (APK) itself.

* Set up a closed beta testing program in the Play Store. This allows you to distribute the app to a limited group of end users. You will need to set up a closed beta testing program in your [Google Play Developer Console](<https://play.google.com/apps/publish/>), specify (or import) the email addresses of the end users that will have access to your beta testing program, share the opt-in URL with them, upload your app package (APK) and publish your app.  
    Note that the Play Store's closed beta functionality cannot ensure that only the devices of authorized end users are able to install and run your beta mobile app. While iOS enforces this through a list of authorized device IDs, in Android there are no such limits. Check the [Google Play Developer Console documentation](<https://support.google.com/googleplay/android-developer/answer/3131213?hl=en#runtest>) for more information on running beta testing programs for Android mobile apps.
