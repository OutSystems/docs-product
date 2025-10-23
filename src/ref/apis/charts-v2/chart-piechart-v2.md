---
tags: ide usage, reactive web apps, tutorials for beginners, data visualization, chart configuration
summary: Learn how to create a labeled Pie Chart without a legend in OutSystems 11 (O11) using the Pie Chart widget and data point customization.
locale: en-us
guid: 58AC97D9-F40C-4B66-825B-4E0D3F6CD41E
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2526:4533
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Pie Chart

This example shows how you can create a simple Pie Chart showing the labels of the data points instead of the legend.

1. From the Toolbox, drag the **Pie Chart** widget to the Screen.

    ![Screenshot showing the Pie Chart widget being dragged to the Screen in the development environment.](images/chartpiedrag-ss.png "Dragging Pie Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to add data points.](images/chartpie-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a slice on the pie chart.

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Pie Chart.](images/chartpie-datapointlist-ss.png "Setting Data Point Properties")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot showing the process of adding additional data points to the Pie Chart.](images/chartpie-extrapoints-ss.png "Adding Additional Data Points")

1. To show each of the data point values, in the **AddOns** placeholder, click **SeriesStyling**, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    **Note**: Since the **SeriesName** property was not set, this property is applied to all of the series.

    ![Screenshot of the SeriesStyling section where ShowDataPointValues property is set to True to display data point values on the Pie Chart.](images/chartpie-datapointvalues-ss.png "Enabling Data Point Values Display")

1. To remove the chart legend, delete the **Chart Legend** Addon.

    ![Screenshot depicting the deletion of the Chart Legend Addon from the Pie Chart.](images/chartpie-delete-legend-ss.png "Removing Chart Legend")

After following these steps, you can publish your module:

![Image of the final Pie Chart with labels on data points and without a legend, as seen in the published module.](images/chartpie-result.png "Final Pie Chart Result")
