---
tags: runtime-traditionalweb; 
summary: Explore advanced customization of modal animation speeds in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: a9618344-1b9f-4aa8-892b-456d7d7a75eb
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:525
---

# Modal Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of a Modal component in Traditional Web Apps](images/modal-5-diag.png "Modal Layout and Classes Diagram")

## Advanced use case

### Change the animation speed

It is possible to change the animation speed of Modal by using custom CSS. To implement this in your application, copy the CSS to the theme.

```css
.modal .animate {
    -webkit-animation-duration: 500ms;
            animation-duration: 500ms;
}
```
