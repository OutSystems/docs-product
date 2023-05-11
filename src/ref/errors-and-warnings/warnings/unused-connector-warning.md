---
locale: en-us
guid: 42bf68d5-449b-479f-8009-d02639218f6b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Unused Connector Warning

Message
:   `Connector from <screen> to <screen> in never used in <flow>`

Cause
:   You have a connector between two screens that has not been instantiated.

Recommendation
:   Open the first screen and add a Link or a Button to connect to the second screen. This instantiates the connector defined in the web flow.  
