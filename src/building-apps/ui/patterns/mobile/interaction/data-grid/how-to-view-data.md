---
tags: outsystems data grid, data management, display data, reactive web apps, service studio
summary: Learn how to display and manage data using the OutSystems Data Grid (O11) component in OutSystems 11.
guid: cca0de21-e1fb-452f-9ff7-c73b55b3c287
locale: en-us
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?type=design&node-id=1142%3A332&mode=design&t=bneC7SMvNg6A2EZ4-1
coverage-type:
  - apply
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
---
# How to use the OutSystems Data Grid

**Prerequisites** 

* Download and install the [OutSystems Data Grid (O11)](https://www.outsystems.com/forge/component-overview/9764/data-grid-reactive) component from Forge.

This example fetches data from a database and displays it in the grid. (This example does not define any column structure.) 

1. In Service Studio, in the Toolbox, search for Grid.

    The Grid widget is displayed.

    ![Screenshot showing the Grid widget in the Service Studio toolbox.](images/grid-widget-ss.png "Grid Widget in Service Studio")

1. From the Toolbox, drag the Grid widget into the Main Content area of your application's screen.

    ![Screenshot illustrating the process of dragging the Grid widget into the Main Content area of an application screen.](images/grid-widget-drag-ss.png "Dragging Grid Widget into Main Content")

    By default, the Grid widget contains the following placeholders:

    * ContextMenu
    * Loading (displayed while data is being fetched from the server)
    * NoResults (displayed when no results are returned)
    * GridColumns

    ![Screenshot displaying the default placeholders within the Grid widget, including ContextMenu, Loading, NoResults, and GridColumns.](images/grid-placeholders-ss.png "Default Grid Widget Placeholders")

    You can change the content of these placeholders as required.

1. Create a Data Action to fetch the data you want to display in the grid.

    ![Screenshot showing the creation of a Data Action to fetch data for the grid.](images/grid-fetch-data-ss.png "Creating a Data Action")

1. Enter a name for the Action's output parameter (for example, Data) and ensure the **Data Type** is **Text**.

    This output parameter is used to receive the data fetched from the database.

    ![Screenshot of the output parameter settings for a Data Action with the Data Type set to Text.](images/grid-output-par-ss.png "Setting Output Parameter for Data Action")

1. On the **Data** tab, drag the data source entity onto the flow.

    ![Screenshot showing the process of dragging a data source entity onto the flow in Service Studio.](images/grid-drag-entity-ss.png "Dragging Data Source Entity")

    An aggregate (in this example, GetProducts) is automatically created. 

1. On the **Logic** tab, drag the **ArrangeData** Server Action onto the flow.

    The **Grid** block receives data in JSON format. The **ArrangeData** Server Action (**only available for O11**) analyzes this data, serializes it, and retrieves the information from each column, whether it be in, for example, string, number, or boolean format.

    ![Screenshot depicting the ArrangeData Server Action being dragged onto the flow to format data for the grid.](images/grid-arrange-data-ss.png "ArrangeData Server Action in Flow")

1. Set the **Data Action** property to the aggregate result. 

    All of the aggregate data is passed to the action.

    **Note:** Because the **ArrangeData** Server Action action can receive any data structure, you must use the **ToObject** function. **ArrangeData is only available for O11**.

    ![Screenshot showing the Data Action property being set to the result of an aggregate in the flow.](images/grid-aggregate-result-ss.png "Setting Data Action Property to Aggregate Result")

1. Drag an **Assign** onto the flow and set the **Data** action output parameter to the **ArrangeData.DataJSON** property.

    ![Screenshot of an Assign step in the flow setting the Data action output parameter to the ArrangeData.DataJSON property.](images/grid-set-assign-ss.png "Assigning DataJSON to Data Action Output")

1. Return to the main screen and select the Grid. On the **Properties** tab, set the **Data** property to the output of the Data Action you created earlier (step. 3).

    ![Screenshot showing the Grid's Data property being set to the output of a previously created Data Action.](images/grid-data-prop-ss.png "Setting Grid Data Property")

1. Bind the Grid's **IsDataFetched** property to the Data Action property **IsDataFetched**.

    ![Screenshot illustrating the binding of the Grid's IsDataFetched property to the Data Action's IsDataFetched property.](images/grid-isdata-fetched-ss.png "Binding IsDataFetched Property")

After following these steps and publishing the module, you can test the component in your app.

**Result**

![Screenshot of the final result showing data displayed in the OutSystems Data Grid component.](images/grid-result-ss.png "Data Grid Component Result")

## Properties

| **Properties** | **Description** |
|---|---|
| Data (Text): Mandatory  | The data displayed in the Grid.  |
| IsDataFetched (Boolean): Mandatory | Defines what is displayed while data is loading. | 
| GridHeight (Integer): Optional  |  Sets the Grid's height in pixels. Default height is 400 pixels. |  
| HasGroupPanel (Boolean): Optional  | Enables the group panel to allow dragging columns and apply the grouping by the fields corresponding to the dragged columns. Default value is True. |  
| AllowColumnEdit (Boolean): Optional  | Allows columns to be edited. Default value is False.  |   
| AllowColumnReorder (Boolean): Optional  | Allows columns to be reordered. Default value is True. | 
| AllowColumnResize (Boolean): Optional  | Allows column width to be resized. Default value is True. |  
| AllowColumnSort (Boolean): Optional  | Allows sorting data by column. Default value is True. | 
| KeyBinding (Text): Optional  | Set the primary key field of the data. Expected format: 'Entity.Attribute'. <br/>Use this field when doing Server-side validations. <br/>Don’t want to refresh the grid after adding lines. Combine with UpdateAddedLineKey and GetRowNumberByKey actions. | 
| RowHeight (Integer): Optional  | Sets the row height in pixels. Default height is 48 pixels. | 
| RowsPerPage (Integer): Optional  | Sets the number of rows displayed per page. Default value is 50.| 
| ShowAggregateValues (Boolean): Optional  | Set to True to display a line below the grid with the column values aggregated (sum, min, max, etc.). <br/>By default, the parameter is set to False. <br/>To define the aggregation function of a given numeric (Number or Currency) column, use the SetColumnAggregate client action.| 
| SanitizeInputValues (Boolean): Optional  | Set True to assure the values inputed in the grid will be sanitized or False if you want to explicitly allow custom code to run.| 
| ServerSidePagination (Boolean): Optional  | Set to True if you want to enable server-side pagination. By default, False.| 
| RowHeader (RowHeader Identifier): Optional  | Defines what is shown on the first column of the grid. Default value is *Entities.RowHeader.RowNumber*.| 

