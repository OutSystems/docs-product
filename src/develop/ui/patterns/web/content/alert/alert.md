---
tags: runtime-traditionalweb; 
summary: Alert gets the end user's attention and highlights important information, errors or warnings on the screen.
---

# Alert

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![](<images/alert-image-1.png>)

**How to use the Alert UI Pattern**

1. In Service Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![](<images/alert-image-7.png>)

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![](<images/alert-image-8.png>)

1. Select the Text placeholder, and enter the Alert message you want to display.
    
    ![](<images/alert-image-11.png>)

1. On the **Property** tab, set the mandatory **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. Additionally, the (optional) **ShowCloseButton** property is set to True. This enables a Close button for the Alert. 
    
    ![](<images/alert-image-9.png>)

    ![](<images/alert-image-10.png>)

1. After following these steps and publishing the module, you can test the pattern in your app. 


## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/gknfwE7WX4U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

| **Property** |  **Description** | 
|---|---|
| AlertType (Alert Identifer): Mandatory  | Select the type of alert. the predefined options are: <p><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li><p>Examples<ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></p> | 
| ShowCloseButton (Boolean): Optional  | Enable a Close button for the Alert. <p>Examples<ul><li>_True_ A close button is enabled.</li><li>_False_ - No Close button. This is the default value.</li></p> |
| ExtendedClass (Text): Optional  |  Add custom style classes to the Alert UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Alert UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Alert UI styles being applied.  |

