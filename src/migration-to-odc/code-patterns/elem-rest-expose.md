---
summary: 
locale: en-us
guid: 1a85194d-6f42-44b3-9176-c5d6494250de
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30541
---
# Library exposing a REST API

In ODC, Libraries can't expose REST.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

Solve this pattern by reviewing the O11 to ODC architecture mapping and moving the O11 Module with the REST Expose to a new O11 App, then map that O11 App to an ODC App instead of to an ODC Library.
