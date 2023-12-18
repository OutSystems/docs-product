---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Progress Bar UI Pattern.
locale: en-us
guid: e574e089-b093-408e-9ed1-6850d664a81d
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A535&mode=design&t=Cx8ecjAITJrQMvRn-1
---

# Progress Bar Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of a progress bar in a traditional web app](images/progressbar-6-diag.png "Progress Bar Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .progress-container | .progress-container.flex-direction-column |  When IsInline parameter is False  |
| .progress-container | .progress-container.flex-direction-row |  When IsInline parameter is False  |

## Advanced use case

### Change color of Progress Bar based on value

1. Create a local Integer variable "Value".

1. Drag the Progress Bar pattern into the preview.

1. Set the Value of the Progress Bar's Percentage parameter.

1. To change the color of your ProgressBar based on values, create a condition and set limits to use color. In this example, 3 colors represent diferent states of progress. Set the Color parameter to `If(Value <= 50, Entities.Color.Red, If( Value > 50 and Value < 75,  Entities.Color.Yellow ,  Entities.Color.Green))`.

    ![Screenshot demonstrating how to change the color of a progress bar based on its value](images/progressbar-7-ss.png "Progress Bar Color Change Example")

1. Publish and test.

    ![Animated GIF showing a progress bar in action within a traditional web app](images/progressbar-5.gif "Progress Bar Animation")

### Change the style of Progress Bar

It is possible to change the style of Progress bar by using custom CSS. To implement this in your application, copy the CSS and add it to the theme.

```css
.progress {
    padding: var(--space-s);`
    border: var(--space-xs) solid var(--color-primary);`
}
```

![Image of a progress bar with custom styling applied](images/progressbar-8.png "Custom Styled Progress Bar")

### Remove background of Progress Bar

To remove the background, use this CSS snippet.

```css
.progress {
    background-color: transparent;
}
```

![Image of a progress bar with its background removed, showing transparency](images/progressbar-9.png "Progress Bar with Transparent Background")
