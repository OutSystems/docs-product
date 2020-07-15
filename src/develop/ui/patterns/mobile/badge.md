---
tags: runtime-mobileandreactiveweb; 
summary: Badge display numerical information as notification.
---

# Badge

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Badge UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![](<images/badge-image-7.png>)

**How to use the Badge UI Pattern**

<!-- The Badge UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). -->
The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Badge`.

    The Badge widget is displayed.

    ![](<images/badge-10-ss.png>)

1. From the Toolbox, drag the Badge widget into the Main Content area of your application's screen.

    ![](<images/badge-11-ss.png>)

1. To create an aggregate that retrieves all of the users on your platform, right-click your screen name and select **Fetch Data from Database**.

    ![](<images/badge-1-ss.png>)

1. Click the Aggregate screen, and from the **Select Source** popup, select the relevant database entity (in this example, **Users**), and click **Ok**. 

    ![](<images/badge-2-ss.png>)

1. To reopen your screen,  double-click on your screen name.

1. Select the Badge widget, and on the **Properties** tab, from the **Number** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **Done**.

    ``(GetUsers.Count)``

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Count** output parameter.

   ![](<images/badge-3-ss.png>)

   The **Number** property is now set to display the Count property of the aggregate you created, which retrieves the number of users on your platform and displays it in your Badge.

1. On the **Properties** tab, you can also customize the Badge's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, small sized, circle badge.  

    ![](<images/badge-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property |  Description |
|---|---|
| Number (LongInteger): Optional  | Number that appears inside the badge. Set this to a Data source that contains the value that the Badge will display. Common use cases include displaying a value contained in a Variable or the result of an Aggregate (for instance, querying a 'Messages' table for the current user to return the count of new messages). <p>Examples <ul><li>_Blank_ - displays the number 8 (default value)</li><li>_22_ - displays the number 22</li><li>_VariableName_ - displays the value that the variable "VariableName" holds at that time </li><li>_ExampleAggregate.Count_ - displays the number of records returned by the "ExampleAggregate" aggregate execution</li></ul></p>| 
| Color (Color Identifier): Optional  | Set the badge color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - displays the badge in the color you chose when creating the app (default value)</li><li>_Entities.Color.Red_ - displays a red badge</li></ul></p> | 
| Size (Size Identifier): Optional  | Set the badge size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>_Blank_ - displays a medium sized badge (default value)</li><li>_Entities.Size.Small_ - displays a small sized badge</li></ul></p> |
| Shape (Shape Identifier): Optional  | Set the badge shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>_Blank_ - displays a rounded badge (default value)</li><li>_Entities.Shape.Sharp_ - displays a square badge</li></ul></p>| 
| IsLight (Boolean): Optional  | Specify the badge's background color. <p>Examples <ul><li>_Blank_ - A darker hue of the color is applied to the badge and a lighter color to the text (default value)</li><li>_True_ - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the badge and a lighter color to the text</li></ul></p> |
| ExtendedClass (Text): Optional | Add custom style classes to the Badge UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value)</li><li>_''myclass''_ - Adds the myclass style to the Badge UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Badge UI styles being applied.</li></ul></p> |