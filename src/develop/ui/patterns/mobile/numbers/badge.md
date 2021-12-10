---
tags: runtime-mobileandreactiveweb; 
summary: Badge display numerical information as notification.
---

# Badge

You can use the Badge UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![](<images/badge-image-7.png>)

**How to use the Badge UI Pattern**

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Badge`.

    The Badge widget is displayed.

    ![](<images/badge-10-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Badge widget into the Main Content area of your application's screen.

    ![](<images/badge-11-ss.png>)

1. To create an aggregate that retrieves all of the users on your platform, right-click your screen name and select **Fetch Data from Database**.

    ![](<images/badge-1-ss.png>)

1. Click the Aggregate screen, and from the **Select Source** popup, select the relevant database entity (in this example, **Users**), and click **Select**.

    ![](<images/badge-2-ss.png>)

1. To reopen your screen, double-click on your screen name.

1. Select the Badge widget, and on the **Properties** tab, from the **Number** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **Close**.

    `(GetUsers.Count)`

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Count** output parameter.

    ![](<images/badge-3-ss.png>)

    The **Number** property is now set to display the Count property of the aggregate you created, which retrieves the number of users on your platform and displays it in your Badge.

1. On the **Properties** tab, you can also customize the Badge's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, medium-sized, soft-rounded badge.  

    ![](<images/badge-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Number (LongInteger): Optional | Number that appears inside the badge. Set this to a Data source that contains the value that the Badge will display. Common use cases include displaying a value contained in a Variable or the result of an Aggregate (for instance, querying a 'Messages' table for the current user to return the count of new messages). <p>Examples <ul><li>_Blank_ - displays the number 8 (default value)</li><li>_22_ - displays the number 22</li><li>_VariableName_ - displays the value that the variable "VariableName" holds at that time </li><li>_ExampleAggregate.Count_ - displays the number of records returned by the "ExampleAggregate" aggregate execution</li></ul></p> |
| Color (Color Identifier): Optional  | Set the badge color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - displays the badge in the color you chose when creating the app (default value)</li><li>_Entities.Color.Red_ - displays a red badge</li></ul></p> |
| Size (Size Identifier): Optional  | Set the badge size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>_Blank_ - displays a medium sized badge (default value)</li><li>_Entities.Size.Small_ - displays a small sized badge</li></ul></p> |
| Shape (Shape Identifier): Optional  | Set the badge shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>_Blank_ - displays a rounded badge (default value)</li><li>_Entities.Shape.Sharp_ - displays a square badge</li></ul></p> |
| IsLight (Boolean): Optional  | Specify the badge's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the badge and a lighter color to the text (default value)</li><li>_True_ - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the badge and a lighter color to the text</li></ul></p> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - Adds the myclass style to the UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
