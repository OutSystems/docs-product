---
tags: runtime-traditionalweb; 
summary: RangeSlider gives the end users an option to select a value within a configured range by dragging a slider. 
---

# RangeSlider

Set a value by dragging a handle within a configured range.

Offer the UI control for letting end users select a value from a fixed set of options.

**How to use**

Place the range slider on your screen. On the pattern properties, you must select the minimum and maximum range values.

1. Drag RangeSlider pattern into the preview
    
    ![](<images/rangeslider-image1.png>)

1. Set the mandatory values
    
    ![](<images/rangeslider-image2.png>)

## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| MinValue  |  Sets lowest possible value. |  Integer | True | none |
| MaxValue  |  Sets highest possible value. |  Integer | True | none |
| InitialValue  |  The value selected by default. Must be between min and max values. |  Integer | False | 1 |
| Step  |  The increment value for each step. For instance, a step of 5 would make the slider jump across 0-5-10-15-20 and so on. The default value is 1. |  Integer | True | none |
| ShowPips  |  If true, displays the range values near the slider. The default value is true. |  Boolean | False | True |
| PipsStepsNumber  | Sets the number of Pip Steps. Only applied if ShowPips is true. |  Integer | False | 0 |
| ExtendedClass| Adds custom style classes to this block. | Text | False | none |
| AdvancedFormat  | Enables you to use more options than what is provided in the input parameters. To find more options that can be used, go to [noUiSlider library](https://refreshless.com/nouislider/ "noUiSlider library"). Example: `{ pips: { density: 1 } }` |  Text | False | "{}" |

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnChange | Event triggered once a handler is dragged and the value changes.  |  True  |

**Return Values**

SelectedValue: Integer
  
## Layout and classes

![](<images/rangeslider-image3.png>)


## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| Handle |  .noUi-handle |  It's the handle element. Use this selector to customize it (use also the :before and :after).  |
| Interval  |  .noUi-connect  |  It's the colored interval. Use this selector to change the color of the interval from zero to the selected value.  |

## Advanced Use Case

### Change the interval color

Write the following CSS in the CSS editor and change the `yourcolor` to your color:

`.range-slider .noUi-connect {
background: yourcolor;
}` 

Or use the CSS variable: `var(--color-yourcolor)`:

`.range-slider .noUi-connect {
background: var(--color-red);
}`

### Removing the || of the handlers

1. Create a class `.range-slider .noUi-handle:before, .range-slider .noUi-handle:after`.

1. Set the content to `height: 0px`.

1. Publish and test.
