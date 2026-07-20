---
helpids: 30555
summary: This article explains how to resolve the Common Plugin dependency in O11 by replacing it with the Common Plugin Library before converting mobile plugins to ODC.
tags: common plugin, mobile plugins, app conversion, o11 to odc, dependency management
guid: fda33fd0-371e-4252-b822-578aee484673
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma:
audience:
  - Developer
  - Architect
  - Tech lead
coverage-type:
  - apply
  - unblock
outsystems-tools:
  - forge
isautopublish: true
---

# Asset consuming a reference to the Common plugin

In O11, most mobile plugins use the Common Plugin app. However, in ODC, mobile plugins are treated as libraries instead of apps. Due to architectural differences between O11 and ODC, it isn't possible to convert O11 apps directly to ODC libraries. If you want to convert a plugin from O11 to an ODC library, the plugin needs to be a library.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

When preparing your O11 mobile plugins to convert to ODC, replace the app [Common Plugin](https://www.outsystems.com/forge/component-overview/1417/common-plugin-o11) with the [Common Plugin Libary](https://www.outsystems.com/forge/component-overview/20521/common-plugin-library-o11). Then, convert your plugin to the ODC library.
