---
summary: OutSystems 11 (O11) displays an "Invalid Page Name Error" when a page name contains characters other than letters, digits, dash, tilde, or slash.
tags: seo-friendly urls, error handling, web development best practices, application configuration, user experience enhancement
locale: en-us
guid: 6237e558-882b-40a4-9276-64dff7b6b16d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Page Name

Service Studio shows **Invalid Page Name Error**:

* Page Name in [screen name] screen contains invalid characters. Please use only digits, letters, or any of these special characters: `-`, `~`, `/`.

Some characters in the URLs have special uses and you can't use those characters in the **Page Name** property. To fix the error, remove all characters different from letters, digits, dash (`-`), tilde (`~`), or forward slash (`/`).

<div class="info" markdown="1">

This error is part of [SEO-friendly URLs for Reactive Web Apps](../../../building-apps/seo/intro.md).

</div>
