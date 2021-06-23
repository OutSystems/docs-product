---
summary: Frequently asked questions about modules of the same app on different deployment zones and the changes introduced in Platform Server 11.8.0.
---

# Modules and apps in deployment zones
From the release of Platform Server 11.8.0 only complete applications can be configured for different deployment zones. Mixed-mode configurations—different deployment zones for individual modules of the same app—is deprecated. 

<div class="info" markdown="1">

While existing applications with modules in different deployment zones are still supported, OutSystems will stop supporting this option in the future. At that time mixed-mode applications must be refactored and reorganized to meet this restriction.

</div>

**After upgrading the Platform Server what will be the behavior of my apps with modules configured for different modes?**
 
Nothing changes. Mixed-mode apps will keep their current configurations untouched at the module level.

**Can modules in a mixed-mode scenario be changed?**

Modules in mixed-mode scenarios can be changed, just as any other module. All module-level operations are still available. They can also be moved to other deployment zones.

**Can new modules be added to mixed-mode apps?**

New modules can be added to mixed-mode apps. New modules will be created on the [default deployment zone](intro.md) for that environment. Just like other modules in a mixed-mode application, they can be changed to another deployment zone.

**What about new apps?**

It will not be possible to define mixed-mode scenarios for new apps. The configuration of deployment zones for new apps applies only to the whole app.

**What happens if we configure a deployment zone for an application with modules in different deployment zones?**

The deployment zone configurations at module level will be deleted and the application-level configuration will be used.
