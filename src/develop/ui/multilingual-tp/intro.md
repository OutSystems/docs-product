---
summary: Learn how to create multilingual Reactive Web and Mobile App with OutSystems. This feature is a technical preview.
tags: support-application_development;
---

# Technical Preview - Multilingual Reactive Web and Mobile Apps

With Multilingual Reactive Web and Mobile Apps you can translate an app to other languages. Once the translations are available in the app, you can switch the language automatically or let users do it.

<div class="info" markdown="1">

When translating apps, note the following important information about language codes:

* The default language code is **en-US**.
* The current language is bound to the user session and when the user logs out, the language code automatically changes to the default language code.
* All language codes are in the [RFC 1766](https://tools.ietf.org/html/rfc1766) standard format.
* Language codes are **case sensitive**.

</div>

## Prerequisites { #prerequisites }

To translate **Reactive Web** and **Mobile Apps** in Service Studio as part of a technical preview, you need to meet the following requirements:

* Platform Server 11.10.0 or later
* LifeTime 11.6.0 or later
* Up-to-date Service Studio
* Activated [technical preview](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features) **Multilingual for Mobile and Reactive** in LifeTime

## Getting started

Here's how to get started:

* For instructions on how to translate your app directly in Service Studio, see [Translate your app](translate-your-app.md).
* If you want to extract text for sending it to a translation service, see [Translation management](translation-management.md).
* For instructions on how to translate older, Traditional Web Apps, see [this section](../multilingual/intro.md).

You can translate the following elements of your app:

* Screen titles
* Text in buttons, links, and screens
* Text literals in expressions
* Instructions in human activities
* Validation messages, widget confirmation messages, and empty state messages
* Static entities. Check [Working with Static Entities](translate-your-app.md#working-with-static-entities) for important notes.

## Translating systems components

You can translate systems components. See the forum blog post [System Components Translations](https://www.outsystems.com/forums/discussion/10760/system-components-translations/) for instructions. 

<div class="info" markdown="">

You need to define at least one locale to be able to export the text resources from a system component.

</div>

## Send feedback

If you experience issues with this technical preview, let us know by posting [a new question with the **technical preview** tag](https://www.outsystems.com/forums/tag/6875/technical-preview/) in Forums.

## Training resources

Check out the [Multi-Language in OutSystems](https://www.outsystems.com/training/courses/182/multi-language-in-outsystems/) training section for video resources and demos.
