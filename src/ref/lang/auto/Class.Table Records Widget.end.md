## Layout of the widget

The layout of this widget follows these rules:

* Each record of the entity or structure corresponds to one row in this widget.

* Each attribute corresponds to one column.

* For each attribute, there is one column with *n+1* rows with the following semantics:

    **First row:** The name of the attribute that corresponds to the "Label" property, if any, or the name of the attribute. You can apply styles to this row, by setting the "Header style" property.

    **Other rows:** The value of the attribute for each record is displayed as a Expression widget and, therefore, you can use the Expression editor to modify it (they can optionally be presented using one of the input widgets to allow editing). You can have different styles in odd and even lines, by setting the "Odd Line style" and "Even Line style" properties.


## Iterating the widget

The entity and/or structure records that you want to display are defined in the "Source Record List" property of this widget, which must be of the List type. Each record of this list is displayed on a different line. The first record that is displayed on the widget corresponds to the "Start Index" position on the list and the number of records displayed depends on the "Line Count" property.

To iterate over the Source Record List, you have to update the "Start Index" property for each iteration by using the "Line Count" and "Start Index" runtime properties of the Table Records widget.


## Additional Notes

* The widget "Id" runtime property is only available in the screen scope if the widget property "Name" is not empty.
* LineCount and StartIndex are very useful to implement the Previous and Next behaviors of a Table Records widget.
