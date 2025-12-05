---
summary: This article provides guidance on refactoring dependencies to private Structures in O11 apps to ensure compatibility with ODC.
locale: en-us
guid: a9064f2d-eb97-450c-8053-8c543087c3c0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30533
tags: service actions, data migration, code conversion, outsystems development, outsystems platform
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming a private Structure

In O11, you can set Structures as public and share them between modules.

In ODC, Structures are private by default and you can't manually set them as public. Only when you use a Structure as the data type of a Service Action parameter, ODC automatically makes that Structure available to consuming assets.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* Create a copy of the Structure in the consuming module. Use this approach when the Structure isn't used in Service Action parameters.

* Use the Structure as a parameter of a Service Action exposed by the producer and referenced in the consumer.
