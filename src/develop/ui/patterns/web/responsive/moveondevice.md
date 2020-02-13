---
tags: runtime-traditionalweb; 
summary: MoveOnDevice defines where information is displayed thereby improving the display on different devices.
---

# MoveOnDevice 

Defines the target container for several elements in different devices without duplicating them.

Use Move on Device to define where information is displayed thereby improving the display on different devices.

**How to use**

1. Drag the MoveOnDevice pattern into the preview.

    ![](<images/moveondevice-image-1.png>)

1. Set the required content in the placeholder.
1. Set the Ids of the target containers you want to move the content to.

    ![](<images/moveondevice-image-2.png>)

1. Publish and test.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| PhoneWidgetId | Target container that will receive this block on phones. | Text | No | none |
| TabletWidgetId | Target container that will receive this block on tablets. | Text | No | none |
