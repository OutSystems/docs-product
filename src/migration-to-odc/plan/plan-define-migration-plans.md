---
guid: ab447daa-dffc-4374-8ae6-986c8f3d63c4
locale: en-us
summary: Group small sets of apps using conversion plans based on your different app domains.
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2655-1045
coverage-type:
  - apply
  - understand
topic: 
app_type: mobile apps, reactive web apps
platform-version: o11
audience:
  - architects
  - platform administrators
  - tech leads
tags: app conversion, conversion process, conversion plans
outsystems-tools:
  - conversion assessment tool
  - app conversion kit
helpids: 
---

# Define conversion plans

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit.

</div>

The Conversion Assessment Tool enables you to plan the conversion of sets of apps based on your different app domains and your teams' development lifecycle.

After [mapping a set of O11 apps into ODC assets](plan-map-apps.md), you can group those ODC assets in conversion plans. With conversion plans, you can:

* Identify the dependencies between apps included in different conversion plans.

* Have different development teams focusing only on the [preparation of their own apps](../prepare/prep-intro.md)

![Diagram showing the Define conversion plans step in the conversion process.](images/prep-define-plans-diag.png "Define conversion plans")

<div class="info" markdown="1">

Your [LifeTime permissions for the Development environment](mat-permissions.md#plans) determine which conversion plan operations and ODC assets are available to you in the Conversion Assessment Tool.

</div>

## Create a conversion plan

To create a conversion plan, follow these steps:

1. Log into the Conversion Assessment Tool console (`https://<cat_console_environment>/ConversionAssessment`) using your IT User credentials.

1. In the **Conversion plans** tab, click **Create plan**.

1. Enter a **Name** for your conversion plan.

1. Select the **ODC assets** to include in the plan. 

    You can only select assets that aren’t included in other conversion plans yet.

1. Click **Save plan**.

After creating the conversion plan, you can validate if the assets in the plan [have dependencies](#dependencies) on assets in other plans.

![Conversion plan list in Conversion Assessment Tool.](images/migration-plan-list-at.png "Conversion plan list")

## Identify dependencies between apps { #dependencies }

In the **Conversion plans** list, you can identify the following:

* If an asset in the conversion plan has dependencies on producer or consumer assets that are not in the same plan. This helps you understand which plans must be converted first. For example, you must first convert the plans that don't have dependencies on producers or the producer's assets were already converted to ODC.

* If an asset has a [weak dependency](../../building-apps/reuse-and-refactor/strong-weak-dependencies.md#weak-dependencies) on a producer asset that is not in the same plan.

![Conversion plan details showing weak dependencies.](images/migration-plan-details-at.png "Conversion plan details")

To validate the dependencies of a conversion plan, follow these steps:

1. In the Conversion Assessment Tool console, go to the **Conversion plans** tab to view the list of plans already created.

1. Select a conversion plan from the list.

    The following details of the plan are displayed:

      * The number of assets.
      * The overall ODC readiness status of the assets.
      * The list of different plans including producer assets. Under **Unplanned**, you also find the producer assets not included in any plan yet.
      * The list of different plans including consumer assets. Under **Unplanned**, you also find the consumer assets not included in any plan yet.

1. Expand a plan in the list of **Producers** or **Consumers** to view the list of producer or consumer assets.

1. Select an asset from the list to open the **Dependency details**.

If you are validating an identified weak dependency on a producer asset in a different plan, you can decide to ignore the warning and manage the dependency after conversion. To do that, switch the **Resolve in ODC** toggle on.

![Dependency details with Resolve in ODC option.](images/migration-plan-dependency-details-at.png "Dependency details")

The **Resolve in ODC** option is only available when validating producer assets, and is not available when validating consumer assets.
