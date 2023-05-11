---
locale: en-us
guid: c8621cd0-b3e5-4521-b4c4-c461639c4f37
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Unexpected Error Handler Warning

Message
:   `'Abort Transaction' should be set to 'Yes' for 'AllException' error handler at screen flow level`

Cause
:   You have an Error Handler in a Screen Flow to catch general exceptions and the Abort Transaction property is set to 'No'.

Recommendation
:   You should change the Abort Transaction property to 'Yes' because, since the Error Handler is catching all exceptions, the current database transactions should be aborted to avoid committing  inconsistent data.
