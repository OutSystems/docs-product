---
tags: runtime-traditionalweb; 
summary: LayoutPopup is the layout used to display additional off-canvas information.
---

# LayoutPopup

The Layout for the [RichWidgets Popup Editor](../../../inputs/popup.md).

Useful to display additional off-canvas information.

**How to use**

1. In the Popup screen, select the object tree and set the layout to LayoutPopup.

1. Add your content inside the layout. 

1. Use this screen as destination for the [RichWidgets Popup Editor](../../../inputs/popup.md).

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| DeviceConfiguration  |  Configuration to change the default values that set when the application will be seen as phone, tablet or desktop |  DeviceConfig | False | none |

## Layout and Classes

![](<images/layout-popup-image-1.png>)

### MainContent

Drag your content to this placeholder.

## Advanced Use Case

### Customize your responsive breakpoints

1. Go to the Common Flow.
1. Double-click the Layout to open the widget tree. 
1. Go to the LayoutPopup properties.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set the custom breakpoints (in pixels). In the example below, the phone breaks are set to happen only when the Device width is at 200px.
1. Publish and test.

![](<images/layout-popup-image-2.png>)

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

## Compatibility with other Patterns

[RichWidgets Popup Editor](../../../inputs/popup.md)




