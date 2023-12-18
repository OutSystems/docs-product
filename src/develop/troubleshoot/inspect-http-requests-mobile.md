---
summary: Learn how to inspect the HTTP requests for mobile apps built for iOS.
tags: support-application_development; support-Application_Troubleshooting; support-Mobile_Apps; runtime-mobile;
locale: en-us
guid: 2bea2ff9-7655-4952-a00c-2a3f1e3316e9
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:140
---

# Inspect the HTTP requests in Mobile Apps for iOS

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Use the network inspector to see the network activity of your iOS app. The user interface of the network inspector consists of a toolbar and a button that opens the screen with the network traffic details. 

![Screenshot of the network inspector toolbar in an iOS app](images/network-inspector-toolbar.png "Network Inspector Toolbar")

<div class="info" markdown="1">

The network inspector is available in the debug builds created with MABS 6.0 and later. For apps built with the earlier versions of MABS, use Web Inspector in Safari.

</div>


## Enabling and opening the network inspection on iOS

Here is how you can activate and open the network inspection screen on the iOS devices.

1. Start the app. A permission dialog shows.

1. Tap **Allow** in "App would like to send you notifications".

1. Hold three fingers on the screen for about half of a second. You can perform this gesture anywhere in the app at any time.

    ![Illustration of the three-finger gesture to activate the network inspector on an iOS device](images/network-inspector-gesture.png "Activating Network Inspector")

1. The network toolbar shows. Tap **Network**.

    ![Screenshot of the network inspector toolbar in an iOS app](images/network-inspector-toolbar.png "Network Inspector Toolbar")

1. The network debugging is disabled by default on iOS, and you need to enable it. Tap the **Settings** button and activate **Network Debugging** option. Tap **Done** when you finish.

    The settings button:

    ![Close-up of the network inspector settings button in an iOS app](images/network-inspector-settings.png "Network Inspector Settings Button")

    The debugging settings:

    ![Network debugging settings screen on an iOS app with the 'Network Debugging' option highlighted](images/network-inspector-debugging.png "Enabling Network Debugging")

1. Finally, tap the **Network** button to show all requests. Tap a request to see the details.

    ![Screen showing a list of network requests in the network inspector of an iOS app](images/network-inspector-request-list.png "Network Requests List")

<div class="info" markdown="1">

You only need to grant the notification permission and enable the network debugging once. After that, you can use the three-finger gesture to show the toolbar.

</div>

## Notes

* The network inspector feature is available in the **development build** for iOS.
* The requests are only added to the list after the **Network Debugging** option is enabled. If you see an empty list or only a few requests, restart the app and open the network requests screen again.
* Enabling the feature is only valid for that app in that particular device. A fresh install of the app requires that you set the permissions again and turn on the network debugging.
* Dismissing the notification prompt can affect the behavior of the app if it uses notifications for other purposes.