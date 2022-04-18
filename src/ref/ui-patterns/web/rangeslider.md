---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Range Slider UI Pattern.
locale: en-us
guid: 6b1ad133-79fa-4894-8d51-26e0c33f8f39
app_type: traditional web apps
---

# Range Slider Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnChange | Event triggered once a handler is dragged and the value changes.  |  True  |

**Return values**

SelectedValue: Integer
  
## Layout and classes

![](<images/rangeslider-3-diag.png>)

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| Handle |  .noUi-handle |  It's the handle element. Use this selector to customize it (use also the :before and :after). |
| Interval  |  .noUi-connect  |  It's the colored interval. Use this selector to change the color of the interval from zero to the selected value. |

## Advanced use case

### Change the interval color

Write the following CSS in the CSS editor and change the `yourcolor` to your color:

```css
.range-slider .noUi-connect {
    background: yourcolor;
}
```

Or use the CSS variable: `var(--color-yourcolor)`:

```css
.range-slider .noUi-connect {
    background: var(--color-red);
}
```

### Removing the || of the handlers

1. Create a class `.range-slider .noUi-handle:before, .range-slider .noUi-handle:after`.

1. Set the content to `height: 0px`.

1. Publish and test.
