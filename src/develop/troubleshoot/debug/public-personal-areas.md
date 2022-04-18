---
summary: Learn more about the two areas where modules can be executed and debugged.
locale: en-us
guid: 4c1e3298-79aa-4d28-83d1-36c9b4b27cd7
app_type: traditional web apps, mobile apps, reactive web apps
---

# Public and Personal Areas

A Traditional Web module can be executed and debugged in two different areas: the Public Area or the Personal Area.

<div class="info" markdown="1">

Reactive Web and Mobile modules are always published and debugged in the Public Area.

</div>

## Public Area

The **Public Area** is a common area of the environment where modules are published when using "1-Click Publish". This operation stores a new version of the module on the environment, allowing you to keep your module under version control. Shared services like Processes, Timers, and Emails are only executed in the Public Area.

When a developer publishes a module to the Public Area, all changes become public to other developers. For example, if you change a screen and publish the module to the Public Area, other developers executing the application will start using the screen with your changes. If they are working on the same module and publish their changes, they will merge their work with your changes.

## Personal Area

Each developer has an associated **Personal Area** to test changes to web application modules without affecting the work of other team members in the same modules.

When a developer publishes a module to their Personal Area they can test and debug changes privately, since the changes made to the module are not visible to other developers nor to consumer modules. For example, if you change a screen and publish the module to the Personal Area, none of the developers executing the application or working on the same module are affected by your changes.

You can publish a module to your Personal Area using the command "Run and Debug in *[user name]* Personal Area" from the Debugger menu. Besides publishing the module in your Personal Area, this command will also attach the debugger to both your Personal Area and the Public Area. This means that, from this moment on, you will be able to debug threads executing in both areas. When testing a module in the Personal Area, links to screens that are referenced from other modules automatically redirect to the Public Area.

You must publish a module in the Public Area at least once before publishing it to your Personal Area. We are removing some of these limitations, but currently changes to the following elements also require the module to be published to the Public Area to ensure the consistency between the Public and the Personal Areas:

* Entities
* Site Properties
* Session Variables
* Timers
* Roles
* Module references
