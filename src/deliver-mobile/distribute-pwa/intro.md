---
summary: Develop a progressive web app (PWA) by creating a mobile app and toggling on the option to distribute the app as PWA. Try your app in Android and iOS.
tags: support-application_development; runtime-mobile;
---

# Distribute as a progressive web app (PWA)

A progressive web app (PWA) provides a native-like experience without having to distribute a native app. PWA is an emerging technology that combines existing web development techniques with functionalities of modern browsers.

The main benefits of PWAs:

* More efficient to manage, as they don't require app stores like native mobile apps.
* Based on the web browser technology that doesn't depend on a platform. The same app runs on Android and iOS. Additionally, in OutSystems you can distribute an app as a PWA and as native builds for Android/iOS. 
* They update the moment you publish changes to your OutSystems environment.
* Lighter on user devices' systems resources.
* When you develop PWAs in OutSystems, you get all benefits of the low-code development. It's enough to turn on the PWA distribution of the app.

PWA in OutSystems is a **distribution mode** for mobile apps. A mobile app belongs to the Mobile App runtime, and the default app templates of this type are **Phone App** and **Tablet App**. Select them when you're creating a new app in Service Studio that you want to offer users as a PWA. You can simultaneously distribute a mobile app as a native mobile app and as a PWA.

<div class="info" markdown="1">

**Prerequisites**

To distribute your app as a PWA, you need:

* Service Studio 11.6 or later
* Platform Server 11.9 or later
* LifeTime Oct.2019 CP1 or later
* A valid SSL certificate to allow HTTPS communication

</div>

## Create an app and enable the PWA

Create a mobile app and turn on the toggle **Distribute as PWA** in the app details. 

1. Start creating a new app, and in the **New Application** window select **Phone App** or **Tablet App** app template.

    ![New Phone or Tablet app](images/pwa-new-app-window-ss.png?width=600)

    <div class="info" markdown="1">

    You can use an existing Mobile App to activate the PWA distribution. Review the user experience if your mobile app uses native plugins that work only with native Android or iOS builds.

    </div>

1. Add a Screen and some logic to it.

1. Publish the app.

1. In the app details, under the **Distribute** tab, turn on the toggle **Distribute as PWA**. To locate the **Distribute** tab, go back to the home screen of Service Studio and click your application icon.
   
    ![The PWA toggle to activate progressive web app distribution](images/pwa-toggle.png?width=600)

You don't have to republish your app after changing the value of the **Distribute as PWA**, as this change is effective immediately.

<div class="warning" markdown="1">

Mobile best practices apply for PWA development as well, particularly about [designing lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#Design_a_Lightweight_Local_Storage).

</div>

## Run the PWA

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


## Customize your PWA

You can customize your app by:

* Editing the details in the app details screen.
* Overriding the settings in the [PWA manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest), in the Extensibility Configurations.

### Changing the PWA properties

You can edit your app name, description, color, and logo through the UI of Service Studio. Make sure you republish the app.
  
### The manifest values you can edit in Service Studio

Service Studio generates the manifest automatically. Modify the manifest only if you want to override the values. You can edit the following manifest options from the Service Studio UI.

| Service Studio property | Manifest key  |
| ----------------------- | ------------- |
| Application Name        | `name`        |
| Application Description | `description` |
| App Primary Color       | `theme_color` |
| Application Logo*       | `icons`       |

(*) Service Studio generates the four required resolutions of the icon.

### Override the manifest settings {#override-pwa-manifest}

<div class="warning" markdown="1">

OutSystems identified an issue that prevents LifeTime from overriding the PWA Extensibility Configurations. The development team is working on the fix. Note that you can still use Extensibility Configurations in Service Studio.

</div>

<div class="info" markdown="1">

Keep in mind that the LifeTime PWA manifest overrides the manifest in Service Studio.

</div>

Using the manifest overrides the values you set in Service Studio. You have to use the manifest in the `PWAManifest` section of the JSON of the **Extensibility Configurations** field. You can edit the manifest in two places:

* In Service Studio, where the manifest overrides all UI settings **in all environments**. Edit the JSON manifest in the **Extensibility Configurations** field of the module properties.
* In LifeTime, where the manifest overrides all UI settings **in the current environment only**. Find the **Extensibility Configurations** field in **Applications** > **(app name)** > **Settings** > **Advanced** > **Extensibility Configurations**

### Manifest resources and sample JSON

You can use [Web App Manifest Generator](https://app-manifest.firebaseapp.com/) to generate the manifest, or experiment with this sample.

```
{ 
   "PWAManifest":{ 
      "name":"Name overridden",
      "short_name":"ShortName overridden",
      "description":"Description overridden",
      "theme_color":"#EDEDED",
      "background_color":"black",
      "dir":"ltr",
      "orientation": "portrait",
      "serviceworker":{ 
         "src":"/PWAServiceWorker/scripts/PWAServiceWorker.ServiceWorker.js"
      }
   }
}
```

You should be able to use the JSON for both PWA and plugins.

### Prompt to install PWA in iOS

Use a prompt to tell your users they can install the PWA version of the app. For the iOS devices, try out the community-contributed plugin [Prompt to Install PWA](https://www.outsystems.com/forge/component-overview/8216/prompt-to-install-pwa), or develop a custom solution. 

![A prompt to install PWA in iOS](images/prompt-pwa-install.png?width=300)

Android (Chrome) offers a native experience for the install prompt, so you don't need a plugin. 

## Use plugins in PWA {#plugins}

These are officially supported plugins for PWAs:

* [Camera Plugin](https://www.outsystems.com/forge/component-overview/1390/camera-plugin), from version 6.0
* [Location Plugin](https://www.outsystems.com/forge/component-versions/1395), from version 5.1

More plugins are coming soon, and you can contribute with your own on the Forge.

## Debug you PWA

To debug a PWA, emulate the app in Google Chrome. Go to the **Debugger** tab, and then in the **Debug Setup** select **Emulate using Chrome**.

![Activating the PWA debugger](images/pwa-debug-ss.png?width=750)

## Troubleshooting

Here are some troubleshooting tips to assist you in fixing you PWA.

### The toggle button has no effect

If you haven't done it already, republish the apps in the factory and then turn on the toggle **Distribute as PWA**. For the new features to work correctly, you need to republish your apps after a Platform Server upgrade, as instructed in the Platform Server upgrade list.

### I'm getting an invalid home URL for PWA

If the PWA can't load because you're getting the URL that matches the URL of the environment, for example ` https://example.com/`, check if your set a home module for your app.

Open the app details screen. If the **Test in browser button** is deactivated, the app doesn't have a module defined. Click the curly arrow icon on the right side of the module name to set that module as the home module. Try loading the PWA again.

![Set a home module](images/set-home-module-ss.png?width=600)

### The PWA debugging isn't starting

The window **Waiting for application** stays open, and nothing happens when you start the debugging of your PWA.

To fix this issue, set the debugger to **Emulate using Chrome** before you click **Start debugging**. Note that the options **Android device** and **iOS device** of the debugger work only when you distribute your app as a native build, and can't work with an app you distribute as PWA.

### Extensibility Configurations override isn't working when applied in LifeTime

There's an issue with applying Extensibility Configurations from LifeTime to override the manifest. The team is working on the fix. Note that you can still use Extensibility Configurations in Service Studio.

### PWA doesn't install in iOS

If you're using Platform Server 11.7 or earlier **and** iOS 13 and later, you should **either**:

* Upgrade to Platform Server 11.8 or later.

* Disable Web SQL. Go to **Settings** > **Safari** > **Advanced** > **Experimental Features** > and make sure **Disable Web SQL** is off.
    
    ![WebSQL Settings in Safari iOS](images/pwa-ios-websql-settings.png?width=250)

### PWA isn't working in iOS 13.0 to 13.2

There's an iOS bug that prevents PWAs from running correctly in the iOS versions 13.0 to 13.2. To fix the issue, use iOS 13.3 or later.

### PWA is slow and queries take too long to execute

If your PWA performs poorly and queries take too long to execute, your local storage model might be too complex or the amount of data that the app needs to handle is too high. See [Design a lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#Design_a_Lightweight_Local_Storage) for recommendations.

### I'm getting "not connected to the environment" error when I enable the PWA

You're getting the following error in Service Studio when you try to enable the PWA: "There was an error connecting to your development environment. Confirm your connection and retry".

Here are some suggestions to fix the issue:

* Connect to Service Studio by entering your environment URL that begins with "https". For example, instead of connecting to `http://myenvironment.example.com`, connect to `https://myenvironment.example.com`. After that, retry enabling the PWA.

* Check if you have a valid and properly configured SSL certificate. When you distribute a mobile app, by a native build or as a PWA, you need the certificate for secure communication with the server. For more information, see notes in [Enforce HTTPS Security](../../managing-the-applications-lifecycle/secure-the-applications/enforce-https-security.md).

### There are runtime errors

Try deleting the local data of the app. Locate the settings in the browser, and clear the data for the app installation domain. In Chrome, go to **Settings** > **Site Settings** > **Cookies and site data** > **See all cookies and site data**, search for the domain and clear the data.
