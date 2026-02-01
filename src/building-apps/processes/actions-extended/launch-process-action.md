---
summary: Learn how to use the Launch Process Action in OutSystems 11 (O11) to execute processes asynchronously and manage input and output parameters.
locale: en-us
guid: b710c30e-e103-430c-8646-2488f414a422
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: asynchronous processing, process automation, workflow management, process execution, application development
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - remember
topic:
  - trigger-processes
  - event-driven-processes
---

# Launch Process Action

Use the **Launch&lt;Process Name&gt;** [process extended action](intro.md) in an action flow to launch the execution of a **Process**. This process is **executed asynchronously**, that is, it is launched and executed independently from the action flow execution, which immediately steps to the next element in the flow.

<div class="warning" markdown="1">

**Important!** When using **Launch&lt;Process Name&gt;** in an action, the launched process might start before the current transaction has been committed. This means that any changes that were made during the transaction that launched the process might not yet be visible in that process. For example, if you update an entity and then launch a process using **Launch&lt;Process Name&gt;** by passing that entity's id, that process might not yet see the updated values for that entity, as the transaction updating the entity might not have been committed yet.

</div>

## Input parameters

* **Process Input Parameters**: one parameter for each input parameter in the process definition.

<div class="warning" markdown="1">

The input parameters must be in the same order and of the same type as what is defined in the process.

</div>

<div class="info" markdown="1">

Text input parameters are limited to 2000 characters. See [performance best practices for data modeling](../../data/modeling/data-model-best-practices.md#isolate-large-text-and-binary-data).

</div>

## Output parameters

* **Id**: Identifier of the created process. The `Id` argument is of type Process Identifier.

See [how to access the output parameters](intro.md).
