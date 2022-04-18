---
tags: runtime-traditionalweb; 
summary: DisplayOnDevice improves the way information is displayed on different devices.
locale: en-us
guid: cb68aaf9-4836-4eeb-b3f2-0a9fcc5164a4
app_type: traditional web apps
---

# Display on Device

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Display on Device UI pattern to select what elements are displayed on which device types. With this pattern you can improve the way information is displayed on different devices - computers, tablets, and phones - by specifically specifying which elements display on each of them.

![](<images/displayondevice-1.png>)

**How to use the Display on Device UI Pattern**

1. In Service Studio, in the Toolbox, search for `Display on Device`.

    The Display on Device widget is displayed.

    ![](<images/displayondevice-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Display on Device widget into the Main Content area of your application's screen.

    ![](<images/displayondevice-3-ss.png>)

1. Add the required content to the placeholders inside the Display on Device widget.

    In this example, we add images by dragging the Image widget into the Display on Device widget and selecting an image from the sample OutSystems UI images.

    ![](<images/displayondevice-4-ss.png>)

1. On the **Properties** tab, from the **Behavior** drop-down list, choose the device types you want to display this widget on. These images are displayed on the device types you specify, and not shown for any other devices.

    ![](<images/displayondevice-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| Behavior (DeviceResponsive Identifier): Mandatory | Select the device types upon which the content is displayed. The following are the predefined options available: <p><ul><li>DesktopOnly</li><li>DesktopAndTablet</li><li>TabletOnly</li><li>TabletAndPhone</li><li>PhoneOnly</li><li>AllDevices</li></ul></p><p>Examples<ul><li>Entities.DeviceResponsive.DesktopOnly - Content is displayed on Desktop browsers only</li><li>Entities.DeviceResponsive.TabletAndPhone - Content is displayed on Tablet and Phone browsers only</li></ul></p> |
