---
tags: case management, dynamic case management, milestones, workflow management, outsystems
summary: Learn how to define intermediate goals using milestones in dynamic case management with OutSystems 11 (O11).
guid: 31c89686-510e-4586-ad31-d04f21c21154
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - business analysts
outsystems-tools:
  - service studio
  - case management framework
coverage-type:
  - understand
---

# Defining intermediate goals with milestones

A milestone represents an intermediate goal in the context of the resolution of a case. Milestones provide modularity by helping define phases for dynamic cases, whose workflow isn't predictable and can't be fully defined while designing your app.

Achieving a milestone usually means the case meets conditions defined by you, like completing one or more activities, or achieving another milestone.
The achievement of a milestone can then trigger other actions in the case lifecycle like starting another process or assigning an activity.

In the Case Management framework a **milestone definition** is a type of milestone and a **milestone instance** is a specific occurrence of a milestone definition in the context of a case instance.
