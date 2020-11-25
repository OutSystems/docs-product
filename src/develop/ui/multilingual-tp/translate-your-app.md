---
summary: Translate your app directly from Service Studio by translating the module text and then creating a language switcher.
tags: support-application_development
---

# Translate your app

You can add other languages to your app and translate the text in the app, to support users in languages other than the default.

<div class="info" markdown="1">

These instructions are part of the technical preview for translating Reactive Web and Mobile Apps. See [Technical Preview: Multilingual apps](intro.md) for more information.  

</div>

## Quick start

Service Studio has tools to translate your app. To let the users use your app in their language, you need to:

1. [Add a new language](#add-new-language) and then translate the text in the module by using the Service Studio translation editor. An app may have more than one module with user interface elements, and you need to translate all such modules.
2. [Create a language switcher](#add-language-switcher) to let users change the language in the app.

## Add a new language and translate the text { #add-new-language }

<div class="info" markdown="1">

These instructions are part of the technical preview for translating Reactive Web and Mobile Apps. See [Technical Preview: Multilingual apps](intro.md) for more information.  

</div>

To add a new language and translate your app, do the following in Service Studio:

1. Go to the **Data** tab and right-click on the **Multilingual Locales**. Then, select **Add Locale**. The **Select Locale** window opens.

    ![Add new language for translation](images/add-new-language-translation-ss.png?width=550)

2. Select a locale and then select **OK**. The **translations editor** opens. See [Translating with the translation editor](translation-editor.md) for more information on how to use the editor.

    ![Select new language](images/select-new-language-ss.png?width=400)

    <div class="info" markdown="1">

    Note the language code, as you need it later. For example, for **Portuguese (Portugal)** the code is **pt-PT**.

    </div>

3. In the translations editor, select **Show Translate** option in the filter list to see all text that needs translation.

    ![Shows text that needs translation](images/show-translatable-text-ss.png?width=650)

4. Translate the text in the **Translation in (language code)** column. Click on **Done** when you finish.

    ![Translation in the translation editor](images/enter-translation-ss.png?width=650)

When you're happy with the translation, move on to creating a language switcher.

## Create a language switcher { #add-language-switcher }

<div class="info" markdown="1">

These instructions are part of the technical preview for translating Reactive Web and Mobile Apps. See [Technical Preview: Multilingual apps](intro.md) for more information.  

</div>

A language switcher lets your users change the UI language. To create a link to switch language in the app, do the following:

1. Drag a Link widget to a screen. Then, enter the language name in the **Text** part of the **Link**. 

    ![Link with a language name](images/link-with-language-name-ss.png?width=750)

2. Select the Link widget and in the properties, in the **On Click** list, select **New Client Action**. New Client Action opens for editing.

    ![New client action from the list](images/new-client-action-for-link-ss.png?width=750)

3. With the logic editor opened, go to the **Logic** tab and expand the **(System)** section. Locate the **SetCurrentLocale Client Action** and drag it to the logic flow.

    ![SetCurrentLocale in the Logic tab](images/client-action-in-logic-tab.png?width=550)

    <div class="info" markdown="1">

    If you can't find the **SetCurrentLocale Client Action**, you need to reference it first. Press **Ctrl+Q** to open the **Manage Dependencies** window. Select **(System)**; then, in the right pane under **Client Actions**, select **SetCurrentLocale**. Click on the **Apply** to confirm. You can now use **SetCurrentLocale Client Action** in your app logic.

    ![SetCurrentLocale Client Action in Manage Dependencies](images/set-current-locale-in-manage-dependencies.png?width=550)

    </div>

    <div class="warning" markdown="1">

    Be careful with SetCurrentLocale **Server** Action in the Reactive Web and Mobile Apps UI logic, as this **server action** requires connection to the server and doesn't work offline. Use **SetCurrentLocale Client Action** whenever possible.

    </div>

4. In the **SetCurrentLocale Client Action** you just added, in the **Locale** property, enter the code of the language. For example, `"pt-PT"`.

    ![SetCurrentLocale and the Locale property](images/locale-in-client-action.png?width=550)

    <div class="info" markdown="1">

    To let users switch back to the default UI language, create a language switcher with SetCurrentLocale Client Action set to the default locale code (**en-US**).

    </div>

5. Publish the app and select on the link you just created. The language in the app switches after you select the links, but you can use other UI elements to create the switcher, for example a combo box or buttons.

## Edit existing translation

Use the [translation editor](translation-editor.md) to edit existing translations. In Service Studio, go to the **Data** tab, right-click on the **Multilingual Locales**, then select **Edit Translations**.

You can also [export and import text for translation](translation-management.md). 

## Get the identifier of the current language

You can get information about the current language with the [GetCurrentLocale built-in function](<../../../ref/lang/auto/builtinfunction.Environment.final.md#GetCurrentLocale>).

![GetCurrentLocale function in the expression editor](images/get-current-locale-language-ss.png?width=750)

## Send feedback

If you experience issues with this technical preview, let us know by posting [a new question with the **technical preview** tag](https://www.outsystems.com/forums/tag/6875/technical-preview/) in Forums.