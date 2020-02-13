---
summary: Component with widgets for plotting charts in web apps.
tags: support-application_development; support-Front_end_Development
---

The OutSystems API for plotting charts.

You can create a chart by dragging a chart widget to the screen. The widget property `SourceDataPointList` is the list consisting of the `DataPoint` elements. The `DataPoint` element defines drawing of the chart: `Label`, `Value`, `DataSeriesName`, `Tooltip` and `Color`. You need to provide values to the `DataPoint`, and in charts with more than one series, you need to specify each series you want to represent in the chart.

OutSystems uses Highcharts 6.1.0 to generate the charts, and you should consult the [Highcharts documentation](https://api.highcharts.com/highcharts/) for implementation and the API.
