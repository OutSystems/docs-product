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

1. From the Toolbox, drag the Pagination widget into the Main Content area of your application's screen.

    In this example, we drag the Pagination widget below a table of Application data.

    ![](<images/pagination-3-ss.png>)

    By default, the Pagination widget contains Previous and Next placeholders with icons.

1. On the **Properties** tab, set the (mandatory) **StartIndex**, **MaxRecords**, **TotalCount**, and **Handler** properties.

    ![](<images/pagination-4-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Pagination

| Property | Description |
|---|---|
| StartIndex (Integer): Mandatory | Sets the initial index to start pagination. |
| MaxRecords (Integer): Mandatory | Number of records to display per page. |
| TotalCount (Integer): Mandatory | Total number of records in the list.|
| ShowGoToPage (Boolean): Optional | If True, there's an input box that allows the user to enter and jump to a specific page. If False, there is no functionality to jump to a specific page. This is the default.|
| ExtendedClass (Text): Optional | Add custom style classes to the Pagination UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Pagination UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Pagination UI styles being applied.</li></ul></p> |
