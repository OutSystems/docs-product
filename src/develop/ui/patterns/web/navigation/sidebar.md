---
tags: runtime-traditionalweb; 
summary: Sidebar shows additional content on the side of the screen.
---

# Sidebar

You can use the Sidebar UI Pattern to place additional information in the margin of the main content. The additional information supports the user's understanding of the main content.

![](<images/sidebar-image-4.png>)

**How to use the Sidebar UI Pattern**

To trigger the sidebar, call a new screen action through a button with Ajax submit and use the ToggleSidebar action (found in the Logic Tab) to open/close it. Use the parameters to define if it has Overlay in the page.

1. In Service Studio, in the Toolbox, search for `Sidebar`. 

    The Sidebar widget is displayed.

    ![](<images/sidebar-image-5.png>)


1. From the Toolbox, drag the Sidebar widget onto your application's screen.

1. Set the relevant content in the placeholders.

    ![](<images/sidebar-image-1.png>)

After following these steps and publishing the module, you can test the pattern in your app. 

![](<images/sidebar-image-2.png?width=750>)


## Properties

| **Property** |  **Description** |  **Usage** |
|---|---|---|
| HasOverlay(Boolean): Optional  |  When set to true enables a clickable overlay. |
| ExtendedClass(Text): Optional  |  Add custom style classes to the block. |  

## See also
* OutSystems UI Live Style Guide: [Sidebar](https://outsystemsui.outsystems.com/WebStyleGuidePreview/Sidebar.aspx)
* OutSystems UI Pattern Page: [Sidebar](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/PatternDetail?PatternId=67)
