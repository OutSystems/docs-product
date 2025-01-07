---
tags: component customization, css styling, web development, ui components, outsystems ui framework
summary: Explore the features and customization options of the Range Slider Interval component in OutSystems 11 (O11).
locale: en-us
guid: 3c86ec87-d4c6-441b-adf1-bdb30f056a62
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A549&mode=design&t=Cx8ecjAITJrQMvRn-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Range Slider Interval Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Events

| **Event Name** |  **Description** |  **Mandatory**  |
| ---|---|--- |  
| OnChange | Event triggered once a handler is dragged and the values change.  |  True  |

**Return values**

* SelectedMinValue: Integer
* SelectedMaxValue: Integer
  
## Layout and classes

![Diagram illustrating the layout and classes of the Range Slider Interval component](images/rangesliderinterval-3-diag.png "Range Slider Interval Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| Lesser handle |  .noUi-handle-lower |  It's the lesser handle, used to customize (use also the :before and :after).  |
| Upper Handle  |  .noUi-handle-upper  |  It's the upper handle, used to customize (use also the :before and :after). |
| Interval  |  .noUi-connect  |  Used to change the color of the interval.  |
  
## Advanced use case

### Change the interval color

Write the following CSS in the CSS editor and change the `yourcolor` to your color:

```css
.range-slider .noUi-connect {
    background: yourcolor;
}
```

Or using the CSS variables: `var(--color-yourcolor)`  
Example:  

```css
.range-slider .noUi-connect {
    background: var(--color-red);
}
```

### Removing the || of the handlers

1. Create a class `.range-slider .noUi-handle:before, .range-slider .noUi-handle:after`.

1. Set the content to `height: 0px`.

1. Publish the application.

![Screenshot showing the Range Slider Interval with customized color and removed handler lines](images/rangesliderinterval-5-ss.png "Range Slider Interval Styling Screenshot")
