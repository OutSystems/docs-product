---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Layout Side Menu web block.
locale: en-us
guid: 4d5d4869-2345-4646-a8b0-5c24c0f6a8cd
app_type: traditional web apps
platform-version: o11
---

# Layout Side Menu Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/layout-sm-1-diag.png?width=600>)

## Responsive behavior

This layout comes with a default responsive behavior. On tablets it remains the same as on desktop. But on phones it breaks the content vertically, making the placeholders Title and Actions full-width.

![](<images/layout-sm-3-ss.png>)

![](<images/layout-sm-7-ss.png>)

The menu also adapts to mobile, hiding the navigation sidebar, which can be toggled by a hamburger icon.

![](<images/layout-sm-4-ss.gif>)

![](<images/layout-sm-8-ss.png>)

## Advanced

Here are some more advanced use-cases of the widget.

### Customize your responsive breakpoints

1. Go to the Common Web Flow.
1. Double-click on your Layout to open the widget tree.
1. Go to the LayoutTopMenu parameters.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set your custom breakpoints (in pixels). On the example below the phone breaks is set to happen only when the Device with is at 200px.
1. Publish and test.

![](<images/layout-sm-5-ss.png?width=600>)

### Customize your content max-width

1. Go to Themes.
1. In the Grid section, set your custom width (default value is 1280px) in the Max. Width parameter.
1. Publish and test.

![](<images/layout-sm-6-ss.png?width=600>)

## Device compatibility

In Internet Explorer we made specific CSS that uses 'position: fixed' instead of 'position: sticky', as 'sticky' is not supported in Internet Explorer.

## Notes

In Internet Explorer 10 and 11, we added some specific behaviors to account for the flicker caused by the slow loading time of polyfill CSS Variables. If there are any JavaScript errors, this will cause the screen to appear white.

To override this behavior, add the following code snippet to your CSS theme:

```css
.ie10, .ie11 {
    display: block;
}
```
