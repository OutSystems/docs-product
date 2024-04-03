---
tags: runtime-mobileandreactiveweb;  
summary: Align Center places content horizontally or vertically within a container.
locale: en-us
guid: 911674fa-b1b7-42e4-8e72-eb103d0294e4
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=218:74
---

# Align Center

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use Align Center UI Pattern to center content horizontally or vertically on the screen.

![Example of content centered horizontally and vertically using Align Center UI Pattern](images/aligncenter-1.png "Align Center UI Pattern Example")

**How to use the Align Center UI Pattern**

This example shows you how to center align a user's name and initials.

1. In Service Studio, in the Toolbox, search for `Align Center`.

    The Align Center widget is displayed.

    ![Screenshot showing Align Center widget in Service Studio's Toolbox](images/aligncenter-2-ss.png "Service Studio Align Center Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Align Center widget into the Main Content area of your application's screen.

    ![Dragging Align Center widget into the Main Content area in Service Studio](images/aligncenter-3-ss.png "Dragging Align Center Widget")

    By default, the Align Center widget contains a Content placeholder.

1. From the Toolbox, drag the User Avatar pattern into Content placeholder.

    ![User Avatar pattern dragged into Content placeholder of Align Center widget](images/aligncenter-9-ss.png "User Avatar in Content Placeholder")

1. On the **Properties** tab, in the **Name** property, enter a name. In this example, we enter `Scott Richie`.

    ![Setting the Name property to 'Scott Richie' in Align Center widget properties](images/aligncenter-4-ss.png "Setting Name Property")

1. Add any other relevant content to the Content placeholder. In this example we add some text (Scott Richie) and an image.

    ![Adding text and image to the Content placeholder in Align Center widget](images/aligncenter-5-ss.png "Adding Content to Placeholder")

1. On the Align Center **Properties** tab, you can set the content's orientation (either vertical or horizontal).

    ![Align Center Properties tab with options to set content orientation to vertical or horizontal](images/aligncenter-6-ss.png "Align Center Properties Tab")

After following these steps and publishing the module, you can test the pattern in your app.

**Without Align Center UI Pattern** 

![Screenshot showing user interface without the use of Align Center UI Pattern](images/aligncenter-7-ss.png "Without Align Center UI Pattern")

**With Align Center UI Pattern**

![Screenshot showing user interface with the use of Align Center UI Pattern](images/aligncenter-8-ss.png "With Align Center UI Pattern")

## Properties

| Property | Description |
|---|---|
| IsHorizontal (Boolean): Optional | If True, content is displayed horizontally. This is the default. If False, the content is displayed vertically. |
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
