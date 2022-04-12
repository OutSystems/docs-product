---
locale: en-us
guid: b710c30e-e103-430c-8646-2488f414a422
---

# Launch Process Action

Use the **Launch&lt;Process Name&gt;** [process extended action](intro.md) in an action flow to launch the execution of a **Process**. This process is **executed asynchronously**, that is, it is launched and executed independently from the action flow execution, which immediately steps to the next element in the flow.

## Input parameters

* **Process Input Parameters**: one parameter for each input parameter in the process definition.

<div class="warning" markdown="1">

The input parameters must be in the same order and of the same type as what is defined in the process.

</div>

## Output parameters

* **Id**: Identifier of the created process. The `Id` argument is of type Process Identifier.

See [how to access the output parameters](intro.md).
