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

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

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
| AlertType (Alert Identifer): Mandatory  | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></ul> | 
| ShowCloseButton (Boolean): Optional  | Enable a Close button for the Alert.<br/><br/>Examples<br/><br/><ul><li>_True_ A close button is enabled.</li><li>_False_ - No Close button. This is the default value.</li></ul> |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ No custom styles are added (default value).</li><li>_"myclass"_ Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
