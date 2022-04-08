---
locale: en-us
guid: 7b4eaa43-6615-4829-8e22-b7df71e4f887
---

# Invalid Username or Password Error

The `Invalid (<property name>)` error is issued in the following situation:

* `(<property name>) cannot have more than 128 characters`

    `<property name>` is either the Username or the Password property in the Basic Authentication group of the REST API properties. These cannot be longer than 128 characters.

    Change the username or password or consider using other type of authentication.
