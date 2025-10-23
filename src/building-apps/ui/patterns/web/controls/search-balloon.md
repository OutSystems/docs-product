---
tags: ui patterns, search functionality, ux design, web applications, real-time data
summary: Learn how to implement the Search Balloon UI Pattern in OutSystems 11 (O11) for real-time search results in Traditional Web Apps.
locale: en-us
guid: b50125b9-419e-42f0-a55e-1deb3cfe5fc9
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=234%3A36&mode=design&t=KpVEJMvnBwiukqql-1
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Search Balloon

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Search Balloon UI Pattern to provide users with a search field and while the user searches for content, the results are simultaneously updated in a results list.

![Demonstration of the Search Balloon UI Pattern in a browser interface](images/search-balloon-demo-browser.png "Search Balloon Demo")

**How to use the Search Balloon UI Pattern**

In this use case, we create a search balloon for a list of employees.

1. In Service Studio, in the Toolbox, search for `Search Balloon`.

    The Search Balloon widget is displayed.

    ![Search Balloon widget displayed in the OutSystems Service Studio](images/searchballoon-1-ss.png "Search Balloon in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Search Balloon widget into the Main Content area of your application's screen.

    ![Dragging the Search Balloon widget into the Main Content area in Service Studio](images/searchballoon-2-ss.png "Drag Search Balloon Widget")

    By default, the Search Balloon widget contains Icon, Input, Actions, and Answers placeholders.

1. Select the Input widget, and on the **Properties** tab, from the **Variable** drop-down, select **New Local Variable**.

    ![Configuring the Input widget properties for the Search Balloon in Service Studio](images/searchballoon-3-ss.png "Configure Input Widget")

1. Enter a name for the variable. In this example, we enter `SearchText`.

    ![Setting a new local variable for the Search Balloon's Input widget in Service Studio](images/searchballoon-4-ss.png "Set Local Variable")

1. Add a preparation action by right-clicking your screen name, and selecting **Add Preparation**.

    ![Adding a preparation action to the screen for the Search Balloon in Service Studio](images/searchballoon-5-ss.png "Add Preparation Action")

1. Drag the relevant data to the preparation flow. In this example, we drag an **Employee** entity to the preparation flow.

    ![Dragging the Employee entity to the preparation flow for the Search Balloon in Service Studio](images/searchballoon-6-ss.png "Data Preparation Flow")

1. Select the **ListRecords1** widget, and on the **Properties** tab, from the **Source Record List**  drop-down, select the relevant source list. In this example, we select **GetEmployees.List**. Additionally, we enter `1` in the **Start Index** field.

    ![Selecting the source record list for the ListRecords widget in the Search Balloon setup](images/searchballoon-8-ss.png "ListRecords Widget Configuration")

1. Select the **Input** widget, and on the **Properties** tab, from the **Destination** drop-down, select **New Screen Action**.

    ![Setting the destination for the Input widget in the Search Balloon configuration](images/searchballoon-9-ss.png "Input Widget Destination")

1. Drag a **Refresh Data** node to the OnChange action flow, and in the **Select Data Source** window, select **GetEmployees** and then click **OK**.

    ![Adding a Refresh Data node to the OnChange action flow for the Search Balloon](images/searchballoon-10-ss.png "Refresh Data Node")

1. Drag an **Ajax Refresh** node to the OnChange action flow, and in the **Select Widget** window, navigate and select the relevant widget. In this example, we select **ListRecords1** and click **OK**.

    ![Dragging an Ajax Refresh node to the OnChange action flow for the Search Balloon](images/searchballoon-11-ss.png "Ajax Refresh Node")

1. Double-click the Preparation action and then double-click the **GetEmployees** aggregate.

1. Click **Filters**, then click **Add Filter** and in the **Filter Condition** field, enter the relevant logic and click **Close**. In this example, we enter the following condition:

     `Employee.FirstName like "%" + SearchText + "%" or Employee.LastName like "%" + SearchText + "%" or SearchText = ""`.

    This forces the aggregate to return all records that have **SearchText** in the employee's name.

    ![Setting a filter condition in the GetEmployees aggregate for the Search Balloon](images/searchballoon-12-ss.png "Set Aggregate Filter")

1. Double-click your screen name, select the Search Balloon Widget, right-click the Text placeholder, and select **Delete**.

    ![Deleting the Text placeholder from the Search Balloon Widget in Service Studio](images/searchballoon-13-ss.png "Delete Text Placeholder")

1. Drag an Expression Widget to the list and enter the relevant expression value, and click **Close**. In this example, we enter the following:

    `ListRecords1.List.Current.Employee.Name + " "`

    This filters the list to show the employees' name.

    ![Adding an Expression Widget to the Search Balloon to display employee names](images/searchballoon-14-ss.png "Add Expression Widget")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
| AdvancedFormat (Text): Optional | Allows you to use more options than what is provided in the input parameters. <p>Example <ul><li> `{ arrow: false,   showOnInit: true }`</li></ul></p> For more information, see <https://atomiks.github.io/tippyjs/>. |
