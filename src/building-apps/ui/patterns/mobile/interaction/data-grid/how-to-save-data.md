---
tags: outsystems data grid, save data, client actions, server actions, database
summary: Learn how to save edited data from the OutSystems 11 (O11) Data Grid to a database using client and server actions.
guid: 5650f891-e674-4ae4-a937-92965677b5ae
locale: en-us
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?type=design&node-id=1187%3A354&mode=design&t=bneC7SMvNg6A2EZ4-1
coverage-type:
  - apply
audience:
  - frontend developers
outsystems-tools:
  - none
---
# How to save changes to the OutSystems Data Grid

This example shows how to edit the Grid data and save those changes to the database.

**Prerequisites:**

* Complete [How to edit data in the Grid component](how-to-edit-data.md).

1. Select the Grid component and on the **Properties** tab, enter a **Name**.

    In this example, **ProductGrid** is entered.

    ![Screenshot showing the Name property field with 'ProductGrid' entered as the name of the Grid component.](images/grid-save-name-ss.png "Setting the Name Property of the Grid Component")

1. Add a Save button to the screen.

    In this example, the button is added to the Actions placeholder.

    This button saves the changed data in the grid  to the server's database.

    ![Screenshot depicting the addition of a Save button to the Actions placeholder on the screen.](images/grid-save-button-ss.png "Adding a Save Button to the Screen")

1. On the **Properties** tab, from the **On Click** dropdown, select **New Client Action**.

    ![Screenshot illustrating the selection of 'New Client Action' from the On Click dropdown in the Properties tab.](images/grid-save-clientaction-ss.png "Creating a New Client Action")

1. Add a **Run Client Action** to the flow, select the **GetChangedLines** from the **API_Data folder**, and click **OK**.

    ![Screenshot showing the process of adding a 'Run Client Action' to the flow and selecting 'GetChangedLines' from the API_Data folder.](images/grid-save-runaction-ss.png "Adding Run Client Action to the Flow")

1. Enter the **GridWidgetId**.

    In this example, ProductGrid.Id is entered.

    ![Screenshot displaying the entry of 'ProductGrid.Id' into the GridWidgetId field.](images/grid-save-gridid-ss.png "Entering the GridWidgetId")

1. Add a **JSON Deserialize** to the flow.

    The JSON Deserialize node is added because any data changed in the Grid is in JSON format.

    ![Screenshot showing the JSON Deserialize node added to the flow to handle data in JSON format.](images/grid-save-json-ss.png "Adding JSON Deserialize to the Flow")

1. From the **JSON String** dropdown, select **ChangedLines.EditedLines** of the client action **GetChangedLines**.

    ![Screenshot highlighting the selection of 'ChangedLines.EditedLines' from the GetChangedLines client action for JSON deserialization.](images/grid-save-jsonstring-ss.png "Selecting JSON String for Deserialization")

1. From the **Data Type** dropdown, select **List** and select the relevant element type from the list.

    In this example, the **Sample_Product** aggregate is used so the **Data Type** is **Sample_Product List**.

    ![Screenshot showing the selection of 'Sample_Product List' as the Data Type for JSON deserialization.](images/grid-save-datatype-ss.png "Selecting Data Type for JSON Deserialization")

    **Note:** It is necessary to select the correct **Data Type** to deserialize the changed data.

1. On the **Logic** tab, create a Server Action and add an input parameter. The input parameter receives the data to be updated in the database. Select the input parameter's **Data Type**, in this example, Sample_Product List.

    ![Screenshot illustrating the creation of a Server Action with an input parameter of type 'Sample_Product List'.](images/grid-save-serveraction-ss.png "Creating a Server Action with an Input Parameter")

1. Add the logic that updates the data in the database.

    In this example the following is added:

    | **Logic** | **Property** | **Value** |
    |---|---|---|
    | **For Each**  | Record List | EditedProducts (Input Parameter) |
    | **Run Server Action** | Source | EditedProducts.Current |

    ![Screenshot showing the logic added to update data in the database using a For Each loop and Run Server Action.](images/grid-save-logic-ss.png "Adding Logic to Update Data in the Database")

1. Return to the **Save** button logic and call the **UpdateProducts** server action and set the **EditedProdcuts** to the output of the **JSON Deserialize** node.

    ![Screenshot depicting the call to the 'UpdateProducts' server action and setting the 'EditedProducts' to the output of the JSON Deserialize node.](images/grid-save-callaction-ss.png "Calling the UpdateProducts Server Action")

1. After saving the data in the database, you must remove the change indicator in each of the cells. To do this, call the **MarkChangesAsSaved** API client action and set the **GridWidgetId** to the Grid Id.

    ![Screenshot showing the call to the 'MarkChangesAsSaved' API client action to remove the change indicator from the grid cells.](images/grid-save-removemarks-ss.png "Removing Change Indicators from the Grid")

After following these steps and publishing the module, you can test the component in your app. If you change cell contents and then click Save changes, the data is saved in the database and the change indicator in each of the cells disappear.

**Result**

![Screenshot of the data grid before saving changes, with some cells marked to indicate changes.](images/grid-save-resultbefore-ss.png "Data Grid Before Saving Changes")

![Screenshot of the data grid after saving changes, with the change indicators removed from the cells.](images/grid-save-resultafter-ss.png "Data Grid After Saving Changes")
