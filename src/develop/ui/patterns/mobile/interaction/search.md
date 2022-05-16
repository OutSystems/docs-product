---
tags: runtime-mobileandreactiveweb;
summary: Search allows the user to find pieces of content without the use of navigation.
locale: en-us
guid: 583538cf-ffe1-4c39-9fe5-60667fd05f26
app_type: mobile apps, reactive web apps
---

# Search

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Search UI Pattern to provide users with a search field. Use the Search UI Pattern to allow users find pieces of content by entering queries. Unlike navigation, knowledge of the content's location isn't required and searching is often the primary means of finding content.

![](<images/search-5-ss.png>)

**How to use the Search UI Pattern**

1. In Service Studio, in the Toolbox, search for `Search`.

    The Search widget is displayed.

    ![](<images/search-1-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Search widget into the Main Content area of your application's screen.

    ![](<images/search-2-ss.png>)

    By default, the Search widget contains an Input placeholder and widget.

1. Select the Input widget, and on the **Properties** tab, create a local variable by selecting the **Variable** dropdown and selecting **New Local Variable**.

    ![](<images/search-3-ss.png>)

1. Enter a name for the variable.

    In this example, we enter `SearchText`.

    ![](images/search-4-ss.png)

    This variable holds the value entered by the user. This variable can be reused throughout your app.

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Properties | Description |
|---|---|
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/><ul><li>Blank - No custom styles are added (default value). </li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |  
