---
guid: 46402d14-c102-4977-86f1-ce3475df2910
locale: en-us
summary: This article provides guidelines for refactoring the usage of BPT entities and actions in O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - full stack developers
  - frontend developers
  - mobile developers
tags: cloud-native applications,system entities,api development,data integration,platform version migration
outsystems-tools:
  - service studio
helpids: 30628
---

# Asset consuming O11 Business Process (BPT) elements

In ODC, business processes are available as [workflows](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/), which have a different architecture and may still have yet limited support when compared to [O11 BPTs](../../building-apps/processes/intro.md).

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to O11 BPTs. OutSystems is working on automating the migration capabilities to map existing O11 BPTs functionality to ODC Workflows.

</div>

This pattern isn't supported yet.

You can only proceed with the migration of ODC assets that don’t consume O11 BPT elements.

In the meantime, rethink how you can comply with the ODC architecture using [ODC workflows](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/) to implement your business processes.
