---
tags: responsive design, customization, ux/ui design, web development, front-end frameworks
summary: Explore the responsive design and customization options of the Layout Side Menu in OutSystems 11 (O11) for Traditional Web Apps.
locale: en-us
guid: 4d5d4869-2345-4646-a8b0-5c24c0f6a8cd
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:500
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Layout Side Menu Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Layout Side Menu for Traditional Web Apps](images/layout-sm-1-diag.png "Layout Side Menu Diagram")

## Responsive behavior

This layout comes with a default responsive behavior. On tablets it remains the same as on desktop. But on phones it breaks the content vertically, making the placeholders Title and Actions full-width.

![Screenshot showing the Layout Side Menu's responsive behavior on a tablet device](images/layout-sm-3-ss.png "Layout Side Menu on Tablet")

![Screenshot displaying the Layout Side Menu's full-width placeholders Title and Actions on a phone device](images/layout-sm-7-ss.png "Layout Side Menu on Phone")

The menu also adapts to mobile, hiding the navigation sidebar, which can be toggled by a hamburger icon.

<iframe src="https://player.vimeo.com/video/1002680199" width="344" height="750" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the toggle of the navigation sidebar in the Layout Side Menu on a mobile device.</iframe>

![Screenshot showing the Layout Side Menu's adaptation to mobile devices with a hidden navigation sidebar](images/layout-sm-8-ss.png "Layout Side Menu Mobile Adaptation")

## Advanced

Here are some more advanced use-cases of the widget.

### Customize your responsive breakpoints

1. Go to the Common Web Flow.
1. Double-click on your Layout to open the widget tree.
1. Go to the LayoutTopMenu parameters.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set your custom breakpoints (in pixels). On the example below the phone breaks is set to happen only when the Device with is at 200px.
1. Publish and test.

![Screenshot of the process to customize responsive breakpoints for the Layout Side Menu in the Common Web Flow](images/layout-sm-5-ss.png "Custom Responsive Breakpoints")

### Customize your content max-width

1. Go to Themes.
1. In the Grid section, set your custom width (default value is 1280px) in the Max. Width parameter.
1. Publish and test.

![Screenshot illustrating how to customize the content max-width for the Layout Side Menu in the Themes grid section](images/layout-sm-6-ss.png "Custom Content Max-Width")

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
