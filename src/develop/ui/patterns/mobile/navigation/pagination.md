---
tags: runtime-mobileandreactiveweb;  
summary: The Pagination UI Pattern helps users find a specific item on long listings.
locale: en-us
guid: 20819218-aa75-441f-b2e6-6796dc14f1d8
app_type: mobile apps, reactive web apps
platform-version: o11
---

# Pagination

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Pagination UI pattern to help users find a specific item on long listings. This pattern is typically used on listings, such as e-commerce category pages, search engines, and article archives.

![](<images/pagination-5-ss.png>)

**How to use the Pagination UI Pattern**

1. In Service Studio, in the Toolbox, search for `Pagination`.
  
    The Pagination widget is displayed.

    ![](<images/pagination-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

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

| Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StartIndex (Integer): Mandatory  | Sets the initial index to start pagination.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MaxRecords (Integer): Mandatory  | Number of records to display per page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TotalCount (Integer): Mandatory  | Total number of records in the list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ShowGoToPage (Boolean): Optional | If True, there's an input box that allows the user to enter and jump to a specific page. If False, there is no functionality to jump to a specific page. This is the default.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ExtendedClass (Text): Optional   | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
