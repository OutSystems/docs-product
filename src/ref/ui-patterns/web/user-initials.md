---
tags: runtime-traditionalweb;
summary: Advanced use cases for the User Initials UI Pattern.
locale: en-us
guid: 02ba4227-0341-4645-8202-58dcb3119d8d
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:618
---

# User Initials Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes for the User Initials UI Pattern in Traditional Web Apps](images/userinitials-2-diag.png "User Initials Layout Diagram")

## Advanced use case

### Use the User Initials Pattern with tables

1. Drag the Users table into preview.

1. Remove the expression from the Name and drag the UserInitials pattern to it.

1. In the UserInititals, set the name parameter to the value of the name field from the database.

    ![Screenshot of the User Initials Pattern being used within a table in a Traditional Web App](images/userinitials-3-ss.png "User Initials in Table Preview")

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

    ![Screenshot showing the IF condition tool being used in the User Initials Pattern setup](images/userinitials-5-ss.png "IF Condition Tool in User Initials")

1. In the True branch, drag the UserInitials pattern and set the name parameter to the value of the name field from the database.

1. To adapt the UserInitials to the size of container, set the ExtendedClass parameter to `full-width full-height`.

    ![Screenshot of the True branch configuration for the User Initials Pattern with extended class parameters](images/userinitials-6-ss.png "User Initials True Branch Configuration")

1. In the False branch, drag an image and set the Style Classes to  `border-radius-circle`.

    ![Screenshot of the False branch in the User Initials Pattern showing an image with a circular border](images/userinitials-7-ss.png "User Initials False Branch Image")

1. Publish and test.

    ![Screenshot of the published test for the User Initials Pattern in a Traditional Web App](images/userinitials-8-ss.png "Published User Initials Test")
