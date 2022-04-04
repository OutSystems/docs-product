---
summary: Component with widgets for plotting charts in web apps.
tags: article-page; support-application_development; support-Front_end_Development
---

# Charts API


The OutSystems API for plotting charts.

You can create a chart by dragging a chart widget to the screen. The widget property `SourceDataPointList` is the list consisting of the `DataPoint` elements. The `DataPoint` element defines drawing of the chart: `Label`, `Value`, `DataSeriesName`, `Tooltip` and `Color`. You need to provide values to the `DataPoint`, and in charts with more than one series, you need to specify each series you want to represent in the chart.

OutSystems uses Highcharts 9.1.2 to generate the charts, and you should consult the [Highcharts documentation](https://api.highcharts.com/highcharts/) for implementation and the API.

## Summary

Widget | Description
---|---
[AreaChart](<#AreaChart>) | Area charts illustrate the contribution of values to a total over time.
[BarChart](<#BarChart>) | Bar charts compare multiple values using horizontal bars.<br/>In this chart, the X-axis runs vertically and the Y-axis runs horizontally.
[ColumnChart](<#ColumnChart>) | Column charts compare multiple values using vertical bars.
[LineChart](<#LineChart>) | Line charts illustrate trends of values over time.
[PieChart](<#PieChart>) | Pie charts illustrate proportions of values.

Action | Description
---|---
[AdvancedFormat_Init](<#AdvancedFormat_Init>) | Initializes an AdvancedFormat record with the values passed as arguments. The record is returned by the action.
[ChartFormat_Init](<#ChartFormat_Init>) | Initializes a ChartFormat record with the values passed as arguments. The record is returned by the action.
[DataPoint_GetClicked](<#DataPoint_GetClicked>) | Returns the data point that was clicked on the chart.<br/>Execute this action in the On Click action of a chart.
[DataPoint_Init](<#DataPoint_Init>) | Initializes a DataPoint record with the values passed as arguments. The record is returned by the action.
[DataPoint_InitMissing](<#DataPoint_InitMissing>) | Initializes a DataPoint to plot a gap on the chart. The record is returned by the action.
[XAxisFormat_Init](<#XAxisFormat_Init>) | Initializes an XAxisFormat record with the values passed as arguments. The record is returned by the action.
[YAxisFormat_Init](<#YAxisFormat_Init>) | Initializes an YAxisFormat record with the values passed as arguments. The record is returned by the action.

Structure | Description
---|---
[AdvancedDataPointFormat](<#Structure_AdvancedDataPointFormat>) | Information to format a data point using Highcharts JSON.
[AdvancedDataSeriesFormat](<#Structure_AdvancedDataSeriesFormat>) | Information to format a data series using Highcharts JSON.
[AdvancedFormat](<#Structure_AdvancedFormat>) | Information to format chart elements using Highcharts JSON.
[ChartFormat](<#Structure_ChartFormat>) | Information to format the chart.
[DataPoint](<#Structure_DataPoint>) | Information to plot a data point on the chart.
[XAxisFormat](<#Structure_XAxisFormat>) | Information to format the X-axis on the chart.
[YAxisFormat](<#Structure_YAxisFormat>) | Information to format the Y-axis on the chart.

Static Entity | Description
---|---
[LegendPosition](<#StaticEntity_LegendPosition>) | The position where the legend is displayed on charts.
[StackingType](<#StaticEntity_StackingType>) | The way to plot multiple data series on Area, Bar, or Column charts:<br/>- ‘NoStacking’: plot data series side by side to compare them;<br/>- ‘Stacked’: plot data series stacked to show their contribution to a total;<br/>- ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.
[XAxisValuesType](<#StaticEntity_XAxisValuesType>) | The data type of labels displayed on the X-axis to format them.<br/>Using ‘Auto’ means the type is inferred from the label of the first data point.

## Widgets

### AreaChart { #AreaChart }

Area charts illustrate the contribution of values to a total over time.

*Inputs*

SourceDataPointList
:   Type: mandatory, [DataPoint](<#Structure_DataPoint>) List.  
    The list of all data points to be plotted on the chart.

StackingType
:   Type: optional, StackingType Identifier.  
    The way to plot multiple data series on the chart:  
    \- ‘NoStacking’: plot data series overlapped to compare them;  
    \- ‘Stacked’: plot data series stacked to show their contribution to a total;  
    \- ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  
    ‘Stacked’ is the default option.

Height
:   Type: optional, Integer.  
    The vertical size of the chart in pixels (300 by default).  
    The horizontal size of the chart is the parent’s width.

LegendPosition
:   Type: optional, LegendPosition Identifier.  
    The position where the legend is displayed on the chart (‘Bottom’ by default).  
    The legend is hidden if no series name is set in any data point.

XAxisFormat
:   Type: optional, [XAxisFormat](<#Structure_XAxisFormat>).  
    Formatting options for the X-axis.  
    Action XAxisFormat_Init helps to create and initialize this parameter.

YAxisFormat
:   Type: optional, [YAxisFormat](<#Structure_YAxisFormat>).  
    Formatting options for the Y-axis.  
    Action YAxisFormat_Init helps to create and initialize this parameter.

ChartFormat
:   Type: optional, [ChartFormat](<#Structure_ChartFormat>).  
    Formatting options for the chart.  
    Action ChartFormat_Init helps to create and initialize this parameter.

Clickable
:   Type: optional, Boolean.  
    Set to True to allow clicking on plotted values and execute the On Click action (False by default).

AdvancedFormat
:   Type: optional, [AdvancedFormat](<#Structure_AdvancedFormat>).  
    Highcharts JSON to format elements displayed on the chart.  
    Action AdvancedOptions_Init helps to create and initialize this parameter.

### BarChart { #BarChart }

Bar charts compare multiple values using horizontal bars.  
In this chart, the X-axis runs vertically and the Y-axis runs horizontally.

*Inputs*

SourceDataPointList
:   Type: mandatory, [DataPoint](<#Structure_DataPoint>) List.  
    The list of all data points to be plotted on the chart.

StackingType
:   Type: optional, StackingType Identifier.  
    The way to plot multiple data series on the chart:  
    \- ‘NoStacking’: plot data series side by side to compare them;  
    \- ‘Stacked’: plot data series stacked to show their contribution to a total;  
    \- ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  
    ‘NoStacking’ is the default option.

Height
:   Type: optional, Integer.  
    The vertical size of the chart in pixels (300 by default).  
    The horizontal size of the chart is the parent’s width.

LegendPosition
:   Type: optional, LegendPosition Identifier.  
    The position where the legend is displayed on the chart (‘Bottom’ by default).  
    The legend is hidden if no series name is set in any data point.

XAxisFormat
:   Type: optional, [XAxisFormat](<#Structure_XAxisFormat>).  
    Formatting options for the X-axis.  
    Action XAxisFormat_Init helps to create and initialize this parameter.

YAxisFormat
:   Type: optional, [YAxisFormat](<#Structure_YAxisFormat>).  
    Formatting options for the Y-axis.  
    Action YAxisFormat_Init helps to create and initialize this parameter.

ChartFormat
:   Type: optional, [ChartFormat](<#Structure_ChartFormat>).  
    Formatting options for the chart.  
    Action ChartFormat_Init helps to create and initialize this parameter.

Clickable
:   Type: optional, Boolean.  
    Set to True to allow clicking on plotted values and execute the On Click action (False by default).

AdvancedFormat
:   Type: optional, [AdvancedFormat](<#Structure_AdvancedFormat>).  
    Highcharts JSON to format elements displayed on the chart.  
    Action AdvancedOptions_Init helps to create and initialize this parameter.

### ColumnChart { #ColumnChart }

Column charts compare multiple values using vertical bars.

*Inputs*

SourceDataPointList
:   Type: mandatory, [DataPoint](<#Structure_DataPoint>) List.  
    The list of all data points to be plotted on the chart.

StackingType
:   Type: optional, StackingType Identifier.  
    The way to plot multiple data series on the chart:  
    \- ‘NoStacking’: plot data series side by side to compare them;  
    \- ‘Stacked’: plot data series stacked to show their contribution to a total;  
    \- ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  
    ‘NoStacking’ is the default option.

Height
:   Type: optional, Integer.  
    The vertical size of the chart in pixels (300 by default).  
    The horizontal size of the chart is the parent’s width.

LegendPosition
:   Type: optional, LegendPosition Identifier.  
    The position where the legend is displayed on the chart (‘Bottom’ by default).  
    The legend is hidden if no series name is set in any data point.

XAxisFormat
:   Type: optional, [XAxisFormat](<#Structure_XAxisFormat>).  
    Formatting options for the X-axis.  
    Action XAxisFormat_Init helps to create and initialize this parameter.

YAxisFormat
:   Type: optional, [YAxisFormat](<#Structure_YAxisFormat>).  
    Formatting options for the Y-axis.  
    Action YAxisFormat_Init helps to create and initialize this parameter.

ChartFormat
:   Type: optional, [ChartFormat](<#Structure_ChartFormat>).  
    Formatting options for the chart.  
    Action ChartFormat_Init helps to create and initialize this parameter.

Clickable
:   Type: optional, Boolean.  
    Set to True to allow clicking on plotted values and execute the On Click action (False by default).

AdvancedFormat
:   Type: optional, [AdvancedFormat](<#Structure_AdvancedFormat>).  
    Highcharts JSON to format elements displayed on the chart.  
    Action AdvancedOptions_Init helps to create and initialize this parameter.

### LineChart { #LineChart }

Line charts illustrate trends of values over time.

*Inputs*

SourceDataPointList
:   Type: mandatory, [DataPoint](<#Structure_DataPoint>) List.  
    The list of all data points to be plotted on the chart.

Height
:   Type: optional, Integer.  
    The vertical size of the chart in pixels (300 by default).  
    The horizontal size of the chart is the parent’s width.

LegendPosition
:   Type: optional, LegendPosition Identifier.  
    The position where the legend is displayed on the chart (‘Bottom’ by default).  
    The legend is hidden if no series name is set in any data point.

XAxisFormat
:   Type: optional, [XAxisFormat](<#Structure_XAxisFormat>).  
    Formatting options for the X-axis.  
    Action XAxisFormat_Init helps to create and initialize this parameter.

YAxisFormat
:   Type: optional, [YAxisFormat](<#Structure_YAxisFormat>).  
    Formatting options for the Y-axis.  
    Action YAxisFormat_Init helps to create and initialize this parameter.

ChartFormat
:   Type: optional, [ChartFormat](<#Structure_ChartFormat>).  
    Formatting options for the chart.  
    Action ChartFormat_Init helps to create and initialize this parameter.

Clickable
:   Type: optional, Boolean.  
    Set to True to allow clicking on plotted values and execute the On Click action (False by default).

AdvancedFormat
:   Type: optional, [AdvancedFormat](<#Structure_AdvancedFormat>).  
    Highcharts JSON to format elements displayed on the chart.  
    Action AdvancedOptions_Init helps to create and initialize this parameter.

### PieChart { #PieChart }

Pie charts illustrate proportions of values.

*Inputs*

SourceDataPointList
:   Type: mandatory, [DataPoint](<#Structure_DataPoint>) List.  
    The list of all data points to be plotted on the chart.

Height
:   Type: optional, Integer.  
    The vertical size of the chart in pixels (300 by default).  
    The horizontal size of the chart is the parent’s width.

LegendPosition
:   Type: optional, LegendPosition Identifier.  
    The position where the legend is displayed on the chart (‘Bottom’ by default).

ChartFormat
:   Type: optional, [ChartFormat](<#Structure_ChartFormat>).  
    Formatting options for the chart.  
    Action ChartFormat_Init helps to create and initialize this parameter.

Clickable
:   Type: optional, Boolean.  
    Set to True to allow clicking on plotted values and execute the On Click action (False by default).

AdvancedFormat
:   Type: optional, [AdvancedFormat](<#Structure_AdvancedFormat>).  
    Highcharts JSON to format elements displayed on the chart.  
    Action AdvancedOptions_Init helps to create and initialize this parameter.


## Actions

### AdvancedFormat_Init { #AdvancedFormat_Init }

Initializes an AdvancedFormat record with the values passed as arguments. The record is returned by the action.

*Inputs*

DataPointFormats
:   Type: optional, [AdvancedDataPointFormat](<#Structure_AdvancedDataPointFormat>) List.  
    Advanced JSON formatting for the data points.

DataSeriesFormats
:   Type: optional, [AdvancedDataSeriesFormat](<#Structure_AdvancedDataSeriesFormat>) List.  
    Advanced JSON formatting for the data series.

XAxisJSON
:   Type: optional, Text.  
    Advanced JSON formatting for the X-axis.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#xAxis) for all available options.  
    As an example, format the dates on the X-axis to &quot;MMM YYYY&quot; using the following Highcharts JSON:  
    &quot;labels:{ formatter: function() { return Highcharts.dateFormat('%b %Y', this.value); } }&quot;

YAxisJSON
:   Type: optional, Text.  
    Advanced JSON formatting for the Y-axis.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#yAxis) for all available options.  
    As an example, prevent using decimals in the axis values using the following Highcharts JSON:  
    &quot;allowDecimals: false&quot;

HighchartsJSON
:   Type: optional, Text.  
    Advanced JSON formatting for any element of the chart.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts) for all available options.

*Outputs*

AdvancedFormat
:   Type: [AdvancedFormat](<#Structure_AdvancedFormat>).  
    The initialized AdvancedFormat record.

### ChartFormat_Init { #ChartFormat_Init }

Initializes a ChartFormat record with the values passed as arguments. The record is returned by the action.

*Inputs*

ShowDataPointValues
:   Type: optional, Boolean.  
    Set to True to display the value of the data points.

UseAnimation
:   Type: optional, Boolean.  
    Set to True to plot the chart with animation.

*Outputs*

ChartFormat
:   Type: [ChartFormat](<#Structure_ChartFormat>).  
    The initialized ChartFormat record.

### DataPoint_GetClicked { #DataPoint_GetClicked }

Returns the data point that was clicked on the chart.  
Execute this action in the On Click action of a chart.

*Outputs*

DataPoint
:   Type: [DataPoint](<#Structure_DataPoint>).  
    The clicked Data Point.

### DataPoint_Init { #DataPoint_Init }

Initializes a DataPoint record with the values passed as arguments. The record is returned by the action.

*Inputs*

Label
:   Type: mandatory, Text.  
    The label on the X-axis for the data point.  
    To display dates in the X-axis use the Platform Server date format (by default YYYY-MM-DD).

Value
:   Type: mandatory, Decimal.  
    The value to be plotted.

DataSeriesName
:   Type: optional, Text.  
    Name of the series where the data point belongs.

Tooltip
:   Type: optional, Text.  
    Custom tooltip for the data point when hovering the mouse.

Color
:   Type: optional, Text.  
    Custom color for the data point.

*Outputs*

DataPoint
:   Type: [DataPoint](<#Structure_DataPoint>).  
    The initialized DataPoint record.

### DataPoint_InitMissing { #DataPoint_InitMissing }

Initializes a DataPoint to plot a gap on the chart. The record is returned by the action.

*Inputs*

Label
:   Type: mandatory, Text.  
    The label on the X-axis for the data point.  
    To display dates in the X-axis use the Platform Server date format (by default YYYY-MM-DD).

DataSeriesName
:   Type: optional, Text.  
    Name of the series where the data point belongs.

*Outputs*

DataPoint
:   Type: [DataPoint](<#Structure_DataPoint>).  
    The initialized DataPoint record.

### XAxisFormat_Init { #XAxisFormat_Init }

Initializes an XAxisFormat record with the values passed as arguments. The record is returned by the action.

*Inputs*

Title
:   Type: optional, Text.  
    The text displayed next to the X-axis.

LabelsRotation
:   Type: optional, Integer.  
    The rotation in degrees of all labels displayed on the X-axis.

MinValue
:   Type: optional, Text.  
    The minimum value that is displayed on the X-axis.

MaxValue
:   Type: optional, Text.  
    The maximum value that is displayed on the X-axis.

ValuesType
:   Type: optional, XAxisValuesType Identifier.  
    The data type of labels displayed on the X-axis to format them.  
    Using ‘Auto’ means the type is inferred from the label of the first data point.

*Outputs*

XAxisFormat
:   Type: [XAxisFormat](<#Structure_XAxisFormat>).  
    The initialized XAxisFormat record.

### YAxisFormat_Init { #YAxisFormat_Init }

Initializes an YAxisFormat record with the values passed as arguments. The record is returned by the action.

*Inputs*

Title
:   Type: optional, Text.  
    The text displayed next to the Y-axis.

MinValue
:   Type: optional, Decimal.  
    The minimum value that is displayed on the Y-axis.

MaxValue
:   Type: optional, Decimal.  
    The maximum value that is displayed on the Y-axis.

ValuesPrefix
:   Type: optional, Text.  
    The text prefixing the values displayed on the Y-axis.

ValuesSuffix
:   Type: optional, Text.  
    The text suffixing the values displayed on the Y-axis.

GridLineStep
:   Type: optional, Decimal.  
    The step by which grid lines are displayed on the Y-axis.

*Outputs*

YAxisFormat
:   Type: [YAxisFormat](<#Structure_YAxisFormat>).  
    The initialized YAxisFormat record.


## Structures

### AdvancedDataPointFormat { #Structure_AdvancedDataPointFormat }

Information to format a data point using Highcharts JSON.

*Attributes*

DataPoint
:   Type: [DataPoint](<#Structure_DataPoint>).  
    Data point to format.

DataPointJSON
:   Type: Text (50).  
    Highcharts JSON to format the data point.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#series) for all available options.  
    As an example, show a custom data label in this point, using the following Highcharts JSON:  
    &quot;dataLabels: { enabled: true, formatter: function () { return 'top value' } }&quot;

### AdvancedDataSeriesFormat { #Structure_AdvancedDataSeriesFormat }

Information to format a data series using Highcharts JSON.

*Attributes*

DataSeriesName
:   Type: Text (50).  
    Name of the data series to format.

DataSeriesJSON
:   Type: Text (50).  
    Highcharts JSON to format the data series.  
    All data points belonging to the data series are affected by this formatting.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#series and http://api.highcharts.com/highcharts#plotOptions.series) for all available options.  
    As an example, plot a series with a thicker line in a Line chart using the following Highcharts JSON:  
    &quot;lineWidth: 5&quot;

### AdvancedFormat { #Structure_AdvancedFormat }

Information to format chart elements using Highcharts JSON.

*Attributes*

DataPointFormats
:   Type: [AdvancedDataPointFormat](<#Structure_AdvancedDataPointFormat>) List.  
    Highcharts JSON to format data points.

DataSeriesFormats
:   Type: [AdvancedDataSeriesFormat](<#Structure_AdvancedDataSeriesFormat>) List.  
    Highcharts JSON to format data series.

XAxisJSON
:   Type: Text (50).  
    Highcharts JSON to format the X-axis.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#xAxis) for all available options.  
    As an example, format the dates on the X-axis to &quot;MMM YYYY&quot; using the following Highcharts JSON:  
    &quot;labels:{ formatter: function() { return Highcharts.dateFormat('%b %Y', this.value); } }&quot;

YAxisJSON
:   Type: Text (50).  
    Highcharts JSON to format the Y-axis.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts#yAxis) for all available options.  
    As an example, prevent using decimals in the axis values using the following Highcharts JSON:  
    &quot;allowDecimals: false&quot;

HighchartsJSON
:   Type: Text (50).  
    Highcharts JSON to format any element of the chart.  
    Refer to Highcharts API (http://api.highcharts.com/highcharts) for all available options.

### ChartFormat { #Structure_ChartFormat }

Information to format the chart.

*Attributes*

ShowDataPointValues
:   Type: Boolean.  
    Set to True to display the value of the data points.

UseAnimation
:   Type: Boolean.  
    Set to True to plot the chart with animation.

### DataPoint { #Structure_DataPoint }

Information to plot a data point on the chart.

*Attributes*

Label
:   Type: Text (50).  
    The label on the X-axis for the data point.  
    To display dates in the X-axis use the Platform Server date format (by default YYYY-MM-DD).

Value
:   Type: Decimal (37, 0).  
    The value to be plotted.

DataSeriesName
:   Type: Text (50).  
    Name of the series where the data point belongs.

Tooltip
:   Type: Text (50).  
    Custom tooltip for the data point when hovering the mouse.

Color
:   Type: Text (50).  
    Custom color for the data point.  
    As an example, set the color of a data point to red using either of the following values: &quot;Red&quot;, &quot;#FF0000&quot;, &quot;rgb(255,0,0)&quot; or &quot;rgba(255,0,0,1)&quot;

### XAxisFormat { #Structure_XAxisFormat }

Information to format the X-axis on the chart.

*Attributes*

Title
:   Type: Text (50).  
    The text displayed next to the X-axis.

LabelsRotation
:   Type: Integer.  
    The counterclockwise rotation in degrees of all labels displayed on the X-axis.

MinValue
:   Type: Text (50).  
    The minimum value that is displayed on the X-axis.

MaxValue
:   Type: Text (50).  
    The maximum value that is displayed on the X-axis.

ValuesType
:   Type: XAxisValuesType Identifier.  
    The data type of labels displayed on the X-axis to format them.  
    Using ‘Auto’ means the type is inferred from the label of the first data point.

### YAxisFormat { #Structure_YAxisFormat }

Information to format the Y-axis on the chart.

*Attributes*

Title
:   Type: Text (50).  
    The text displayed next to the Y-axis.

MinValue
:   Type: Decimal (37, 0).  
    The minimum value that is displayed on the Y-axis.

MaxValue
:   Type: Decimal (37, 0).  
    The maximum value that is displayed on the Y-axis.

ValuesPrefix
:   Type: Text (50).  
    The text prefixing the values displayed on the Y-axis.

ValuesSuffix
:   Type: Text (50).  
    The text suffixing the values displayed on the Y-axis.

GridLineStep
:   Type: Decimal (37, 0).  
    The step by which grid lines are displayed on the Y-axis.


## Static Entities

### LegendPosition { #StaticEntity_LegendPosition }

The position where the legend is displayed on charts.

*Attributes*

Id
:   Type: Integer.  
    

Order
:   Type: Integer.  
    

Is_Active
:   Type: Boolean.  
    

*Records*

* Bottom
* Top
* Hidden
* Inside
* Right
* Left

### StackingType { #StaticEntity_StackingType }

The way to plot multiple data series on Area, Bar, or Column charts:  
- ‘NoStacking’: plot data series side by side to compare them;  
- ‘Stacked’: plot data series stacked to show their contribution to a total;  
- ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.

*Attributes*

Id
:   Type: Integer.  
    

Order
:   Type: Integer.  
    

Is_Active
:   Type: Boolean.  
    

*Records*

* NoStacking
* Stacked100Percent
* Stacked

### XAxisValuesType { #StaticEntity_XAxisValuesType }

The data type of labels displayed on the X-axis to format them.  
Using ‘Auto’ means the type is inferred from the label of the first data point.

*Attributes*

Id
:   Type: Integer.  
    

Label
:   Type: Text (50).  
    

Order
:   Type: Integer.  
    

*Records*

* Text
* Auto


