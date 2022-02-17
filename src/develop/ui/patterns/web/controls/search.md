---
tags: runtime-traditionalweb; 
summary: Search allows the user to find pieces of content without the use of navigation.
---

# Search

You can use the Search UI Pattern to provide users with a search field.

**How to use the Search UI Pattern**

1. In Service Studio, in the Toolbox, search for `Search`.

    The Search widget is displayed.

    ![](<images/search-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Search widget into the Main Content area of your application's screen.

    ![](<images/search-2-ss.png>)

    By default, the Search widget contains Icon, Input, and Actions placeholders.

1. Create a local variable by right-clicking on your screen name and selecting **Add Local Variable**.

    ![](<images/search-3-ss.png>)

1. Enter a name for the variable. In this example, we enter ``SearchText``.

   ![](images/search-4-ss.png)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Properties** |  **Description** |  
|---|---|
|ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>_Blank_ - No custom styles are added (default value). </li><li>_"myclass"_ - Adds the _myclass_ style to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |  
