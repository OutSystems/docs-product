---
tags: runtime-traditionalweb; 
summary: Fieldset labels groups of related interface elements and fields.
---

# Fieldset

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can use the Fieldset UI Pattern to group and label related information, such as a users personal details, improving the overall look and layout of your application.

![](<images/fieldset-image-1.png>)

**How to use the Fieldset UI Pattern**

1. In Service Studio, in the Toolbox, search for `Fieldset`.

    The Fieldset widget is displayed.

   ![](<images/fieldset-image-6.png>)

1. From the Toolbox, drag the Fieldset widget into the Main Content area of your application's screen.

   ![](<images/fieldset-image-7.png>)

1. On the **Properties** tab, set the Title property.

    In the following example, we set the Title to `Basic Information`.

    ![](<images/fieldset-image-5.png>)

1. Add the relevant content to the placeholder, for example, textboxes and labels.

    ![](<images/fieldset-image-8.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Properties | Description |
|---|---|
| Title (Text): Mandatory   |  The Fieldset title.  <p>Examples <ul><li>_"Basic Information"_ - the title is set to Basic Information</li></ul></p> | 
| ExtendedClass (Text): Optional  | Add custom style classes to the Fieldset UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass style_ to the Fieldset UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Fieldset UI styles being applied.</li></ul></p> |
