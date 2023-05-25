---
tags:
summary: T
locale: en-us
guid: 63FB9BE0-A9BA-4173-8BF2-8049B69DCC6B
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Bar Chart

This example shows how you can create a simple Bar Chart with a customized legend.

1. From the Toolbox, drag the **Bar Chart** widget to the Screen.

    ![Drag the Bar Chart widget to the screen ](images/chartbar-drag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartbar-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the bar chart.

    ![Set the Position and Layout properties](images/chartbar-datapoint-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

1. To customize the legend, in the **AddOns** placeholder, click **ChartLegend**, and on the **Properties** tab, set the **Position** property to **Entities.LegendPosition.TopRight** and the **Layout** to **Entities.LegendLayout.Vertical**.

    ![Set the Position and Layout properties](images/chartbar-addon-ss.png)

1. Set the extra configurations to customize the legend.

    ![Customize the legend](images/chartbar-customize-ss.png)

After following these steps, you can publish your module:

![Example Bar Chart](images/chartbar-result.png)


