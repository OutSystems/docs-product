---
summary: Troubleshoot issues that can arise while connecting your mobile device to your PC for debugging purposes.
tags: runtime-mobile; support-application_development; support-Mobile_Apps
locale: en-us
guid: dc4e00b1-34e4-4bf0-9fa6-b63c6d4f6719
---

# Troubleshoot Debugger Connection Issues

<div class="info" markdown="1">

Use Service Studio 11.5.44.2557 or later to debug the mobile apps if you generate them with MABS 6.

</div>

When trying to debug a mobile application using Google Chrome or a real device some issues can arise, like a firewall blocking local ports or a device not being discovered by Service Studio.

Below you can find a list of the most common problems that you may find when you are starting a mobile app debug session, and suggestions for fixing them.

## Issues Related With Unavailable Local Ports

The mobile app debugger feature of Service Studio requires one or two available local ports according to the debugging target:

When debugging on an Android device or in Google Chrome
:   One available port in the development machine starting at port 9222. If this port is unavailable, Service Studio checks port 9223, and so on.

When debugging on an iOS device
:   Two available local ports in the development machine starting at port 9221. If this port is unavailable, Service Studio checks port 9222, and so on.

If there are no available ports because they're in use or they're blocked (for example, by a firewall), you can't debug your mobile app in Service Studio.

## Issues While Connecting an Android Device

Check the following sections for more information on how to solve these issues:

* [USB/Android Debugging not enabled in device](<#usbandroid-debugging-not-enabled-in-device>)
* [Device not recognized by Windows](<#device-not-recognized-by-windows>)
* [Incompatible USB mode selected in device](<#incompatible-usb-mode-selected-in-device>)
* [USB Debugging was not allowed in device](<#usb-debugging-was-not-allowed-in-device>)
* [More than one Android device is connected to your PC](<#more-than-one-android-device-is-connected-to-your-pc>)

### USB/Android Debugging not enabled in device { #usbandroid-debugging-not-enabled-in-device }

For the device to be detected by Service Studio, you should start by having the USB debugging (or Android Debugging) option enabled.

1. Navigate to the **Developer options** section inside the **Settings** and enable the **USB debugging** option.

    ![](<images/device-usb-debugging.png>)

    *Note:* If you don't have the **Developer options** section in **Settings**, check how to [enable **Developer options**](<https://developer.android.com/studio/debug/dev-options.html#enable>) on your device.

### Device not recognized by Windows { #device-not-recognized-by-windows }

After ensuring that the USB debugging option is enabled, you should check if the device is detected by Windows and its drivers are correctly installed:

1. Open **Control Panel**.

1. Navigate to the **Hardware and Sound** category.

1. Open **Device Manager**, located under **Devices and Printers**.

1. If your device is listed under **Other devices**, you need to install the correct drivers before proceeding:

    ![](<images/device-unrecognized.png>)

To help Windows correctly detect the device, follow [this guide](<https://developer.android.com/studio/run/oem-usb.html>) to install the drivers provided by the manufacturer.

If after following the guide mentioned above Windows still fails to recognize the device properly, try using the drivers provided by Google by taking these steps:

1. Download the [Google USB Driver ZIP file](<https://developer.android.com/studio/run/win-usb.html>) and extract it (to the Desktop, for example).

1. Right-click on your device and select **Update Driver Software...**.

    ![](<images/device-update-driver.png>)

1. Choose **Browse my computer for driver software**.

    ![](<images/device-browse-for-driver.png>)

1. Choose **Let me pick from a list of device drivers on my computer**.

    ![](<images/device-pick-driver-from-list.png>)

1. Select **Show All Devices** and click **Next**.

    ![](<images/device-show-all-devices.png>)

1. Choose the option **Have Disk...**, browse to the `usb_driver` folder located on the extracted folder and click **OK**.

    ![](<images/device-install-from-disk.png>)

1. Select **Android ADB Interface** and click **Next**.

    ![](<images/device-android-adb-interface.png>)

1. Confirm the installation of the driver by pressing **Yes**.

    ![](<images/device-driver-warning.png>)

1. Install the driver by choosing **Install**.

    ![](<images/device-driver-install-prompt.png>)

When the installation completes, press **Close** and check that the device appears in Device Manager:

![](<images/device-install-success.png>)

### Incompatible USB mode selected in device { #incompatible-usb-mode-selected-in-device }

The USB mode which the device is configured to use when connecting to a PC can also cause issues in the device detection process.

Depending on the version of Android and the manufacturer of the device, this option can be in different places.
First of all, check if you have any notification referring to the USB mode, like the ones below:

![](<images/device-usb-mode-1.png>)

![](<images/device-usb-mode-2.png>)

![](<images/device-usb-mode-3.png>)

If you find these options, try to switch between them (`MTP`, `PTP` and `Camera` modes), disconnecting and reconnecting the device to the PC, and retrying the device discovery in Service Studio.


### USB Debugging was not allowed in device { #usb-debugging-was-not-allowed-in-device }

Whenever an Android device is connected to a PC, a request to allow USB Debugging is shown on the device. This request should be accepted so that Service Studio can communicate with the device.

If you get a pop-up on your device like the one below, just tap **OK** and try again on Service Studio to detect the device:

![](<images/device-allow-usb-debugging.png>)

### More than one Android device is connected to your PC { #more-than-one-android-device-is-connected-to-your-pc }

Only one device from each platform (Android/iOS) can be connected to the PC for the device discovery process to run successfully. 

Ensure that you only have one Android device connected to your PC.


## Issues While Connecting an iOS Device

Check the following sections for more information on how to solve these issues:

* [iTunes is not installed on your PC](<#itunes-is-not-installed-on-your-pc>)
* [Web Inspector is not enabled on your device](<#web-inspector-is-not-enabled-on-your-device>)
* [PC is not trusted for debugging](<#pc-is-not-trusted-for-debugging>)
* [More than one iOS device is connected to your PC](<#more-than-one-ios-device-is-connected-to-your-pc>)

### iTunes is not installed on your PC { #itunes-is-not-installed-on-your-pc }

One of the requirements for the debugger to work with iOS devices is the iTunes installation on the machine where Service Studio is executing. Please make sure that you have it installed on your machine before trying to perform any debug session with an iOS device.

[Download the latest version](<https://www.apple.com/itunes/download/>) from Apple's website.

_Note:_ If you installed iTunes from the Microsoft Store you must have iTunes running to be able to debug OutSystems mobile apps in iOS devices.

### Web Inspector is not enabled on your device { #web-inspector-is-not-enabled-on-your-device }

<div class="info" markdown="1">

For checking network requests in iOS apps built with MABS 6.0 and later, use the [build-in network inspection tool](../inspect-http-requests-mobile.md).

</div>

To ensure that your device is correctly detected you should make sure that the Web Inspector is enabled. 

Do the following:

1. On your iOS mobile device tap Settings > Safari > Advanced.

1. Make sure that the "Web Inspector" option is turned **on**.

    ![](<images/ios-web-inspector.png>)

### PC is not trusted for debugging { #pc-is-not-trusted-for-debugging }

The final step to setup your device to be ready for debugging is to trust the PC so it can communicate with the device. To do so, tap **Trust** when the following pop-up appears on your device:

![](<images/device-trust-computer.png>)

Check [Apple Support](<https://support.apple.com/en-us/HT202778>) for more information on trusted computers.

### More than one iOS device is connected to your PC { #more-than-one-ios-device-is-connected-to-your-pc }

You can only connect one device from each platform (Android/iOS) to the PC for the device discovery process to run successfully.

Ensure that you only have one iOS device connected to your PC.


## Issues During App Detection by Service Studio

When starting a new debug session using a device, and after the device has been correctly detected, Service Studio starts to actively look for the mobile app that you are debugging.

If you find issues during the app detection step (for example, the detection is taking too long), make sure you generated the mobile app with the `Debug` Build Type for Android and `Development` Build Type for iOS.

If your app is still not detected, try performing each of the following steps in your device and check if any of them solves your problem:

* Close all other running OutSystems mobile apps.
* Close any browser app that could be running.
* Close all running apps.
