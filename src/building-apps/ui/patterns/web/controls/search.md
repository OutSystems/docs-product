---
tags: search functionality, ui design, widget customization, dependency management, local variables
summary: Learn how to implement the Search UI Pattern in OutSystems 11 (O11) for Traditional Web Apps, including widget setup and customization.
locale: en-us
guid: e0731879-d8a5-406c-b5a8-7b08cc36caee
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=234%3A51&mode=design&t=KpVEJMvnBwiukqql-1
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Search

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Search UI Pattern to provide users with a search field.

**How to use the Search UI Pattern**

1. In Service Studio, in the Toolbox, search for `Search`.

    The Search widget is displayed.

    ![Screenshot of the Search widget in the Service Studio toolbox](images/search-1-ss.png "Search Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Search widget into the Main Content area of your application's screen.

    ![Image showing how to drag the Search widget into the Main Content area of an application screen](images/search-2-ss.png "Dragging Search Widget to Main Content")

    By default, the Search widget contains Icon, Input, and Actions placeholders.

1. Create a local variable by right-clicking on your screen name and selecting **Add Local Variable**.

    ![Screenshot of the process to add a local variable in OutSystems Service Studio](images/search-3-ss.png "Creating a Local Variable")

1. Enter a name for the variable. In this example, we enter ``SearchText``.

   ![Image depicting the naming of a local variable as 'SearchText' in OutSystems Service Studio](images/search-4-ss.png "Naming the Local Variable")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Properties** | **Description** |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
