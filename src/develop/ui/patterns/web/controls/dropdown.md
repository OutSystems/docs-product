---
tags: runtime-traditionalweb; 
summary: Dropdown allows end-users to make a choice from several options.
---

# Dropdown

Allow end-users to make a choice from several options.

Use the Dropdown to offer a choice of more than four options. For a very large number of options, consider using the Dropdown Select to avoid loss of context.

**How to use**

Fill in the label of the Dropdown and add the required links in the DropdownList placeholder.

1. Drag the Dropdown pattern into the preview.

    ![](<images/dropdown-image-1.png?width=500>)

1. Set your content in the placeholders.
1. Publish and test.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |
  
## Layout and Classes

![](<images/dropdown-image-2.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| .dropdown |  .is--hidden |  Defines if the dropdown list is closed  |
| .dropdown |  .is--visible |  Defines if the dropdown list is open  |

## Advanced Use Case

### Use with ListRecords to make a list of links

1. Drag the Dropdown Pattern into the page.

1. In the DropdownList placeholder, drag a ListRecords widget.
1. Set the Line Separator property of the ListRecords widget to None.
1. In the ListRecords widget, drag a link and connect it to the required destination.
1. Inside the List, use expressions to display the content.
1. In the Prompt placeholder, set the text you want to define as the prompt.
1. Publish and test.

![](<images/dropdown-image-3.png>)

![](<images/dropdown-gif-1.gif>)
