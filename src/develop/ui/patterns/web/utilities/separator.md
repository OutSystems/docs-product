---
tags: runtime-traditionalweb; 
summary: Separator distributes content into clear groups and ease visual organization.
---

# Separator

You can use the Separator UI Pattern to separate content clearly and ease visual organization.

  ![](<images/separator-1.png>)

**How to use the Separator UI Pattern**

1. In Service Studio, in the Toolbox, search for `Separator`. 

    The Separator widget is displayed.

    ![](<images/separator-5-ss.png>)

1. From the Toolbox, drag the Separator widget into the Main Content area of your application's screen, where you want to separate content. In this example, we drag the widget in between an image and some text.

    ![](<images/separator-7-ss.png>)

1. On the **Properties** tab, set the relevant (optional) properties, for example, the colour and the amount of space separating the content.

    ![](<images/separator-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** | 
|---|---|
| Color (Color Identifier): Optional  | Set the color for the separator line. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - Displays a gray (Neutral4) line (default value).</li><li>_Entities.Color.Red_ - Displays a red line.</li></ul></p> |
| Space (Space Identifier): Optional |Set the space around the separator line. The predefined vales are: <p> <ul><li>None</li><li>Extra small</li><li>Small</li><li>Base</li><li>Medium</li><li>Large</li><li>Extra large</li><li>Extra extra large</li><p>Examples <ul><li>_Blank_ - Displays a space of 16px (_Entities.Space.Base_) around the line separator. This is the default value.</li><li>_Entities.Space.Large_ - Displays a space of 32px around the line separator.</li></ul></p> | 
| IsVertical (Boolean): Optional |If set to False, the separator line displays horizontally (default). If set to True, the separator line displays vertically. |
| ExtendedClass (Text): Optional | Add custom style classes to the Separator UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Separator UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Separator UI styles being applied.</li></ul></p>|