---
tags: runtime-traditionalweb; 
summary: Floating Actions displays an action that floats in the bottom right corner of the screen.
---

# Floating Actions

You can use the Floating Actions UI Pattern to display an action that floats in the bottom right corner of the screen, providing access to a set of additional actions.

Use the Floating Action UI Pattern to show the primary action on a screen. Choose actions such as create, share, explore and so on. Avoid actions such as delete, archive or an alert. Exclude limited actions such as cut-and-paste text or actions that should be in a toolbar.

**How to use the Floating Actions UI Pattern**

1. In Service Studio, in the Toolbox, search for `Floating Actions`.

    The Floating Actions widget is displayed.

    ![](<images/floatingactions-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Floating Actions widget into the Main Content area of your application's screen.

    ![](<images/floatingactions-3-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

## Properties

### Floating Actions

| **Property** |  **Description** |
|---|---|
| Trigger (Trigger Identifier): Optional  | Set the type of trigger for the button. the predefined values are: <p><ul><li>Click</li><li>Hover</li><li>Manual</li></ul></p><p>Examples</p><p><ul><li>_Entities.Trigger.Click_ - Clicking the button triggers the button. This is the default.</li><li>_Entities.Trigger.Hover_ - Hovering over the button triggers the button.</li></ul></p> |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |

### Floating Actions Item

| **Property** |  **Description** |  
|---|---|
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles).
