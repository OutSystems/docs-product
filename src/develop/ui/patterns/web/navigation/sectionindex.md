---
tags: runtime-traditionalweb; 
summary: Section Index organizes the content of a screen, enabling quick navigation within the page.
---

# Section Index

You can use the Section Index UI Pattern to organize the content of a screen, enabling quick navigation within the page.

**How to use the Section Index UI Pattern**

**Prerequisite**: Your application screen contains sections. 

1. In Service Studio, from the Toolbox, search for and drag the Section widget into the Main Content area of your application's screen. Add as many sections as you require.
        
    ![](<images/sectionindex-image-8.png>)
   
1. From the Toolbox, drag the Section Index widget into the Main Content area of your application's screen.

    ![](<images/sectionindex-image-7.png>)

    A link is automatically created to every section you have on the screen. The name of the link is based on the text you entered in the **Title** placeholder of each section. In the following example, the links are set to the In-Ear Audio Black, In-Ear Audio Sport Grey etc., sections that we added earlier.

    ![](<images/sectionindex-image-2.png>)
   
After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| **Property** |  **Description** | 
|---|---|
| IsSmooth (Boolean): Optional  |  If True, the navigation to the destination is animated. If False, the navigation is instant. this is the default. |
| IsFixed (Text): Optional  |  If True, the Section Index Pattern is always in the same position on the screen. This is the default. If False, the Section Index Pattern scrolls with the page content. |
| TopPosition (Integer): Optional  |  Distance in pixels from the top of the page to the first item in the section index.  |
| ExtendedClass (Text): Optional | Add custom style classes to the Section Index UI Pattern. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Section Index UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Section Index UI styles being applied.</li></ul></p> |
  


## Additional notes

Remember to use the **Title** placeholder in the Section Index pattern as this defines the text for each SectionIndex link. 

## Device compatibility

In Internet Explorer, `position: fixed` is used instead of `position sticky` as the latter is unsupported.

## Compatibility with other patterns

This UI pattern only works with the Section Pattern in the same screen.