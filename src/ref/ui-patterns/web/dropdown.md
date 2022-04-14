---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Dropdown UI Pattern.
locale: en-us
guid: 53de8e92-e178-4967-a3cc-e36407f71669
---

# Dropdown Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

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



