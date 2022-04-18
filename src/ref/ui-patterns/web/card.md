---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Card UI Pattern.
locale: en-us
guid: 64b922a7-ca05-4d8f-bb40-2c75539b0bc2
app_type: traditional web apps
---

# Card Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/card-2-diag.png>)

## Advanced use case

### Change background color

1. Write the following classes in the ExtendedClass property of the card.
    `background-yourcolor text-neutral-0 border-size-none `

    ![](<images/card-3-ss.png>)
    
    The class `text-neutral-0` is to set the text-color to white, in contrast with the new background. The `border-size-none` class is to remove the border.
    
1. Publish and test.

    **Before**

    ![](<images/card-4.png>)

    **After**

    ![](<images/card-5.png>)
