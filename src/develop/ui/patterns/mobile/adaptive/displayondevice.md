---
tags: runtime-mobileandreactiveweb;  
summary: Display on Device improves the way information is displayed on different devices.
---

# Display on Device

You can use the Display on Device UI pattern to select what elements are displayed on which device types. With this pattern you can improve the way information is displayed on different devices - computers, tablets, and phones - by specifically specifying which elements display on each of them.

![](<images/displayondevice-1.png>)

**How to use the Display on Device UI Pattern**

1. In Service Studio, in the Toolbox, search for `Display on Device`.

    The Display on Device widget is displayed.

    ![](<images/displayondevice-2-ss.png>)
  
    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Display on Device widget into the Main Content area of your application's screen.

    ![](<images/displayondevice-3-ss.png>)

    By default, the Display on Device widget contains OnDesktop, OnTablet, and OnPhone placeholders.

1. Add the required content to each of the placeholders.

    In this example, we add images by dragging the Image widget into each of the placeholders, and on the **Properties** tab, from the **Image** dropdown, selecting an image from the sample OutSystems UI images.

    ![](<images/displayondevice-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.
