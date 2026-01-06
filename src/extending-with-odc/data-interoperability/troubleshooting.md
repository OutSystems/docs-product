---
guid: b8bedc84-3aed-47e6-a6f7-f610c3741fed
locale: en-us
summary: Learn how to solve some common issues with data interoperability between ODC and O11.
figma: https://www.figma.com/design/epaiN2jasbbKgJA0iSYfZn/Extending-with-ODC?node-id=2637-905
coverage-type:
  - unblock
topic: 
app_type: mobile apps,reactive web apps,traditional web apps
platform-version: o11
audience:
  - infrastructure managers
  - platform administrators
  - tech leads
tags: entities,data interoperability,troubleshooting
outsystems-tools:
  - lifetime
  - odc portal
helpids: 30651
---

# Troubleshooting data interoperability issues

This page describes some common issues you may encounter when using data interoperability between ODC and O11, and how to solve them.

## Missing prerequisites in OutSystems 11 database connection {#missing-prerequisites}

You get the error **Missing prerequisites** when opening the details of an OutSystems 11 connection in **ODC Portal > INTEGRATE > Connections**.

![Missing prerequisites error in OutSystems 11 connection](images/troubleshooting-missing-prerequisites-pl.png "Missing prerequisites error in OutSystems 11 connection")

This can happen in the following situations:

* The setup of your OutSystems 11 infrastructure is not supported for data interoperability.

* The version of LifeTime or Platform Server in your O11 environments is not supported for data interoperability.

* The connection from ODC to your O11 infrastructure is not correctly configured.

### Recommended action

Make sure:

* Your O11 infrastructure follow the [prerequisites for data interoperability](intro.md#prerequisites).

* The connection from your ODC tenant to the O11 infrastructure is correctly configured. See [Connect ODC to your O11 infrastructure](configure-connection.md#connect-o11-infrastructure) for further details.

## Error exposing entities in LifeTime

You get the error **Platform server version requirement** when accessing **Applications > Expose Entities** in the O11 LifeTime console.

![Platform server version requirement error in LifeTime Expose Entities](images/troubleshooting-baseline-version-lt.png "Platform server version requirement error in LifeTime Expose Entities")

This happens because the Platform Server version of your O11 environments is not supported for data interoperability.

### Recommended action

To start [exposing your O11 entities to ODC](expose-entities.md), make sure the Platform Server version of your O11 environments is **11.40.0 or later**. See the [prerequisites for data interoperability](intro.md#prerequisites) for further details.

## Expose entities screen showing only the baseline environment

When accessing **Applications > Expose Entities** in the O11 LifeTime console, you see the [baseline environment](expose-entities.md#configure-baseline) but the remaining environments of the pipeline are missing.

![Missing environments in LifeTime Expose Entities](images/troubleshooting-missing-environments-lt.png "Missing environments in LifeTime Expose Entities")

This happens because the Platform Server version of the remaining O11 environments in your pipeline is not supported for data interoperability.

### Recommended action

Make sure the Platform Server version of all your O11 environments is **11.40.0 or later**. See the [prerequisites for data interoperability](intro.md#prerequisites) for further details.
