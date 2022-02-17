---
tags: runtime-mobileandreactiveweb;  
summary: Timeline Item indicates related events in chronological order.
---

# Timeline Item

You can use the Timeline Item UI Pattern to show related events in a chronological order, such as a user's upcoming, current, and past activities.

![](<images/timelineitem-1-ss.png>)

**How to use the Timeline Item UI Pattern**

1. In Service Studio, in the Toolbox, search for `Timeline Item`.

    The Timeline Item widget is displayed.

    ![](<images/timelineitem-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Timeline widget onto your application's screen.

    ![](<images/timelineitem-3-ss.png?width=800>)

    By default, the Timeline Item widget contains Left, Icon, Title, Content, and Right placeholders. You can add as many Timeline Item widgets as required.

    In this example we add two more Timeline Item widgets.

1. Set the required content in each of the placeholders.

    In this example we add some icons and text.

    ![](<images/timelineitem-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Timeline Item

| Property | Description |
|---|---|
| IsActive (Boolean): Optional | If True, the item is set to active. If False, the item is inactive. This is the default.<br/><br/>**NOTE**: This property is deprecated. It renders an element as being active in mobile applications based on the OutSystems UI Base Theme prior to version 2.4.0. It has no effect in applications created after OutSystems UI version 2.4.0. |
| Color (Color Identifier): Optional | Icon background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The icon background color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The icon background color is red.</li></ul></p> |
| ExtendedClass (Text): Optional | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
