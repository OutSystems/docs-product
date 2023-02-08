---
locale: en-us
guid: 5d3d786b-ebf4-47f0-b289-a207dadd8bb0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Recursive Theme Hierarchy Error

The `Recursive Theme Hierarchy`error is issued in the following situation:

* `Your module has a circular dependency between themes`

    A typical scenario is when your module has two themes. The first theme uses the second as its Base theme, and the second uses the first as its Base theme, thus creating a circular reference in their definitions.

    Change one of the themes to stop using the other as its Base theme.
