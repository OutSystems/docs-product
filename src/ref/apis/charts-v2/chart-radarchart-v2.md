---
tags: data visualization, chart configuration, ui components, widget usage, visual design
summary: Learn how to create and customize a Radar Chart in OutSystems 11 (O11) using fixed or variable data and series styling options.
locale: en-us
guid: C623895D-2A0A-4259-9B65-88C68142E2C9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2534:4614
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Radar Chart

This example shows how you can create a simple Radar Chart with multiple series types.

1. From the Toolbox, drag the **Radar Chart** widget to the Screen.

    ![Screenshot showing the Radar Chart widget being dragged onto the screen in the development environment](images/chartradardrag-ss.png "Dragging Radar Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show options](images/chartradar-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the radar chart.  

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Radar Chart](images/chartradar-datapoint-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property field in the Radar Chart widget's Properties tab](images/chartradar-seriesname-ss.png "Setting SeriesName Property")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add more data points to the Radar Chart by repeating previous steps](images/chartradar-extra-datapoints-ss.png "Adding Additional Data Points")

1. To customize a Series, in the AddOns placeholder, click **SeriesStyling** and on the **Properties** tab, set the **SeriesName** property to the Series you want to customize (in this example, Series 3).

    ![Screenshot of the SeriesStyling option in the AddOns placeholder used to customize a series in the Radar Chart](images/chartradar-customize-series-ss.png "Customizing a Series in Radar Chart")

1. To customize the Series type, on the **Properties** tab, set the **SeriesType** to **Entities.SeriesType.Area**. This sets the Series type to Area.  

    ![Screenshot showing the SeriesType property set to Entities.SeriesType.Area in the Radar Chart Properties tab](images/chartradar-series-type-ss.png "Setting Series Type to Area")

After following these steps, you can publish your module:

![Image of the final Radar Chart result after publishing the module](images/chartradar-result.png "Final Radar Chart Result")
