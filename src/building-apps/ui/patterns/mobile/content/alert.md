---
tags: ide usage, reactive web apps, tutorials for beginners, ui design, ui patterns
summary: Explore how to implement and customize the Alert UI Pattern in OutSystems 11 (O11) for mobile and reactive web apps.
locale: en-us
guid: 19bf61bf-cf92-4e5f-b0d1-44f667b32bc7
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:5
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Alert

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Alert UI Pattern to highlight and display important information, errors, or warnings.

![Example of an Alert UI Pattern in a mobile or reactive web app](images/alert-1.png "Alert UI Pattern Example")

**How to use the Alert UI Pattern**

1. In Service Studio, in the Toolbox, search for `Alert`.

    The Alert widget is displayed.

    ![Service Studio displaying the Alert widget in the Toolbox](images/alert-7-ss.png "Service Studio Alert Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Alert widget into the Main Content area of your application's screen.

    ![Dragging the Alert widget into the Main Content area in Service Studio](images/alert-8-ss.png "Dragging Alert Widget")

1. Select the MessageText placeholder, and enter the Alert message you want to display.
    
    ![Selecting the MessageText placeholder to enter an Alert message](images/alert-11-ss.png "Setting Alert Message")

1. On the **Property** tab, set the **AlertType** property. In this example, the alert type is set to error which changes the message to display in red. 
    
    ![Setting the AlertType property to error in the Property tab](images/alert-9-ss.png "Alert Type Property")

After following these steps and publishing the module, you can test the pattern in your app. 


## Properties

| **Property**                           | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlertType (Alert Identifer): Mandatory | Select the type of alert. the predefined options are:<br/><br/><ul><li>Error</li><li>Info</li><li>Success</li><li>Warning</li></ul><br/>Examples<br/><br/><ul><li>_Entities.Alert.Warning_ - Displays a yellow warning message.</li><li>_Entities.Alert.Info_ - Displays a blue information message.</li></ul>                                                                                                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional         | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank No custom styles are added (default value).</li><li>"myclass" Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. </li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
