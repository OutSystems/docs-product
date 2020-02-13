---
tags: runtime-traditionalweb; 
summary: LoginForm is used to accelerate the creation of a custom login page.
---

# LoginForm

Component used in the OutSystems UI Login Layouts by default. Has CSS and Animated Labels along with all the basic pieces for a login.

![](<images/loginform-image-3.png>)

This component can be used to accelerate the creation of a custom login page.

**How to use**

Drag the block to the respective placeholder when creating a custom login page.

## Layout and Classes

![](<images/loginform-image-1.png>) ![](<images/loginform-image-2.png>)

### Login

Drag login related content to this placeholder.

## Advanced Use Case

### Add a Sign In button

1. In the Interface tab, go to the Login screen.

1. In the widgets tree, expand the Login placeholder.

1. Drag a Columns 2 structure to the "layout-login-button" container.

1. Drag the "Log In" button to the Column1 placeholder.

1. Drag a new button to the Column2 placeholder and set the value of the Label to "Sign In".

1. Publish and test.

    ![](<images/loginform-image-4.png>)

## Compatibility with other Patterns

[Layouts](layout-login.md)
