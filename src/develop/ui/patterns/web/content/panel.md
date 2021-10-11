---
tags: runtime-traditionalweb; 
summary: Panel groups short pieces of information in small blocks and highlights them on the screen with a specific structure.
---

# Panel

You can use the Panel UI Pattern to group information in a small block, organized in different sections for title, actions, content, and a small footer that is easily noticeable.

Use a panel to group short pieces of information and highlight them on the screen with a specific structure.

![](<images/panel-1.png>)

**How to use the Panel UI Pattern**

1. In Service Studio, in the Toolbox, search for `Panel`.
  
    The Panel widget is displayed.

    ![](<images/panel-2-ss.png>)

    If the UI widget does not display, it may be because you used a ready-made app, which deletes unused widgets from the module. To make additional widgets available in your app:

    a. Go to **Module > Manage dependencies**.

    b. Search for and select the relevant Producer, for example OutSystemsUI. Ensure Show All is selected. 

    c. On the Public elements for the selected Producer displayed on the right, ensure Show All is selected.
    
    d. Search for and select the element you want to add, and click **Apply**. 
    
    e. In Service Studio, in the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Panel widget into the Main Content area of your application's screen.

    ![](<images/panel-3-ss.png?width=800>)

    By default, the Panel widget contains Title, Actions, Content, and Footer placeholders.

1. Add your content to the placeholders. In this example, we add a title to the Title placeholder, text to the Content placeholder, and a button to the Actions placeholder.

    ![](<images/panel-4-ss.png?width=800>)

1. Add the desired action to the content you have added to the Actions placeholder. In this example, the button we added redirects the user to a new page.

    ![](<images/panel-5-ss.png?width=800>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Properties** |  **Description** |  
|---|---|
| ExtendedClass (Text): Optional |  Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
