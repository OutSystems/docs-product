---
tags: runtime-traditionalweb; 
summary: Fieldset labels groups of related interface elements and fields.
---

# Fieldset

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Fieldset UI Pattern to group and label related information, such as a users personal details, improving the overall look and layout of your application.

![](<images/fieldset-1-ss.png>)

**How to use the Fieldset UI Pattern**

1. In Service Studio, in the Toolbox, search for `Fieldset`.

    The Fieldset widget is displayed.

    ![](<images/fieldset-6-ss.png>)

    If the UI widget doesn't display, it's because the dependency isn't added. For example, if you are using a ready-made app, it deletes unused widgets from the module. Make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.
    
    1. In **Search in other Modules**, select the widget you want to add from the **OutSystemsUIWeb** module, and click **Add Dependency**. 
    
    1. In the Toolbox, search for the widget again.

1. From the Toolbox, drag the Fieldset widget into the Main Content area of your application's screen.

    ![](<images/fieldset-7-ss.png>)

1. On the **Properties** tab, set the Title property.

    In the following example, we set the Title to `Basic Information`.

    ![](<images/fieldset-5-ss.png>)

1. Add the relevant content to the placeholder, for example, text boxes and labels.

    ![](<images/fieldset-8-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Properties | Description |
|---|---|
| Title (Text): Mandatory   |  The Fieldset title.  <p>Examples <ul><li>_"Basic Information"_ - the title is set to Basic Information</li></ul></p> | 
| ExtendedClass (Text): Optional  | Adds custom style classes to the Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass style_ to the UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the UI styles being applied.</li></ul></p>You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Live Style Guide](https://outsystemsui.outsystems.com/StyleGuidePreview/Styles). |
