---
tags: runtime-traditionalweb; 
summary: RangeSliderInterval selects a single value or a range between two values.
---

# Range Slider Interval

You can use the Range Slider Interval UI Pattern to allow users select a single value between two range values. This pattern enables the adjustment of content by predetermined intervals and within a chosen range. Moving the slider along the track, increases or decreases the value. 

**How to use the Range Slider UI Pattern**

1. Drag RangeSliderInterval pattern into the preview.

    ![](images/RangeSliderInterval-1.png)

1. Enter the mandatory values in the properties pane.

    ![](images/RangeSliderInterval-2.png)


## Properties

| **Property** |  **Description** |  
|---|---|
|MinValue (Decimal): Mandatory  |  Slider's minimum value. <p>Examples <ul><li>_0_ - The slider's minimum value is 0.</li><li>_12_ - The slider's minimum value is 12</li> </ul></p> |
|MaxValue (Decimal): Mandatory  |  Slider's maximum value. <p>Examples <ul><li>_100_ - The slider's maximum value is 100.</li></ul></p> |
|InitialIntervalStart  |  Start value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>_10_ - Slider's default start value when the page is rendered is 10.</li></ul></p> 
|InitialIntervalEnd  |  End value selected by default when the page is rendered. Must be between min and max values. <p>Examples <ul><li>_10_ - Slider's default end value when the page is rendered is 10.</li></ul></p> 
|Step (Decimal): Optional  | The slider moves in increments of steps.<p>Examples <ul><li>_Blank_ - The slider increases in steps of 1. This is the default value. </li><li>_10_ - The slider increases in steps of 10.</li></ul></p>
|ShowPips (Boolean): Optional  | If True, pips are shown below the slider. This is the default value. If False, no pips are shown. | 
|PipsStepNumber (Integer): Optional  | Sets the number of Pip steps. This property is only applicable if the ShowPips property is set to True.|
|IsVertical (Boolean): Optional | If True, the slider orientation is vertical. If False, the slider orientation is horizontal. | 
|VerticalHeight (Integer): Optional | If IsVertical is True, use this property to set the height (in px) of the slider. <p>Examples <ul><li>_Blank_ - The slider is 100px high. This is the default value. </li><li>_250_ - The slider is 250px high.</li></ul></p> | 
|IsDisabled (Boolean): Optional | If True, the slider is disabled. If False, the slider is enabled. This is the default value. | 
|ExtendedClass (Text): Optional | Add custom style classes to the Range Slider Interval UI Pattern. You define your [custom style classes](../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the Range Slider Interval UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Range Slider Interval UI styles being applied.</li></ul> |  
|AdvancedFormat (Text): Optional | Allows you to use more options than what is provided in the input parameters. For more information, see [noUiSlider library](https://refreshless.com/nouislider/ "noUiSlider library"). <p> Example <li> `{ pips: { density: 1 } }` </li></p> | 
