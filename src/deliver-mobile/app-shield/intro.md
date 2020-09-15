---
summary: Protect your mobile apps against tampering. OutSystems AppShield hardens the native mobile build, enabling the app to detect attempts of modification and misuse.
tags: support-application_development; runtime-mobile;
---

# Harden the protection of mobile apps with AppShield

OutSystems AppShield lets you harden the protection of your native Android and iOS apps. OutSystems AppShield is fully integrated with Mobile Apps Build Service (MABS) builds and adds protection at runtime and at rest.

<div class="info" markdown="1">

To use OutSystems AppShield, you need to have a license. If you haven't got it already, contact the sales team.

</div>

## Prerequisites

To protect your apps with AppShield, you need to meet the following requirements.

* You installed the AppShield plugin in your environment. To download the plugin, check out [OutSystems AppShield](https://www.outsystems.com/forge/component-overview/9379/) in Forge. 
* You have a license for AppShield.
* You're using MABS 6.1 or later.

Additionally:

* You need to rebuild and redistribute the mobile apps that you want to protect.
* Account for the app file size increases after hardening the security, and additional time for MABS to create the build.  

## Supported features

These are the features you can use with the current release of the AppShield plugin.

### Android

Protection available for the Android builds.

* Root detection
* Repackaging detection
* Code obfuscation
* Code injection protection
* Debugger protection
* Emulator detection
* Keylogger protection
* Screenshot protection
* Task hijacking protection

### iOS

Protection available for the iOS builds.

* Jailbreak detection
* Repackaging detection
* Code injection protection
* Debugger protection
* Screenshot protection

## How to use OutSystems AppShield

To create a mobile app build with AppShield to hardened security, do the following:

1. Install the AppShield component.
2. Add AppShield dependencies to your app. Press **Ctrl+Q** to open the **Manage Dependencies** window. Enter `OutSystemsAppShieldPlugin` in the producer search field and then select all the elements in the right pane. Click **Apply** to add the references to your app and close the window.

    ![Manage dependencies](images/reference-appshield-ss.png?width=600)

4. Publish the app.
5. Create native mobile builds of the app.

### Configuration

AppShield and its features are enabled by default when you install it. You may want to disable it in one or more environments for **testing purposes**.

* To disable AppShield functionalities in one or more environments, edit the Extensibility Configuration settings **in LifeTime** for the environment. Disabling the plugin in the development environment, for example, lets you run the app in emulators or debug the app.
* To disable AppShield functionalities globally, edit the Extensibility Configuration settings **in Service Studio**. LifeTime copies configuration from Service Studio to environments during deployment. 

<div class="info" markdown="1">

When working with AppShield JSON for Extensibility Configuration, keep in mind:

* Specific settings in Extensibility Configuration override global Extensibility Configuration settings.
* Extensibility Configuration settings in LifeTime override the Extensibility Configuration in Service Studio.

</div>

Here is an example of the JSON for Extensibility Configurations. You can use different sections for iOS and Android.

```
{
    "preferences": {
        "global": [
            {
                "name": "DisableAppShielding",
                "value": "false"
            },
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "false"
            }
        ],
        "android": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            }
        ],
        "ios": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            }
        ]
    }
}
```

### Configuration reference

These are the values available in the AppShield configuration JSON.

| Value                        | Type       | OS           | Description                                                            |
| ---------------------------- | ---------- | ------------ | ---------------------------------------------------------------------- |
| DisableAppShielding          | boolean    | iOS, Android | Activates or deactivates App Shield.                                |
| AllowScreenshot              | boolean    | iOS, Android | If set to true, allows users to take screenshots of the app.           |
| AllowJailbrokenRootedDevices | boolean    | iOS          | If set to true, allows users to run the app on the jailbroken devices. |
| global                       | JSON value | iOS, Android | Settings in this section apply to both Android and iOS builds.         |
| android                      | JSON value | Android      | The key denoting values that apply to the Android devices.             |
| ios                          | JSON value | iOS          | The key denoting values that apply to the iOS devices.                 |


## Obfuscation

In the current version, native code from the shell and supported plugins are obfuscated. A crash from the core OutSystems components generates an obfuscated stack trace.

## Limitations

AppShield has the following limitations. 

### General

Non-specific limitations.

* On iOS the plugin doesn't block user-initiated screenshots, it only notifies the app that a screenshot was taken. OutSystems currently doesn't support this event. However, AppShield blocks taking screenshots of the iOS App Switcher.
* After MABS creates a build, with the AppShield plugin active, and signs the build, you can't sign that build again manually because the app would recognize that as signs of tampering.

### Obfuscation

The limitations that are specific to the obfuscation.

<div class="info" markdown="1">

We know how important obfuscation of JavaScript is to our customers. Our development team is working hard on delivering JavaScript obfuscation in one of the upcoming versions of AppShield.

</div>

* The plugin obfuscates only the supported OutSystems mobile plugins.
* The plugin obfuscates native Android logs in Service Center. You need to use an external tool to deobfuscate the logs.
* JavaScript files obfuscation isn't supported. OutSystems provides guidance to obfuscate JavaScript.
* Native iOS bitcode obfuscation isn't supported.
* You need to contact Support to get the mapping files.


## How to retrace Android obfuscated logs

The purpose of the obfuscation is to make the app harder to reverse-engineer. During the obfuscation process, the platform creates a mapping with the old and new names of methods and classes.

In an obfuscated app, an error stack trace might look like this:

![Obfuscation example](images/obfuscated.png?width=600)

**Prerequisites**

These are the prerequisites to deobfuscate the logs.

* Android Studio on Mac, Linux, or Windows.
* The mapping.txt file from the build. Please reach Support and request the mapping file. 
* A stack trace to deobfuscate and retrace.

**Steps**

1. Have the mapping file ready.
1. Locate the proguard tools, located under your Android SDK folder, usually in `$ANDROID_HOME/tools/proguard/bin`.
1. Inside, you should have the retrace cli, or the proguardgui.

    With **retrace cli**. Use the retrace command, followed by the path to the mapping file and the file with the stack trace. Or, run the command without the stack trace file and then paste the log content. 

    With **proguardgui**. Click the **ReTrace** button in the left pane and locate your mapping file. Paste the obfuscated stack trace and click **ReTrace!**.

    ![Proguard UI](images/proguard-log.png?width=600) 

### Known limitations

The lines that for parsing can't have the timestamp, which is what logcat tools usually produce. Instead, the lines must start with the **at** keyword.

### More information

For more information, see:

* [Write and View Logs with Logcat](https://developer.android.com/studio/debug/am-logcat#format)
* [ReTrace](https://www.guardsquare.com/en/products/proguard/manual/retrace)
* [ProGuard](https://www.guardsquare.com/en/products/proguard)