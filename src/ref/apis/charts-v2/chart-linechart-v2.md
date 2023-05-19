---
tags:
summary: Learn how to create a simple Line Chart with a Spline line and custom markers in OutSystems.
locale: en-us
guid: 0A9D1277-D008-4B96-8BCF-F559BEE3374C
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Line Chart

This example shows how you can create a simple Line Chart with a Spline line and custom markers.

1. From the Toolbox, drag the **Line Chart** widget to the Screen.

    ![Drag the Line Chart widget to the screen ](images/chartline-drag-ss.png)

1. On the **Property** tab, expand the **DataPointList** -> **[0]** property and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the line chart. 

    ![Set datapoint](images/chartline-datapoint-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

    ![Add more data points](images/chartline-extradatapoints-ss.png)

1. To enable the Spline Line, set the **Spline** property to **True**.

    ![Set the Spline property](images/chartline-spline-ss.png)

1. To customize a Series, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this case, **Series 1**).

    ![Select the series to customize](images/chartline-addon-ss.png)

1. Expand the **Marker** property and set the extra configurations to customize the marker.

    ![SSet marker properties](images/chartline-marker-ss.png)

After following these steps, you can publish your module:

![Example Line Chart](images/chartline-result.png)
