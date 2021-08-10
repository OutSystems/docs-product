---
tags: runtime-mobileandreactiveweb;
summary: The Animated Label animates a label when there is user input.
---

# Animated Label

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![](<images/animatedlabel-10-ss.png>)

**How to use the Animated Label UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![](<images/animatedlabel-7-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![](<images/animatedlabel-1-ss.png>)

    By default, the Animated Label widget contains Label and Input placeholders.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

    ![](<images/animatedlabel-2-ss.png>)

1. Create a new local variable for the Input widget by selecting the Input widget and on the **Properties** tab, from the **Variable** drop-down, and select **New Local Variable**.

    ![](<images/animatedlabel-3-ss.png>)

1. Enter a name for the new local variable. In this example, we enter `UserInput`.

    ![](<images/animatedlabel-4-ss.png>)

    This variable can be reused throughout your app.

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![](<images/animatedlabel-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
