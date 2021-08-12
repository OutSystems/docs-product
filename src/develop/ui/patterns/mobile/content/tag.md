---
tags: runtime-mobileandreactiveweb;  
summary: Tag styles small texts in a colored tag format.
---

# Tag

You can use the Tag UI Pattern to style small texts in a colored tag format. Use the Tags UI Pattern to display statuses, labels, or categories thus providing great user experience.

**How to use the Tag UI Pattern**

1. In Service Studio, in the Toolbox, search for `Tag`.
  
    The Tag widget is displayed.

    ![](<images/tag-1-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Tag widget into the Main Content area of your application's screen.

    ![](<images/tag-2-ss.png>)

1. Add your content to the placeholders. In this example, we add some text.

    ![](<images/tag-3-ss.png>)

1. On the properties tab, you can change the Tag's look and feel by setting the (optional) properties, for example, size and color.

    ![](<images/tag-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Color (Color Identifier): Optional  | Set the Tag's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. <p>Examples <ul><li>_Blank_ - Displays the badge in the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The Tag's background is red.</li></ul></p> |
| Shape (Shape Identifier): Optional| Set the Tag's shape. Rounded, soft rounded, and sharp are the predefined shapes available. <p>Examples <ul><li>_Blank_ - Displays a rounded shaped Tag (default value).</li><li>_Entities.Shape.Sharp_ - Displays a square shaped Tag.</li></ul></p> |
| Size (Size Identifier): Optional  | Set the Tag's size. Small and medium are the predefined sizes available. <p>Examples <ul><li>_Entities.Size.Medium_ - Displays a medium-sized badge.</li><li>_Entities.Size.Small_ - Displays a small sized Tag.</li></ul></p> |
| IsLight (Boolean): Optional  | Specify the Tag's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the Tag and a lighter color to the text (default value).</li><li>_True_ - A brighter hue of the color is applied to the Tag and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the Tag and a lighter color to the text.</li></ul></p> |
| ExtendedClass (Text): Optional |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
