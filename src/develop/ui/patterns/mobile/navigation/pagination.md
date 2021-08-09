---
tags: runtime-mobileandreactiveweb;  
summary: The Pagination UI Pattern helps users find a specific item on long listings.
---

# Pagination

You can use the Pagination UI pattern to help users find a specific item on long listings. This pattern is typically used on listings, such as e-commerce category pages, search engines, and article archives.

![](<images/pagination-5-ss.png>)

**How to use the Pagination UI Pattern**

1. In Service Studio, in the Toolbox, search for `Pagination`.
  
    The Pagination widget is displayed.

    ![](<images/pagination-1-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. From the Toolbox, drag the Pagination widget into the Main Content area of your application's screen.

    In this example, we drag the Pagination widget below a table of Application data.

    ![](<images/pagination-3-ss.png>)

    By default, the Pagination widget contains Previous and Next placeholders with icons.

1. Add 2 local variables - one to store the starting index value and the other to store the maximum number of records per page. In this example, we add the **StartIndex**  and **MaxRecords** variables. Both are of type integer and we set the default value of the **MaxRecords** to 50. This means there are 50 records shown per page.

    ![](<images/pagination-9-ss.png>)

1. Select the Pagination widget, and on the **Properties** tab, set the **StartIndex** and **MaxRecords** properties to the respective local variables we just created.

    ![](<images/pagination-10-ss.png>)

1. Staying on the **Properties** tab, set the **TotalCount** to the number of records fetched in the aggregate that is the source of the table.  in this example, we set it to **GetApplications.Count**.

    ![](<images/pagination-11-ss.png>)

1. To define what happens when the end user changes from one page to another, from the **Handler** dropdown, select **New Client Action**. By default the **New Client Action** contains a **NewStartIndex** input.

1. To set the start index of the pagination, drag the **StartIndex** onto the client action and set its value to **NewStartIndex**. When a user changes page, the start index will change accordingly.

    ![](<images/pagination-12-ss.png>)

1. Refresh the data by re-executing the aggregate so the data for the new page appears in the table.

    ![](<images/pagination-13-ss.png>)

    In this example, when the user changes page, and the refresh action runs, it will take into account the current **StartIndex** and the **MaxRecords** to determine the **NewStartIndex** (in this case 50 for the new page.)

1. So that we only fetch the data we need for each page, select the aggregate and set the **Start Index** and **Max. Records** properties to the the variables we created earlier, **StartIndex** and **MaxRecords**.

    ![](<images/pagination-14-ss.png>)



After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| StartIndex (Integer): Mandatory | Sets the initial index to start pagination. |
| MaxRecords (Integer): Mandatory | Number of records to display per page. |
| TotalCount (Integer): Mandatory | Total number of records in the list. |
| ShowGoToPage (Boolean): Optional | If True, there's an input box that allows the user to enter and jump to a specific page. If False, there is no functionality to jump to a specific page. This is the default. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
