---
tags: Case Management; Case Management framework;
summary: Learn about how you can set and enforce service level agreement (SLA) resolution or response times at the case level and activity level.
guid: e745cd81-f50a-483d-a08d-4279288fceae
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Ensuring resolution times with SLAs

With the Case Management framework, you can set and enforce service level agreement (SLA) resolution or response times at two levels. You can set and enforce SLA times with a case, or with a case's activity.

## SLA time for a case

Setting and enforcing an SLA time with a case definition means that an end user must close a case instance before a set amount of time, otherwise the app triggers an event.

You can set the start of the SLA time at the creation of a case instance or at the moment an end user picks up a case instance.

To enforce SLA time limits at the case level, you must also ensure an event is triggered when that SLA time limit runs out by setting the **GenerateEvent** input parameter as **True** in the **Case_AssociateProcess** action.

If the **OverrideMinutesForCompletion** parameter is set it overrides any previously configured SLA for that process and this value can be used to calculate the SLA. 

An option to use a [calendar](calendar.md) is also available with the **CalendarId** input parameter. Setting this input ensures the SLA calculation takes into account the working days, working hours, and holidays for that calendar.

### Set default SLA at case creation

You can set the default SLA time limit for each case definition adding it to every case instance.
To set up a default SLA time that starts counting when case instances are created, follow these steps:

1. In **&lt;business-entity&gt;_CS**, open  **Manage Dependencies**, and add **ProcessDefinitionSLA_CreateOrUpdate** action from the **CaseProcessConfigurations_API** producer.

1. In the **Data** tab, add a **Static Entity** named `ProcessSLAConfiguration` with the following attributes:

    * `Id` type text.
    * `ResponseTimeInMinutes` type integer.
    * `IsActive` type boolean.

1. Create a new **Record** in the static entity and set its **Identifier**. For example, if the SLA time is 5 days, set the **Identifier** as `SLAFiveDays`.

1. Generate a GUID and paste that GUID into the value field of the **Id** attribute of the record.

    <div class="info" markdown="1">

    A Globally Unique IDentifier, or GUID, is used as a unique identifier to ensure integrity across environments.  
    You can use an online GUID generator to create a GUID for each record.

    Check the [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) for more information on GUIDs and their format.

    </div>

1. Set the following attributes:

    * Set **ResponseTimeInMinutes** as the SLA time in minutes.
    * Set **IsActive** as **True**.

1. In the **Logic** tab, open the **Bootstrap_CaseConfigurations** action, and drag the **ProcessSLAConfiguration** static entity before the **End** of the action flow.

1. Set the aggregate's **Max. Records** as `1`.

1. Add a **ProcessDefinitionSLA_CreateOrUpdate** action after the aggregate.

1. Set the action's input record, **ProcessDefinitionSLARec**, as the output of the aggregate, `GetProcessSLAConfigurations.List.Current.ProcessSLAConfiguration`.

1. Set the following mappings:

    * **Id** = `TextToIdentifier(GetProcessSLAConfigurations.List.Current.ProcessSLAConfiguration.Id)`

    * **ProcessDefinitionId** = `GetCaseDefinitionData.List.Current.Process_Definition.Id`

    * **ResponseTimeInMinutes** = `GetProcessSLAConfigurations.List.Current.ProcessSLAConfiguration.ResponseTimeInMinutes`

    * **IsActive** = `GetProcessSLAConfigurations.List.Current.ProcessSLAConfiguration.IsActive`

1. Publish the module by selecting **1-Click Publish**.

After these steps the bootstrap timer runs adding th SLA time limit to the case definition.

### Act on an overdue case SLA

Before starting this procedure ensure the **GenerateEvent** input parameter as **True** in the **Case_AssociateProcess** action.
To act on overdue case SLA, follow these steps:

1. In **&lt;app-name&gt;_WF**, open  **Manage Dependencies**, and add  **ProcessEvent** and **ProcessEventType** entities from the **CM_ProcessEvent_CS** producer.

1. Open process associated with your case, drag a **Conditional Start** to the process flow, and name it `ProcessSLAOverdue`.

1. Set the following **Conditional Start** properties:

    * Set the **Start On** property as a **CreateProcessEvent** entity action.
    * Set the **ProcessId** input as the **ProcessId** runtime property.
    * Set the **ProcessEventTypeId** input as `SLAOverdue`.

1. Connect the conditional start to an **End** node.

1. Add the logic to deal with an overdue case between the **Conditional Start** and the **End**. For example, if you would like to complete your case if the SLA is overdue. You could achieve this by:

    1. Select the **Conditional Start**, and set **Terminate Process** property as **Yes**.

    1. Add an **Automatic Activity**.

    1. Inside the **Automatic Activity** add a **Case_Complete** and set the properties to close the case.

1. Publish the module by selecting **1-Click Publish**.
