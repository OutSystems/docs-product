---
summary: Import data from Excel files to quickly have your data up and running in the application while developing it.
tags: support-Database; support-database-featured
---

# Bootstrap an Entity Using an Excel File

You can import data from an Excel file to load data to an entity. This is useful when you are developing and testing your application. This way, you can quickly have your data up and running in the application while developing it.

## Validate the Excel file

1. Open the Excel file, check that the Excel sheet has the name of the Entity and the column headers have the names of the entity attributes.

1. Close the Excel file. The bootstrap can't read the Excel file if it's open.

If your spreadsheet has blank cells and you're getting import errors, check [this How-to Guide](https://success.outsystems.com/Documentation/How-to_Guides/How_to_bootstrap_numeric_data_from_Excel_with_blank_cells) on how to proceed.

## Bootstrap the data

To bootstrap data from the first sheet of an Excel file to an existing entity, follow these steps:

1. In Service Studio, go to the Data tab, right-click on the entity and in the Advanced menu, choose 'Create Action to Bootstrap data from an Excel...'. 

1. Select the Excel file, check the mappings to see if they're correct and click on **Proceed**.
    Service Studio creates:

    * An action with the bootstrap logic named "Bootstrap&lt;entityname&gt;" in the Server Actions folder in the Logic tab.

    * A structure with the content of the Excel file named "Excel_&lt;filename&gt;" in the Structures folder in the Data tab.

    * A resource with the Excel file in the Resources folder in the Data tab.

    * A timer to execute the action at publish time named "Bootstrap&lt;entityname&gt;" in the Timers folder in the Processes tab.

1. Publish to bootstrap the data.

When you publish the module, it executes the action to bootstrap the data. If the entity already has data, the action with the bootstrap logic is **not** executed.

## Demo/Sample

Check this demo on how to bootstrap your data from an Excel file, and [download the Sample](resources/BootstrapFromExcel.oml) and the [sample data](resources/SampleData.xls) used in it.

<iframe width="750" height="500" src="https://www.youtube.com/embed/pIeuSPahI9o" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>
