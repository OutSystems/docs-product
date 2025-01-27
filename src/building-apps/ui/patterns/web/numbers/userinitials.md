---
tags: ui patterns, user interface design, widget implementation, dependency management, user profile display
summary: OutSystems 11 (O11) supports the User Initials UI Pattern for displaying user initials or images in a circular badge within Traditional Web Apps.
locale: en-us
guid: 079fe985-0d1e-435c-984a-cbd125908f13
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=245:23
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# User Initials

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the User Initials UI Pattern to display a user’s initials or their image in a circular badge. 

![Screenshot of the User Initials UI Pattern in a Traditional Web App](images/userinitials-4-ss.png "User Initials UI Pattern Example")

**How to use the User Initials UI Pattern**

The User Initials UI Pattern usually displays dynamic information. In most cases, prior to using this pattern, you will need [to retrieve or update the Data](../../../../data/intro.md) that contains the information you want to display onscreen. You do this by using an [Action](../../../../logic/action-web.md).

The following example demonstrates how you can display the initials of the registered users on your platform.

1. In Service Studio, in the Toolbox, search for `User Initials`.

    The User Initials widget is displayed.

    ![Image showing the User Initials widget in the Service Studio toolbox](images/userinitials-11-ss.png "User Initials Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the User Initials widget into the Main Content area of your application's screen.

     ![Screenshot of dragging the User Initials widget into the Main Content area of an application screen](images/userinitials-12-ss.png "Dragging User Initials Widget")

1. From the Element tree, create a Preparation action by right-clicking on your screen, and from the drop-down, select **Add Preparation**.

    This Preparation action executes logic that fetches the data before the screen is displayed.

     ![Image showing how to add a Preparation action by right-clicking on the screen in Service Studio](images/userinitials-13-ss.png "Adding Preparation Action")

1. Select the **Data** tab, and from the Entities tree, navigate to the **User** entity and drag it onto the Preparation action.

    ![Screenshot of dragging the User entity onto the Preparation action to create an aggregate](images/userinitials-14-ss.png "Creating an Aggregate for User Data")

    This creates an [aggregate](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Queries/Aggregate) that retrieves all the users on your platform.

1. To reopen your screen, select the **Interface** tab, and double-click on your screen.

1. Select the User Initials widget, and on the **Properties** tab, from the **Name** drop-down, select **Expression Editor**.

1. In the Expression Editor, enter the following expression and click **Close**.

    `GetUsers.List.Current.User.Name`

    Note: You can also add the expression by navigating through the Expression Editor's **Scope** tree and double-clicking on the **Name** output parameter.

    ![Image showing the Expression Editor with the expression to display user names in the User Initials widget](images/userinitials-15-ss.png "Setting Name Property in User Initials Widget")

    The **Name** property is now set to display the Name property of the Aggregate you added to the Preparation action, which gets the names of the registered users on your platform and displays them in the badge.

1. On the **Properties** tab, you can also customize the badge's look and feel by setting any of the optional properties, for example, the color, shape, and size. The following example displays a blue, medium-sized, circle badge.  

    ![Screenshot of the Properties tab with options to customize the User Initials badge's color, shape, and size](images/userinitials-10-ss.png "Customizing User Initials Badge Appearance")  

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name (Text): Optional              | The initials that appear inside the badge. Set this to a Data source that contains the value that the badge will display. Common use cases include displaying a value contained in a Variable or the result of an Aggregate (for instance, querying a 'Messages' table for the current user to return the count of new messages). <p>Examples <ul><li>Blank - displays the initials JJ (default value)</li><li>VariableName - displays the value that the variable "VariableName" holds at that time </li><li>ExampleAggregate.Name - displays the names contained in the records returned by the "ExampleAggregate" aggregate execution</li></ul></p> |
| Color (Color Identifier): Optional | Set the badge color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>Blank - displays the badge in the color you chose when creating the app (default value)</li><li>Entities.Color.Red - displays a red badge</li></ul></p>                                                                                                                                                                                                                                                                                                                                  |
| Shape (Shape Identifier): Optional | Set the badge shape. Rounded, soft rounded, and sharp are the predefined shapes available for the badge. <p>Examples <ul><li>Blank - displays a rounded badge (default value)</li><li>Entities.Shape.Sharp - displays a square badge</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                                                     |
| Size (Size Identifier): Optional  | Set the badge size. Small and medium are the predefined sizes available for the badge. <p>Examples <ul><li>Blank - displays a medium sized badge (default value)</li><li>Entities.Size.Small - displays a small sized badge</li></ul></p> | |
| IsLight (Boolean): Optional | Specify the badge's background color. <p>Examples <ul><li>Blank - A darker hue of the color is applied to the badge and a lighter color to the text (default value)</li><li>True - A brighter hue of the color is applied to the badge and a darker color to the text.</li><li>False - A darker hue of the color is applied to the badge and a lighter color to the text</li></ul></p> |
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet).|
