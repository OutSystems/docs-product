---
tags: runtime-traditionalweb; 
summary: Sidebar shows additional content on the side of the screen.
---

# Sidebar

You can use the Sidebar UI Pattern to display additional information in the margin of the main content. The additional information supports the user's understanding of the main content.

![](<images/sidebar-image-4.png>)

**How to use the Sidebar UI Pattern**

In this example, we create a button that opens and closes the Sidebar widget.

To trigger the sidebar, call a new screen action through a button with Ajax submit and use the ToggleSidebar action (found in the Logic Tab) to open/close it. Use the parameters to define if it has Overlay in the page.

1. In Service Studio, in the Toolbox, search for `Sidebar`. 

    The Sidebar widget is displayed.

    ![](<images/sidebar-image-5.png>)

1. From the Toolbox, drag the Sidebar widget into the Main Content area of your application's screen.

    ![](<images/sidebar-image-6.png>)

1. On the **Properties** tab, in the Name field, enter a name for the Sidebar widget. In this example, we call it **MySidebar**.

    ![](<images/sidebar-image-name.png>)

1. Add your content to the Header and Content placeholders, for example, forms, images, text etc. In this example we add some text. 
   
    ![](<images/sidebar-image-content.png>)

1. From the Toolbox, drag the Button widget just below the Sidebar widget and on the **Properties** tab, in the **Label** field, enter the text you want to appear on the button (in this example, we enter **Open**) and from the **Method** drop-down, select **Ajax Submit**.

    ![](<images/sidebar-image-button-ajax.png>)

1. To create a screen action for the button, double-click the button, select the **Logic** tab, and from the **Server Actions** folder, navigate to and drag the ToggleSidebar action onto the screen action.

    ![](<images/sidebar-image-toggle.png>)

1. On the **Properties** tab, from the **WidgetId** drop-down, select the Id for the widget. In this example, **MySidebar.Id**.

    ![](<images/sidebar-toggle-properties.png>)

After following these steps and publishing the module, you can test the pattern in your app. 


## Properties

| **Property** |  **Description** | 
|---|---|---|
| HasOverlay(Boolean): Optional  | If set to True, an overlay is displayed behind the Sidebar. If set to False, there is no overlay. This is the default value. |
| ExtendedClass (Text): Optional | Add custom style classes to the Sidebar UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Sidebar UI styles being applied. </li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Sidebar UI styles being applied.</li></ul></p> | 
