---
summary: Learn how to manually implement table pagination and sorting in OutSystems 11 (O11) with detailed instructions for enhancing user interface functionality.
tags:
  - Accessibility
  - Aggregates
  - Pagination
  - Sorting
  - Table
  - Traditional Web
  - UI
locale: en-us
guid: c85c1a3d-327a-49e1-af6d-bd99a67b4ebc
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=199:30
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - apply
isautopublish: true
---

# Table pagination and sorting

Pagination and sorting are the features you get automatically if you create a table by dragging an Entity to the screen. For cases where you need to implement them manually, follow the instructions in this article.

## Sorting

### In Reactive Web and Mobile

Service Studio automatically creates a Client Action with the full sort logic when you wire up the OnSort event. Before doing that, set the sort attribute on each column header you want to make sortable.

#### Add sorting to a table

1. In the **Widget Tree**, select the **Header Cell** of each column you want to make sortable. In the **Sort Attribute** property, select the entity attribute to sort by. Repeat for each sortable column.

    This associates each column with the database attribute that controls the sort order. The `ClickedColumn` Input Parameter of the OnSort event automatically receives the Sort Attribute value of the header cell the user clicks.

    ![Screenshot showing how to change the sort attribute in a table widget within Service Studio](images/table-sort-attribute-ss.png "Table Sort Attribute Selection")

    <div class="info" markdown="1">

    With a nested structure as the table **Source** variable, to select a nested item as **Sort Attribute**, set the **Data Type** of the **Source** to a **List of Record** with your structure. When using a structure **List** instead of **Record List**, you can only select the first-level attributes as the **Sort Attribute**.

    </div>

1. Select the Table widget. In the **OnSort** drop-down list box of the properties, select **New On Sort Client Action**.

    Service Studio creates a Client Action with the sort logic already implemented:

    * A `TableSort` Local Variable on the screen to hold the current sort attribute.
    * An **If** node that checks whether the user clicked the same column again. If yes, it appends `" DESC"` to toggle descending order. If no, it sets `TableSort` to the new column's sort attribute.
    * A **Dynamic Sort** on the Aggregate set to `TableSort`.
    * A **Refresh Data** node to re-execute the Aggregate and update the table.

1. Publish the module.

#### Remove sorting

To remove sorting from a table column, delete the value of the **Sort Attribute** parameter of the **Header Cell** element.

### In Traditional Web

In Traditional Web apps, sorting is a built-in feature of the **Table Records** widget. When you create a screen by dragging an Entity onto a web flow, Service Studio scaffolds the table with sortable column headers automatically. Refer to [Table Records Widget](../../../ref/lang/auto/class-table-records-widget.md) for details on configuring fixed and dynamic sorting.

### Sorting and accessibility

To meet WCAG 2.2 accessibility standards, since Platform Server 11.42.0 the Table widget supports communicating sort state to assistive technologies such as screen readers.

When you enable **Enable WCAG 2.2** in the **Platform Configurations** tab of [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration), the Table widget automatically adds the `aria-sort` attribute to sortable column headers. This attribute communicates the current sort state to screen readers, as required by WCAG 1.3.1 (Info and Relationships).

The `aria-sort` attribute is set as follows:

* `aria-sort="none"` — the column is sortable but not currently sorted.
* `aria-sort="ascending"` — the column is currently sorted in ascending order.
* `aria-sort="descending"` — the column is currently sorted in descending order.

By default, the Table widget assumes the following sort convention:

* The first click on a column sorts it in ascending order.
* A second click on the same column sorts it in descending order.
* Clicking a different column sorts the new column in ascending order.

The auto-generated **OnSort** action created by Service Studio follows this convention, and `aria-sort` reflects the correct state automatically.

#### Custom OnSort actions with a different default direction

If your custom **OnSort** action sorts a column in descending order on the first click (for example, a date column that shows the newest records first), the default assumption above is wrong, and `aria-sort` will not match the actual sort state announced to screen readers.

To fix this, declare the initial direction on the **Header Cell** using the `default-sort-direction` **Extended Property**:

1. In the **Widget Tree**, select the **Header Cell**.
1. In the widget properties, locate **Extended Properties** and add a new entry:

    * **Name**: `default-sort-direction`
    * **Value**: `"descending"` (use `"ascending"` to keep the default; any other value also falls back to `"ascending"`)

With this property set, the first click on the column produces `aria-sort="descending"`, and subsequent clicks on the same column toggle between `descending` and `ascending`. Set this property per column — each **Header Cell** can declare its own default direction.

## Pagination

Follow these steps to add pagination to your table. You should already have an Aggregate and a Table widget added to your screen.

### In Reactive Web and Mobile

1. Create **StartIndex** and **MaxRecords** Local Variables of the Integer data type. Set the default value of **StartIndex** to `0` and the default value of **MaxRecords** to the number of records to display per page (for example, `50`).

1. Drag the **Pagination** widget below the Table widget.

1. In the **Pagination** widget properties, set the following:

    * **StartIndex** to `StartIndex`
    * **MaxRecords** to `MaxRecords`
    * **TotalCount** to the `.Count` Output Parameter of your Aggregate (for example, `GetEmployees.Count`)

    ![Screenshot displaying the Pagination Widget properties with StartIndex, MaxRecords, and TotalCount settings](images/pagination-paginate-props-ss.png "Pagination Widget Properties")

1. In the **Handler** drop-down list box, select **New Client Action**. The new action opens.

1. In the action, add an **Assign** node and set `StartIndex = NewStartIndex`. Then drag a **Refresh Data** node to the flow and set it to refresh the Aggregate.

    The `NewStartIndex` Input Parameter holds the index of the first record on the page the user navigated to.

    ![Screenshot depicting the PaginationOnNavigate action logic for updating the StartIndex in a pagination system](images/pagination-logic-ss.png "Pagination Logic Configuration")

1. In the Aggregate properties, set **Start Index** to `StartIndex` and **Max. Records** to `MaxRecords`.

    ![Screenshot illustrating the settings for StartIndex and Max. Records in an Aggregate for pagination](images/pagination-aggregate-props-ss.png "Aggregate Index and Max Records Settings")

1. Publish the module.

### In Traditional Web

The Table Records widget uses the **Start Index** and **Line Count** properties for pagination. Pass the current page offset as a screen Input Parameter and use Previous and Next links to navigate between pages.

1. Select the Table Records widget. In the properties, set **Line Count** to the number of records to display per page.
1. Add a **StartIndex** Input Parameter of the Integer data type to the screen. Set its default value to `0`.
1. Set the **Start Index** property of the Table Records widget to the `StartIndex` Input Parameter.
1. Open the Preparation Aggregate. Set **Max. Records** to `StartIndex + TableRecords.LineCount + 1`. This limits the database query to only the records needed for the current page.
1. Add **Previous** and **Next** Link widgets below the Table Records widget. For each link, set the destination to the same screen and pass a new `StartIndex` value:

    * **Previous**: `StartIndex = StartIndex - TableRecords.LineCount`
    * **Next**: `StartIndex = StartIndex + TableRecords.LineCount`

1. Publish the module.
