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
| ExtendedClass (Text): Optional |  Add custom style classes to the Panel UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Panel UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Panel UI styles being applied.</li></ul></p> |
