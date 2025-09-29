---
summary: This article provides guidance on refactoring dependencies to Server Actions in O11 apps to ensure compatibility with ODC.
locale: en-us
guid: bf0d4524-95c4-477b-9254-1e369a3f1f80
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-6594
helpids: 30519
tags: code conversion, server actions, service actions, dependency management, refactoring code
audience:
  - frontend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming an ODC application server action

A dependency to a server action is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies. This means that it isn't possible to consume Server actions from other apps, only from libraries.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* If the server sction includes business logic, change the strong dependency to a weak dependency by [converting the server action to a service action](../../building-apps/reuse-and-refactor/services.md). Unlike server actions, service actions don't share the same process and transaction with the consumers, so make sure you account for [distributed transactions](../../building-apps/reuse-and-refactor/services.md#dealing-with-transactionality-and-networking) while refactoring your code.

    ![Diagram illustrating the conversion of a server action to a service action to change a strong dependency to a weak dependency.](images/convert-server-to-service-action-diag.png "Convert Server Action to Service Action")

* If the server action includes business agnostic logic to implement patterns like a an integration wrapper or logic utilities (for example for XML parsing), review the O11 to ODC architecture mapping. Converting the O11 module with the server action to an O11 library module, move that O11 module to a new O11 app, then map that new O11 app to an ODC library.

    ![Diagram showing the architecture review process. Before the review, O11 modules are within ODC apps. After the review, O11 modules are moved to an O11 library mapped to an ODC library.](images/review-arch-move-to-lib-1-diag.png "Architecture Review Before and After")
