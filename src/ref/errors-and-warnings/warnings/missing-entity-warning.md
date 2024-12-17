---
summary: Explore error handling for missing entities in OutSystems 11 (O11) when entities are not found on the server.
locale: en-us
guid: 714e8e95-4ada-4a81-9929-e392e5ae55dd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, entity management, outsystems platform, server configuration, deployment issues
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - unblock
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
