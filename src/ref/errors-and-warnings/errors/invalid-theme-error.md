---
locale: en-us
guid: 3b85b1ca-c60b-4109-8b41-64d006328f17
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid Theme Error

The `Invalid Theme Error` is issued in the following situation:

* `The web flow cannot be the 'Error Handling Flow' of the theme because it has no error handlers`

    The Error Handling Flow property of the theme has a web flow that does not implement error handling.

    Change the web flow to have error handlers, or change the theme to user a web flow that already implements them.
