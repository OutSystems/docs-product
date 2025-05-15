---
tags: responsive design, layout customization, web design, ui components, breakpoints
summary: Explore the responsive design and customization options of the Layout Top Menu in OutSystems 11 (O11).
locale: en-us
guid: 32bd92fb-5665-45a8-ac9c-69d26270cb75
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:508
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Layout Top Menu Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Layout Top Menu web block](images/layout-tm-1-diag.png "Layout Top Menu Diagram")

## Responsive behavior

This layout comes with a default responsive behavior. On tablets it remains the same as on desktop. But on phones it breaks the content vertically, making the placeholders Title and Actions full-width.

![Screenshot showing the Layout Top Menu's responsive behavior on desktop and tablet devices](images/layout-tm-3-ss.png "Layout Top Menu on Desktop and Tablet")

The menu also adapts to mobile, moving the navigation to a sidebar, toggled by a hamburger icon.

<iframe src="https://player.vimeo.com/video/1002731447" width="344" height="750" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the Layout Top Menu's responsive behavior on mobile devices with a sidebar navigation.</iframe>

On a mobile phone and tablet:

![Screenshot displaying the Layout Top Menu's appearance on mobile phones and tablets](images/layout-tm-7-ss.png "Layout Top Menu on Mobile Devices")

## Advanced

Here are some more advanced use-cases of the widget.

### Customize your responsive breakpoints

1. Go to the Common Flow.
1. Double-click on your Layout to open the widget tree.
1. Go to the LayoutTopMenu parameters.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set your custom breakpoints (in pixels). On the example below the phone breaks is set to happen only when the Device with is at 200px.
1. Publish and test.

![Screenshot of the process to customize responsive breakpoints for the Layout Top Menu](images/layout-tm-5-ss.png "Custom Responsive Breakpoints")

### Customize your content max-width

1. Go to Themes.
1. In the Grid section, set your custom width (default value is 1280px) in the Max. Width parameter.
1. Publish and test.

![Screenshot showing how to customize the content max-width in the Layout Top Menu](images/layout-tm-6-ss.png "Custom Content Max-Width Setting")

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
