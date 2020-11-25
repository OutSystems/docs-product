---
summary: How to use the translation editor to translate your app in Service Studio.
tags: support-application_development
---

# Translating with the translation editor

The **translation editor** lets you translate text and manage your translation directly from Service Studio. To open the editor go to the **Data** > right-click the **Multilingual Locales** folder > click **Edit Translations**. Translation editor also opens when you [add a new translation language](translate-your-app.md).

<div class="info" markdown="1">

These instructions are part of the technical preview for translating Reactive Web and Mobile Apps. See [Technical Preview: Multilingual apps](intro.md) for more information.  

</div>

Once you open the translation editor, you can:

* **Translate** text by entering the translation in the **Translation in (language code)** column (1).
* **Switch languages for translation** by selecting the language code in the heading of the **Translation in (language code)** column (2).
* **Set text as translatable / non-translatable** by selecting one of the options in the **Behavior** list (3). See 
* **Filter and search** the text by using the tools in the **Filter** section of the translation editor (4). With the translation window open, select an element in the screen, and then click the button with the arrow icon to show that element in the editor.
* **Navigate to a text in the module** by double-clicking a **Text** field, to see the text in the context.
* **See the translation progress**, as it shows in the **Statistics** section (5).

![Translation editor overview](images/translation-editor-overview.png?width=690)

<div class="info" markdown="1">

If a translatable text has no translation, the app shows the text in the default language of the app (**en-US**).

</div>

## Translatable and non-translatable text

The **Behavior** column in the translation editor shows what to do with the text in the translation process:

* **Translate**. Translatable and it's **exported** in the translation files.
* **Don't translate**. Non-translatable and it **isn't exported** in the translation files.
* **Not defined**. Neither translatable or non-translatable, and it **isn't exported** in the translation files.

You can also set property for several selected cells with text by using **TRANSLATE**, **DON'T TRANSLATE**, and **NOT DEFINED** buttons. Use the **Ctrl/Shift** key for multiple selection or **Ctrl+A** to select all cells in the list. 

Service Studio automatically sets as translatable the following text:  

* Screen titles
* Button labels
* Text in the screens

## Send feedback

If you experience issues with this technical preview, let us know by posting [a new question with the **technical preview** tag](https://www.outsystems.com/forums/tag/6875/technical-preview/) in Forums.