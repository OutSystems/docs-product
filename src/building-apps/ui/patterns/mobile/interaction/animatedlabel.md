---
tags: runtime-mobileandreactiveweb;
summary: Explore how to animate user input labels using the Animated Label UI Pattern in OutSystems 11 (O11).
locale: en-us
guid: 6b42f314-f637-444d-b908-f0609c1ba46f
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=205%3A92&mode=design&t=KpVEJMvnBwiukqql-1
---

# Animated Label

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![Screenshot of an example of the Animated Label in action](images/animatedlabel-example-ss.png "Animated Label Example")

**How to use the Animated Label UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![Screenshot showing the Animated Label widget in the Service Studio toolbox](images/animatedlabel-widget-ss.png "Animated Label Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![Screenshot demonstrating how to drag the Animated Label widget into the Main Content area](images/animatedlabel-dragwidget-ss.png "Dragging Animated Label Widget")

    By default, the Animated Label widget contains Label and Input placeholders. The Input placeholder contains a variable of type Text. You can use this variable throughout your app.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![Screenshot showing the Label placeholder with the text 'Name' entered in the Animated Label widget](images/animatedlabel-labelname-ss.png "Setting Label Text in Animated Label")

1. Enter a name and select a type for the Input variable.

    In this example, we enter the name User_Input and select UserInput as the variable type.

    ![Screenshot where a name and type for the Input variable are being set in the Animated Label widget](images/animatedlabel-variable-type-ss.png "Defining Variable for Animated Label")

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![Screenshot of the Properties tab for the Animated Label widget with optional properties settings](images/animatedlabel-properties-ss.png "Animated Label Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Framework Cheat Sheet](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/CheatSheet). |
