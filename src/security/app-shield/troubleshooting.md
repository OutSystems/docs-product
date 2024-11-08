---
summary: 
tags: support-application_development; runtime-mobile;
locale: en-us
guid: 51175e8a-0f68-472a-928b-96b81646011a
app_type: mobile apps
platform-version: o11
figma: 
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

### iOS

On iOS, it isn't possible to have such logs. Thus, the best way to troubleshoot the reason for an app crash from AppShield protection features is to implement the **[ExitOnURL](./ExitOnUrl.md)** configuration to inform the user of the reason. The **ExitOnURL** lets you define an **Exit URL** which the app opens in the default browser. It also lets you explain the issue to the app users.

## Shutdown reasons

Although unclear, these logs contain an Hexadecimal value which is the `Reason` for the exit to happen. Here's a list of codes for the `Reason`:

### Android

A list of reasons for app shutdown in Android devices.

| ExitOnUrl (Decimal)| Log (Hex) | Explanation                                                  |
| ------- | ------- | ------------------------------------------------------------------------- |
| 00      | 00      | Device is rooted                                                          |
| 01      | 01      | Application is modified or repackaged<br />**Note**: Removed from ExitOnUrl functionality from AppShield version 1.4.0 because it was not guaranteed to be triggered.|
| 02      | 02      | Application is being run in an emulator<br />**Note**: Removed from ExitOnUrl functionality from AppShield version 1.4.0 because it was not guaranteed to be triggered.|
| 03      | 03      | Java debugger attached to app                                             |
| 04      | 04      | Untrusted keyboard detected                                               |
| 05      | 05      | Untrusted screen reader detected                                          |
| 06      | 06      | Native code hooks, possibly inserted by malicious app                     |
| 08      | 08      | Shield could not read configuration file                                  |
| 09      | 09      | Problem with Native Debugger Protection                                   |
| 25      | 19      | Problem initializing Shield                                               |
| 26      | 1a      | Developer Options enabled on device                                       |
| 27      | 1b      | Untrusted Installer found on device                                       |
| 32      | 20      | App received termination signal                                           |
| 33      | 21      | Application crashed outside of Java-code, either native library or Shield |
| 34      | 22      | Hooking frameworks detected                                               |
| 35      | 23      | Native debugger prevention not possible on this device                    |
| 50      | 32      | App started from a private space or work profile                          |

### iOS 

A list of reasons for app shutdown in iOS devices.

| ExitOnUrl (Decimal)| Explanation   						  |
| ------- | ------------------------------------------------- |
| 00      | Device is jailbroken/rooted                       |
| 01      | Application is being debugged                     |
| 02      | Application is modified or repackaged             |
| 03      | A screenshot of the application was taken         |
| 04      | An injected library was found in the process      |
| 05      | A hooking framework was found in the process      |
| 06      | A screen recording of the application was started |
| 08      | Running on emulator                               |
| 09      | Running with Developer Mode enabled               |

