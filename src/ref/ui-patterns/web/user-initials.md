---
tags: runtime-traditionalweb;
summary: Advanced use cases for the User Initials UI Pattern.
locale: en-us
guid: 02ba4227-0341-4645-8202-58dcb3119d8d
---

# User Initials Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/userinitials-2-diag.png>)

## Advanced use case

### Use the User Initials Pattern with tables

1. Drag the Users table into preview.

1. Remove the expression from the Name and drag the UserInitials pattern to it.

1. In the UserInititals, set the name parameter to the value of the name field from the database.

    ![](<images/userinitials-3-ss.png>)

1. Change the pattern values.

1. Publish and test.

### Use the User Initials Pattern with IF conditions

1. Create a custom class called "table-image-size".

        .table-image-size {
            height: 100px;
            width: 100px;
        }

1. Drag the Users Entity into the preview.

1. Remove the expression from the Name and drag a container into the cell.

1. Drag an IF condition tool into the container and set the condition to `UserTable.List.Current.User.Is_Active`.

    ![](<images/userinitials-5-ss.png>)

1. In the True branch, drag the UserInitials pattern and set the name parameter to the value of the name field from the database.

1. To adapt the UserInitials to the size of container, set the ExtendedClass parameter to `full-width full-height`.

    ![](<images/userinitials-6-ss.png>)

1. In the False branch, drag an image and set the Style Classes to  `border-radius-circle`.

    ![](<images/userinitials-7-ss.png>)

1. Publish and test.

    ![](<images/userinitials-8-ss.png?width=750>)
