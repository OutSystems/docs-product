---
tags: runtime-traditionalweb; 
summary: Timeline indicates related events in chronological order.
---

# Timeline

You can use the Timeline UI Pattern to show related events in a chronological order, such as a user’s upcoming, current, and past activities.

![](<images/timeline-1.png>)

**How to use the Timeline UI Pattern**

1. In Service Studio, in the Toolbox, search for `Timeline`.

    The Timeline widget is displayed.

    ![](<images/timeline-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Timeline widget onto your application’s screen.

    ![](<images/timeline-3-ss.png>)

    By default, the Timeline widget contains a Timeline Item widget which contains an Icon, Date, and Content placeholder. You can add as many Timeline Items as required.

1. Set the required content in the Icon, Date, and Content placeholders. In this example we add some text.

    ![](<images/timeline-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

**Timeline**

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |

**Timeline Item**

| **Property** |  **Description** |
|---|---|
| Color (Color Identifier): Optional  | Icon background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The icon background color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The icon background color is red.</li></ul></p> |
| ExtendedClass (Text): Optional  | <p>Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
