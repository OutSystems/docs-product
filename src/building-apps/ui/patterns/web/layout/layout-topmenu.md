---
tags: runtime-traditionalweb; 
summary: Layout Top Menu uses the space available on the top for navigation.
locale: en-us
guid: a4be094e-5543-4200-8b86-4a6b834f7cc6
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=238:19
---

# Layout Top Menu

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

The Layout Top Menu is a pre-existing web block for a fixed top menu and is useful for simple apps, without a complex navigation structure. The web block is located in **UI Flows > OutSystemsUIWeb > Layouts**, and contains various placeholders and widgets that you can customize. You can then reuse and apply the web block to any of the screens in your app.

![Screenshot of the Layout Top Menu web block in OutSystems UI showing placeholders and widgets for customization](images/layouttopmenu-1-ss.png "Layout Top Menu in OutSystems")

## Properties

| **Property** |  **Description** |
|---|---|
| DeviceConfiguration (DeviceConfig): Optional  |  Configuration that changes the default values that apply when the application is viewed on a phone, tablet, or desktop. |
| AccessibilityConfiguration (AccessibilityConfiguration): Optional | Configuration that changes the default values for the options that reset tab index values and the options that add a visible outline to focused elements. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
