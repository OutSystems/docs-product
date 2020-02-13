---
tags:
summary: Learn how to customize Charts with JSON.
---
# Advanced Charts customization with JSON

Since OutSystems Charts uses the Highcharts API, you can customize and change your Chart by using [Highcharts configuration options](https://api.highcharts.com/highcharts/). These configuration options are defined as JSON snippets and can be used in the **AdvancedFormat** \> **HighchartsJSON** field of a Chart.

## JSON snippets and examples

### Customizing the fill color of an Area Chart

Change the color and add a vertical gradient to an Area Chart by entering the following JSON snippet to **AdvancedFormat** \> **HighchartsJSON**:

    "plotOptions: {
        area: {
            color:'<line-color>',
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, '<top-color>'],
                    [1, '<bottom-color>']
                ]
            }
        }
    }"

Where `<line-color>` is the color of the line, `<top-color>` is the color at the top of filled area, and `<bottom-color>` is the color at the bottom of the filled area.

**Example**

    "plotOptions: {
    area: {
        color:'rgba(255,0,0,1)',
        fillColor: {
            linearGradient: {
                x1: 0,
                y1: 0,
                x2: 0,
                y2: 1
            },
            stops: [
                [0, 'rgba(255,0,0,1)'],
                [1, 'rgba(255,0,0,0)']
            ]
        }}}"

![](images/adv-area-01.png?width=300)

### Combine two different chart types

To combine two different data series types in one chart follow these steps:

1. Create a Chart of the type of the first data series, for example a Column Chart.

1. Add the following JSON snippet to **AdvancedFormat** \> **HighchartsJSON** in order to define a secondary y-axis and modify the second data series to another data series type:

        "yAxis: [    
            { 
                // options for primary y-axis or yAxis 0
            },
            { 
                // options for secondary y-axis or yAxis 1
                opposite: true
            }
        ]
        series: [
            {
                // options for the first series
            },
            {
                // options for the second series
                type: '<type>',
                yAxis: 1
            }            
        ]"    

    Where `<type>` is a type of chart, for example `spline`.

**Example**

    "yAxis: [ 
        {},
        { 
            opposite: true
        }
    ],
    series: [
        {},
        {
            type: 'spline',
            yAxis: 1
        }
    ]"

![](images/adv-comb-01.png?width=300)


## Adding JSON from Highcharts demos to OutSystems Charts

Besides the simple examples and JSON snippets provided in this topic, you can also check out the [Highcharts demo page](https://www.highcharts.com/demo) for a list of other examples of chart customization.  
You can access the JSON of these Highcharts demos by selecting **VIEW OPTIONS \>**, or edit the demos by selecting one of the edit options.

To use JSON from Highcharts demos or from JSFiddle you need to:

1. Enter the JSON in the **AdvancedFormat** \> **HighchartsJSON** of a Chart.

1. In **AdvancedFormat** \> **HighchartsJSON**, delete the first line, `Highcharts.chart('container', {`, and the last line, `});` from the JSON.

1. Wrap the JSON in quotation marks `" "`.
