---
tags: runtime-traditionalweb; 
summary: Layout Side Menu uses the space available on the side to improve navigation. 
---

# Layout Side Menu

The Layout Side Menu is a pre-existing web block for a side menu. The web block is located in **UI Flows > OutSystemsUIWeb > Layouts**, and contains various placeholders and widgets that you can customize. You can then reuse and apply the web block to any of the screens in your app.

![](<images/layoutsidemenu-1-ss.png?width=800>)

## Properties

| **Property** |  **Description** |  
|---|---|
| DeviceConfiguration (DeviceConfig): Optional  |  Configuration that changes the default values that apply when the application is viewed on a phone, tablet, or desktop. |
| AccessibilityConfiguration (AccessibilityConfiguration): Optional | Configuration that changes the default values for the options that reset tab index values and the options that add a visible outline to focused elements. |
| ExtendedClass (Text): Optional |  Add custom style classes to the Layout Side Menu web block. You define your [custom style classes](../../../../../develop/ui/look-feel/css.md) in your application using CSS. <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Layout Side Menu UI styles being applied.</li><li>_"myclass1 myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Layout Side Menu UI styles being applied.</li></ul></p> |
