---
tags: runtime-traditionalweb; 
summary: Search Balloon lets the users search a list while showing the results simultaneously.
---

# Search Balloon

You can use the Search Balloon UI Pattern to provide users with a search field and while the user searches for content, the results are simultaneously updated in a results list.

![](images/search-balloon-demo-browser.png?width=500)

**How to use the Search Balloon UI Pattern**

In this use case, we create a search balloon for a list of employees.

1. In Service Studio, in the Toolbox, search for `Search Balloon`. 

    The Search Balloon widget is displayed.

    ![](images/searchballoon-1-ss.png)

1. From the Toolbox, drag the Search Balloon widget into the Main Content area of your application's screen.

    ![](images/searchballoon-2-ss.png?width=800)

    By default, the Search Balloon widget contains Icon, Input, Actions, and Answers placeholders. 

1. Select the Input widget, and on the **Properties** tab, from the **Variable** drop-down, select **New Local Variable**.

    ![](images/searchballoon-3-ss.png)

1. Enter a name for the variable. In this example, we enter ``SearchText``.

   ![](images/searchballoon-4-ss.png)

1. Add a preparation action by right-clicking your screen name, and selecting **Add Preparation**.

   ![](images/searchballoon-5-ss.png)

1. Drag the relevant data to the preparation flow. In this example, we drag an **Employee** entity to the preparation flow. 

   ![](images/searchballoon-6-ss.png)

1. Select the **ListRecords1** widget, and on the **Properties** tab, from the **Source Record List**  drop-down, select the relevant source list. In this example, we select **GetEmployees.List**. Additionally, we enter `1` in the **Start Index** field.

   ![](images/searchballoon-8-ss.png)

1. Select the **Input** widget, and on the **Properties** tab, from the **Destination** drop-down, select **New Screen Action**. 

    ![](images/searchballoon-9-ss.png)

1. Drag a **Refresh Data** node to the OnChange action flow, and in the **Select Data Source** window, select **GetEmployees** and then click **OK**.

   ![](images/searchballoon-10-ss.png)
    
1. Drag an **Ajax Refresh** node to the OnChange action flow, and in the **Select Widget** window, navigate and select the relevant widget. In this example, we select **ListRecords1** and click **OK**. 

   ![](images/searchballoon-11-ss.png?width=800)

1. Double-click the Preparation action and then double-click the **GetEmployees** aggregate.

1. Click **Filters**, then click **Add Filter** and in the **Filter Condition** field, enter the relevant logic and click **Done**. In this example, we enter the following condition:
`Employee.FirstName like "%" + SearchText + "%" or Employee.LastName like "%" + SearchText + "%" or SearchText = ""`.

    This forces the aggregate to return all records that have **SearchText** in the employee's name.

   ![](images/searchballoon-12-ss.png)

1. Double-click your screen name, select the Search Balloon Widget, right-click the Text placeholder, and select **Delete**. 

    ![](images/searchballoon-13-ss.png)

1. Drag an Expression Widget to the list and enter the relevant expression value, and click **Done**. In this example, we enter the following: 

    `ListRecords1.List.Current.Employee.Name + " " ` 
    
    This filters the list to show the employees' name.

   ![](images/searchballoon-14-ss.png)

After following these steps and publishing the module, you can test the pattern in your app. 
   



## Properties

| **Property** |  **Description** | 
|---|---|
|ExtendedClass (Text): Optional | Add custom style classes to the Search Balloon UI Pattern. You define your [custom style classes](../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the Search Balloon UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Search Balloon UI styles being applied.</li></ul> | 
|AdvancedFormat (Text): Optional| Allows you to use more options than what is provided in the input parameters. <p>Example <li> `{ arrow: false,   showOnInit: true }`</li></p> For more information, see https://atomiks.github.io/tippyjs/. | 

