---
tags: runtime-traditionalweb; 
summary: ButtonGroup displays available choices to the user.
---

# ButtonGroup

Represent a choice of available options that are displayed.

Use the ButtonGroup to display all available choices to the user simultaneously. It is ideal when you have between two to four options. To show a larger number of options, consider using a Dropdown.

**How to use**

Add ButtonGroup items to the content placeholder.

1. Drag the ButtonGroup pattern into the preview.

1. By default, the pattern comes with three ButtonGroupItems.

    ![](<images/buttongroup-image-1.png>)

1. Drag as many ButtonGroupItems as you need.

1. Set a Variable and a Value.

    ![](<images/buttongroup-image-2.png>)

1. Change the text in the label of the ButtonGroupItems.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| IsJustified  |  The Items are evenly distributed in the space available. | Boolean | False | False |

## Layout and Classes

![](<images/buttongroup-image-3.png>)

## Advanced Use Case

### Use ButtonGroup with ListRecords

1. Drag the ButtonGroup Pattern into the preview.

1. In the Content placeholder, drag a ListRecords widget.

1. In the ListRecords widget, drag a ButtonGroupItem.

1. In the ButtonGroupItem, use expressions with the class btn to display the content.

    ![](<images/buttongroup-image-4.png>)

1. In the ListRecords Widget, set the Line Separator to None in order to avoid additional margin between elements.

1. Publish and test.
