---
summary: Assess your O11 app architecture and ODC readiness for migration using the Migration Assessment Tool.
locale: en-us
guid: 0b89d709-a914-4f96-8869-3c653149576d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2168-1376
tags: application migration, odc architecture, platform updates, migration process, architecture assessment
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - migration assessment tool
coverage-type:
  - apply
---

# Assess app architecture and ODC readiness

<div class="info" markdown="1">

This article only applies to customers with access to the Migration Kit.

</div>

After [mapping a set of O11 apps into ODC assets](plan-map-apps.md), the Migration Assessment Tool automatically queues the assessment for those assets to run. A new assessment is also queued when there are application changes in the environment or when you choose to run a new assessment manually on the console.

When an analysis finishes, you can [go through the assessment report](#report) to assess the app architecture and ODC readiness for the mapped ODC assets.

![Diagram showing the Assess app architecture and ODC readiness step in the migration process](images/prep-assess-app-arch-diag.png "Assess app architecture and ODC readiness")

The assessment report helps you plan your migration to ODC, by supporting you with the following:

* [Adjust the mapping](#adjust-mapping) of your O11 apps to ODC architecture.

* Understand and decide on what adjustments your team needs to make in O11 before migrating the apps to ODC. This information is important for your development team, so they can estimate the refactoring effort and [prepare for the app migration](../prepare/prep-refactor-o11-apps.md).

## View the assessment report { #report }

To view the assessment report of an [ODC asset already mapped from your O11 apps](plan-map-apps.md), follow these steps:

1. Log into the Migration Assessment Tool console (`https://<mat_console_environment>/MigrationAssessment/`) using your IT User credentials.

1. Go to the **ODC Blueprint** tab.

1. Click on the ODC asset you want to assess to navigate to its assessment report.

If you already created [migration plans](plan-define-migration-plans.md), follow these steps to view the assessment report of a specific plan:

1. In the Migration Assessment Tool console, go to the **Assessment** tab.

1. Select the plan you want to assess from the **Migration plans** filter.

![Screen showing an assessment report in the Migration Assessment Tool.](images/assess-report-at.png "Assessment report in Migration Assessment Tool")

Then, go through the assessment report to validate its findings:

1. Select a pattern from the **Code Patterns** list.

    The list of findings of that pattern displays on the right side. 

1. Select **Learn more** to access the code pattern documentation that guides you on how to solve it.

## Adjust the mapping of O11 apps to ODC architecture { #adjust-mapping }

The assessment report helps you validate if the [mapping of your O11 apps into ODC assets](plan-map-apps.md) is compatible with ODC architecture by identifying **Architecture** code patterns that you can adjust in your mapping.

To validate the mapping of your O11 apps to ODC architecture, follow these steps:

1. In the **Category** filter, select **Architecture**.

    The architecture patterns and findings are displayed.

1. Select a pattern from the **Code Patterns** list.

1. Select **Learn more** to understand the code pattern and how to solve it.

1. If the code pattern can only be solved by adjusting the [mapping into ODC architecture](plan-map-apps.md), make the necessary changes for each **Finding**.

1. As you make the changes to solve each finding, rerun the assessment, to ensure you resolved the issue.

    If you don’t run a new assessment manually, the Migration Assessment Tool automatically queues a new assessment every 15 minutes to check for changes.

1. Repeat steps 2 to 5 for each code pattern that can only be solved by adjusting your mapping to ODC architecture.

After ensuring the mapping of your O11 apps is compatible with ODC architecture, clean up the **Category** filter to focus on the findings for the remaining categories and assess the refactoring effort to [prepare for the app migration](../prepare/prep-refactor-o11-apps.md).
