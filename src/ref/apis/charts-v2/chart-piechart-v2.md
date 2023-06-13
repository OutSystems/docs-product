---
tags:
summary: Learn how to create a simple Pie Chart showing the labels of the data points.
locale: en-us
guid: 58AC97D9-F40C-4B66-825B-4E0D3F6CD41E
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Pie Chart

This example shows how you can create a simple Pie Chart showing the labels of the data points instead of the legend.

1. From the Toolbox, drag the **Pie Chart** widget to the Screen.

    ![Drag the Pie Chart widget to the screen ](images/chartpiedrag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartpie-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a slice on the pie chart. 

    ![Set datapoint](images/chartpie-datapointlist-ss.png)

1. To add more data points, repeat steps 2 and 3.
    
    ![Add more datapoint](images/chartpie-extrapoints-ss.png)

1. To show each of the data point values, in the **AddOns** placeholder, click **SeriesStyling**, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    **Note**: Since the **SeriesName** property was not set, this property is applied to all of the series.

    ![Show data point values](images/chartpie-datapointvalues-ss.png)

1. To remove the chart legend, delete the **Chart Legend** Addon.

    ![Delete legend](images/chartpie-delete-legend-ss.png)

After following these steps you can publish your module:


![DResult](images/chartpie-result.png)
