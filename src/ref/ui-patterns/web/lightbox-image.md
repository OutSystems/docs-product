---
tags: css customization, ui design, web development, ui patterns, outsystems ui
summary: Learn to customize the Light Box Image UI Pattern in OutSystems 11 (O11) with CSS for enhanced visuals.
locale: en-us
guid: 6b8b6bad-949d-4561-9cd9-a062b11fc20b
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=615%3A515&mode=design&t=Cx8ecjAITJrQMvRn-1
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Light Box Image Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout of the Light Box Image UI Pattern in a traditional web app](images/lightboximage-3-diag.png "Light Box Image Layout Diagram") 

![Diagram illustrating the CSS classes associated with the Light Box Image UI Pattern](images/lightboximage-4-diag.png "Light Box Image Classes Diagram")

## Advanced use case

### Change the Light Box Image overlay

It is possible to change the opacity of Light Box Image overlay when it is open by adding custom CSS. To implement this in your application, copy the CSS code below and add it to the theme.

```css
.pswp__bg {
    background-color: rgba(0, 0, 0, 0.8);
}

.pswp__ui--fit .pswp__top-bar, .pswp__ui--fit .pswp__caption {
    background-color: rgba(0, 0, 0, 0);
}
```

![Screenshot of custom CSS code to change the Light Box Image overlay opacity](images/lightboximage-5-ss.png "Custom CSS for Light Box Image Overlay")

### Add rounded corners to images inside Light Box Image Pattern

To add rounded corners to images inside Light Box Image, add the following custom css to the theme.

```css
.lightbox-content-thumbnail img,
.pswp__item img {
    border-radius: var(--border-radius-soft);
}
```

![Screenshot showing CSS code to add rounded corners to images in the Light Box Image Pattern](images/lightboximage-6-ss.png "CSS for Rounded Corners in Light Box Image")
    