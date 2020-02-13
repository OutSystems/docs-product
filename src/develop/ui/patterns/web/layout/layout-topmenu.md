---
tags: runtime-traditionalweb; 
summary: LayoutTopMenu uses the space available on the top for navigation.
---

# LayoutTopMenu

Custom layout with a fixed menu on top.

Useful for simple applications, without a complex navigation structure. 

**How to use**

Fill in the placeholders with the content that you need. 

![](<images/layout-tm-image-2.png?width=600>)

## Input parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Adds custom style classes to this Block |  Text | False | none |
| DeviceConfiguration  |  Configuration to change the default values that set when the application is seen as phone, tablet or desktop. |  DeviceConfig | False | none |

## Layout and classes

![](<images/layout-tm-image-1.png>)
 
## Responsive behavior

This layout comes with a default responsive behavior. On tablets it remains the same as on desktop. But on phones it breaks the content vertically, making the placeholders Title and Actions full-width.

![](<images/layout-tm-image-3.png>)

The menu also adapts to mobile, moving the navigation to a sidebar, toggled by a hamburger icon.

![](<images/layout-tm-image-4.gif>)

On a mobile phone and tablet:

![](<images/layout-tm-image-7.png>)

## Advanced

Here are some more advanced use-cases of the widget.

### Customize your responsive breakpoints

1. Go to the Common Flow.
1. Double-click on your Layout to open the widget tree. 
1. Go to the LayoutTopMenu parameters.
1. Toggle the DeviceConfiguration 'plus icon'.
1. Set your custom breakpoints (in pixels). On the example below the phone breaks is set to happen only when the Device with is at 200px.
1. Publish and test.

    ![](<images/layout-tm-image-5.png>)

### Customize your content max-width

1. Go to Themes.
1. In the Grid section, set your custom width (default value is 1280px) in the Max. Width parameter.
1. Publish and test.

    ![](<images/layout-tm-image-6.png>)

## Device compatibility

In Internet Explorer we made specific CSS that uses 'position: fixed' instead of 'position: sticky', as 'sticky' is not supported in Internet Explorer.

## Notes

In Internet Explorer 10 and 11, we added some specific behaviors to account for the flicker caused by the slow loading time of polyfill CSS Variables. If there are any JavaScript errors, this will cause the screen to appear white.

To override this behavior, add the following code snippet to your CSS theme:

```css
.ie10,
.ie11 {
   display: block;
}
```
