---
summary: The automatic migration of O11 BPTs to ODC Workflows isn't yet supported.
locale: en-us
guid: a2ff3f16-e5b9-4ed0-ad63-341083e96101
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30526
tags: process automation, bpt, process migration, rest apis, outsystems upgrades
audience:
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---
# Asset consuming a Process

Currently, the Migration Kit doesn't support the automatic migration of O11 BPTs to [ODC Workflows](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to O11 BPTs. OutSystems is working on migration automation capabilities to map existing O11 BPTs to ODC Workflows.

</div>

If you have access to the Migration Kit, and want to unblock the migration of this ODC asset, you can consider the following:

* If you are doing a one-shot migration, replace the Process consumption with a placeholder Action. Once it's possible to automatically migrate O11 BPTs to ODC Workflows, you'll be able to migrate the missing Processes and BPT functionality.

* If you are doing an incremental migration, in the Producer app, create a REST Expose that wraps the Process. Then in the consuming asset replace the process consumption with a Consume REST that consumes the Process REST Expose.
