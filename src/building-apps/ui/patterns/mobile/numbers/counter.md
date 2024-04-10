---
tags: runtime-mobileandreactiveweb;
summary: Counter shows the total number of occurrences of several values regarding a single topic.
locale: en-us
guid: 18443b28-3b50-4e2d-9731-a84aac8cdaf1
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=218:29
---

# Counter

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Counter UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![Screenshot showing the Counter UI Pattern used for notifications, such as unread emails or messages.](images/counter-2-ss.png "Counter UI Pattern Notification Example")

**How to use the Counter UI Pattern**

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Counter`.

    The Counter widget is displayed.

    ![Screenshot of the Counter widget in the Service Studio toolbox.](images/counter-1-ss.png "Counter Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Counter widget into the Main Content area of your application's screen.

    ![Screenshot illustrating how to drag the Counter widget into the main content area of an application's screen.](images/counter-3-ss.png "Dragging Counter Widget into Main Content Area")

    By default, the Counter widget contains a Content placeholder.

1. To create an aggregate (in this example to retrieve all the users on the platform), right-click the screen name and select **Fetch Data from Database**.

    ![Screenshot showing the process of creating an aggregate to fetch user data from the database.](images/counter-4-ss.png "Creating an Aggregate for User Data")

1. To add a database entity, click the screen, and from the **Select Source** pop-up, select the relevant entity and click **OK**. In this example, we select the **User** entity.

    ![Screenshot depicting the addition of a database entity, specifically the User entity, to the application screen.](images/counter-5-ss.png "Adding a Database Entity to the Screen")

    The aggregate **GetUsers** is created.

    ![Screenshot displaying the newly created GetUsers aggregate in Service Studio.](images/counter-6-ss.png "Aggregate GetUsers Created")

1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. From the Toolbox, drag an Expression widget into the Content placeholder, and in the **Expression Editor** enter the following expression and click **Done**.

    `GetUsers.Count`

    ![Screenshot of an Expression widget in Service Studio showing the expression to display the user count.](images/counter-7-ss.png "Expression Widget with User Count")

   You have now created an expression that displays the Count property of the Aggregate you created earlier, which gets and displays the number of users on your platform.

1. On the **Properties** tab, you can customize the Counter's look and feel by setting any of the optional properties, for example, the height and orientation.

    ![Screenshot highlighting the properties tab where the Counter's appearance can be customized.](images/counter-8-ss.png "Customizing Counter Properties")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property| Description|
|---|---|
| BackgroundColor (Color Identifier): Optional | The counter's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - No background color is applied to the counter. This is the default.</li><li>Entities.Color.Red - Displays a red counter.</li></ul></p>|
| IsVertical (Boolean): Optional| If True, the content is displayed vertically. If False, the content is displayed horizontally. This is the default.|
| Height (Text): Optional| The counter's height (in pixels units). By default the counter height is 100 (pixel units).|
| ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
