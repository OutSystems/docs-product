---
tags: runtime-traditionalweb; 
summary: Alert gets the end user's attention and highlights important information, errors or warnings on the screen.
locale: en-us
guid: 8b7fa781-fd52-47d6-a24a-1f0ffa05b99b
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=222%3A30&mode=design&t=ANpsYvOCthr9AWot-1
---

# Alert

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![Example of an Alert UI Pattern in a Traditional Web App](images/alert-image-1.png "Alert UI Pattern Example")

**How to use the Alert UI Pattern**

1. In Service Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![Screenshot showing the Alert widget in the Service Studio Toolbox](images/alert-image-7.png "Alert Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![Process of dragging the Alert widget into the Main Content area of an application's screen](images/alert-image-8.png "Dragging Alert Widget into Main Content")

1. Select the Text placeholder, and enter the Alert message you want to display.
    
    ![Entering the Alert message text into the Text placeholder of the Alert widget](images/alert-image-11.png "Setting Alert Message Text")

1. On the **Property** tab, set the mandatory **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. Additionally, the (optional) **ShowCloseButton** property is set to True. This enables a Close button for the Alert. 
    
    ![Property tab showing the AlertType property set to error in the Alert widget](images/alert-image-9.png "AlertType Property Settings")

    ![Property tab showing the ShowCloseButton property enabled in the Alert widget](images/alert-image-10.png "ShowCloseButton Property Settings")

1. After following these steps and publishing the module, you can test the pattern in your app. 

## Demo

<iframe width="750" height="500" src="https://www.youtube.com/embed/gknfwE7WX4U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>

## Properties

| **Property** | **Description** |
|---|---|
| AlertType (Alert Identifer): Mandatory | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>Entities.Alert.Warning - Displays a yellow warning message.</li><li>Entities.Alert.Info - Displays a blue information message.</li></ul> |
| ShowCloseButton (Boolean): Optional | Enable a **Close** button for the Alert.<br/><br/>Examples<br/><br/><ul><li>True - A **Close** button is enabled.</li><li>False - No **Close** button. This is the default value.</li></ul> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank No custom styles are added (default value).</li><li>"myclass" Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
