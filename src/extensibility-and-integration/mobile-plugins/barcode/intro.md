---
summary: Learn how to use the Barcode Plugin to scan barcodes and QR codes.
tags: runtime-mobile; support-application_development; support-Mobile_Apps;
---

# Barcode Plugin

The Barcode Plugin works with native mobile apps and lets users of the app scan 1D and 2D barcodes. Set the options in the plugin to customize the scanner, to add instructions, or change camera direction.

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a demo app.

</div>

## Demo app

OutSystems provides a demo app to help you learn how to use this plugin. Install the [Barcode Demo App](https://www.outsystems.com/forge/component-versions/1403) from Forge and then open the app in Service Studio. The demo app contains logic for common use cases, that you can examine and create in your apps. For example, how to:

* Scan a code
* Use the a predefined UI block
* Create a settings page

![demo app main screen](images/sample-app-main.png?width=400)

Here is the settings screen:

![demo app settings screen](images/sample-app-settings.png?width=400)

## Creating a user interface

To set up the user interface, see an example for the [Camera plugin](../camera/intro.md#creating-a-user-interface). You can use a similar approach in your app with the Barcode plugin.

## Creating logic to scan a code

To create the logic to scan for barcodes, follow these steps in Service Studio:

1. Go to **Logic** > **Client Actions** > **BarcodePlugin**.

2. To open the camera in your app for scanning, drag the **ScanBarcode** action to the flow.

    ![Client action to scan a barcode](images/client-action-ss.png?width=400)

    In the **ScanBarcode** action you can set scan instructions, back or front camera, or UI orientation, and enable the scan button. For more information about the **ScanBarcode** action, see [Scanning options](#scanning-options).

3. Check the **ScanResult** text for the result of the scan.

To prevent errors, it's a good practice to first check if the plugin is available using the action **CheckBarcodePlugin**. To confirm the device can read the barcodes, verify that the value of **ScanBarcode.Success** is true. See the [sample app](#sample-app) for the examples.

## Reference

More information about the plugin.

### Supported barcode formats

The following list shows which barcode formats the plugin can read.

* UPC-A
* UPC-E
* EAN-8
* EAN-13
* ISBN-10
* ISBN-13
* ISBN-13 Dual Barcode
* Code 39
* Code 93
* Code 128
* GS1 DataBar
* ITF-14
* Codabar
* QR Code
* PDF 417
* Data Matrix
* Aztec Code

### Scanning options

Here is the list of the actions you can use in the plugin actions.

| Action                   | Description                                   | 
| ------------------------ | --------------------------------------------- | 
| **ScanInstructions**    | Displays the scanning instructions. |
| **CameraDirection**    | Select the front or back camera as default when triggering a new scan action. |
| **ScanOrientation**    | Allows you to set the Scan UI to Adaptive, which detects your device's orientation, Landscape, or Portrait mode. |
| **ScanLine**    | If set to true, enables a white line-of-sight that sweeps the screen when scanning the code. |
| **ScanButton**    | If set to true, enables a scan button in the Scan UI. Pressing the button triggers the scan action, instead of scanning automatically when framing the code. |

The Barcode Plugin uses a Cordova plugin, and for more information check [cordova-outsystems-barcodescanner](https://github.com/OutSystems/cordova-outsystems-barcodescanner).

## Known issues

What follows is the list of known issues and workarounds.  

### Reading a PDF147 can crash an app

**Applies to iOS only.**

Reading a PDF147 barcode can crash an iOS app. OutSystems is working on a potential fix.

### Poor scanning results with the front camera

On some devices with a low-resolution front camera, the app doesn't scan barcodes well. For best results use the back camera. The back camera has higher resolution and can focus better on a barcode.   