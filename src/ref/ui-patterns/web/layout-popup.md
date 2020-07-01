---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Layout Popup web block.
---

# Layout Popup Reference

## Layout and classes

![](<images/layout-popup-1-diag.png>)

### Main Content

Drag your content to this placeholder.

## Advanced use case

### Customize your responsive breakpoints

1. Go to the Common Flow.
1. Double-click the Layout to open the widget tree. 
1. Go to the LayoutPopup properties.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set the custom breakpoints (in pixels). In the example below, the phone breaks are set to happen only when the Device width is at 200px.
1. Publish and test.

    ![](<images/layout-popup-2-ss.png>)

## Notes

In Internet Explorer 10 and 11, we added some specific behaviors to account for the flicker caused by the slow loading time of polyfill CSS Variables. If there are any JavaScript errors, this will cause the screen to appear white.

You can override the following code to avoid this behavior.

```css
.ie10,
.ie11 {
   display: none;
}

.ie10.ponyfill-ready,
.ie11.ponyfill-ready {
   display: block;
}
```

## Compatibility with other patterns

[RichWidgets Popup Editor](../../../inputs/popup.md)
