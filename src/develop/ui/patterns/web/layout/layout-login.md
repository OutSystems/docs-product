---
tags: runtime-traditionalweb; 
summary: LayoutLogin is a custom page layout for the login screen.
---

# LayoutLogin

A custom page layout for the login screen.

**How to use**

OutSystems UI already has LayoutLogin and LoginForm by default. Add input widgets to the correct placeholders as required.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| DeviceConfiguration  |  Configuration to change the default values that set when the application will be seen as phone, tablet or desktop |  DeviceConfig | False | none |

## Layout and Classes

![](<images/layoutlogin-image-1.png>)

### Login

Drag login related content to this placeholder.

### BackgroundImage

Drag an image, GIF or video to this placeholder.

## Advanced Use Case

### Change background-color

1. In the Interface tab, go to the Login screen.
1. Drag a container to the BackgroundImage placeholder.
1. Set the Style Classes of that container to `full-height background-your-color`. 
1. Publish and test.

![](<images/layoutlogin-image-2.png?width=750>)

## Compatibility with other Patterns

[LoginForm](loginform.md)
