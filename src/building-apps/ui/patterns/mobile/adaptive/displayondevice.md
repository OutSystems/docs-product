---
tags: ide usage, reactive web apps, mobile apps, ui design, cross-platform development
summary: Explore how OutSystems 11 (O11) enhances UI flexibility with the Display on Device pattern for optimal content presentation across different devices.
locale: en-us
guid: cfb2d1db-e5a7-42ef-85d9-a4348e3f1895
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=201:31
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Display on Device

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Display on Device UI pattern to select what elements are displayed on which device types. With this pattern you can improve the way information is displayed on different devices - computers, tablets, and phones - by specifically specifying which elements display on each of them.

![Overview of Display on Device pattern showing different device types](images/displayondevice-1.png "Display on Device Pattern Overview")

**How to use the Display on Device UI Pattern**

1. In Service Studio, in the Toolbox, search for `Display on Device`.

    The Display on Device widget is displayed.

    ![Service Studio interface with Display on Device widget highlighted](images/displayondevice-2-ss.png "Display on Device Widget in Service Studio")
  
    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Display on Device widget into the Main Content area of your application's screen.

    ![Dragging the Display on Device widget into the Main Content area in Service Studio](images/displayondevice-3-ss.png "Dragging Display on Device Widget")

    By default, the Display on Device widget contains OnDesktop, OnTablet, and OnPhone placeholders.

1. Add the required content to each of the placeholders.

    In this example, we add images by dragging the Image widget into each of the placeholders, and on the **Properties** tab, from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![Adding images to OnDesktop, OnTablet, and OnPhone placeholders in Display on Device widget](images/displayondevice-4-ss.png "Configuring Display on Device Placeholders")

After following these steps and publishing the module, you can test the pattern in your app.
