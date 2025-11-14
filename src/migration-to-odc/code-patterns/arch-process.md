---
summary: The automatic conversion of O11 BPTs to ODC Workflows isn't yet supported.
locale: en-us
guid: a2ff3f16-e5b9-4ed0-ad63-341083e96101
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30526
tags: process automation, bpt, process conversion, rest apis, outsystems upgrades
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

In ODC, business processes are available as [workflows](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/), which have a different architecture and may still have limited support when compared to [O11 BPTs](../../building-apps/processes/intro.md).

Thus, currently, ODC Assets can't consume Processes.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

<div class="info" markdown="1">

If you are only preparing your code for the conversion, at present, OutSystems recommends not making any changes to O11 BPTs. OutSystems is working on conversion automation capabilities to map existing O11 BPTs to ODC Workflows.

</div>

If you have access to the [O11 to ODC App Conversion Kit EAP](https://www.outsystems.com/o11-odc-migration/), and want to unblock the conversion of this ODC asset, you can consider one of the following:

* Replace the Process consumption with a placeholder Action. Once it's possible to automatically convert O11 BPTs to ODC Workflows, you'll be able to convert the missing Processes and BPT functionality.

* In the Producer app, create a REST Expose that wraps the Process. Then, in the consumer asset, replace the Process consumption with a Consume REST that consumes the Process REST Expose.
