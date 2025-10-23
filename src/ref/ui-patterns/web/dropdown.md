---
tags: component customization, dropdown menus, web development, css selectors, frontend engineering
summary: Explore dropdown component customization in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: 53de8e92-e178-4967-a3cc-e36407f71669
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:452
audience:
  - frontend developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Dropdown Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Image illustrating the layout and classes of a dropdown component in a traditional web app](images/dropdown-image-2.png "Dropdown Layout")

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|--- |
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

    ![Screenshot showing the use of ListRecords with a dropdown to create a list of links](images/dropdown-image-3.png "Dropdown ListRecords Example")

    <iframe src="https://player.vimeo.com/video/996245584" width="458" height="658" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the interaction with a dropdown in a traditional web app.</iframe>
