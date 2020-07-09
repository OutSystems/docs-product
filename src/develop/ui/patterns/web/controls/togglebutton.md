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

1. From the Toolbox, drag the Toggle Button widget into the Main Content area of your application's screen.

    ![](<images/togglebutton-7-ss.png>)

1. Right-click your screen name and select **Add Local Variable**. 

    ![](<images/togglebutton-8-ss.png>)

1. Enter a name and select a data type. In this example, we enter the name ``IsToggled``, set the data type to **Boolean** and the default value to **False**.

    ![](<images/togglebutton-9-ss.png>)

1. In this example, we add some text and a button. We enter a name for the button (SubmitButton), and set the **Enabled** property to the local variable we created earlier (IsToggled). 

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
|ExtendedClass (Text): Optional | Add custom style classes to the Toggle Button UI Pattern. You define your [custom style classes](../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the Toggle Button UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Toggle Button UI styles being applied.</li></ul> |


