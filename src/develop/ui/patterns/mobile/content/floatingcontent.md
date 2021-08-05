---
tags: runtime-mobileandreactiveweb;  
summary: Floating Content displays a panel that floats over content (like a map or an image), docked to a screen corner or direction.
---

# Floating Content

You can use the Floating Content UI Pattern to display content on top of other screen elements, such as a map with navigation instructions.

![](<images/floatingcontent-1-ss.png>)

**How to use the Floating Content UI Pattern**

1. In Service Studio, in the Toolbox, search for `Floating Content`.

    The Floating Content widget is displayed.

    ![](<images/floatingcontent-2-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Floating Content widget into the Main Content area of your application's screen.

    In this example, the Main Content area of already contains an image of a map. 

    ![](<images/floatingcontent-3-ss.png?width=800>)

    By default, the Floating Content widget contains a Content placeholder.

1. Add the relevant content to the placeholder.

    In this example, we add a Search widget. 

    ![](<images/floatingcontent-4-ss.png?width=800>)

1. Select the Floating Content widget, and on the **Properties** tab, set the mandatory **Position** property. This defines where the widget is displayed. You can customize the Section's look and feel by setting any of the (optional) properties.

    ![](<images/floatingcontent-5-ss.png?width=800>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

### Floating Content

| **Property** |  **Description** |
|---|---|
| Position (Position Identifier): Mandatory | The position the floating content is displayed on screen. |
| UseFullHeight (Boolean): Optional| If True, the widget takes up the full height of the screen. If False, the widget doesn't take up the full height of the screen. This is the default.   |
| UseFullWidth (Boolean): Optional| If True, the widget takes up the full width of the screen. If False, the widget doesn't take up the full width of the screen. This is the default. |
| UseMargin (Boolean): Optional| If True, a margin is applied to the widget. This is the default. If False, there is no margin applied to the widget. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
