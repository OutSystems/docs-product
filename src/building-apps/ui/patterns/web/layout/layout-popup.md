---
tags: ui design, web development, application development, outsystems ui, web blocks
summary: Explore the Layout Popup in OutSystems 11 (O11), a customizable web block for displaying off-canvas information in Traditional Web Apps.
locale: en-us
guid: 6e0a8f5c-f734-4478-913e-21c6e81e8f1e
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=238:15
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# Layout Popup

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

The Layout Popup is a pre-existing web block useful for displaying additional off-canvas information. The web block is located in **UI Flows > OutSystemsUIWeb > Layouts**, and contains various placeholders and widgets that you can customize. You can then reuse and apply the web block to any of the screens in your app. 

![Screenshot of the Layout Popup web block in OutSystems Traditional Web App](images/layoutpopup-1-ss.png "Layout Popup Example")

For more information about creating and using a popup, see [RichWidgets Popup Editor](../../../inputs/popup.md).

## Properties

| Property | Description |
|---|---|
| DeviceConfiguration (DeviceConfig): Optional | Configuration that changes the default values that apply when the application is viewed on a phone, tablet, or desktop. |
| AccessibilityConfiguration (AccessibilityConfiguration): Optional | Configuration that changes the default values for the options that reset tab index values and the options that add a visible outline to focused elements. |
