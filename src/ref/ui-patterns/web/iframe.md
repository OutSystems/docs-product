---
tags: runtime-traditionalweb; 
summary: Explore Iframe customization for traditional web apps in OutSystems 11 (O11), including responsive width adjustments based on device type.
locale: en-us
guid: d2e2b815-ef17-438b-b200-fe7ec9c1cd23
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:485
---

# Iframe Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of an Iframe in a traditional web app](images/iframe-3-diag.png "Iframe Layout Diagram")

## Advanced use case

### Change the Iframe width according to the device

This can be very useful if you are using a fixed width.

1. Set the Width to `If(IsDesktop(), "500px", "100%")`.

1. Publish and test.

    ![Screenshot demonstrating how to change the Iframe width according to the device in a traditional web app](images/iframe-4-ss.png "Iframe Width Adjustment Example")

You can change the condition of the width used. This code makes the width 500px on desktop, but on mobile, it is still full-width as the fixed width would probably overflow the screen.
