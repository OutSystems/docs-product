---
tags: Case Management; Case Management framework;
summary: Learn about case statuses and how to use case statuses with the Case Management framework.
guid: fc30b404-7533-4e75-9e88-392cf3f454b6
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# Case status

A case can go through several statuses during its lifecycle. For example, on creation a new case instance can start with the "Submitted" status, and depending on the manual task of the end user, it can change to the "Approved" status or to the "Rejected" status.

The Case Management framework lets you define a set of statuses associated with a case definition, and each case definition must have one initial status associated.

The case status set as initial is automatically assigned to a case upon the initialization of the case, unless another status is set using the non-mandatory **CaseStatusId** input field of the [Case_Initialize](ref/auto/CaseServices_API.final.md#Case_Initialize) action, from the CaseServices_API module.

<div class="info" markdown="1">

A case must be initialized with a case status, otherwise an exception is thrown.  
If there isn't a case status set as initial, you must set a CaseStatusId when you initialize a case.

</div>

After you [set up your app to work with the Case Management framework](bootstrap-app.md), the **CaseStatusConfiguration** static entity from &lt;business-entity&gt;_CS module, contains the case statuses for the case definition in that module.

## Define a case status

Before you start make sure you [set up your app to work with the Case Management framework](bootstrap-app.md).

To define a new case status follow these steps:

1. In the **&lt;business-entity&gt;_CS** module, add a `<state>` record to the **CaseStatusConfiguration** static entity. Replace &lt;state&gt; with the state of the case definition, for example, `Approved`.

1. Generate a GUID and paste that GUID into the value field of the **CaseStatusId** attribute of the **&lt;state&gt;** record.

    <div class="info" markdown="1">

    A Globally Unique IDentifier, or GUID, is used as a unique identifier to ensure integrity across environments.  
    You can use an online GUID generator to create a GUID for each record.

    Check the [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) for more information on GUIDs.

    </div>

1. Set the remaining attributes.

1. Publish the module by selecting **1-Click Publish**.

After these steps, the bootstrapping action loads the new case status and associates it with the case definition.

## Update the status of a case

To update the status of a case, use the [**Case_UpdateStatus**](ref/auto/CaseServices_API.final.md#Case_UpdateStatus) action from the **CaseServices_API** module.

A case status update is successful if the following conditions are met:

* The Case Identifier exists.

* The case status is valid for the given case.

* If you defined a state machine, the change between the previous state and the new status is valid for the case.
