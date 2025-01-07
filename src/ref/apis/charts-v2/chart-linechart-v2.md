---
tags: ide usage, reactive web apps, tutorials for beginners, chart implementation, data visualization, design integration, spline charts, custom markers
summary: Learn how to create a Line Chart with a Spline line and custom markers using OutSystems 11 (O11).
locale: en-us
guid: 0A9D1277-D008-4B96-8BCF-F559BEE3374C
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2421:4216
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Line Chart

This example shows how you can create a simple Line Chart with a Spline line and custom markers.

1. From the Toolbox, drag the **Line Chart** widget to the Screen.

    ![Screenshot of dragging the Line Chart widget onto the screen in OutSystems](images/chartline-drag-ss.png "Dragging Line Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot showing the expansion of the DataPointList property in OutSystems](images/chartline-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the line chart. 

    ![Screenshot of setting Label and Value properties for a data point in OutSystems Line Chart](images/chartline-datapoint-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot where the SeriesName property is being set in OutSystems Line Chart](images/chart-seriesname-ss.png "Setting SeriesName Property")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot illustrating the addition of extra data points to the Line Chart in OutSystems](images/chartline-extradatapoints-ss.png "Adding Additional Data Points")

1. To enable the Spline Line, set the **Spline** property to **True**.

    ![Screenshot showing the Spline property set to True to enable Spline Line in OutSystems Line Chart](images/chartline-spline-ss.png "Enabling Spline Line")

1. To customize a Series, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this case, **Series 1**).

    ![Screenshot of SeriesStyling customization for Series 1 in OutSystems Line Chart](images/chartline-addon-ss.png "Customizing Series with SeriesStyling")

1. Expand the **Marker** property and set the extra configurations to customize the marker.

    ![Screenshot displaying the customization options for the marker in OutSystems Line Chart](images/chartline-marker-ss.png "Customizing Chart Marker")

After following these steps, you can publish your module:

![Image of the final result of a Line Chart with a Spline line and custom markers in OutSystems](images/chartline-result.png "Final Line Chart Result")
