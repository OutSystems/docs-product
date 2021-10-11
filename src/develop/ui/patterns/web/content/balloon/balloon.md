---
tags: runtime-traditionalweb; 
summary: Balloon shows a content overlay to users, without forcing them to lose the UI context.
---

# Balloon

You can use the Balloon UI Pattern to display content in a pop-up on the UI. The Balloon UI Pattern is useful when you need to display additional information related to a small on-screen element.

![](<images/balloon-image-6.png>)

**How to use the Balloon UI Pattern**

In this example, we use the Balloon as a tooltip on a screen with a form.

1. In Service Studio, in the Toolbox, search for `Balloon`.

    The Balloon widget is displayed.

    ![](<images/balloon-image-3.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Balloon widget into the Main Content area of your application's screen.

    ![](<images/balloon-image-7.png>)

1. To bind the Balloon widget to the First Name input widget, on the **Properties** tab, from the **WidgetId** dropdown, select **firstname.Id**.

    ![](<images/balloon-image-8.png>)

    **Note**: The **WidgetId** comes from the element **Name** you are binding the balloon with.

1. In the Content placeholder, enter the content you want to display. In this example we add text.

    ![](<images/balloon-image-9.png>)

1. Repeat steps 2-4 for each of the elements that require a Balloon pop-up.

1. On the **Properties** tab, you can change the look and feel of the Balloon widget by setting the (optional) properties, for example, the position of the content on screen and what action triggers the content to display.

    ![](<images/balloon-image-10.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/FYTapAjZPj8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

| **Property** |  **Description** | 
|---|---|
| WidgetId (Text): Mandatory | Id that triggers the element so it is visible. |
| Position (PositionBase Identifier): Optional | Sets the position of where the Balloon content is displayed in relation to the widget. The predefined options are:<br/><br/><ul><li>Bottom</li><li>Left</li><li>Right</li><li>Top</li></ul><br/>Examples<br/><br/><ul><li>_Entities.PositionBase.Bottom_ - The content displays below the element. This is the default value.</li><li>_Entities.PositionBase.Right_ - The content displays to the right of the element.</li></ul> |
| Trigger (Trigger Identifier): Optional | Sets the action that triggers the content to display. The predefined options are:<br/><br/><ul><li>Click</li><li>Hover</li><li>Manual</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Trigger.Click_ - Content displays when the user clicks the element.</li><li>_Entities.Trigger.Manual_ - Requires that the tooltip is triggered programmatically. </li><li>_Entities.Trigger.Hover_ - Content displays when the user hovers over the element. </li></ul> | 
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
| AdvancedFormat (Text): Optional  |  Enables you to use more options than what is provided in the input parameters. <br/><br/>Example: `{ arrow: false,   showOnInit: true }`<br/><br/>For more information visit: <https://atomiks.github.io/tippyjs/> |
