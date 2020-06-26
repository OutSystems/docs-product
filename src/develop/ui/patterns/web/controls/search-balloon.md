---
tags: runtime-traditionalweb; 
summary: Search Balloon lets the users search a list while showing the results simultaneously.
---

# Search Balloon

Search Balloon Widget lets the users search the content while the results update in the results list. Use the Search Balloon to guide users by, for example, showing recommendations based on what they enter in the Search field.

**How to use the Search Balloon UI Pattern**

Follow these steps to create a result list that automatically updates when users enter a search query.

Before you start:

* Reference [Sample Data](../../../screen-templates-create/sample-data.md) in your app.
* Create a new blank Screen and add a Preparation Action to it (right-click a Web Screen and select **Add Preparation**). Drag Sample_Employee Entity (from Sample Data) to the Preparation flow.

Then:

1. Drag Search Balloon Widget from the widget toolbox to your Screen.

1. Go to Search Balloon Widget > select the Input Widget  > locate the Input properties > click the **Variable** field and select **New Local Variable** from the list. Name the variable SearchText.
    
    ![Search Balloon variable](images/search-balloon-variable-ss.png?width=700)
   
1. Go to Search Balloon Widget > select the ListRecords1 Widget > locate ListRecords1 properties > click the **Source Record List** field and select "GetEmployees.List" from the list. Still in the properties, enter `1` in the **Start Index** field.

1. Go to Search Balloon Widget > select the Input Widget > locate the Input properties > click **Destination** field and select **New Screen Action** from the list. The OnChange Action opens. In the OnChange Action flow:
   
    * Drag a **Refresh Data** node and select "GetEmployees" in the **Select Data Source** window.
    
    * Drag an **Ajax Refresh** to the flow, navigate by expanding to **ListRecords1**, select **ListRecords1** and click **OK**.   

1. Go to the Preparation Action > double-click the GetEmployees Aggregate > click **Filters** > click **Add Filter** > enter this text in the **Filter Condition** field:
`Sample_Employee.FirstName like "%" + SearchText + "%" or Sample_Employee.LastName like "%" + SearchText + "%" or SearchText = ""`. Click **Done**.

    This forces the Aggregate to return all records that have SearchText in the first or last name.

    ![The logic flow that refreshes data and widget](images/search-balloon-refresh-data-flow-ss.png?width=400)
    

1. Go back to the Screen and select Search Balloon Widget.
    
    * Delete the "Put your results here" placeholder text and drag an Expression Widget to the list.

    * Double-click the Expression Widget and enter `ListRecords1.List.Current.Sample_Employee.FirstName + " " + ListRecords1.List.Current.Sample_Employee.LastName` as the Expression Value. Click **Done**.
    
    Now the filtered list shows employees' first and last names.

    ![Expression Widget in Search Balloon](images/search-balloon-expression-ss.png?width=700)

1. Publish your app and try entering a name in the search field.
   
   ![Search Balloon demo in a browser](images/search-balloon-demo-browser.png?width=500)


## Properties

| **Property** |  **Description** | 
|---|---|
|ExtendedClass (Text): Optional | Add custom style classes to the Search Balloon UI Pattern. You define your [custom style classes](../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the Search Balloon UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Search Balloon UI styles being applied.</li></ul> | 
|AdvancedFormat (Text): Optional| Allows you to use more options than what is provided in the input parameters. <p>Example <li> `{ arrow: false,   showOnInit: true }`</li></p> For more information, see https://atomiks.github.io/tippyjs/. | 

