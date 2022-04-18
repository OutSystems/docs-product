---
locale: en-us
guid: 5f57c113-47fb-4a99-b6f6-377b71ff2227
app_type: traditional web apps, mobile apps, reactive web apps
---

# HTML Injection Warning

Message
:   `Ensure the expression is protected by using EncodeHTML(), EncodeJavascript(), or SanitizeHtml() from the Sanitization extension, to avoid security flaws.`

Cause
:   The expression mentioned in the warning has a value that comes from the end user input and that is susceptible to contain malicious content.

Recommendation
:   Do one of the following:

    * Enable the `Escape Content` property of the expression.
    * Use the **EncodeHtml()** built-in function to replace all HTML reserved characters by their escaped counterpart.
    * Use the **EncodeJavascript()** built-in function to replace all JavaScript reserved characters by their escaped counterpart so they can be included in a JavaScript string.
    * Use the **SanitizeHtml()** function from the Sanitization extension module to ensure that the value entered by the end user does not contain any malicious content.
    * Use the **EncodeUrl()** built-in function to replace all URL invalid characters by their percent-encoded counterpart.
