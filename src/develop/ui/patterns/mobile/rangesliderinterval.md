---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# RangeSliderInterval Pattern

The RangeSliderInterval pattern enables you to set an interval by dragging two handles. You can control an interval value with simple and interactive user input.

## How to Use the RangeSliderInterval Pattern

1\. Bind your variables to the InitialIntervalStart and InitialIntervalEnd inputs and use the OnChange event to add your logic to handle value changes.

![](images/range_slider_interval_interaction.png)  

2\. After setting the MinValue, MaxValue, InitialIntervalStart and the InitialIntervalEnd, create the OnChange event.

![](images/range_slider_interval_create.png)  

3\. Create an integer value and assign it.

![](images/range_slider_interval_assign.png)  

**Result**:

![](images/RangesliderInterval_BasicEndResult.gif)

### Changing the Color of the Bar

![](images/range_slider_interval_change_colors.png)

![](images/range_slider_interval_change_color_of_the_bar.png)

![](images/range_slider_interval_change_colors_2.png)

### Changing the Size of the Handles

![](images/change_size_of_handles.png)

![](images/change_size.png)

![](images/change_size_of_handles_2.png)

## Input Parameters

**Input Name** |  **Description** |  **Default Value**  
---|---|---  
![](images/input.png) |  MinValue  |  Slider's minimum value.  |  none  
![](images/input.png) |  MaxValue  |  Slider's maximum value.  |  none  
![](images/input.png) |  InitialIntervalStart  |  Value selected by default. Must be between min and max values.  |  none  
![](images/input.png) |  InitialIntervalEnd  |  Default value for the interval's end. Must be between min and max values.  |  none  
![](images/input.png) |  Step  |  Slider moves in increments of Step. If Step is 10, the slider will go from 0 to 10, to 20, to 30, etc.  |  1  
![](images/input.png) |  ShowPips  |  Show pips below the slider.  |  _True_  
![](images/input.png) |  PipsStep  |  Range interval after which a Pip is drawn (when ShowPips is enabled). If not specified, the component will try to guess what step fits your data.  |  -1  
![](images/input.png) |  ChangeEventDuringSlide  |  Trigger Change events while the slider is being dragged. If set to False, the Change events will only be triggered when the user releases the slider.  **Tip**: if you're refreshing a query based on the value of the slider, you probably want to set this to False.  |  _True_  
  
## Events

**Event Name** |  **Description** |  **Mandatory**  
---|---|---  
![](images/Event.png) OnChange  |  Action to execute after selecting a new value on the slider. Returns the new IntervalStart and the new IntervalEnd.  |  _True_  
  
## Layout and Classes

![](images/range_slider_layout_and_classes.png)

## CSS Selectors

**Element** |  **CSS Class** |  **Description**  
---|---|---  
![](images/css_selector.png) |  noUi-handle  |  .noui-active  |  Class added when you click the handle.  
  
## Samples

This sample uses the RangeSliderInterval pattern:

![](images/RangeSliderInterval-Sample-1.PNG)
