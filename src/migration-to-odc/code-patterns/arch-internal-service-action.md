---
guid: 16151f20-2b8d-448b-8b51-ef3acc0fa311
locale: en-us
summary: Learn how to solve the findings for the conversion code pattern "Asset consuming its own service action".
figma:
coverage-type:
  - unblock
topic:
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - full stack developers
  - architects
outsystems-tools:
  - odc studio
helpids: 30670
tags: service actions, server actions, odc, code refactoring, transaction management
---
# Asset consuming its own service action

In ODC, an asset can't consume a service action defined in that same asset.

While service actions are essential for communication between different assets, using one for an internal call is an architectural anti-pattern that harms app performance and forces developers to write complex compensating logic to manage data rollbacks across separate transactions.

This pattern occurs when O11 modules with a service action dependency between them are mapped into a single ODC asset. This is an invalid self-referencing call in ODC.

## How to solve

This pattern can be solved in O11 or in ODC. The goal in both cases is to adapt the logic to replace the internal Service action reference with a Server action.

<div class="info" markdown="1">

**Note on transactions:** When you convert a Service action to a Server action, you move from a separate database transaction to a unified one. Ensure this change doesn't negatively impact any logic that relied on the previous [transactional separation](../../building-apps/reuse-and-refactor/services.md#dealing-with-transactionality-and-networking).

</div>

### Solve in ODC

After code conversion, ODC Studio reports a TrueChange error because an asset can't call its own Service Action. Solve this by doing the following:

1. Convert the Service action to a Server action:

   1. In the **Logic** tab, cut the Service action causing the error.

   1. Paste it into the **Server Actions** folder.

1. Then, update the logic that was causing the error by replacing the reference to the original Service action with the new Server action.

### Solve in O11

Solve this pattern by doing the following:

1. In the producer module convert the Service action to a public Server action:

   1. In the **Logic** tab, cut the Service action from its folder.

   1. Paste it into the **Server Actions** folder.

1. Set the new Server's action **Public** property to **Yes**.

1. Publish the module.

1. In the consuming module, replace the reference to the original Service action with the new Server action.
