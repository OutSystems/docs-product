---
summary: Provide additional detail to AppShield users on each of the AppShield's protection features;
locale: en-us
guid: 7696c5bc-71ab-4eeb-ac4c-2805bd79f5b1
app_type: mobile apps
platform-version: o11
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

After activating this feature you will block all screen readers (other than the system ones);

### Untrusted keyboard detection { #android-untrusted-keyboard }

* **What it does:** Detects and blocks untrusted keyboards. All system installed keyboards are trusted if the device's firmware is trusted (i.e. the device is not rooted).
* **What happens:** On positive detections block the app from running. If **ExitOnURL** is configured, a URL will open when blocking the app. The URL can be used to inform end-users about the occurrence. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) for more information.
* **Is it configurable?:** Yes. By default, this feature is disabled. To activate it you need to add the extensibility "BlockUntrustedKeyboards" with the value “true”. See the following example:

{
    "name": "BlockUntrustedKeyboards",
    "value": "true"
},

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




