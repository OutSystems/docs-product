---
tags: runtime-mobileandreactiveweb;
summary: Icon Badge displays numerical information as notification.
---

# Icon Badge

You can use the Icon Badge UI Pattern to display numerical information as a notification. For example, the Icon Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![](<images/iconbadge-1-ss.png>)

**How to use the Icon Badge UI Pattern**

<!--The Icon Badge UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). -->

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Icon Badge`.

    The Icon Badge widget is displayed.

    ![](<images/iconbadge-2-ss.png>)

1. From the Toolbox, drag the Icon Badge widget into the Main Content area of your application's screen.

    ![](<images/iconbadge-3-ss.png>)

    By default, the Icon Badge contains an Icon placeholder with a pre existing icon.

1. To create an aggregate (in this example to retrieve all the users on the platform), right-click the screen name and select **Fetch Data from Database**.

    ![](<images/iconbadge-4-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant entity and click **Select**. In this example, we select the **User** entity.

    ![](<images/iconbadge-5-ss.png>)

    The aggregate **GetUsers** is created.

    ![](<images/iconbadge-6-ss.png>)

1. To reopen your screen, select the **Interface** tab, and double-click on your screen name.

1. Select the Icon Badge widget, and on the **Properties** tab, from the **Number** drop-down, select **Expression Editor**, and in the Expression Editor enter the following expression and click **Close**.

    `GetUsers.Count`

    ![](<images/iconbadge-7-ss.png>)

    The **Number** property is now set to display the Count property of the Aggregate you created earlier, which gets and displays the number of users on your platform.

1. On the **Properties** tab, you can customize the Icon Badge's look and feel by setting any of the optional properties, for example, the color.

    ![](<images/iconbadge-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| Number (Integer): Mandatory | The number that appears inside the badge. Set this to a data source that contains the value you want to display. <p>Examples <ul><li>_VariableName_ - Displays the value that the variable "VariableName" holds at that time.</li><li>_ExampleAggregate.Name_ - Displays the names contained in the records returned by the "ExampleAggregate" aggregate execution.</li></ul></p> |
| Color (Color Identifier): Optional | Set the icon badge's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the icon badge. <p>Examples <ul><li>_Blank_ - Displays the icon badge in the color you chose when creating the app. This is the default.</li><li>_Entities.Color.Red_ - Displays a red icon badge.</li></ul></p> |
| IsLight (Boolean): Optional | Specify the badge's background and text color. <p>Examples <ul><li>_True_ - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>_False_ - A darker hue of the color is applied to the badge and a lighter color to the text. This is the default.</li></ul></p> |
| ExtendedClass (Text):Optional | Add custom style classes to the Icon Badge UI Pattern.You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Icon Badge UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Icon Badge UI styles being applied.</li></ul></p> |
