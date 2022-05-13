---
tags: runtime-mobileandreactiveweb;
summary: The Animated Label animates a label when there is user input.
locale: en-us
guid: 6b42f314-f637-444d-b908-f0609c1ba46f
app_type: mobile apps, reactive web apps
---

# Animated Label

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![](<images/animatedlabel-example-ss.png>)

**How to use the Animated Label UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![](<images/animatedlabel-widget-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![](<images/animatedlabel-dragwidget-ss.png>)

    By default, the Animated Label widget contains Label and Input placeholders. The Input placeholder contains a variable of type Text. You can use this variable throughout your app.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![](<images/animatedlabel-labelname-ss.png>)

1. Enter a name and select a type for the Input variable.

    In this example, we enter the name User_Input and select UserInput as the variable type.

    ![](<images/animatedlabel-variable-type-ss.png>)

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![](<images/animatedlabel-properties-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet). |
