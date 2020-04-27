---
tags: runtime-mobileandreactiveweb;  
summary: 
---

# Range Slider 

You can use the Range Slider UI Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content within a predetermined range. Moving the slider along the track, increases or decreases the value.  

![](images/rangeslider-preview.png)

## How to use the Range Slider UI Pattern

1. In Service Studio, in the Toolbox, search for  `Range Slider`. 

    The Range Slider widget is displayed.

    ![](images/rangeslider-widget.png)

1. From the Toolbox, drag the Range Slider widget onto your application's screen.

    ![](images/rangeslider-image-1.png)

1. Bind your variable to the **InitialValue** input and use the **OnChange** event to add your logic to handle value changes.

    ![](images/range_slider.png)

1. After setting the **MinValue** , **MaxValue** and the **InitialValue** , you must create the **OnChange** event.

    ![](images/range_slider_on_change.png)

1. Create an integer value and assign it.

    ![](images/range_slder_integer.png)

After following these steps and publishing the module, you can test the pattern in your app. 

**Result**:

![](images/Rangeslider_BasicEndResult.gif)

### Changing the color of the bar

![](images/range_slider_color_bar_1.png)

![](images/range_slider__change_color.png)

![](images/range_slider_color_bar_2.png)

### Changing the size of the handles

![](images/range_slider_handle_size_1.png)

![](images/range_slider_change_size_of_handles.png)

![](images/range_slider_handle_size_2.png)

## Properties

**Property** |  **Description** |  **Default Value**  
---|---|---  
 MinValue  |  Slider's minimum value.  |  none  
 MaxValue  |  Slider's maximum value.  |  none  
 InitialValue  |  Value selected by default. Must be between min and max values.  |  none  
 Step  |  Slider moves in increments of Step. If Step is 10, the slider will go from 0 to 10, to 20, to 30, etc.  |  1  
 ShowPips  |  Show pips below the slider.  |  True  
 PipsStep  |  Range interval after which a Pip is drawn (when ShowPips is enabled). If not specified, the component will try to guess what step fits your data.  |  -1  
ChangeEventDuringSlide  |  Triggers Change events while the slider is being dragged. If set to _False_ , the Change events will only be triggered when the user releases the slider. **Tip**: If you're refreshing a query based on the value of the slider, you probably want to set this to False.  |  True  
  
## Samples

This sample uses the Range Slider Pattern:

![](images/RangeSlider-Sample-1.PNG)

## See also

* OutSystems UI Live Style Guide: [Range Slider](https://outsystemsui.outsystems.com/WebStyleGuidePreview/RangeSlider.aspx)
* OutSystems UI Pattern Page: [Range Slider](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=60)
