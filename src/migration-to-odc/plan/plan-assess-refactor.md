---
summary: Assess your O11 app architecture and ODC readiness for conversion using the Conversion Assessment Tool.
locale: en-us
guid: 0b89d709-a914-4f96-8869-3c653149576d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2168-1376
tags: app conversion, odc architecture, platform updates, conversion process, architecture assessment
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - conversion assessment tool
coverage-type:
  - apply
---

# Assess app architecture and ODC readiness

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit.

</div>

After [mapping a set of O11 apps into ODC assets](plan-map-apps.md), the Conversion Assessment Tool automatically queues the assessment for those assets to run. A new assessment is also queued when there are application changes in the environment or when you choose to run a new assessment manually on the console.

When an analysis finishes, you can [go through the assessment report](#report) to assess the app architecture and ODC readiness for the mapped ODC assets.

![Diagram showing the Assess app architecture and ODC readiness step in the conversion process](images/prep-assess-app-arch-diag.png "Assess app architecture and ODC readiness")

The assessment report helps you plan your conversion to ODC, by supporting you with the following:

* Adjust the mapping of your O11 apps to ODC architecture.

* Understand and decide on what adjustments your team needs to make in O11 before migrating the apps to ODC. This information is important for your development team, so they can estimate the refactoring effort and [prepare for the app conversion](../prepare/prep-refactor-o11-apps.md).

<div class="info" markdown="1">

Your [LifeTime permissions for the Development environment](mat-permissions.md#assessment-findings) determine which assessment operations and findings are available to you in the Conversion Assessment Tool.

</div>

## View the assessment report { #report }

To view the assessment report of an [ODC asset already mapped from your O11 apps](plan-map-apps.md), follow these steps:

1. Log into the Conversion Assessment Tool console (`https://<cat_console_environment>/ConversionAssessment/`) using your IT User credentials.

1. Go to the **ODC Blueprint** tab.

1. Click on the ODC asset you want to assess to navigate to its assessment report.

If you already created [conversion plans](plan-define-migration-plans.md), follow these steps to view the assessment report of a specific plan:

1. In the Conversion Assessment Tool console, go to the **Assessment** tab.

1. Select the plan you want to assess from the **Conversion plans** filter.

![Screen showing an assessment report in the Conversion Assessment Tool.](images/assess-report-at.png "Assessment report in Conversion Assessment Tool")

## Validate findings { #validate-findings }

Go through the assessment report to validate its findings:

1. Select a pattern from the **Code**, **Data**, or **Infrastructure** patterns lists.

    The list of findings of that pattern displays on the right side. 

1. Select **Learn more** to access the code pattern documentation that guides you on how to solve it.

1. As you make the changes to solve each finding, rerun the assessment, to ensure you resolved the issue.

    If you don’t run a new assessment manually, the Conversion Assessment Tool automatically queues a new assessment to check for changes based on the defined [code assessment cycle](../setup-assessement-tool.md#cycles).

Repeat these steps for each pattern, assessing the refactoring effort to [prepare for the app conversion](../prepare/prep-refactor-o11-apps.md).
