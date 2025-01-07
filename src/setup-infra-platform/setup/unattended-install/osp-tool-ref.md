---
summary: Learn how to use the Solution Pack Tool (OSPTool) for publishing solutions in OutSystems 11 (O11) environments.
tags: command line tools, deployment automation, environment configuration, application publishing, devops
locale: en-us
guid: dee8f358-e76a-4277-af9f-c18bd1a05616
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
outsystems-tools:
  - none
coverage-type:
  - remember
---

# Solution Pack Tool Command Line Reference - OSPTool

<div class="info" markdown="1">

This article applies to: **OutSystems 11**&#8195;&#8195;Other versions available: [10](https://success.outsystems.com/Documentation/10/Setting_Up_OutSystems/Unattended_Installation_and_Upgrade/Solution_Pack_Tool_(OSPTool)_Command_Line_Reference)

</div>

The Solution Pack Tool (OSPTool) allows you to publish OutSystems solutions on an environment.

The default path of the Solution Pack Tool command line is the following:

```
C:\Program Files\Common Files\OutSystems\<version>\OSPTool.com
```

The Solution Pack Tool command line returns non-zero values when an error occurs.

## Syntax

```
OSPTool.com /Publish {<osp_file>|<oap_file>} <hostname> <username> <password>
    | /PublishFactory <hostname> <username> <password>
```

## Parameters

`/Publish {<osp_file>|<oap_file>} <hostname> <username> <password>`

:   Publishes the specified OutSystems Solution Pack (`.osp`) or OutSystems Application Pack (`.oap`) file.

`/PublishFactory <hostname> <username> <password>`

:   Publishes all non-system components in the Environment specified by hostname. This helps to apply patch updates.

## Example

Publish an OutSystems Solution Pack (`file.osp`) file:

```
OSPTool.com /Publish "file.osp" <hostname> <username> <password>
```

Publish an entire factory:

```
OSPTool.com /PublishFactory <hostname> <username> <password>
```
