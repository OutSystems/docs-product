---
tags: runtime-mobileandreactiveweb;  
summary: Use the Button Loading pattern to call actions that don't run immediately.
---

# Button Loading

You can use the Button Loading UI Pattern to call actions that don't run immediately, provide a visual hint, and disable the button from being clicked until it becomes available again.

![](<images/buttonloading-2.png>)

**How to use the Button Loading UI Pattern**

1. In Service Studio, in the Toolbox, search for `Button Loading`.

    The Button Loading widget is displayed.

    ![](<images/buttonloading-1-ss.png>)

1. From the Toolbox, drag the Margin Button Loading widget into the Main Content area of your application's screen.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| IsLoading (Boolean): Mandatory | If True, the button shows the loading spinner. If False, the button doesn't show the loading spinner. |
| ShowLoadingAndLabel (Boolean): Optional | If True, the loading spinner displays beside the label. If False, the loading spinner displays underneath the label. This is the default. |
| ExtendedClass (Text): Optional | <p>Add custom style classes to the Button Loading UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Button Loading UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Button Loading UI styles being applied.</li></ul></p> |
