---
summary: 
locale: en-us
guid: 0b89d709-a914-4f96-8869-3c653149576d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Assess app architecture and ODC readiness

After completing the [mapping of O11 to ODC architecture and adding the first version of your ODC architecture to the Migration Assessment Tool](plan-map-apps.md), you are ready to check the first assessment.

The app assessment helps you plan your migration to ODC, by supporting you with the following:

* Validate the ODC architecture.

* Understand and decide on what adjustment your team needs to do in O11, before migrating the apps to ODC.

## Validate the ODC architecture

1. After [mapping your ODC architecture](plan-map-apps.md), open the assessment by selecting **Open assessment**.

1. Filter the assessment by Architecture code patterns, in the **Categories** filter, select **Architecture**.

1. Select a **Code pattern**, and then select **Learn more** to understand the code pattern and how to solve it.

1. If the code pattern can only be solved by reviewing the architecture, check each **Finding** and do the necessary changes to adapt your architecture.

1. As you do the needed changes to solve each finding, re-check the Assessment, to ensure you resolved the issue. A new assessment runs every 10 minutes.

1. Repeat steps 3 to 5 for each code pattern that can only be solved by reviewing the architecture.

After these steps, you have validated your ODC architecture, and your team needs to solve the remaining code patterns and findings by refactoring apps.

## Prepare O11 app changes for ODC readiness

1. In the Assessment report, remove the **Categories** filter.

1. Check each code pattern, then decide how to solve each finding. This information is important for your development team, so they can estimate the refactoring effort and [prepare for the app migration](../prepare/prep-refactor-o11-apps.md).

<div class="info" markdown="1">

Make sure all O11 End Users have their email address field set. In **Users**, [set email addresses for all the End Users](../../user-management/end-user-manage/add-delete-users.md).
This is needed to unblock the migration to ODC, since in ODC Users must have an email address set.

</div>
