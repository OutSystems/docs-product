---
summary: Develop a Progressive Web App (PWA) by creating a Mobile App and toggling on the option to distribute the app as PWA. Try your app in Android and iOS.
tags: support-application_development; runtime-mobile;
---

<div class="info" markdown="1">

This document is a work in progress. Please share your feedback in the [forum topic dedicated to the PWA feature](https://www.outsystems.com/forums/discussion/56090/progressive-web-apps-early-access-now-open-to-everyone/).

</div>

# Early Access - Distribute as a progressive web app (PWA)

Progressive web apps (PWA) provide native-like experiences without having to distribute a native app. When you develop PWAs in OutSystems, you get all the benefits of the low-code development, as all you need is to build a Mobile App and enable the PWA feature.

<div class="info" markdown="1">

**Prerequisites**

To distribute your app as a PWA, you need:

* Service Studio 11.6 or later
* Platform Server 11.7 or later
* LifeTime Oct.2019 CP1 or later
* A valid SSL certificate to allow HTTPS communication 
* Enable the [early access feature](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Early_access_to_OutSystems_features) in LifeTime

</div>

## Create a Progressive Web App

<div class="info" markdown="1">

The **Distribute** tab is available only after you activate the feature in LifeTime.

</div>

Create a Mobile App and turn on the toggle **Distribute as PWA** in the app details. 

1. Start creating a new app, and in the **New Application** window select **Phone App** or **Tablet App** app template. Note that the PWA feature works with Mobile Apps only.
2. Add a Screen and some logic to it.
3. Publish the app.
4. In the app details, under the **Distribute** tab, turn on the toggle **Distribute as PWA**. To locate the **Distribute** tab, go back to the home screen of Service Studio and click your application icon.
   
    ![The PWA toggle to activate progressive web app distribution](images/pwa-toggle.png?width=600)

You don't have to republish your app after changing the value of the **Distribute as PWA**, as this change is effective immediately.

<div class="warning" markdown="1">

When you develop a progressive web app, keep in mind that mobile best practices apply, particularly about [designing a lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#Design_a_Lightweight_Local_Storage).

</div>

## Try out your progressive web app

Here is how you can run your PWA. Go to app details and click **Distribute** tab:

* To open on your mobile device, scan the QR code.
* To open in a desktop browser, click the link.

![The QR code and links to run progressive web app](images/pwa-open-links.png?width=400)

### PWA in Android

Follow these steps to install and run your PWA on an Android device.

1. Visit the app URL in Chrome.
2. Tap the banner **Add (my app) to Home screen**.

    ![Installing app in Android](images/pwa-app-install-android.png?width=300)

3. After you see a confirmation saying that the app was added to the home screen, open the app like any other app installed from a store. You can also uninstall it like any other app.
    
    ![PWA on Android home screen](images/pwa-app-android-home.png?width=300)

### PWA in iOS

Follow these steps to install and run your PWA on an iOS device.

<div class="info" markdown="1">

Due to a bug in iOS, PWAs aren't working in the iOS versions 13.0 to 13.2. Use iOS 13.3 or later instead.

</div>

1. Visit the app URL in Safari.
2. Tap the Share button. The share menu opens.
   
    ![Share button in Safari iOS](images/pwa-share-button-ios.png?width=300)

3. Tap **Add to home screen**. The confirmation screen opens.

    ![Share options on iOS](images/pwa-share-options-ios.png?width=300)

4. In the confirmation screen, tap **Add**.
    
    ![Confirm adding to iPhone home screen](images/pwa-ios-share-confirm.png?width=300)

5. Your app should now be on the home screen. You can also uninstall it like any other app.
    
    ![Add to home screen share option on iOS](images/pwa-app-ios-home.png?width=300)


## Customize your app

You can customize your app by:

* Editing the details in the app details screen
* Overriding the settings in by using the [PWA manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) in the Extensibility Configuration

### Changing the app properties

You can edit your app name, description, color, and logo through the UI of Service Studio. Make sure you republish the app.
  
### The manifest values editable in Service Studio

Service Studio generates the manifest automatically, and you can modify the manifest only if you want to override some values. You can edit the following manifest options from the Service Studio UI.

| Service Studio property | Manifest key  |
| ----------------------- | ------------- |
| Application Name        | `name`        |
| Application Description | `description` |
| App Primary Color       | `theme_color` |
| Application Logo*       | `icons`       |

(*) Service Studio generates the four required resolutions of the icon.

### Overriding the manifest settings {#override-pwa-manifest}

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

You can use [Web App Manifest Generator](https://app-manifest.firebaseapp.com/) to generate the manifest, or experiment with the sample we provide here.

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

An efficient way to tell your users to install the PWA version of the app is to use a prompt. For the iOS devices, try out the community-contributed plugin [Prompt to Install PWA](https://www.outsystems.com/forge/component-overview/8216/prompt-to-install-pwa), or develop a custom solution. Android (Chrome) offers a native experience for the install prompt, so you don't need a plugin.

![A prompt to install PWA in iOS](images/prompt-pwa-install.png?width=300)


## Plugins in PWA {#plugins}

During the early access, you can try out the following officially supported plugins in your PWAs:

* [Camera Plugin](https://www.outsystems.com/forge/component-overview/1390/camera-plugin), from version 6.0
* [Location Plugin](https://www.outsystems.com/forge/component-versions/1395), from version 5.1

There are more plugins coming soon, and you can contribute with your own on the Forge.

## Debugging

To debug a PWA, emulate the app in Google Chrome. Go to the **Debugger** tab, and then in the **Debug Setup** select **Emulate using Chrome**.

![Activating the PWA debugger](images/pwa-debug.png?width=750)

## Troubleshooting

Here are some notes that can help you in troubleshooting the PWA feature.

### The toggle button has no effect

Note that you need to republish your apps after the Platform Server upgrade for the new features to work correctly, as instructed in the Platform Server upgrade list. If you haven't done it already, republish the apps in the factory and then turn on the toggle **Distribute as PWA**.

There is a potential workaround for the PWA toggle button to work without the republishing step, which is to republish the current module once and then try turning on the toggle **Distribute as PWA**. However, keep in mind that republishing the apps after the upgrade is a mandatory step, and skipping it can cause unintended effects.

### I'm getting an invalid home URL for PWA

If the PWA can't load because you're getting the URL that matches the URL of the environment, for example ` https://example.com/`, check if your set a home module for your app.

Open the app details screen. If the **Test in browser button** is deactivated, the app doesn't have a module defined. Click the curly arrow icon on the right side of the module name to set that module as the home module.

![Set a home module](images/set-home-module.png?width=600)

### There are runtime errors

Try deleting the local data of the app. Locate the settings in the browser, and clear the data for the app installation domain. In Chrome, go to **Settings** > **Site Settings** > **Cookies and site data** > **See all cookies and site data**, search for the domain and clear the data.

### Extensibility Configurations override isn't working when applied in LifeTime

There's an issue with applying Extensibility Configurations from LifeTime to override the manifest. The team is working on the fix. Note that you can still use Extensibility Configurations in Service Studio.

### PWA doesn't install in iOS

If you're using Platform Server 11.7 or earlier **and** iOS 13 and later, you should either:

* Upgrade to Platform Server 11.8 or later
* Disable Web SQL. Go to **Settings** > **Safari** > **Advanced** > **Experimental Features** > and make sure **Disable Web SQL** is off.
    
    ![WebSQL Settings in Safari iOS](images/pwa-ios-websql-settings.png?width=250)


### PWA doesn't work in iOS

One of the reasons why your PWA isn't working in iOS might be because of an iOS bug that prevents PWAs from running correctly in the iOS versions 13.0 to 13.2. 

To fix this issue, use iOS 13.3 or later instead.

### PWA is slow and queries take too long to execute

If your PWA performs poorly and queries take too long to execute, your local storage model might be too complex or the amount of data that the app needs to handle is too high. See [Design a lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#Design_a_Lightweight_Local_Storage) for recommendations.

### I get "not connected to the environment" error when I enable the PWA

You're getting the following error in Service Studio when you try to enable the PWA: "There was an error connecting to your development environment. Confirm your connection and retry".

Here are some suggestions to fix the issue:

* Connect to Service Studio by entering your environment URL that begins with "https". For example, instead of connecting to `http://myenvironment.example.com`, connect to `https://myenvironment.example.com`. After that, retry enabling the PWA. You can change the environment you're signed in by clicking the URL in the lower right corner of Service Studio.
* Check if you have a valid and properly configured SSL certificate. When you distribute a Mobile App, by a native build or as a PWA, you need the certificate for secure communication with the server. For more information see notes in [Enforce HTTPS Security](../../managing-the-applications-lifecycle/secure-the-applications/enforce-https-security.md).

### The PWA debugging doesn't start

The window **Waiting for application** stays open and nothing happens when you start the debugging of your PWA.

To fix this issue, set the debugger to **Emulate using Chrome** before you click **Start debugging**. Note that the options **Android device** and **iOS device** of the debugger work only when you distribute your app as a native build, and can't work with an app you distribute as PWA.  