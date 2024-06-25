---
summary: 
locale: en-us
guid: 5c4356eb-5d71-4bd8-999d-48dfafb743ce
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30532
---
# Library consuming a Service Action

In ODC, Libraries can't consume Service Actions.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* If the ODC producer is also a Library, convert the Service Action to a Server Action.

* If the ODC producer is an App, review the O11 to ODC architecture mapping, to remove the dependency from the Library to the Service Action.
