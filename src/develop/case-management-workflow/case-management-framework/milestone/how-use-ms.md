---
tags: Case Management; Case Management framework; CMf;
summary: Learn how to use milestone instances in your case management app.
guid: 34bb2be4-ccf7-4cff-81ee-b517dc31f5d0
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to use milestones

In the Case Management framework, a **milestone instance** is a specific occurrence of a milestone definition in the context of a case instance.

Learn how to use milestone instances in your case management app, in the following sections.

## Fetch milestones for a case

Fetch milestone instances for a given case instance using the [Case_GetMilestones](../ref/auto/CaseServices_API.final.md#Service_Case_GetMilestones) action from the CaseServices_API module.

## Set a milestone as achieved

To set a milestone instance as achieved use the [Milestone_SetAchieved](../ref/auto/CaseServices_API.final.md#Milestone_SetAchieved) action from the CaseServices_API.

For example, to automatically update the achievement status of a milestone once a Human Activity is completed in your workflow, use the **Milestone_SetAchieved** action in the **On Close** callback action flow of that activity to set the milestone instance as achieved.

You can also set a milestone instance back as unachieved using the [Milestone_SetUnachieved](../ref/auto/CaseServices_API.final.md#Milestone_SetUnachieved) from the CaseServices_API.

## Check milestone status

Check the achievement status of a milestone using the [Case_IsMilestoneAchieved](../ref/auto/CaseServices_API.final.md#Case_IsMilestoneAchieved) action from the CaseServices_API module. For a given **CaseId** and **MilestoneDefinitionId** input parameter pair this action returns a boolean **IsAchieved** output parameter that indicates whether the milestone instance has been achieved or not.
