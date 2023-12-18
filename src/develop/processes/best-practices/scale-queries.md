---
summary: The article provides a solution for scaling queries over process entities in OutSystems by creating a custom entity to store necessary runtime information
locale: en-us
guid: c50b149e-e4f0-4399-a941-b5e2a9bd86d5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---
# Scale Queries over Process Entities

When designing functionality that queries runtime information of [Processes](../intro.md), it is normally done through [Process Entities](../process-entities/intro.md).

![Diagram showing how each process entity provides a part of the overall process runtime information in OutSystems.](images/scale-queries-1.png "Process Entity Runtime Information")

Each process entity makes available part of the whole process runtime information stored by OutSystems. As such, if the number of executing process instances grows to millions of records, queries over process entities will be slow.

In this case, we recommend that you do the following:

1. Create an **Entity** to manually store runtime information you need about the process. This entity should be called **&lt;ProcessName&gt;Process**.

1. Use a [Process Callback Action](../actions-callback/actions-callback.md) or an [Activity Callback Action](../actions-callback/actions-activities-callback.md) to add logic to manually store the needed runtime information.

By creating this entity, you may also extend the logic and **store other runtime information** you need.

## Example

As an example, imagine a process to pay invoices of suppliers: the invoice has to pass a first level of approval, then a possible second level of approval (depending on the amount to pay), and, if rejected on any approval, an e-mail is sent to notify the supplier.

![Flowchart of the invoice approval process with two levels of approval and a notification step for rejections.](images/scale-queries-2.png "Invoice Approval Process")

There is a requirement to make a report with the time it takes to make the first approval and also the possible second approval. There are thousands of invoices to pay, therefore, we should not use the process entity.

Let's disable the process entity...

![Illustration of the action to disable the process entity in OutSystems.](images/scale-queries-3.png "Disabling Process Entity")

...and create an **InvoiceProcess** entity to store the date and time of: invoice creation, first approval, and second approval.

![Entity diagram for InvoiceProcess with attributes for invoice creation, first approval, and second approval dates.](images/scale-queries-4.png "InvoiceProcess Entity Structure")

Now, use the callback actions to fill the new entity with values for their attributes:

![Example of using callback actions to populate the InvoiceProcess entity with runtime information.](images/scale-queries-5.png "Callback Actions Implementation")

1. Add a **On Process Start** callback action to the process to create a **InvoiceProcess** record with the invoice identifier and its creation date and time.

2. On the **Level1Approval** human activity, add a **On Close** callback action to update the **InvoiceProcess** record with the first approval date and time.

3. On the **Level2Approval** human activity, add a **On Close** callback action to update the **InvoiceProcess** record with the second approval date and time.
