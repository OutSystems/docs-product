---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Modal UI Pattern.
---

# Modal Reference

## Layout and classes

![](<images/modal-5-diag.png>)

## Advanced use case

### Change the animation speed

It is possible to change the animation speed of Modal by using custom CSS. To implement this in your application, copy the CSS to the theme.

```css
.modal .animate {
    -webkit-animation-duration: 500ms;
            animation-duration: 500ms;
}
```
