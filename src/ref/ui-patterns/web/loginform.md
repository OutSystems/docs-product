---
tags: runtime-traditionalweb; 
summary: Explore the detailed guide on implementing and customizing the Login Form in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: bf2c05bb-2a29-4a57-903b-98007af0401b
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:521
---

# Login Form Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram showing the layout and classes of the Login Form for Traditional Web Apps](images/loginform-1-diag.png "Login Form Layout Diagram")

![Screenshot of the Login Form interface in a Traditional Web App](images/loginform-2-ss.png "Login Form Screenshot")

### Login

Drag login related content to this placeholder.

## Advanced use case

### Add a Sign In button

1. In the Interface tab, go to the Login screen.

1. In the widgets tree, expand the Login placeholder.

1. Drag a Columns 2 structure to the "layout-login-button" container.

1. Drag the "Log In" button to the Column1 placeholder.

1. Drag a new button to the Column2 placeholder and set the value of the Label to "Sign In".

1. Publish and test.

    ![Screenshot depicting the addition of a Sign In button to the Login Form](images/loginform-4-ss.png "Sign In Button Addition")

## Compatibility with other patterns

[Layouts](../../../building-apps/ui/patterns/web/layout/layout-login.md)
