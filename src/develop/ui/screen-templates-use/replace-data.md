---
summary: Replace data in Screens created from Screen Templates with your data. The replacement can be manual or semi-automatic.
---

# Replace the sample data in Screens created from Screen Templates

You can replace the Sample Data either manually or semi-automatically, in a Screen you create from a Screen Template. The manual replacement involves editing the data sources and updating the UI references, and can be assisted by the semi-automated replacement.

## Manual replacement of Sample Data

Use the manual replacement when you want full control over the changes in the Screen. Here are some examples of the manual replacement steps.

1. Remove the UI elements that you don't need. This minimizes the number of warnings in the later steps.
2. Delete the Sample Data references. In the Element Tree, locate the Screen you want to edit. Remove the source of the data: in a Traditional Web App, open the aggregates inside the **Preparation** Action and delete the source entries inside the aggregates; in a Mobile App, delete the source entries inside the aggregates assigned to the Screen.
3. Insert the entries for new sources.
4. Replace the data references.
5. Review the errors and warnings in the **TrueChange** pane. Double-click on each, and fix them by assigning a valid variable or by deleting the associated Widget.

## Semi-automatic replacement of Sample Data

The semi-automatic replacement works by dragging and dropping an Entity to the Widget that supports the automatic data replacement. Sometimes the labels associated with the data in your Screen are also replaced. The semi-automatic replacement is designed as an assistance to the manual data replacement and it does not always result in best matches. 

When replacing the data inside the Screen created from a Screen Template, you can only replace server data with server data, and local data with local data. The drag and drop data replacement accelerators do not work with the mixed data sources.

1. Drag and drop the Entity, that has the data you want to use over the Widget for which you want to replace the data.
2.  Check the **TrueChange** tab for errors and warnings and fix them.
3.  Verify the Widget labels correspond to the data and edit the labels or Expressions if needed.

For more information about importing data from an Excel file to an entity, see [Bootstrap an Entity Using an Excel File](../../data/excel-bootstrap.md)
