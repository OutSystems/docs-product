---
tags: runtime-traditionalweb; 
summary: Learn how to implement the Floating Actions UI Pattern in OutSystems 11 (O11) for enhanced user interface design in Traditional Web Apps.
locale: en-us
guid: 2d4b31df-c2f5-46c6-945b-8fd711f22542
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=232%3A4&mode=design&t=KpVEJMvnBwiukqql-1
---

# Floating Actions

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Floating Actions UI Pattern to display an action that floats in the bottom right corner of the screen, providing access to a set of additional actions.

Use the Floating Action UI Pattern to show the primary action on a screen. Choose actions such as create, share, explore and so on. Avoid actions such as delete, archive or an alert. Exclude limited actions such as cut-and-paste text or actions that should be in a toolbar.

**How to use the Floating Actions UI Pattern**

1. In Service Studio, in the Toolbox, search for `Floating Actions`.

    The Floating Actions widget is displayed.

    ![Screenshot of Service Studio showing the Floating Actions widget in the Toolbox](images/floatingactions-1-ss.png "Service Studio Floating Actions Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Floating Actions widget into the Main Content area of your application's screen.

    ![Screenshot of dragging the Floating Actions widget into the Main Content area in Service Studio](images/floatingactions-3-ss.png "Dragging Floating Actions Widget to Main Content")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Floating Actions

| **Property** | **Description** |
|---|---|
| Trigger (Trigger Identifier): Optional | Set the type of trigger for the button. the predefined values are: <p><ul><li>Click</li><li>Hover</li><li>Manual</li></ul></p><p>Examples</p><p><ul><li>Entities.Trigger.Click - Clicking the button triggers the button. This is the default.</li><li>Entities.Trigger.Hover - Hovering over the button triggers the button.</li></ul></p> |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

### Floating Actions Item

| **Property** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
