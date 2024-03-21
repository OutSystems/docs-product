---
tags: runtime-traditionalweb; 
summary: The Animated Label animates a label when there is user input.
locale: en-us
guid: cada799f-c2fe-4d0a-98aa-309bf3a4fd16
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=226:14
---

# Animated Label

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![Screenshot of the Animated Label UI Pattern in use](images/animatedlabel-10-ss.png "Animated Label in Action")

**How to use the Animated Label UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![Screenshot showing the Animated Label widget in the Service Studio toolbox](images/animatedlabel-7-ss.png "Animated Label Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Animated Label widget into the Main Content area of an application screen](images/animatedlabel-8-ss.png "Dragging Animated Label Widget")

    By default, the Animated Label widget contains Label and Input placeholders.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![Screenshot showing the Label placeholder with the text 'Name' entered in the Animated Label widget](images/animatedlabel-9-ss.png "Label Placeholder Text")

1. Create a new local variable for the Input widget by selecting the Input widget and on the **Properties** tab, and from the **Variable** drop-down, and select **New Local Variable**.

    ![Screenshot of creating a new local variable for the Input widget in the Animated Label properties](images/animatedlabel-1-ss.png "Creating a New Local Variable")

1. Enter a name for the new local variable. In this example, we enter `UserInput`.

    ![Screenshot showing the process of naming the new local variable 'UserInput' for the Animated Label](images/animatedlabel-2-ss.png "Naming the New Local Variable")

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![Screenshot of the optional properties available for customizing the Animated Label's appearance](images/animatedlabel-3-ss.png "Animated Label Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| IsInline (Boolean): Optional | If False, the Animated Input is displayed in a white input box. If True, there is no white input box. This is the default. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
