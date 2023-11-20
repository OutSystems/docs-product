---
tags: runtime-mobile; support-application_development; support-Application_Troubleshooting-featured; support-Mobile_Apps
locale: en-us
guid: ed285ef6-c4cc-4d6b-925a-fddb12c4205d
app_type: mobile apps
platform-version: o11
figma:
---

# Offline Data Sync Patterns

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

In this section you can find some common data synchronization patterns between the local storage (mobile device) and server database. The patterns are provided as samples you can use to create an implementation for your use case.

For each synchronization pattern, we provide a working sample module that you can use to explore the implementation of the synchronization mechanism. [Download an application from the Forge](http://www.outsystems.com/forge/component/1638/Offline+Data+Sync+Patterns/) that contains all sample modules.

We approach the following patterns:

* [Read-only data](read-only-data.md)
* [Read-only data optimized](read-only-data-optimized.md)
* [Read / write data last write wins](read-write-data-last-write-wins.md)
* [Read / write data with conflict detection](read-write-data-with-conflict-detection.md)
* [Read / write data one-to-many](read-write-data-one-to-many.md)
