---
tags: runtime-traditionalweb; 
summary: Layout Side Menu uses the space available on the side to improve navigation. 
locale: en-us
guid: a2d35777-96f1-42e8-b9b6-760eb59d24cd
---

# Layout Side Menu

The Layout Side Menu is a pre-existing web block for a side menu. The web block is located in **UI Flows > OutSystemsUIWeb > Layouts**, and contains various placeholders and widgets that you can customize. You can then reuse and apply the web block to any of the screens in your app.

![](<images/layoutsidemenu-1-ss.png?width=800>)

## Properties

| **Property** |  **Description** |  
|---|---|
| DeviceConfiguration (DeviceConfig): Optional  |  Configuration that changes the default values that apply when the application is viewed on a phone, tablet, or desktop. |
| AccessibilityConfiguration (AccessibilityConfiguration): Optional | Configuration that changes the default values for the options that reset tab index values and the options that add a visible outline to focused elements. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
