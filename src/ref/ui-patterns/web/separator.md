---
tags: runtime-traditionalweb; 
summary: Explore the Separator UI Pattern in Traditional Web Apps using OutSystems 11 (O11), detailing layout, CSS selectors, and advanced use cases.
locale: en-us
guid: fb3e8080-28b4-44a2-89dd-0c5c940c7e5a
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:570
---

# Separator Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes for the Separator UI Pattern in Traditional Web Apps](images/separator-2-diag.png "Separator Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .separator | .separator-horizontal |  When IsVertical parameter is False  |
| .separator | .separator-vertical |  When IsVertical parameter is True  |

## Advanced use case

### Use the vertical separator

1. Drag a container into the preview.

1. Create a class called "separator-height".

        .separator-height {
            height: 100px;
        }

1. Drag the Separator pattern into the container.

1. Set the IsVertical parameter to True.

1. Publish and test.

![Example of a vertical separator in a Traditional Web App interface](images/separator-3.png "Vertical Separator Example")
