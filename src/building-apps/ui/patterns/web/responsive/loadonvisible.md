---
tags: ui patterns, lazy loading, performance optimization, user experience, web development
summary: Explore the Load on Visible UI pattern in OutSystems 11 (O11) to enhance application speed and user experience by loading content only when visible.
locale: en-us
guid: 768c98ad-bb82-496b-a311-1f577e2e221f
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=245%3A40&mode=design&t=u4ANW5BJS7Flsdmg-1
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Load on Visible

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Load on Visible UI Pattern to enhance the speed of your application as well as improve user experience. Using this UI pattern, information is loaded onto the page only when it is visible to the user. For example, instead of loading all text and images onto a page at once, they only appear when the user scrolls down the page and the information/image becomes visible.

**How to use the Load on Visible UI Pattern**

1. In Service Studio, in the Toolbox, search for `Load on Visible`.

    The Load on Visible widget is displayed.

     ![Screenshot showing the Load on Visible widget in the Service Studio toolbox](images/loadonvisible-3-ss.png "Load on Visible Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Load on Visible widget into the Main Content area of your application's screen.

    ![Image depicting the process of dragging the Load on Visible widget into the Main Content area](images/loadonvisible-4-ss.png "Dragging Load on Visible Widget")

1. Add the required content to the placeholder inside the Load on Visible widget.

    In this example, we add images by dragging the Image widget into the Load on Visible widget and selecting an image from the sample OutSystems UI images.

    ![Example of adding images to the Load on Visible widget placeholder in Service Studio](images/loadonvisible-5-ss.png "Adding Content to Load on Visible Widget")

After following these steps and publishing the module, you can test the pattern in your app.
