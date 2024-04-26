---
summary: Provide additional detail to AppShield users on each of the AppShield's protection features;
locale: en-us
guid: 7696c5bc-71ab-4eeb-ac4c-2805bd79f5b1
app_type: mobile apps
platform-version: o11
figma:
---

# AppShield protection features

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

This page provides additional detail on each protection feature of the AppShield plugin.
There are three sections:

* General - includes protection features common to Android and iOS apps;
* Android - includes protection features specific to Android apps;
* iOS - includes protection features specific to iOS apps;

## General

Protection available for both iOS and Android apps.

### Root/Jailbreak detection

* **What it does:** Check if the device has privilege escalation enabling features, by evaluating artifacts that provide high levels of certainty that the device is rooted.
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** Yes. This protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)

### Repackaging detection

* **What it does:** Determines if the application bundle in its entirety has either been binary modified/manipulated or has been signed with a different keystore to the one originally used.
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** No.

### Code injection protection

* **What it does:** Performs checks to detect attack vectors used by hooking frameworks such as Frida, by using methods such as in-memory scanning within the application address space.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** No.

### Debugger protection

* **What it does:** Detects and blocks debuggers. Blocking of native (such as lldb and gdb) and Dalvik-based debuggers is automatic when debugger protection is enabled.
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** No.

## Android

Protection available specific to Android apps.

### Code Obfuscation

* **What it does:** Applies native mobile code obfuscation. This includes both encryption and scrambling of static data.
* **What happens:** Hinders readability of the native code of your application for external agents or attackers.
* **Is it configurable?:** Yes, you can enable/disable code obfuscation. If enabled you should define custom obfuscation rules that suit your application. For more information on this, see [Creating custom obfuscation rules](obfuscate-custom-rules.md)

### Emulator detection

* **What it does:** Prevents the application from running in emulators.
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** No.

### Keylogger protection

* **What it does:** Applies a combination of protection features to block keylogging. The first uses Screen reader blocking (see [Screen Reader Protection](#android-screen-reader) to prevent keylogging through screen readings. The second uses screenshot protection to prevent keylogging through screenshot analysis. (see [Screenshot protection](#android-screenshot)).

### Screen reader detection { #android-screen-reader }

* **What it does:** Detects and blocks untrusted screen readers. Malware usually uses screen readers to abuse the accessibility permissions of a device.
* **What happens:** On positive detections block screen readers. In case the screen reader could not be blocked, it will block the app from running. If **ExitOnURL** is configured, a URL will open when blocking the app. The URL can be used to inform end-users about the occurrence. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) for more information.
* **Is it configurable?:** Yes. By default, this feature is disabled because Screen Reader detection might affect apps that use features for accessibility. To activate it you will need to add the extensibility "BlockUntrustedScreenreaders" with the value “true”. See the following example:

{
    "name": "BlockUntrustedScreenreaders",
    "value": "true"
},

When you activate this feature, all screen readers, except system ones, are blocked. To allow the use of some specific screen reader software, you must add the  "AddTrustedScreenReaderSigner" extensibility with the hash value of the screen reader software that you want to allow. You can allow multiple screen reader software by adding "AddTrustedScreenReaderSigner" as many times as needed. See the following example:

{
    "name": "AddTrustedScreenReaderSigner",
    "value": "16a14259f274eaafc190a0fcffa3a59c822b99d09f259e0ed3147c01e24b0179"
},
{
    "name": "AddTrustedScreenReaderSigner",
    "value": "b6bf61861c71c93ad26d84fc3e5e2c1ddb662ffb9f871904be8f5697adb0c5e0"
},

For more information, see [how to get the application hash](#how-to-get-the-application-hash)

### Untrusted keyboard detection { #android-untrusted-keyboard }

* **What it does:** Detects and blocks untrusted keyboards. All system installed keyboards are trusted if the device's firmware is trusted (i.e. the device is not rooted).
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL will open when blocking the app. The URL can be used to inform end-users about the occurrence. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) for more information.
* **Is it configurable?:** Yes. By default, this feature is disabled. To activate it you need to add the extensibility "BlockUntrustedKeyboards" with the value “true”. See the following example:

{
    "name": "BlockUntrustedKeyboards",
    "value": "true"
},

To allow the use of some specific keyboard software, you must add the "AddTrustedKeyboardSigner" extensibility with the hash value of the  keyboard software that you want to allow. You can allow multiple keyboard software by adding "AddTrustedKeyboardSigner" as many times as needed. See the following example:

{
    "name": "AddTrustedKeyboardSigner",
    "value": "ea43e0f05f6ef9e5d16283d90504749d4e03630de7ea792c70f72b9be6c02e5e"
},
{
    "name": "AddTrustedKeyboardSigner",
    "value": "9ac6ca814a945e5aaed450614a99427912f4d2751fb044ea2250e940e1e95e46"
},

For more information, see [how to get the application hash](#how-to-get-the-application-hash)

### Task hijacking protection

* **What it does:** Prevents overlay attacks that use attack vectors such as task affinity hijacking and reflection calls to attack multiple targets simultaneously (such as Strandhogg 1 and Strandhogg 2).
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md)
* **Is it configurable?:** No.

### Screenshot protection { #android-screenshot }

* **What it does:** Blocks the creation of both user and system screenshots.
* **What happens:** When trying to mirror the screen or trying to take screenshots of the application, a black screen is shown instead.
* **Is it configurable?:** Yes, this protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)


## iOS

Protection available specific to iOS apps.


### Screen mirroring detection

* **What it does:** Prevent external screens (connected through an adapter or through Airplay) from mirroring the application window often used for social engineering attacks and external scraping of screen data.
* **What happens:** On positive detections block the screen mirroring functionality.
* **Is it configurable?:** No.


### Screenshot protection

* **What it does:** Blocks the creation of system screenshots.
* **What happens:** On positive detections blocks system screenshots.
* **Is it configurable?:** Yes, this protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)

## How to get the application hash

To get the hash of the application that you want to allow, follow these steps:
- Download the [PubkeyHash.jar here](resources/PubkeyHash.jar)
- Run the PubkeyHash.jar in the terminal with the software apk that you want to allow as a parameter
```sh
> java -jar PubkeyHash.jar app.apk
ea43e0f05f6ef9e5d16283d90504749d4e03630de7ea792c70f72b9be6c02e5e
```

### Obtain the apk from Android phone

One way to get the apk is by downloading it directly from an Android phone.
- On an Android phone, download the software that you want.
* Use the `adb shell pm list packages -f -3` command to find the software path (To filter the list, you can use `| grep <package>`, replacing `<package>` with the package you are looking for).

```sh
> adb shell pm list packages -f -3 | grep swiftkey
package:/data/app/~~wY5boYcbiuH6YBc4e8RL9A==/com.touchtype.swiftkey-CSxEcewNZB_BuMgQV55l8A==/base.apk=com.touchtype.swiftkey
```

- Select the full package path out of the list, which is `package:/data/app/~~wY5boYcbiuH6YBc4e8RL9A==/com.touchtype.swiftkey-CSxEcewNZB_BuMgQV55l8A==/base.apk` in this example and use the following command to download the apk to your computer.

```sh
> adb pull /data/app/~~wY5boYcbiuH6YBc4e8RL9A==/com.touchtype.swiftkey-CSxEcewNZB_BuMgQV55l8A==/base.apk output.apk
```
