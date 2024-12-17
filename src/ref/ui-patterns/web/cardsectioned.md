---
tags: ui patterns, responsive design, css, accessibility, web development
summary: Explore the Card Sectioned UI Pattern in OutSystems 11 (O11), detailing layout, CSS classes, and responsive orientation adjustments.
locale: en-us
guid: 31a87c67-318b-4a23-8ce5-f46cdca4a0ab
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:416
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Card Sectioned Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of the Card Sectioned UI Pattern](images/cardsectioned-2-diag.png "Card Sectioned Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---
| .card-sectioned |  .flex-direction-row |  When the parameter Orientation of the card is set to horizontal |
| .card-sectioned |  .flex-direction-column | When the parameter Orientation of the card is set to vertical  |
| .card-image |  .padding-none | When the parameter ImagePadding of the card is set to False  |
| .card-sectioned |  .card-sectioned-right | When the parameter IsRight is set to True  |

## Advanced use case

### Change orientation according to device

1. Drag the Card Sectioned Pattern into the preview.

1. Set the Orientation parameter to `If(IsPhone(),Entities.Orientation.Vertical, Entities.Orientation.Horizontal)`. Use the server action IsPhone as the condition to set the orientation for a phone. You can also use the IsTablet action or invert the False & True statements, according to your needs. This way, the CardSectioned pattern will be horizontal on Desktop and Tablet. On the Phone, it will be vertical.

1. Publish and test.

**Desktop & Tablet**

![Example of the Card Sectioned Pattern displayed on desktop and tablet devices](images/cardsectioned-3.png "Card Sectioned on Desktop & Tablet")

**Phone**

![Example of the Card Sectioned Pattern displayed on a phone device](images/cardsectioned-4.png "Card Sectioned on Phone")

## Notes
The parameter IsRight only works if the parameter Orientation is Not Vertical.
