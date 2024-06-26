---
summary: 
locale: en-us
guid: 56c2610d-3b0b-4d57-bed6-a76552c9269b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30530
---
# Library consuming a Screen in a web application

In ODC, Libraries can't include Screens, nor consume Screens from other Assets.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping by moving the O11 Module with the Screen to a new O11 App, then map that O11 App to an ODC App instead of to an ODC Library.
