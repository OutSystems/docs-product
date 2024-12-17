---
tags: ui customization, css, web development, component customization, design systems
summary: Explore card component customization in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: 64b922a7-ca05-4d8f-bb40-2c75539b0bc2
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:405
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Card Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of a card component in a traditional web app](images/card-2-diag.png "Card Layout Diagram")

## Advanced use case

### Change background color

1. Write the following classes in the ExtendedClass property of the card.
    `background-yourcolor text-neutral-0 border-size-none `

    ![Screenshot showing how to change the background color of a card by adding classes in the ExtendedClass property](images/card-3-ss.png "Card Background Color Change")
    
    The class `text-neutral-0` is to set the text-color to white, in contrast with the new background. The `border-size-none` class is to remove the border.
    
1. Publish and test.

    **Before**

    ![Image of a card before the background color change, showing the default appearance](images/card-4.png "Card Before Background Change")

    **After**

    ![Image of a card after the background color change, demonstrating the contrast with white text and no border](images/card-5.png "Card After Background Change")
