---
tags: runtime-traditionalweb; 
summary: Section separates content into groups, easing visual organization.
---

# Section

You can use the Section UI Pattern to organize on-screen content into different sections. This pattern can also be used with the Section Index UI Pattern to create anchors for each section.

![](<images/section-5-ss.png>)

**How to use the Section UI Pattern**

1. In Service Studio, in the Toolbox, search for `Section`.
  
    The Section widget is displayed.

    ![](<images/section-1-ss.png>) 

1. To From the Toolbox, drag the Section widget into the Main Content area of your application's screen.

    ![](<images/section-2-ss.png?width=800>)

    By default, the Section widget contains Title, Actions, and Content placeholders.

1. Add your content to the placeholders. In this example, we add a title to the Title placeholder, text to the Content placeholder, and a button to the Actions placeholder.

    ![](<images/section-3-ss.png?width=800>)

1. Add the desired action to the content you have added to the Actions placeholder. In this example, the button we added redirects the user to a new page.

    ![](<images/section-6-ss.png?width=800>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| ExtendedClass (Text): Optional |  Add custom style classes to the Section UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Section UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Section UI styles being applied.</li></ul></p> |
