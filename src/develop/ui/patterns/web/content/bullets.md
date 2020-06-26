---
tags: runtime-traditionalweb; 
summary: Bullets break up large blocks of text into smaller points that are easier to read.
---

# Bullets

You can use the Bullets UI Pattern to organize topics into separate bullet points.

**How to use the Bullets UI Pattern**

1. In Service Studio, in the Toolbox, search for `Bullets`.

    The Bullets widget is displayed.

    ![](<images/bullets-1-ss.png>)

1. From the Toolbox, drag the Bullets widget into the Main Content area of your application's screen.

    ![](<images/bullets-2-ss.png>)

    By default, the Bullets widget contains 3 Bullet Items. You can add or delete Bullet Items as required. To create sub-bullets, you can drag the Bullets widget into the Bullet Item placeholder.

1. Add your content to the placeholders. In this example we add text to each of the placeholders. 

    **Note**: If you leave any placeholder blank, it will not be displayed when the page is rendered.

    ![](<images/bullets-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

| **Property** |  **Description** |  
|---|---|
| ExtendedClass (Text): Optional  |  Add custom style classes to the Bullets UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<p>Examples</p><ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Bullets UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Bullets UI styles being applied. </li></ul> |
