---
summary: Learn more about how to fix Aggregates and SQL nodes not identified after converting to ODC.
tags: o11 service modules, aggregate, sql, logic flow, o11 to odc conversion
guid: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
locale: en-us
app_type: traditional web apps, reactive web apps, mobile apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?m=auto&node-id=2849-240&t=Kul2SDydEJD6RIhT-1
audience:
  - architects
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Aggregate or SQL node referenced outside its scope

In O11, the scope of aggregates and SQL nodes in a [Service](../../building-apps/reuse-and-refactor/services.md) module is different from the scope in a Reactive Web module.

When designing the logic of a Service module's action, you can access any aggregate or SQL node outside the scope where it was declared. For example, an aggregate declared in the False branch of an **If** can be accessed outside the **If** scope, even if the False branch isn't executed during runtime. Whether the False or the True branch executes, the node after the **If** has access to the aggregate.

![Screenshot of a logic flow on an O11 Service showing that an aggregate declared inside an If is available everywhere in the flow.](images/aggregate-scope-ss.png "Logic flow on an O11 Service showing that an aggregate declared inside an If is available everywhere in the flow.")

In ODC apps' logic, an aggregate or SQL node only exists in the scope where it was declared. In this example, an aggregate declared in the False branch of an **If** cannot be accessed outside that scope. Whether the False or the True branch executes, the node after the **If** doesn't have access to the aggregate.

![Screenshot of a logic flow on an ODC app showing that an aggregate declared inside an If is not available outside that scope.](images/aggregate-scope-odcs.png "Logic flow on an ODC app showing that an aggregate declared inside an If is not available outside that scope.")

Therefore, after converting to ODC an O11 Service module that uses this pattern, you'll get a TrueChange error: "Can't identify &#39;&lt;aggregate or SQL node&gt;&#39; element in expression".

## How to solve

You must solve this pattern in ODC after proceeding with the code conversion to ODC.

### Solve in ODC

After converting your app to ODC, inspect the Invalid Expression errors in TrueChange to find out where you're using aggregates or SQL nodes that cannot be identified. If you confirm your asset has those errors because it uses the pattern described on this page, adjust your logic to ensure the aggregate or SQL node runs before it is referenced. Make sure aggregates and SQL nodes are only referenced in the same scope where they're declared.

![Screenshot of a logic flow on an ODC app showing an aggregate used inside its scope.](images/aggregate-scope-fixed-odcs.png "Logic flow on an ODC app showing an aggregate used inside its scope.")
