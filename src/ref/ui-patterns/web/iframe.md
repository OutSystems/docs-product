---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Iframe UI Pattern.
---

# Iframe Reference

## Layout and classes

![](<images/iframe-3-diag.png>)

## Advanced use case

### Change the Iframe width according to the device

This can be very useful if you are using a fixed width.

1. Set the Width to `If(IsDesktop(), "500px", "100%")`.

1. Publish and test.

    ![](<images/iframe-4-ss.png>)

You can change the condition of the width used. This code makes the width 500px on desktop, but on mobile, it is still full-width as the fixed width would probably overflow the screen.
