---
tags: runtime-traditionalweb; 
summary: Input with Icon allows the end user to input data with the help of a hint.
---

# Input with Icon

You can use the Input with Icon UI Pattern to allow the end user input data with the help of a hint in the form of an icon.

The Input with Icon UI Pattern includes an icon and placeholder text that supports the user when entering data. Is assists the user's comprehension by providing an example of the type of input required.  

![](<images/inputwithicon-8-ss.png>)

**How to use the Input with Icon**

1. In Service Studio, in the Toolbox, search for `Input with Icon`.

    The Input with Icon widget is displayed.

    ![](<images/inputwithicon-1-ss.png>)

1. From the Toolbox, drag the Input with Icon widget into the Main Content area of your application's screen.

    ![](<images/inputwithicon-2-ss.png>)

1. Select the Input widget, and on the **Properties** tab, from the **Variable** drop-down, select **New Local Variable**.

    ![](<images/inputwithicon-3-ss.png>)

1. Enter a name for variable. In this example we enter `Username` and set the **Data Type** property to Text.

    ![](<images/inputwithicon-5-ss.png>)

1. Select the Input widget again, and on the **Properties** tab, in the **Prompt** property, enter the text you want displayed in the input box that describes the expected value. In this example, we enter `Username`.

    ![](<images/inputwithicon-9-ss.png>)

1. To change the icon, select the Icon widget, and from the **Name** drop-down, select the icon you want to display in the input box. In this example, we select the user icon.

    ![](<images/inputwithicon-6-ss.png>)

1. You can change the Input with Icon's look and feel by setting the (optional) properties on the **Property** tab.

    ![](<images/inputwithicon-7-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property |  Description |  
|---|---|
| AlignIconRight (Boolean): Optional  |  If True, the icon is displayed on the right of the input box. If False, the icon is displayed on the left of the input box. This is the default. |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Input with Icon UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Input with Icon UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Input with Icon UI styles being applied.</li></ul> |
