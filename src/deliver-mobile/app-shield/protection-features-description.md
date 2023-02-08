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

The following page intends to provide additional detail on each protection feature of the AppShield plugin. It is divided in three sections:

* General - includes protection features that are common to Android and iOS apps;
* Android - includes protection features that are specific to Android apps;
* iOS - includes protection features that are specific to iOS apps;

## General

Protection available for both iOS and Android apps.

### Root / Jailbreak detection

* **What it does:** Checks if the device has privilege escalation enabling features, by evaluating artifacts that provide high levels of certainty that the device is rooted.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** Yes.This protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)

### Repackaging detection

* **What it does:** Determines if the application bundle in its entirety has either been binary modified/manipulated or has been signed with a different keystore than the one originally used.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** No.

### Code injection protection

* **What it does:** Performs checks to detect attack vectors used by hooking frameworks such as Frida, by using methods such as in memory scanning within the application address space.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** No.

### Debugger protection

* **What it does:** Detects and blocks debuggers. Blocking of native (such as lldb and gdb) and Dalvik-based debuggers is automatic when debugger protection is enabled.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** No.

## Android

Protection available specific to Android apps.

### Code Obfuscation

* **What it does:** Applies native mobile code obfuscation. This includes both encryption and scrambling of static data.
* **What happens:** Hinders readability of the native code of your application for external agents or attackers.
* **Is it configurable?:** Yes, you can enable/disable code obfuscation and in the case of enabling you should define custom obfuscation rules that suits your application. For more information on this, see [Creating custom obfuscation rules](obfuscate-custom-rules.md)

### Emulator detection

* **What it does:** Prevents the application from running in emulators.
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** No.

### Key Logger protection

* **What it does:** Applies a combination of protection features to block key logging. The first leans on the Screen reader blocking (see [Screen Reader Protection](#android-screen-reader) to prevent key logging through screen readings. The second uses screenshot protection to prevent key logging through screenshot analysis. (see [Screenshot protection](#android-screenshot)).

### Screen Reader detection { #android-screen-reader }

* **What it does:** Blocks screen readers which are commonly used by malware trying to abuse the accessibility permissions of a device.
* **What happens:** On positive detections blocks screen readers.
* **Is it configurable?:** Yes. Currently, this feature is disabled by default. This is due to the fact that activating Screen Reader detection might affect apps using accessibility features. To activate this feature you will need to add the extensibility AppShield_blockUntrustedScreenreaders with the value “1”, see example below:

{
    "name": "AppShield_blockUntrustedScreenreaders",
    "value": "1"
},

After activating this feature you will block all screen readers (other than the system ones);

### Task hijacking protection

* **What it does:** Prevents overlay attacks that use attack vectors such as task affinity hijacking and reflection calls to attack multiple targets simultaneously (Strandhogg 1 and Strandhogg 2).
* **What happens:** On positive detections blocks the app from running. If **ExitOnURL** is configured, an URL, which the app developer can use to inform the app end-user, is opened upon blocking the app. See [Configuring an exit URL for a blocked app](ExitOnUrl.md) 
* **Is it configurable?:** No.

### Screenshot protection { #android-screenshot }

* **What it does:** Blocks the creation of both user and system screenshots.
* **What happens:** When trying to mirror the screen or trying to take screenshots of the application, a black screen is shown instead.
* **Is it configurable?:** Yes, this protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)


## iOS

Protection available specific to iOS apps.


### Screen Mirroring detection

* **What it does:** Prevent external screens (connected through an adapter or through Airplay) from mirroring the application window often used for social engineering attacks and external scraping of screen data.
* **What happens:** On positive detections blocks the screen mirroring functionality.
* **Is it configurable?:** No.


### Screenshot protection

* **What it does:** Blocks the creation of system screenshots.
* **What happens:** On positive detections blocks system screenshots.
* **Is it configurable?:** Yes, this protection feature can be disabled. See [AppShield Configuration](intro.md#configuration)




