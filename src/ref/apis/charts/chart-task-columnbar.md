---
tags:
summary: Explore how to create column and bar charts in OutSystems 11 (O11) using fixed or variable data points and multiple series.
locale: en-us
guid: 7115204b-9a1e-42f8-87f8-d1d771608667
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=609:478
---
# Create Column and Bar Charts

Learn how to create a simple Column or Bar chart in OutSystems.
If you are creating your first chart, start with [a Column Chart with a fixed number of columns](#create-a-column-or-bar-chart-with-a-fixed-number-of-columns-or-bars)

## Create a Column or Bar Chart with a fixed number of columns or bars

1. Drag a **Column Chart** or **Bar Chart** from the Toolbox to the Screen.

    ![Screenshot showing how to drag a Column Chart or Bar Chart from the Toolbox to the Screen in OutSystems.](images/col-01.png "Adding a Column or Bar Chart to the Screen")

1. On the Property pane of the chart, click **+** to the left of **SourceDataPointList** to create a list with one data point.

    ![Image illustrating the addition of a new SourceDataPointList by clicking the plus icon in the Property pane of the chart.](images/col-02.png "Creating a Source Data Point List")

    Each data point corresponds to one column or bar of the chart.

1. Click **+** to the left of data point **\[0\]** and set the **Label** and **Value** properties to define the first data point. 
  
    ![Screenshot of the OutSystems interface where the Label property for a data point is being set.](images/col-03.png "Setting the Label Property for a Data Point")
    ![Screenshot of the OutSystems interface where the Value property for a data point is being set.](images/col-04.png "Setting the Value Property for a Data Point")

    Optionally, you can also set **DataSeriesName**, **Tooltip** and **Color** for the [data points](../auto/charts-api.final.md#Structure_DataPoint).

1. To add another data point, repeat steps **.2** and **.3**.

    ![Image showing the process of adding another data point in the OutSystems chart Property pane.](images/col-07.png "Adding Additional Data Points")

After publishing your module you can check your chart by opening the screen in browser or device:

![Final result of a Column or Bar Chart displayed in a browser or device after publishing the module.](images/col-result.png "Final Column or Bar Chart Result")

## Create a Column or Bar Chart with a variable number of columns or bars

Before you start, make sure your List of data points is ready to be used in your chart: each data point must include a label and a numerical value.

To create a Column or Bar Chart with a variable number of columns or bars follow these steps:

1. Drag a **Column Chart** or **Bar Chart** from the Toolbox to the Screen.

    ![Screenshot showing how to drag a Column Chart or Bar Chart from the Toolbox to the Screen in OutSystems.](images/col-01.png "Adding a Column or Bar Chart to the Screen")
    
1. On the Property pane of the chart, set the **SourceDataPointList** property to a List containing the data points for the chart.

    ![Image depicting the setting of the SourceDataPointList property to a list of data points in the chart's Property pane.](images/col-a02.png "Setting the SourceDataPointList Property")

1. Map the **Label** and **Value** of the **SourceDataPointList** to the correct Attributes from the List containing the data points for the chart.

    ![Screenshot showing the mapping of Label and Value attributes from the SourceDataPointList to the chart in OutSystems.](images/col-a03.png "Mapping Label and Value for Data Points")
    
    Optionally, you can also set **DataSeriesName**, **Tooltip** and **Color** for the [data points](../auto/charts-api.final.md#Structure_DataPoint).

After publishing your module you can check your chart by opening the screen in browser or device.

## Create a Column or Bar Chart with multiple series

To create a Column or Bar Chart with multiple series follow one of the previous procedures and set the **DataSeriesName** property for the data points.

![Image illustrating the first step in creating a Column or Bar Chart with multiple series in OutSystems.](images/col-ms01.png "Column or Bar Chart with Multiple Series - Step 1")
![Image illustrating the second step in creating a Column or Bar Chart with multiple series by setting the DataSeriesName property.](images/col-ms02.png "Column or Bar Chart with Multiple Series - Step 2")

After publishing your module you can check your chart by opening the screen in browser or device:

![Final result of a Column or Bar Chart with multiple series as seen in a browser or device after module publication.](images/col-ms0-result.png "Final Result of Column or Bar Chart with Multiple Series")
