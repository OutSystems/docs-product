---
summary: Provides actions for validating and securely storing passwords in the database, compliant with established cryptographic practices.
tags: 
---

The PlatformPasswordUtils API provides actions for validating and securely storing passwords in the database, compliant with established cryptographic practices. This is accomplished through actions that enable you to:

* generate a salted password and hash it using the MD5 hash algorithm (deprecated)
* generate a salted password and hash it using the SHA512 hash algorithm
* validate a password against its salted hash
