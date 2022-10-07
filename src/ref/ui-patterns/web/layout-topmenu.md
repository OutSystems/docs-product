---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Layout Top Menu web block.
locale: en-us
guid: 32bd92fb-5665-45a8-ac9c-69d26270cb75
app_type: traditional web apps
---

# Layout Top Menu Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/layout-tm-1-diag.png>)

## Responsive behavior

This layout comes with a default responsive behavior. On tablets it remains the same as on desktop. But on phones it breaks the content vertically, making the placeholders Title and Actions full-width.

![](<images/layout-tm-3-ss.png>)

The menu also adapts to mobile, moving the navigation to a sidebar, toggled by a hamburger icon.

![](<images/layout-tm-4-ss.gif>)

On a mobile phone and tablet:

![](<images/layout-tm-7-ss.png>)

## Advanced

Here are some more advanced use-cases of the widget.

### Customize your responsive breakpoints

1. Go to the Common Flow.
1. Double-click on your Layout to open the widget tree.
1. Go to the LayoutTopMenu parameters.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set your custom breakpoints (in pixels). On the example below the phone breaks is set to happen only when the Device with is at 200px.
1. Publish and test.

![](<images/layout-tm-5-ss.png>)

### Customize your content max-width

1. Go to Themes.
1. In the Grid section, set your custom width (default value is 1280px) in the Max. Width parameter.
1. Publish and test.

![](<images/layout-tm-6-ss.png>)

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
