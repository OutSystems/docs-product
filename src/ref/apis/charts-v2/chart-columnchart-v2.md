---
tags: chart visualization, data visualization, ui components, web development, outsystems widgets
summary: Learn how to create a column chart with data labels in OutSystems 11 (O11) using the Column Chart widget and configuring properties for data visualization.
locale: en-us
guid: A1458CB9-862F-4F78-B823-E1D0A3453FDE
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2415:4179
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Column Chart

This example shows how to create a simple Column Chart with data labels.

1. From the Toolbox, drag the **Column Chart** widget to the Screen.

    ![Screenshot showing the Column Chart widget being dragged onto the screen in the development environment](images/chartcolumn-drag-ss.png "Dragging Column Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded to show its options](images/chartcolumn-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data).

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the column chart.

    ![Screenshot illustrating how to set the Label and Value properties for a data point in the Column Chart](images/chartcolumn-datapointlist-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property field in the Properties tab for the Column Chart](images/chart-seriesname-ss.png "Setting SeriesName Property")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add more data points to the Column Chart by repeating previous steps](images/chartcolumn-extradatapoints-ss.png "Adding Additional Data Points")

1. To show the values of each data point, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    Since the **SeriesName** property was not set, this property will be applied to all series.

    ![Screenshot of the SeriesStyling section where ShowDataPointValues property is set to True to display data point values](images/chartcolumn-showdatapoint-ss.png "Enabling Data Point Values Display")

After following these steps, you can publish your module:

![Image of the final result showing a published Column Chart with data labels](images/chart-column-result.png "Final Column Chart Result")
