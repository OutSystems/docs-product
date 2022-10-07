---
summary: Translate your app directly from Service Studio by translating the module text and then creating a language switcher.
tags: support-application_development
locale: en-us
guid: e664c563-cb0f-491c-bd05-8f1684d4a5a3
app_type: traditional web apps, mobile apps, reactive web apps
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

    ![Add new language for translation](images/add-new-language-translation-ss.png)

2. Select a locale and then click **OK** to open the **translations editor**.

    ![Select new language](images/select-new-language-ss.png)

    <div class="info" markdown="1">

    Make note of the language code, since you will need it later. For example, for **Portuguese (Brazil)** the code is **pt-BR**.

    </div>

3. In the translations editor, select the **Translate** option in the behavior list to see all text that needs translation.

    ![Shows text that needs translation](images/show-translatable-text-ss.png)

    See [Translating with the translation editor](translation-editor.md) for more information on how to use the editor.

4. Translate the text in the **Translation in (language code)** column. Click **Done** when you are finished.

    ![Translation in the translation editor](images/enter-translation-ss.png)
    
After you finish translating the text in your app, you then need to create a language switcher to show the available translations.

<div class="info" markdown="1">

Translate the text in **all modules of your app**. This is important as an app can have multiple modules with user interface elements.

</div>

## Creating a language switcher

A language switcher lets your users change the language of the app. To create a language switcher, do the following:

1. Drag a Link widget to a screen and enter the language name in the **Text** part of the **Link**. 

    ![Link with a language name](images/link-with-language-name-ss.png)

    The example shows how to use the Link widget to change the app language. You can create the same action with other widgets, including Button and Dropdown.

2. Select the Link widget to view its properties. In the **On Click** list, select **New Client Action**. New Client Action opens for editing.

    ![New client action from the list](images/new-client-action-for-link-ss.png)

3. With the logic editor open, go to the **Logic** tab and expand the **(System)** section in **Client Actions**. Locate the **SetCurrentLocale** client action and drag it to the logic flow.

    ![SetCurrentLocale in the Logic tab](images/client-action-in-logic-tab.png)

    <div class="info" markdown="1">

    If you can't find the **SetCurrentLocale Client Action**, you need to reference it first. Press **Ctrl+Q** to open the **Manage Dependencies** window and select **(System)**. In the right pane under **Client Actions**, select **SetCurrentLocale** and click **Apply** to confirm. You can now use **SetCurrentLocale Client Action** in your app logic.

    ![SetCurrentLocale Client Action in Manage Dependencies](images/set-current-locale-in-manage-dependencies.png)

    </div>

    <div class="warning" markdown="1">

    Keep in mind that SetCurrentLocale **Server** Action doesn't work offline. Use **SetCurrentLocale Client Action** whenever possible.

    </div>

4. In the **SetCurrentLocale Client Action**, enter the code of the language (for example, `"pt-BR"`) in the **Locale** property.

    ![SetCurrentLocale and the Locale property](images/locale-in-client-action.png)

    <div class="info" markdown="1">

    If you have translations from **Static Entities**, add **Refresh Data** after **SetCurrentLocale**. For more information see [Working with Static Entities](#working-with-static-entities).

    </div>

5. Publish the app and select your link to change the language of the app.

## Editing existing translations

Use the [translation editor](translation-editor.md) to edit existing translations. You can also [export and import text for translation](translation-management.md). 

## Getting the identifier of the current language

You can get information about the current language with the [GetCurrentLocale built-in function](<../../../ref/lang/auto/builtinfunction.Environment.final.md#GetCurrentLocale>).

![GetCurrentLocale function in the expression editor](images/get-current-locale-language-ss.png)

## Working with Static Entities

Follow these steps to translate the text in Static Entities and show the translation in the app. 

1. In the [translation editor](translation-editor.md), search for the text you want to translate and set **Behavior** to **Translate**.

    ![Translation editor](images/static-entity-search-ss.png)

2. While still in the translation editor, enter the translation in the **Translation in (language code)** cell and click **Done**.

    ![Translation editor](images/static-entity-translate-ss.png)

3. In the logic, to switch the locale, add **Refresh Data** just after the **SetCurrentLocale** action and select the Static Entity.

    ![Refresh of Static Entity](images/static-entity-refresh-ss.png)

## Switching back to the default language

To let users switch back to the default UI language, [create a language switcher](#creating-a-language-switcher) that sets the locale code to **en-US**.
