---
summary: Learn how to design polling of external systems using OutSystems 11 (O11) for efficient data synchronization and process continuation.
locale: en-us
guid: 4a3be3da-ce0d-4940-a534-60a2c22468cf
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=273:18
tags: external system integration, data synchronization, process automation, workflow implementation, sap integration
audience:
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - apply
  - evaluate
topic:
  - process-decision-patterns
---

# Designing Polling of External Systems

Use this pattern to poll an external system, that is, to periodically request data from an external system and take an action when some condition is met with the returned data.

## Example

As an example, think of an integration with SAP, where a process submits an invoice to the SAP system and has to wait for it to be approved in SAP before continuing.

![Diagram illustrating the process of polling an external system, such as submitting an invoice to SAP and waiting for approval](images/polling-external-systems.png "Polling External Systems Process Diagram")

When the process is executed the following occurs:

1. The [Automatic Activity](<../../../ref/lang/auto/class-automatic-activity.md>) submits the invoice to SAP.

2. The **Wait** activity holds the execution of the process.

3. When the timeout occurs, the **Wait** activity is tentatively ended by executing the **OnClose** callback action: it only ends when the invoice is ok, otherwise the waiting continues until the next timeout (one more day from the current date and time).
