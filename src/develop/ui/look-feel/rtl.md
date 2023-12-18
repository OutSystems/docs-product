---
summary: Creating apps that display content right-to-left (RTL).
tags: 
locale: en-us
guid: f7a12f2e-55b0-4a1a-8a50-a7b2e7fff65e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=1043%3A13342&mode=design&t=VUTD7oZE9xvPWlG0-1
---

# Right-to-Left

Most applications are designed and created with all content displaying from left to right (LTR). However, to accommodate languages from the Middle East, for example, Arabic, the written content and layout must be swapped so that it displays from right to left (RTL). All patterns on the OutSystems UI framework support RTL by default. 

## Using the Multilingual feature

To translate your application to, for example, Arabic, you just need to set the locale **"ar"** and the RTL is applied by default. 

When you use the Multilingual feature, the RTL is automatically applied based on the language applied to the HTML and the platform adds the CSS class **"is-rtl"** to the body, changing the direction of this content.

```
.is-rtl {
   direction: rtl;
}
```

![Screenshot showing how to enable multilingual RTL support in an application](images/rtl-multilingual.png "Multilingual RTL Support")

Here's the final result:

![Final result of an application interface displaying content in both Arabic and English with RTL applied](images/rtl-arabic-english-applied-4.png "Final Result of RTL Application")

The multilingual feature is available from [Platform Server version 11.11.1 onwards](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server). To enable the Multilingual feature in your application, follow the [Multilingual Reactive Web and Mobile Apps](../multilingual-tp/intro.md) guidelines. For more information about RTL languages, see [Checklist: Right-To-Left Languages (RTL)](https://lingohub.com/academy/best-practices/rtl-language-list).

**Note:** OutSystems doesn’t support Aramaic, Khowar, Hausa, or Kashmiri.

## Applying RTL manually

<div class="warning" markdown="1">

For environments that have a Platform server lower than **version 11.11.1**, you can apply the RTL manually by adding a class directly to the body element. 

</div>

To add the class injection, you must create an action with a JS node with the following JS snippet:

```
document.body.classList.add('is-rtl');
```

![Code snippet demonstrating how to manually apply RTL to an application](images/rtl-applyrtl-ss.png "Manual RTL Application")

Here's the final result:

![Final result of an application interface displaying content in both Arabic and English with RTL applied](images/rtl-arabic-english-applied-4.png "Final Result of RTL Application")

## Changing the application’s content based on RTL

OutSystems UI provides an **IsRTL** action that checks if RTL is applied or not (boolean value). This action also works like a function. You can find it in the **Utilities** folder. 

|![Image of the IsRTL action located in the Utilities folder of OutSystems UI](images/rtl-isrtl-ss.png "IsRTL Action in Utilities")

You can use it in the following ways:

* To set values on input parameters

![Example of using advanced format settings in an application with RTL support](images/rtl-advancedformat-ss.png "Advanced Format with RTL")

* To control the Container’s visibility

![Illustration of controlling container visibility based on RTL settings](images/rtl-container-ss.png "RTL Container Visibility")

* To set conditions (If widget)

![Screenshot showing how to set conditions for RTL in an application interface](images/rtl-condition-ss.png "RTL Condition Settings")

* To apply logic inside client actions on If conditions

![Example of applying logic in client actions for RTL conditions](images/rtl-logic-ss.png "RTL Logic Application")

## Utilities

The following are some useful utilities that you can use during your app development to handle your RTL based content.

### Selectors and code snippets

Selector to get the **is-rtl** class:
```
document.querySelector('.is-rtl')
```

Selector to check if the **is-rtl** class is applied:
```
document.body.classList.contains('is-rtl')
```

Selector to get the HTML lang:
```
document.documentElement.lang
```

Use one of the following JS Snippets to toggle **is-rtl** class on the body:

```
var element = document.body;
if(element.classList.contains('is-rtl')) {
  element.classList.remove('is-rtl');
} else {
  element.classList.add('is-rtl');
}
```

**or**

```
var element = document.body;
element.classList.contains('is-rtl') ? element.classList.remove('is-rtl') : element.classList.add('is-rtl');
```

### Adding RTL class to the layout element

You can add the RTL class to the **layout** element instead of the **body** element. The RTL behavior on OutSystems UI patterns is the same.

You can add the class using a JS Node:

```
var element = document.querySelector('.layout');
element.classList.add('is-rtl')
```

You can also apply it directly to the layout block using the **ExtendedClass** parameter:

![Demonstration of adding an RTL class to the layout element using the ExtendedClass parameter](images/rtl-extendedclass-ss.png "Adding RTL Class to Layout Element")
