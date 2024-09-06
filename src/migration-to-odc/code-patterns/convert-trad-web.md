---
summary: 
tags: 
guid: 5599ed1d-6b0e-4862-9fe5-0603ab025fa5
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?node-id=2318-2
helpids: 30549
---

# Asset consuming a reference to a Traditional Web element

In ODC, all Web apps are reactive. Traditional Web apps aren't supported. This means that if your app/module is consuming a dependency from a Traditional Web app/module, you must convert it to a Reactive Web app/module 

## How to solve

You must solve this pattern in O11 before proceeding with the code migration to ODC.

### **Solve in O11**

Depending on your scenario, solve this pattern in one of the following ways:

* Traditional web app modules that only contain logic can be converted to Service or Library modules as follows:

    1. In Service Studio, open the module you want to convert.

    1. Convert the Traditional Web app module to a Service or Library module.

        ![Screenshot in Service Studio on how to convert a module to a service or library module](images/convert-service-module-lib-ss.png "How to convert a module to a service or library module")

    1. Move the Service module to a Reactive Web app in Service Studio.

    1. Map your module to an ODC asset.

* For Traditional Web app modules that contain UI elements, the entire module must be converted into a Reactive Web module. For more information on how to do this, refer to  [Introduction to migrating Traditional Web to Reactive Web Apps](https://success.outsystems.com/documentation/how_to_guides/development/introduction_to_migrating_traditional_web_to_reactive_web_apps/)
