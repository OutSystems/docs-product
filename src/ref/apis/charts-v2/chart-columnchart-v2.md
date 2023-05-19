---
tags:
summary: Learn how to create a simple Column Chart with data labels.
locale: en-us
guid: A1458CB9-862F-4F78-B823-E1D0A3453FDE
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Column Chart

This example shows how to create a simple Column Chart with data labels.

1. From the Toolbox, drag the **Column Chart** widget to the Screen.

    ![Drag the Column Chart widget to the screen ](images/chartcolumn-drag-ss.png)

1. On the **Property** tab, expand the **DataPointList** -> **[0]** property and set the **Label** and **Value** properties using [fixed data](chart-data-v2#populate-your-chart-with-fixed-data) or [variable data](chart-data-v2#populate-your-chart-with-variable-data). This example uses fixed data. These properties define the first data point. Each data point corresponds to a point on the column chart. 

    ![Set datapoint](images/chartcolumn-datapointlist-ss.png)

1. Set the **SeriesName** property.

    ![Set the series name](images/chart-seriesname-ss.png)

1. To add more data points, repeat steps 2 and 3.

    ![Add more data points](images/chartcolumn-extradatapoints-ss.png)



After following these steps, you can publish your module:

![Example Area Chart](images/chartcolumn-result.png)

