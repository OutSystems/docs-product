---
tags: runtime-mobileandreactiveweb;  
summary: Allows the user select a single value between two range values.
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



## Properties

**Property** |  **Description** |
---|---|---  
 MinValue (Decimal): Mandatory  |  Slider's minimum value. <p>Examples <ul><li>_0_ - The slider's minimum value is 0.</li><li>_150.5_ - The slider's minimum value is 150.5</li> </ul></p> |  
 MaxValue (Decimal): Mandatory  |  Slider's maximum value. <p>Examples <ul><li>_100_ - The slider's maximum value is 100.</li></ul></p>   | 
 InitialValue (Decimal): Mandatory  |  Value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>_10_ - Slider's default value is 10.</li></ul></p> |
 Step (Decimal): Optional  | The slider moves in increments of steps.<p>Examples <ul><li>_Blank_ - The slider increases in steps of 1. This is the default value. </li><li>_10_ - The slider increases in steps of 10.</li></ul></p>  |   
 ShowPips (Boolean): Optional  | If True, pips are shown below the slider. This is the default value. If False, no pips are shown. | 
 PipsStep (Integer): Optional  |  Range interval after which a Pip is drawn (when ShowPips is enabled). If not specified, the component will try to guess what step fits your data.  |
 ChangeEventDuringSlide (Boolean): Optional  | If True, a change event is triggered while the slider is being dragged. This is the default value. If False, the change events are only triggered when the user releases the slider. **Tip**: If you're refreshing a query based on the value of the slider, you probably want to set this to False.  | 
 IsDisabled (Boolean): Optional | If True, the slider is disabled. If False, the slider is enabled. This is the default value. | 
 IsVertical (Boolean): Optional | If True, the slider orientation is vertical. If False, the slider orientation is horizontal. | 
 VerticalHeight (Integer): Optional | If IsVertical is True, use this property to set the height (in px) of the slider. <p>Examples <ul><li>_Blank_ - The slider is 100px high. This is the default value. </li><li>_250_ - The slider is 250px high.</li></ul></p> | 
 AdvancedFormat (Text): Optional  |  Allow for more options beyond what is provided through the input parameters. For more information, visit: https://kimmobrunfeldt.github.io/progressbar.js/. Example: `{ easing: 'bounce' }` | 
  
  
## Samples

This sample uses the Range Slider Pattern:

![](images/RangeSlider-Sample-1.PNG)

## See also

* OutSystems UI Live Style Guide: [Range Slider](https://outsystemsui.outsystems.com/WebStyleGuidePreview/RangeSlider.aspx)
* OutSystems UI Pattern Page: [Range Slider](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=60)
