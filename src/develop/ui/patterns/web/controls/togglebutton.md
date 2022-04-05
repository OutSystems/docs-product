---
tags: runtime-traditionalweb; 
summary: The Toggle Button UI Pattern prompts end users to choose between two states.
---

# Toggle Button

You can use the Toggle Button UI Pattern to provide users with a stand-alone control that allows them to choose between two states, for example, a Yes/No value.

![](<images/togglebutton-2-ss.png>)

**How to use the Toggle Button UI Pattern**

In this example, we create a toggle button to activate a widget that can is activated only when a condition is met.

1. In Service Studio, in the Toolbox, search for `Toggle Button`.

    The Toggle Button widget is displayed.

    ![](<images/togglebutton-6-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Toggle Button widget into the Main Content area of your application's screen.

    ![](<images/togglebutton-7-ss.png>)

1. Right-click your screen name and select **Add Local Variable**.

    ![](<images/togglebutton-8-ss.png>)

1. Enter a name and select a data type. In this example, we enter the name `IsToggled`, set the data type to **Boolean** and the default value to **False**.

    ![](<images/togglebutton-9-ss.png>)

1. In this example, we add some text and a button. We enter a name for the [button](<../../../../../ref/lang/auto/Class.Button Widget.final.md>) (SubmitButton), and set the **Enabled** property to the local variable we created earlier (IsToggled).

    ![](images/togglebutton-11-ss.png?width=800)

1. Select the Checkbox widget, and on the **Properties** tab, from the **Variable** drop-down, select the local variable you just created (in this example, **IsToggled**).

    ![](images/togglebutton-10-ss.png?width=800) 

1. From the OnChange **Destination** drop-down, select **New Screen Action**.

    ![](images/togglebutton-12-ss.png?width=800) 

1. From the Toolbox, add the **Ajax Refresh** to the screen action, and in the **Select Widget** pop-up, navigate to and select the Submit button name (in this example, SubmitButton), and click **OK**.

    ![](images/togglebutton-13-ss.png?width=800) 

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
