---
tags: runtime-mobileandreactiveweb;
summary: Sidebar shows additional content on the side of the screen.
---

# Sidebar

You can use the Sidebar UI Pattern to display additional information in the margin of the main content. The additional information supports the user's understanding of the main content.

![](<images/sidebar-4.png>)

**How to use the Sidebar UI Pattern**

In this example, we create a button that opens and closes the Sidebar widget.

1. In Service Studio, in the Toolbox, search for `Sidebar`.

    The Sidebar widget is displayed.

    ![](<images/sidebar-5-ss.png>)

1. From the Toolbox, drag the Sidebar widget into the Main Content area of your application's screen.

    ![](<images/sidebar-3-ss.png?width=800>)

1. On the **Properties** tab, in the **Name** field, enter a name for the Sidebar widget (in this example, we enter it `MySidebar`), and from the **IsOpen** dropdown, select a value (in this example, we select **False**).

    ![](<images/sidebar-1-ss.png>)

1. Add your content to the Header and Content placeholders, for example, forms, images, text etc. In this example we add some text.
   
    ![](<images/sidebar-8-ss.png?width=800>)

1. From the Toolbox, drag the Button widget just below the Sidebar widget and on the **Properties** tab, in the **Text** field, enter the text you want to appear on the button (in this example, we enter `Open`).

    ![](<images/sidebar-6-ss.png?width=800>)

1. To create a screen action for the button, double-click the button, select the **Logic** tab, and from the **Client Actions** folder, navigate to and drag the **SidebarToggle** action onto the screen action.

    ![](<images/sidebar-2-ss.png>)

1. On the **Properties** tab, from the **WidgetId** drop-down, select the Id for the widget. In this example, **MySidebar.Id**.

    ![](<images/sidebar-7-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
|---|---|
| IsOpen(Boolean): Mandatory | The variable that handles the state of the Sidebar. |
| ExtendedClass (Text): Optional | Add custom style classes to the Sidebar UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Sidebar UI styles being applied. </li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Sidebar UI styles being applied.</li></ul></p> |
