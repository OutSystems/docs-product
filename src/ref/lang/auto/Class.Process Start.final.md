---
kinds: ServiceStudio.Model.Nodes+Start+Kind, ServiceStudio.Model.ProcessNodes+Start+Kind
helpids: 0
---

# Process Start

When designing the process flow of your process, you must start the process flow with the **Process Start** activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../develop/processes/process-flow/process-flow-toolbox.md>). Only one Process Start activity is allowed in a process flow design as this is where the process flow execution starts when the process is launched.

However, when designing the process flow of your process, you can start specific flows in the process to handle [entity actions events](<../../../develop/processes/intro.md#entity-actions-events>) raised by your application.

## Starting Alternative Flows

Whenever an entity record is **created** or **updated** with an Entity Action you may use the [Conditional Start](<Class.Conditional Start.final.md>) process activity to start alternative flows to your normal process flow. A typical usage is to handle exceptions to the normal process flow.

### Example

When a process is using an entity record that, at some moment in time, is updated in the application and becomes invalid for the process; handle this in your process by adding a **Conditional Start** to start in the event of updating the entity record, and then design a flow to take an action in the process when the entity record is invalid.



