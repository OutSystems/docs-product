---
tags: runtime-traditionalweb; 
summary: Sidebar shows additional content on the side of the screen.
---

# Sidebar

Shows additional content on the side of the screen.

Use the Sidebar to place additional information in the margin of the main content. The additional information supports the end-user's understanding of the main content. 

**How to use**

To trigger the sidebar, call a new screen action through a button with Ajax submit and use the ToggleSidebar action (found in the Logic Tab) to open/close it. Use the parameters to define if it has Overlay in the page.

1. Drag the Sidebar pattern into the preview.

1. Set the content in the placeholders.

    ![](<images/sidebar-image-1.png>)

1. Publish and test.

    ![](<images/sidebar-image-2.png?width=750>)


## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| HasOverlay  |  When set to true enables a clickable overlay. |  Boolean | False | False |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/sidebar-image-3.png>)

## CSS Selectors

| **Element** |  **CSS Class** |  **Description**  |
| --- | --- | --- |
| .sidebar | .sidebar.is--hidden |  When Sidebar is closed  |
| .sidebar | .sidebar.is--visible |  When Sidebar is open  |
