---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Separator UI Pattern.
---

# Separator Reference

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
