---
tags: runtime-traditionalweb; 
summary: Fieldset labels groups of related interface elements and fields.
locale: en-us
guid: b22dd0ca-8b9a-4d0f-a848-384bec9e6bc9
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=245:97
---

# Fieldset

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can use the Fieldset UI Pattern to group and label related information, such as a users personal details, improving the overall look and layout of your application.

![Screenshot of an example Fieldset UI Pattern grouping related user information in a Traditional Web App](images/fieldset-1-ss.png "Fieldset UI Pattern Example")

**How to use the Fieldset UI Pattern**

1. In Service Studio, in the Toolbox, search for `Fieldset`.

    The Fieldset widget is displayed.

    ![Image showing the Fieldset widget in the Service Studio toolbox for Traditional Web Apps](images/fieldset-6-ss.png "Fieldset Widget in Service Studio")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.
    
    1. Select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Fieldset widget into the Main Content area of your application's screen.

    ![Screenshot demonstrating how to drag the Fieldset widget into the main content area of a Traditional Web App](images/fieldset-7-ss.png "Dragging Fieldset Widget into Main Content Area")

1. On the **Properties** tab, set the Title property.

    In the following example, we set the Title to `Basic Information`.

    ![Example of setting the Title property to 'Basic Information' for the Fieldset widget in a Traditional Web App](images/fieldset-5-ss.png "Setting the Title Property of Fieldset")

1. Add the relevant content to the placeholder, for example, text boxes and labels.

    ![Image showing the addition of text boxes and labels to the placeholder of a Fieldset in a Traditional Web App](images/fieldset-8-ss.png "Adding Content to Fieldset Placeholder")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Properties                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Title (Text): Mandatory        | The Fieldset title.  <p>Examples <ul><li>"Basic Information" - the title is set to Basic Information</li></ul></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>Blank - No custom styles are added (default value).</li><li>"myclass" - Adds the ``myclass`` style to the UI styles being applied.</li><li>"myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied.</li></ul>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |
