---
tags: runtime-mobileandreactiveweb;
summary: Progress Bar displays the progress of a task by incrementing values in a bar.
---

# Progress Bar

You can use the Progress Bar to display percentage values by incrementing values in a bar and to show the current progress of a task flow.

![](<images/progressbar-1-ss.png>)

**How to use the Progress Bar UI Pattern**

1. In Service Studio, in the Toolbox, search for `Progress Bar`.

    The Progress Bar widget is displayed.

    ![](<images/progressbar-2-ss.png>)

1. From the Toolbox, drag the Progress Bar widget into the Main Content area of your application's screen.

    ![](<images/progressbar-3-ss.png>)

1. On the **Properties** tab, in the **Progress** property, enter the progress percentage. In this example we enter `55` but you can also use functions or local variables.

    ![](<images/progressbar-4-ss.png>)

1. Add the text you want to appear as the Progress Bar title. In this example, we add `On Going`.

    ![](<images/progressbar-10-ss.png>)

1. On the **Properties** tab, you can customize Progress Bar's look and feel by setting any of the optional properties, for example, the shape, color, and size of the Progress Bar.

    ![](<images/progressbar-9-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Progress (Integer): Mandatory | Percentage displayed on progress bar. You can use integers (usually between 0 and 100), functions, or local variables. |
| Color (Color Identifier): Optional | Progress bar color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The progress bar color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The progress bar color is red.</li></ul></p> |
| Height (Integer): Optional | Progress Bar height (in pixels). The default value is 12. |
| AnimateInitialProgress (Boolean): Optional | If True, the percentage progress in the progress bar is animated. This is the default. If False, the progress is not animated. |
| Text (Text): Optional | **Deprecated in OutSystems UI.** |
| Shape (Shape Identifier): Optional | Set the Progress Bar shape. The predefined options are: <ul><li>Rounded</li><li> Soft Rounded </li> <li>Sharp</li></ul><p>Examples <ul><li>_Blank_ - The Progress Bar has a rounded shape (Entities.Shape.Rounded). This is the default.</li><li>_Entities.Shape.Sharp_ - The Progress Bar has a sharp shape.</li></ul></p> |
| ExtendedClass (Text): Optional | Add custom style classes to the Progress Bar UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Progress Bar UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Progress Bar UI styles being applied.</li></ul></p> |
