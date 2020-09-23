---
tags: runtime-mobileandreactiveweb;  
summary: The Bottom Bar Item provides access to a bottom navigation drawer
---

# Bottom Bar Item 

You can use the Bottom Bar Item UI Pattern to provide access to a bottom navigation drawer and up to four actions, including the floating action button. Main pieces of core functionality are made available with one tap while allowing rapid switching between features.

![](<images/bottombaritem-1-ss.png>)

**How to use the Bottom Bar Item UI Pattern**

1. In Service Studio, in the Toolbox, search for `Bottom Bar Item`.
  
    The Bottom Bar Item widget is displayed.

    ![](<images/bottombaritem-3-ss.png>)

1. From the Toolbox, drag the Bottom Bar Item  widget into the Bottom placeholder area of your application's screen.

    ![](<images/bottombaritem-2-ss.png>)

    By default, the Bottom Bar Item contains Icon and Text placeholders. You can add as many Bottom Bar Items as required. 
    
    In this example, we add another three more Bottom Bar Items.

    ![](<images/bottombaritem-4-ss.png>)
      
1. For each of the Bottom Bar Items, add the relevant content. 
    
    In this example we add linked icons and linked text to each of placeholders.

    ![](<images/bottombaritem-5-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

### Bottom Bar Item

| Property | Description |
|---|---|
| ExtendedClass (Text): Optional | Add custom style classes to the Bottom Bar Item UI Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Bottom Bar Item UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Bottom Bar Item UI styles being applied.</li></ul></p> |