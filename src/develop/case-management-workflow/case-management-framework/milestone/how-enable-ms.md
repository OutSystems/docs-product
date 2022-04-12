---
tags: Case Management; Case Management framework; CMf;
summary: Learn how to enable milestones for a case defintion.
guid: f27173b5-6489-408e-8259-6d429d569cba
locale: en-us
---

# How to enable milestones

In the Case Management framework, a **milestone definition** represents a type of milestone which can be associated with case definitions.

Before using milestones in a case management app, you start by [enabling milestones for a case definition](#enable) in your app's configuration module and then by [creating the milestones definitions](#add).

## Enable milestones for a case definition { #enable }

Before you start make sure you [set up your app to work with the Case Management framework](../bootstrap-app.md).

To enable the use of milestone definitions with a case definition, you adapt the core services module for that case type by adding static entities to hold milestone definitions, and then adapting the setup timer that sets up your case.
Follow these steps:

1. In **&lt;business-entity&gt;_CS** module, go to the **Data** tab, create a **static entity**, and name it `MilestoneConfiguration`.

    <div class="info" markdown="1">

    The &lt;business-entity&gt;_CS module is the module that contains the case definition for which you want to use milestone definitions, where &lt;business-entity&gt; is the name of the business entity associated with that case definition.

    </div>

1. Ensure the **MilestoneConfiguration** static entity has the following attributes:

    * `MilestoneDefinitionId`, **Identifier** with **Text** data type and length of `36`. **Is Mandatory** set as **True**.
    * `Name`, with **Text** data type and length of `50`. **Is Mandatory** set as **True**.
    * `Description`, with **Text** data type and length of `200`.
    * `IsActive`, with **Boolean** data type.

1. In the **Logic** tab, open the **Bootstrap_CaseConfiguration** action flow, drag the **MilestoneConfiguration** static entity before the **Assign** to add an aggregate that fetches the milestone definitions.

1. In the **Assign** used to set the inputs the **SetupData**, set **SetupData.MilestoneDefinitionList** as `GetMilestoneconfigurations.List`, the output of the aggregate created in the previous step.

1. Set the mapping with the data from the aggregate:

    * Set **MilestoneDefinitionId** as `TextToIdentifier(MilestoneDefinitionId)`.
    * Set **Name** as `Name`.
    * Set **Description** as `Description`.
    * Set **IsActive** as `IsActive`.

1. Publish the module by selecting **1-Click Publish**.

After publishing these steps you are ready to start [adding milestone defintions](#add).

## Add milestone definitions { #add }

Before you start make sure you [enabled milestones for the case definition](#enable).

To add milestone definitions and associate them with a case definition, follow these steps:

1. In **&lt;business-entity&gt;_CS** module, add a record to the **MilestoneConfiguration** static entity.

    <div class="info" markdown="1">

    The &lt;business-entity&gt;_CS module is the module that contains the case definition for which you want to use milestone definitions, where &lt;business-entity&gt; is the name of the business entity associated with that case definition.

    </div>

1. Generate a GUID and paste that GUID into the value field of the **Id** attribute of the record.

    <div class="info" markdown="1">

    A Globally Unique IDentifier, or GUID, is used as a unique identifier to ensure integrity across environments.  
    You can use an online GUID generator to create a GUID for each record.

    Check the [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) for more information on GUIDs.

    </div>

1. Set the **Name** and **Description**.

1. Set **IsActive** as **True**.

1. For each milestone you want to add, repeat steps 1 to 4.

1. Publish the module by selecting **1-Click Publish**.

After publishing the module, the Bootstrap_CaseConfiguration timer runs, associating the milestone definitions with the case definition of the module.

After this, when Case_Initialize action is used to create new case instances of this case definition, a milestone instance is automatically created for each active and associated milestone definition.
