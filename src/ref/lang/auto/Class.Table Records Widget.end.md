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