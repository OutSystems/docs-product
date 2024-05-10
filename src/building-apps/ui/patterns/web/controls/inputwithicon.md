---
tags: runtime-traditionalweb; 
summary: OutSystems 11 (O11) features the Input with Icon UI Pattern for enhanced data entry in Traditional Web Apps.
locale: en-us
guid: 28c2a35c-1fad-450b-bb5f-a31926f49c1a
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=234%3A2&mode=design&t=KpVEJMvnBwiukqql-1
---

# Input with Icon

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Input with Icon UI Pattern to allow the end user input data with the help of a hint in the form of an icon.

The Input with Icon UI Pattern includes an icon and placeholder text that supports the user when entering data. Is assists the user's comprehension by providing an example of the type of input required.  

![Screenshot showing an example of the Input with Icon UI Pattern in a Traditional Web App](images/inputwithicon-8-ss.png "Input with Icon UI Pattern Example")

**How to use the Input with Icon**

1. In Service Studio, in the Toolbox, search for `Input with Icon`.

    The Input with Icon widget is displayed.

    ![Image of the Input with Icon widget found in the Service Studio Toolbox](images/inputwithicon-1-ss.png "Input with Icon Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Input with Icon widget into the Main Content area of your application's screen.

    ![Dragging the Input with Icon widget into the Main Content area of an application screen](images/inputwithicon-2-ss.png "Dragging Input with Icon Widget")

1. Select the Input widget, and on the **Properties** tab, from the **Variable** drop-down, select **New Local Variable**.

    ![Selecting the Input widget and setting a new local variable in the Properties tab](images/inputwithicon-3-ss.png "Setting Variable for Input Widget")

1. Enter a name for variable. In this example we enter `Username` and set the **Data Type** property to Text.

    ![Entering a name for the new local variable for the Input widget, example using 'Username'](images/inputwithicon-5-ss.png "Naming the Local Variable")

1. Select the Input widget again, and on the **Properties** tab, in the **Prompt** property, enter the text you want displayed in the input box that describes the expected value. In this example, we enter `Username`.

    ![Entering text in the Prompt property of the Input widget to describe the expected value](images/inputwithicon-9-ss.png "Configuring Prompt Property")

1. To change the icon, select the Icon widget, and from the **Name** drop-down, select the icon you want to display in the input box. In this example, we select the user icon.

    ![Selecting a new icon for the Input with Icon widget from the Name drop-down](images/inputwithicon-6-ss.png "Changing the Icon in Input with Icon")

1. You can change the Input with Icon's look and feel by setting the (optional) properties on the **Property** tab.

    ![Setting optional properties on the Property tab to change the look and feel of the Input with Icon](images/inputwithicon-7-ss.png "Customizing Input with Icon Appearance")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| AlignIconRight (Boolean): Optional | If True, the icon is displayed on the right of the input box. If False, the icon is displayed on the left of the input box. This is the default. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
