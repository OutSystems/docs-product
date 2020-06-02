---
tags: runtime-mobileandreactiveweb;  
summary: the Range Slider Interval UI Pattern allows users select a single value between two range values.
---

# Range Slider Interval

You can use the Range Slider Interval Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track, increases or decreases the value. 

![](images/rangesliderinterval-1.png)

## How to use the Range Slider Interval UI Pattern

1. In Service Studio, in the Toolbox, search for `Range Slider Interval`. 

    The Range Slider Interval widget is displayed.

    ![](images/rangesliderinterval-2-ss.png)

1. From the Toolbox, drag the Range Slider widget onto your application's screen.

1. Bind your variables to the InitialIntervalStart and InitialIntervalEnd inputs and use the OnChange event to add your logic to handle value changes.

    ![](images/rangesliderinterval-3-ss.png)  

1. After setting the MinValue, MaxValue, InitialIntervalStart and the InitialIntervalEnd, create the OnChange event.

    ![](images/rangesliderinterval-4-ss.png)  

1. Create an integer value and assign it.

    ![](images/rangeslider-5-ss.png)  

After following these steps and publishing the module, you can test the pattern in your app. 

**Result**

![](images/rangesliderinterval-7.gif)

### Changing the color of the bar

![](images/rangesliderinterval-6.png)

![](images/rangesliderinterval-8.png)

![](images/rangesliderinterval-9.png)

### Changing the size of the handles

![](images/rangesliderinterval-10.png)

![](images/rangesliderinterval-11.png)

![](images/rangesliderinterval-12.png)

## Properties

**Property** |  **Description** |  
---|---|
|  MinValue  |  Slider's minimum value.  |
|  MaxValue  |  Slider's maximum value.  |  none  
 |  InitialIntervalStart  |  Value selected by default. Must be between min and max values.  |  none  
 |  InitialIntervalEnd  |  Default value for the interval's end. Must be between min and max values.  |  none  
 |  Step  |  Slider moves in increments of Step. If Step is 10, the slider will go from 0 to 10, to 20, to 30, etc.  |  1  
 |  ShowPips  |  Show pips below the slider.  |  _True_  
 |  PipsStep  |  Range interval after which a Pip is drawn (when ShowPips is enabled). If not specified, the component will try to guess what step fits your data.  |  -1  
 |  ChangeEventDuringSlide  |  Trigger Change events while the slider is being dragged. If set to False, the Change events will only be triggered when the user releases the slider.  **Tip**: if you're refreshing a query based on the value of the slider, you probably want to set this to False.  |  _True_  
  
