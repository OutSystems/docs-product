---
tags: ui development, custom ui components, web blocks, ui customization, css customization
summary: Explore the Layout Side Menu web block in OutSystems 11 (O11) for customizable UI components in Traditional Web Apps.
locale: en-us
guid: a2d35777-96f1-42e8-b9b6-760eb59d24cd
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=238:17
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# Layout Side Menu

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

The Layout Side Menu is a pre-existing web block for a side menu. The web block is located in **UI Flows > OutSystemsUIWeb > Layouts**, and contains various placeholders and widgets that you can customize. You can then reuse and apply the web block to any of the screens in your app.

![Screenshot of the Layout Side Menu web block in OutSystems Traditional Web Apps](images/layoutsidemenu-1-ss.png "Layout Side Menu Screenshot")

## Properties

| **Property** |  **Description** |  
|---|---|
| DeviceConfiguration (DeviceConfig): Optional  |  Configuration that changes the default values that apply when the application is viewed on a phone, tablet, or desktop. |
| AccessibilityConfiguration (AccessibilityConfiguration): Optional | Configuration that changes the default values for the options that reset tab index values and the options that add a visible outline to focused elements. |
| ExtendedClass (Text): Optional  |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
