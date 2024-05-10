---
tags: runtime-traditionalweb; 
summary: Explore how to implement a Toggle Button in OutSystems 11 (O11) for Traditional Web Apps to manage two-state user interactions.
locale: en-us
guid: 77270b71-d3f8-4ae7-93a2-92dd501e7d21
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=237:7
---

# Toggle Button

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Toggle Button UI Pattern to provide users with a stand-alone control that allows them to choose between two states, for example, a Yes/No value.

![Screenshot of the Toggle Button UI Pattern in a Traditional Web App](images/togglebutton-2-ss.png "Toggle Button UI Pattern")

**How to use the Toggle Button UI Pattern**

In this example, we create a toggle button to activate a widget that can is activated only when a condition is met.

1. In Service Studio, in the Toolbox, search for `Toggle Button`.

    The Toggle Button widget is displayed.

    ![Service Studio displaying the Toggle Button widget in the Toolbox](images/togglebutton-6-ss.png "Toggle Button Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Toggle Button widget into the Main Content area of your application's screen.

    ![Dragging the Toggle Button widget into the Main Content area of an application's screen](images/togglebutton-7-ss.png "Dragging Toggle Button Widget")

1. Right-click your screen name and select **Add Local Variable**.

    ![Adding a new local variable to the screen in Service Studio](images/togglebutton-8-ss.png "Adding Local Variable")

1. Enter a name and select a data type. In this example, we enter the name `IsToggled`, set the data type to **Boolean** and the default value to **False**.

    ![Setting properties for the local variable 'IsToggled' with a Boolean data type and default value False](images/togglebutton-9-ss.png "Setting Local Variable Properties")

1. In this example, we add some text and a button. We enter a name for the [button](<../../../../../ref/lang/auto/class-button-widget.md>) (SubmitButton), and set the **Enabled** property to the local variable we created earlier (IsToggled).

    ![Configuring the Submit button to be enabled based on the 'IsToggled' local variable state](images/togglebutton-11-ss.png "Configuring Submit Button")

1. Select the Checkbox widget, and on the **Properties** tab, from the **Variable** drop-down, select the local variable you just created (in this example, **IsToggled**).

    ![Selecting the local variable 'IsToggled' for the Checkbox widget in the Properties tab](images/togglebutton-10-ss.png "Selecting Checkbox Variable") 

1. From the OnChange **Destination** drop-down, select **New Screen Action**.

    ![Setting the OnChange destination to a new screen action for the Toggle Button](images/togglebutton-12-ss.png "Setting OnChange Destination") 

1. From the Toolbox, add the **Ajax Refresh** to the screen action, and in the **Select Widget** pop-up, navigate to and select the Submit button name (in this example, SubmitButton), and click **OK**.

    ![Adding an Ajax Refresh to the screen action and selecting the Submit button for refresh](images/togglebutton-13-ss.png "Adding Ajax Refresh to Screen Action") 

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
