---
summary: 
locale: en-us
guid: 4ab916bc-6375-4cd6-9e46-804540e72a33
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30522
---
# Library consuming an ODC application Entity

In ODC, Libraries are stateless by design, which means they can't persist data. Not storing data ensures libraries act solely as providers of functionality and logic, leaving the data management and storage to the apps.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

To solve this pattern, review the O11 to ODC architecture mapping and move the O11 Module with the Entity to a new O11 App, then map that O11 App to an ODC App instead of to an ODC Library.
