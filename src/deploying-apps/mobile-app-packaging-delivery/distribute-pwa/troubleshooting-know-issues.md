---
summary: Troubleshooting tips and notes. Know issues.
tags: support-application_development; runtime-mobile;
locale: en-us
guid: 894f3950-7424-4995-9f8b-4e7e9c2645d7
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=1818:841
---

# Troubleshooting and known issues

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

This document contains information about troubleshooting and known issues.

## Known issues

Here are the known issues with PWA.

### Overriding the Extensibility Configurations in LifeTime isn't working

There's an issue that prevents LifeTime from overriding the PWA Extensibility Configurations. Upgrade to Platform Server 11.11.0 to resolve the issue.

### Staging of the PWA toggle value in LifeTime isn't working

In Platform Server 11.9.0, the staging of the PWA toggle value in LifeTime isn't working as expected. Upgrade to Platform Server 11.10.0 or later to resolve the issue.

## Troubleshooting

Here are some troubleshooting tips to assist you in fixing you PWA.

### The toggle button has no effect

If you haven't done it already, republish the apps in the factory and then turn on the toggle **Distribute as PWA**. For the new features to work correctly, you need to republish your apps after a Platform Server upgrade, as instructed in the Platform Server upgrade list.

### I'm getting an invalid home URL for PWA

If the PWA can't load because you're getting the URL that matches the URL of the environment, for example ` https://example.com/`, check if you set a home module for your app.

Open the app details screen. If the **Test in browser button** is deactivated, the app doesn't have a module defined. Click the curly arrow icon on the right side of the module name to set that module as the home module. Try loading the PWA again.

![Screenshot showing how to set a home module in OutSystems application details screen](images/set-home-module-ss.png "Setting a Home Module in OutSystems")

### The PWA debugging isn't starting

The window **Waiting for application** stays open, and nothing happens when you start the debugging of your PWA.

To fix this issue, set the debugger to **Emulate using Chrome** before you click **Start debugging**. Note that the options **Android device** and **iOS device** of the debugger work only when you distribute your app as a native build, and can't work with an app you distribute as PWA.

### PWA doesn't install in iOS

If you're using Platform Server 11.7 or earlier **and** iOS 13 and later, you should **either**:

* Upgrade to Platform Server 11.8 or later.

* Disable Web SQL. Go to **Settings** > **Safari** > **Advanced** > **Experimental Features** > and make sure **Disable Web SQL** is off.
    
    ![Screenshot of disabling Web SQL in Safari's Experimental Features settings on iOS](images/pwa-ios-websql-settings.png "WebSQL Settings in Safari on iOS")

### PWA isn't working in iOS 13.0 to 13.2

There's an iOS bug that prevents PWAs from running correctly in the iOS versions 13.0 to 13.2. To fix the issue, use iOS 13.3 or later.

### PWA is slow and queries take too long to execute

If your PWA performs poorly and queries take too long to execute, your local storage model might be too complex or the amount of data that the app needs to handle is too high. See [Design a lightweight local storage](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices#lightweight-local-storage) for recommendations.

### I'm getting "not connected to the environment" error when I enable the PWA

You're getting the following error in Service Studio when you try to enable the PWA: "There was an error connecting to your development environment. Confirm your connection and retry".

Here are some suggestions to fix the issue:

* Connect to Service Studio by entering your environment URL that begins with "https". For example, instead of connecting to `http://myenvironment.example.com`, connect to `https://myenvironment.example.com`. After that, retry enabling the PWA.

* Check if you have a valid and properly configured SSL certificate. When you distribute a mobile app, by a native build or as a PWA, you need the certificate for secure communication with the server. For more information, see notes in [Enforce HTTPS Security](../../../security/enforce-https-security.md).

### There are runtime errors

Try deleting the local data of the app. Locate the settings in the browser, and clear the data for the app installation domain. In Chrome, go to **Settings** > **Site Settings** > **Cookies and site data** > **See all cookies and site data**, search for the domain and clear the data.
