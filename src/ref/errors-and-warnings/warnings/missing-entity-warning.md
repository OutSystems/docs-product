---
locale: en-us
guid: 714e8e95-4ada-4a81-9929-e392e5ae55dd
---

# Missing Entity Warning

Message
:   `Foreign Entity <entity> was not found in Platform Server.`

Cause
:   You are using a Foreign Entity that does not exist in the server you are connected to. This situation occurs, for example, when you are hosting your module in a production server and the entity does not exist yet.

Recommendation
:   Check whether the extension that exposes `<entity>` is published in the Platform Server being used.

---

Message
:   `Referenced Entity <entity> was not found in Platform Server.`

Cause
:   You are using an Entity Reference that does not exist in the server you are connected to. The entity may either have been deleted from the Producer or if, for example, you are hosting it in a production server, the entity may not exist yet.

Recommendation
:   Check whether the Producer module that exposes `<entity>` is published in the Platform Server being used.
