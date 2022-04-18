---
tags: runtime-mobileandreactiveweb;  
summary: Card groups small pieces of information and highlights them on the screen.
locale: en-us
guid: a44ab647-aef4-44ba-b68b-d7a0d421a92c
app_type: mobile apps, reactive web apps
---

# Card

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

You can use the Cards UI Pattern to group small pieces of information and highlight them on the screen. The information is grouped into a small block that is easily noticeable on-screen.

![](<images/card-1.png>)

**How to use the Card UI Pattern**

1. In Service Studio, in the Toolbox, search for `Card`.

    The Card widget is displayed.

    ![](<images/card-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Card widget into the Main Content area of your application's screen.

    ![](<images/card-3-ss.png>)

1. Add your content to the placeholder. In this example we add some text.

    ![](<images/card-4-ss.png>)

1. On the **Properties** tab, you can customize the Card's look and feel by setting any of the (optional) properties.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| UsePadding (Boolean): Optional  |  If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
