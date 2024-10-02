---
summary: 
locale: en-us
guid: bf0d4524-95c4-477b-9254-1e369a3f1f80
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2350-6594
helpids: 30519
---
# Asset consuming an ODC application Server Action

A dependency to a Server Action is a strong dependency, and in ODC, dependencies to other Apps must be weak dependencies.
This means that it isn't possible to consume Server Actions from other Apps, only from Libraries.

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* If the Server Action includes business logic, change the strong dependency to a weak dependency by [converting the server action to a service action](../../building-apps/reuse-and-refactor/services.md). Unlike Server Actions, Service Actions don't share the same process and transaction with the consumers, so make sure you account for [distributed transactions](../../building-apps/reuse-and-refactor/services.md#dealing-with-transactionality-and-networking) while refactoring your code.

    ![Diagram illustrating the conversion of a server action to a service action to change a strong dependency to a weak dependency.](images/convert-server-to-service-action-diag.png "Convert Server Action to Service Action")

* If the Server Action includes business agnostic logic to implement patterns like a an integration wrapper or logic utilities (for example for XML parsing), review the O11 to ODC architecture mapping. Converting the O11 Module with the Theme to an O11 Library module, move that O11 Module to a new O11 App, then map that new O11 app to an ODC Library.

    ![Diagram showing the architecture review process. Before the review, O11 Modules are within ODC Apps. After the review, O11 Modules are moved to an O11 Library within an ODC Library.](images/review-arch-move-to-lib-1-diag.png "Architecture Review Before and After")
