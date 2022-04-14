---
tags: runtime-mobileandreactiveweb;
summary: List Item Content is used to layout content such as icons, text, and actions inside a list in a readable way.
locale: en-us
guid: 1c561d9b-7797-4365-b605-9c56261bfe04
---

# List Item Content

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps

</div>

You can use the List Item Content UI Pattern to quickly organize critical content in a readable way, helping the user understand the content. The List Item Content pattern is often used to organize content such as icons, text, and actions inside a list in a readable way.

![](<images/listitemcontent-1-ss.png>)

**How to use the List Item Content UI Pattern**

1. In Service Studio, in the Toolbox, search for `List Item Content`.

    The List Item Content widget is displayed.

    ![](<images/listitemcontent-2-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the List Item Content widget into the Main Content area of your application's screen.

    ![](<images/listitemcontent-3-ss.png>)

1. Add the relevant content to the placeholders.

    In this example, we add some texts and icons. 

    ![](<images/listitemcontent-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property |  Description |
|---|---|
| ExtendedClass (Text): Optional |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
