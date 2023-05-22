---
tags:
summary: The Charts API v2 allows you to create, populate, and customize charts.
locale: en-us
guid: CA58D796-3D68-4221-8DD8-33049ACEA9E5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Charts API v2

<div class="info" markdown="1">

Available from OutSystems Charts v3.0.0. For more information on how to use the new version of Charts, see the [OutSystems Charts Sample](https://charts.outsystems.com/).

</div>

The Charts API v2 allows you to create, populate, and customize charts. OutSystems uses Highcharts 11.0.0 to generate the charts. For more information about implementation and the API, see the [Highcharts documentation](https://api.highcharts.com/highcharts/).


## Charts

OutSystems provides a collection of charts that allow you to build your screens with a simple drag-and-drop from Service Studio’s toolbox.

|Widget|Description |
|---|---|
|Area Chart|The Area Chart is composed of data points plotted and connected by a line with a colored area below the line.|
|Bar Chart|The Bar Chart is a simple, two-dimensional chart where rectangular bars are placed along the X Axis with bar length representing the value for a specific category.|
|Column Chart|The Column Chart is a two-dimensional chart where rectangular bars are placed along the Y Axis with bar height representing the value for a specific category.|
|Donut Chart|The Donut Chart is a circular graph that displays data in rings, where each ring represents a category and the size of the ring corresponds to the value of the data being presented.|
|Line Chart|The Line Chart is a simple, two-dimensional chart where each point represents a single value. The data points are joined by a line to depict a trend, usually a period of time.
|Pie Chart|The Pie Chart is a circular graph that displays data in sections, where each section represents a category and the size of the section corresponds to the value of the data being presented.|
|Radar Chart|The Radar Chart, also known as a polar chart, illustrates multivariate data in a two-dimensional chart, plotted along a radial axis.|

## Addons

You can enrich your charts with addons to customize their elements, such as axes, legends, and series styles.

|Widget|Description|
|---|---|
|ChartXAxis|Chart addon used to customize the horizontal axis of the chart. However, if the chart is inverted, this is the vertical axis (for example, the Bar Chart).|
|ChartYAxis|Chart addon used to customize the vertical axis of the chart. However, if the chart is inverted, this is the horizontal axis (for example, the Bar Chart).|
|ChartLegend|Chart addon used to customize the box containing a symbol and a name for each series or data point in the chart.|
|ChartSeriesStyling|Chart addon used to customize the styling of the chart series. You can bind it to a specific series or apply the styles to all of them.|

## APIs

Collection of all client actions that trigger the API methods to customize and extend the charts and addon blocks.

|Widget|Description|
|---|---|
|SetHighchartsChartConfigs|Extend the chart block properties with additional Highcharts configurations. You can find all Highcharts chart properties [here](https://api.highcharts.com/highcharts/).|
|SetHighchartsXAxisConfigs|Extend the x-axis properties with additional Highcharts configurations. You can find all Highcharts chart properties [here](https://api.highcharts.com/highcharts/xAxis).|
|SetHighchartsYAxisConfigs|Extend the y-axis properties with additional Highcharts configurations. You can find all Highcharts chart properties [here](https://api.highcharts.com/highcharts/yAxis).|
|SetHighchartsSeriesConfigs|Extend the series properties with additional Highcharts configurations. You can find all Highcharts chart properties [here](https://api.highcharts.com/highcharts/series).|
