---
summary: Explore multilingual app translation and language switching features in OutSystems 11 (O11) using Service Studio.
tags: internationalization, localization, language support, user experience, application development
locale: en-us
guid: e664c563-cb0f-491c-bd05-8f1684d4a5a3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=249:45
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Translate your app

Translate the interface of your app to other languages to let more users use your app.

## Quick start

Here is a quick start to help you translate your app. To let the users use your app in their language, you need to:

1. [Add a new language and translate the text in the app](#adding-a-new-language-and-translating-the-text) by using the Service Studio translation editor.

1. [Create a language switcher](#creating-a-language-switcher) to let users change the language in the app.

1. If your app uses Static Entities, check [Working with Static Entities](#working-with-static-entities) for more information.

## Adding a new language and translating the text

To add a new language and translate your app, do the following in Service Studio:

1. Go to the **Data** tab and right-click on the **Multilingual Locales**. Then, select **Add Locale**. The **Select Locale** window opens.

    ![Screenshot showing how to add a new language for translation in Service Studio](images/add-new-language-translation-ss.png "Adding a New Language in Service Studio")

1. Select a locale and then click **OK** to open the **translations editor**.

    ![Screenshot of the Select Locale window in Service Studio for choosing a new language](images/select-new-language-ss.png "Selecting a New Language")

    <div class="info" markdown="1">

    Make note of the language code, since you will need it later. For example, for **Portuguese (Brazil)** the code is **pt-BR**.

    </div>

1. In the translations editor, select the **Translate** option in the behavior list to see all text that needs translation.

    ![Screenshot displaying text that needs translation in the Service Studio translations editor](images/show-translatable-text-ss.png "Translatable Text in Service Studio")

    See [Translating with the translation editor](translation-editor.md) for more information on how to use the editor.

1. Translate the text in the **Translation in (language code)** column. Click **Done** when you are finished.

    ![Screenshot of the translation editor in Service Studio with a column for entering translations](images/enter-translation-ss.png "Entering Translations in Service Studio")
    
After you finish translating the text in your app, you then need to create a language switcher to show the available translations.

<div class="info" markdown="1">

Translate the text in **all modules of your app**. This is important as an app can have multiple modules with user interface elements.

</div>

## Creating a language switcher

A language switcher lets your users change the language of the app. To create a language switcher, do the following:

1. Drag a Link widget to a screen and enter the language name in the **Text** part of the **Link**. 

    ![Screenshot showing a Link widget with a language name in Service Studio](images/link-with-language-name-ss.png "Link Widget with Language Name")

    The example shows how to use the **Link** widget to change the app language. You can create the same action with other widgets, including **Button** and **Dropdown**.

1. Select the Link widget to view its properties. In the **On Click** list, select **New Client Action**. New Client Action opens for editing.

    ![Screenshot of Service Studio showing how to create a new client action for a language switcher link](images/new-client-action-for-link-ss.png "Creating a New Client Action for a Link")

1. With the logic editor open, go to the **Logic** tab and expand the **(System)** section in **Client Actions**. Locate the **SetCurrentLocale** client action and drag it to the logic flow.

    ![Screenshot of the Logic tab in Service Studio with the SetCurrentLocale client action highlighted](images/client-action-in-logic-tab.png "SetCurrentLocale Client Action in Logic Tab")

    <div class="info" markdown="1">

    If you can't find the **SetCurrentLocale Client Action**, you need to reference it first. Press **Ctrl+Q** to open the **Manage Dependencies** window and select **(System)**. In the right pane under **Client Actions**, select **SetCurrentLocale** and click **Apply** to confirm. You can now use **SetCurrentLocale Client Action** in your app logic. 
    
    **Note**: **SetCurrentLocale** and **GetCurrentLocale** can only be persisted across client and server actions when that locale is defined in the module.

    ![Screenshot showing the SetCurrentLocale client action in the Manage Dependencies window of Service Studio](images/set-current-locale-in-manage-dependencies.png "SetCurrentLocale in Manage Dependencies")

    </div>

    <div class="warning" markdown="1">

    Keep in mind that SetCurrentLocale **Server** Action doesn't work offline. Use **SetCurrentLocale Client Action** whenever possible. 

    </div>

1. In the **SetCurrentLocale Client Action**, enter the code of the language (for example, `"pt-BR"`) in the **Locale** property.

    **Note**: For a locale to persist across client and server requests, you must define it at module level. 

    ![Screenshot of the SetCurrentLocale client action in Service Studio with the Locale property field highlighted](images/locale-in-client-action.png "Locale Property in SetCurrentLocale Client Action")

    <div class="info" markdown="1">

    If you have translations from **Static Entities**, add **Refresh Data** after **SetCurrentLocale**. For more information see [Working with Static Entities](#working-with-static-entities).

    </div>

1. Publish the app and select your link to change the language of the app.

## Editing existing translations

Use the [translation editor](translation-editor.md) to edit existing translations. You can also [export and import text for translation](translation-management.md). 

## Getting the identifier of the current language

You can get information about the current language with the [GetCurrentLocale built-in function](<../../../ref/lang/auto/builtinfunction-environment.md#GetCurrentLocale>).

![Screenshot showing the GetCurrentLocale function in Service Studio](images/get-current-locale-language-ss.png "GetCurrentLocale Function in Service Studio")

## Working with Static Entities

<div class="info" markdown="1">

Text Identifiers in Static Entities cannot be translated.

</div>

Follow these steps to translate the text in Static Entities and show the translation in the app.

1. In the [translation editor](translation-editor.md), search for the text you want to translate and set **Behavior** to **Translate**.

    ![Screenshot of the translation editor in Service Studio with a search for Static Entity text](images/static-entity-search-ss.png "Static Entity Search in Translation Editor")

1. While still in the translation editor, enter the translation in the **Translation in (language code)** cell and click **Done**.

    ![Screenshot of the translation editor in Service Studio showing the translation process for a Static Entity](images/static-entity-translate-ss.png "Translating Static Entity in Translation Editor")
    
    <div class="info" markdown="1">

    Translations for static entity records are defined in the same module as the static entity 
    records. The static entity records and the translations can then be referenced in a UI module.
    
    </div>

1. In the logic, to switch the locale, add **Refresh Data** just after the **SetCurrentLocale** action and select the Static Entity.

    ![Screenshot showing the Refresh Data action for a Static Entity in Service Studio](images/static-entity-refresh-ss.png "Refreshing Static Entity Data")

## Switching back to the default language

To let users switch back to the default UI language, [create a language switcher](#creating-a-language-switcher) that sets the locale code to **en-US**.
