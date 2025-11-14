---
summary: This article explains that O11 modules containing Business Process Technology (BPT) cannot be converted to ODC and advises on how to proceed.
locale: en-us
guid: 53396f3a-ec98-4870-adb5-47dc8c52e8ea
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30539
tags: bpt, workflow automation, conversion, outsystems 11, outsystems platform
audience:
  - full stack developers
  - architects
outsystems-tools:
  - service studio
  - conversion assessment tool
coverage-type:
  - unblock
  - understand
---

# The Asset cannot contain BPTs

Business Process Technology (BPT) enables you to define and execute business processes within the applications. [BPT processes](https://success.outsystems.com/documentation/11/developing_an_application/use_processes_bpt/) are sequences of activities that build the workflow of a process, which is executed in the background. BPT is useful for implementing workflows that involve system-to-system or human-to-system interactions, and it allows for activities to run in parallel, providing flexibility in how business processes are managed and executed.

## How to solve

<div class="info" markdown="1">

If you are only preparing your code for the conversion, at present, OutSystems recommends not making any changes to O11 BPTs. OutSystems is working on conversion automation capabilities to map existing O11 BPTs to ODC Workflows.

</div>

This pattern isn't supported yet.

If you have access to the [O11 to ODC App Conversion Kit EAP](https://www.outsystems.com/o11-odc-migration/), and want to proceed with the conversion of other ODC assets without BPT, ensure the O11 modules with findings for this code pattern aren't mapped to any ODC Assets.
