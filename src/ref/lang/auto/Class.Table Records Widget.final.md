---
kinds: ServiceStudio.Model.WebWidgets+TableRecords+Kind, ServiceStudio.Model.WebWidgets+ReferenceTableRecords+Kind
helpids: 4042
summary: Learn how to use the Table Records widget to display the records of an entity or a structure in a tabular layout. Reference.
tags: runtime-traditionalweb
locale: en-us
guid: 8d4c86cd-8f7b-4c79-8dcd-6d4152036b1e
---

# Table Records Widget


You can use the Table Records widget to display the records of an entity or a structure in a tabular layout. You can define the table records as sortable making it easier for the user to read or find information faster. Record sorting can be fixed or dynamic, meaning that it can change during runtime. You can change the emphasis of a table row by changing its height and increase users' ability to read and interpret data in a table record by using zebra stripping. You can also use pagination to divide content and present it in a limited and digestible manner.

![Overview of Table Records widget in use](<images/tablerecords-1-ss.png>)

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

## How to use the Table Records widget

In this example, user data is fetched from the User entity and displayed on screen using the Table Records widget.

1. In Service Studio, in the Toolbox, search for `Table Records`.

    The Table Records widget is displayed.

    ![Table Records widget](<images/tablerecords-2-ss.png>)

1. From the Toolbox, drag the Table Records widget into the Main Content area of your application's screen.

    ![Drag Table Records widget onto screen](<images/tablerecords-3-ss.png>)

1. Add the relevant content to the Table Records widget. 

    In this example, from the **Data** tab, we drag the **User** entity into the Table Records widget. 

    ![Drag User database into widget](<images/tablerecords-4-ss.png>)

1. Return to your screen by selecting the **Interface** tab. Right-click the screen name and select **Add Preparation**.

    ![Add preparation](<images/tablerecords-5-ss.png>)

1. Add an Aggregate to the Preparation.

    ![Add an aggregate](<images/tablerecords-7-ss.png>)

1. Double-click the Aggregate, click the screen, and from the **Select Source** popup, select the database entity you want to retrieve data from. Click **OK**. In this example, we select the User entity.

    ![Select source entity](<images/tablerecords-6-ss.png>)

    The **GetUsers** aggregate is created.

    ![GetUsers aggregate is created](<images/tablerecords-8-ss.png>)

1. Return to your main screen, select the Table Records widget, and on the **Properties** tab, select the Source Record List (in this example, the GetUsers aggregate we just created).

    ![Select Source Record List](<images/tablerecords-9-ss.png>)

After following these steps and publishing the module, you can test the widget in your app.

### How to add a new column

1. Select and right-click the Table Records widget, and select **Table** > **Insert Column to the Left** or **Insert column to the Right**.


    ![Add new column](<images/tablerecords-10-ss.png>)

For more information about the Table Records widget properties, see [Table Records Widget](<../../../ref/lang/auto/Class.Table Records Widget.final.md>).

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Source Record List">Source Record List</td>
<td>Current list of records displayed by the widget.</td>
<td>Yes</td>
<td></td>
<td>The expression used in this property (if present) is evaluated when a widget runtime property is first used (e.g. an expression using the list Length runtime property) or when the widget is rendered.</td>
</tr>
<tr>
<td title="Empty Message">Empty Message</td>
<td>Text displayed in the first row of the widget when there are no records to show.</td>
<td></td>
<td>"No items to show..."</td>
<td></td>
</tr>
<tr>
<td title="Line Count">Line Count</td>
<td>Maximum number of rows to display in this widget.</td>
<td>Yes</td>
<td>50</td>
<td></td>
</tr>
<tr>
<td title="Start Index">Start Index</td>
<td>Index of the first List item to iterate. Can be an expression.</td>
<td>Yes</td>
<td>0</td>
<td>The expression used in this property (if present) is evaluated before the web screen preparation.</td>
</tr>
<tr>
<td title="Cell Height">Cell Height</td>
<td>Height of cells in the table in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Cell Spacing">Cell Spacing</td>
<td>Space between cells in pixels. Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Show Header">Show Header</td>
<td>Set as Yes to display the header row of the table.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords"</td>
<td></td>
</tr>
<tr>
<td title="Header Style">Header Style</td>
<td>Specifies one or more style classes to apply to the header of the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_Header"</td>
<td></td>
</tr>
<tr>
<td title="Odd Line Style">Odd Line Style</td>
<td>Specifies one or more style classes to apply to the odd lines of the widget (excluding the header). Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_OddLine"</td>
<td></td>
</tr>
<tr>
<td title="Even Line Style">Even Line Style</td>
<td>Specifies one or more style classes to apply to the even lines of the widget (excluding the header). Separate multiple values with spaces.</td>
<td></td>
<td>"TableRecords_EvenLine"</td>
<td></td>
</tr>
<tr >
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td>Name of an attribute to add to the HTML translation for this element.</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or type a free text. The name of the property will not be validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>List</td>
<td>Collection of records returned by the performed query.</td>
<td></td>
<td>Record List</td>
<td></td>
</tr>
<tr>
<td>LineCount</td>
<td>Maximum number of rows displayed in the widget as defined in the Line Count property.</td>
<td>Yes</td>
<td>Integer</td>
<td></td>
</tr>
<tr>
<td>StartIndex</td>
<td>Index of the first record displayed in the widget as defined in the Start Index property.</td>
<td>Yes</td>
<td>Integer</td>
<td></td>
</tr>
<tr>
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

## Layout of the widget

The layout of this widget follows these rules:

* Each record of the entity or structure corresponds to one row in this widget.
* Each attribute corresponds to one column.
* For each attribute, there is one column with **n+1** rows with the following semantics:

    **First row:** The name of the attribute that corresponds to the **Label** property, if any, or the name of the attribute. You can apply styles to this row, by setting the **Header style** property.

    **Other rows:** The value of the attribute for each record shows as a Expression widget and, therefore, you can use the Expression editor to modify the content. You can also use the input widgets to allow editing. Set different styles in odd and even lines with **Odd Line style** and **Even Line style** properties.


## Iterating the widget

Set the source data (entity and/or structure records) in the **Source Record List** property of Table Records. The data must be of the List type, and each item of the list shows on a different line. The first record that shows in the widget corresponds to the **Start Index** position on the list. The number of records that the table shows depends on the **Line Count** property.

To iterate over the Source Record List, you have to update the **Start Index** property for each iteration by using the **Line Count** and **Start Index** runtime properties of the Table Records widget.

## Additional notes

* The widget **Id** runtime property is only available in the screen scope when the widget property **Name** isn't empty.
* **LineCount** and **StartIndex** are useful when you want to implement the previous/next behavior of a Table Records widget, because the parameters control how many records you show in the table and from which record number. Scaffold a screen by dragging an Entity to a web flow to get a table with pagination. You can then check out how **LineCount** and **StartIndex** work. 
* If you have an Aggregate in the Preparation that provides a list of records to Table Records and you leave empty the value **Max. Records** of the Aggregate, the platform calculates the value of **Max. Records** for you according to the following formula: **Start Index** of the Table Records + **Line Count** of the table + 1. A workaround is to set a static **Line Count** in the Table Records widget that's at least equal to the maximum number of records your query can retrieve.

