---
tags: chart visualization, data visualization, ui design, widget configuration, data binding
summary: Learn how to create a stacked area chart in OutSystems 11 (O11) using the Area Chart widget and configuring data points and series properties.
locale: en-us
guid: BA3C3E2A-BFD3-454E-B527-00AAE44DEA8F
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2411:4149
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Area Chart

This example shows how you can create a simple Area Chart with a Stacked Series.

1. From the Toolbox, drag the **Area Chart** widget to the Screen.

    ![Screenshot showing the process of dragging the Area Chart widget onto the screen in OutSystems](images/chartarea-drag-ss.png "Dragging Area Chart Widget")

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Screenshot of the Properties tab with the DataPointList property expanded in OutSystems](images/chartarea-expand-ss.png "Expanding DataPointList Property")

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the area chart. 

    ![Screenshot illustrating how to set the Label and Value properties for a data point in an Area Chart in OutSystems](images/chartarea-datapointlist-ss.png "Setting Data Point Properties")

1. Set the **SeriesName** property.

    ![Screenshot showing the SeriesName property field in the Area Chart widget properties in OutSystems](images/chart-seriesname-ss.png "Setting Series Name Property")

1. To add more data points, repeat steps 2 and 3.

    ![Screenshot demonstrating how to add additional data points to the Area Chart in OutSystems](images/chartarea-extradatapoints-ss.png "Adding Extra Data Points")

1. To enable the Stacked Series, set the **StackingType** property to **Entities.StackingType.Stacked**.

    ![Screenshot depicting the StackingType property set to Stacked in the Area Chart widget in OutSystems](images/chartarea-stackingtype-ss.png "Enabling Stacked Series")

After following these steps, you can publish your module:

![Screenshot of the final result of an Area Chart with Stacked Series in OutSystems](images/chartarea-result.png "Final Area Chart Result")
