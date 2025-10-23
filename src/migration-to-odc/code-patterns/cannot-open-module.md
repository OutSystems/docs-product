---
summary: Recommendation to solve the issue where Conversion Assessment Tool can't open the module for analysis.
locale: en-us
guid: e7f28e4a-0568-4062-9a3a-3495e4dc212f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30554
coverage-type:
  - unblock
tags: conversion issues, module troubleshooting, error resolution, outsystems 11, service studio
audience:
  - platform administrators
  - tech leads
outsystems-tools:
  - service studio
  - service center
---

# Cannot open module

The Conversion Assessment Tool cannot access and analyze the module, which blocks its preparation for the conversion to ODC. This error can occur for several reasons, such as a corrupted module.

## How to solve

You must solve this pattern in O11 before proceeding with the code conversion to ODC.

### Solve in O11

1. Try opening the module in Service Studio.

1. If the module opens successfully, look for issues like errors or outdated references.

1. Fix the error and republish the module.

If you can't open the module in Service Studio:

Try publishing an earlier version of the module. In **Service Center** > **Factory** > **Modules** > search for module name > publish from the version list.

If this fails, contact the Early Access Program representatives to send it to OutSystems. OutSystems can then investigate the issue more closely.
