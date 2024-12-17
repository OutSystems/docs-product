---
tags: ide usage, reactive web apps, tutorials for beginners, chart creation, data visualization
summary: Learn how to create line and area charts with fixed or variable data points using OutSystems 11 (O11).
locale: en-us
guid: 2b5fe8d2-2a3d-4957-bd07-951d20a824d7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=609:491
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Create Line and Area Charts

Learn how to create a simple Line or Area chart in OutSystems.  
If you are creating your first chart, start with [a Line Chart with a fixed number of data points](#create-a-line-or-area-chart-with-a-fixed-number-of-data-points)

## Create a Line or Area Chart with a fixed number of data points

1. Drag a **Line Chart** or **Area Chart** from the Toolbox to the Screen.

    ![Screenshot showing how to drag a Line Chart or Area Chart from the Toolbox to the Screen in OutSystems](images/line-01.png "Adding a Line or Area Chart to the Screen")

1. On the Property pane of the chart, click **+** to the left of **SourceDataPointList** to create a list with one data point.

    ![Screenshot of the Property pane in OutSystems with the '+' button to add a SourceDataPointList](images/line-02.png "Creating a Data Point List")

1. Click **+** to the left of data point **\[0\]** and set the **Label** and **Value** properties to define the first data point. 
  
    ![Screenshot illustrating the process of setting the Label and Value properties for the first data point in OutSystems](images/line-03.png "Setting Label and Value for the First Data Point")
    ![Screenshot showing additional property settings for the first data point in OutSystems](images/line-04.png "Defining Properties for the First Data Point")

    Optionally, you can also set **DataSeriesName**, **Tooltip** and **Color** for the [data points](../auto/charts-api.final.md#Structure_DataPoint).

1. To add another data point, repeat steps **2** and **3**.

    ![Screenshot demonstrating how to add another data point in the OutSystems Property pane](images/line-07.png "Adding Another Data Point")

After publishing your module you can check your chart by opening the screen in browser or device:

![Example image of a completed Line or Area Chart as displayed in a browser or device after publishing the module](images/line-result.png "Final Line or Area Chart Result")

## Create a Line or Area Chart with a variable number of data points

Before you start, make sure your list of data points is ready to be used in your chart. In the example below, an entity has been created that includes rows for a label and a numerical value.

To create a Line or Area Chart with a variable number of data points follow these steps:

1. Drag a **Line Chart** or **Area Chart** from the Toolbox to the Screen.

    ![Screenshot showing how to drag a Line Chart or Area Chart from the Toolbox to the Screen in OutSystems](images/line-01.png "Adding a Line or Area Chart to the Screen")
    
1. On the Property pane of the chart, set the **SourceDataPointList** property to a List containing the data points for the chart.

    ![Screenshot showing the Property pane where SourceDataPointList is set to a List for a variable number of data points in OutSystems](images/line-a02.png "Setting SourceDataPointList for Variable Data Points")

1. Map the **Label** and **Value** of the **SourceDataPointList** to the correct Attributes from the List containing the data points for the chart.

    ![Screenshot of the process of mapping Label and Value of SourceDataPointList to the correct Attributes in OutSystems](images/line-a03.png "Mapping Label and Value for Data Points")
    
    Optionally, you can also set **DataSeriesName**, **Tooltip** and **Color** for the [data points](../auto/charts-api.final.md#Structure_DataPoint).

After publishing your module you can check your chart by opening the screen in browser or device.

## Create a Line or Area Chart with multiple series

To create a Line or Area Chart with multiple series follow one of the previous procedures and set the **DataSeriesName** property for the data points.

![Screenshot depicting the initial step in creating a Line or Area Chart with multiple series in OutSystems](images/line-ms01.png "Creating a Chart with Multiple Series - Step 1")
![Screenshot showing the process of setting the DataSeriesName property for multiple series in a chart in OutSystems](images/line-ms02.png "Creating a Chart with Multiple Series - Step 2")

After publishing your module you can check your chart by opening the screen in browser or device:

![Example image of a completed Line or Area Chart with multiple series as seen in a browser or device after module publication](images/line-ms-result.png "Final Result of Line or Area Chart with Multiple Series")
