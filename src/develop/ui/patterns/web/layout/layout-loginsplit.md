---
tags: runtime-traditionalweb; 
summary: LayoutLoginSplit is a custom page layout for the login screen that divides the page into 2 columns.
---

# LayoutLoginSplit

A custom page layout for the login screen that divides the page into 2 columns. 

**How to use**

1. In the Login screen, select the object tree and use LayoutLoginSplit instead of the current Layout. 
1. OutSystems UI Layout Login already has the LoginForm by default. Add input widgets to the correct placeholders as required.

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| DeviceConfiguration  |  Configuration to change the default values that set when the application will be seen as phone, tablet or desktop |  DeviceConfig | False | none |

## Layout and Classes

![](<images/layout-loginsplit-image-1.png>)

### Login

Drag login related content to this placeholder.

## Advanced Use Case

### Change background to image

1. In the Interface tab, go to the Login screen.
1. Remove the background container and drag an image. 
1. Publish and test.
    
    ![](<images/layout-loginsplit-gif-1.gif?width=600>)

### Change Layout structure

1. In the Interface tab, go to the Login screen.
1. Change the Column type by using the corresponding parameter (for instance, ColumnsMediumRight).
1. Publish and test.
    
    ![](<images/layout-loginsplit-gif-2.gif?width=600>)

## Compatibility with other Patterns

LoginForm
