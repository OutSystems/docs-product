---
tags: runtime-traditionalweb; 
summary: Stacked Icon expands the icon set and creates new graphical representation of concepts.
---

# Stacked Icon

You can use the Stacked Icon Pattern to stack two icons on top of each other.  

![](<images/stackedicon-8.png>)

**How to use the Stacked Icon UI Pattern**

1. In Service Studio, in the Toolbox, search for `Stacked Icon`. 

    The Stacked Icon widget is displayed.

   ![](<images/stackedicon-9-ss.png>)

1. From the Toolbox, drag the Stacked Icon widget into the Main Content area of your application's screen.

    ![](<images/stackedicon-10-ss.png>)

1. On the **Properties** tab, set any of the optional properties for the icons, for example, the front and back icons as well as the size and color of the icon. 

    ![](<images/stackedicon-7-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| IconFront (IconName Identifier): Optional| The icon that displays in front of the other icon. Some of the predefined values include:<p><ul><li>Android</li><li>Bell</li><li>Camera</li><li>Desktop</li><li>Envelope</li><p>Examples <ul><li>_Blank_ - Displays a camera icon (default value).</li><li>_Entities.IconName.instagram_ - Displays the Instgram icon.</li></ul></p>  |
| IconBack (IconName Identifier): Optional | The icon that displays behind the icon. Some of the predefined values include:<p><ul><li>Circle</li><li>Square</li><li>Heart</li></ul></p><p>Examples <ul><li>_Blank_ - Displays a ban icon.</li><li>_Entities.IconName.birthday_cake_ - Displays a birthday cake icon.</li></ul></p> |
| IconFrontColor (Color Identifier): Optional | Front icon color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - Displays a black (Neutral10) icon (default value).</li><li>_Entities.Color.Red_ - Displays a red icon.</li></ul></p>  | 
| IconBackColor (Color Identifier): Optional | Back Icon color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - Displays a black (Neutral10) icon (default value).</li><li>_Entities.Color.Green_ - Displays a green icon.</li></ul></p> |
| IconSize (IconSize Identifier): Optional| Sets the icon size. The predefined values are:<p><ul><li>Size_2x</li><li>Size_3x</li><li>Size_4x</li><li>Size_5x</li><li>Percent_33</li></ul></p><p>Examples <ul><li>_Entities.IconSize.Size_2x_ - Increases the font to two times larger relative to the icon container.</li><li>_Entities.IconSize.Size_Percent_33_ - Increases the font to 33% larger relative to the icon container.</li></ul></p>  |
| InvertSize (Boolean): Optional | If True, the icon sizes are swapped. If False, they are not swapped. |
| ExtendedClass (Text): Optional | Add custom style classes to the Separator UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Stacked Icon UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Stacked Icon UI styles being applied.</li></ul></p> | 