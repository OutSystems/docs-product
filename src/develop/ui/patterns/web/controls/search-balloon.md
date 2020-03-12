---
tags: runtime-traditionalweb; 
summary: SearchBalloon lets the users search a list while showing results.
---

# SearchBalloon

Search Balloon Widget lets the users search the content while the results update in the results list. Use the Search Balloon to guide users by, for example, showing recommendations based on what they enter in the Search field.

**How to use**

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


## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Adds custom style classes to the Tabs Block. |  Text | False | none |
| AdvancedFormat  |  Enables you to use more options than what is provided in the input parameters. Example: `{ arrow: false,   showOnInit: true }`. For more information visit: https://atomiks.github.io/tippyjs/ |  Text | False | none |

## Layout and classes

![](images/search-balloon-image-2.png?width=800)

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnHide | Event triggered once the balloon is hidden.  |  False  |
| OnShow | Event triggered once the balloon is shown.  |  False  |

## Advanced

Here are some more advanced use-cases of the widget.

### Show results on init

1. Drag Search Balloon to the preview.
2. On the AdvancedFormat parameter add the following line:
`{ showOnInit: true }`.

### Change animation of results

1. Drag Search Balloon to the preview.
2. On the AdvancedFormat parameter add the following line:
`{ showOnInit: true }`.

![](images/search-balloon-gif-1.gif?width=800))
![](images/search-balloon-gif-2.gif?width=800))
