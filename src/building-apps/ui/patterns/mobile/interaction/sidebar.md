---
tags: runtime-mobileandreactiveweb;
summary: Sidebar shows additional content on the side of the screen.
locale: en-us
guid: d948b2a9-574a-43a1-bf6a-9465bdc22dfe
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=213:73
---

# Sidebar

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

**This documentation is not valid for deprecated components.** To check if your component is deprecated and how to migrate old versions, see the [Patterns and Versions Overview](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/MigrationOverview).
                            
</div>

You can use the Sidebar UI Pattern to display additional information in the margin of the main content. The additional information supports the user's understanding of the main content.

![Example of a Sidebar UI Pattern implemented in an application interface](images/sidebar-example.png "Sidebar UI Pattern Example")

<div class="info" markdown="1">

**Note:** To avoid conflicts with the browser native gestures, the Sidebar pattern only works with gestures on Native Apps not running as PWA.  

</div>

**How to use the Sidebar UI Pattern**

In this example, we create a button that opens and closes the Sidebar widget.

1. In Service Studio, in the Toolbox, search for `Sidebar`.

    The Sidebar widget is displayed.

    ![Screenshot showing how to search for the Sidebar widget in OutSystems Service Studio](images/sidebar-widget-ss.png "Searching for Sidebar Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Sidebar widget into the Main Content area of your application's screen.

    ![Screenshot illustrating the process of dragging the Sidebar widget into the main content area of an application screen in Service Studio](images/sidebar-drag-ss.png "Dragging Sidebar Widget into Main Content Area")

    By default, the Sidebar widget contains Header and Content placeholders.

1. On the **Properties** tab, in the **Name** field, enter a name for the Sidebar widget.

    In this example, we enter it `MySidebar`.

    ![Screenshot depicting the naming of the Sidebar widget as 'MySidebar' in the properties tab of Service Studio](images/sidebar-name-ss.png "Naming the Sidebar Widget")

1. Select and right-click your screen name, and select **Add Local Variable**.

    ![Screenshot showing the addition of a local variable for controlling the Sidebar state in Service Studio](images/sidebar-add-var-ss.png "Adding a Local Variable for Sidebar")

1. Enter a name for the variable.

    In this example, name the variable ``IsSidebarOpen``, set the **Data Type** as Boolean, and the **Default Value** to **False**.

    ![Screenshot displaying the naming of the Sidebar variable as 'IsSidebarOpen' with a Boolean data type in Service Studio](images/sidebar-var-name-ss.png "Naming the Sidebar Variable")

1. Select the Sidebar widget, and on the **Properties** tab, from the **StartsOpen** dropdown, select the newly created variable.

    ![Screenshot showing the configuration of the StartsOpen property of the Sidebar widget to the 'IsSidebarOpen' variable in Service Studio](images/sidebar-isopen-ss.png "Setting the StartsOpen Property of Sidebar")

1. Add your content to the **Header** and **Content** placeholders, for example, forms, images and text. 
    
    In this example we add some text.
   
    ![Screenshot demonstrating how to add content to the Header and Content placeholders of the Sidebar widget in Service Studio](images/sidebar-content-ss.png "Adding Content to Sidebar Placeholders")

1. From the Toolbox, drag the **Button** widget just below the **Sidebar** widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button.

    In this example, we enter `Open Sidebar`.

    ![Screenshot of adding a button labeled 'Open Sidebar' below the Sidebar widget in Service Studio](images/sidebar-button-ss.png "Adding a Button to Toggle Sidebar")

1. To create a screen action to toggle the Sidebar:

    a. Double-click the **Open Sidebar** button.

    b. Drag an **If** statement to the screen action, and on the **Properties** tab, set the **Condition** to the **IsSidebarOpen** variable.

    ![Screenshot illustrating the addition of an If statement to a screen action for toggling the Sidebar in Service Studio](images/sidebar-if-ss.png "Adding If Statement for Sidebar Toggle")

    c. On the **True** branch, add the **SidebarClose** client action and set the **WidgetId** parameter to the Sidebar Id.

    ![Screenshot showing the SidebarClose client action being added to the True branch of an If statement in Service Studio](images/sidebar-close-ss.png "Adding SidebarClose Client Action")

    d. On the **False** branch, add the **SidebarOpen** client action and set the **WidgetId** parameter to the Sidebar Id.

    e. Drag an **Assign** to the screen action and set **IsSidebarOpen** variable to ``not IsSidebarOpen``.
    
    ![Screenshot depicting an Assign action to toggle the 'IsSidebarOpen' variable in Service Studio](images/sidebar-assign-ss.png "Assigning the Sidebar Open State")

1. You can customize the Sidebar by selecting the pattern, and on the **Properties** tab, set the relevant (optional) properties.

    ![Screenshot displaying the setting of optional properties for the Sidebar pattern in Service Studio](images/sidebar-properties-ss.png "Setting Optional Properties of Sidebar")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
|StartsOpen (Boolean): Optional| Set to True to display the Sidebar. The default value is False.|
|Direction (Direction Entity): Optional | Set the position where the Sidebar appears on the screen.<br/>The predefined options are Left and Right.<br/><br/>Examples:<ul><li>Entities.Direction.Right - The sidebar is displayed on the right side of the screen.</li><li>Entities.Direction.Left - The sidebar is displayed on the left side of the screen. </li></ul>  |
|HasOverlay (Boolean): Optional| Set to True, to show an overlay when the Sidebar is open. When you click on the overlay, the Sidebar is closed.|
|Width (String): Optional| Defines the Sidebar width. Accepts any kind of unit (px, %, vw). Default value is 500px. |
|ExtendedClass (Text): Optional| Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Events

|Event| Description  | 
|---|---|
|OnToggle: Optional  | Event triggered when the Sidebar is toggled. | 
