---
tags: runtime-mobileandreactiveweb;
summary: Counter shows the total number of occurrences of several values regarding a single topic.
---

# Counter

You can use the Counter UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![](<images/counter-2-ss.png>)

**How to use the Counter UI Pattern**

<!-- The Counter UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../../develop/data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../../develop/logic/action-web.md). -->

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Counter`.

    The Counter widget is displayed.

    ![](<images/counter-1-ss.png>)

1. From the Toolbox, drag the Counter widget into the Main Content area of your application's screen.

    ![](<images/counter-3-ss.png>)

    By default, the Counter widget contains a Content placeholder.

1. To create an aggregate (in this example to retrieve all the users on the platform), right-click the screen name and select **Fetch Data from Database**.

    ![](<images/counter-4-ss.png>)

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant entity and click **OK**. In this example, we select the **User** entity.

    ![](<images/counter-5-ss.png>)

    The aggregate **GetUsers** is created.

    ![](<images/counter-6-ss.png>)

1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. From the Toolbox, drag an Expression widget into the Content placeholder, and in the **Expression Editor** enter the following expression and click **Done**.

    `GetUsers.Count`

    ![](<images/counter-7-ss.png>)

   You have now created an expression that displays the Count property of the Aggregate you created earlier, which gets and displays the number of users on your platform.

1. On the **Properties** tab, you can customize the Counter's look and feel by setting any of the optional properties, for example, the height and orientation.

    ![](<images/counter-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

<<<<<<< HEAD
| Property |  Description |
|---|---|
| BackgroundColor (Color Identifier): Optional  | The counter's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied to the counter. This is the default.</li><li>_Entities.Color.Red_ - Displays a red counter.</li></ul></p>  |
| Height (Text): Optional | The counter's height (in pixels units). By default the counter height is 100 (pixel units). |
| ExtendedClass (Text): Optional | Add custom style classes to the Counter UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Counter UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Counter UI styles being applied.</li></ul></p> |
>>>>>>> master-withchanges
