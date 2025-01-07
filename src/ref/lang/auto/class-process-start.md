---
summary: Learn how to initiate and manage process flows in OutSystems 11 (O11) using the Process Start and Conditional Start activities.
locale: en-us
guid: 6f406b45-353d-49f7-b859-2d3b5e153240
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: process flows, outsystems, process start activity, conditional start activity, entity actions
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Process Start

When designing the process flow of your process, you must start the process flow with the **Process Start** activity which you can drag onto your canvas from the [Process Flow Toolbox](<../../../building-apps/processes/process-flow/process-flow-toolbox.md>). Only one Process Start activity is allowed in a process flow design as this is where the process flow execution starts when the process is launched.

However, when designing the process flow of your process, you can start specific flows in the process to handle [entity actions events](<../../processes/intro.md#entity-actions-events>) raised by your application.

## Starting Alternative Flows

Whenever an entity record is **created** or **updated** with an Entity Action you may use the [Conditional Start](<class-conditional-start.md>) process activity to start alternative flows to your normal process flow. A typical usage is to handle exceptions to the normal process flow.

### Example

When a process is using an entity record that, at some moment in time, is updated in the application and becomes invalid for the process; handle this in your process by adding a **Conditional Start** to start in the event of updating the entity record, and then design a flow to take an action in the process when the entity record is invalid.



