---
tags: runtime-mobileandreactiveweb;  
summary: Timeline Item indicates related events in chronological order.
locale: en-us
guid: ae0bd8db-c13e-4c6d-83f8-dabc43562bb6
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=218:0
---

# Timeline Item

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Timeline Item UI Pattern to show related events in a chronological order, such as a user's upcoming, current, and past activities.

![Screenshot showing an overview of the Timeline Item UI Pattern in a mobile app interface](images/timelineitem-1-ss.png "Timeline Item UI Pattern Overview")

**How to use the Timeline Item UI Pattern**

1. In Service Studio, in the Toolbox, search for `Timeline Item`.

    The Timeline Item widget is displayed.

    ![Screenshot of the Timeline Item widget found in the Service Studio toolbox](images/timelineitem-2-ss.png "Timeline Item Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Timeline widget onto your application's screen.

    ![Screenshot illustrating how to drag the Timeline widget onto an application's screen in Service Studio](images/timelineitem-3-ss.png "Dragging Timeline Widget onto the Screen")

    By default, the Timeline Item widget contains Left, Icon, Title, Content, and Right placeholders. You can add as many Timeline Item widgets as required.

    In this example we add two more Timeline Item widgets.

1. Set the required content in each of the placeholders.

    In this example we add some icons and text.

    ![Screenshot showing the configuration of content within the Timeline Item placeholders with icons and text](images/timelineitem-4-ss.png "Configuring Timeline Item Content")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Timeline Item

| Property| Description|
|---|---|
| IsActive (Boolean): Optional       | If True, the item is set to active. If False, the item is inactive. This is the default.<br/><br/>**NOTE**: This property is deprecated. It renders an element as being active in mobile applications based on the OutSystems UI Base Theme prior to version 2.4.0. It has no effect in applications created after OutSystems UI version 2.4.0.|
| Color (Color Identifier): Optional | Icon background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The icon background color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The icon background color is red.</li></ul></p>|
| ExtendedClass (Text): Optional     | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
