---
summary: This article explains how to resolve outdated or broken dependencies in O11 before proceeding with the conversion to ODC.
locale: en-us
guid: 567da663-34d7-4078-8975-0064fcf42019
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
tags: dependency management, code conversion, o11 to odc, application lifecycle
audience:
  - full stack developers
  - architects
outsystems-tools:
  - app conversion kit
  - service studio
figma:
helpids: 30552
---

# Asset with outdated or broken dependencies

Outdated or broken dependencies occur when the producer model is updated without refreshing the consumer model. Having an issue with a reference blocks the Conversion Assessment Tool to inspect the module.

## How to solve

You must solve this pattern in O11 before proceeding with the code conversion to ODC.

### Solve in O11

To refresh the dependencies in your consumer model, refer to [Handle changes in exposed functionality](../../building-apps/reuse-and-refactor/handle-changes.md#refresh-dependencies).
