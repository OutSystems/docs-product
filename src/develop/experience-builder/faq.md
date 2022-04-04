---
tags: Experience Builder; Mobile.
summary: Check the answers to the frequently asked questions about Experience Builder.
---

# Experience Builder FAQ

## Can I add a flow more than once in the same app?

**No**.
In Experience Builder, you can only add one instance of a flow to each app.

Note that **Empty Screens** aren’t considered flows, and you can add them multiple times. Furthermore each Empty Screen can have a different name and content. All the Empty Screens of your app are placed in a flow called “Others”.

## Do the flow/screen names in Experience Builder match the flow/screen you see when you open the generated app in Service Studio?

**Yes**.<br/>
This also means that the naming conventions and restrictions that exist in Service Studio also apply to Experience Builder.

Note that the **Empty Screens** are a particular case - since they don’t belong to a flow, they are placed in a flow called **Others**.

## Why does Experience Builder ask for such high-resolution images for both app icon and splash screen?

Experience Builder asks for [native app icons](../../deliver-mobile/customize-mobile-app/modify-the-app-icon.md) images with 1024x1024 and [splash screen images](../../deliver-mobile/customize-mobile-app/use-custom-splash-screens.md) with 2048x2048 to ensure the creation of all the image sizes needed to publish your mobile app in Google and Apple app stores.

Experience Builder packages all these images in a zip file with the correct folders structure, and adds all the extensibility configurations required to use all these assets once you publish your app.
