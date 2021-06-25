---
summary: 
---

# Right-to-Left (RTL)

Most applications are designed and created with all content displaying from left to right (LTR). However, to accommodate languages from the Middle East, for example, Arabic, the written content and layout must be swapped so that it displays from right to left. All patterns on the OutSystems UI framework support RTL by default. 

## Using the Multilingual feature

To translate your application to, for example, Arabic, you just need to set the locale **"ar"** and the RTL is applied by default. 

When you use the Multilingual feature, the RTL is automatically applied based on the language applied to the HTML and the platform adds the CSS class **"is-rtl"** to the body, changing the direction of this content:

`.is-rtl {
   direction: rtl;
}`

The multilingual feature is available from [Platform Server version 11.11.1 onwards](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server). To enable the Multilingual feature in your application, follow the [Multilingual Reactive Web and Mobile Apps](../multilingual-tp/intro.md) guidelines.

## Applying RTL manually

You can manually apply RTL to your application by adding a class directly to the body element. To add the class injection, you must create an action with a JS node with the following JS snippet:

## Changing the application’s content based on RTL

OutSystems UI provides an **IsRTL** action that checks if RTL is applied or not (boolean value). This action also works like a function. You can find it in the **Utilities** folder: 

You can use it in the following ways:

* To set values on input parameters:

* To control the Container’s visibility:

* To set conditions (If widget):

* To apply logic inside client actions on If conditions:

## Exceptions

On the OutSystems UI Framework, there are exceptions (RangeSlider, RangeSliderInterval, DropdownSearch, and DropdownTags) that, when used, must apply RTL using the AdvancedFormat parameter. The following is the library option that you must add when applying the RTL:

**Note:** By default, the DatePicker pattern already has full RTL support.

## Utilities

The following are some useful utilities that you can use during your app development to handle your RTL based content.

### Selectors and code cnippets
