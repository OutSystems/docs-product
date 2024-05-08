---
tags: runtime-traditionalweb; 
summary: Explore the CSS selectors and advanced use cases for the Alert UI Pattern in OutSystems 11 (O11) for Traditional Web Apps.
locale: en-us
guid: 252cc44d-c1de-4848-869b-55f9c33c3430
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:355
---

# Alert Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and Classes

![Screenshot showing the layout and classes of the Alert UI Pattern in a traditional web application](images/alert-image-2.png "Alert UI Pattern Layout")

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .alert | .alert-error |  When Alert type selected is Error  |
| .alert | .alert-info |  When Alert type selected is Info  |
| .alert | .alert-success |  When Alert type selected is Success  |
| .alert | .alert-warning |  When Alert type selected is Warning  |
| .alert | .alert-close.is--hidden |  When ShowCloseButton parameter is False  |

## Advanced Use Case

### Add enter animation to Alert pattern

1. Create a local variable of type Boolean called "ShowAlert" and set the default value to False.

1. Drag a container into preview and name it (for instance, AlertAnimation).

1. In the properties of the container, change the display from True to ShowAlert.

    ![Image displaying the properties settings of the Alert animation container in a web application](images/alert-image-3.png "Alert Animation Container Properties")

1. Drag the Animate pattern into the container.

1. Change the EnterAnimation property to EnterTop.

    ![Image demonstrating the process of setting the Enter Animation property for the Alert pattern in a web application](images/alert-image-4.png "Setting Enter Animation Property")

1. Drag the Alert pattern into the Animate placeholder.

1. Set the Alert type (mandatory value).

1. Type the message you want to display.

    ![Image illustrating the user interface for configuring the Alert message within the Alert pattern](images/alert-image-5.png "Configuring Alert Message")
    
1. Publish and test.

    ![Animated GIF demonstrating the Alert pattern with enter animation in a web application](images/alert-image-6.gif "Alert Pattern Animation Demonstration")
