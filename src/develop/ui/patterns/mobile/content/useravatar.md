---
tags: runtime-mobileandreactiveweb;
summary: User Avatar displays user information in a circular badge.
---

# User Avatar

You can use the User Avatar UI Pattern to display a user's initials or their image in a circular badge.

![](<images/useravatar-4-ss.png>)

**How to use the User Avatar UI Pattern**

The following example demonstrates how you can display the initials of the registered users on your platform in a table.

1. In Service Studio, in the Toolbox, search for and drag the `Table` widget into the Main Content area of your application's screen.  

    ![](<images/useravatar-9-ss.png>)

1. To create an aggregate (in this example to retrieve all the users on the platform), right-click the screen name and select **Fetch Data from Database**.

    ![](<images/useravatar-3-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant entity and click **OK**. In this example, we select the **User** entity.

    ![](<images/useravatar-5-ss.png>)

    The aggregate **GetUsers** is created.

    ![](<images/useravatar-6-ss.png>)

1. To reopen your screen, select the **Interface** tab, and double-click on your screen name.

1. Drag the **GetUsers** aggregates into the table.

    ![](<images/useravatar-1-ss.png>)

1. In the table, delete the **Name** row cell, and replace it with the **User Avatar** widget. 

    ![](<images/useravatar-2-ss.png>)

1. Select the User Avatar widget, and on the **Properties** tab, from the **Name** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **DONE**.

    `GetUsers.List.Current.User.Name`

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Name** output parameter.

    ![](<images/useravatar-7-ss.png>)

    The **Name** property is now set to display the Name property of the aggregate you created earlier, which gets and displays the names of the registered users on your platform.

1. On the **Properties** tab, you can also customize User Avatar's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, medium-sized, circle badge.  

    ![](<images/useravatar-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Name (Text): Optional | The initials that appear inside the user avatar. Set this to a data source that contains the value you want to display. If the Image property is set, the user initials do not display.<p>Examples <ul><li>_Blank_ - Displays the initials JD (John Doe). This is the default.</li><li>_VariableName_ - Displays the value that the variable "VariableName" holds at that time.</li><li>_ExampleAggregate.Name_ - Displays the names contained in the records returned by the "ExampleAggregate" aggregate execution.</li></ul></p> |
| Image (Binary Data): Optional | The users image. If you do not specify an image, the user initials are displayed.|
| Color (Color Identifier): Optional | Set the badge's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - Displays the icon badge in the color you chose when creating the app. This is the default.</li><li>_Entities.Color.Red_ - Displays a red icon badge.</li></ul></p> |
| Size (Size Identifier): Optional | Set the badge's size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>_Blank_ - Displays a medium sized badge. This is the default value. </li><li>_Entities.Size.Small_ - Displays a small sized badge.</li></ul></p> |
| Shape (Shape Identifier): Optional | Set the badge's shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>_Blank_ - Displays a rounded badge. This is the default value.</li><li>_Entities.Shape.Sharp_ - displays a square badge</li></ul></p> |
| IsLight (Boolean): Optional | Specify the badge's background and text color. If True, a brighter hue of the color is applied to the badge and a darker color to the text. If False, a darker hue of the color is applied to the badge and a lighter color to the text. This is the default. |
| ExtendedClass (Text): Optional | Add custom style classes to the User Avatar UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the User Avatar UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the User Avatar UI styles being applied.</li></ul></p> |
