---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Light Box Image UI Pattern.
---

# Light Box Image Reference

## Layout and classes

![](<images/lightboximage-image-3.png>) 

![](<images/lightboximage-image-4.png>)

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

![](<images/lightboximage-image-5.png>)

### Add rounded corners to images inside Light Box Image Pattern

To add rounded corners to images inside Light Box Image, add the following custom css to the theme.

```css
.lightbox-content-thumbnail img,
.pswp__item img {
    border-radius: var(--border-radius-soft);
}
```

![](<images/lightboximage-image-6.png>)
    