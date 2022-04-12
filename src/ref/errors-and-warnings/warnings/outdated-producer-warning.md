---
locale: en-us
guid: 2d0f78ae-6d89-437a-ab38-cf89125d8036
---

# Outdated Producer Warning

Message
:   `Producer '<producer>' uses outdated references. Please republish '<producer>' to prevent runtime errors`

Cause
:   Your current module (e.g.: MyModule) has one or more references to another module (e.g.: Module1) which is referencing other producers that have changed since it (Module1) was last published.

Recommendation
:   Republish Module1 to refresh its references, and retry MyModule publishing, afterwards.
