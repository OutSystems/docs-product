---
summary: OutSystems 11 (O11) addresses the "Invalid Use of Grid Units" error by specifying widget dimensions or adjusting theme settings.
locale: en-us
guid: f62c6f07-cf7c-4ccd-b3a4-61d72b1f062a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, styling issues, ui design best practices, theme customization
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Use of Grid Units Error

The `Invalid Use Of Grid Units` error is issued in the following situation:

* `The widget dimensions must be set using 'px', 'pt' or '%'. To use grid units you must set the 'Use Grid' to 'Yes' in the theme`

    The widget has its Width, Min. Height, Margin Left, or Margin Top properties set using 'col', but it needs to be set with 'px', 'pt', or '%' instead.

    Change the property with the error to use 'px', 'pt', or '%', or change the 'Use Grid' property of the theme to 'Yes' to specify the property with 'col'.
