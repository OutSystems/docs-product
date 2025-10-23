---
tags: ide usage, reactive web apps, tutorials for beginners, chart visualization, data binding
summary: Learn how to create and customize a Bar Chart with a legend in OutSystems 11 (O11) using fixed or variable data.
locale: en-us
guid: 63FB9BE0-A9BA-4173-8BF2-8049B69DCC6B
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2453:4384
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Bar Chart

This example shows how you can create a simple Bar Chart with a customized legend.

1. From the Toolbox, drag the **Bar Chart** widget to the Screen.

    ![Screenshot showing the Bar Chart widget being dragged onto the screen in the development environment](images/chartbar-drag-ss.png "Dragging Bar Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show options](images/chartbar-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the bar chart.

    ![Screenshot demonstrating how to set the Label and Value properties for a data point in the Bar Chart](images/chartbar-datapoint-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property field in the Bar Chart widget properties](images/chart-seriesname-ss.png "Setting SeriesName Property")

1. To add more data points, repeat steps 2 and 3.

1. To customize the legend, in the **AddOns** placeholder, click **ChartLegend**, and on the **Properties** tab, set the **Position** property to **Entities.LegendPosition.TopRight** and the **Layout** to **Entities.LegendLayout.Vertical**.

    ![Screenshot of the AddOns placeholder with the ChartLegend selected and Properties tab open](images/chartbar-addon-ss.png "ChartLegend AddOn Configuration")

1. Set the extra configurations to customize the legend.

    ![Screenshot showing the extra configuration options for customizing the chart legend](images/chartbar-customize-ss.png "Customizing Chart Legend")

After following these steps, you can publish your module:

![Image of the final result of the Bar Chart with customized legend after publishing the module](images/chartbar-result.png "Final Bar Chart Result")
