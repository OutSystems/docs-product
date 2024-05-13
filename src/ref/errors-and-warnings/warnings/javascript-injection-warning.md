---
summary: OutSystems 11 (O11) advises using EncodeJavaScript() or VerifyJavascriptLiteral() to prevent JavaScript injection vulnerabilities from user inputs.
locale: en-us
guid: 8afc6360-df8d-451d-81cd-fd499fa5bd15
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# JavaScript Injection Warning

Message
:   `Ensure the expression is protected by using EncodeJavaScript(), or VerifyJavascriptLiteral() from the Sanitization extension, to avoid security flaws.`

Cause
:   The expression mentioned in the warning has a value that comes from the end user input and that is susceptible to contain malicious content.

Recommendation
:   Use the **EncodeJavascript()** built-in function to replace all JavaScript reserved characters by their escaped counterpart.
