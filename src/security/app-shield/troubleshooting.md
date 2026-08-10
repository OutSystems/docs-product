---
summary: Troubleshoot AppShield crashes for mobile apps on OutSystems 11 (O11) by analyzing crash logs for Android and configuring ExitOnURL for iOS.
tags: support-application_development, runtime-mobile
locale: en-us
guid: 51175e8a-0f68-472a-928b-96b81646011a
app_type: mobile apps
platform-version: o11
figma:
coverage-type:
  - unblock
audience:
  - Developer
outsystems-tools:
  - none
isautopublish: true
---
# Troubleshooting AppShield crashes

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

## Crash logs

When AppShield detects a security threat to the app, it either blocks it or, in some scenarios, immediately **crashes the app** to close all windows at malicious attempts.

### Android

When a crash occurs on **Android**, the device log should contain an entry that can help identify the reason of the crash.
These crash logs are usually in the following format:

```
--------- beginning of crash
E  FATAL EXCEPTION: 
Process: com.outsystems.myapp, PID: 25983
i.aw: 1a
 at i.ap.b(Unknown Source:69)
 at i.ap.a(Unknown Source:0)
```

In the scenario, the line `i.aw: 1a` includes the reason for the crash which has the code `1a` - `Developer Options enabled on device`.
The first part of the line varies from app to app, and the reason code is next to the colon (:).

<div class="info" markdown="1">

AppShield may cause shielded Android apps to fail Google Play Store and 16KB page size compatibility reviews. This happens because Google tested the apps on rooted devices and emulators and AppShield exits the app when it detects these environments as security risks.

If a shielded app fails one of these reviews, check the stack trace provided by Google. If the crash resembles
`gxffgth.jMo: XX` then the app exited due to its configured security policy.

In this example, `XX` is the exit code. For a full list of exit codes, refer to the [Shutdown reasons](#shutdown-reasons) section. The most common codes in this context are `00` (rooting detection) and `02` (emulator detection).

If this occurs, contact Google directly and explain that the app exited for security reasons and shouldn't be tested on a rooted device or emulator during the review process.

</div>

### iOS

On iOS, it isn't possible to have such logs. Thus, the best way to troubleshoot the reason for an app crash from AppShield protection features is to implement the **[ExitOnURL](./ExitOnUrl.md)** configuration to inform the user of the reason. The **ExitOnURL** lets you define an **Exit URL** which the app opens in the default browser. It also lets you explain the issue to the app users.

## Shutdown reasons

Although unclear, these logs contain an Hexadecimal value which is the `Reason` for the exit to happen. Here's a list of codes for the `Reason`:

### Android

A list of reasons for app shutdown in Android devices.

| ExitOnUrl (Decimal) | Log (Hex) | Explanation |
| ------- | ------- | ------------------------------------------------------------------------- |
| 0 | 00 | Device is rooted |
| 1 | 01 | Application is modified or repackaged.<br />**Note**: Removed from AppShield version 1.4.0 because it was not guaranteed to be triggered. |
| 2 | 02 | Application is being run in an emulator.<br />**Note**: Removed from AppShield version 1.4.0 because it was not guaranteed to be triggered. |
| 3 | 03 | Java debugger attached to app |
| 4 | 04 | Untrusted keyboard detected |
| 5 | 05 | Untrusted screen reader detected |
| 6 | 06 | Native code hooks detected, possibly inserted by a malicious app |
| 8 | 08 | AppShield could not read the configuration file |
| 9-17 | 09-11 | Problem with Native Debugger Protection |
| 19 | 13 | Problem initializing AppShield |
| 20 | 14 | App received a termination signal |
| 21 | 15 | Application crashed outside of Java code, either in a native library or AppShield |
| 22 | 16 | Hooking frameworks detected |
| 23 | 17 | Native debugger prevention not possible on this device |
| 27 | 1B | Untrusted installer found on device |
| 29 | 1D | Application launched via a virtual space application |
| 31 | 1F | Emulated input detected |
| 32 | 20 | Application launched in a Private Space or Work Profile |
| 33 | 21 | Device bootloader is unlocked |
| 34 | 22 | Tapjacking event detected |
| 35 | 23 | Code injected into the application process |
| 37 | 25 | Device connected to a VPN |

### iOS

A list of reasons for app shutdown in iOS devices.

| ExitOnUrl (Decimal) | Explanation |
| ------- | ------------------------------------------------- |
| 00 | Device is jailbroken/rooted |
| 01 | Application is being debugged |
| 02 | Application is modified or repackaged |
| 03 | A screenshot of the application was taken |
| 04 | An injected library was found in the process |
| 05 | A hooking framework was found in the process |
| 06 | A screen recording of the application was started |
| 07 | iOS app running on macOS. |
| 08 | Running on emulator |
| 09 | Running with Developer Mode enabled |
