---
tags: runtime-traditionalweb; 
summary: Alert gets the end user's attention and highlights important information, errors or warnings on the screen.
---

# Alert

You can use the Alert UI Pattern to highlight important information, errors, or warnings.

![](<images/alert-image-1.png>)

**How to use the Alert UI Pattern**

1. In Service Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![](<images/alert-image-7.png>)

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![](<images/alert-image-8.png>)

1. Select the Text placeholder, and enter the Alert message you want to display.
    
    ![](<images/alert-image-11.png>)

1. On the **Property** tab, set the mandatory **AlertType** property. In this example, the alert type is set to error.
    
    ![](<images/alert-image-9.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 


## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/gknfwE7WX4U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

| **Property** |  **Description** | 
|---|---|
| AlertType (Alert Identifer): Mandatory  | Select the type of alert. the predefined options are: <p><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li><p>Examples<ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></p> | 
| ShowCloseButton (Boolean): Optional  | Enable a Close button for the Alert. <p>Examples<ul><li>_True_ A close button is enabled.</li><li>_False_ - There is no Close button. This is the default value.</li></p> 
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/alert-image-2.png>)

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

    ![](<images/alert-image-3.png>)

1. Drag the Animate pattern into the container.
1. Change the EnterAnimation property to EnterTop.

    ![](<images/alert-image-4.png>)

1. Drag the Alert pattern into the Animate placeholder.
1. Set the Alert type (mandatory value).
1. Type the message you want to display.

    ![](<images/alert-image-5.png>)
    
1. Publish and test.

    ![](<images/alert-image-6.gif>)

