---
summary: Learn how to use the Barcode Plugin to scan barcodes and QR codes.
tags: runtime-mobile; support-application_development; support-Mobile_Apps;
---

# Barcode Plugin

Use the Barcode Plugin in your apps to let users scan barcodes and QR codes. 

<div class="info" markdown="1">

See [Adding plugins](../intro.md#adding-plugins) to learn how to install and reference a plugin in your OutSystems apps, and how to install a sample app.

</div> 

To let users scan barcodes and QR codes in the app, do the following in Service Studio:

1. Go to **Logic** > **Client Actions** > **BarcodePlugin**.

1. Drag the **ScanBarcode** action to the flow. This action opens the camera in the app for scanning.

    ![Client action to scan a barcode](images/client-action-ss.png?width=400)

1. Check the **ScanResult** value for  the result of the scan. 

## Additional configurations 

Barcode Plugin provides some additional configurations to improve the experience for the end users when they scan a new barcode or QR code. 

You can set up the following configurations in the **ScanBarcode** client action: 

* **Helper Title**: The title of the scanner. Android only.
* **Helper Instructions**: The instructions for the scanning. Android only.
* **Camera**: There are two options for the camera, **back** and **front**. The default value is **back**.
* **Flash**: There are three options for the flash, **auto**, **off** and **on**. The default value is "auto".
* **DrawSight**: If set to **True**, draws a red line of sight in the center of the scanner view. The default value is **True**. 
