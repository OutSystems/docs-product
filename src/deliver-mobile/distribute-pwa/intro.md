---
summary: Develop a progressive web app (PWA) by creating a mobile app and toggling on the option to distribute the app as PWA. Try your app in Android and iOS.
tags: support-application_development; runtime-mobile;
---

# Distribute as a progressive web app (PWA)

A progressive web app (PWA) provides a native-like experience without having to distribute a native mobile app. PWA is an emerging technology that combines existing web technologies with modern browser features.

The main benefits of PWAs:

* More efficient to manage, as they don't require app stores like native mobile apps.
* Based on the web browser technology that doesn't depend on a platform. The same app runs on Android and iOS. Additionally, in OutSystems you can distribute an app as a PWA and as native builds for Android/iOS. 
* They update the moment you publish changes to your OutSystems environment.
* Lighter on user devices' systems resources.
* When you develop PWAs in OutSystems, you get all benefits of the low-code development. It's enough to turn on the PWA distribution of the app.

<div class="info" markdown="1">

Check out [PWA - The Fastest, Easiest Way to Deploy your OutSystems Apps](https://www.youtube.com/watch?v=_YQKTDV_YpE) for a quick video intro!

</div>

PWA in OutSystems is a **distribution mode** for mobile apps. A mobile app belongs to the Mobile App runtime, and the default app templates of this type are **Phone App** and **Tablet App**. Select them when you're creating a new app in Service Studio that you want to offer users as a PWA. You can simultaneously distribute a mobile app as a native mobile app and as a PWA.

<div class="info" markdown="1">

**Prerequisites**

To distribute your app as a PWA, you need:

* Service Studio 11.6 or later
* Platform Server 11.9 or later
* LifeTime Oct.2019 CP1 or later
* A valid SSL certificate to allow HTTPS communication

</div>

## Creating an app and enabling the PWA

Create a mobile app and turn on the toggle **Distribute as PWA** in the app details. 

1. Start creating a new app, and in the **New Application** window select **Phone App** or **Tablet App** app template.

    ![New Phone or Tablet app](images/pwa-new-app-window-ss.png?width=600)

    <div class="info" markdown="1">

    You can use an existing Mobile App to activate the PWA distribution. Review the user experience if your mobile app uses native plugins that work only with native Android or iOS builds.

    </div>

1. Add a Screen and some logic to it.

1. Publish the app.

1. In the app details, under the **Distribute** tab, turn on the toggle **Distribute as PWA**. To locate the **Distribute** tab, go back to the home screen of Service Studio and click your app icon.
   
    ![The PWA toggle to activate progressive web app distribution](images/pwa-toggle.png?width=600)

**Notes**

* You don't have to republish your app after changing the value of the **Distribute as PWA**, as this change is effective immediately.
* You can also change the PWA settings for an app in an environment through Service Center. For more information, see [Generate and distribute your mobile app](../generate-distribute-mobile-app/intro.md#distribute-your-app-as-pwa).

<div class="warning" markdown="1">

Mobile best practices apply for PWA development as well, particularly about [designing lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#Design_a_Lightweight_Local_Storage).

</div>

## Running the PWA

Here is how you can run your PWA. Go to the app details in Service Studio and click **Distribute** tab:

* **Scan the QR code** to open the PWA on your mobile device. 
* **Click the link** to open the PWA in a desktop browser.

![The QR code and links to run progressive web app](images/pwa-open-links-ss.png?width=350)

### PWA in Android

Follow these steps to install and run your PWA on an Android device.

1. Visit the app URL in Chrome.

1. Tap the banner **Add (my app) to Home screen**.

    ![Installing app in Android](images/pwa-app-install-android.png?width=300)

1. After you see a confirmation that Android added the shortcut to the home screen, open the app like any other app installed from a store. You can uninstall it like any other Android app.
    
    ![PWA on Android home screen](images/pwa-app-android-home.png?width=300)

### PWA in iOS

Follow these steps to install and run your PWA on an iOS device.

1. Visit the app URL in Safari.

1. Tap the Share button. The share menu opens.
   
    ![Share button in Safari iOS](images/pwa-share-button-ios.png?width=300)

1. Tap **Add to home screen**. The confirmation screen opens.

    ![Share options on iOS](images/pwa-share-options-ios.png?width=300)

1. In the confirmation screen, tap **Add**.
    
    ![Confirm adding to iPhone home screen](images/pwa-ios-share-confirm.png?width=300)

1. Your app should now be on the home screen. You can uninstall it like any other iOS app.
    
    ![Add to home screen share option on iOS](images/pwa-app-ios-home.png?width=300)


## Customizing your PWA

You can customize your app by:

* Editing the details in the app details screen.
* [Editing the PWA manifest](advanced.md#editing-manifest).

### Changing the PWA properties

You can edit your app name, description, color, and logo through the UI of Service Studio. Make sure you republish the app. For overriding properties with the PWA manifest, check out [Advanced settings and customizations](advanced.md).

### Prompting users to install PWA in iOS

Use a prompt to tell your users they can install the PWA version of the app. For the iOS devices, try out the community-contributed plugin [Prompt to Install PWA](https://www.outsystems.com/forge/component-overview/8216/prompt-to-install-pwa), or develop a custom solution. 

![A prompt to install PWA in iOS](images/prompt-pwa-install.png?width=300)

Android (Chrome) offers a native experience for the install prompt, so you don't need a plugin. 

## Using plugins {#plugins}

These are the officially supported plugins for PWAs:

* [Camera Plugin](https://www.outsystems.com/forge/component-overview/1390/camera-plugin), from version 6.0
* [Location Plugin](https://www.outsystems.com/forge/component-versions/1395), from version 5.1

More plugins are coming soon, and you can contribute with your own on the Forge.

## Debugging your PWA

To debug a PWA, emulate the app in Google Chrome. Go to the **Debugger** tab, and then in the **Debug Setup** select **Emulate using Chrome**.

![Activating the PWA debugger](images/pwa-debug-ss.png?width=750)

<div class="info" markdown="1">

Having issues with your PWA? Check out [Troubleshooting and known issues](troubleshooting-know-issues.md).

</div>

## Learning resources

* [PWAs overview and best practices](https://www.outsystems.com/training/courses/164/pwa-overview-and-best-practices/) is an intermediate course about progressive web apps in OutSystems. Learn more about differences between PWAs and native apps, advantages and challenges, installation and desktop support.

<div class="info" markdown="1">

The team would love to hear what you think of this document and if it helps you. Please **leave feedback** in the feedback section. If you want to get a reply, select **Yes, you may contact me about this feedback**.

</div>