---
tags:
summary: Learn how to create a simple Column Chart with data labels.
locale: en-us
guid: A1458CB9-862F-4F78-B823-E1D0A3453FDE
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=2415:4179
---

# Column Chart

This example shows how to create a simple Column Chart with data labels.

1. From the Toolbox, drag the **Column Chart** widget to the Screen.

    ![Drag the Column Chart widget to the screen ](images/chartcolumn-drag-ss.png)

1. On the **Properties** tab, click **[+]** to expand the **DataPointList** property.

    ![Expand the Data Point List property](images/chartcolumn-expand-ss.png)

1. Click **+[0]** and set the **Label** and **Value** properties using [fixed data](chart-data-v2.md#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2.md#populate-your-chart-with-variable-data). 

    This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the column chart. 

    ![Set datapoint](images/chartcolumn-datapointlist-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

    ![Add more data points](images/chartcolumn-extradatapoints-ss.png)

1. To show the values of each data point, click on the **SeriesStyling** in the **AddOns** placeholder, and on the **Properties** tab, set the **ShowDataPointValues** property to **True**.

    Since the **SeriesName** property was not set, this property will be applied to all series.

    ![Show data point values](images/chartcolumn-showdatapoint-ss.png)

After following these steps, you can publish your module:

![Example Area Chart](images/chartcolumn-result.png)

