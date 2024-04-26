---
tags: runtime-traditionalweb; 
summary: Counter shows the total number of occurrences of several values regarding a single topic.
locale: en-us
guid: 91058e55-ccbb-494d-bc74-9bdeab106742
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=243%3A10&mode=design&t=u4ANW5BJS7Flsdmg-1
---

# Counter

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Counter UI Pattern to display numerical information as a notification. For example, the Badge UI pattern is frequently used to notify users about the number of unread emails, unopened messages, or new tasks they may have.

![Screenshot of the Counter UI Pattern used to display numerical information as a notification in a Traditional Web App](images/counter-14-ss.png "Counter UI Pattern Example")

**How to use the Counter UI Pattern**

The Counter UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../logic/action-web.md).

The following example demonstrates how you can display the number of registered users on your platform.

1. In Service Studio, in the Toolbox, search for `Counter`.

    The Counter widget is displayed.

    ![Image showing the Counter widget in the Service Studio toolbox for Traditional Web Apps](images/counter-7-ss.png "Counter Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Counter widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Counter widget into the main content area of an application's screen in Service Studio](images/counter-9-ss.png "Dragging Counter Widget into Main Content Area")

1. From the Element tree, create a Preparation action by right-clicking on your screen, and from the drop-down, select **Add Preparation**.

    This Preparation action executes logic that fetches the data before the screen is displayed.

    ![Image depicting the process of adding a Preparation action to fetch data before the screen is displayed in Service Studio](images/counter-8-ss.png "Adding Preparation Action")

1. Select the **Data** tab, and from the Entities tree, navigate to the **User** entity and drag it onto the Preparation action.

    ![Screenshot showing the creation of an aggregate to retrieve user data by dragging the User entity onto the Preparation action in Service Studio](images/counter-10-ss.png "Creating an Aggregate for User Entity")

    This creates an [aggregate](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Aggregate) that retrieves all of the users on your platform.

1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. Within the Counter widget, right-click in the Text widget (containing the number 26), and select Convert to Expression.

    ![Image illustrating the conversion of a text widget to an expression within the Counter widget in Service Studio](images/counter-11-ss.png "Converting Text Widget to Expression")

1. In the Expression Editor, enter the following expression and click **Done**.

    `GetUsers.Count`

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Count** output parameter.

   ![Screenshot of setting an expression in the Expression Editor to display the user count in the Counter widget](images/counter-12-ss.png "Setting the Expression to Display User Count")

   You have now created an expression that displays the Count property of the Aggregate you added to the Preparation action, which gets the number of users on your platform and displays them in your Counter.

1. From the **Properties** tab of each of the Counter's widgets, you can customize the Counter's display text and icon. For this example, the display text is changed to Registered Users.

      ![Image showing the customization of the Counter's display text and icon in the Properties tab of Service Studio](images/counter-13-ss.png "Customizing Counter Display Text and Icon")

1. Additionally, on the **Properties** tab, you can customize the Counter's look and feel by setting any of the optional properties, for example, the height and orientation.

      ![Screenshot of the Properties tab where the Counter's height and orientation can be customized in Service Studio](images/counter-3-ss.png "Customizing Counter's Look and Feel")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Orientation (Orientation Identifier): Optional | Set the counter orientation. By default the counter is displayed horizontally. <p> Examples <ul><li>Entities.Orientation.Horizontal - The counter displays horizontally </li><li>Entities.Orientation.Vertical - The counter displays vertically</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                     |
| Height (Text): Optional                        | Set the counter height. By default the counter height is 100 (pixel units).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ExtendedClass (Text): Optional                 | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
