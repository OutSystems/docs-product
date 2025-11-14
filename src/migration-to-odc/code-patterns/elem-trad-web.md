---
guid: e0247801-d291-4da0-8a7a-f20098ade92b
locale: en-us
summary: This article provides guidelines for handling Traditional Web modules before converting O11 apps to OutSystems Developer Cloud (ODC).
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2993-53
coverage-type: 
  - unblock
topic: 
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
audience: 
  - frontend developers
  - full stack developers
  - tech leads
tags: reactive web apps, module conversion, conversion guide, outsystems 11, traditional web apps
outsystems-tools: 
  - service studio
helpids: 
---

# Asset cannot contain Traditional Web modules

In ODC, all Web apps are reactive. Traditional Web apps aren't supported. This means that if your ODC asset is mapped to one or more O11 apps that include Traditional Web modules, you must convert these modules to Reactive Web modules.

## How to solve

You must solve this pattern in O11 before proceeding with the code conversion to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* Traditional Web modules that only contain logic can be [converted to Service modules](../../building-apps/reuse-and-refactor/convert-to-service.md) as follows:

    1. In Service Studio, open the module you want to convert.

    1. Convert the Traditional Web module to a Service module.

        ![Screenshot in Service Studio on how to convert a Traditional module to a service module](images/trad-web-module-convert-service-ss.png "How to convert a Traditional module to a service module")

* For Traditional Web modules that contain UI elements, the entire module must be converted into a Reactive Web module. For more information on how to do this, refer to [Introduction to migrating Traditional Web to Reactive Web Apps](https://www.outsystems.com/tk/redirect?g=6fd52b69-653d-4384-b9fe-7e30b698609b).
