---
summary: Learn how to create multilingual Reactive Web and Mobile App with OutSystems.
tags: support-application_development;
locale: en-us
guid: d92eca43-e46e-4db0-8445-4dfb51e0b73d
---

# Multilingual Reactive Web and Mobile Apps

With Multilingual Reactive Web and Mobile Apps you can translate an app to other languages. Once the translations are available in the app, you can switch the language automatically or let users do it.

<div class="info" markdown="1">

Available in Platform Server 11.12.0 or later and up-to-date Service Studio.

</div>

When translating apps, note the following important information about language codes:

* The default language code is **en-US**.
* The current language is bound to the user session and when the user logs out, the language code automatically changes to the default language code.
* All language codes are in the [RFC 1766](https://tools.ietf.org/html/rfc1766) standard format.
* Language codes are **case sensitive**.

## Getting started

Here's how to get started:

* For instructions on how to translate your app directly in Service Studio, see [Translate your app](translate-your-app.md).
* If you want to extract text for sending it to a translation service, see [Translation management](translation-management.md).

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

## Training resources

Check out the [Multi-Language in OutSystems](https://www.outsystems.com/training/courses/182/multi-language-in-outsystems/) training section for video resources and demos.
