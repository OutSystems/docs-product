---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Separator UI Pattern.
locale: en-us
guid: fb3e8080-28b4-44a2-89dd-0c5c940c7e5a
app_type: traditional web apps
platform-version: o11
---

# Separator Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/separator-2-diag.png>)

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

![](<images/separator-3.png>)
