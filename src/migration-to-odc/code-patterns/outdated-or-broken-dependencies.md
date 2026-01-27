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

Outdated or broken dependencies occur when the functionality exposed by a producer module changes without refreshing the consumer modules.

Having an outdated or broken dependency blocks the Conversion Assessment Tool to inspect the consumer module, because the new version of the producer may generate new findings.

While the Conversion Assessment Tool always flags outdated dependencies, Service Studio flags them differently based on their impact:

* **Producer updated with no signature changes:** In this case, Service Studio doesn't show outdated references.

* **Producer updated with compatible signature changes:** Service Studio shows a blue information indicator for modified signatures in **Manage Dependencies**.

* **Producer updated with incompatible signature changes:** Service Studio shows an incompatibility indicator in **Manage Dependencies**.

For additional details, see [Handle Changes in Exposed Functionality](../../building-apps/reuse-and-refactor/handle-changes.md).

## How to solve

You must solve this pattern in O11 before proceeding with the code conversion to ODC.

### Solve in O11

Follow these steps to refresh the dependencies in your consumer module:

1. [Refresh the dependencies](../../building-apps/reuse-and-refactor/handle-changes.md#refresh-dependencies) of your module in Service Studio, even if no update indicator appears.
1. Publish the consumer module.
1. Run a new assessment in the Conversion Assessment Tool to verify if there are new findings.
