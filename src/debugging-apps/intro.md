---
summary: OutSystems 11 (O11) provides advanced debugging features in Service Studio for detailed app analysis and troubleshooting.
tags: debugging, breakpoints, native mobile app debugging, pwa (progressive web app), debugger ui
locale: en-us
guid: 78def0b5-863d-4d58-8ea0-bb9f28bf1ef8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:129
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - debug-troubleshoot-app-logic
---

# Debugging apps

Debug your app in Service Studio by pausing the execution at [breakpoints](<breakpoints.md>), specific points in a module, and then running the logic step-by-step. This lets you find any issues in your logic design.

The [Debugger tab](<debugger-ui-reference.md>) shows app information like variable and runtime values. It also shows the current debugging context (current [thread](<threads.md>), event name, UI flow, screen and action, when applicable. Use the debugger commands available in the Debugger Toolbar and in the Debugger menu.

![Screenshot of the initial debugger interface in OutSystems Service Studio](images/debugger-intro-ss.png "Debugger Introduction in Service Studio")

## How to debug your app

To debug your app, do the following in Service Studio:

1. Click the 1-Click Publish button to save the latest changes in the module before debugging. 

1. Set one or more [breakpoints](<breakpoints.md>) in the module you're debugging.

1. Before debugging a **native mobile app**, choose a debugging target in the [Debugger tab](<debugger-ui-reference.md>): Android, iOS, or Google Chrome which emulates a device. The section [Mobile Debugging Scenarios](<#mobile-debugging-scenarios>) includes further details about the different targets. If you're debugging a **mobile app distributed as a PWA**, select **Emulate using Google Chrome** in **Debugger** > **Debug Setup**. 

    ![Debugger tab in Service Studio showing options for native mobile app debugging](images/debugger-tab.png "Debugger Tab in Service Studio")

1. Start debugger by clicking the **Start Debugging** button in the [Debugger tab](<debugger-ui-reference.md>) or by selecting **Debug in the Public Area** in the Debugger menu. When you're debugging mobile apps using the Google Chrome target, Service Studio opens a dedicated Chrome browser instance for debugging only.

    Note: To also open a browser when starting a debug session in a **web application**, check the **Open in new browser window** option in the **Debug Setup** tab.

    ![Debug setup options in Service Studio for web applications](images/debug-setup-tab-web.png "Debug Setup for Web Applications")

1. Do some tasks in the module, up to a point when the execution runs into a breakpoint and suspends.

1. When you switch to the Service Studio window, the flow or screen containing the element with the breakpoint shows on the canvas. Service Studio selects the element with the breakpoint and marks is with the ![Icon indicating an active debug request in OutSystems Service Studio](images/overlay-active-request.png "Debug Icon") debug icon.

1. The execution context shows in the **Threads** tab of the **Debugger** tab, marked with the ![Icon indicating an active debug request in OutSystems Service Studio](images/overlay-active-request.png "Debug Icon") current thread icon, showing the current execution stack of the module elements. The **Debugger** tab also shows additional information you can explore.

1. After analyzing the runtime values at that execution point, you can continue running the app by:

    * Selecting one of the commands available for advancing the execution of the application logic: ![Continue command icon in the debugger toolbar of OutSystems Service Studio](images/toolbar-button-continue.png "Continue Command Icon") **Continue**, ![Step Over command icon in the debugger toolbar of OutSystems Service Studio](images/toolbar-button-step-over.png "Step Over Command Icon") **Step Over**, ![Step Into command icon in the debugger toolbar of OutSystems Service Studio](images/toolbar-button-step-into.png "Step Into Command Icon") **Step Into** or ![Step Out command icon in the debugger toolbar of OutSystems Service Studio](images/toolbar-button-step-out.png "Step Out Command Icon") **Step Out**. The execution point advances according to the command you run.

    * Right-clicking an element on the canvas (or in the module tree) and selecting the **Continue To Here** option in the context menu. The execution continues until it reaches that element on the canvas.

In some scenarios you need to [debug some functionality exposed by another module](<debug-producer-modules.md>) (called a producer module).

While developing **Traditional Web apps** you can also [debug modules in your Personal Area](<public-personal-areas.md>). This lets you test your changes separately from other developer's changes in the same module.

## Mobile debugging scenarios { #mobile-debugging-scenarios }

There are different ways of debugging a mobile app that help you discover, understand, and fix issues. You can debug your mobile app in one of the following ways:

* **Emulate the mobile app using the Google Chrome browser on your PC**

    Use the Chrome browser on your computer to debug your mobile app if you don't need to execute native plugins, as native plugins can't run on a personal computer. This option is convenient to test the logic of the app. However, to check the performance or experience of the mobile app, test your app on a real mobile device. Also, consider this scenario if all the native plugins in the mobile app have action wrappers defined that return mock data when the plugin isn't available. For more information, refer to the best practices topic on [creating wrapper actions for native plugins](https://success.outsystems.com/documentation/best_practices/development/outsystems_mobile_best_practices/#Define-Fallbacks-for-Your-Native-Plugins).

* **Install the mobile app on a device**

    Test the mobile app directly on a device as your users would run it. It's the best place to test the performance and experience of your app. You can do it on an iOS or Android device. Generate the native app package for your app in Service Studio using the Debug (Android) or Development (iOS) build type, install it on the device, and follow the steps below according to your mobile device platform and computer operating system.

    * **To test a mobile app on an iOS device running on Service Studio:**
    
        1. On your **Windows computer**, install [iTunes](<https://www.apple.com/itunes/download/>) (this step is not necessary if you're running Service Studio on a MacOS computer).

        1. On your **device**, turn the **Web Inspector** option **On**. 
        
            For detailed instructions, refer to [Troubleshoot Debugger Connection Issues](<troubleshoot-debugger-connection.md#web-inspector-is-not-enabled-on-your-device>).

        1. Connect your device to the computer using a USB cable.

            The **Trust This Computer** popup is displayed on your device.

        1. Click **Trust** to allow debugging on the device.
    
    * **To test a mobile app on an Android device**:
    
        1. On your **device**, turn [USB debugging On](<https://developer.android.com/studio/debug/dev-options.html#enable>).

        1. Connect your mobile device to the computer using a USB cable.

            The **Allow USB debugging** popup is displayed.

        1. Click **Allow** to allow debugging on your device.

For more information, refer to [Troubleshoot Debugger Connection Issues](<troubleshoot-debugger-connection.md>).

If you need to troubleshoot app crashes, a plugin or check the native code of apps, debug your apps with the mobile platform's native tools, such as Android Studio for Android and Xcode for iOS. Before debugging using the native tools, you must generate a mobile package with `Debug` (Android) or `Development` (iOS) build type.

<div class="info" markdown="1">

For more information, refer to [Solve Common Mobile App Development Issues](<../monitor-and-troubleshoot/solve-common-mobile-app-development-issues.md>) and [Best Practices](<https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices>). These resources have useful tips that might save you some troubleshooting time.

</div>

## Working with dates and times

When debugging an app and checking the values of the Date Time data type, keep in mind the following:

* During debugging, Service Studio shows UTC date and time in the debugger.
* In the client UI, the date and time are in the timezone of the client.
* On the server, the date and time are in the timezone of the server.

You can read more about timezones in [Available Data Types](../ref/data/data-types/available-data-types.md#date-time-notes).

## Debugging in Proxy Scenarios and Farm Environments

In environments with multiple front-end servers behind a load balancer or proxy server, debugging may encounter issues due to unmatched origin IP addresses.

For Traditional Web Applications, adding the proxy IP address to the Trusted Proxy addresses in Service Center > Administration > Security > Network Security resolves this issue, enabling proper debugging.

It's important to note that debugger functionality remains unaffected for Mobile and Reactive Applications, as breakpoints are honored regardless of origin IP addresses.

In farm setups, debugging can be challenging as user connections to specific front-ends cannot be guaranteed. This necessitates ensuring that the load balancer redirects users based on immutable criteria for effective debugging. 
Alternatively, manual distribution of users across front-ends or using DNS load balancing can also help manage debugging challenges.

<div class="info" markdown="1">

Proxy scenarios are supported in self-managed environments. However, there is no option to add Trusted proxy addresses in OutSystems Cloud installations.

</div>

## Debugging with redirect rules

When debugging an app that has a redirect rule (e.g., `oldurl/module -> newurl/module`), always connect Service Studio to the **new URL** (`newurl`). Attempting to connect to the old URL may result in debugging issues.
