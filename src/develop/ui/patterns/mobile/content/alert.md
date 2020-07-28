---
tags: runtime-mobileandreactiveweb;  
summary: Alert gets the end user's attention and highlights important information, errors or warnings on the screen.
---

# Alert

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![](<images/alert-1.png>)

**How to use the Alert UI Pattern**

1. In Service Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![](<images/alert-7-ss.png>)

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![](<images/alert-8-ss.png?width=800>)

1. Select the MessageText placeholder, and enter the Alert message you want to display.
    
    ![](<images/alert-11-ss.png>)

1. On the **Property** tab, set the **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. 
    
    ![](<images/alert-9-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 


## Properties

| **Property** |  **Description** | 
|---|---|
| AlertType (Alert Identifer): Mandatory  | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></ul> | 
| ExtendedClass (Text): Optional  |  Add custom style classes to the Alert UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the Alert UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Alert UI styles being applied. </li></ul> |
