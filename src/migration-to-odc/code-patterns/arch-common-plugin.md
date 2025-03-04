---
helpids: 30555
summary: 
tags: 
guid: fda33fd0-371e-4252-b822-578aee484673
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: 
---

# Asset consuming a reference to the Common Plugin

In O11, most mobile plugins use the Common Plugin app. However, in ODC, mobile plugins are treated as libraries instead of apps. Due to architectural differences between O11 and ODC, it isn't possible to migrate O11 apps directly to ODC libraries. If you want to migrate a plugin from O11 to an ODC library, the plugin needs to be a library. 

## How to solve

You must solve this pattern in O11, before proceeding with the code migration to ODC.

### Solve in O11

When preparing your O11 mobile plugins to migrate to ODC, replace the app [Common Plugin](https://www.outsystems.com/forge/component-overview/1417/common-plugin-o11?_gl=1*as0iuv*_gcl_au*NzkwNzEzODg1LjE3MzQzMzc2MzM.*_ga*NzY1OTI2MjE3LjE2OTUwMjY5ODA.*_ga_ZD4DTMHWR2*MTc0MTA3ODk2OS4xNjUuMS4xNzQxMDg3NzU1LjU5LjAuMA..*_ga_HGKNZZMWJS*MTc0MTA4NzE0My40NTkuMS4xNzQxMDg3NzU1LjU5LjEuMTYyMDYzMzQwNg..*_ga_G11QMS1MBT*MTc0MTA4NzE0My4xMDUuMS4xNzQxMDg3NzU1LjAuMC4w) with the [Common Plugin Libary](https://www.outsystems.com/forge/component-overview/20521/common-plugin-library-o11?_gl=1*qnq6gw*_gcl_au*NzkwNzEzODg1LjE3MzQzMzc2MzM.*_ga*NzY1OTI2MjE3LjE2OTUwMjY5ODA.*_ga_ZD4DTMHWR2*MTc0MTA3ODk2OS4xNjUuMS4xNzQxMDg3Nzg4LjI2LjAuMA..*_ga_HGKNZZMWJS*MTc0MTA4NzE0My40NTkuMS4xNzQxMDg3Nzg4LjI2LjEuMTYyMDYzMzQwNg..*_ga_G11QMS1MBT*MTc0MTA4NzE0My4xMDUuMS4xNzQxMDg3Nzg4LjAuMC4w). Then, migrate your plugin to the ODC library. 
