---
tags: runtime-traditionalweb; 
summary: DisplayOnDevice improves the way information is displayed on different devices.
---

# Display on Device 

You can use the Display on Device UI pattern to select what elements are displayed on which device types. With this pattern you can improve the way information is displayed on different devices - computers, tablets, and phones - by specifically specifying which elements show on each of them. 

  ![](<images/displayondevice-image-4.png>)

**How to use the Display on Device UI Pattern**

1. In Service Studio, in the Toolbox, search for `Display on Device`. 

    The Display on Device widget is displayed.

    ![](<images/displayondevice-image-5.png>)
  
1. From the Toolbox, drag the Display on Device widget into the Main Content area of your application's screen.

    ![](<images/displayondevice-image-6.png>)
    
1. Add the required content to the placeholders inside the Display on Device widget. 

    In this example, we add images by dragging the Image widget into the Display on Device widget and selecting an image from the sample OutSystems UI images. 

    ![](<images/displayondevice-image.png>)

1. On the **Properties** tab, from the **Behavior** drop-down list, choose the device types you want to display this widget on.

    These images are displayed on the device types you specify, and not shown for any other devices.

    ![](<images/displayondevice-image-2.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| Behavior (DeviceResponsive Identifier): Mandatory | Select the device types upon which the content is displayed. The following are the predefined options available: <p><ul><li>DesktopOnly</li><li>DesktopAndTablet</li><li>TabletOnly</li><li>TabletAndPhone</li><li>PhoneOnly</li><li>AllDevices</li><p>Examples<ul><li>Entities.DeviceResponsive.DesktopOnly - Content is only displayed on Desktop browsers only</li><li>Entities.DeviceResponsive.TabletAndPhone - Content is displayed on Tablet and Phone browsers only</li></ul></p>|

