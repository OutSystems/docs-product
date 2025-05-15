---
summary:
locale: en-us
guid: a9064f2d-eb97-450c-8053-8c543087c3c0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30533
tags: service actions, data migration, code migration, outsystems development, outsystems platform
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

In ODC, Structures are private by default, and can't be explicitly shared between ODC assets. Structures can be implicitly shared between ODC assets if they're used as the Data Type of parameters of Service Actions.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* Replicate the Structure in the consumer.

* Implicitly share the Structure by using it in a Service Action exposed by the producer and referenced in the consumer.
