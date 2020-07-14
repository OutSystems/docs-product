---
tags: runtime-mobileandreactiveweb;  
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

    By default, the Section widget contains Title and Content placeholders.

1. Add your content to the placeholders. 

    In this example, we add a title to the Title placeholder as well as  text and a button to the Content placeholder. We also set the button to redirect the user to a new page when clicked.

    ![](<images/section-3-ss.png?width=800>)

1. On the **Properties** tab, you can customize the Section's look and feel by setting any of the (optional) properties. 

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** |
|---|---|
| UsePadding (Boolean): Optional  |  If set to True, padding is applied to the content area. This is the default value. If set to False, the content area has no padding.| 
| ExtendedClass (Text): Optional |  Add custom style classes to the Section UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Section UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Section UI styles being applied.</li></ul></p> |
