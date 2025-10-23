---
tags: chart implementation, data visualization, outsystems ui, outsystems data layer, user interface design
summary: Learn how to add fixed and variable data to charts in OutSystems 11 (O11) using the DataPointList property.
locale: en-us
guid: 5891D247-9954-4FF7-A2EB-2888EC827A54
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=2409%3A4136&mode=design&t=Ix2yojgoXorQvo4C-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Data

To add data to your chart you must input **DataPoint** labels and values for the **DataPointList** property.

There are two different ways to add data to the **DataPointList** property: **Fixed data** and **Variable data**.

## Populate your chart with fixed data {#populate-your-chart-with-fixed-data}

1. From the Toolbox, drag a Chart to the Screen.

    This example uses the Line Chart.

    ![Screenshot of dragging a Line Chart component to the screen in the development environment](images/chartline-drag-ss.png "Dragging a Line Chart to the Screen")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.  

    ![Screenshot showing the expansion of the DataPointList property in the chart's properties tab](images/chartline-expand-ss.png "Expanding the DataPointList Property")

1. To create a list with one data point, click **+[0]** and set the **Label** and **Value** properties.

    These properties define the first data point of the chart. Each data point corresponds to a point on the chart. Optionally, you can also set the **SeriesName**, **Tooltip**, and **Color** for the data points.

    ![Screenshot of setting the Label and Value properties for a data point in a Line Chart](images/chartline-datapoint-ss.png "Setting Label and Value for Data Points")

1. To add more data points, repeat steps 2 and 3.

After following these steps, you can publish your module.

![Line Chart displayed on the screen with fixed data points added](images/chartline-result-data.png "Line Chart with Fixed Data")

## Populate your chart with variable data {#populate-your-chart-with-variable-data}

Before you start, make sure you have a List of data points to use in your chart. Each data point must include a label and a numerical value.

1. From the Toolbox, drag a Chart to the Screen.

    This example uses the Column Chart.

    ![Screenshot of dragging a Column Chart component to the screen in the development environment](images/chartcolumn-drag-ss.png "Dragging a Column Chart to the Screen")

1. On the **Properties** tab, set the **DataPointList** property to a List containing the data points for the chart.

    ![Screenshot showing the DataPointList property being set to a list of data points in a Column Chart](images/chart-data-datapointlist-ss.png "Setting the DataPointList Property")

1. Map the **Value** and the **Label** of the **DataPointList** to the attributes from the List containing the data points for the chart.

    Optionally, you can also set **DataSeriesName**, **Tooltip**, and **Color** for the data points.

    ![Screenshot of mapping the Value and Label of the DataPointList to attributes from a list in a Column Chart](images/chart-data-mapping-ss.png "Mapping Data Points to List Attributes")

After following these steps, you can publish your module.

![Column Chart displayed on the screen with variable data points added](images/chart-data-result.png "Column Chart with Variable Data")

## Create a chart with multiple series

To create a Chart with multiple series, follow one of the previous procedures and set the **SeriesName** property for the data points.

![Screenshot showing the process of adding multiple series to a chart by setting the SeriesName property](images/chart-data-addseries-ss.png "Adding Multiple Series to a Chart")
![Screenshot of a chart's properties with multiple series added](images/chart-data-multiple-series-ss.png "Chart with Multiple Series")

After following these steps, you can publish your module.

![Example chart displayed on the screen with multiple data series represented](images/chart-example-multiple-series.png "Example of a Chart with Multiple Series")
